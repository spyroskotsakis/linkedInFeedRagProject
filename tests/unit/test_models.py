"""
Unit tests for Post and PostMetrics models.

Tests data validation, serialization, and business logic methods.
"""

import json
from datetime import datetime, timedelta
import pytest
from pydantic import ValidationError

from linkedin_feed_capture.models.post import Post, PostMetrics


class TestPostMetrics:
    """Test cases for PostMetrics model."""
    
    def test_valid_metrics(self):
        """Test creating valid metrics."""
        metrics = PostMetrics(likes=10, comments=5, shares=2, views=100)
        
        assert metrics.likes == 10
        assert metrics.comments == 5
        assert metrics.shares == 2
        assert metrics.views == 100
    
    def test_default_metrics(self):
        """Test default metric values."""
        metrics = PostMetrics()
        
        assert metrics.likes == 0
        assert metrics.comments == 0
        assert metrics.shares == 0
        assert metrics.views is None
    
    def test_negative_metrics_rejected(self):
        """Test that negative metrics are rejected."""
        with pytest.raises(ValidationError):
            PostMetrics(likes=-1)
        
        with pytest.raises(ValidationError):
            PostMetrics(comments=-5)
        
        with pytest.raises(ValidationError):
            PostMetrics(shares=-2)
        
        with pytest.raises(ValidationError):
            PostMetrics(views=-10)


class TestPost:
    """Test cases for Post model."""
    
    @pytest.fixture
    def valid_post_data(self):
        """Fixture providing valid post data."""
        return {
            "urn": "urn:li:activity:1234567890",
            "author": "John Doe",
            "content": "This is a test post content.",
            "posted_at": datetime(2024, 1, 15, 10, 30, 0),
            "url": "https://linkedin.com/posts/activity-1234567890",
        }
    
    def test_minimal_valid_post(self, valid_post_data):
        """Test creating a post with minimal required fields."""
        post = Post(**valid_post_data)
        
        assert post.urn == "urn:li:activity:1234567890"
        assert post.author == "John Doe"
        assert post.content == "This is a test post content."
        assert post.url == "https://linkedin.com/posts/activity-1234567890"
        assert post.metrics.likes == 0  # Default metrics
        assert post.post_type == "text"  # Default type
        assert post.scraped_at is not None
    
    def test_complete_post(self):
        """Test creating a post with all fields."""
        metrics = PostMetrics(likes=42, comments=5, shares=2, views=1000)
        
        post = Post(
            urn="urn:li:activity:1234567890",
            author="Jane Smith",
            author_profile_url="https://linkedin.com/in/janesmith",
            content="Complete post with all fields #test @mention",
            posted_at=datetime(2024, 1, 15, 10, 30, 0),
            url="https://linkedin.com/posts/activity-1234567890",
            metrics=metrics,
            company_name="ACME Corp",
            job_title="Software Engineer",
            media_urls=["https://example.com/image.jpg"],
            hashtags=["test", "linkedin"],
            mentions=["mention"],
            post_type="image",
            language="en",
        )
        
        assert post.author == "Jane Smith"
        assert post.company_name == "ACME Corp"
        assert post.job_title == "Software Engineer"
        assert post.metrics.likes == 42
        assert post.has_media()
        assert post.is_company_post()
    
    def test_invalid_urn(self, valid_post_data):
        """Test that invalid URNs are rejected."""
        valid_post_data["urn"] = "invalid-urn"
        
        with pytest.raises(ValidationError, match="URN must start with 'urn:li:'"):
            Post(**valid_post_data)
    
    def test_empty_author(self, valid_post_data):
        """Test that empty author is rejected."""
        valid_post_data["author"] = ""
        
        with pytest.raises(ValidationError):
            Post(**valid_post_data)
    
    def test_invalid_url(self, valid_post_data):
        """Test that invalid URLs are rejected."""
        valid_post_data["url"] = "not-a-url"
        
        with pytest.raises(ValidationError, match="Invalid URL"):
            Post(**valid_post_data)
    
    def test_future_datetime(self, valid_post_data):
        """Test that future datetime is rejected."""
        future_date = datetime.now() + timedelta(days=1)
        valid_post_data["posted_at"] = future_date
        
        with pytest.raises(ValidationError, match="Datetime cannot be in the future"):
            Post(**valid_post_data)
    
    def test_hashtag_normalization(self, valid_post_data):
        """Test hashtag normalization and deduplication."""
        post = Post(**valid_post_data, hashtags=["#Python", "python", "AI", "#ai"])
        
        # Should normalize and deduplicate
        assert "python" in post.hashtags
        assert "ai" in post.hashtags
        assert len(post.hashtags) == 2  # Deduplicated
    
    def test_media_url_validation(self, valid_post_data):
        """Test media URL validation."""
        # Valid URLs should pass
        post = Post(**valid_post_data, media_urls=[
            "https://example.com/image.jpg",
            "http://test.com/video.mp4"
        ])
        assert len(post.media_urls) == 2
        
        # Invalid URLs should be rejected
        with pytest.raises(ValidationError, match="Invalid media URL"):
            Post(**valid_post_data, media_urls=["not-a-url"])
    
    def test_to_json_dict(self, valid_post_data):
        """Test JSON serialization."""
        post = Post(**valid_post_data)
        json_dict = post.to_json_dict()
        
        assert isinstance(json_dict, dict)
        assert json_dict["urn"] == post.urn
        assert json_dict["author"] == post.author
        assert "posted_at" in json_dict
        assert "scraped_at" in json_dict
        
        # Should be serializable to JSON
        json_str = json.dumps(json_dict)
        assert isinstance(json_str, str)
    
    def test_engagement_rate_calculation(self, valid_post_data):
        """Test engagement rate calculation."""
        # With views
        metrics = PostMetrics(likes=10, comments=5, shares=2, views=100)
        post = Post(**valid_post_data, metrics=metrics)
        
        # (10 + 5 + 2) / 100 = 0.17
        assert post.get_engagement_rate() == 0.17
        
        # Without views
        metrics_no_views = PostMetrics(likes=10, comments=5, shares=2)
        post_no_views = Post(**valid_post_data, metrics=metrics_no_views)
        
        assert post_no_views.get_engagement_rate() == 0.0
    
    def test_is_company_post(self, valid_post_data):
        """Test company post detection."""
        # Without company name
        post = Post(**valid_post_data)
        assert not post.is_company_post()
        
        # With company name
        post_with_company = Post(**valid_post_data, company_name="ACME Corp")
        assert post_with_company.is_company_post()
    
    def test_has_media(self, valid_post_data):
        """Test media detection."""
        # Without media
        post = Post(**valid_post_data)
        assert not post.has_media()
        
        # With media
        post_with_media = Post(**valid_post_data, media_urls=["https://example.com/image.jpg"])
        assert post_with_media.has_media()
    
    def test_string_representation(self, valid_post_data):
        """Test string representation."""
        post = Post(**valid_post_data)
        str_repr = str(post)
        
        assert post.author in str_repr
        assert post.content[:50] in str_repr  # Content preview
    
    def test_long_content_truncation(self, valid_post_data):
        """Test that very long content is handled properly."""
        # Content longer than 150 characters for string representation
        long_content = "A" * 200
        valid_post_data["content"] = long_content
        post = Post(**valid_post_data)
        
        str_repr = str(post)
        assert "..." in str_repr  # Should be truncated in string representation
        assert len(post.content) == 200  # But full content should be preserved 