#!/usr/bin/env python3
"""
Production Logger for LinkedIn Feed Scraper
===========================================

Comprehensive logging system for production-scale LinkedIn scraping operations.
Categorizes errors into connection, logic, and content issues for better monitoring
and debugging of daily 2000-post extraction operations.

Features:
- Structured logging with different categories (connection, logic, content, auth)
- Multiple log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Separate log files for different types of issues
- Production-ready formatting with timestamps and structured data
- Error counting and alerting thresholds
- Recovery recommendations for different error types
"""

import logging
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
from enum import Enum
import traceback

class ErrorCategory(Enum):
    """Error categories for production monitoring"""
    CONNECTION = "connection"
    AUTHENTICATION = "authentication" 
    LOGIC = "logic"
    CONTENT = "content"
    BROWSER = "browser"
    RATE_LIMIT = "rate_limit"
    VALIDATION = "validation"

class ProductionLogger:
    """Production-ready logger with error categorization and monitoring"""
    
    def __init__(self, log_dir: str = "logs", run_id: Optional[str] = None):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        self.run_id = run_id or datetime.now().strftime("%Y%m%d_%H%M%S")
        self.session_start = datetime.now()
        
        # Error counters for monitoring
        self.error_counts = {
            ErrorCategory.CONNECTION: 0,
            ErrorCategory.AUTHENTICATION: 0,
            ErrorCategory.LOGIC: 0,
            ErrorCategory.CONTENT: 0,
            ErrorCategory.BROWSER: 0,
            ErrorCategory.RATE_LIMIT: 0,
            ErrorCategory.VALIDATION: 0
        }
        
        # Critical thresholds for alerts
        self.alert_thresholds = {
            ErrorCategory.CONNECTION: 5,
            ErrorCategory.AUTHENTICATION: 3,
            ErrorCategory.LOGIC: 10,
            ErrorCategory.CONTENT: 50,  # Higher threshold for content issues
            ErrorCategory.BROWSER: 5,
            ErrorCategory.RATE_LIMIT: 1,  # Immediate alert for rate limiting
            ErrorCategory.VALIDATION: 20
        }
        
        self._setup_loggers()
        
    def _setup_loggers(self):
        """Setup multiple loggers for different purposes"""
        
        # Main application logger
        self.main_logger = self._create_logger(
            "main",
            self.log_dir / f"linkedin_scraper_{self.run_id}.log",
            logging.INFO
        )
        
        # Error-specific loggers
        self.error_logger = self._create_logger(
            "errors",
            self.log_dir / f"errors_{self.run_id}.log",
            logging.WARNING
        )
        
        # Connection issues logger
        self.connection_logger = self._create_logger(
            "connection",
            self.log_dir / f"connection_{self.run_id}.log",
            logging.WARNING
        )
        
        # Authentication logger
        self.auth_logger = self._create_logger(
            "auth",
            self.log_dir / f"authentication_{self.run_id}.log",
            logging.INFO
        )
        
        # Performance logger for monitoring extraction rates
        self.performance_logger = self._create_logger(
            "performance",
            self.log_dir / f"performance_{self.run_id}.log",
            logging.INFO
        )
        
    def _create_logger(self, name: str, log_file: Path, level: int) -> logging.Logger:
        """Create a logger with consistent formatting"""
        logger = logging.getLogger(f"linkedin_scraper_{name}_{self.run_id}")
        logger.setLevel(level)
        
        # Avoid duplicate handlers
        if logger.handlers:
            return logger
            
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        
        # Console handler for critical issues
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        
        # Formatter with structured data
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        return logger
    
    def log_session_start(self, target_posts: int, config: Dict[str, Any]):
        """Log session initialization"""
        session_info = {
            "run_id": self.run_id,
            "target_posts": target_posts,
            "session_start": self.session_start.isoformat(),
            "config": config
        }
        
        self.main_logger.info(f"SESSION_START: {json.dumps(session_info)}")
        self.performance_logger.info(f"EXTRACTION_TARGET: {target_posts} posts")
    
    def log_error(self, category: ErrorCategory, message: str, 
                  exception: Optional[Exception] = None, 
                  context: Optional[Dict[str, Any]] = None):
        """Log categorized error with context"""
        
        self.error_counts[category] += 1
        
        error_data = {
            "category": category.value,
            "message": message,
            "error_count": self.error_counts[category],
            "timestamp": datetime.now().isoformat(),
            "context": context or {}
        }
        
        if exception:
            error_data["exception"] = {
                "type": type(exception).__name__,
                "message": str(exception),
                "traceback": traceback.format_exc()
            }
        
        log_message = f"ERROR_{category.value.upper()}: {json.dumps(error_data)}"
        
        # Log to main error logger
        self.error_logger.error(log_message)
        
        # Log to category-specific logger
        if category == ErrorCategory.CONNECTION:
            self.connection_logger.error(log_message)
        elif category == ErrorCategory.AUTHENTICATION:
            self.auth_logger.error(log_message)
        
        # Check alert thresholds
        if self.error_counts[category] >= self.alert_thresholds[category]:
            self._trigger_alert(category)
    
    def log_auth_event(self, event_type: str, success: bool, details: Optional[str] = None):
        """Log authentication events"""
        auth_data = {
            "event_type": event_type,
            "success": success,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        
        log_level = logging.INFO if success else logging.ERROR
        self.auth_logger.log(log_level, f"AUTH_{event_type.upper()}: {json.dumps(auth_data)}")
        
        if not success:
            self.log_error(ErrorCategory.AUTHENTICATION, f"Authentication failed: {event_type}", context=auth_data)
    
    def log_extraction_progress(self, current: int, target: int, success_rate: float, 
                              time_elapsed: float):
        """Log extraction progress for monitoring"""
        progress_data = {
            "current_posts": current,
            "target_posts": target,
            "progress_percent": (current / target) * 100,
            "success_rate": success_rate,
            "time_elapsed_minutes": time_elapsed / 60,
            "posts_per_minute": current / (time_elapsed / 60) if time_elapsed > 0 else 0,
            "estimated_completion_minutes": ((target - current) / (current / (time_elapsed / 60))) if current > 0 and time_elapsed > 0 else None
        }
        
        self.performance_logger.info(f"PROGRESS: {json.dumps(progress_data)}")
        
        # Alert if success rate drops below threshold
        if success_rate < 95.0 and current > 50:  # After 50 posts with <95% success rate
            self.log_error(
                ErrorCategory.VALIDATION,
                f"Success rate dropped to {success_rate:.1f}% after {current} posts",
                context=progress_data
            )
    
    def log_connection_issue(self, issue_type: str, details: str, retry_count: int = 0):
        """Log connection-related issues"""
        self.log_error(
            ErrorCategory.CONNECTION,
            f"Connection issue: {issue_type}",
            context={
                "issue_type": issue_type,
                "details": details,
                "retry_count": retry_count,
                "recovery_action": self._get_recovery_action(ErrorCategory.CONNECTION, issue_type)
            }
        )
    
    def log_rate_limit(self, response_code: int, details: str):
        """Log rate limiting events"""
        self.log_error(
            ErrorCategory.RATE_LIMIT,
            f"Rate limit detected: HTTP {response_code}",
            context={
                "response_code": response_code,
                "details": details,
                "recovery_action": self._get_recovery_action(ErrorCategory.RATE_LIMIT, str(response_code))
            }
        )
    
    def log_browser_issue(self, issue_type: str, details: str):
        """Log browser-related issues"""
        self.log_error(
            ErrorCategory.BROWSER,
            f"Browser issue: {issue_type}",
            context={
                "issue_type": issue_type,
                "details": details,
                "recovery_action": self._get_recovery_action(ErrorCategory.BROWSER, issue_type)
            }
        )
    
    def log_content_issue(self, post_index: int, issue_type: str, details: str):
        """Log content extraction issues"""
        self.log_error(
            ErrorCategory.CONTENT,
            f"Content extraction issue at post {post_index}: {issue_type}",
            context={
                "post_index": post_index,
                "issue_type": issue_type,
                "details": details
            }
        )
    
    def log_session_end(self, final_stats: Dict[str, Any]):
        """Log session completion with final statistics"""
        session_duration = (datetime.now() - self.session_start).total_seconds()
        
        session_summary = {
            "run_id": self.run_id,
            "session_duration_minutes": session_duration / 60,
            "final_stats": final_stats,
            "error_summary": {category.value: count for category, count in self.error_counts.items()},
            "session_end": datetime.now().isoformat()
        }
        
        self.main_logger.info(f"SESSION_END: {json.dumps(session_summary)}")
        self.performance_logger.info(f"SESSION_SUMMARY: {json.dumps(session_summary)}")
        
        # Generate session report
        self._generate_session_report(session_summary)
    
    def _trigger_alert(self, category: ErrorCategory):
        """Trigger alert when error thresholds are exceeded"""
        alert_data = {
            "category": category.value,
            "error_count": self.error_counts[category],
            "threshold": self.alert_thresholds[category],
            "timestamp": datetime.now().isoformat(),
            "recommended_action": self._get_recovery_action(category)
        }
        
        alert_message = f"ALERT_{category.value.upper()}_THRESHOLD_EXCEEDED: {json.dumps(alert_data)}"
        
        self.error_logger.critical(alert_message)
        self.main_logger.critical(alert_message)
        
        # Print to console for immediate attention
        print(f"🚨 ALERT: {category.value} error threshold exceeded ({self.error_counts[category]}/{self.alert_thresholds[category]})")
        print(f"   Recommended action: {self._get_recovery_action(category)}")
    
    def _get_recovery_action(self, category: ErrorCategory, specific_issue: str = None) -> str:
        """Get recommended recovery action for different error types"""
        
        recovery_actions = {
            ErrorCategory.CONNECTION: {
                "default": "Check internet connection, retry with exponential backoff",
                "timeout": "Increase timeout values, check network stability",
                "dns": "Check DNS settings, try different network"
            },
            ErrorCategory.AUTHENTICATION: {
                "default": "Verify credentials, check for account locks",
                "security_challenge": "Complete manual security challenge",
                "session_expired": "Re-authenticate with fresh login"
            },
            ErrorCategory.RATE_LIMIT: {
                "default": "Wait 24 hours before retry, reduce extraction frequency",
                "429": "Implement exponential backoff, reduce post count",
                "999": "IP may be flagged, wait 24-48 hours or use different IP"
            },
            ErrorCategory.BROWSER: {
                "default": "Restart browser, clear cache",
                "driver_crash": "Update ChromeDriver, restart selenium",
                "memory": "Reduce batch size, restart browser periodically"
            },
            ErrorCategory.CONTENT: {
                "default": "Review selector updates, check LinkedIn DOM changes"
            },
            ErrorCategory.LOGIC: {
                "default": "Review code logic, check for edge cases"
            },
            ErrorCategory.VALIDATION: {
                "default": "Review post validation logic, update selectors"
            }
        }
        
        category_actions = recovery_actions.get(category, {})
        return category_actions.get(specific_issue, category_actions.get("default", "Manual investigation required"))
    
    def _generate_session_report(self, session_summary: Dict[str, Any]):
        """Generate human-readable session report"""
        report_file = self.log_dir / f"session_report_{self.run_id}.md"
        
        with open(report_file, 'w') as f:
            f.write(f"# LinkedIn Scraping Session Report\n\n")
            f.write(f"**Run ID:** {self.run_id}\n")
            f.write(f"**Date:** {self.session_start.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Duration:** {session_summary['session_duration_minutes']:.1f} minutes\n\n")
            
            f.write("## Extraction Results\n\n")
            stats = session_summary['final_stats']
            f.write(f"- **Posts Attempted:** {stats.get('attempted', 0)}\n")
            f.write(f"- **Posts Successful:** {stats.get('successful', 0)}\n")
            f.write(f"- **Success Rate:** {stats.get('success_rate', 0):.1f}%\n")
            f.write(f"- **Empty Posts Skipped:** {stats.get('empty_posts_skipped', 0)}\n")
            f.write(f"- **Extraction Errors:** {stats.get('extraction_errors', 0)}\n\n")
            
            f.write("## Error Summary\n\n")
            error_summary = session_summary['error_summary']
            total_errors = sum(error_summary.values())
            f.write(f"**Total Errors:** {total_errors}\n\n")
            
            for category, count in error_summary.items():
                if count > 0:
                    f.write(f"- **{category.title()} Errors:** {count}\n")
            
            f.write("\n## Production Readiness Assessment\n\n")
            
            success_rate = stats.get('success_rate', 0)
            if success_rate >= 98:
                f.write("✅ **EXCELLENT** - Production ready for daily 2000-post operations\n")
            elif success_rate >= 95:
                f.write("⚠️ **GOOD** - Suitable for production with monitoring\n")
            elif success_rate >= 90:
                f.write("🔍 **REVIEW** - Investigate issues before full production\n")
            else:
                f.write("❌ **CRITICAL** - Not ready for production use\n")
            
            # Recommendations
            f.write("\n## Recommendations\n\n")
            if error_summary.get('rate_limit', 0) > 0:
                f.write("- Implement longer delays between extractions\n")
            if error_summary.get('connection', 0) > 5:
                f.write("- Check network stability and implement better retry logic\n")
            if error_summary.get('authentication', 0) > 0:
                f.write("- Review authentication method and credentials\n")
            if success_rate < 98:
                f.write("- Review and update selectors for better extraction\n")
        
        self.main_logger.info(f"Session report generated: {report_file}")

# Global production logger instance
production_logger = None

def get_production_logger(log_dir: str = "logs", run_id: Optional[str] = None) -> ProductionLogger:
    """Get or create production logger instance"""
    global production_logger
    if production_logger is None:
        production_logger = ProductionLogger(log_dir, run_id)
    return production_logger

def log_error(category: ErrorCategory, message: str, exception: Optional[Exception] = None, context: Optional[Dict[str, Any]] = None):
    """Convenience function for logging errors"""
    logger = get_production_logger()
    logger.log_error(category, message, exception, context)

def log_auth_event(event_type: str, success: bool, details: Optional[str] = None):
    """Convenience function for logging auth events"""
    logger = get_production_logger()
    logger.log_auth_event(event_type, success, details)

def log_extraction_progress(current: int, target: int, success_rate: float, time_elapsed: float):
    """Convenience function for logging extraction progress"""
    logger = get_production_logger()
    logger.log_extraction_progress(current, target, success_rate, time_elapsed) 