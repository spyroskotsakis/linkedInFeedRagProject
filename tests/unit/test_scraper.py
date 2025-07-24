"""
Unit tests for scraper module.

Tests scroll management, post parsing, and data extraction.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from linkedin_feed_capture.scraper.scroll import ScrollManager, ScrollConfig
from linkedin_feed_capture.scraper.parser import PostParser, ParsingConfig
from linkedin_feed_capture.scraper.extractor import FeedExtractor, ExtractionConfig
from linkedin_feed_capture.models.post import Post, PostMetrics


class TestScrollConfig:
    """Test cases for ScrollConfig."""
    
    def test_default_config(self):
        """Test default scroll configuration."""
        config = ScrollConfig()
        
        assert config.scroll_pause_time == 2.0
        assert config.max_scrolls == 50
        assert config.scroll_increment == 1000
        assert config.duplicate_threshold == 5
        assert config.no_new_posts_threshold == 3
        assert config.min_posts_per_scroll == 1
        assert config.max_wait_time == 10.0
        assert config.scroll_randomness is True
        assert config.human_like_scrolling is True

    def test_custom_config(self):
        """Test custom scroll configuration."""
        config = ScrollConfig(
            scroll_pause_time=3.0,
            max_scrolls=100,
            scroll_increment=500,
            duplicate_threshold=10
        )
        
        assert config.scroll_pause_time == 3.0
        assert config.max_scrolls == 100
        assert config.scroll_increment == 500
        assert config.duplicate_threshold == 10


class TestScrollManager:
    """Test cases for ScrollManager."""
    
    def test_init(self):
        """Test scroll manager initialization."""
        mock_driver = Mock()
        config = ScrollConfig()
        manager = ScrollManager(mock_driver, config)
        
        assert manager.driver == mock_driver
        assert manager.config == config
        assert manager.logger is not None
        assert manager.seen_posts == set()
        assert manager.scroll_count == 0
        assert manager.consecutive_no_new_posts == 0
    
    @patch('linkedin_feed_capture.scraper.scroll.time.sleep')
    def test_scroll_page_basic(self, mock_sleep):
        """Test basic page scrolling."""
        mock_driver = Mock()
        manager = ScrollManager(mock_driver)
        
        manager.scroll_page()
        
        mock_driver.execute_script.assert_called()
        mock_sleep.assert_called()
    
    @patch('linkedin_feed_capture.scraper.scroll.time.sleep')
    def test_scroll_page_with_randomness(self, mock_sleep):
        """Test page scrolling with randomness enabled."""
        mock_driver = Mock()
        config = ScrollConfig(scroll_randomness=True)
        manager = ScrollManager(mock_driver, config)
        
        manager.scroll_page()
        
        # Should execute scroll script
        mock_driver.execute_script.assert_called()
        mock_sleep.assert_called()
    
    def test_is_at_bottom_true(self):
        """Test detection when at bottom of page."""
        mock_driver = Mock()
        mock_driver.execute_script.return_value = True
        
        manager = ScrollManager(mock_driver)
        result = manager.is_at_bottom()
        
        assert result is True
    
    def test_is_at_bottom_false(self):
        """Test detection when not at bottom of page."""
        mock_driver = Mock()
        mock_driver.execute_script.return_value = False
        
        manager = ScrollManager(mock_driver)
        result = manager.is_at_bottom()
        
        assert result is False
    
    def test_extract_post_ids_from_page(self):
        """Test extracting post IDs from current page."""
        mock_driver = Mock()
        
        # Mock post elements
        mock_post1 = Mock()
        mock_post1.get_attribute.return_value = "urn:li:activity:123"
        mock_post2 = Mock()
        mock_post2.get_attribute.return_value = "urn:li:activity:456"
        
        mock_driver.find_elements.return_value = [mock_post1, mock_post2]
        
        manager = ScrollManager(mock_driver)
        post_ids = manager.extract_post_ids_from_page()
        
        assert len(post_ids) == 2
        assert "urn:li:activity:123" in post_ids
        assert "urn:li:activity:456" in post_ids
    
    def test_extract_post_ids_no_posts(self):
        """Test extracting post IDs when no posts found."""
        mock_driver = Mock()
        mock_driver.find_elements.return_value = []
        
        manager = ScrollManager(mock_driver)
        post_ids = manager.extract_post_ids_from_page()
        
        assert len(post_ids) == 0
    
    def test_should_continue_scrolling_max_scrolls(self):
        """Test scroll continuation check with max scrolls reached."""
        mock_driver = Mock()
        config = ScrollConfig(max_scrolls=5)
        manager = ScrollManager(mock_driver, config)
        manager.scroll_count = 5
        
        result = manager.should_continue_scrolling()
        
        assert result is False
    
    def test_should_continue_scrolling_at_bottom(self):
        """Test scroll continuation check when at bottom."""
        mock_driver = Mock()
        mock_driver.execute_script.return_value = True  # At bottom
        
        manager = ScrollManager(mock_driver)
        result = manager.should_continue_scrolling()
        
        assert result is False
    
    def test_should_continue_scrolling_too_many_no_new_posts(self):
        """Test scroll continuation check with too many consecutive no new posts."""
        mock_driver = Mock()
        mock_driver.execute_script.return_value = False  # Not at bottom
        
        config = ScrollConfig(no_new_posts_threshold=3)
        manager = ScrollManager(mock_driver, config)
        manager.consecutive_no_new_posts = 3
        
        result = manager.should_continue_scrolling()
        
        assert result is False
    
    def test_should_continue_scrolling_continue(self):
        """Test scroll continuation check when should continue."""
        mock_driver = Mock()
        mock_driver.execute_script.return_value = False  # Not at bottom
        
        manager = ScrollManager(mock_driver)
        manager.scroll_count = 2
        manager.consecutive_no_new_posts = 1
        
        result = manager.should_continue_scrolling()
        
        assert result is True
    
    def test_get_scroll_stats(self):
        """Test getting scroll statistics."""
        mock_driver = Mock()
        manager = ScrollManager(mock_driver)
        manager.scroll_count = 10
        manager.seen_posts = {"post1", "post2", "post3"}
        
        stats = manager.get_scroll_stats()
        
        assert stats["total_scrolls"] == 10
        assert stats["unique_posts_found"] == 3
        assert "scroll_efficiency" in stats


class TestParsingConfig:
    """Test cases for ParsingConfig."""
    
    def test_default_config(self):
        """Test default parsing configuration."""
        config = ParsingConfig()
        
        assert config.extract_images is True
        assert config.extract_videos is True
        assert config.extract_links is True
        assert config.extract_hashtags is True
        assert config.extract_mentions is True
        assert config.parse_reactions is True
        assert config.parse_comments is True
        assert config.max_content_length == 5000
        assert config.timeout == 30.0
        assert config.retry_attempts == 3

    def test_custom_config(self):
        """Test custom parsing configuration."""
        config = ParsingConfig(
            extract_images=False,
            extract_videos=False,
            max_content_length=10000,
            timeout=60.0
        )
        
        assert config.extract_images is False
        assert config.extract_videos is False
        assert config.max_content_length == 10000
        assert config.timeout == 60.0


class TestPostParser:
    """Test cases for PostParser."""
    
    def test_init(self):
        """Test post parser initialization."""
        mock_driver = Mock()
        config = ParsingConfig()
        parser = PostParser(mock_driver, config)
        
        assert parser.driver == mock_driver
        assert parser.config == config
        assert parser.logger is not None
    
    @patch('linkedin_feed_capture.scraper.parser.WebDriverWait')
    def test_parse_post_success(self, mock_wait):
        """Test successful post parsing."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        # Mock post element
        mock_post_element = Mock()
        
        # Mock sub-elements
        mock_author_element = Mock()
        mock_author_element.text = "John Doe"
        mock_content_element = Mock()
        mock_content_element.text = "This is a test post #test"
        mock_time_element = Mock()
        mock_time_element.get_attribute.return_value = "2024-01-01T12:00:00.000Z"
        
        mock_post_element.find_element.side_effect = [
            mock_author_element,
            mock_content_element,
            mock_time_element
        ]
        
        # Mock metrics
        mock_likes = Mock()
        mock_likes.text = "10 likes"
        mock_comments = Mock()
        mock_comments.text = "5 comments"
        
        mock_post_element.find_elements.side_effect = [
            [mock_likes],  # Like elements
            [mock_comments],  # Comment elements
            [],  # Share elements
            []   # Media elements
        ]
        
        post_urn = "urn:li:activity:123"
        result = parser.parse_post(mock_post_element, post_urn)
        
        assert result is not None
        assert result.urn == post_urn
        assert result.author == "John Doe"
        assert "test post" in result.content
        assert "#test" in result.hashtags
    
    def test_parse_post_missing_element(self):
        """Test post parsing with missing required element."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        mock_post_element.find_element.side_effect = NoSuchElementException()
        
        post_urn = "urn:li:activity:123"
        result = parser.parse_post(mock_post_element, post_urn)
        
        assert result is None
    
    def test_extract_author_success(self):
        """Test successful author extraction."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        mock_author_element = Mock()
        mock_author_element.text = "Jane Smith"
        mock_post_element.find_element.return_value = mock_author_element
        
        author = parser._extract_author(mock_post_element)
        
        assert author == "Jane Smith"
    
    def test_extract_author_not_found(self):
        """Test author extraction when element not found."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        mock_post_element.find_element.side_effect = NoSuchElementException()
        
        author = parser._extract_author(mock_post_element)
        
        assert author == "Unknown"
    
    def test_extract_content_success(self):
        """Test successful content extraction."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        mock_content_element = Mock()
        mock_content_element.text = "This is test content with #hashtag and @mention"
        mock_post_element.find_element.return_value = mock_content_element
        
        content = parser._extract_content(mock_post_element)
        
        assert content == "This is test content with #hashtag and @mention"
    
    def test_extract_content_truncated(self):
        """Test content extraction with truncation."""
        mock_driver = Mock()
        config = ParsingConfig(max_content_length=10)
        parser = PostParser(mock_driver, config)
        
        mock_post_element = Mock()
        mock_content_element = Mock()
        mock_content_element.text = "This is a very long content that should be truncated"
        mock_post_element.find_element.return_value = mock_content_element
        
        content = parser._extract_content(mock_post_element)
        
        assert len(content) <= 10
        assert content.endswith("...")
    
    def test_extract_timestamp_success(self):
        """Test successful timestamp extraction."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        mock_time_element = Mock()
        mock_time_element.get_attribute.return_value = "2024-01-01T12:00:00.000Z"
        mock_post_element.find_element.return_value = mock_time_element
        
        timestamp = parser._extract_timestamp(mock_post_element)
        
        assert isinstance(timestamp, datetime)
        assert timestamp.year == 2024
        assert timestamp.month == 1
        assert timestamp.day == 1
    
    def test_extract_metrics_success(self):
        """Test successful metrics extraction."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        
        # Mock metric elements
        mock_likes = Mock()
        mock_likes.text = "15 reactions"
        mock_comments = Mock()
        mock_comments.text = "3 comments"
        mock_shares = Mock()
        mock_shares.text = "2 reposts"
        
        mock_post_element.find_elements.side_effect = [
            [mock_likes],     # Reactions
            [mock_comments],  # Comments
            [mock_shares]     # Shares
        ]
        
        metrics = parser._extract_metrics(mock_post_element)
        
        assert metrics.likes == 15
        assert metrics.comments == 3
        assert metrics.shares == 2
    
    def test_extract_metrics_no_elements(self):
        """Test metrics extraction when no elements found."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        mock_post_element = Mock()
        mock_post_element.find_elements.return_value = []
        
        metrics = parser._extract_metrics(mock_post_element)
        
        assert metrics.likes == 0
        assert metrics.comments == 0
        assert metrics.shares == 0
    
    def test_extract_hashtags(self):
        """Test hashtag extraction from text."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        text = "This is a post with #test #hashtag and #example tags"
        hashtags = parser._extract_hashtags(text)
        
        assert len(hashtags) == 3
        assert "test" in hashtags
        assert "hashtag" in hashtags
        assert "example" in hashtags
    
    def test_extract_hashtags_no_hashtags(self):
        """Test hashtag extraction with no hashtags."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        text = "This is a post with no hashtags"
        hashtags = parser._extract_hashtags(text)
        
        assert len(hashtags) == 0
    
    def test_extract_mentions(self):
        """Test mention extraction from text."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        text = "Thanks to @johndoe and @janesmith for the collaboration"
        mentions = parser._extract_mentions(text)
        
        assert len(mentions) == 2
        assert "johndoe" in mentions
        assert "janesmith" in mentions
    
    def test_extract_mentions_no_mentions(self):
        """Test mention extraction with no mentions."""
        mock_driver = Mock()
        parser = PostParser(mock_driver)
        
        text = "This is a post with no mentions"
        mentions = parser._extract_mentions(text)
        
        assert len(mentions) == 0


class TestExtractionConfig:
    """Test cases for ExtractionConfig."""
    
    def test_default_config(self):
        """Test default extraction configuration."""
        config = ExtractionConfig()
        
        assert config.max_posts == 100
        assert config.include_promoted is False
        assert config.min_engagement == 0
        assert config.date_range is None
        assert config.content_filters == []
        assert config.author_filters == []
        assert config.save_screenshots is False
        assert config.output_format == "json"

    def test_custom_config(self):
        """Test custom extraction configuration."""
        config = ExtractionConfig(
            max_posts=500,
            include_promoted=True,
            min_engagement=10,
            save_screenshots=True,
            output_format="csv"
        )
        
        assert config.max_posts == 500
        assert config.include_promoted is True
        assert config.min_engagement == 10
        assert config.save_screenshots is True
        assert config.output_format == "csv"


class TestFeedExtractor:
    """Test cases for FeedExtractor."""
    
    def test_init(self):
        """Test feed extractor initialization."""
        mock_driver = Mock()
        config = ExtractionConfig()
        extractor = FeedExtractor(mock_driver, config)
        
        assert extractor.driver == mock_driver
        assert extractor.config == config
        assert extractor.logger is not None
        assert isinstance(extractor.scroll_manager, ScrollManager)
        assert isinstance(extractor.post_parser, PostParser)
    
    @patch('linkedin_feed_capture.scraper.extractor.time.time')
    def test_extract_posts_success(self, mock_time):
        """Test successful post extraction."""
        mock_time.side_effect = [0, 10]  # 10 second duration
        
        mock_driver = Mock()
        config = ExtractionConfig(max_posts=2)
        extractor = FeedExtractor(mock_driver, config)
        
        # Mock scroll manager
        extractor.scroll_manager.should_continue_scrolling.side_effect = [True, False]
        extractor.scroll_manager.extract_post_ids_from_page.side_effect = [
            ["urn:li:activity:123", "urn:li:activity:456"],
            []
        ]
        extractor.scroll_manager.get_scroll_stats.return_value = {
            "total_scrolls": 1,
            "unique_posts_found": 2,
            "scroll_efficiency": 2.0
        }
        
        # Mock post parser
        mock_post1 = Mock(spec=Post)
        mock_post1.urn = "urn:li:activity:123"
        mock_post2 = Mock(spec=Post)
        mock_post2.urn = "urn:li:activity:456"
        
        extractor.post_parser.parse_post.side_effect = [mock_post1, mock_post2]
        
        # Mock driver elements
        mock_elements = [Mock(), Mock()]
        mock_driver.find_elements.return_value = mock_elements
        
        result = extractor.extract_posts()
        
        assert result["success"] is True
        assert len(result["posts"]) == 2
        assert result["stats"]["total_posts"] == 2
        assert result["stats"]["extraction_time"] == 10
    
    def test_extract_posts_max_posts_limit(self):
        """Test extraction with max posts limit."""
        mock_driver = Mock()
        config = ExtractionConfig(max_posts=1)
        extractor = FeedExtractor(mock_driver, config)
        
        # Mock successful extraction of one post
        extractor.scroll_manager.should_continue_scrolling.return_value = True
        extractor.scroll_manager.extract_post_ids_from_page.return_value = ["urn:li:activity:123"]
        
        mock_post = Mock(spec=Post)
        mock_post.urn = "urn:li:activity:123"
        extractor.post_parser.parse_post.return_value = mock_post
        
        mock_elements = [Mock()]
        mock_driver.find_elements.return_value = mock_elements
        
        with patch('linkedin_feed_capture.scraper.extractor.time.time', side_effect=[0, 5]):
            result = extractor.extract_posts()
        
        assert result["success"] is True
        assert len(result["posts"]) == 1
    
    def test_should_include_post_promoted_excluded(self):
        """Test post inclusion check with promoted posts excluded."""
        mock_driver = Mock()
        config = ExtractionConfig(include_promoted=False)
        extractor = FeedExtractor(mock_driver, config)
        
        mock_post = Mock(spec=Post)
        mock_post.is_promoted = True
        
        result = extractor._should_include_post(mock_post)
        
        assert result is False
    
    def test_should_include_post_low_engagement(self):
        """Test post inclusion check with low engagement."""
        mock_driver = Mock()
        config = ExtractionConfig(min_engagement=10)
        extractor = FeedExtractor(mock_driver, config)
        
        mock_post = Mock(spec=Post)
        mock_post.is_promoted = False
        mock_post.get_engagement_rate.return_value = 5.0
        
        result = extractor._should_include_post(mock_post)
        
        assert result is False
    
    def test_should_include_post_valid(self):
        """Test post inclusion check with valid post."""
        mock_driver = Mock()
        config = ExtractionConfig(min_engagement=5)
        extractor = FeedExtractor(mock_driver, config)
        
        mock_post = Mock(spec=Post)
        mock_post.is_promoted = False
        mock_post.get_engagement_rate.return_value = 10.0
        
        result = extractor._should_include_post(mock_post)
        
        assert result is True
    
    def test_save_screenshot(self):
        """Test screenshot saving functionality."""
        mock_driver = Mock()
        config = ExtractionConfig(save_screenshots=True)
        extractor = FeedExtractor(mock_driver, config)
        
        mock_post = Mock(spec=Post)
        mock_post.urn = "urn:li:activity:123"
        
        with patch('pathlib.Path.mkdir'), \
             patch('pathlib.Path.exists', return_value=False):
            
            extractor._save_screenshot(mock_post)
            
            mock_driver.save_screenshot.assert_called_once()
    
    def test_get_extraction_summary(self):
        """Test extraction summary generation."""
        mock_driver = Mock()
        extractor = FeedExtractor(mock_driver)
        
        posts = [Mock(spec=Post) for _ in range(5)]
        stats = {
            "total_scrolls": 10,
            "unique_posts_found": 5,
            "scroll_efficiency": 0.5,
            "extraction_time": 30.0
        }
        
        summary = extractor._get_extraction_summary(posts, stats)
        
        assert summary["total_posts"] == 5
        assert summary["extraction_time"] == 30.0
        assert summary["average_posts_per_scroll"] == 0.5
        assert summary["posts_per_minute"] == 10.0 