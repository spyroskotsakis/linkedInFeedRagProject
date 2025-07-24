#!/usr/bin/env python3
"""
Production-Ready LinkedIn Feed Scraper
Phase 3: Comprehensive solution with multiple extraction methods
"""

import asyncio
import json
import time
import logging
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor
import traceback

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('linkedin_scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ProductionLinkedInScraper:
    """Production-ready LinkedIn scraper with multiple extraction methods"""
    
    def __init__(self, method="selenium", headless=True, max_retries=3):
        self.method = method
        self.headless = headless
        self.max_retries = max_retries
        self.driver = None
        self.browser = None
        self.page = None
        self.extracted_posts = []
        self.success_rate = 0
        self.error_count = 0
        self.start_time = None
        
    def setup_selenium_driver(self):
        """Setup Selenium driver with enhanced error handling"""
        try:
            options = Options()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            if self.headless:
                options.add_argument("--headless=new")
            
            options.add_argument("--window-size=1920,1080")
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            
            # Execute stealth script
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            logger.info("✅ Selenium driver ready")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to create Selenium driver: {e}")
            return False
    
    async def setup_playwright_browser(self):
        """Setup Playwright browser"""
        try:
            from playwright.async_api import async_playwright
            
            self.playwright = await async_playwright().start()
            
            self.browser = await self.playwright.chromium.launch(
                headless=self.headless,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-blink-features=AutomationControlled'
                ]
            )
            
            self.context = await self.browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            
            self.page = await self.context.new_page()
            
            # Add stealth scripts
            await self.page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined,
                });
            """)
            
            logger.info("✅ Playwright browser ready")
            return True
            
        except Exception as e:
            logger.error(f"❌ Failed to create Playwright browser: {e}")
            return False
    
    def login_with_selenium(self):
        """Login using Selenium"""
        email = os.getenv('LINKEDIN_EMAIL')
        password = os.getenv('LINKEDIN_PASSWORD')
        
        if not email or not password:
            logger.error("❌ LinkedIn credentials not found")
            return False
        
        try:
            logger.info("🌐 Navigating to LinkedIn login (Selenium)...")
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(3)
            
            # Fill email
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            email_field.clear()
            email_field.send_keys(email)
            
            # Fill password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Click login
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for login to complete
            WebDriverWait(self.driver, 30).until(
                lambda driver: "/feed/" in driver.current_url or "/mynetwork/" in driver.current_url
            )
            
            logger.info("✅ Selenium login successful")
            return True
            
        except Exception as e:
            logger.error(f"❌ Selenium login failed: {e}")
            return False
    
    async def login_with_playwright(self):
        """Login using Playwright"""
        email = os.getenv('LINKEDIN_EMAIL')
        password = os.getenv('LINKEDIN_PASSWORD')
        
        if not email or not password:
            logger.error("❌ LinkedIn credentials not found")
            return False
        
        try:
            logger.info("🌐 Navigating to LinkedIn login (Playwright)...")
            await self.page.goto("https://www.linkedin.com/login")
            await self.page.wait_for_load_state('networkidle')
            
            # Fill email
            await self.page.fill("#username", email)
            
            # Fill password
            await self.page.fill("#password", password)
            
            # Click login
            await self.page.click("button[type='submit']")
            
            # Wait for login to complete
            await self.page.wait_for_url(lambda url: "/feed/" in url or "/mynetwork/" in url, timeout=30000)
            
            logger.info("✅ Playwright login successful")
            return True
            
        except Exception as e:
            logger.error(f"❌ Playwright login failed: {e}")
            return False
    
    def extract_with_selenium(self, target_posts=10, scroll_delay=2, verbose=False):
        """Extract posts using Selenium"""
        try:
            logger.info(f"📱 Extracting {target_posts} posts with Selenium...")
            
            # Navigate to feed
            self.driver.get("https://www.linkedin.com/feed/")
            time.sleep(5)
            
            extracted_posts = []
            seen_urns = set()
            scroll_attempts = 0
            max_scrolls = 50
            
            while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
                try:
                    # Find post elements
                    posts = self.driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
                    
                    if not posts:
                        logger.warning("⚠️  No posts found, scrolling...")
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(scroll_delay)
                        scroll_attempts += 1
                        continue
                    
                    new_posts_found = 0
                    
                    for post_element in posts:
                        try:
                            urn = post_element.get_attribute("data-id")
                            
                            if urn in seen_urns:
                                continue
                            
                            seen_urns.add(urn)
                            
                            if verbose:
                                logger.info(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                            
                            post_data = self.extract_post_data_selenium(post_element)
                            
                            if post_data and post_data['content']:
                                extracted_posts.append(post_data)
                                new_posts_found += 1
                                
                                if verbose:
                                    author = post_data['author'][:30] + "..." if len(post_data['author']) > 30 else post_data['author']
                                    logger.info(f"      ✅ {author}: {post_data['content'][:50]}...")
                                
                                if len(extracted_posts) >= target_posts:
                                    break
                                    
                        except Exception as e:
                            self.error_count += 1
                            if verbose:
                                logger.warning(f"   ⚠️  Error processing post: {e}")
                            continue
                    
                    if new_posts_found == 0:
                        logger.info(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1})")
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(scroll_delay)
                        scroll_attempts += 1
                    else:
                        scroll_attempts = 0
                
                except Exception as e:
                    self.error_count += 1
                    logger.error(f"   ⚠️  Error during extraction: {e}")
                    scroll_attempts += 1
                    time.sleep(scroll_delay)
            
            logger.info(f"✅ Selenium extraction complete! Found {len(extracted_posts)} posts")
            return extracted_posts
            
        except Exception as e:
            logger.error(f"❌ Selenium extraction failed: {e}")
            return []
    
    def extract_post_data_selenium(self, post_element):
        """Extract post data using Selenium with working selectors"""
        try:
            urn = post_element.get_attribute("data-id")
            
            # Extract author
            author = "Unknown Author"
            author_selectors = [
                "span[aria-hidden='true']",
                ".feed-shared-actor__name",
                ".feed-shared-actor__title"
            ]
            
            for selector in author_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        for elem in elements:
                            text = elem.text.strip()
                            if text and text != "•" and len(text) > 1:
                                author = text
                                break
                        if author != "Unknown Author":
                            break
                except:
                    continue
            
            # Extract content
            content = ""
            content_selectors = [
                ".feed-shared-update-v2__description",
                ".update-components-text",
                ".feed-shared-text"
            ]
            
            for selector in content_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        for elem in elements:
                            text = elem.text.strip()
                            if text and len(text) > 10:
                                content = text
                                break
                        if content:
                            break
                except:
                    continue
            
            # Extract engagement
            likes = 0
            comments = 0
            
            reaction_selectors = [".social-details-social-counts__reactions-count"]
            for selector in reaction_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        text = elements[0].text.strip()
                        likes = self.parse_count(text)
                        break
                except:
                    continue
            
            comment_selectors = [".social-details-social-counts__comments"]
            for selector in comment_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    if elements:
                        text = elements[0].text.strip()
                        if 'comment' in text.lower():
                            comments = self.parse_count(text.split()[0])
                        else:
                            comments = self.parse_count(text)
                        break
                except:
                    continue
            
            # Extract media
            has_image = False
            has_video = False
            media_urls = []
            
            try:
                img_elements = post_element.find_elements(By.CSS_SELECTOR, "img")
                for img in img_elements:
                    src = img.get_attribute("src")
                    if src and "media.licdn.com" in src:
                        media_urls.append(src)
                        has_image = True
            except:
                pass
            
            try:
                video_elements = post_element.find_elements(By.CSS_SELECTOR, "video")
                if video_elements:
                    has_video = True
            except:
                pass
            
            # Create post data
            post_data = {
                "urn": urn,
                "author": author,
                "content": content,
                "posted_at": None,
                "engagement": {
                    "likes": likes,
                    "comments": comments,
                    "shares": 0
                },
                "hashtags": [],
                "media": {
                    "has_image": has_image,
                    "has_video": has_video,
                    "urls": media_urls
                },
                "extracted_at": datetime.now().isoformat(),
                "source": "selenium"
            }
            
            return post_data
            
        except Exception as e:
            logger.error(f"Error extracting post data: {e}")
            return None
    
    def parse_count(self, text):
        """Parse engagement count"""
        if not text:
            return 0
        
        try:
            text = text.strip().lower()
            
            if 'k' in text:
                number = float(text.replace('k', '').replace(',', ''))
                return int(number * 1000)
            
            if 'm' in text:
                number = float(text.replace('m', '').replace(',', ''))
                return int(number * 1000000)
            
            return int(text.replace(',', ''))
            
        except:
            return 0
    
    async def extract_with_playwright(self, target_posts=10, scroll_delay=2, verbose=False):
        """Extract posts using Playwright"""
        try:
            logger.info(f"📱 Extracting {target_posts} posts with Playwright...")
            
            # Navigate to feed
            await self.page.goto("https://www.linkedin.com/feed/")
            await self.page.wait_for_load_state('networkidle')
            await asyncio.sleep(3)
            
            extracted_posts = []
            seen_urns = set()
            scroll_attempts = 0
            max_scrolls = 50
            
            while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
                try:
                    # Find post elements
                    posts = await self.page.query_selector_all('[data-id^="urn:li:activity"]')
                    
                    if not posts:
                        logger.warning("⚠️  No posts found, scrolling...")
                        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        await asyncio.sleep(scroll_delay)
                        scroll_attempts += 1
                        continue
                    
                    new_posts_found = 0
                    
                    for post_element in posts:
                        try:
                            urn = await post_element.get_attribute("data-id")
                            
                            if urn in seen_urns:
                                continue
                            
                            seen_urns.add(urn)
                            
                            if verbose:
                                logger.info(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                            
                            post_data = await self.extract_post_data_playwright(post_element)
                            
                            if post_data and post_data['content']:
                                extracted_posts.append(post_data)
                                new_posts_found += 1
                                
                                if verbose:
                                    author = post_data['author'][:30] + "..." if len(post_data['author']) > 30 else post_data['author']
                                    logger.info(f"      ✅ {author}: {post_data['content'][:50]}...")
                                
                                if len(extracted_posts) >= target_posts:
                                    break
                                    
                        except Exception as e:
                            self.error_count += 1
                            if verbose:
                                logger.warning(f"   ⚠️  Error processing post: {e}")
                            continue
                    
                    if new_posts_found == 0:
                        logger.info(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1})")
                        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                        await asyncio.sleep(scroll_delay)
                        scroll_attempts += 1
                    else:
                        scroll_attempts = 0
                
                except Exception as e:
                    self.error_count += 1
                    logger.error(f"   ⚠️  Error during extraction: {e}")
                    scroll_attempts += 1
                    await asyncio.sleep(scroll_delay)
            
            logger.info(f"✅ Playwright extraction complete! Found {len(extracted_posts)} posts")
            return extracted_posts
            
        except Exception as e:
            logger.error(f"❌ Playwright extraction failed: {e}")
            return []
    
    async def extract_post_data_playwright(self, post_element):
        """Extract post data using Playwright"""
        try:
            urn = await post_element.get_attribute("data-id")
            
            # Extract author
            author = "Unknown Author"
            author_selectors = [
                "span[aria-hidden='true']",
                ".feed-shared-actor__name",
                ".feed-shared-actor__title"
            ]
            
            for selector in author_selectors:
                try:
                    author_elem = await post_element.query_selector(selector)
                    if author_elem:
                        text = await author_elem.text_content()
                        if text and text.strip() and len(text.strip()) > 1:
                            author = text.strip()
                            break
                except:
                    continue
            
            # Extract content
            content = ""
            content_selectors = [
                ".feed-shared-update-v2__description",
                ".update-components-text",
                ".feed-shared-text"
            ]
            
            for selector in content_selectors:
                try:
                    content_elem = await post_element.query_selector(selector)
                    if content_elem:
                        text = await content_elem.text_content()
                        if text and len(text.strip()) > 10:
                            content = text.strip()
                            break
                except:
                    continue
            
            # Extract engagement
            likes = 0
            comments = 0
            
            reaction_selectors = [".social-details-social-counts__reactions-count"]
            for selector in reaction_selectors:
                try:
                    reaction_elem = await post_element.query_selector(selector)
                    if reaction_elem:
                        text = await reaction_elem.text_content()
                        if text:
                            likes = self.parse_count(text.strip())
                            break
                except:
                    continue
            
            comment_selectors = [".social-details-social-counts__comments"]
            for selector in comment_selectors:
                try:
                    comment_elem = await post_element.query_selector(selector)
                    if comment_elem:
                        text = await comment_elem.text_content()
                        if text:
                            if 'comment' in text.lower():
                                comments = self.parse_count(text.split()[0])
                            else:
                                comments = self.parse_count(text)
                            break
                except:
                    continue
            
            # Extract media
            has_image = False
            has_video = False
            media_urls = []
            
            try:
                img_elements = await post_element.query_selector_all("img")
                for img in img_elements:
                    src = await img.get_attribute("src")
                    if src and "media.licdn.com" in src:
                        media_urls.append(src)
                        has_image = True
            except:
                pass
            
            try:
                video_elements = await post_element.query_selector_all("video")
                if video_elements:
                    has_video = True
            except:
                pass
            
            # Create post data
            post_data = {
                "urn": urn,
                "author": author,
                "content": content,
                "posted_at": None,
                "engagement": {
                    "likes": likes,
                    "comments": comments,
                    "shares": 0
                },
                "hashtags": [],
                "media": {
                    "has_image": has_image,
                    "has_video": has_video,
                    "urls": media_urls
                },
                "extracted_at": datetime.now().isoformat(),
                "source": "playwright"
            }
            
            return post_data
            
        except Exception as e:
            logger.error(f"Error extracting post data: {e}")
            return None
    
    def save_data(self, posts, output_file=None, post_count=None):
        """Save extracted posts with comprehensive metadata"""
        
        if not post_count:
            post_count = len(posts)
        
        # Create organized directory structure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        date_friendly = datetime.now().strftime("%Y-%m-%d_%H-%M")
        subfolder_name = f"posts_{post_count}_{date_friendly}_production"
        output_dir = Path("data") / subfolder_name
        
        if not output_file:
            output_file = output_dir / f"linkedin_feed_{timestamp}.json"
        else:
            output_file = output_dir / Path(output_file).name
        
        # Ensure directory exists
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Calculate metrics
        total_likes = sum(post['engagement']['likes'] for post in posts)
        total_comments = sum(post['engagement']['comments'] for post in posts)
        posts_with_media = [p for p in posts if p['media']['has_image'] or p['media']['has_video']]
        
        # Create comprehensive data structure
        data = {
            "metadata": {
                "extraction_method": self.method,
                "timestamp": datetime.now().isoformat(),
                "target_posts": post_count,
                "actual_posts": len(posts),
                "success_rate": (len(posts) / post_count) * 100 if post_count > 0 else 0,
                "error_count": self.error_count,
                "extraction_duration": time.time() - self.start_time if self.start_time else None,
                "version": "3.0"
            },
            "analytics": {
                "total_likes": total_likes,
                "total_comments": total_comments,
                "posts_with_media": len(posts_with_media),
                "average_content_length": sum(len(p['content']) for p in posts) / len(posts) if posts else 0
            },
            "posts": posts
        }
        
        # Save main data file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Save summary
        summary_file = output_dir / f"extraction_summary_{timestamp}.txt"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("Production LinkedIn Feed Extraction Summary\n")
            f.write("=" * 50 + "\n")
            f.write(f"Extraction Method: {self.method}\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target Posts: {post_count}\n")
            f.write(f"Actual Posts: {len(posts)}\n")
            f.write(f"Success Rate: {(len(posts)/post_count)*100:.1f}%\n")
            f.write(f"Error Count: {self.error_count}\n")
            f.write(f"Total Likes: {total_likes:,}\n")
            f.write(f"Total Comments: {total_comments:,}\n")
            f.write(f"Posts with Media: {len(posts_with_media)}\n")
            f.write(f"Production Ready: ✓\n")
        
        logger.info(f"📁 Data organized in: {output_dir}")
        logger.info(f"   📄 Main data: {output_file.name}")
        logger.info(f"   📋 Summary: extraction_summary_{timestamp}.txt")
        
        return str(output_file)
    
    def close(self):
        """Close all resources"""
        try:
            if self.driver:
                self.driver.quit()
            logger.info("✅ Selenium driver closed")
        except:
            pass
    
    async def close_async(self):
        """Close async resources"""
        try:
            if self.page:
                await self.page.close()
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            if hasattr(self, 'playwright'):
                await self.playwright.stop()
            logger.info("✅ Playwright browser closed")
        except:
            pass

async def main():
    """Main production function"""
    parser = argparse.ArgumentParser(description='Production LinkedIn Feed Scraper')
    parser.add_argument('--posts', type=int, default=10, help='Number of posts to extract')
    parser.add_argument('--method', choices=['selenium', 'playwright'], default='selenium', help='Extraction method')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--scroll-delay', type=float, default=2.0, help='Delay between scrolls')
    parser.add_argument('--max-retries', type=int, default=3, help='Maximum retry attempts')
    
    args = parser.parse_args()
    
    logger.info("🚀 PRODUCTION LINKEDIN FEED SCRAPER")
    logger.info("=" * 50)
    logger.info(f"Method: {args.method}")
    logger.info(f"Target Posts: {args.posts}")
    logger.info(f"Headless: {args.headless}")
    logger.info(f"Verbose: {args.verbose}")
    
    scraper = ProductionLinkedInScraper(
        method=args.method,
        headless=args.headless,
        max_retries=args.max_retries
    )
    
    scraper.start_time = time.time()
    
    try:
        if args.method == "selenium":
            # Setup Selenium
            if not scraper.setup_selenium_driver():
                return
            
            # Login
            if not scraper.login_with_selenium():
                return
            
            # Extract posts
            posts = scraper.extract_with_selenium(
                target_posts=args.posts,
                scroll_delay=args.scroll_delay,
                verbose=args.verbose
            )
            
        elif args.method == "playwright":
            # Setup Playwright
            if not await scraper.setup_playwright_browser():
                return
            
            # Login
            if not await scraper.login_with_playwright():
                return
            
            # Extract posts
            posts = await scraper.extract_with_playwright(
                target_posts=args.posts,
                scroll_delay=args.scroll_delay,
                verbose=args.verbose
            )
        
        if posts:
            # Save data
            filename = scraper.save_data(posts, post_count=args.posts)
            
            # Display results
            logger.info(f"\n📊 PRODUCTION EXTRACTION RESULTS:")
            logger.info(f"📈 Total Posts: {len(posts)}")
            total_likes = sum(post['engagement']['likes'] for post in posts)
            total_comments = sum(post['engagement']['comments'] for post in posts)
            logger.info(f"👍 Total Likes: {total_likes:,}")
            logger.info(f"💬 Total Comments: {total_comments:,}")
            logger.info(f"🎯 Success Rate: {(len(posts)/args.posts)*100:.1f}%")
            logger.info(f"❌ Error Count: {scraper.error_count}")
            logger.info(f"⏱️  Duration: {time.time() - scraper.start_time:.1f}s")
            logger.info(f"💾 Data saved to: {filename}")
            logger.info(f"✅ PRODUCTION READY: ✓")
        else:
            logger.error("❌ No posts extracted")
    
    except Exception as e:
        logger.error(f"❌ Production scraper error: {e}")
        logger.error(traceback.format_exc())
    
    finally:
        if args.method == "selenium":
            scraper.close()
        elif args.method == "playwright":
            await scraper.close_async()

if __name__ == "__main__":
    asyncio.run(main()) 