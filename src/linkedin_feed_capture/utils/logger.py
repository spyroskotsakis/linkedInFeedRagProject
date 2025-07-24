"""
Structured logging configuration for LinkedIn feed capture.

Provides consistent, structured logging throughout the application with
support for JSON formatting, rotation, and different output formats.
"""

import logging
import logging.handlers
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional

import structlog
from structlog.types import FilteringBoundLogger


def setup_logging(
    log_level: str = "INFO",
    log_format: str = "json", 
    log_file_path: Optional[str] = None,
    log_rotation_size: str = "10MB",
    log_retention_days: int = 30,
    enable_console: bool = True,
) -> None:
    """
    Configure structured logging for the application.
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_format: Format type ('json' or 'console')
        log_file_path: Path to log file (optional)
        log_rotation_size: Size at which to rotate logs
        log_retention_days: How many days to keep old logs
        enable_console: Whether to log to console
    """
    # Configure structlog
    shared_processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]
    
    if log_format == "json":
        shared_processors.append(structlog.processors.JSONRenderer())
    else:
        shared_processors.append(
            structlog.dev.ConsoleRenderer(colors=enable_console and sys.stderr.isatty())
        )
    
    structlog.configure(
        processors=shared_processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    # Configure stdlib logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stderr if enable_console else None,
        level=getattr(logging, log_level.upper()),
    )
    
    # Setup file logging if specified
    if log_file_path:
        _setup_file_logging(
            log_file_path=log_file_path,
            log_level=log_level,
            log_rotation_size=log_rotation_size,
            log_retention_days=log_retention_days,
        )
    
    # Reduce noise from external libraries
    logging.getLogger("selenium").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)


def _setup_file_logging(
    log_file_path: str,
    log_level: str,
    log_rotation_size: str,
    log_retention_days: int,
) -> None:
    """Setup rotating file handler for logs."""
    log_path = Path(log_file_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert size string to bytes
    size_bytes = _parse_size_string(log_rotation_size)
    
    # Create rotating file handler
    file_handler = logging.handlers.RotatingFileHandler(
        filename=log_path,
        maxBytes=size_bytes,
        backupCount=log_retention_days,
        encoding="utf-8",
    )
    file_handler.setLevel(getattr(logging, log_level.upper()))
    
    # Add handler to root logger
    root_logger = logging.getLogger()
    root_logger.addHandler(file_handler)


def _parse_size_string(size_str: str) -> int:
    """Parse size string like '10MB' to bytes."""
    size_str = size_str.upper().strip()
    
    # Order matters - check longer suffixes first to avoid 'B' matching 'KB', 'MB', etc.
    multipliers = [
        ('GB', 1024 ** 3),
        ('MB', 1024 ** 2), 
        ('KB', 1024),
        ('B', 1),
    ]
    
    for suffix, multiplier in multipliers:
        if size_str.endswith(suffix):
            size_part = size_str[:-len(suffix)].strip()
            try:
                return int(float(size_part) * multiplier)
            except ValueError:
                break
    
    raise ValueError(f"Invalid size format: {size_str}")


def get_logger(name: str) -> FilteringBoundLogger:
    """
    Get a structured logger instance.
    
    Args:
        name: Logger name (typically __name__)
        
    Returns:
        Configured structlog logger instance
    """
    return structlog.get_logger(name)


class LoggerMixin:
    """Mixin class to add logging capability to any class."""
    
    @property
    def logger(self) -> FilteringBoundLogger:
        """Get logger for this class."""
        return get_logger(self.__class__.__module__ + "." + self.__class__.__name__)


def log_function_call(
    logger: FilteringBoundLogger,
    level: str = "debug",
) -> Any:
    """
    Decorator to log function calls with arguments and return values.
    
    Args:
        logger: Logger instance to use
        level: Log level for the messages
        
    Returns:
        Decorator function
    """
    def decorator(func: Any) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = f"{func.__module__}.{func.__qualname__}"
            
            # Log function entry
            logger.log(
                level,
                "Function call started",
                function=func_name,
                args=_sanitize_args(args),
                kwargs=_sanitize_kwargs(kwargs),
            )
            
            try:
                result = func(*args, **kwargs)
                
                # Log successful completion
                logger.log(
                    level,
                    "Function call completed",
                    function=func_name,
                    result_type=type(result).__name__,
                )
                
                return result
                
            except Exception as e:
                # Log exception
                logger.error(
                    "Function call failed",
                    function=func_name,
                    error=str(e),
                    error_type=type(e).__name__,
                )
                raise
                
        return wrapper
    return decorator


def _sanitize_args(args: tuple) -> list:
    """Sanitize function arguments for logging."""
    sanitized = []
    for arg in args:
        if isinstance(arg, (str, int, float, bool, type(None))):
            sanitized.append(arg)
        else:
            sanitized.append(f"<{type(arg).__name__}>")
    return sanitized


def _sanitize_kwargs(kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Sanitize keyword arguments for logging."""
    sanitized = {}
    sensitive_keys = {'password', 'token', 'key', 'secret', 'auth'}
    
    for key, value in kwargs.items():
        if any(sensitive in key.lower() for sensitive in sensitive_keys):
            sanitized[key] = "***REDACTED***"
        elif isinstance(value, (str, int, float, bool, type(None))):
            sanitized[key] = value
        else:
            sanitized[key] = f"<{type(value).__name__}>"
    
    return sanitized


# Application-specific log helpers
def log_scraping_start(
    logger: FilteringBoundLogger, 
    target_posts: int,
    config: Dict[str, Any],
) -> None:
    """Log the start of a scraping session."""
    logger.info(
        "Starting LinkedIn feed scraping session",
        target_posts=target_posts,
        headless=config.get("headless", True),
        max_retries=config.get("max_retries", 5),
        scroll_delay=config.get("scroll_delay_ms", 2000),
    )


def log_scraping_progress(
    logger: FilteringBoundLogger,
    posts_found: int,
    target_posts: int,
    scroll_attempts: int,
) -> None:
    """Log scraping progress."""
    progress_pct = (posts_found / target_posts * 100) if target_posts > 0 else 0
    
    logger.info(
        "Scraping progress update",
        posts_found=posts_found,
        target_posts=target_posts,
        progress_percentage=round(progress_pct, 1),
        scroll_attempts=scroll_attempts,
    )


def log_post_extracted(
    logger: FilteringBoundLogger,
    post_urn: str,
    author: str,
    content_length: int,
) -> None:
    """Log successful post extraction."""
    logger.info(
        "Post extracted successfully",
        post_urn=post_urn,
        author=author,
        content_length=content_length,
    )


def log_scraping_complete(
    logger: FilteringBoundLogger,
    total_posts: int,
    duration_seconds: float,
    success_rate: float,
) -> None:
    """Log completion of scraping session."""
    logger.info(
        "Scraping session completed",
        total_posts_extracted=total_posts,
        duration_seconds=round(duration_seconds, 2),
        posts_per_second=round(total_posts / duration_seconds, 2) if duration_seconds > 0 else 0,
        success_rate_percentage=round(success_rate * 100, 1),
    ) 