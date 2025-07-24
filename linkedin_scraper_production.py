#!/usr/bin/env python3
"""
LinkedIn Feed Scraper - Production Version for Daily Operations
==============================================================

Production-ready LinkedIn feed scraper designed for reliable daily 2000-post
operations with comprehensive error handling, recovery mechanisms, and monitoring.

Features:
- Integrated production logging with error categorization
- Automatic retry and recovery mechanisms
- Circuit breaker pattern for rate limiting
- Session persistence and recovery
- Performance monitoring and alerting
- Production-ready error handling for all failure scenarios
- Daily operation optimization with batch processing
"""

import time
import json
import re
import os
import traceback
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, WebDriverException
import argparse

# Import production systems
from production_logger import ErrorCategory, get_production_logger, log_error, log_auth_event, log_extraction_progress
from production_recovery import get_recovery_system, retry_with_recovery, RecoveryStrategy

class ProductionLinkedInScraper:
    """Production-ready LinkedIn scraper with comprehensive error handling"""
    
    def __init__(self, headless: bool = True, verbose: bool = False, batch_size: int = 100):
        self.logger = get_production_logger()
        self.recovery = get_recovery_system()
        self.headless = headless
        self.verbose = verbose
        self.batch_size = batch_size  # Process posts in batches for memory management
        
        # Production configuration
        self.config = {
            "headless": headless,
            "verbose": verbose,
            "batch_size": batch_size,
            "max_scroll_attempts": 200,  # Increased for 2000 posts
            "scroll_delay": 3.0,  # Increased delay for production
            "post_processing_delay": 0.5,  # Small delay between posts
            "browser_restart_threshold": 500,  # Restart browser every 500 posts
            "performance_check_interval": 50  # Check performance every 50 posts
        }
        
        self.driver = None
        self.session_stats = {
            "attempted": 0,
            "successful": 0,
            "empty_posts_skipped": 0,
            "extraction_errors": 0,
            "browser_restarts": 0,
            "session_start": datetime.now()
        }
    
    @retry_with_recovery(ErrorCategory.BROWSER, max_attempts=3)
    def setup_driver(self):
        """Setup Chrome driver with production configuration and stealth measures"""
        try:
            self.logger.main_logger.info("Setting up production Chrome driver...")
            
            chrome_options = Options()
            
            # Production browser configuration
            if self.headless:
                chrome_options.add_argument("--headless=new")
            
            # Enhanced stealth configuration for production
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--start-maximized")
            
            # User agent rotation for production
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            ]
            chrome_options.add_argument(f"--user-agent={user_agents[0]}")
            
            # Memory optimization for long-running operations
            chrome_options.add_argument("--max_old_space_size=4096")
            chrome_options.add_argument("--memory-pressure-off")
            
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            
            # Setup service
            service = Service(ChromeDriverManager().install())
            
            # Create driver
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Execute stealth script
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            # Set production timeouts
            self.driver.implicitly_wait(10)
            self.driver.set_page_load_timeout(30)
            
            self.logger.main_logger.info("Production driver setup completed successfully")
            return True
            
        except Exception as e:
            log_error(ErrorCategory.BROWSER, f"Driver setup failed", e)
            raise
    
    @retry_with_recovery(ErrorCategory.AUTHENTICATION, max_attempts=3)
    def login_to_linkedin(self, email: str, password: str) -> bool:
        """Login to LinkedIn with production retry logic"""
        try:
            log_auth_event("login_attempt", True, "Starting authentication process")
            
            self.logger.main_logger.info("Navigating to LinkedIn login...")
            self.driver.get("https://www.linkedin.com/login")
            
            # Wait for and fill credentials
            wait = WebDriverWait(self.driver, 15)
            
            email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
            password_field = self.driver.find_element(By.ID, "password")
            
            email_field.clear()
            email_field.send_keys(email)
            password_field.clear()
            password_field.send_keys(password)
            
            # Submit login
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Check for successful login or security challenge
            try:
                # Wait for either feed or challenge
                wait.until(lambda driver: 
                    "feed" in driver.current_url or 
                    "checkpoint" in driver.current_url or
                    "challenge" in driver.current_url
                )
                
                if "feed" in self.driver.current_url:
                    log_auth_event("login_success", True, "Direct login successful")
                    self.logger.main_logger.info("✅ Login successful!")
                    return True
                elif "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url:
                    log_auth_event("security_challenge", True, "Security challenge detected")
                    self.logger.main_logger.warning("🔒 Security challenge detected - manual intervention required")
                    
                    if not self.headless:
                        print("🔒 Security challenge detected - please complete manually")
                        print("Press Enter after completing the challenge...")
                        input()
                        
                        # Wait for navigation after challenge completion
                        try:
                            wait.until(lambda driver: "feed" in driver.current_url, timeout=30)
                            log_auth_event("challenge_completed", True, "Security challenge completed successfully")
                            self.logger.main_logger.info("✅ Login successful after challenge!")
                            return True
                        except TimeoutException:
                            self.logger.main_logger.error("❌ Challenge completion timed out - please check if you're on the feed page")
                            return False
                    
                    log_auth_event("challenge_failed", False, "Could not complete security challenge")
                    return False
                else:
                    log_auth_event("login_failed", False, f"Unexpected redirect: {self.driver.current_url}")
                    return False
                    
            except TimeoutException:
                log_auth_event("login_timeout", False, "Login process timed out")
                return False
                
        except Exception as e:
            log_auth_event("login_error", False, f"Login error: {str(e)}")
            log_error(ErrorCategory.AUTHENTICATION, f"Login failed", e)
            raise
    
    def is_valid_post(self, post_element):
        """Enhanced post validation for production reliability"""
        try:
            # Check if post has any meaningful text content
            all_text = post_element.text.strip()
            if not all_text or len(all_text) < 10:
                return False, "No meaningful text content"
            
            # Check for author indicators
            author_indicators = [
                "span[aria-hidden='true']",
                ".ember-view span[aria-hidden='true']"
            ]
            
            has_author_indicator = False
            for selector in author_indicators:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        for elem in elements:
                            text = elem.text.strip()
                            if text and len(text) > 1 and text not in ["•", "...", "more"]:
                                has_author_indicator = True
                                break
                    if has_author_indicator:
                        break
                except:
                    continue
            
            if not has_author_indicator:
                return False, "No author indicator found"
            
            # Check for content indicators
            content_indicators = [
                ".feed-shared-update-v2__description",
                ".update-components-text",
                ".feed-shared-inline-show-more-text"
            ]
            
            has_content_indicator = False
            for selector in content_indicators:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        for elem in elements:
                            text = elem.text.strip()
                            if text and len(text) > 10:
                                has_content_indicator = True
                                break
                    if has_content_indicator:
                        break
                except:
                    continue
            
            if not has_content_indicator:
                return False, "No content indicator found"
            
            return True, "Valid post"
            
        except Exception as e:
            log_error(ErrorCategory.VALIDATION, f"Post validation error", e, {"post_text_length": len(all_text) if 'all_text' in locals() else 0})
            return False, f"Validation error: {e}"
    
    def extract_post_data_with_recovery(self, post_element, index: int):
        """Extract post data with enhanced error handling and recovery"""
        try:
            self.session_stats["attempted"] += 1
            
            # Pre-validate post
            is_valid, validation_reason = self.is_valid_post(post_element)
            if not is_valid:
                self.logger.main_logger.debug(f"   ⏭️  Skipping post {index}: {validation_reason}")
                self.session_stats["empty_posts_skipped"] += 1
                return None
            
            # Extract data with fallback selectors
            post_data = {
                "urn": "",
                "author": "Unknown Author",
                "author_url": "",
                "author_headline": "",
                "content": "",
                "posted_at": "",
                "engagement": {"likes": 0, "comments": 0, "shares": 0},
                "hashtags": [],
                "media": {"has_image": False, "has_video": False, "urls": []},
                "extracted_at": datetime.now().isoformat(),
                "post_url": ""
            }
            
            # Extract URN
            try:
                urn_element = post_element.find_element(By.CSS_SELECTOR, "[data-id]")
                post_data["urn"] = urn_element.get_attribute("data-id")
            except:
                pass
            
            # Extract author with proven working selectors
            author_selectors = [
                "span[aria-hidden='true']",
                ".ember-view span[aria-hidden='true']",
                ".update-components-actor__name",
                ".feed-shared-actor__name"
            ]
            
            for selector in author_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    for elem in elements:
                        text = elem.text.strip()
                        if text and len(text) > 1 and text not in ["•", "...", "more", "Like", "Comment", "Share"]:
                            post_data["author"] = text
                            break
                    if post_data["author"] != "Unknown Author":
                        break
                except:
                    continue
            
            # Extract content with proven working selectors
            content_selectors = [
                ".feed-shared-update-v2__description",
                ".update-components-text",
                ".feed-shared-inline-show-more-text",
                ".feed-shared-text"
            ]
            
            for selector in content_selectors:
                try:
                    content_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    content = content_elem.text.strip()
                    if content and len(content) > 10:
                        post_data["content"] = content
                        break
                except:
                    continue
            
            # Extract engagement
            try:
                likes_elem = post_element.find_element(By.CSS_SELECTOR, ".social-details-social-counts__reactions-count")
                likes_text = likes_elem.text.strip()
                post_data["engagement"]["likes"] = self.parse_count(likes_text)
            except:
                pass
            
            # Extract hashtags
            try:
                hashtag_pattern = r'#\w+'
                hashtags = re.findall(hashtag_pattern, post_data["content"])
                post_data["hashtags"] = list(set(hashtags))
            except:
                pass
            
            # Check media presence
            try:
                images = post_element.find_elements(By.CSS_SELECTOR, "img")
                videos = post_element.find_elements(By.CSS_SELECTOR, "video")
                post_data["media"]["has_image"] = len(images) > 0
                post_data["media"]["has_video"] = len(videos) > 0
            except:
                pass
            
            # Final validation
            if post_data["author"] == "Unknown Author" and len(post_data["content"]) < 10:
                self.logger.main_logger.debug(f"   ⏭️  Skipping post {index}: Failed final validation")
                self.session_stats["empty_posts_skipped"] += 1
                return None
            
            self.session_stats["successful"] += 1
            
            # Log progress if verbose
            if self.verbose:
                content_preview = post_data["content"][:80] + "..." if len(post_data["content"]) > 80 else post_data["content"]
                self.logger.main_logger.info(f"      ✅ {post_data['author']}: {content_preview}")
            
            return post_data
            
        except Exception as e:
            self.session_stats["extraction_errors"] += 1
            log_error(ErrorCategory.CONTENT, f"Post extraction failed at index {index}", e, {"post_urn": post_data.get("urn", "unknown")})
            return None
    
    def parse_count(self, count_text: str) -> int:
        """Parse engagement count from text with enhanced error handling"""
        if not count_text:
            return 0
        
        try:
            # Remove commas and spaces
            clean_text = count_text.replace(',', '').replace(' ', '').lower()
            
            # Handle K/M suffixes
            if 'k' in clean_text:
                number = float(clean_text.replace('k', ''))
                return int(number * 1000)
            elif 'm' in clean_text:
                number = float(clean_text.replace('m', ''))
                return int(number * 1000000)
            else:
                # Try to extract just numbers
                numbers = re.findall(r'\d+', clean_text)
                if numbers:
                    return int(numbers[0])
                return 0
        except:
            return 0
    
    @retry_with_recovery(ErrorCategory.CONNECTION, max_attempts=3)
    def scroll_and_extract_posts_production(self, target_posts: int) -> list:
        """Production-optimized scrolling and extraction with batch processing"""
        
        self.logger.main_logger.info(f"📱 Navigating to feed and extracting {target_posts} posts...")
        
        try:
            self.driver.get("https://www.linkedin.com/feed/")
            
            # Wait for feed to load
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-id*="urn:li:activity"]')))
            
        except TimeoutException:
            log_error(ErrorCategory.CONNECTION, "Feed failed to load within timeout")
            raise
        
        extracted_posts = []
        scroll_attempts = 0
        empty_scroll_count = 0
        last_post_count = 0
        
        self.logger.main_logger.info("🔍 Starting production post extraction...")
        
        session_start_time = time.time()
        last_performance_check = time.time()
        
        while len(extracted_posts) < target_posts and scroll_attempts < self.config["max_scroll_attempts"]:
            try:
                # Find all post elements
                post_elements = self.driver.find_elements(By.CSS_SELECTOR, '[data-id*="urn:li:activity"]')
                
                # Process new posts in current view
                current_post_count = len(post_elements)
                
                for i in range(last_post_count, current_post_count):
                    if len(extracted_posts) >= target_posts:
                        break
                    
                    try:
                        post_element = post_elements[i]
                        self.logger.main_logger.info(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                        
                        # Extract post data
                        post_data = self.extract_post_data_with_recovery(post_element, len(extracted_posts) + 1)
                        
                        if post_data:
                            extracted_posts.append(post_data)
                        
                        # Small delay between posts for production stability
                        time.sleep(self.config["post_processing_delay"])
                        
                    except Exception as e:
                        log_error(ErrorCategory.CONTENT, f"Error processing post {i}", e)
                        continue
                
                # Check if we found new posts
                if current_post_count > last_post_count:
                    last_post_count = current_post_count
                    empty_scroll_count = 0
                else:
                    empty_scroll_count += 1
                
                # Performance monitoring
                current_time = time.time()
                if current_time - last_performance_check > self.config["performance_check_interval"]:
                    time_elapsed = current_time - session_start_time
                    success_rate = (self.session_stats["successful"] / max(self.session_stats["attempted"], 1)) * 100
                    
                    log_extraction_progress(len(extracted_posts), target_posts, success_rate, time_elapsed)
                    self.recovery.update_performance_metrics(len(extracted_posts), target_posts, success_rate, time_elapsed)
                    
                    last_performance_check = current_time
                
                # Browser restart for memory management
                if len(extracted_posts) > 0 and len(extracted_posts) % self.config["browser_restart_threshold"] == 0:
                    self.logger.main_logger.info(f"🔄 Restarting browser for memory management at {len(extracted_posts)} posts")
                    self._restart_browser_for_memory_management()
                
                # Stop if too many empty scrolls
                if empty_scroll_count >= 10:
                    self.logger.main_logger.warning(f"   ⚠️  Too many empty scrolls ({empty_scroll_count}), stopping extraction")
                    break
                
                # Scroll for more posts
                if len(extracted_posts) < target_posts:
                    self.logger.main_logger.info(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1})")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(self.config["scroll_delay"])
                    scroll_attempts += 1
                
            except Exception as e:
                scroll_attempts += 1
                log_error(ErrorCategory.LOGIC, f"Scroll and extract error", e, {"scroll_attempt": scroll_attempts, "posts_extracted": len(extracted_posts)})
                
                # Try to recover
                if scroll_attempts < self.config["max_scroll_attempts"]:
                    time.sleep(5)  # Wait before retry
                    continue
                else:
                    break
        
        self.logger.main_logger.info(f"\n✅ Extraction complete! Found {len(extracted_posts)} posts")
        
        # Final statistics
        time_elapsed = time.time() - session_start_time
        success_rate = (self.session_stats["successful"] / max(self.session_stats["attempted"], 1)) * 100
        
        self.logger.main_logger.info(f"\n📊 PRODUCTION EXTRACTION STATISTICS:")
        self.logger.main_logger.info(f"   📈 Posts attempted: {self.session_stats['attempted']}")
        self.logger.main_logger.info(f"   ✅ Posts successful: {self.session_stats['successful']}")
        self.logger.main_logger.info(f"   ⏭️  Empty posts skipped: {self.session_stats['empty_posts_skipped']}")
        self.logger.main_logger.info(f"   ❌ Extraction errors: {self.session_stats['extraction_errors']}")
        self.logger.main_logger.info(f"   🎯 Success rate: {success_rate:.1f}%")
        self.logger.main_logger.info(f"   ⏱️  Total time: {time_elapsed/60:.1f} minutes")
        self.logger.main_logger.info(f"   📊 Extraction rate: {len(extracted_posts)/(time_elapsed/60):.1f} posts/minute")
        
        return extracted_posts
    
    def _restart_browser_for_memory_management(self):
        """Restart browser for memory management during long operations"""
        try:
            self.session_stats["browser_restarts"] += 1
            
            # Save current state
            current_url = self.driver.current_url
            
            # Close browser
            self.driver.quit()
            time.sleep(5)
            
            # Restart browser
            self.setup_driver()
            
            # Navigate back to feed
            self.driver.get(current_url)
            time.sleep(3)
            
            self.logger.main_logger.info(f"✅ Browser restarted successfully (restart #{self.session_stats['browser_restarts']})")
            
        except Exception as e:
            log_error(ErrorCategory.BROWSER, "Browser restart failed", e)
            raise
    
    def save_production_data(self, posts: list, output_file: Path = None):
        """Save extracted data with production-quality organization and analytics"""
        
        if not posts:
            self.logger.main_logger.warning("❌ No posts to save")
            return
        
        # Create organized output directory
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        output_dir = Path("data") / f"posts_{len(posts)}_{timestamp}"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filenames
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        main_file = output_dir / f"linkedin_feed_{timestamp_str}.json"
        analytics_file = output_dir / f"analytics_{timestamp_str}.json"
        summary_file = output_dir / f"extraction_summary_{timestamp_str}.txt"
        
        # Save main data
        with open(main_file, 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        
        # Generate analytics
        analytics = self._generate_production_analytics(posts)
        with open(analytics_file, 'w', encoding='utf-8') as f:
            json.dump(analytics, f, indent=2, ensure_ascii=False, default=str)
        
        # Generate summary
        self._generate_production_summary(posts, analytics, summary_file)
        
        self.logger.main_logger.info(f"📁 Production data saved to: {output_dir}")
        self.logger.main_logger.info(f"   📄 Main data: {main_file.name}")
        self.logger.main_logger.info(f"   📊 Analytics: {analytics_file.name}")
        self.logger.main_logger.info(f"   📋 Summary: {summary_file.name}")
        
        return main_file
    
    def _generate_production_analytics(self, posts: list) -> dict:
        """Generate comprehensive analytics for production monitoring"""
        
        total_likes = sum(p['engagement']['likes'] for p in posts)
        total_comments = sum(p['engagement']['comments'] for p in posts)
        
        analytics = {
            "extraction_info": {
                "timestamp": datetime.now().isoformat(),
                "total_posts": len(posts),
                "extraction_stats": dict(self.session_stats),
                "success_rate": (self.session_stats["successful"] / max(self.session_stats["attempted"], 1)) * 100,
                "production_config": self.config
            },
            "engagement_metrics": {
                "total_likes": total_likes,
                "total_comments": total_comments,
                "average_likes": total_likes / len(posts) if posts else 0,
                "average_comments": total_comments / len(posts) if posts else 0,
                "high_engagement_posts": len([p for p in posts if p['engagement']['likes'] > 100])
            },
            "content_analysis": {
                "posts_with_substantial_content": len([p for p in posts if len(p['content']) > 200]),
                "posts_with_media": len([p for p in posts if p['media']['has_image'] or p['media']['has_video']]),
                "average_content_length": sum(len(p['content']) for p in posts) / len(posts) if posts else 0,
                "hashtag_count": len(set(tag for p in posts for tag in p['hashtags']))
            },
            "production_metrics": self.recovery.get_production_readiness_assessment()
        }
        
        return analytics
    
    def _generate_production_summary(self, posts: list, analytics: dict, summary_file: Path):
        """Generate human-readable production summary"""
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("LinkedIn Feed Extraction - Production Summary\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Posts Extracted: {len(posts)}\n")
            f.write(f"Success Rate: {analytics['extraction_info']['success_rate']:.1f}%\n\n")
            
            f.write("Extraction Statistics:\n")
            stats = analytics['extraction_info']['extraction_stats']
            f.write(f"- Posts Attempted: {stats['attempted']}\n")
            f.write(f"- Posts Successful: {stats['successful']}\n")
            f.write(f"- Empty Posts Skipped: {stats['empty_posts_skipped']}\n")
            f.write(f"- Extraction Errors: {stats['extraction_errors']}\n")
            f.write(f"- Browser Restarts: {stats['browser_restarts']}\n\n")
            
            f.write("Production Assessment:\n")
            prod_metrics = analytics['production_metrics']['production_ready']
            f.write(f"- Status: {prod_metrics['status']}\n")
            f.write(f"- Ready for 2000 posts: {prod_metrics['ready_for_2000_posts']}\n")
            
            if prod_metrics['issues']:
                f.write("- Issues:\n")
                for issue in prod_metrics['issues']:
                    f.write(f"  * {issue}\n")
            
            if prod_metrics['recommendations']:
                f.write("- Recommendations:\n")
                for rec in prod_metrics['recommendations']:
                    f.write(f"  * {rec}\n")
    
    def cleanup(self):
        """Cleanup resources and generate final session report"""
        try:
            if self.driver:
                self.driver.quit()
            
            # Generate final session statistics
            final_stats = dict(self.session_stats)
            final_stats["session_duration"] = (datetime.now() - self.session_stats["session_start"]).total_seconds()
            
            self.logger.log_session_end(final_stats)
            
            self.logger.main_logger.info("🧹 Production session cleanup completed")
            
        except Exception as e:
            log_error(ErrorCategory.LOGIC, "Cleanup failed", e)

def run_production_scraper():
    """Main entry point for production LinkedIn scraper"""
    
    # Parse arguments
    parser = argparse.ArgumentParser(
        description="LinkedIn Feed Scraper - Production Version for Daily Operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Production Examples:
  python linkedin_scraper_production.py --posts 2000 --headless         # Daily production run
  python linkedin_scraper_production.py --posts 500 --batch-size 100    # Smaller batch
  python linkedin_scraper_production.py --posts 100 --verbose           # Debug mode
        """
    )
    
    parser.add_argument("-n", "--posts", type=int, default=None, help="Number of posts to extract")
    parser.add_argument("--headless", action="store_true", help="Run browser in headless mode (recommended for production)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    parser.add_argument("--batch-size", type=int, default=100, help="Batch size for processing (default: 100)")
    
    args = parser.parse_args()
    
    # Load environment
    load_dotenv()
    
    print("🚀 LinkedIn Feed Scraper - Production Version")
    print("=" * 70)
    print("🔧 Production-ready with comprehensive error handling and recovery")
    print("📈 Optimized for daily 2000-post operations")
    
    # Get credentials
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    if not email or not password:
        print("❌ Error: No credentials found in .env")
        print("   Run: python setup_credentials.py")
        return False
    
    # Get post count
    if args.posts:
        post_count = args.posts
        print(f"📊 Posts to extract: {post_count} (from command line)")
    else:
        try:
            post_count = int(input(f"📊 How many posts to extract? (recommended: 2000 for daily operation): "))
        except (ValueError, KeyboardInterrupt):
            print("\n⏹️  Operation cancelled")
            return False
    
    # Configuration display
    browser_mode = "Headless" if args.headless else "Visible"
    print(f"🌐 Browser mode: {browser_mode}")
    print(f"📦 Batch size: {args.batch_size}")
    print(f"🔍 Verbose output: {args.verbose}")
    
    # Initialize production scraper
    scraper = None
    
    try:
        scraper = ProductionLinkedInScraper(
            headless=args.headless,
            verbose=args.verbose,
            batch_size=args.batch_size
        )
        
        # Log session start
        scraper.logger.log_session_start(post_count, scraper.config)
        
        # Setup browser
        scraper.setup_driver()
        
        # Login
        if not scraper.login_to_linkedin(email, password):
            print("❌ Login failed. Cannot proceed.")
            return False
        
        # Extract posts
        posts = scraper.scroll_and_extract_posts_production(post_count)
        
        if not posts:
            print("❌ No posts extracted")
            return False
        
        # Save data
        output_file = scraper.save_production_data(posts)
        
        # Show results
        print("\n" + "=" * 70)
        print("📊 PRODUCTION EXTRACTION RESULTS")
        print("=" * 70)
        
        print(f"📈 Total Posts: {len(posts)}")
        print(f"👍 Total Likes: {sum(p['engagement']['likes'] for p in posts):,}")
        print(f"💬 Total Comments: {sum(p['engagement']['comments'] for p in posts):,}")
        print(f"📸 Posts with Media: {sum(1 for p in posts if p['media']['has_image'] or p['media']['has_video'])}")
        print(f"🏷️  Unique Hashtags: {len(set(tag for p in posts for tag in p['hashtags']))}")
        print(f"📝 Substantial Posts (>200 chars): {sum(1 for p in posts if len(p['content']) > 200)}")
        
        # Production assessment
        assessment = scraper.recovery.get_production_readiness_assessment()
        prod_ready = assessment['production_ready']
        
        print(f"\n🎯 PRODUCTION READINESS ASSESSMENT:")
        print(f"   Status: {prod_ready['status']}")
        print(f"   Ready for 2000 posts: {'✅' if prod_ready['ready_for_2000_posts'] else '❌'}")
        
        if prod_ready['issues']:
            print(f"   Issues: {len(prod_ready['issues'])}")
            for issue in prod_ready['issues'][:3]:  # Show first 3 issues
                print(f"     - {issue}")
        
        print(f"\n💾 Data saved to: {output_file}")
        print(f"📄 File size: {output_file.stat().st_size / 1024:.1f} KB")
        
        return True
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Production scraping interrupted by user")
        return False
    except Exception as e:
        print(f"❌ Production scraping failed: {e}")
        log_error(ErrorCategory.LOGIC, "Production scraper failed", e)
        return False
    finally:
        if scraper:
            scraper.cleanup()
        print(f"\n✅ Production scraping session completed!")

if __name__ == "__main__":
    run_production_scraper() 