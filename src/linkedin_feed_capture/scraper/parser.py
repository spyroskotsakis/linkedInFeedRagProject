"""
LinkedIn post parser for extracting structured data from DOM elements.

Handles parsing of various post types and extracts comprehensive metadata
using BeautifulSoup and robust CSS selectors.
"""

import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup, Tag
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from linkedin_feed_capture.models.post import Post, PostMetrics
from linkedin_feed_capture.utils.logger import get_logger, LoggerMixin

logger = get_logger(__name__)


class ParsingError(Exception):
    """Base exception for parsing errors."""
    pass


class InvalidPostError(ParsingError):
    """Error for invalid or unparseable posts."""
    pass


@dataclass
class ParsingConfig:
    """Configuration for post parsing."""
    
    extract_media: bool = True
    extract_hashtags: bool = True
    extract_mentions: bool = True
    detect_language: bool = False
    include_comments: bool = False
    include_reactions: bool = True
    validate_urls: bool = True
    max_content_length: int = 10000
    timeout_per_post: float = 5.0


class PostParser(LoggerMixin):
    """Parses LinkedIn post elements into structured Post objects."""
    
    def __init__(self, config: Optional[ParsingConfig] = None):
        """
        Initialize post parser.
        
        Args:
            config: Parsing configuration
        """
        self.config = config or ParsingConfig()
        
        # Common CSS selectors for LinkedIn posts
        self.selectors = {
            'author_name': [
                '.feed-shared-actor__name',
                '.update-components-actor__name',
                '[data-control-name="actor_name"]',
                '.feed-shared-update-v2__actor-name',
            ],
            'author_profile': [
                '.feed-shared-actor__meta a',
                '.update-components-actor__meta a',
                '.feed-shared-update-v2__actor-meta a',
            ],
            'job_title': [
                '.feed-shared-actor__description',
                '.update-components-actor__description',
                '.feed-shared-update-v2__actor-description',
            ],
            'company_name': [
                '.feed-shared-actor__sub-description',
                '.update-components-actor__sub-description',
            ],
            'content': [
                '.feed-shared-update-v2__description',
                '.feed-shared-text',
                '.update-components-text',
                '[data-test-id="main-feed-activity-card__commentary"]',
            ],
            'timestamp': [
                '.feed-shared-actor__sub-description time',
                '.update-components-actor__sub-description time',
                'time[datetime]',
                '[data-test-id="feed-shared-actor__sub-description"] time',
            ],
            'post_url': [
                '.feed-shared-control-menu__trigger',
                'a[data-tracking-control-name="public_post_feed-object_title"]',
                '.update-components-header__timestamp a',
            ],
            'likes_count': [
                '.social-details-social-counts__reactions-count',
                '[data-test-id="social-counts-reactions"]',
                '.social-counts-reactions',
            ],
            'comments_count': [
                '.social-details-social-counts__comments',
                '[data-test-id="social-counts-comments"]',
                '.social-counts-comments',
            ],
            'shares_count': [
                '.social-details-social-counts__shares',
                '[data-test-id="social-counts-shares"]',
                '.social-counts-shares',
            ],
            'media_elements': [
                '.feed-shared-update-v2__content img',
                '.feed-shared-update-v2__content video',
                '.update-components-image img',
                '.update-components-video video',
            ],
        }
    
    def parse_post_element(
        self,
        driver: webdriver.Chrome,
        post_element: WebElement,
    ) -> Optional[Post]:
        """
        Parse a single post element into a Post object.
        
        Args:
            driver: Chrome WebDriver instance
            post_element: WebElement containing the post
            
        Returns:
            Parsed Post object or None if parsing fails
            
        Raises:
            ParsingError: If parsing fails critically
        """
        try:
            # Get URN first
            urn = self._extract_urn(post_element)
            if not urn:
                raise InvalidPostError("No URN found for post")
            
            self.logger.debug("Parsing post", urn=urn)
            
            # Get HTML content for BeautifulSoup parsing
            html_content = post_element.get_attribute("outerHTML")
            soup = BeautifulSoup(html_content, "lxml")
            
            # Extract all fields
            author = self._extract_author_name(soup)
            author_profile_url = self._extract_author_profile_url(soup, driver.current_url)
            content = self._extract_content(soup)
            posted_at = self._extract_timestamp(soup)
            url = self._extract_post_url(soup, driver.current_url)
            metrics = self._extract_metrics(soup)
            
            # Optional fields
            company_name = self._extract_company_name(soup) if author else None
            job_title = self._extract_job_title(soup)
            media_urls = self._extract_media_urls(soup, driver.current_url) if self.config.extract_media else []
            hashtags = self._extract_hashtags(content) if self.config.extract_hashtags else []
            mentions = self._extract_mentions(content) if self.config.extract_mentions else []
            post_type = self._detect_post_type(soup, media_urls)
            language = self._detect_language(content) if self.config.detect_language else None
            
            # Create Post object
            post = Post(
                urn=urn,
                author=author,
                author_profile_url=author_profile_url,
                content=content,
                posted_at=posted_at,
                url=url,
                metrics=metrics,
                company_name=company_name,
                job_title=job_title,
                media_urls=media_urls,
                hashtags=hashtags,
                mentions=mentions,
                post_type=post_type,
                language=language,
            )
            
            self.logger.debug(
                "Post parsed successfully",
                urn=urn,
                author=author,
                content_length=len(content),
                media_count=len(media_urls),
            )
            
            return post
            
        except InvalidPostError:
            self.logger.warning("Skipping invalid post", urn=urn if 'urn' in locals() else "unknown")
            return None
        except StaleElementReferenceException:
            self.logger.warning("Post element became stale during parsing")
            return None
        except Exception as e:
            self.logger.error(
                "Failed to parse post",
                error=str(e),
                error_type=type(e).__name__,
                urn=urn if 'urn' in locals() else "unknown",
            )
            raise ParsingError(f"Failed to parse post: {e}") from e
    
    def parse_multiple_posts(
        self,
        driver: webdriver.Chrome,
        post_elements: List[WebElement],
    ) -> List[Post]:
        """
        Parse multiple post elements.
        
        Args:
            driver: Chrome WebDriver instance
            post_elements: List of post WebElements
            
        Returns:
            List of successfully parsed Post objects
        """
        posts = []
        successful_parses = 0
        failed_parses = 0
        
        self.logger.info("Parsing multiple posts", total_elements=len(post_elements))
        
        for i, element in enumerate(post_elements):
            try:
                post = self.parse_post_element(driver, element)
                if post:
                    posts.append(post)
                    successful_parses += 1
                else:
                    failed_parses += 1
            except Exception as e:
                failed_parses += 1
                self.logger.warning(
                    "Failed to parse post element",
                    index=i,
                    error=str(e),
                )
        
        self.logger.info(
            "Batch parsing completed",
            successful=successful_parses,
            failed=failed_parses,
            success_rate=round(successful_parses / len(post_elements) * 100, 1) if post_elements else 0,
        )
        
        return posts
    
    def _extract_urn(self, element: WebElement) -> Optional[str]:
        """Extract URN from post element."""
        try:
            urn = element.get_attribute("data-id")
            if urn and urn.startswith("urn:li:"):
                return urn
        except Exception as e:
            self.logger.debug("Failed to extract URN", error=str(e))
        return None
    
    def _extract_author_name(self, soup: BeautifulSoup) -> str:
        """Extract author name from post."""
        for selector in self.selectors['author_name']:
            element = soup.select_one(selector)
            if element:
                name = element.get_text(strip=True)
                if name:
                    return name
        
        raise InvalidPostError("No author name found")
    
    def _extract_author_profile_url(self, soup: BeautifulSoup, base_url: str) -> Optional[str]:
        """Extract author profile URL."""
        for selector in self.selectors['author_profile']:
            element = soup.select_one(selector)
            if element and element.get('href'):
                url = element['href']
                # Convert relative URL to absolute
                if url.startswith('/'):
                    return urljoin(base_url, url)
                elif url.startswith('http'):
                    return url
        return None
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """Extract post content text."""
        for selector in self.selectors['content']:
            element = soup.select_one(selector)
            if element:
                # Get text and clean it up
                content = element.get_text(" ", strip=True)
                if content:
                    # Clean up common LinkedIn artifacts
                    content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
                    content = re.sub(r'…\s*see more$', '', content, flags=re.IGNORECASE)
                    content = content.strip()
                    
                    # Enforce length limit
                    if len(content) > self.config.max_content_length:
                        content = content[:self.config.max_content_length] + "..."
                    
                    return content
        
        # Try alternative method - get all text from post
        content = soup.get_text(" ", strip=True)
        if content:
            content = re.sub(r'\s+', ' ', content)
            return content[:self.config.max_content_length] if len(content) > self.config.max_content_length else content
        
        raise InvalidPostError("No content found")
    
    def _extract_timestamp(self, soup: BeautifulSoup) -> datetime:
        """Extract post timestamp."""
        for selector in self.selectors['timestamp']:
            element = soup.select_one(selector)
            if element:
                # Try datetime attribute first
                datetime_attr = element.get('datetime')
                if datetime_attr:
                    try:
                        # Parse ISO format timestamp
                        dt = datetime.fromisoformat(datetime_attr.replace('Z', '+00:00'))
                        return dt.replace(tzinfo=None)  # Convert to naive datetime
                    except ValueError:
                        pass
                
                # Try parsing text content
                time_text = element.get_text(strip=True)
                if time_text:
                    parsed_time = self._parse_relative_time(time_text)
                    if parsed_time:
                        return parsed_time
        
        # Default to current time if no timestamp found
        self.logger.warning("No timestamp found, using current time")
        return datetime.utcnow()
    
    def _parse_relative_time(self, time_text: str) -> Optional[datetime]:
        """Parse relative time strings like '2h', '1d', etc."""
        try:
            now = datetime.utcnow()
            time_text = time_text.lower().strip()
            
            # Handle "now" or "just now"
            if any(phrase in time_text for phrase in ['now', 'just now']):
                return now
            
            # Extract number and unit
            match = re.search(r'(\d+)\s*(m|h|d|w|mo|y)', time_text)
            if match:
                value = int(match.group(1))
                unit = match.group(2)
                
                if unit == 'm':  # minutes
                    return now - timedelta(minutes=value)
                elif unit == 'h':  # hours
                    return now - timedelta(hours=value)
                elif unit == 'd':  # days
                    return now - timedelta(days=value)
                elif unit == 'w':  # weeks
                    return now - timedelta(weeks=value)
                elif unit == 'mo':  # months (approximate)
                    return now - timedelta(days=value * 30)
                elif unit == 'y':  # years (approximate)
                    return now - timedelta(days=value * 365)
            
        except Exception as e:
            self.logger.debug("Failed to parse relative time", time_text=time_text, error=str(e))
        
        return None
    
    def _extract_post_url(self, soup: BeautifulSoup, base_url: str) -> str:
        """Extract direct post URL."""
        # Try to find permalink
        for selector in self.selectors['post_url']:
            element = soup.select_one(selector)
            if element and element.get('href'):
                url = element['href']
                if '/posts/' in url or '/activity-' in url:
                    return urljoin(base_url, url) if url.startswith('/') else url
        
        # Fallback to extracting from URN
        urn_element = soup.select_one('[data-id^="urn:li:activity"]')
        if urn_element:
            urn = urn_element.get('data-id')
            if urn:
                # Extract activity ID from URN
                match = re.search(r'urn:li:activity:(\d+)', urn)
                if match:
                    activity_id = match.group(1)
                    return f"https://www.linkedin.com/posts/activity-{activity_id}"
        
        # Final fallback
        return "https://www.linkedin.com/feed/"
    
    def _extract_metrics(self, soup: BeautifulSoup) -> PostMetrics:
        """Extract engagement metrics from post."""
        likes = self._extract_count(soup, self.selectors['likes_count'])
        comments = self._extract_count(soup, self.selectors['comments_count'])
        shares = self._extract_count(soup, self.selectors['shares_count'])
        
        return PostMetrics(
            likes=likes,
            comments=comments,
            shares=shares,
        )
    
    def _extract_count(self, soup: BeautifulSoup, selectors: List[str]) -> int:
        """Extract numeric count from element."""
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                count_text = element.get_text(strip=True)
                if count_text:
                    # Parse count (handle formats like "1,234", "1.2K", etc.)
                    count = self._parse_count_string(count_text)
                    if count is not None:
                        return count
        return 0
    
    def _parse_count_string(self, count_str: str) -> Optional[int]:
        """Parse count string to integer."""
        try:
            count_str = count_str.strip().replace(',', '')
            
            # Handle suffixes like K, M
            if count_str.endswith('K'):
                return int(float(count_str[:-1]) * 1000)
            elif count_str.endswith('M'):
                return int(float(count_str[:-1]) * 1000000)
            else:
                return int(count_str)
        except (ValueError, TypeError):
            return None
    
    def _extract_company_name(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract company name if author is posting as company."""
        for selector in self.selectors['company_name']:
            element = soup.select_one(selector)
            if element:
                company = element.get_text(strip=True)
                if company and not any(word in company.lower() for word in ['at', 'views', 'connections']):
                    return company
        return None
    
    def _extract_job_title(self, soup: BeautifulSoup) -> Optional[str]:
        """Extract author's job title."""
        for selector in self.selectors['job_title']:
            element = soup.select_one(selector)
            if element:
                title = element.get_text(strip=True)
                if title and len(title) < 200:  # Reasonable job title length
                    return title
        return None
    
    def _extract_media_urls(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """Extract media URLs from post."""
        media_urls = []
        
        for selector in self.selectors['media_elements']:
            elements = soup.select(selector)
            for element in elements:
                src = element.get('src') or element.get('data-src')
                if src:
                    # Convert to absolute URL
                    if src.startswith('/'):
                        src = urljoin(base_url, src)
                    
                    if self.config.validate_urls and self._is_valid_media_url(src):
                        media_urls.append(src)
                    elif not self.config.validate_urls:
                        media_urls.append(src)
        
        return media_urls
    
    def _is_valid_media_url(self, url: str) -> bool:
        """Validate media URL."""
        try:
            parsed = urlparse(url)
            return all([parsed.scheme, parsed.netloc]) and parsed.scheme in ['http', 'https']
        except:
            return False
    
    def _extract_hashtags(self, content: str) -> List[str]:
        """Extract hashtags from content."""
        hashtag_pattern = r'#([a-zA-Z0-9_]+)'
        hashtags = re.findall(hashtag_pattern, content)
        return list(set(hashtags))  # Remove duplicates
    
    def _extract_mentions(self, content: str) -> List[str]:
        """Extract mentions from content."""
        # Simple mention pattern - LinkedIn mentions are complex
        mention_pattern = r'@([a-zA-Z0-9_.]+)'
        mentions = re.findall(mention_pattern, content)
        return list(set(mentions))  # Remove duplicates
    
    def _detect_post_type(self, soup: BeautifulSoup, media_urls: List[str]) -> str:
        """Detect the type of post."""
        if media_urls:
            # Check for video
            if any('video' in url.lower() for url in media_urls):
                return "video"
            else:
                return "image"
        
        # Check for article/link shares
        if soup.select_one('.feed-shared-external-article'):
            return "article"
        
        # Check for poll
        if soup.select_one('[data-test-id="poll-option"]'):
            return "poll"
        
        # Check for job posting
        if soup.select_one('.job-flavored-update'):
            return "job"
        
        # Default to text
        return "text"
    
    def _detect_language(self, content: str) -> Optional[str]:
        """Detect content language (simplified implementation)."""
        # This is a simplified implementation
        # In production, you might want to use a proper language detection library
        if not content:
            return None
        
        # Simple heuristics based on character patterns
        if re.search(r'[а-яё]', content.lower()):
            return "ru"
        elif re.search(r'[àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ]', content.lower()):
            return "es"  # or other European language
        elif re.search(r'[一-龯]', content):
            return "zh"
        elif re.search(r'[ひらがなカタカナ]', content):
            return "ja"
        else:
            return "en"  # Default to English 