"""
Intelligent scrolling manager for LinkedIn feed navigation.

Implements human-like scrolling patterns with anti-detection measures
and dynamic post discovery for efficient feed processing.
"""

import random
import time
from dataclasses import dataclass
from typing import List, Set, Tuple, Optional

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from linkedin_feed_capture.browser.stealth import (
    simulate_human_scroll,
    simulate_mouse_movement,
    add_human_delay,
    is_likely_detected
)
from linkedin_feed_capture.utils.logger import get_logger, LoggerMixin
from linkedin_feed_capture.utils.backoff import with_retries, RetryConfig, RateLimitError

logger = get_logger(__name__)


class ScrollingError(Exception):
    """Base exception for scrolling errors."""
    pass


class PostDiscoveryError(ScrollingError):
    """Error when no new posts are discovered."""
    pass


class DetectionError(ScrollingError):
    """Error when anti-bot detection is triggered."""
    pass


@dataclass
class ScrollConfig:
    """Configuration for scrolling behavior."""
    
    base_delay: float = 2.0
    jitter_range: Tuple[float, float] = (0.5, 1.5)
    scroll_pixels_range: Tuple[int, int] = (300, 800)
    smooth_scroll: bool = True
    max_scroll_attempts: int = 100
    detection_check_frequency: int = 5  # Check every N scrolls
    mouse_movement_probability: float = 0.3
    reading_pause_probability: float = 0.4
    max_stale_scrolls: int = 10  # Max scrolls without new posts
    viewport_randomization: bool = True
    enable_intersection_observer: bool = True


class ScrollManager(LoggerMixin):
    """Manages intelligent scrolling for LinkedIn feed discovery."""
    
    def __init__(self, config: Optional[ScrollConfig] = None):
        """
        Initialize scroll manager.
        
        Args:
            config: Scrolling configuration
        """
        self.config = config or ScrollConfig()
        self.discovered_posts: Set[str] = set()
        self.scroll_count = 0
        self.stale_scroll_count = 0
        self.last_post_count = 0
        
    def scroll_to_discover_posts(
        self,
        driver: webdriver.Chrome,
        target_posts: int,
        post_selector: str = '[data-id^="urn:li:activity"]',
    ) -> List[str]:
        """
        Scroll through feed to discover post URNs.
        
        Args:
            driver: Chrome WebDriver instance
            target_posts: Number of posts to discover
            post_selector: CSS selector for post elements
            
        Returns:
            List of discovered post URNs
            
        Raises:
            ScrollingError: If scrolling fails
            DetectionError: If bot detection is triggered
        """
        self.logger.info(
            "Starting intelligent scrolling for post discovery",
            target_posts=target_posts,
            post_selector=post_selector,
        )
        
        # Reset state
        self.discovered_posts.clear()
        self.scroll_count = 0
        self.stale_scroll_count = 0
        self.last_post_count = 0
        
        # Initialize intersection observer if enabled
        if self.config.enable_intersection_observer:
            self._inject_intersection_observer(driver)
        
        try:
            while len(self.discovered_posts) < target_posts:
                # Check for detection periodically
                if self.scroll_count % self.config.detection_check_frequency == 0:
                    if is_likely_detected(driver):
                        raise DetectionError("Bot detection triggered during scrolling")
                
                # Discover current posts
                current_posts = self._discover_posts_on_page(driver, post_selector)
                new_posts = current_posts - self.discovered_posts
                
                if new_posts:
                    self.discovered_posts.update(new_posts)
                    self.stale_scroll_count = 0
                    
                    self.logger.info(
                        "Discovered new posts",
                        new_posts_count=len(new_posts),
                        total_discovered=len(self.discovered_posts),
                        target=target_posts,
                        progress_pct=round(len(self.discovered_posts) / target_posts * 100, 1),
                    )
                else:
                    self.stale_scroll_count += 1
                    
                    # Check if we're stuck
                    if self.stale_scroll_count >= self.config.max_stale_scrolls:
                        self.logger.warning(
                            "No new posts discovered after maximum stale scrolls",
                            stale_scrolls=self.stale_scroll_count,
                            total_discovered=len(self.discovered_posts),
                        )
                        break
                
                # Check scroll limit
                if self.scroll_count >= self.config.max_scroll_attempts:
                    self.logger.warning(
                        "Reached maximum scroll attempts",
                        scroll_attempts=self.scroll_count,
                        total_discovered=len(self.discovered_posts),
                    )
                    break
                
                # Exit if we have enough posts
                if len(self.discovered_posts) >= target_posts:
                    break
                
                # Perform intelligent scroll
                self._perform_intelligent_scroll(driver)
                self.scroll_count += 1
                
                # Occasional human behaviors
                self._maybe_perform_human_behavior(driver)
            
            discovered_urns = list(self.discovered_posts)
            
            self.logger.info(
                "Scrolling completed",
                total_posts_discovered=len(discovered_urns),
                target_posts=target_posts,
                scroll_attempts=self.scroll_count,
                success_rate=round(len(discovered_urns) / target_posts * 100, 1) if target_posts > 0 else 0,
            )
            
            return discovered_urns
            
        except Exception as e:
            self.logger.error(
                "Scrolling failed",
                error=str(e),
                error_type=type(e).__name__,
                scroll_count=self.scroll_count,
                posts_discovered=len(self.discovered_posts),
            )
            raise ScrollingError(f"Scrolling failed: {e}") from e
    
    def _discover_posts_on_page(
        self,
        driver: webdriver.Chrome,
        post_selector: str,
    ) -> Set[str]:
        """
        Discover post URNs currently visible on the page.
        
        Args:
            driver: Chrome WebDriver instance
            post_selector: CSS selector for post elements
            
        Returns:
            Set of post URNs found on current page
        """
        try:
            post_elements = driver.find_elements(By.CSS_SELECTOR, post_selector)
            urns = set()
            
            for element in post_elements:
                try:
                    urn = element.get_attribute("data-id")
                    if urn and urn.startswith("urn:li:"):
                        urns.add(urn)
                except StaleElementReferenceException:
                    # Element no longer in DOM, skip it
                    continue
                except Exception as e:
                    self.logger.debug(
                        "Failed to extract URN from element",
                        error=str(e),
                    )
                    continue
            
            return urns
            
        except Exception as e:
            self.logger.error(
                "Failed to discover posts on page",
                error=str(e),
                error_type=type(e).__name__,
            )
            return set()
    
    def _perform_intelligent_scroll(self, driver: webdriver.Chrome) -> None:
        """
        Perform an intelligent scroll with human-like characteristics.
        
        Args:
            driver: Chrome WebDriver instance
        """
        # Calculate scroll parameters
        scroll_pixels = random.randint(*self.config.scroll_pixels_range)
        pause_time = self.config.base_delay * random.uniform(*self.config.jitter_range)
        
        # Adjust based on current performance
        if self.stale_scroll_count > 0:
            # Increase scroll distance if we're not finding new posts
            scroll_pixels = int(scroll_pixels * (1 + self.stale_scroll_count * 0.1))
            pause_time *= 1.5  # Slow down when struggling
        
        # Perform scroll
        if self.config.smooth_scroll:
            self._smooth_scroll(driver, scroll_pixels)
        else:
            driver.execute_script(f"window.scrollBy(0, {scroll_pixels});")
        
        # Variable pause with human characteristics
        self._intelligent_pause(driver, pause_time)
        
        # Occasionally randomize viewport if enabled
        if self.config.viewport_randomization and random.random() < 0.05:  # 5% chance
            self._randomize_viewport(driver)
    
    def _smooth_scroll(self, driver: webdriver.Chrome, total_pixels: int) -> None:
        """
        Perform smooth scrolling in increments.
        
        Args:
            driver: Chrome WebDriver instance
            total_pixels: Total pixels to scroll
        """
        increments = random.randint(3, 8)
        pixels_per_increment = total_pixels // increments
        
        for i in range(increments):
            # Add some variation to each increment
            current_pixels = pixels_per_increment
            if i == increments - 1:  # Last increment gets remainder
                current_pixels = total_pixels - (pixels_per_increment * (increments - 1))
            
            # Add small random variation
            variation = random.randint(-20, 20)
            current_pixels = max(50, current_pixels + variation)
            
            driver.execute_script(f"window.scrollBy(0, {current_pixels});")
            time.sleep(random.uniform(0.05, 0.2))
    
    def _intelligent_pause(self, driver: webdriver.Chrome, base_pause: float) -> None:
        """
        Perform intelligent pause with reading simulation.
        
        Args:
            driver: Chrome WebDriver instance
            base_pause: Base pause time in seconds
        """
        # Check if we should simulate reading
        if random.random() < self.config.reading_pause_probability:
            # Simulate reading by checking visible content
            try:
                visible_posts = driver.find_elements(
                    By.CSS_SELECTOR,
                    '[data-id^="urn:li:activity"]:not([style*="display: none"])'
                )
                
                if visible_posts:
                    # Estimate reading time based on visible content
                    total_content_length = 0
                    for post in visible_posts[:3]:  # Check first 3 visible posts
                        try:
                            content = post.text
                            total_content_length += len(content)
                        except:
                            continue
                    
                    # Add reading time (assuming 200 WPM reading speed)
                    words = total_content_length / 5  # Rough words estimation
                    reading_time = (words / 200) * 60  # Convert to seconds
                    reading_time = min(reading_time, 5.0)  # Cap at 5 seconds
                    
                    base_pause += reading_time
                    
            except Exception as e:
                self.logger.debug("Failed to estimate reading time", error=str(e))
        
        # Apply final pause
        time.sleep(base_pause)
    
    def _maybe_perform_human_behavior(self, driver: webdriver.Chrome) -> None:
        """
        Occasionally perform human-like behaviors.
        
        Args:
            driver: Chrome WebDriver instance
        """
        # Random mouse movement
        if random.random() < self.config.mouse_movement_probability:
            try:
                simulate_mouse_movement(driver, randomize=True)
            except Exception as e:
                self.logger.debug("Failed to simulate mouse movement", error=str(e))
        
        # Occasional scroll up (like a human might do)
        if random.random() < 0.1:  # 10% chance
            scroll_up_pixels = random.randint(50, 200)
            driver.execute_script(f"window.scrollBy(0, -{scroll_up_pixels});")
            time.sleep(random.uniform(0.5, 1.0))
    
    def _randomize_viewport(self, driver: webdriver.Chrome) -> None:
        """
        Slightly randomize viewport size to avoid fingerprinting.
        
        Args:
            driver: Chrome WebDriver instance
        """
        try:
            current_size = driver.get_window_size()
            width = current_size['width']
            height = current_size['height']
            
            # Small random adjustments
            width_adj = random.randint(-20, 20)
            height_adj = random.randint(-20, 20)
            
            new_width = max(800, width + width_adj)
            new_height = max(600, height + height_adj)
            
            driver.set_window_size(new_width, new_height)
            
            self.logger.debug(
                "Randomized viewport",
                old_size=f"{width}x{height}",
                new_size=f"{new_width}x{new_height}",
            )
            
        except Exception as e:
            self.logger.debug("Failed to randomize viewport", error=str(e))
    
    def _inject_intersection_observer(self, driver: webdriver.Chrome) -> None:
        """
        Inject intersection observer for efficient post detection.
        
        Args:
            driver: Chrome WebDriver instance
        """
        try:
            script = """
            if (!window.linkedinPostObserver) {
                window.linkedinPostObserver = {
                    observedPosts: new Set(),
                    newPosts: new Set(),
                    
                    init: function() {
                        const observer = new IntersectionObserver((entries) => {
                            entries.forEach(entry => {
                                if (entry.isIntersecting) {
                                    const urn = entry.target.getAttribute('data-id');
                                    if (urn && !this.observedPosts.has(urn)) {
                                        this.observedPosts.add(urn);
                                        this.newPosts.add(urn);
                                    }
                                }
                            });
                        }, {
                            rootMargin: '100px 0px',
                            threshold: 0.1
                        });
                        
                        // Observe existing posts
                        document.querySelectorAll('[data-id^="urn:li:activity"]').forEach(post => {
                            observer.observe(post);
                        });
                        
                        // Observe future posts
                        const postObserver = new MutationObserver((mutations) => {
                            mutations.forEach(mutation => {
                                mutation.addedNodes.forEach(node => {
                                    if (node.nodeType === Node.ELEMENT_NODE) {
                                        const posts = node.querySelectorAll ? 
                                            node.querySelectorAll('[data-id^="urn:li:activity"]') : [];
                                        posts.forEach(post => observer.observe(post));
                                    }
                                });
                            });
                        });
                        
                        postObserver.observe(document.body, {
                            childList: true,
                            subtree: true
                        });
                        
                        this.observer = observer;
                        this.postObserver = postObserver;
                    },
                    
                    getNewPosts: function() {
                        const posts = Array.from(this.newPosts);
                        this.newPosts.clear();
                        return posts;
                    }
                };
                
                window.linkedinPostObserver.init();
            }
            """
            driver.execute_script(script)
            self.logger.debug("Intersection observer injected successfully")
            
        except Exception as e:
            self.logger.warning(
                "Failed to inject intersection observer",
                error=str(e),
            )
    
    def get_new_posts_from_observer(self, driver: webdriver.Chrome) -> List[str]:
        """
        Get new posts detected by intersection observer.
        
        Args:
            driver: Chrome WebDriver instance
            
        Returns:
            List of new post URNs
        """
        try:
            script = "return window.linkedinPostObserver ? window.linkedinPostObserver.getNewPosts() : [];"
            new_posts = driver.execute_script(script)
            return new_posts or []
        except Exception as e:
            self.logger.debug("Failed to get posts from observer", error=str(e))
            return []
    
    def get_scroll_statistics(self) -> dict:
        """Get statistics about the current scrolling session."""
        return {
            "total_scrolls": self.scroll_count,
            "posts_discovered": len(self.discovered_posts),
            "stale_scrolls": self.stale_scroll_count,
            "discovery_rate": len(self.discovered_posts) / max(1, self.scroll_count),
            "efficiency_score": min(100, (len(self.discovered_posts) / max(1, self.scroll_count)) * 100),
        } 