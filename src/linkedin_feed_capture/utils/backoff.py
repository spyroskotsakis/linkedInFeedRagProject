"""
Retry and backoff utilities for handling transient failures.

Provides exponential backoff, jitter, and configurable retry mechanisms
for handling network failures, rate limits, and other transient errors.
"""

import random
import time
from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, Optional, Tuple, Type, Union

from linkedin_feed_capture.utils.logger import get_logger

logger = get_logger(__name__)


class RetryableError(Exception):
    """Base exception for errors that should trigger retries."""
    pass


class RateLimitError(RetryableError):
    """Error for when we hit rate limits."""
    pass


class TemporaryNetworkError(RetryableError):
    """Error for temporary network issues."""
    pass


class AntiDetectionError(RetryableError):
    """Error for when anti-detection measures are triggered."""
    pass


@dataclass
class RetryConfig:
    """Configuration for retry behavior."""
    
    max_retries: int = 5
    base_delay: float = 1.0
    max_delay: float = 60.0
    backoff_multiplier: float = 2.0
    jitter: bool = True
    jitter_range: Tuple[float, float] = (0.0, 1.0)
    retryable_exceptions: Tuple[Type[Exception], ...] = (
        RetryableError,
        ConnectionError,
        TimeoutError,
    )


def exponential_backoff(
    attempt: int,
    base_delay: float = 1.0,
    backoff_multiplier: float = 2.0,
    max_delay: float = 60.0,
    jitter: bool = True,
    jitter_range: Tuple[float, float] = (0.0, 1.0),
) -> float:
    """
    Calculate exponential backoff delay with optional jitter.
    
    Args:
        attempt: Current attempt number (0-indexed)
        base_delay: Base delay in seconds
        backoff_multiplier: Multiplier for exponential backoff
        max_delay: Maximum delay in seconds
        jitter: Whether to add random jitter
        jitter_range: Range for jitter (min, max) as fraction of delay
        
    Returns:
        Delay in seconds
    """
    # Calculate exponential delay
    delay = min(base_delay * (backoff_multiplier ** attempt), max_delay)
    
    # Add jitter if enabled
    if jitter:
        jitter_min, jitter_max = jitter_range
        jitter_amount = delay * random.uniform(jitter_min, jitter_max)
        delay += jitter_amount
    
    return delay


def with_retries(
    config: Optional[RetryConfig] = None,
    on_retry: Optional[Callable[[int, Exception], None]] = None,
) -> Callable:
    """
    Decorator to add retry logic to functions.
    
    Args:
        config: Retry configuration
        on_retry: Callback function called on each retry
        
    Returns:
        Decorated function with retry logic
    """
    if config is None:
        config = RetryConfig()
    
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            
            for attempt in range(config.max_retries + 1):
                try:
                    return func(*args, **kwargs)
                    
                except config.retryable_exceptions as e:
                    last_exception = e
                    
                    if attempt == config.max_retries:
                        logger.error(
                            "Function failed after all retries",
                            function=func.__name__,
                            attempts=attempt + 1,
                            error=str(e),
                            error_type=type(e).__name__,
                        )
                        raise
                    
                    # Calculate delay
                    delay = exponential_backoff(
                        attempt=attempt,
                        base_delay=config.base_delay,
                        backoff_multiplier=config.backoff_multiplier,
                        max_delay=config.max_delay,
                        jitter=config.jitter,
                        jitter_range=config.jitter_range,
                    )
                    
                    logger.warning(
                        "Function failed, retrying",
                        function=func.__name__,
                        attempt=attempt + 1,
                        max_attempts=config.max_retries + 1,
                        error=str(e),
                        error_type=type(e).__name__,
                        retry_delay=round(delay, 2),
                    )
                    
                    # Call retry callback if provided
                    if on_retry:
                        on_retry(attempt, e)
                    
                    # Wait before retry
                    time.sleep(delay)
                    
                except Exception as e:
                    # Non-retryable exception
                    logger.error(
                        "Function failed with non-retryable error",
                        function=func.__name__,
                        error=str(e),
                        error_type=type(e).__name__,
                    )
                    raise
            
            # This should never be reached, but just in case
            raise last_exception or RuntimeError("Unexpected retry loop exit")
        
        return wrapper
    return decorator


class RetryManager:
    """
    Context manager for retry logic with more control.
    
    Example:
        retry_manager = RetryManager(max_retries=3)
        
        for attempt in retry_manager:
            try:
                result = risky_operation()
                break
            except RetryableError as e:
                retry_manager.record_failure(e)
                if not retry_manager.should_retry():
                    raise
    """
    
    def __init__(self, config: Optional[RetryConfig] = None):
        self.config = config or RetryConfig()
        self.attempt = 0
        self.last_exception: Optional[Exception] = None
        
    def __iter__(self):
        return self
        
    def __next__(self) -> int:
        if self.attempt > self.config.max_retries:
            raise StopIteration
            
        current_attempt = self.attempt
        self.attempt += 1
        return current_attempt
    
    def record_failure(self, exception: Exception) -> None:
        """Record a failure for this attempt."""
        self.last_exception = exception
        
        if self.attempt <= self.config.max_retries:
            delay = exponential_backoff(
                attempt=self.attempt - 1,
                base_delay=self.config.base_delay,
                backoff_multiplier=self.config.backoff_multiplier,
                max_delay=self.config.max_delay,
                jitter=self.config.jitter,
                jitter_range=self.config.jitter_range,
            )
            
            logger.warning(
                "Retry manager recorded failure",
                attempt=self.attempt,
                max_attempts=self.config.max_retries + 1,
                error=str(exception),
                error_type=type(exception).__name__,
                retry_delay=round(delay, 2),
            )
            
            time.sleep(delay)
    
    def should_retry(self) -> bool:
        """Check if we should continue retrying."""
        if self.last_exception is None:
            return False
            
        if self.attempt > self.config.max_retries:
            return False
            
        return isinstance(self.last_exception, self.config.retryable_exceptions)


def smart_delay(
    base_delay: float = 2.0,
    request_count: int = 0,
    recent_errors: int = 0,
    success_rate: float = 1.0,
) -> float:
    """
    Calculate smart delay based on current performance metrics.
    
    This function adapts delay based on:
    - Recent error count (more errors = longer delay)
    - Success rate (lower success rate = longer delay) 
    - Request count (implements basic rate limiting)
    
    Args:
        base_delay: Base delay in seconds
        request_count: Number of recent requests
        recent_errors: Number of recent errors
        success_rate: Success rate (0.0 to 1.0)
        
    Returns:
        Calculated delay in seconds
    """
    # Base delay
    delay = base_delay
    
    # Increase delay based on recent errors
    error_multiplier = 1 + (recent_errors * 0.5)
    delay *= error_multiplier
    
    # Increase delay based on low success rate
    if success_rate < 0.8:
        success_multiplier = 2.0 - success_rate  # Range: 1.2 to 2.0
        delay *= success_multiplier
    
    # Rate limiting based on request count
    if request_count > 50:
        rate_multiplier = 1 + ((request_count - 50) * 0.1)
        delay *= rate_multiplier
    
    # Add jitter
    jitter = random.uniform(0.8, 1.2)
    delay *= jitter
    
    # Cap maximum delay
    delay = min(delay, 30.0)
    
    return delay


def circuit_breaker(
    failure_threshold: int = 5,
    recovery_timeout: float = 60.0,
    expected_exception: Type[Exception] = Exception,
) -> Callable:
    """
    Circuit breaker decorator to prevent cascading failures.
    
    Args:
        failure_threshold: Number of failures before opening circuit
        recovery_timeout: Time to wait before trying to close circuit
        expected_exception: Exception type that triggers circuit breaker
        
    Returns:
        Decorated function with circuit breaker logic
    """
    def decorator(func: Callable) -> Callable:
        func._circuit_failures = 0
        func._circuit_last_failure_time = 0
        func._circuit_state = "closed"  # closed, open, half-open
        
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            now = time.time()
            
            # Check if circuit should transition from open to half-open
            if (func._circuit_state == "open" and 
                now - func._circuit_last_failure_time > recovery_timeout):
                func._circuit_state = "half-open"
                logger.info(
                    "Circuit breaker transitioning to half-open",
                    function=func.__name__,
                )
            
            # Reject calls if circuit is open
            if func._circuit_state == "open":
                raise RuntimeError(
                    f"Circuit breaker is open for {func.__name__}. "
                    f"Try again in {recovery_timeout - (now - func._circuit_last_failure_time):.1f}s"
                )
            
            try:
                result = func(*args, **kwargs)
                
                # Reset on success
                if func._circuit_failures > 0:
                    logger.info(
                        "Circuit breaker reset after success",
                        function=func.__name__,
                        previous_failures=func._circuit_failures,
                    )
                    func._circuit_failures = 0
                    func._circuit_state = "closed"
                
                return result
                
            except expected_exception as e:
                func._circuit_failures += 1
                func._circuit_last_failure_time = now
                
                if func._circuit_failures >= failure_threshold:
                    func._circuit_state = "open"
                    logger.error(
                        "Circuit breaker opened due to failures",
                        function=func.__name__,
                        failure_count=func._circuit_failures,
                        recovery_timeout=recovery_timeout,
                    )
                
                raise
        
        return wrapper
    return decorator 