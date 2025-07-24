#!/usr/bin/env python3
"""
Production Recovery System for LinkedIn Feed Scraper
====================================================

Comprehensive retry and recovery mechanisms for production-scale LinkedIn scraping.
Handles authentication failures, connection issues, rate limiting, and browser crashes
with intelligent recovery strategies for daily 2000-post operations.

Features:
- Exponential backoff for different error types
- Circuit breaker pattern for rate limiting
- Automatic browser restart on crashes
- Session persistence and recovery
- Intelligent retry strategies based on error type
- Production-ready monitoring and alerting
"""

import time
import random
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, Callable, Tuple
from enum import Enum
import json
from pathlib import Path
from dataclasses import dataclass

from production_logger import ErrorCategory, get_production_logger

class RecoveryStrategy(Enum):
    """Recovery strategies for different error types"""
    IMMEDIATE_RETRY = "immediate_retry"
    EXPONENTIAL_BACKOFF = "exponential_backoff"
    CIRCUIT_BREAKER = "circuit_breaker"
    BROWSER_RESTART = "browser_restart"
    SESSION_RESET = "session_reset"
    WAIT_AND_RETRY = "wait_and_retry"
    ABORT_OPERATION = "abort_operation"

@dataclass
class RetryConfig:
    """Configuration for retry behavior"""
    max_retries: int
    initial_delay: float
    max_delay: float
    backoff_multiplier: float
    jitter: bool = True

class ProductionRecovery:
    """Production-ready recovery system for LinkedIn scraping"""
    
    def __init__(self):
        self.logger = get_production_logger()
        
        # Retry configurations for different error types
        self.retry_configs = {
            ErrorCategory.CONNECTION: RetryConfig(
                max_retries=5,
                initial_delay=2.0,
                max_delay=60.0,
                backoff_multiplier=2.0
            ),
            ErrorCategory.AUTHENTICATION: RetryConfig(
                max_retries=3,
                initial_delay=5.0,
                max_delay=30.0,
                backoff_multiplier=1.5
            ),
            ErrorCategory.BROWSER: RetryConfig(
                max_retries=3,
                initial_delay=5.0,
                max_delay=30.0,
                backoff_multiplier=2.0
            ),
            ErrorCategory.CONTENT: RetryConfig(
                max_retries=2,
                initial_delay=1.0,
                max_delay=10.0,
                backoff_multiplier=2.0
            ),
            ErrorCategory.RATE_LIMIT: RetryConfig(
                max_retries=1,
                initial_delay=3600.0,  # 1 hour for rate limits
                max_delay=86400.0,     # 24 hours max
                backoff_multiplier=2.0
            )
        }
        
        # Circuit breaker states
        self.circuit_breakers = {
            ErrorCategory.RATE_LIMIT: {
                "state": "closed",  # closed, open, half_open
                "failure_count": 0,
                "failure_threshold": 1,
                "recovery_timeout": 3600,  # 1 hour
                "last_failure_time": None
            },
            ErrorCategory.AUTHENTICATION: {
                "state": "closed",
                "failure_count": 0,
                "failure_threshold": 3,
                "recovery_timeout": 1800,  # 30 minutes
                "last_failure_time": None
            }
        }
        
        # Session state tracking
        self.session_state = {
            "browser_restart_count": 0,
            "auth_retry_count": 0,
            "last_successful_extraction": None,
            "consecutive_failures": 0,
            "session_start_time": datetime.now()
        }
        
        # Performance tracking
        self.performance_metrics = {
            "extraction_rate": 0.0,
            "success_rate": 100.0,
            "average_response_time": 0.0,
            "last_performance_check": datetime.now()
        }
    
    def should_retry(self, error_category: ErrorCategory, attempt: int, exception: Exception = None) -> Tuple[bool, RecoveryStrategy, float]:
        """
        Determine if operation should be retried and with what strategy
        Returns: (should_retry, strategy, delay_seconds)
        """
        
        # Check circuit breaker first
        if error_category in self.circuit_breakers:
            breaker = self.circuit_breakers[error_category]
            if breaker["state"] == "open":
                if self._should_attempt_recovery(error_category):
                    breaker["state"] = "half_open"
                    self.logger.log_error(error_category, f"Circuit breaker moving to half-open for {error_category.value}")
                else:
                    return False, RecoveryStrategy.ABORT_OPERATION, 0
        
        # Get retry config for this error type
        config = self.retry_configs.get(error_category)
        if not config or attempt >= config.max_retries:
            return False, RecoveryStrategy.ABORT_OPERATION, 0
        
        # Determine strategy and delay based on error type and attempt
        strategy, delay = self._get_recovery_strategy(error_category, attempt, exception)
        
        return True, strategy, delay
    
    def _get_recovery_strategy(self, error_category: ErrorCategory, attempt: int, exception: Exception = None) -> Tuple[RecoveryStrategy, float]:
        """Get specific recovery strategy and delay for error type"""
        
        config = self.retry_configs[error_category]
        
        if error_category == ErrorCategory.RATE_LIMIT:
            # Rate limiting requires special handling
            return RecoveryStrategy.CIRCUIT_BREAKER, self._calculate_rate_limit_delay(attempt)
        
        elif error_category == ErrorCategory.AUTHENTICATION:
            if attempt == 1:
                return RecoveryStrategy.SESSION_RESET, 5.0
            else:
                return RecoveryStrategy.WAIT_AND_RETRY, self._calculate_exponential_backoff(config, attempt)
        
        elif error_category == ErrorCategory.BROWSER:
            if "crash" in str(exception).lower() or "session" in str(exception).lower():
                return RecoveryStrategy.BROWSER_RESTART, 10.0
            else:
                return RecoveryStrategy.EXPONENTIAL_BACKOFF, self._calculate_exponential_backoff(config, attempt)
        
        elif error_category == ErrorCategory.CONNECTION:
            return RecoveryStrategy.EXPONENTIAL_BACKOFF, self._calculate_exponential_backoff(config, attempt)
        
        else:
            return RecoveryStrategy.EXPONENTIAL_BACKOFF, self._calculate_exponential_backoff(config, attempt)
    
    def _calculate_exponential_backoff(self, config: RetryConfig, attempt: int) -> float:
        """Calculate exponential backoff delay with jitter"""
        delay = min(config.initial_delay * (config.backoff_multiplier ** attempt), config.max_delay)
        
        if config.jitter:
            # Add jitter (±25% randomization)
            jitter_range = delay * 0.25
            delay += random.uniform(-jitter_range, jitter_range)
        
        return max(delay, 0.1)  # Minimum 0.1 second delay
    
    def _calculate_rate_limit_delay(self, attempt: int) -> float:
        """Calculate delay for rate limiting - increases significantly with attempts"""
        base_delays = [3600, 7200, 14400, 28800]  # 1h, 2h, 4h, 8h
        if attempt <= len(base_delays):
            return base_delays[attempt - 1]
        else:
            return 86400  # 24 hours for persistent rate limiting
    
    def record_failure(self, error_category: ErrorCategory, exception: Exception = None):
        """Record failure for circuit breaker and monitoring"""
        
        # Update circuit breaker
        if error_category in self.circuit_breakers:
            breaker = self.circuit_breakers[error_category]
            breaker["failure_count"] += 1
            breaker["last_failure_time"] = datetime.now()
            
            if breaker["failure_count"] >= breaker["failure_threshold"]:
                breaker["state"] = "open"
                self.logger.log_error(
                    error_category,
                    f"Circuit breaker opened for {error_category.value} after {breaker['failure_count']} failures"
                )
        
        # Update session state
        self.session_state["consecutive_failures"] += 1
        
        # Log failure details
        self.logger.log_error(error_category, f"Operation failed", exception)
    
    def record_success(self, error_category: ErrorCategory = None):
        """Record successful operation"""
        
        # Reset circuit breaker if specified
        if error_category and error_category in self.circuit_breakers:
            breaker = self.circuit_breakers[error_category]
            if breaker["state"] == "half_open":
                breaker["state"] = "closed"
                breaker["failure_count"] = 0
                self.logger.main_logger.info(f"Circuit breaker closed for {error_category.value} after successful operation")
        
        # Update session state
        self.session_state["consecutive_failures"] = 0
        self.session_state["last_successful_extraction"] = datetime.now()
    
    def _should_attempt_recovery(self, error_category: ErrorCategory) -> bool:
        """Check if enough time has passed to attempt recovery"""
        
        breaker = self.circuit_breakers[error_category]
        if not breaker["last_failure_time"]:
            return True
        
        time_since_failure = (datetime.now() - breaker["last_failure_time"]).total_seconds()
        return time_since_failure >= breaker["recovery_timeout"]
    
    def execute_recovery_strategy(self, strategy: RecoveryStrategy, delay: float, context: Dict[str, Any] = None) -> bool:
        """
        Execute the specified recovery strategy
        Returns: True if recovery was successful, False otherwise
        """
        
        context = context or {}
        
        try:
            if strategy == RecoveryStrategy.IMMEDIATE_RETRY:
                return True
            
            elif strategy == RecoveryStrategy.EXPONENTIAL_BACKOFF:
                self.logger.main_logger.info(f"Waiting {delay:.1f} seconds before retry")
                time.sleep(delay)
                return True
            
            elif strategy == RecoveryStrategy.CIRCUIT_BREAKER:
                self.logger.main_logger.warning(f"Rate limit detected, waiting {delay:.0f} seconds")
                # For rate limits, we might want to save state and exit gracefully
                if delay > 1800:  # More than 30 minutes
                    self._save_session_state(context)
                    return False
                time.sleep(delay)
                return True
            
            elif strategy == RecoveryStrategy.BROWSER_RESTART:
                return self._restart_browser(context)
            
            elif strategy == RecoveryStrategy.SESSION_RESET:
                return self._reset_session(context)
            
            elif strategy == RecoveryStrategy.WAIT_AND_RETRY:
                self.logger.main_logger.info(f"Waiting {delay:.1f} seconds before retry")
                time.sleep(delay)
                return True
            
            elif strategy == RecoveryStrategy.ABORT_OPERATION:
                self.logger.main_logger.error("Operation aborted due to persistent failures")
                return False
            
            else:
                self.logger.main_logger.error(f"Unknown recovery strategy: {strategy}")
                return False
                
        except Exception as e:
            self.logger.log_error(ErrorCategory.LOGIC, f"Recovery strategy failed: {strategy}", e)
            return False
    
    def _restart_browser(self, context: Dict[str, Any]) -> bool:
        """Restart browser instance"""
        try:
            self.session_state["browser_restart_count"] += 1
            
            # Close existing browser if available
            driver = context.get("driver")
            if driver:
                try:
                    driver.quit()
                except:
                    pass
            
            self.logger.main_logger.info(f"Browser restart #{self.session_state['browser_restart_count']}")
            
            # Give system time to clean up
            time.sleep(5)
            
            # Browser will be recreated by the calling code
            return True
            
        except Exception as e:
            self.logger.log_error(ErrorCategory.BROWSER, "Browser restart failed", e)
            return False
    
    def _reset_session(self, context: Dict[str, Any]) -> bool:
        """Reset authentication session"""
        try:
            self.session_state["auth_retry_count"] += 1
            
            # Clear cookies/session data
            driver = context.get("driver")
            if driver:
                try:
                    driver.delete_all_cookies()
                except:
                    pass
            
            self.logger.main_logger.info(f"Session reset #{self.session_state['auth_retry_count']}")
            return True
            
        except Exception as e:
            self.logger.log_error(ErrorCategory.AUTHENTICATION, "Session reset failed", e)
            return False
    
    def _save_session_state(self, context: Dict[str, Any]):
        """Save current session state for potential resumption"""
        try:
            state_file = Path("logs") / f"session_state_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            state_data = {
                "session_state": self.session_state,
                "extraction_progress": context.get("extraction_progress", {}),
                "timestamp": datetime.now().isoformat(),
                "reason": "Rate limit exceeded - session paused"
            }
            
            with open(state_file, 'w') as f:
                json.dump(state_data, f, indent=2, default=str)
            
            self.logger.main_logger.info(f"Session state saved to {state_file}")
            
        except Exception as e:
            self.logger.log_error(ErrorCategory.LOGIC, "Failed to save session state", e)
    
    def update_performance_metrics(self, current_posts: int, target_posts: int, success_rate: float, time_elapsed: float):
        """Update performance metrics for monitoring"""
        
        self.performance_metrics.update({
            "extraction_rate": current_posts / (time_elapsed / 60) if time_elapsed > 0 else 0,
            "success_rate": success_rate,
            "average_response_time": time_elapsed / current_posts if current_posts > 0 else 0,
            "last_performance_check": datetime.now()
        })
        
        # Check for performance degradation
        if success_rate < 90.0 and current_posts > 100:
            self.logger.log_error(
                ErrorCategory.VALIDATION,
                f"Performance degradation detected: {success_rate:.1f}% success rate",
                context=self.performance_metrics
            )
    
    def get_production_readiness_assessment(self) -> Dict[str, Any]:
        """Get comprehensive assessment of production readiness"""
        
        session_duration = (datetime.now() - self.session_state["session_start_time"]).total_seconds()
        
        assessment = {
            "session_duration_minutes": session_duration / 60,
            "browser_restarts": self.session_state["browser_restart_count"],
            "auth_retries": self.session_state["auth_retry_count"],
            "consecutive_failures": self.session_state["consecutive_failures"],
            "performance_metrics": self.performance_metrics,
            "circuit_breaker_states": {k: v["state"] for k, v in self.circuit_breakers.items()},
            "production_ready": self._assess_production_readiness()
        }
        
        return assessment
    
    def _assess_production_readiness(self) -> Dict[str, Any]:
        """Assess if system is ready for production 2000-post operations"""
        
        issues = []
        recommendations = []
        
        # Check circuit breaker states
        for category, breaker in self.circuit_breakers.items():
            if breaker["state"] == "open":
                issues.append(f"{category.value} circuit breaker is open")
                recommendations.append(f"Wait for {category.value} recovery timeout")
        
        # Check consecutive failures
        if self.session_state["consecutive_failures"] > 10:
            issues.append(f"High consecutive failure count: {self.session_state['consecutive_failures']}")
            recommendations.append("Investigate root cause of failures")
        
        # Check browser restart frequency
        if self.session_state["browser_restart_count"] > 3:
            issues.append(f"Frequent browser restarts: {self.session_state['browser_restart_count']}")
            recommendations.append("Check browser stability and memory usage")
        
        # Check success rate
        if self.performance_metrics["success_rate"] < 95.0:
            issues.append(f"Low success rate: {self.performance_metrics['success_rate']:.1f}%")
            recommendations.append("Review and update extraction selectors")
        
        # Overall assessment
        if not issues:
            status = "EXCELLENT"
            ready_for_2000_posts = True
        elif len(issues) <= 2 and self.performance_metrics["success_rate"] >= 90.0:
            status = "GOOD"
            ready_for_2000_posts = True
        else:
            status = "NEEDS_ATTENTION"
            ready_for_2000_posts = False
        
        return {
            "status": status,
            "ready_for_2000_posts": ready_for_2000_posts,
            "issues": issues,
            "recommendations": recommendations
        }

# Global recovery system instance
recovery_system = None

def get_recovery_system() -> ProductionRecovery:
    """Get or create recovery system instance"""
    global recovery_system
    if recovery_system is None:
        recovery_system = ProductionRecovery()
    return recovery_system

def retry_with_recovery(error_category: ErrorCategory, max_attempts: int = None):
    """Decorator for functions that need retry with recovery"""
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            recovery = get_recovery_system()
            
            for attempt in range(max_attempts or recovery.retry_configs.get(error_category, RetryConfig(3, 1, 10, 2)).max_retries + 1):
                try:
                    result = func(*args, **kwargs)
                    recovery.record_success(error_category)
                    return result
                    
                except Exception as e:
                    if attempt == 0:  # First attempt
                        recovery.record_failure(error_category, e)
                    
                    should_retry, strategy, delay = recovery.should_retry(error_category, attempt + 1, e)
                    
                    if not should_retry:
                        recovery.logger.log_error(error_category, f"Max retries exceeded for {func.__name__}", e)
                        raise
                    
                    # Execute recovery strategy
                    if not recovery.execute_recovery_strategy(strategy, delay, {"function": func.__name__}):
                        recovery.logger.log_error(error_category, f"Recovery failed for {func.__name__}", e)
                        raise
            
            # If we get here, all retries were exhausted
            raise Exception(f"All retry attempts exhausted for {func.__name__}")
        
        return wrapper
    return decorator 