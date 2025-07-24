"""
Main feed extraction orchestrator for LinkedIn feed capture.

Coordinates scrolling, parsing, and data extraction to provide a complete
feed capture solution with comprehensive error handling and progress tracking.
"""

import time
from dataclasses import dataclass
from typing import List, Optional, Iterator, Dict, Any

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from linkedin_feed_capture.models.post import Post
from linkedin_feed_capture.scraper.scroll import ScrollManager, ScrollConfig
from linkedin_feed_capture.scraper.parser import PostParser, ParsingConfig
from linkedin_feed_capture.browser.stealth import is_likely_detected, add_human_delay
from linkedin_feed_capture.utils.logger import get_logger, LoggerMixin
from linkedin_feed_capture.utils.backoff import with_retries, RetryConfig, AntiDetectionError

logger = get_logger(__name__)


class ExtractionError(Exception):
    """Base exception for extraction errors."""
    pass


class InsufficientPostsError(ExtractionError):
    """Error when insufficient posts are extracted."""
    pass


@dataclass
class ExtractionConfig:
    """Configuration for feed extraction."""
    
    target_posts: int = 50
    post_selector: str = '[data-id^="urn:li:activity"]'
    extraction_timeout: int = 300  # 5 minutes
    batch_size: int = 10  # Process posts in batches
    deduplicate_posts: bool = True
    include_sponsored: bool = False
    max_extraction_attempts: int = 3
    progress_callback: Optional[callable] = None
    
    # Scroll configuration
    scroll_config: Optional[ScrollConfig] = None
    
    # Parsing configuration  
    parsing_config: Optional[ParsingConfig] = None


class ExtractionStats:
    """Statistics tracking for extraction process."""
    
    def __init__(self):
        self.start_time = time.time()
        self.end_time: Optional[float] = None
        self.posts_discovered = 0
        self.posts_parsed = 0
        self.posts_failed = 0
        self.scroll_attempts = 0
        self.detection_events = 0
        self.errors: List[Dict[str, Any]] = []
    
    def add_error(self, error: Exception, context: str = ""):
        """Add an error to the stats."""
        self.errors.append({
            "type": type(error).__name__,
            "message": str(error),
            "context": context,
            "timestamp": time.time(),
        })
    
    def complete(self):
        """Mark extraction as completed."""
        self.end_time = time.time()
    
    def get_duration(self) -> float:
        """Get extraction duration in seconds."""
        end_time = self.end_time or time.time()
        return end_time - self.start_time
    
    def get_success_rate(self) -> float:
        """Get parsing success rate."""
        total_attempts = self.posts_parsed + self.posts_failed
        if total_attempts == 0:
            return 0.0
        return self.posts_parsed / total_attempts
    
    def get_summary(self) -> Dict[str, Any]:
        """Get extraction statistics summary."""
        return {
            "duration_seconds": round(self.get_duration(), 2),
            "posts_discovered": self.posts_discovered,
            "posts_parsed": self.posts_parsed,
            "posts_failed": self.posts_failed,
            "scroll_attempts": self.scroll_attempts,
            "detection_events": self.detection_events,
            "success_rate": round(self.get_success_rate() * 100, 2),
            "posts_per_second": round(self.posts_parsed / max(1, self.get_duration()), 2),
            "errors": len(self.errors),
        }


class FeedExtractor(LoggerMixin):
    """Main orchestrator for LinkedIn feed extraction."""
    
    def __init__(self, config: Optional[ExtractionConfig] = None):
        """
        Initialize feed extractor.
        
        Args:
            config: Extraction configuration
        """
        self.config = config or ExtractionConfig()
        
        # Initialize components
        self.scroll_manager = ScrollManager(
            config=self.config.scroll_config or ScrollConfig()
        )
        self.post_parser = PostParser(
            config=self.config.parsing_config or ParsingConfig()
        )
        
        # State tracking
        self.stats = ExtractionStats()
        self.extracted_posts: List[Post] = []
        self.seen_urns: set = set()
    
    def extract_feed(
        self,
        driver: webdriver.Chrome,
        target_posts: Optional[int] = None,
    ) -> List[Post]:
        """
        Extract posts from LinkedIn feed.
        
        Args:
            driver: Chrome WebDriver instance
            target_posts: Number of posts to extract (overrides config)
            
        Returns:
            List of extracted Post objects
            
        Raises:
            ExtractionError: If extraction fails
        """
        target_posts = target_posts or self.config.target_posts
        
        self.logger.info(
            "Starting LinkedIn feed extraction",
            target_posts=target_posts,
            post_selector=self.config.post_selector,
            timeout=self.config.extraction_timeout,
        )
        
        # Reset state
        self.stats = ExtractionStats()
        self.extracted_posts.clear()
        self.seen_urns.clear()
        
        start_time = time.time()
        
        try:
            # Phase 1: Discover posts through scrolling
            discovered_urns = self._discover_posts(driver, target_posts)
            self.stats.posts_discovered = len(discovered_urns)
            
            # Phase 2: Extract and parse discovered posts
            posts = self._extract_posts(driver, discovered_urns)
            self.extracted_posts = posts
            
            # Phase 3: Post-processing
            if self.config.deduplicate_posts:
                posts = self._deduplicate_posts(posts)
            
            if not self.config.include_sponsored:
                posts = self._filter_sponsored_posts(posts)
            
            self.stats.complete()
            
            self.logger.info(
                "Feed extraction completed successfully",
                **self.stats.get_summary(),
                final_post_count=len(posts),
            )
            
            return posts
            
        except Exception as e:
            self.stats.add_error(e, "main_extraction")
            self.stats.complete()
            
            self.logger.error(
                "Feed extraction failed",
                error=str(e),
                error_type=type(e).__name__,
                **self.stats.get_summary(),
            )
            raise ExtractionError(f"Feed extraction failed: {e}") from e
    
    def extract_feed_streaming(
        self,
        driver: webdriver.Chrome,
        target_posts: Optional[int] = None,
    ) -> Iterator[Post]:
        """
        Extract posts from LinkedIn feed with streaming output.
        
        Args:
            driver: Chrome WebDriver instance
            target_posts: Number of posts to extract
            
        Yields:
            Post objects as they are parsed
        """
        target_posts = target_posts or self.config.target_posts
        
        self.logger.info(
            "Starting streaming LinkedIn feed extraction",
            target_posts=target_posts,
        )
        
        # Reset state
        self.stats = ExtractionStats()
        self.extracted_posts.clear()
        self.seen_urns.clear()
        
        try:
            # Scroll and parse incrementally
            scroll_manager = ScrollManager(self.config.scroll_config or ScrollConfig())
            
            # Start scrolling to discover posts
            while len(self.extracted_posts) < target_posts:
                # Check for detection
                if is_likely_detected(driver):
                    self.stats.detection_events += 1
                    raise AntiDetectionError("Bot detection triggered during streaming extraction")
                
                # Discover new posts on current page
                current_post_elements = driver.find_elements(
                    By.CSS_SELECTOR, 
                    self.config.post_selector
                )
                
                # Parse new posts
                new_posts = []
                for element in current_post_elements:
                    try:
                        urn = element.get_attribute("data-id")
                        if urn and urn not in self.seen_urns:
                            post = self.post_parser.parse_post_element(driver, element)
                            if post:
                                self.seen_urns.add(urn)
                                new_posts.append(post)
                                self.extracted_posts.append(post)
                                self.stats.posts_parsed += 1
                                
                                # Call progress callback if provided
                                if self.config.progress_callback:
                                    self.config.progress_callback(post, len(self.extracted_posts), target_posts)
                                
                                yield post
                            else:
                                self.stats.posts_failed += 1
                    except Exception as e:
                        self.stats.posts_failed += 1
                        self.logger.debug("Failed to parse post during streaming", error=str(e))
                
                # If no new posts found, scroll to discover more
                if not new_posts:
                    scroll_manager._perform_intelligent_scroll(driver)
                    self.stats.scroll_attempts += 1
                    add_human_delay(1.0)
                
                # Check timeout
                if time.time() - self.stats.start_time > self.config.extraction_timeout:
                    self.logger.warning("Extraction timeout reached during streaming")
                    break
            
            self.stats.complete()
            
        except Exception as e:
            self.stats.add_error(e, "streaming_extraction")
            self.stats.complete()
            raise ExtractionError(f"Streaming extraction failed: {e}") from e
    
    def _discover_posts(self, driver: webdriver.Chrome, target_posts: int) -> List[str]:
        """Discover post URNs through scrolling."""
        self.logger.info("Starting post discovery phase", target_posts=target_posts)
        
        discovered_urns = self.scroll_manager.scroll_to_discover_posts(
            driver=driver,
            target_posts=target_posts,
            post_selector=self.config.post_selector,
        )
        
        self.stats.scroll_attempts = self.scroll_manager.scroll_count
        
        self.logger.info(
            "Post discovery completed",
            discovered_posts=len(discovered_urns),
            scroll_attempts=self.stats.scroll_attempts,
        )
        
        return discovered_urns
    
    def _extract_posts(self, driver: webdriver.Chrome, urns: List[str]) -> List[Post]:
        """Extract and parse posts from discovered URNs."""
        self.logger.info("Starting post extraction phase", total_urns=len(urns))
        
        posts = []
        batch_start = 0
        
        while batch_start < len(urns):
            batch_end = min(batch_start + self.config.batch_size, len(urns))
            batch_urns = urns[batch_start:batch_end]
            
            self.logger.debug(
                "Processing batch",
                batch_start=batch_start,
                batch_end=batch_end,
                batch_size=len(batch_urns),
            )
            
            # Find elements for this batch
            batch_elements = []
            for urn in batch_urns:
                try:
                    element = driver.find_element(
                        By.CSS_SELECTOR,
                        f'[data-id="{urn}"]'
                    )
                    batch_elements.append(element)
                except Exception as e:
                    self.logger.debug(
                        "Failed to find element for URN",
                        urn=urn,
                        error=str(e),
                    )
                    self.stats.posts_failed += 1
            
            # Parse batch
            if batch_elements:
                batch_posts = self.post_parser.parse_multiple_posts(driver, batch_elements)
                posts.extend(batch_posts)
                self.stats.posts_parsed += len(batch_posts)
                
                # Call progress callback if provided
                if self.config.progress_callback:
                    for post in batch_posts:
                        self.config.progress_callback(post, len(posts), len(urns))
            
            batch_start = batch_end
            
            # Small delay between batches
            add_human_delay(0.5)
        
        self.logger.info(
            "Post extraction completed",
            extracted_posts=len(posts),
            success_rate=round(len(posts) / len(urns) * 100, 1) if urns else 0,
        )
        
        return posts
    
    def _deduplicate_posts(self, posts: List[Post]) -> List[Post]:
        """Remove duplicate posts based on URN."""
        seen_urns = set()
        deduplicated = []
        
        for post in posts:
            if post.urn not in seen_urns:
                seen_urns.add(post.urn)
                deduplicated.append(post)
        
        removed_count = len(posts) - len(deduplicated)
        if removed_count > 0:
            self.logger.info(
                "Removed duplicate posts",
                removed_count=removed_count,
                unique_posts=len(deduplicated),
            )
        
        return deduplicated
    
    def _filter_sponsored_posts(self, posts: List[Post]) -> List[Post]:
        """Filter out sponsored/promoted posts."""
        filtered = []
        
        for post in posts:
            # Simple heuristic - check for sponsored indicators in content
            is_sponsored = any(
                indicator in post.content.lower()
                for indicator in ["promoted", "sponsored", "ad •"]
            )
            
            if not is_sponsored:
                filtered.append(post)
        
        removed_count = len(posts) - len(filtered)
        if removed_count > 0:
            self.logger.info(
                "Filtered sponsored posts",
                removed_count=removed_count,
                remaining_posts=len(filtered),
            )
        
        return filtered
    
    def get_extraction_stats(self) -> Dict[str, Any]:
        """Get current extraction statistics."""
        return self.stats.get_summary()
    
    def get_extracted_posts(self) -> List[Post]:
        """Get all extracted posts."""
        return self.extracted_posts.copy()
    
    def clear_extracted_posts(self) -> None:
        """Clear extracted posts from memory."""
        self.extracted_posts.clear()
        self.seen_urns.clear()


def extract_linkedin_feed(
    driver: webdriver.Chrome,
    target_posts: int = 50,
    config: Optional[ExtractionConfig] = None,
) -> List[Post]:
    """
    Convenience function for extracting LinkedIn feed posts.
    
    Args:
        driver: Chrome WebDriver instance
        target_posts: Number of posts to extract
        config: Optional extraction configuration
        
    Returns:
        List of extracted Post objects
    """
    if config is None:
        config = ExtractionConfig(target_posts=target_posts)
    else:
        config.target_posts = target_posts
    
    extractor = FeedExtractor(config)
    return extractor.extract_feed(driver, target_posts) 