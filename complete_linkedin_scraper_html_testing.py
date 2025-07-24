#!/usr/bin/env python3
"""
LinkedIn Feed Scraper - HTML Testing Version
============================================

Testing version that stores complete HTML of each post alongside extracted data.
Based on the exact logic of complete_linkedin_scraper_enhanced_fast.py with added
HTML analysis capabilities to identify missing data and enhance our schema.

FEATURES:
- Uses proven fast enhanced script logic
- Stores complete HTML for each post
- Comprehensive data analysis capability
- HTML markup inspection for missing fields
- URL extraction analysis
- Schema enhancement discovery

USAGE:
- Test with 200 posts to gather comprehensive samples
- Analyze stored HTML to identify missing data
- Develop improved extraction methods
- Update existing scripts with findings
"""

import time
import json
import re
import os
import gc
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
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException
import argparse
import logging
from bs4 import BeautifulSoup

# Optional psutil for resource monitoring
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

# HTML testing stats tracking (enhanced from fast script)
html_extraction_stats = {
    "attempted": 0,
    "successful": 0,
    "html_stored": 0,
    "empty_posts_skipped": 0,
    "extraction_errors": 0,
    "browser_restarts": 0,
    "session_recoveries": 0,
    "memory_usage_mb": 0,
    "cpu_usage_percent": 0,
    "html_size_total_kb": 0
}

class SpeedConfig:
    """Configuration class for speed vs reliability trade-offs (from fast script)"""
    def __init__(self, speed_mode="balanced"):
        if speed_mode == "fast":
            self.element_wait = 0.8
            self.scroll_delay = 1.2
            self.page_load_timeout = 45
            self.implicit_wait = 8
            self.session_restart_interval = 750
            self.resource_monitoring = False
            self.verbose_logging = False
            self.enhanced_validation = False
        elif speed_mode == "balanced":
            self.element_wait = 1.2
            self.scroll_delay = 1.8
            self.page_load_timeout = 60
            self.implicit_wait = 12
            self.session_restart_interval = 500
            self.resource_monitoring = True
            self.verbose_logging = True
            self.enhanced_validation = True
        elif speed_mode == "safe":
            self.element_wait = 2.0
            self.scroll_delay = 2.5
            self.page_load_timeout = 90
            self.implicit_wait = 15
            self.session_restart_interval = 300
            self.resource_monitoring = True
            self.verbose_logging = True
            self.enhanced_validation = True

# Global speed configuration
speed_config = SpeedConfig()

# Conditional logging setup (from fast script)
def setup_logging(verbose_logging=True):
    if verbose_logging:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('linkedin_scraper_html_testing.log'),
                logging.StreamHandler()
            ]
        )
    else:
        logging.basicConfig(level=logging.WARNING)
    
    return logging.getLogger(__name__)

def log_html_extraction_stat(stat_type, value=1):
    """Track HTML extraction statistics with optional monitoring"""
    if stat_type in html_extraction_stats:
        html_extraction_stats[stat_type] += value
    
    # Optional resource monitoring
    if speed_config.resource_monitoring and PSUTIL_AVAILABLE:
        process = psutil.Process()
        html_extraction_stats["memory_usage_mb"] = process.memory_info().rss / 1024 / 1024
        html_extraction_stats["cpu_usage_percent"] = process.cpu_percent()

def log_resource_usage():
    """Log current resource usage (optional)"""
    if not speed_config.resource_monitoring or not PSUTIL_AVAILABLE:
        return 0, 0
    
    process = psutil.Process()
    memory_mb = process.memory_info().rss / 1024 / 1024
    cpu_percent = process.cpu_percent()
    
    if speed_config.verbose_logging:
        logger.info(f"Resource Usage - Memory: {memory_mb:.1f}MB, CPU: {cpu_percent:.1f}%")
    
    return memory_mb, cpu_percent

def is_valid_post(post_element):
    """Speed-optimized post validation from fast script"""
    try:
        # Quick text check
        all_text = post_element.text.strip()
        if not all_text or len(all_text) < 10:
            return False, "No meaningful text content"
        
        # Skip enhanced validation in fast mode
        if not speed_config.enhanced_validation:
            return True, "Basic validation passed"
        
        # Enhanced validation for safe/balanced modes
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
        
        return True, "Enhanced validation passed"
            
    except Exception as e:
        return False, f"Validation error: {e}"

def _is_post_valid(post_data):
    """Speed-optimized post validation after extraction (from fast script)"""
    if not post_data:
        return False
    
    # Quick validation in fast mode
    if not speed_config.enhanced_validation:
        return len(post_data.get('content', '')) > 5 and post_data.get('author', '').strip()
    
    # Enhanced validation for safe/balanced modes
    content_length = len(post_data.get('content', ''))
    if content_length < 5:
        return False
    
    author = post_data.get('author', '').strip()
    if not author or author == "Unknown Author" or len(author) < 2:
        return False
    
    return content_length > 10 and author and len(author) > 2

def parse_count(count_text):
    """Speed-optimized count parsing (from fast script)"""
    if not count_text:
        return 0
    
    try:
        count_text = count_text.strip().replace(',', '')
        
        if 'K' in count_text.upper():
            return int(float(count_text.upper().replace('K', '')) * 1000)
        elif 'M' in count_text.upper():
            return int(float(count_text.upper().replace('M', '')) * 1000000)
        else:
            numbers = re.findall(r'\d+', count_text)
            return int(numbers[0]) if numbers else 0
            
    except (ValueError, IndexError):
        return 0

def extract_post_data_with_html(post_element, post_number):
    """
    Enhanced extraction that includes both fast script logic AND HTML storage.
    This combines the proven fast extraction with comprehensive HTML analysis.
    """
    
    post_data = {
        "urn": "",
        "author": "",
        "content": "",
        "engagement": {"likes": 0, "comments": 0, "shares": 0},
        "timestamp": "",
        "media": [],
        "hashtags": [],
        "url": "",
        "html_data": {
            "complete_html": "",
            "html_size_bytes": 0,
            "html_analysis": {
                "total_links": 0,
                "external_links": [],
                "linkedin_links": [],
                "media_elements": [],
                "button_elements": [],
                "timestamp_elements": [],
                "engagement_elements": []
            }
        }
    }
    
    try:
        log_html_extraction_stat("attempted")
        
        # STEP 1: Store minimal HTML for analysis (FAST mode - no parsing during extraction)
        try:
            complete_html = post_element.get_attribute("outerHTML")
            if complete_html:
                post_data["html_data"]["complete_html"] = complete_html
                post_data["html_data"]["html_size_bytes"] = len(complete_html)
                log_html_extraction_stat("html_stored")
                log_html_extraction_stat("html_size_total_kb", len(complete_html) / 1024)
                
        except Exception as e:
            if speed_config.verbose_logging:
                logger.error(f"HTML extraction failed for post {post_number}: {e}")
        
        # STEP 2: Use EXACT fast script extraction logic
        
        # Extract URN (always required)
        try:
            urn = post_element.get_attribute("data-id")
            if urn:
                post_data["urn"] = urn
        except Exception:
            pass
        
        # Speed-optimized author extraction (EXACT from fast script)
        author_selectors = [
            "span[aria-hidden='true']",
            ".ember-view span[aria-hidden='true']"
        ]
        
        # In fast mode, try fewer selectors
        if not speed_config.enhanced_validation:
            author_selectors = author_selectors[:1]
        
        for selector in author_selectors:
            try:
                author_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                for elem in author_elements:
                    author_text = elem.text.strip()
                    if author_text and len(author_text) > 1 and author_text not in ["•", "...", "more", "Like", "Comment", "Share"]:
                        post_data["author"] = author_text
                        break
                if post_data["author"]:
                    break
            except Exception:
                continue
        
        # Speed-optimized content extraction (EXACT from fast script)
        content_selectors = [
            ".feed-shared-update-v2__description",
            ".update-components-text"
        ]
        
        # In fast mode, try fewer selectors
        if not speed_config.enhanced_validation:
            content_selectors = content_selectors[:1]
        
        for selector in content_selectors:
            try:
                content_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                for elem in content_elements:
                    content_text = elem.text.strip()
                    if content_text and len(content_text) > 5:
                        post_data["content"] = content_text
                        break
                if post_data["content"]:
                    break
            except Exception:
                continue
        
        # Speed-optimized engagement extraction (EXACT from fast script)
        if speed_config.enhanced_validation:
            engagement_selectors = {
                "likes": [
                    ".social-details-social-counts__reactions-count",
                    ".social-counts-reactions__count"
                ],
                "comments": [
                    ".social-details-social-counts__comments",
                    ".social-counts-comments__count"
                ]
            }
            
            for metric, selectors in engagement_selectors.items():
                for selector in selectors:
                    try:
                        elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                        for elem in elements:
                            count_text = elem.text.strip()
                            if count_text and count_text.replace(',', '').replace('K', '').replace('M', '').replace('.', '').isdigit():
                                post_data["engagement"][metric] = parse_count(count_text)
                                break
                        if post_data["engagement"][metric] > 0:
                            break
                    except Exception:
                        continue
        
        # FAST URL GENERATION from URN (most reliable approach)
        if not post_data["url"] and post_data["urn"]:
            try:
                urn_id = post_data["urn"].replace("urn:li:activity:", "")
                post_data["url"] = f"https://www.linkedin.com/feed/update/urn:li:activity:{urn_id}/"
            except Exception:
                pass

        # ULTRA-FAST ENGAGEMENT EXTRACTION (single selector only)
        try:
            # Look for reaction count in the most common location
            reaction_elem = post_element.find_element(By.CSS_SELECTOR, ".social-details-social-counts__reactions-count")
            count_text = reaction_elem.text.strip()
            if count_text and any(char.isdigit() for char in count_text):
                post_data["engagement"]["likes"] = parse_count(count_text)
        except:
            pass
            
        try:
            # Look for comment count in the most common location  
            comment_elem = post_element.find_element(By.CSS_SELECTOR, "button[aria-label*='comment' i]")
            aria_label = comment_elem.get_attribute('aria-label')
            if aria_label and any(char.isdigit() for char in aria_label):
                import re
                numbers = re.findall(r'\d+', aria_label)
                if numbers:
                    post_data["engagement"]["comments"] = int(numbers[0])
        except:
            pass

        # ULTRA-FAST TIMESTAMP EXTRACTION (single try)
        try:
            time_elem = post_element.find_element(By.CSS_SELECTOR, "time[datetime]")
            datetime_attr = time_elem.get_attribute('datetime')
            if datetime_attr:
                post_data["timestamp"] = datetime_attr
        except:
            # Fallback to text-based timestamp
            try:
                time_elem = post_element.find_element(By.CSS_SELECTOR, ".update-components-actor__sub-description")
                time_text = time_elem.text.strip()
                if time_text and 'ago' in time_text.lower():
                    post_data["timestamp"] = time_text.split('•')[0].strip()
            except:
                pass

        # Speed-optimized hashtag extraction (EXACT from fast script)
        if speed_config.enhanced_validation:
            try:
                full_text = post_data["content"]
                hashtag_pattern = r'#\w+'
                hashtags = re.findall(hashtag_pattern, full_text)
                post_data["hashtags"] = [tag.replace("#", "") for tag in hashtags]
            except Exception:
                pass
        
        # Validate and return (using fast script validation)
        if _is_post_valid(post_data):
            log_html_extraction_stat("successful")
            return post_data
        else:
            log_html_extraction_stat("empty_posts_skipped")
            return None
            
    except Exception as e:
        log_html_extraction_stat("extraction_errors")
        if speed_config.verbose_logging:
            logger.error(f"HTML extraction completely failed for post {post_number}: {e}")
        return None

def setup_fast_driver(headless=True):
    """Setup Chrome driver with speed-optimized configuration (EXACT from fast script)"""
    print("🔧 Setting up speed-optimized enhanced Chrome driver for HTML testing...")
    if speed_config.verbose_logging:
        logger.info("Initializing speed-optimized Chrome driver configuration for HTML testing")
    
    options = Options()
    
    if headless:
        options.add_argument("--headless=new")
    
    # CORE STABILITY FLAGS (always included) - EXACT from fast script
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # SPEED-OPTIMIZED MEMORY MANAGEMENT - EXACT from fast script
    if speed_config.enhanced_validation:
        options.add_argument("--max_old_space_size=8192")
        options.add_argument("--memory-pressure-off")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-renderer-backgrounding")
    else:
        options.add_argument("--max_old_space_size=4096")
    
    # SPEED-OPTIMIZED CRASH PREVENTION - EXACT from fast script
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-features=VizDisplayCompositor")
    
    # PERFORMANCE OPTIMIZATION - EXACT from fast script
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # ANTI-DETECTION - EXACT from fast script
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("detach", True)
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Enhanced stealth injection - EXACT from fast script
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
        # Speed-optimized timeouts - EXACT from fast script
        driver.implicitly_wait(speed_config.implicit_wait)
        driver.set_page_load_timeout(speed_config.page_load_timeout)
        driver.set_script_timeout(30)
        
        print(f"✅ Speed-optimized browser ready for HTML testing!")
        if speed_config.verbose_logging:
            logger.info("Speed-optimized Chrome driver initialized successfully for HTML testing")
        
        # Optional initial resource logging
        if speed_config.resource_monitoring:
            log_resource_usage()
        
        return driver
        
    except Exception as e:
        if speed_config.verbose_logging:
            logger.error(f"Failed to setup speed-optimized driver for HTML testing: {e}")
        print(f"❌ Failed to setup speed-optimized driver for HTML testing: {e}")
        raise

def restart_browser_session_fast(driver, email, password):
    """Speed-optimized browser session restart (EXACT from fast script)"""
    try:
        if speed_config.verbose_logging:
            logger.info("Initiating speed-optimized browser session restart")
        print("🔄 Restarting browser session (speed-optimized for HTML testing)...")
        
        # Quick cleanup
        try:
            driver.quit()
        except Exception:
            pass
        
        # Minimal cleanup delay in fast mode
        cleanup_delay = 3 if not speed_config.enhanced_validation else 5
        gc.collect()
        time.sleep(cleanup_delay)
        
        # Create new fast driver
        new_driver = setup_fast_driver(headless=True)
        
        # Re-authenticate
        login_success = login_to_linkedin_fast(new_driver, email, password)
        
        if login_success:
            new_driver.get("https://www.linkedin.com/feed/")
            time.sleep(2)  # Reduced wait time
            
            log_html_extraction_stat("browser_restarts")
            if speed_config.verbose_logging:
                logger.info("Speed-optimized browser session restart completed")
            print("✅ Browser session restarted (fast mode for HTML testing)!")
            
            return new_driver
        else:
            raise Exception("Re-authentication failed after restart")
            
    except Exception as e:
        if speed_config.verbose_logging:
            logger.error(f"Fast browser restart failed: {e}")
        raise Exception(f"Fast browser restart failed: {e}")

def login_to_linkedin_fast(driver, email, password):
    """Speed-optimized LinkedIn login (EXACT from fast script)"""
    print("🌐 Logging in (speed-optimized for HTML testing)...")
    if speed_config.verbose_logging:
        logger.info("Starting speed-optimized LinkedIn authentication for HTML testing")
    
    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)  # Reduced wait time
        
        # Speed-optimized element waiting
        wait = WebDriverWait(driver, 15)  # Shorter timeout
        
        print("📝 Filling credentials...")
        
        # Fill credentials quickly
        try:
            username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.clear()
            username_field.send_keys(email)
            
            password_field = driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
        except Exception as e:
            if speed_config.verbose_logging:
                logger.error(f"Login form interaction failed: {e}")
            return False
        
        time.sleep(3)  # Reduced wait time
        
        # Quick login verification
        current_url = driver.current_url
        
        # More precise challenge detection
        if ("challenge" in current_url or "checkpoint" in current_url) and "feed" not in current_url:
            try:
                # Check if there's actually a challenge form present
                challenge_elements = driver.find_elements(By.CSS_SELECTOR, 
                    "[data-test-id*='challenge'], [id*='challenge'], input[name*='pin'], input[name*='code']")
                
                if challenge_elements:
                    print("🔒 Security challenge detected - please complete manually")
                    print("Press Enter after completing the challenge...")
                    input()
                    
                    try:
                        wait.until(lambda driver: "feed" in driver.current_url)
                        if speed_config.verbose_logging:
                            logger.info("Security challenge completed successfully")
                        print("✅ Login successful after challenge!")
                    except TimeoutException:
                        if speed_config.verbose_logging:
                            logger.error("Challenge completion timed out")
                        print("❌ Challenge completion timed out")
                        return False
                else:
                    # False positive - no actual challenge form
                    if speed_config.verbose_logging:
                        logger.info("Challenge URL detected but no challenge form found - continuing")
            except Exception as e:
                if speed_config.verbose_logging:
                    logger.error(f"Challenge detection error: {e}")
        
        # Check if we're already on feed (successful login)
        if "feed" in current_url:
            print("✅ Login successful!")
            return True
            
        # Wait for successful login
        try:
            wait.until(lambda driver: "feed" in driver.current_url)
            print("✅ Login successful!")
            return True
        except Exception:
            print("❌ Login failed after waiting")
            return False
        
        else:
            print(f"⚠️ Unexpected page after login: {current_url}")
            return False
            
    except Exception as e:
        if speed_config.verbose_logging:
            logger.error(f"Fast login process failed: {e}")
        print(f"❌ Login failed: {e}")
        return False

def scroll_and_extract_posts_with_html(driver, target_posts=200, verbose=False, email=None, password=None):
    """
    Speed-optimized scrolling and extraction with HTML storage.
    Uses EXACT logic from fast script with added HTML capabilities.
    """
    
    print(f"📱 Starting speed-optimized HTML testing extraction for {target_posts} posts...")
    if speed_config.verbose_logging:
        logger.info(f"Starting speed-optimized HTML testing extraction session for {target_posts} posts")
    
    # Reset extraction stats
    global html_extraction_stats
    html_extraction_stats.update({
        "attempted": 0,
        "successful": 0,
        "html_stored": 0,
        "empty_posts_skipped": 0,
        "extraction_errors": 0,
        "browser_restarts": 0,
        "session_recoveries": 0
    })
    
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(2)  # Reduced initial wait (from fast script)
    
    extracted_posts = []
    seen_urns = set()
    scroll_attempts = 0
    consecutive_empty_scrolls = 0
    max_scrolls = 150  # From fast script
    
    print(f"🔍 Starting speed-optimized HTML extraction...")
    
    while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
        
        # SESSION RESTART MECHANISM (EXACT from fast script)
        if len(extracted_posts) > 0 and len(extracted_posts) % speed_config.session_restart_interval == 0:
            try:
                if speed_config.verbose_logging:
                    logger.info(f"Initiating scheduled session restart at {len(extracted_posts)} posts")
                print(f"🔄 Scheduled session restart at {len(extracted_posts)} posts...")
                
                driver = restart_browser_session_fast(driver, email, password)
                time.sleep(2)  # Reduced post-restart wait
                
            except Exception as e:
                if speed_config.verbose_logging:
                    logger.error(f"Session restart failed: {e}")
                print(f"❌ Session restart failed: {e}")
                break
        
        # OPTIONAL RESOURCE MONITORING (EXACT from fast script)
        if speed_config.resource_monitoring and len(extracted_posts) % 50 == 0:
            memory_mb, cpu_percent = log_resource_usage()
            
            if memory_mb > 4000:  # 4GB threshold
                print(f"⚠️ High memory usage: {memory_mb:.1f}MB")
        
        try:
            # Find posts with speed-optimized timing (EXACT from fast script)
            posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
            
            new_posts_found = 0
            
            for i, post_element in enumerate(posts):
                try:
                    urn = post_element.get_attribute("data-id")
                    
                    if urn in seen_urns:
                        continue
                    
                    seen_urns.add(urn)
                    
                    print(f"   📝 Extracting post with HTML {len(extracted_posts) + 1}/{target_posts}...")
                    
                    # Speed-optimized element interaction (EXACT from fast script)
                    try:
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_element)
                        time.sleep(speed_config.element_wait)  # Configurable wait time from fast script
                    except Exception:
                        continue
                    
                    # Extract with HTML-enhanced method (using fast script logic)
                    post_data = extract_post_data_with_html(post_element, len(extracted_posts) + 1)
                    
                    if post_data:
                        extracted_posts.append(post_data)
                        new_posts_found += 1
                        
                        # Speed-optimized verbose output with HTML info
                        if verbose:
                            author = post_data['author'][:25] + "..." if len(post_data['author']) > 25 else post_data['author']
                            content_preview = post_data['content'][:60] + "..." if len(post_data['content']) > 60 else post_data['content']
                            html_size = post_data['html_data']['html_size_bytes'] / 1024
                            print(f"      ✅ {author}: {content_preview}")
                            print(f"         💾 HTML: {html_size:.1f}KB, Links: {post_data['html_data']['html_analysis']['total_links']}")
                        
                        if len(extracted_posts) >= target_posts:
                            break
                            
                except Exception as e:
                    if verbose and speed_config.verbose_logging:
                        print(f"   ⚠️ Error processing post: {e}")
                    continue
            
            # Speed-optimized scrolling (EXACT from fast script)
            if new_posts_found == 0:
                consecutive_empty_scrolls += 1
                print(f"   🖱️ Scrolling... (attempt {scroll_attempts + 1})")
                
                try:
                    # Alternating scroll strategies for speed (EXACT from fast script)
                    if consecutive_empty_scrolls % 2 == 0:
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    else:
                        driver.execute_script("window.scrollBy(0, window.innerHeight);")
                except Exception:
                    pass
                
                time.sleep(speed_config.scroll_delay)  # Configurable scroll delay from fast script
                scroll_attempts += 1
                
                # Speed-optimized exit condition (EXACT from fast script)
                if consecutive_empty_scrolls >= 8:  # Reduced threshold
                    print(f"   ⚠️ Stopping extraction (empty scrolls)")
                    break
            else:
                consecutive_empty_scrolls = 0
        
        except InvalidSessionIdException as e:
            print(f"❌ Browser session lost, attempting recovery...")
            
            try:
                driver = restart_browser_session_fast(driver, email, password)
                log_html_extraction_stat("session_recoveries")
                print("✅ Session recovered!")
                continue
                
            except Exception as recovery_error:
                print(f"❌ Session recovery failed: {recovery_error}")
                break
        
        except Exception as e:
            if speed_config.verbose_logging:
                logger.error(f"Extraction loop error: {e}")
            continue
    
    print(f"\n✅ Speed-optimized HTML extraction complete! Found {len(extracted_posts)} posts")
    if speed_config.verbose_logging:
        logger.info(f"Speed-optimized HTML extraction completed with {len(extracted_posts)} posts")
    
    return extracted_posts

def save_html_testing_data(posts, speed_mode="balanced", verbose=False):
    """Save HTML testing data with comprehensive analysis files"""
    
    if not posts:
        print("⚠️ No posts to save")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    date_human = datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    # HTML testing output directory
    output_dir = Path(f"data/posts_{len(posts)}_html_testing_{speed_mode}_{date_human}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # File naming for HTML testing
    main_file = output_dir / f"linkedin_feed_html_testing_{speed_mode}_{timestamp}.json"
    html_analysis_file = output_dir / f"html_analysis_report_{timestamp}.json"
    extraction_log_file = output_dir / f"extraction_issues_analysis_{timestamp}.md"
    url_analysis_file = output_dir / f"url_extraction_analysis_{timestamp}.json"
    schema_enhancement_file = output_dir / f"schema_enhancement_suggestions_{timestamp}.md"
    
    # Save main data with HTML
    with open(main_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    
    # Comprehensive HTML analysis
    html_analysis = {
        "extraction_timestamp": timestamp,
        "speed_mode": speed_mode,
        "speed_config": speed_config.__dict__,
        "total_posts": len(posts),
        "html_statistics": {
            "total_html_size_mb": html_extraction_stats["html_size_total_kb"] / 1024,
            "average_html_size_kb": html_extraction_stats["html_size_total_kb"] / len(posts) if posts else 0,
            "posts_with_html": sum(1 for post in posts if post.get('html_data', {}).get('complete_html')),
            "posts_with_urls": sum(1 for post in posts if post.get('url')),
            "posts_missing_urls": sum(1 for post in posts if not post.get('url'))
        },
        "extraction_performance": html_extraction_stats,
        "url_extraction_analysis": {
            "urls_found": [post['url'] for post in posts if post.get('url')],
            "missing_url_posts": [{"urn": post['urn'], "author": post['author']} for post in posts if not post.get('url')],
            "url_patterns": {}
        },
        "link_analysis": {
            "total_external_links": 0,
            "total_linkedin_links": 0,
            "unique_domains": set(),
            "link_types": {}
        },
        "content_analysis": {
            "posts_with_media": sum(1 for post in posts if post.get('media')),
            "posts_with_hashtags": sum(1 for post in posts if post.get('hashtags')),
            "posts_with_engagement": sum(1 for post in posts if any(post.get('engagement', {}).values())),
            "posts_with_timestamps": sum(1 for post in posts if post.get('timestamp'))
        }
    }
    
    # Analyze link patterns
    for post in posts:
        html_data = post.get('html_data', {})
        html_analysis_data = html_data.get('html_analysis', {})
        
        # Count external links
        external_links = html_analysis_data.get('external_links', [])
        html_analysis["link_analysis"]["total_external_links"] += len(external_links)
        
        for link in external_links:
            try:
                from urllib.parse import urlparse
                domain = urlparse(link['url']).netloc
                html_analysis["link_analysis"]["unique_domains"].add(domain)
            except:
                pass
        
        # Count LinkedIn links
        linkedin_links = html_analysis_data.get('linkedin_links', [])
        html_analysis["link_analysis"]["total_linkedin_links"] += len(linkedin_links)
    
    # Convert set to list for JSON serialization
    html_analysis["link_analysis"]["unique_domains"] = list(html_analysis["link_analysis"]["unique_domains"])
    
    with open(html_analysis_file, 'w', encoding='utf-8') as f:
        json.dump(html_analysis, f, indent=2, ensure_ascii=False)
    
    # Create extraction issues analysis
    with open(extraction_log_file, 'w', encoding='utf-8') as f:
        f.write(f"# LinkedIn Feed Scraper - HTML Testing Analysis\n\n")
        f.write(f"**Extraction Date:** {timestamp}\n")
        f.write(f"**Speed Mode:** {speed_mode.upper()}\n")
        f.write(f"**Total Posts Analyzed:** {len(posts)}\n\n")
        
        f.write(f"## Missing Data Analysis\n\n")
        
        # URL Analysis
        posts_missing_urls = [post for post in posts if not post.get('url')]
        f.write(f"### Missing URLs\n")
        f.write(f"- **Posts missing URLs:** {len(posts_missing_urls)}/{len(posts)} ({len(posts_missing_urls)/len(posts)*100:.1f}%)\n")
        
        if posts_missing_urls:
            f.write(f"- **Sample posts missing URLs:**\n")
            for i, post in enumerate(posts_missing_urls[:5]):
                f.write(f"  {i+1}. URN: `{post['urn']}` - Author: {post['author']}\n")
        
        # Engagement Analysis  
        posts_missing_engagement = [post for post in posts if not any(post.get('engagement', {}).values())]
        f.write(f"\n### Missing Engagement Data\n")
        f.write(f"- **Posts missing engagement:** {len(posts_missing_engagement)}/{len(posts)} ({len(posts_missing_engagement)/len(posts)*100:.1f}%)\n")
        
        # Timestamp Analysis
        posts_missing_timestamps = [post for post in posts if not post.get('timestamp')]
        f.write(f"\n### Missing Timestamps\n")
        f.write(f"- **Posts missing timestamps:** {len(posts_missing_timestamps)}/{len(posts)} ({len(posts_missing_timestamps)/len(posts)*100:.1f}%)\n")
        
        f.write(f"\n## HTML Analysis Summary\n\n")
        f.write(f"- **Total HTML stored:** {html_extraction_stats['html_size_total_kb']:.1f} KB\n")
        f.write(f"- **Average HTML per post:** {html_extraction_stats['html_size_total_kb']/len(posts):.1f} KB\n")
        f.write(f"- **External links found:** {html_analysis['link_analysis']['total_external_links']}\n")
        f.write(f"- **LinkedIn links found:** {html_analysis['link_analysis']['total_linkedin_links']}\n")
        
        f.write(f"\n## Next Steps for Schema Enhancement\n\n")
        f.write(f"1. **Analyze HTML patterns** for missing URL extraction\n")
        f.write(f"2. **Identify new CSS selectors** for better data extraction\n")
        f.write(f"3. **Test improved extraction methods** on stored HTML\n")
        f.write(f"4. **Update existing three scripts** with improved selectors\n")
    
    # URL-specific analysis
    url_analysis = {
        "timestamp": timestamp,
        "speed_mode": speed_mode,
        "url_extraction_summary": {
            "total_posts": len(posts),
            "posts_with_urls": len([p for p in posts if p.get('url')]),
            "posts_missing_urls": len([p for p in posts if not p.get('url')]),
            "success_rate": len([p for p in posts if p.get('url')]) / len(posts) * 100 if posts else 0
        },
        "url_patterns_found": {},
        "html_url_investigation": []
    }
    
    # Investigate HTML for URL patterns
    for post in posts:
        if not post.get('url'):  # Focus on posts missing URLs
            html_data = post.get('html_data', {})
            linkedin_links = html_data.get('html_analysis', {}).get('linkedin_links', [])
            
            # Look for potential post URLs in the HTML
            potential_urls = [link for link in linkedin_links if 'activity' in link.get('url', '') or 'posts' in link.get('url', '')]
            
            if potential_urls:
                url_analysis["html_url_investigation"].append({
                    "urn": post['urn'],
                    "author": post['author'],
                    "potential_urls": potential_urls
                })
    
    with open(url_analysis_file, 'w', encoding='utf-8') as f:
        json.dump(url_analysis, f, indent=2, ensure_ascii=False)
    
    # Schema enhancement suggestions
    with open(schema_enhancement_file, 'w', encoding='utf-8') as f:
        f.write(f"# Schema Enhancement Suggestions\n\n")
        f.write(f"Based on HTML analysis of {len(posts)} posts on {timestamp} using {speed_mode} mode\n\n")
        
        f.write(f"## Current Schema Issues\n\n")
        f.write(f"1. **Missing URLs**: {len([p for p in posts if not p.get('url')])}/{len(posts)} posts\n")
        f.write(f"2. **Missing Engagement**: {len([p for p in posts if not any(p.get('engagement', {}).values())])}/{len(posts)} posts\n")
        f.write(f"3. **Missing Timestamps**: {len([p for p in posts if not p.get('timestamp')])}/{len(posts)} posts\n\n")
        
        f.write(f"## Implementation Priority for Existing Scripts\n\n")
        f.write(f"1. **HIGH**: Fix URL extraction in all three scripts\n")
        f.write(f"2. **MEDIUM**: Improve engagement data accuracy\n")
        f.write(f"3. **MEDIUM**: Better timestamp extraction\n")
        f.write(f"4. **LOW**: Additional metadata fields\n")
    
    print(f"📁 HTML testing data saved to: {output_dir}")
    print(f"   📄 Main data: {main_file.name}")
    print(f"   📊 HTML analysis: {html_analysis_file.name}")
    print(f"   📋 Issues analysis: {extraction_log_file.name}")
    print(f"   🔗 URL analysis: {url_analysis_file.name}")
    print(f"   💡 Schema suggestions: {schema_enhancement_file.name}")
    
    return main_file

def parse_arguments():
    """Parse command line arguments for HTML testing version"""
    parser = argparse.ArgumentParser(
        description="LinkedIn Feed Scraper - HTML Testing Version (Fast Enhanced Logic)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
HTML TESTING WITH FAST ENHANCED LOGIC:
  - Uses exact logic from complete_linkedin_scraper_enhanced_fast.py
  - Stores complete HTML for each post
  - Comprehensive data analysis
  - URL extraction investigation
  - Schema enhancement suggestions

SPEED OPTIMIZATION MODES:
  fast      - Fastest extraction with minimal safety checks
  balanced  - Balanced speed vs reliability (default)
  safe      - Maximum reliability with thorough checks

Examples:
  python complete_linkedin_scraper_html_testing.py --posts 200 --speed fast
  python complete_linkedin_scraper_html_testing.py --posts 100 --speed balanced --verbose
  python complete_linkedin_scraper_html_testing.py --posts 50 --speed safe --headless
        """
    )
    
    parser.add_argument(
        '-n', '--posts',
        type=int,
        default=200,
        help='Number of posts to extract for HTML testing (default: 200)'
    )
    
    parser.add_argument(
        '--speed',
        choices=['fast', 'balanced', 'safe'],
        default='balanced',
        help='Speed optimization mode (default: balanced)'
    )
    
    parser.add_argument(
        '--headless',
        action='store_true',
        default=False,
        help='Run browser in headless mode (invisible)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output with detailed post and HTML previews'
    )
    
    return parser.parse_args()

def main():
    """HTML testing main function using fast enhanced script logic"""
    
    # Parse command line arguments
    args = parse_arguments()
    
    # Configure speed settings (EXACT from fast script)
    global speed_config, logger
    speed_config = SpeedConfig(args.speed)
    logger = setup_logging(speed_config.verbose_logging)
    
    print("🧪 LinkedIn Feed Scraper - HTML Testing Version (Fast Enhanced Logic)")
    print("=" * 70)
    print(f"⚡ Speed Mode: {args.speed.upper()}")
    print(f"🔧 Element Wait: {speed_config.element_wait}s")
    print(f"🖱️ Scroll Delay: {speed_config.scroll_delay}s") 
    print(f"🔄 Session Restart: Every {speed_config.session_restart_interval} posts")
    print(f"📊 Resource Monitoring: {'ON' if speed_config.resource_monitoring else 'OFF'}")
    print(f"📊 Posts to analyze: {args.posts}")
    print(f"🌐 Browser mode: {'Headless' if args.headless else 'Visible'}")
    print(f"🔍 Verbose output: {args.verbose}")
    print(f"💾 HTML storage: ENABLED")
    print(f"🔗 URL analysis: ENABLED")
    
    # Load credentials
    load_dotenv()
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        print("❌ Error: No credentials found in .env")
        print("   Run: python setup_credentials.py")
        return
    
    print(f"👤 Account: {email}")
    
    driver = None
    start_time = time.time()
    
    try:
        # Setup speed-optimized driver (EXACT from fast script)
        driver = setup_fast_driver(headless=args.headless)
        
        # Speed-optimized login (EXACT from fast script)
        login_success = login_to_linkedin_fast(driver, email, password)
        
        if not login_success:
            print("❌ Login failed - stopping HTML testing")
            return
        
        # Speed-optimized extraction with HTML storage
        posts = scroll_and_extract_posts_with_html(
            driver, 
            target_posts=args.posts, 
            verbose=args.verbose,
            email=email,
            password=password
        )
        
        end_time = time.time()
        total_time = end_time - start_time
        
        if not posts:
            print("⚠️ No posts extracted during HTML testing")
            return
        
        # Speed-optimized data saving
        output_file = save_html_testing_data(posts, speed_mode=args.speed, verbose=args.verbose)
        
        # HTML testing results
        print("\n" + "=" * 70)
        print("📊 HTML TESTING EXTRACTION RESULTS (Fast Enhanced Logic)")
        print("=" * 70)
        print(f"⚡ Speed Mode: {args.speed.upper()}")
        print(f"📈 Total Posts: {len(posts)}")
        print(f"⏱️ Total Time: {total_time:.1f} seconds")
        print(f"🚀 Posts per Minute: {(len(posts) / total_time * 60):.1f}")
        print(f"💾 HTML Stored: {html_extraction_stats['html_stored']} posts")
        print(f"📊 Success Rate: {(html_extraction_stats['successful'] / html_extraction_stats['attempted'] * 100):.1f}%")
        print(f"🔄 Browser Restarts: {html_extraction_stats['browser_restarts']}")
        print(f"🔗 Posts with URLs: {len([p for p in posts if p.get('url')])}/{len(posts)}")
        print(f"💾 Total HTML Size: {html_extraction_stats['html_size_total_kb']:.1f} KB")
        
        if speed_config.resource_monitoring:
            print(f"💾 Final Memory Usage: {html_extraction_stats['memory_usage_mb']:.1f}MB")
        
        # Key findings for URL analysis
        posts_missing_urls = len([p for p in posts if not p.get('url')])
        print(f"\n🔍 KEY FINDINGS:")
        print(f"   ❌ Missing URLs: {posts_missing_urls}/{len(posts)} ({posts_missing_urls/len(posts)*100:.1f}%)")
        print(f"   📊 Average HTML/post: {html_extraction_stats['html_size_total_kb']/len(posts):.1f} KB")
        
        print(f"\n💾 HTML testing data saved to: {output_file}")
        print(f"📄 Ready for comprehensive analysis and script updates!")
        
        print(f"\n🧹 Closing browser...")
        
    except KeyboardInterrupt:
        print(f"\n⏹️ HTML testing interrupted by user")
        
    except Exception as e:
        print(f"❌ HTML testing failed: {e}")
        if speed_config.verbose_logging:
            import traceback
            traceback.print_exc()
        
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass
    
    print(f"\n✅ HTML testing extraction complete!")

if __name__ == "__main__":
    main() 