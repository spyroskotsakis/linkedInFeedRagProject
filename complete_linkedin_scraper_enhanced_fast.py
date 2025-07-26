#!/usr/bin/env python3
"""
LinkedIn Feed Scraper - Enhanced Fast Version
=============================================

Speed-optimized enhanced scraper with configurable performance parameters.
Allows testing different speed vs reliability trade-offs while maintaining
crash prevention capabilities.

SPEED OPTIMIZATIONS:
- Configurable delays and timeouts
- Optional resource monitoring
- Adjustable session restart intervals
- Fast mode with reduced safety checks
- Performance tuning parameters

USAGE:
- Test different speed configurations
- Find optimal speed vs reliability balance
- Benchmark performance improvements
- Production tuning and optimization
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

# Optional psutil for resource monitoring (only if monitoring enabled)
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

# Speed-optimized stats tracking
extraction_stats = {
    "attempted": 0,
    "successful": 0,
    "empty_posts_skipped": 0,
    "extraction_errors": 0,
    "browser_restarts": 0,
    "session_recoveries": 0,
    "memory_usage_mb": 0,
    "cpu_usage_percent": 0
}

class SpeedConfig:
    """Configuration class for speed vs reliability trade-offs"""
    def __init__(self, speed_mode="balanced"):
        if speed_mode == "fast":
            self.element_wait = 0.8          # Faster element loading
            self.scroll_delay = 1.2          # Faster scrolling
            self.page_load_timeout = 45      # Shorter timeouts
            self.implicit_wait = 8           # Shorter waits
            self.session_restart_interval = 750  # Less frequent restarts
            self.resource_monitoring = False  # Disable monitoring
            self.verbose_logging = False     # Minimal logging
            self.enhanced_validation = False # Skip extra validation
        elif speed_mode == "balanced":
            self.element_wait = 1.2          # Balanced timing
            self.scroll_delay = 1.8          # Standard scrolling
            self.page_load_timeout = 60      # Standard timeouts
            self.implicit_wait = 12          # Standard waits
            self.session_restart_interval = 500  # Standard restarts
            self.resource_monitoring = True   # Light monitoring
            self.verbose_logging = True      # Standard logging
            self.enhanced_validation = True  # Standard validation
        elif speed_mode == "safe":
            self.element_wait = 2.0          # Slower but safer
            self.scroll_delay = 2.5          # Careful scrolling
            self.page_load_timeout = 90      # Longer timeouts
            self.implicit_wait = 15          # Longer waits
            self.session_restart_interval = 300  # Frequent restarts
            self.resource_monitoring = True   # Full monitoring
            self.verbose_logging = True      # Detailed logging
            self.enhanced_validation = True  # Full validation

# Global speed configuration
speed_config = SpeedConfig()

# Conditional logging setup
def setup_logging(verbose_logging=True):
    if verbose_logging:
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('linkedin_scraper_enhanced_fast.log'),
                logging.StreamHandler()
            ]
        )
    else:
        logging.basicConfig(level=logging.WARNING)
    
    return logging.getLogger(__name__)

def log_extraction_stat(stat_type):
    """Track extraction statistics with optional monitoring"""
    if stat_type in extraction_stats:
        extraction_stats[stat_type] += 1
    
    # Optional resource monitoring
    if speed_config.resource_monitoring and PSUTIL_AVAILABLE:
        process = psutil.Process()
        extraction_stats["memory_usage_mb"] = process.memory_info().rss / 1024 / 1024
        extraction_stats["cpu_usage_percent"] = process.cpu_percent()

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
    """
    Speed-optimized post validation with configurable thoroughness.
    """
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
    """Speed-optimized post validation after extraction"""
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
    """Speed-optimized count parsing"""
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

def extract_post_data_fast(post_element, post_number):
    """
    Speed-optimized post extraction with configurable thoroughness.
    """
    
    post_data = {
        "urn": "",
        "author": "",
        "author_metadata": {
            "profile_url": "",
            "profile_id": "", 
            "avatar_url": "",
            "is_verified": False,
            "is_premium": False,
            "connection_status": "",
            "is_following": False,
            "connection_degree": "",
            "job_title": ""
        },
        "content": "",
        "engagement": {
            "likes": 0, 
            "comments": 0, 
            "shares": 0,
            "reaction_types": [],
            "total_reactions": 0
        },
        "timestamp": "",
        "media": [],
        "hashtags": [],
        "url": "",
        "post_metadata": {
            "visibility": "",
            "is_edited": False,
            "text_direction": "ltr",
            "post_type": ""
        }
    }
    
    try:
        log_extraction_stat("attempted")
        
        # Extract URN (always required)
        try:
            urn = post_element.get_attribute("data-id")
            if urn:
                post_data["urn"] = urn
        except Exception:
            pass
        
        # Speed-optimized author extraction
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
        
        # Speed-optimized content extraction
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
        
        # Speed-optimized engagement extraction
        if speed_config.enhanced_validation:
            # Full engagement extraction for balanced/safe modes
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
        
        # ENHANCED URL GENERATION from URN (100% reliable)
        if not post_data["url"] and post_data["urn"]:
            try:
                urn_id = post_data["urn"].replace("urn:li:activity:", "")
                post_data["url"] = f"https://www.linkedin.com/feed/update/urn:li:activity:{urn_id}/"
            except Exception:
                pass

        # ENHANCED AUTHOR METADATA EXTRACTION
        try:
            # Find author container
            actor_container = post_element.find_element(By.CSS_SELECTOR, ".update-components-actor__container")
            
            # Profile URL and ID
            profile_link = actor_container.find_element(By.CSS_SELECTOR, "a[href*='/in/']")
            if profile_link:
                href = profile_link.get_attribute('href')
                post_data["author_metadata"]["profile_url"] = href
                
                # Extract profile ID from URL
                import re
                profile_match = re.search(r'/in/([^/?]+)', href)
                if profile_match:
                    post_data["author_metadata"]["profile_id"] = profile_match.group(1)
                    
            # Avatar URL
            avatar_img = actor_container.find_element(By.CSS_SELECTOR, "img")
            if avatar_img:
                post_data["author_metadata"]["avatar_url"] = avatar_img.get_attribute('src')
                
            # Verification status
            try:
                actor_container.find_element(By.CSS_SELECTOR, "svg[data-test-icon='verified-small']")
                post_data["author_metadata"]["is_verified"] = True
            except:
                pass
                
            # Premium status  
            try:
                actor_container.find_element(By.CSS_SELECTOR, "svg[class*='premium']")
                post_data["author_metadata"]["is_premium"] = True
            except:
                pass
                
            # Connection status
            try:
                connection_elem = actor_container.find_element(By.CSS_SELECTOR, ".update-components-actor__supplementary-actor-info")
                connection_text = connection_elem.text.strip()
                post_data["author_metadata"]["connection_status"] = connection_text
                post_data["author_metadata"]["is_following"] = "Following" in connection_text
                
                if "1st" in connection_text:
                    post_data["author_metadata"]["connection_degree"] = "1st"
                elif "2nd" in connection_text:
                    post_data["author_metadata"]["connection_degree"] = "2nd"
                elif "3rd" in connection_text:
                    post_data["author_metadata"]["connection_degree"] = "3rd"
            except:
                pass
                
            # Job title
            try:
                description_elem = actor_container.find_element(By.CSS_SELECTOR, ".update-components-actor__description")
                post_data["author_metadata"]["job_title"] = description_elem.text.strip()
            except:
                pass
                
        except Exception:
            pass

        # ENHANCED ENGAGEMENT EXTRACTION
        try:
            # Reaction types from icons
            reaction_icons = post_element.find_elements(By.CSS_SELECTOR, "img[data-test-reactions-icon-type]")
            reaction_types = []
            for icon in reaction_icons:
                reaction_type = icon.get_attribute('data-test-reactions-icon-type')
                if reaction_type:
                    reaction_types.append(reaction_type.lower())
            post_data["engagement"]["reaction_types"] = list(set(reaction_types))
            
            # Total reactions (improved)
            try:
                reaction_elem = post_element.find_element(By.CSS_SELECTOR, ".social-details-social-counts__reactions-count")
                count_text = reaction_elem.text.strip()
                if count_text and any(char.isdigit() for char in count_text):
                    total_reactions = parse_count(count_text)
                    post_data["engagement"]["likes"] = total_reactions
                    post_data["engagement"]["total_reactions"] = total_reactions
            except:
                pass
        except Exception:
            pass

        # ENHANCED POST METADATA EXTRACTION
        try:
            # Post type (suggested, promoted, etc.)
            try:
                header = post_element.find_element(By.CSS_SELECTOR, ".update-components-header__text-view")
                header_text = header.text.strip()
                if header_text:
                    post_data["post_metadata"]["post_type"] = header_text.lower()
            except:
                pass
                
            # Edit status and visibility
            try:
                sub_description = post_element.find_element(By.CSS_SELECTOR, ".update-components-actor__sub-description")
                sub_text = sub_description.text.strip()
                post_data["post_metadata"]["is_edited"] = "Edited" in sub_text
                
                if "Visible to anyone" in sub_text:
                    post_data["post_metadata"]["visibility"] = "public"
                elif "connections" in sub_text.lower():
                    post_data["post_metadata"]["visibility"] = "connections"
                else:
                    post_data["post_metadata"]["visibility"] = "unknown"
            except:
                pass
                
            # Text direction
            try:
                text_container = post_element.find_element(By.CSS_SELECTOR, ".update-components-text")
                dir_attr = text_container.get_attribute('dir')
                if dir_attr:
                    post_data["post_metadata"]["text_direction"] = dir_attr
            except:
                pass
                
        except Exception:
            pass

        # Speed-optimized hashtag extraction
        if speed_config.enhanced_validation:
            try:
                full_text = post_data["content"]
                hashtag_pattern = r'#\w+'
                hashtags = re.findall(hashtag_pattern, full_text)
                post_data["hashtags"] = [tag.replace("#", "") for tag in hashtags]
            except Exception:
                pass
        
        # Validate and return
        if _is_post_valid(post_data):
            log_extraction_stat("successful")
            return post_data
        else:
            log_extraction_stat("empty_posts_skipped")
            return None
            
    except Exception as e:
        log_extraction_stat("extraction_errors")
        if speed_config.verbose_logging:
            logger.error(f"Fast extraction failed for post {post_number}: {e}")
        return None

def setup_fast_driver(headless=True):
    """Setup Chrome driver with speed-optimized configuration"""
    print("🔧 Setting up speed-optimized enhanced Chrome driver...")
    if speed_config.verbose_logging:
        logger.info("Initializing speed-optimized Chrome driver configuration")
    
    options = Options()
    
    if headless:
        options.add_argument("--headless=new")
    
    # CORE STABILITY FLAGS (always included)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    
    # SPEED-OPTIMIZED MEMORY MANAGEMENT
    if speed_config.enhanced_validation:
        # Full memory management for safe/balanced modes
        options.add_argument("--max_old_space_size=8192")
        options.add_argument("--memory-pressure-off")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-renderer-backgrounding")
    else:
        # Minimal memory management for fast mode
        options.add_argument("--max_old_space_size=4096")
    
    # SPEED-OPTIMIZED CRASH PREVENTION
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-features=VizDisplayCompositor")
    
    # PERFORMANCE OPTIMIZATION
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # ANTI-DETECTION
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("detach", True)
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Enhanced stealth injection
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
        # Speed-optimized timeouts
        driver.implicitly_wait(speed_config.implicit_wait)
        driver.set_page_load_timeout(speed_config.page_load_timeout)
        driver.set_script_timeout(30)
        
        print(f"✅ Speed-optimized browser ready! (Mode: {speed_config.__dict__})")
        if speed_config.verbose_logging:
            logger.info("Speed-optimized Chrome driver initialized successfully")
        
        # Optional initial resource logging
        if speed_config.resource_monitoring:
            log_resource_usage()
        
        return driver
        
    except Exception as e:
        if speed_config.verbose_logging:
            logger.error(f"Failed to setup speed-optimized driver: {e}")
        print(f"❌ Failed to setup speed-optimized driver: {e}")
        raise

def restart_browser_session_fast(driver, email, password, headless=False):
    """Speed-optimized browser session restart"""
    try:
        if speed_config.verbose_logging:
            logger.info("Initiating speed-optimized browser session restart")
        print("🔄 Restarting browser session (speed-optimized)...")
        
        # Quick cleanup
        try:
            driver.quit()
        except Exception:
            pass
        
        # Minimal cleanup delay in fast mode
        cleanup_delay = 3 if not speed_config.enhanced_validation else 5
        gc.collect()
        time.sleep(cleanup_delay)
        
        # Create new fast driver with same headless setting as original
        new_driver = setup_fast_driver(headless=headless)
        
        # Re-authenticate
        login_success = login_to_linkedin_fast(new_driver, email, password)
        
        if login_success:
            new_driver.get("https://www.linkedin.com/feed/")
            time.sleep(2)  # Reduced wait time
            
            log_extraction_stat("browser_restarts")
            if speed_config.verbose_logging:
                logger.info("Speed-optimized browser session restart completed")
            print("✅ Browser session restarted (fast mode)!")
            
            return new_driver
        else:
            raise Exception("Re-authentication failed after restart")
            
    except Exception as e:
        if speed_config.verbose_logging:
            logger.error(f"Fast browser restart failed: {e}")
        raise Exception(f"Fast browser restart failed: {e}")

def login_to_linkedin_fast(driver, email, password):
    """Speed-optimized LinkedIn login"""
    print("🌐 Logging in (speed-optimized)...")
    if speed_config.verbose_logging:
        logger.info("Starting speed-optimized LinkedIn authentication")
    
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
        
        if "challenge" in current_url or "checkpoint" in current_url:
            print("🔒 Security challenge detected - please complete manually")
            print("Press Enter after completing the challenge...")
            input()
            
            try:
                wait.until(lambda driver: "feed" in driver.current_url)
                if speed_config.verbose_logging:
                    logger.info("Security challenge completed successfully")
                print("✅ Login successful after challenge!")
                return True
            except Exception:
                print("❌ Challenge completion timed out")
                return False
        
        elif "feed" in current_url:
            if speed_config.verbose_logging:
                logger.info("Direct login successful")
            print("✅ Login successful!")
            return True
        
        else:
            print(f"⚠️ Unexpected page after login: {current_url}")
            return False
            
    except Exception as e:
        if speed_config.verbose_logging:
            logger.error(f"Fast login process failed: {e}")
        print(f"❌ Login failed: {e}")
        return False

def scroll_and_extract_posts_fast(driver, target_posts=10, verbose=False, email=None, password=None, headless=False):
    """
    Speed-optimized scrolling and extraction with configurable performance.
    """
    
    print(f"📱 Starting speed-optimized extraction for {target_posts} posts...")
    if speed_config.verbose_logging:
        logger.info(f"Starting speed-optimized extraction session for {target_posts} posts")
    
    # Reset extraction stats
    global extraction_stats
    extraction_stats.update({
        "attempted": 0,
        "successful": 0,
        "empty_posts_skipped": 0,
        "extraction_errors": 0,
        "browser_restarts": 0,
        "session_recoveries": 0
    })
    
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(2)  # Reduced initial wait
    
    extracted_posts = []
    seen_urns = set()
    scroll_attempts = 0
    consecutive_empty_scrolls = 0
    max_scrolls = 150  # Increased for large operations
    
    print(f"🔍 Starting speed-optimized extraction (Mode: {getattr(speed_config, 'element_wait', 'unknown'):.1f}s waits)...")
    
    while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
        
        # SESSION RESTART MECHANISM (with configurable interval)
        if len(extracted_posts) > 0 and len(extracted_posts) % speed_config.session_restart_interval == 0:
            try:
                if speed_config.verbose_logging:
                    logger.info(f"Initiating scheduled session restart at {len(extracted_posts)} posts")
                print(f"🔄 Scheduled session restart at {len(extracted_posts)} posts...")
                
                # Use the same headless setting as the original session
                driver = restart_browser_session_fast(driver, email, password, headless=headless)
                time.sleep(2)  # Reduced post-restart wait
                
            except Exception as e:
                if speed_config.verbose_logging:
                    logger.error(f"Session restart failed: {e}")
                print(f"❌ Session restart failed: {e}")
                break
        
        # OPTIONAL RESOURCE MONITORING
        if speed_config.resource_monitoring and len(extracted_posts) % 50 == 0:
            memory_mb, cpu_percent = log_resource_usage()
            
            if memory_mb > 4000:  # 4GB threshold
                print(f"⚠️ High memory usage: {memory_mb:.1f}MB")
        
        try:
            # Find posts with speed-optimized timing
            posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
            
            new_posts_found = 0
            
            for i, post_element in enumerate(posts):
                try:
                    urn = post_element.get_attribute("data-id")
                    
                    if urn in seen_urns:
                        continue
                    
                    seen_urns.add(urn)
                    
                    print(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                    
                    # Speed-optimized element interaction
                    try:
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_element)
                        time.sleep(speed_config.element_wait)  # Configurable wait time
                    except Exception:
                        continue
                    
                    # Extract with speed-optimized method
                    post_data = extract_post_data_fast(post_element, len(extracted_posts) + 1)
                    
                    if post_data:
                        extracted_posts.append(post_data)
                        new_posts_found += 1
                        
                        # Speed-optimized verbose output
                        if verbose:
                            author = post_data['author'][:25] + "..." if len(post_data['author']) > 25 else post_data['author']
                            content_preview = post_data['content'][:60] + "..." if len(post_data['content']) > 60 else post_data['content']
                            print(f"      ✅ {author}: {content_preview}")
                        
                        if len(extracted_posts) >= target_posts:
                            break
                            
                except Exception as e:
                    if verbose and speed_config.verbose_logging:
                        print(f"   ⚠️ Error processing post: {e}")
                    continue
            
            # Speed-optimized scrolling
            if new_posts_found == 0:
                consecutive_empty_scrolls += 1
                print(f"   🖱️ Scrolling... (attempt {scroll_attempts + 1})")
                
                try:
                    # Alternating scroll strategies for speed
                    if consecutive_empty_scrolls % 2 == 0:
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    else:
                        driver.execute_script("window.scrollBy(0, window.innerHeight);")
                except Exception:
                    pass
                
                time.sleep(speed_config.scroll_delay)  # Configurable scroll delay
                scroll_attempts += 1
                
                # Speed-optimized exit condition
                if consecutive_empty_scrolls >= 8:  # Reduced threshold
                    print(f"   ⚠️ Stopping extraction (empty scrolls)")
                    break
            else:
                consecutive_empty_scrolls = 0
        
        except InvalidSessionIdException as e:
            print(f"❌ Browser session lost, attempting recovery...")
            
            try:
                # Use the same headless setting as the original session
                driver = restart_browser_session_fast(driver, email, password, headless=headless)
                log_extraction_stat("session_recoveries")
                print("✅ Session recovered!")
                continue
                
            except Exception as recovery_error:
                print(f"❌ Session recovery failed: {recovery_error}")
                break
        
        except Exception as e:
            if speed_config.verbose_logging:
                logger.error(f"Extraction loop error: {e}")
            continue
    
    print(f"\n✅ Speed-optimized extraction complete! Found {len(extracted_posts)} posts")
    if speed_config.verbose_logging:
        logger.info(f"Speed-optimized extraction completed with {len(extracted_posts)} posts")
    
    return extracted_posts

def save_fast_data(posts, speed_mode="balanced", verbose=False):
    """Speed-optimized data saving"""
    
    if not posts:
        print("⚠️ No posts to save")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    date_human = datetime.now().strftime("%Y-%m-%d_%H-%M")
    
    # Speed-mode output directory naming
    output_dir = Path(f"data/posts_{len(posts)}_fast_{speed_mode}_{date_human}")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Main file naming
    output_file = output_dir / f"linkedin_feed_fast_{speed_mode}_{timestamp}.json"
    analytics_file = output_dir / f"analytics_fast_{speed_mode}_{timestamp}.json"
    summary_file = output_dir / f"extraction_summary_fast_{speed_mode}_{timestamp}.txt"
    
    # Save main data
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    
    # Speed-optimized analytics
    total_likes = sum(post['engagement']['likes'] for post in posts)
    total_comments = sum(post['engagement']['comments'] for post in posts)
    
    analytics = {
        "extraction_timestamp": timestamp,
        "speed_mode": speed_mode,
        "speed_config": speed_config.__dict__,
        "total_posts": len(posts),
        "engagement_summary": {
            "total_likes": total_likes,
            "total_comments": total_comments,
            "average_likes": total_likes / len(posts) if posts else 0
        },
        "extraction_performance": extraction_stats,
        "quality_metrics": {
            "success_rate": (extraction_stats["successful"] / extraction_stats["attempted"] * 100) if extraction_stats["attempted"] > 0 else 0,
            "empty_post_rate": (extraction_stats["empty_posts_skipped"] / extraction_stats["attempted"] * 100) if extraction_stats["attempted"] > 0 else 0
        }
    }
    
    with open(analytics_file, 'w', encoding='utf-8') as f:
        json.dump(analytics, f, indent=2, ensure_ascii=False)
    
    # Speed-optimized summary
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"LinkedIn Feed Scraper - Enhanced Fast Version\n")
        f.write(f"=" * 50 + "\n\n")
        f.write(f"Speed Mode: {speed_mode.upper()}\n")
        f.write(f"Extraction Timestamp: {timestamp}\n")
        f.write(f"Total Posts Extracted: {len(posts)}\n\n")
        
        f.write(f"SPEED CONFIGURATION:\n")
        for key, value in speed_config.__dict__.items():
            f.write(f"- {key}: {value}\n")
        f.write(f"\n")
        
        f.write(f"PERFORMANCE METRICS:\n")
        f.write(f"- Posts Attempted: {extraction_stats['attempted']}\n")
        f.write(f"- Posts Successful: {extraction_stats['successful']}\n")
        f.write(f"- Browser Restarts: {extraction_stats['browser_restarts']}\n")
        f.write(f"- Success Rate: {(extraction_stats['successful'] / extraction_stats['attempted'] * 100):.1f}%\n\n")
        
        f.write(f"ENGAGEMENT SUMMARY:\n")
        f.write(f"- Total Likes: {total_likes:,}\n")
        f.write(f"- Total Comments: {total_comments:,}\n\n")
    
    print(f"📁 Speed-optimized data saved to: {output_dir}")
    print(f"   📄 Main data: {output_file.name}")
    print(f"   📊 Analytics: {analytics_file.name}")
    
    return output_file

def parse_arguments():
    """Parse command line arguments for speed-optimized version"""
    parser = argparse.ArgumentParser(
        description="LinkedIn Feed Scraper - Enhanced Fast Version",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
SPEED OPTIMIZATION MODES:
  fast      - Fastest extraction with minimal safety checks
  balanced  - Balanced speed vs reliability (default)
  safe      - Maximum reliability with thorough checks

Examples:
  python complete_linkedin_scraper_enhanced_fast.py --posts 200 --speed fast
  python complete_linkedin_scraper_enhanced_fast.py --posts 500 --speed balanced --verbose
  python complete_linkedin_scraper_enhanced_fast.py --posts 1000 --speed safe --headless
        """
    )
    
    parser.add_argument(
        '-n', '--posts',
        type=int,
        default=None,
        help='Number of posts to extract (default: ask interactively)'
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
        help='Enable verbose output with detailed post previews'
    )
    
    return parser.parse_args()

def main():
    """Speed-optimized main scraper function"""
    
    # Parse command line arguments
    args = parse_arguments()
    
    # Configure speed settings
    global speed_config, logger
    speed_config = SpeedConfig(args.speed)
    logger = setup_logging(speed_config.verbose_logging)
    
    print("🚀 LinkedIn Feed Scraper - Enhanced Fast Version")
    print("=" * 60)
    print(f"⚡ Speed Mode: {args.speed.upper()}")
    print(f"🔧 Element Wait: {speed_config.element_wait}s")
    print(f"🖱️ Scroll Delay: {speed_config.scroll_delay}s") 
    print(f"🔄 Session Restart: Every {speed_config.session_restart_interval} posts")
    print(f"📊 Resource Monitoring: {'ON' if speed_config.resource_monitoring else 'OFF'}")
    
    # Load credentials
    load_dotenv()
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        print("❌ Error: No credentials found in .env")
        print("   Run: python setup_credentials.py")
        return
    
    print(f"👤 Account: {email}")
    
    # Determine post count
    if args.posts is not None:
        post_count = args.posts
        print(f"📊 Posts to extract: {post_count} (from command line)")
    else:
        try:
            post_count = int(input("📊 How many posts to extract? (default: 200): ") or "200")
        except (ValueError, KeyboardInterrupt):
            print("\n⏹️ Extraction cancelled")
            return
    
    print(f"🌐 Browser mode: {'Headless' if args.headless else 'Visible'}")
    print(f"🔍 Verbose output: {args.verbose}")
    
    driver = None
    start_time = time.time()
    
    try:
        # Setup speed-optimized driver
        driver = setup_fast_driver(headless=args.headless)
        
        # Speed-optimized login
        login_success = login_to_linkedin_fast(driver, email, password)
        
        if not login_success:
            print("❌ Login failed - stopping extraction")
            return
        
        # Speed-optimized extraction
        posts = scroll_and_extract_posts_fast(
            driver, 
            target_posts=post_count, 
            verbose=args.verbose,
            email=email,
            password=password,
            headless=args.headless
        )
        
        end_time = time.time()
        total_time = end_time - start_time
        
        if not posts:
            print("⚠️ No posts extracted")
            return
        
        # Speed-optimized data saving
        output_file = save_fast_data(posts, speed_mode=args.speed, verbose=args.verbose)
        
        # Speed performance results
        print("\n" + "=" * 60)
        print("📊 SPEED-OPTIMIZED EXTRACTION RESULTS")
        print("=" * 60)
        print(f"⚡ Speed Mode: {args.speed.upper()}")
        print(f"📈 Total Posts: {len(posts)}")
        print(f"⏱️ Total Time: {total_time:.1f} seconds")
        print(f"🚀 Posts per Minute: {(len(posts) / total_time * 60):.1f}")
        print(f"📊 Success Rate: {(extraction_stats['successful'] / extraction_stats['attempted'] * 100):.1f}%")
        print(f"🔄 Browser Restarts: {extraction_stats['browser_restarts']}")
        
        if speed_config.resource_monitoring:
            print(f"💾 Final Memory Usage: {extraction_stats['memory_usage_mb']:.1f}MB")
        
        # Speed comparison estimate
        standard_time_estimate = len(posts) * 3  # Estimated 3 seconds per post for standard
        speed_improvement = ((standard_time_estimate - total_time) / standard_time_estimate) * 100
        print(f"🏃 Speed Improvement: ~{speed_improvement:.0f}% faster than standard")
        
        print(f"\n💾 Speed-optimized data saved to: {output_file}")
        print(f"📄 File size: {output_file.stat().st_size / 1024:.1f} KB")
        
        print(f"\n🧹 Closing browser...")
        
    except KeyboardInterrupt:
        print(f"\n⏹️ Speed-optimized extraction interrupted by user")
        
    except Exception as e:
        print(f"❌ Speed-optimized extraction failed: {e}")
        if speed_config.verbose_logging:
            import traceback
            traceback.print_exc()
        
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass
    
    print(f"\n✅ Speed-optimized extraction complete!")

if __name__ == "__main__":
    main() 