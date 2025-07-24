"""
Unit tests for utility modules.

Tests logging configuration, backoff mechanisms, and retry logic.
"""

import time
import tempfile
from pathlib import Path
import pytest
from unittest.mock import Mock, patch

from linkedin_feed_capture.utils.logger import (
    setup_logging, 
    get_logger, 
    _parse_size_string,
    LoggerMixin
)
from linkedin_feed_capture.utils.backoff import (
    exponential_backoff,
    with_retries,
    RetryConfig,
    RetryableError,
    RateLimitError,
    smart_delay,
    circuit_breaker
)


class TestLogger:
    """Test cases for logger utilities."""
    
    def test_parse_size_string(self):
        """Test size string parsing."""
        assert _parse_size_string("100B") == 100
        assert _parse_size_string("1KB") == 1024
        assert _parse_size_string("1MB") == 1024 * 1024
        assert _parse_size_string("1GB") == 1024 * 1024 * 1024
        assert _parse_size_string("5.5MB") == int(5.5 * 1024 * 1024)
    
    def test_parse_size_string_invalid(self):
        """Test invalid size string handling."""
        with pytest.raises(ValueError):
            _parse_size_string("invalid")
        
        with pytest.raises(ValueError):
            _parse_size_string("100XB")
    
    def test_get_logger(self):
        """Test logger creation."""
        logger = get_logger("test_module")
        assert logger is not None
        assert hasattr(logger, 'info')
        assert hasattr(logger, 'error')
        assert hasattr(logger, 'debug')
    
    def test_logger_mixin(self):
        """Test LoggerMixin functionality."""
        class TestClass(LoggerMixin):
            pass
        
        instance = TestClass()
        assert hasattr(instance, 'logger')
        assert instance.logger is not None
    
    def test_setup_logging_basic(self):
        """Test basic logging setup."""
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "test.log"
            
            setup_logging(
                log_level="INFO",
                log_format="console",
                log_file_path=str(log_file),
                enable_console=False
            )
            
            # Test that we can get a logger and it works
            logger = get_logger("test")
            logger.info("Test message")
            
            # Log file should be created
            assert log_file.exists()


class TestBackoff:
    """Test cases for backoff and retry utilities."""
    
    def test_exponential_backoff_basic(self):
        """Test basic exponential backoff calculation."""
        # Test increasing delays
        delay0 = exponential_backoff(0, base_delay=1.0, backoff_multiplier=2.0, jitter=False)
        delay1 = exponential_backoff(1, base_delay=1.0, backoff_multiplier=2.0, jitter=False)
        delay2 = exponential_backoff(2, base_delay=1.0, backoff_multiplier=2.0, jitter=False)
        
        assert delay0 == 1.0
        assert delay1 == 2.0
        assert delay2 == 4.0
    
    def test_exponential_backoff_max_delay(self):
        """Test max delay cap."""
        delay = exponential_backoff(10, base_delay=1.0, backoff_multiplier=2.0, max_delay=5.0, jitter=False)
        assert delay == 5.0
    
    def test_exponential_backoff_with_jitter(self):
        """Test jitter functionality."""
        delay1 = exponential_backoff(1, jitter=True, jitter_range=(0.1, 0.2))
        delay2 = exponential_backoff(1, jitter=True, jitter_range=(0.1, 0.2))
        
        # With jitter, delays should be different
        # Note: This test could occasionally fail due to randomness, but probability is low
        base_delay = 2.0  # Default for attempt 1
        assert base_delay < delay1 < base_delay * 1.3  # Should be within jitter range
        assert base_delay < delay2 < base_delay * 1.3
    
    def test_retry_config_defaults(self):
        """Test RetryConfig default values."""
        config = RetryConfig()
        
        assert config.max_retries == 5
        assert config.base_delay == 1.0
        assert config.max_delay == 60.0
        assert config.backoff_multiplier == 2.0
        assert config.jitter is True
        assert RetryableError in config.retryable_exceptions
    
    def test_with_retries_success(self):
        """Test retry decorator with successful function."""
        call_count = 0
        
        @with_retries(RetryConfig(max_retries=3))
        def successful_function():
            nonlocal call_count
            call_count += 1
            return "success"
        
        result = successful_function()
        
        assert result == "success"
        assert call_count == 1  # Should only be called once
    
    def test_with_retries_eventual_success(self):
        """Test retry decorator with function that succeeds after retries."""
        call_count = 0
        
        @with_retries(RetryConfig(max_retries=3, base_delay=0.01))  # Fast retries for testing
        def eventually_successful_function():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise RetryableError("Temporary failure")
            return "success"
        
        result = eventually_successful_function()
        
        assert result == "success"
        assert call_count == 3  # Should be called 3 times
    
    def test_with_retries_max_retries_exceeded(self):
        """Test retry decorator when max retries are exceeded."""
        call_count = 0
        
        @with_retries(RetryConfig(max_retries=2, base_delay=0.01))
        def always_failing_function():
            nonlocal call_count
            call_count += 1
            raise RetryableError("Always fails")
        
        with pytest.raises(RetryableError):
            always_failing_function()
        
        assert call_count == 3  # Initial call + 2 retries
    
    def test_with_retries_non_retryable_error(self):
        """Test retry decorator with non-retryable error."""
        call_count = 0
        
        @with_retries(RetryConfig(max_retries=3))
        def function_with_non_retryable_error():
            nonlocal call_count
            call_count += 1
            raise ValueError("Non-retryable error")
        
        with pytest.raises(ValueError):
            function_with_non_retryable_error()
        
        assert call_count == 1  # Should not retry
    
    def test_smart_delay_basic(self):
        """Test smart delay calculation."""
        # Base case
        delay = smart_delay(base_delay=2.0, request_count=0, recent_errors=0, success_rate=1.0)
        assert 1.6 <= delay <= 2.4  # With jitter
        
        # With errors
        delay_with_errors = smart_delay(base_delay=2.0, recent_errors=2, success_rate=1.0)
        assert delay_with_errors > delay  # Should be longer
        
        # With low success rate
        delay_low_success = smart_delay(base_delay=2.0, success_rate=0.5)
        assert delay_low_success > delay  # Should be longer
        
        # With high request count
        delay_high_requests = smart_delay(base_delay=2.0, request_count=100)
        assert delay_high_requests > delay  # Should be longer
    
    def test_circuit_breaker_closed(self):
        """Test circuit breaker in closed state."""
        call_count = 0
        
        @circuit_breaker(failure_threshold=3, recovery_timeout=0.1)
        def successful_function():
            nonlocal call_count
            call_count += 1
            return "success"
        
        # Should work normally
        result = successful_function()
        assert result == "success"
        assert call_count == 1
    
    def test_circuit_breaker_opens(self):
        """Test circuit breaker opening after failures."""
        call_count = 0
        
        @circuit_breaker(failure_threshold=2, recovery_timeout=0.1)
        def failing_function():
            nonlocal call_count
            call_count += 1
            raise Exception("Always fails")
        
        # First two calls should fail normally
        with pytest.raises(Exception):
            failing_function()
        
        with pytest.raises(Exception):
            failing_function()
        
        # Third call should trigger circuit breaker
        with pytest.raises(RuntimeError, match="Circuit breaker is open"):
            failing_function()
        
        assert call_count == 2  # Third call shouldn't reach the function
    
    def test_circuit_breaker_recovery(self):
        """Test circuit breaker recovery after timeout."""
        call_count = 0
        
        @circuit_breaker(failure_threshold=1, recovery_timeout=0.01)  # Very short timeout
        def function_that_recovers():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise Exception("First call fails")
            return "success"
        
        # First call fails and opens circuit
        with pytest.raises(Exception):
            function_that_recovers()
        
        # Wait for recovery timeout
        time.sleep(0.02)
        
        # Should recover and succeed
        result = function_that_recovers()
        assert result == "success"
        assert call_count == 2


class TestRetryableErrors:
    """Test custom exception hierarchy."""
    
    def test_retryable_error_hierarchy(self):
        """Test that custom errors inherit from RetryableError."""
        rate_limit_error = RateLimitError("Rate limited")
        
        assert isinstance(rate_limit_error, RetryableError)
        assert isinstance(rate_limit_error, Exception)
        
        # Should be catchable as RetryableError
        try:
            raise rate_limit_error
        except RetryableError as e:
            assert str(e) == "Rate limited" 