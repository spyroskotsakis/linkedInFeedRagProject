"""
Integration tests for LinkedIn Feed Capture system.

Tests the integration between different modules and verifies end-to-end functionality.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timezone
import tempfile
from pathlib import Path

from linkedin_feed_capture.models.post import Post, PostMetrics
from linkedin_feed_capture.utils.logger import setup_logging, get_logger
from linkedin_feed_capture.utils.backoff import exponential_backoff, with_retries, RetryConfig


class TestModelIntegration:
    """Test integration between models and utilities."""

    def test_post_creation_and_serialization(self):
        """Test creating a complete post and serializing it."""
        # Create a post with all fields
        metrics = PostMetrics(likes=100, comments=20, shares=5, views=1000)
        
        post = Post(
            urn="urn:li:activity:1234567890",
            author="John Doe",
            content="This is a test post with #hashtags and great content!",
            posted_at=datetime.now(timezone.utc).replace(tzinfo=None),
            url="https://linkedin.com/posts/test-post",
            metrics=metrics,
            hashtags=["hashtags"],
            mentions=[],
            media_urls=[],
            is_promoted=False,
            company_name=None
        )
        
        # Test basic functionality
        assert post.urn == "urn:li:activity:1234567890"
        assert post.author == "John Doe"
        assert "#hashtags" in post.hashtags
        
        # Test calculated methods
        engagement_rate = post.get_engagement_rate()
        assert engagement_rate == 12.5  # (100+20+5)/1000 * 100
        
        assert not post.is_company_post()
        assert not post.has_media()
        
        # Test serialization
        json_dict = post.to_json_dict()
        assert json_dict["urn"] == post.urn
        assert json_dict["metrics"]["likes"] == 100
        
        # Test string representation
        str_repr = str(post)
        assert "John Doe" in str_repr
        assert "urn:li:activity:1234567890" in str_repr


class TestLoggingIntegration:
    """Test logging integration with temporary files."""

    def test_logging_setup_and_usage(self):
        """Test setting up logging and using it across modules."""
        with tempfile.TemporaryDirectory() as temp_dir:
            log_file = Path(temp_dir) / "test.log"
            
            # Setup logging
            setup_logging(
                console_level="INFO",
                file_level="DEBUG",
                file_path=str(log_file),
                max_file_size="1MB",
                backup_count=3,
                json_format=True
            )
            
            # Get logger and test it
            logger = get_logger("test_module")
            
            logger.info("Test info message")
            logger.debug("Test debug message")
            logger.warning("Test warning message")
            
            # Verify log file exists
            assert log_file.exists()
            
            # Read log content
            log_content = log_file.read_text()
            assert "Test info message" in log_content
            assert "test_module" in log_content


class TestRetryIntegration:
    """Test retry mechanisms with realistic scenarios."""

    def test_retry_with_exponential_backoff(self):
        """Test retry mechanism with exponential backoff."""
        call_count = 0
        
        @with_retries(RetryConfig(max_retries=3, base_delay=0.1))
        def flaky_function():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ConnectionError("Temporary failure")
            return "success"
        
        result = flaky_function()
        assert result == "success"
        assert call_count == 3

    def test_exponential_backoff_delays(self):
        """Test that exponential backoff produces correct delays."""
        delays = []
        for attempt in range(5):
            delay = exponential_backoff(attempt, base_delay=1.0, max_delay=60.0)
            delays.append(delay)
        
        # Verify delays increase exponentially
        assert delays[0] == 1.0
        assert delays[1] == 2.0
        assert delays[2] == 4.0
        assert delays[3] == 8.0
        assert delays[4] == 16.0


class TestSystemIntegration:
    """Test overall system integration scenarios."""

    def test_post_processing_pipeline(self):
        """Test a complete post processing pipeline."""
        # Create multiple posts
        posts = []
        for i in range(5):
            metrics = PostMetrics(likes=10*i, comments=2*i, shares=i, views=100*i)
            post = Post(
                urn=f"urn:li:activity:{1000+i}",
                author=f"User {i}",
                content=f"Test post {i} with #test{i}",
                posted_at=datetime.now(timezone.utc).replace(tzinfo=None),
                url=f"https://linkedin.com/posts/test-{i}",
                metrics=metrics,
                hashtags=[f"test{i}"],
                mentions=[],
                media_urls=[],
                is_promoted=False
            )
            posts.append(post)
        
        # Process posts (simulate filtering, sorting, etc.)
        high_engagement_posts = [
            post for post in posts 
            if post.get_engagement_rate() > 5.0
        ]
        
        # Sort by engagement
        high_engagement_posts.sort(
            key=lambda p: p.get_engagement_rate(), 
            reverse=True
        )
        
        # Verify results
        assert len(high_engagement_posts) == 3  # Posts 2, 3, 4 have >5% engagement
        assert high_engagement_posts[0].urn == "urn:li:activity:1004"  # Highest engagement

    def test_error_handling_integration(self):
        """Test error handling across modules."""
        # Test model validation errors
        with pytest.raises(ValueError, match="Invalid URN format"):
            Post(
                urn="invalid-urn",
                author="Test",
                content="Test",
                posted_at=datetime.now(timezone.utc).replace(tzinfo=None),
                url="https://linkedin.com/posts/test"
            )
        
        # Test future datetime validation
        future_date = datetime.now(timezone.utc).replace(tzinfo=None)
        future_date = future_date.replace(year=future_date.year + 1)
        
        with pytest.raises(ValueError, match="Datetime cannot be in the future"):
            Post(
                urn="urn:li:activity:123",
                author="Test",
                content="Test",
                posted_at=future_date,
                url="https://linkedin.com/posts/test"
            )

    def test_configuration_integration(self):
        """Test configuration handling across modules."""
        # Test retry configuration
        config = RetryConfig(
            max_retries=5,
            base_delay=0.5,
            max_delay=30.0,
            backoff_factor=2.0,
            jitter=True
        )
        
        assert config.max_retries == 5
        assert config.base_delay == 0.5
        assert config.max_delay == 30.0
        assert config.backoff_factor == 2.0
        assert config.jitter is True

    def test_data_consistency(self):
        """Test data consistency across operations."""
        # Create a post
        original_post = Post(
            urn="urn:li:activity:123",
            author="Test Author",
            content="Original content",
            posted_at=datetime.now(timezone.utc).replace(tzinfo=None),
            url="https://linkedin.com/posts/test",
            metrics=PostMetrics(likes=50, comments=10, shares=2, views=500)
        )
        
        # Serialize and deserialize
        json_data = original_post.to_json_dict()
        
        # Simulate creating a new post from serialized data
        restored_post = Post(
            urn=json_data["urn"],
            author=json_data["author"],
            content=json_data["content"],
            posted_at=datetime.fromisoformat(json_data["posted_at"]),
            url=json_data["url"],
            metrics=PostMetrics(**json_data["metrics"]),
            hashtags=json_data.get("hashtags", []),
            mentions=json_data.get("mentions", []),
            media_urls=json_data.get("media_urls", []),
            is_promoted=json_data.get("is_promoted", False)
        )
        
        # Verify consistency
        assert restored_post.urn == original_post.urn
        assert restored_post.author == original_post.author
        assert restored_post.content == original_post.content
        assert restored_post.metrics.likes == original_post.metrics.likes
        assert restored_post.get_engagement_rate() == original_post.get_engagement_rate()


class TestPerformanceIntegration:
    """Test performance aspects of the system."""

    def test_bulk_post_processing(self):
        """Test processing large numbers of posts."""
        import time
        
        # Create 100 posts
        start_time = time.time()
        posts = []
        
        for i in range(100):
            post = Post(
                urn=f"urn:li:activity:{10000+i}",
                author=f"User{i}",
                content=f"Content {i} " * 10,  # Longer content
                posted_at=datetime.now(timezone.utc).replace(tzinfo=None),
                url=f"https://linkedin.com/posts/{i}",
                metrics=PostMetrics(likes=i*2, comments=i, shares=i//2, views=i*10)
            )
            posts.append(post)
        
        creation_time = time.time() - start_time
        
        # Process posts
        start_time = time.time()
        processed = []
        for post in posts:
            if post.get_engagement_rate() > 10.0:
                processed.append({
                    'urn': post.urn,
                    'engagement': post.get_engagement_rate(),
                    'json': post.to_json_dict()
                })
        
        processing_time = time.time() - start_time
        
        # Verify performance is reasonable
        assert creation_time < 5.0  # Should create 100 posts in under 5 seconds
        assert processing_time < 5.0  # Should process 100 posts in under 5 seconds
        assert len(processed) > 0  # Should have some high-engagement posts 