#!/usr/bin/env python3
"""
LinkedIn Playwright Scraper
Phase 3: Alternative implementation using Playwright for better stealth
"""

import asyncio
import json
import time
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

class LinkedInPlaywrightScraper:
    """LinkedIn scraper using Playwright for enhanced stealth and reliability"""
    
    def __init__(self, headless=False):
        self.browser = None
        self.page = None
        self.headless = headless
        self.extracted_posts = []
        
    async def create_browser(self):
        """Create Playwright browser with stealth settings"""
        try:
            self.playwright = await async_playwright().start()
            
            # Launch browser with stealth options
            self.browser = await self.playwright.chromium.launch(
                headless=self.headless,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-blink-features=AutomationControlled',
                    '--disable-extensions',
                    '--disable-plugins',
                    '--window-size=1920,1080'
                ]
            )
            
            # Create context with stealth settings
            self.context = await self.browser.new_context(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                viewport={'width': 1920, 'height': 1080},
                locale='en-US',
                timezone_id='America/New_York'
            )
            
            # Create page
            self.page = await self.context.new_page()
            
            # Add stealth scripts
            await self.page.add_init_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined,
                });
                
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5],
                });
                
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['en-US', 'en'],
                });
                
                window.chrome = {
                    runtime: {},
                };
            """)
            
            print("✅ Playwright browser ready!")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create browser: {e}")
            return False
    
    async def login_to_linkedin(self):
        """Login to LinkedIn using Playwright"""
        email = os.getenv('LINKEDIN_EMAIL')
        password = os.getenv('LINKEDIN_PASSWORD')
        
        if not email or not password:
            print("❌ LinkedIn credentials not found in .env file")
            return False
        
        try:
            print("🌐 Navigating to LinkedIn login...")
            await self.page.goto("https://www.linkedin.com/login")
            await self.page.wait_for_load_state('networkidle')
            
            print("📝 Filling credentials...")
            # Fill email
            await self.page.fill("#username", email)
            
            # Fill password
            await self.page.fill("#password", password)
            
            print("🔐 Logging in...")
            # Click login
            await self.page.click("button[type='submit']")
            
            # Wait for login to complete
            await self.page.wait_for_url(lambda url: "/feed/" in url or "/mynetwork/" in url, timeout=30000)
            
            print("✅ Login successful!")
            return True
            
        except Exception as e:
            print(f"❌ Login failed: {e}")
            return False
    
    async def extract_post_data_playwright(self, post_element):
        """Extract post data using Playwright selectors"""
        try:
            # Get URN
            urn = await post_element.get_attribute("data-id")
            
            # Extract author information
            author = "Unknown Author"
            author_url = None
            author_headline = None
            
            # Try multiple author selectors
            author_selectors = [
                "span[aria-hidden='true']",
                ".feed-shared-actor__name",
                ".feed-shared-actor__title",
                ".update-components-actor__name"
            ]
            
            for selector in author_selectors:
                try:
                    author_elem = await post_element.query_selector(selector)
                    if author_elem:
                        text = await author_elem.text_content()
                        if text and text.strip() and len(text.strip()) > 1:
                            author = text.strip()
                            # Try to get profile link
                            try:
                                link_elem = await author_elem.query_selector("a")
                                if link_elem:
                                    author_url = await link_elem.get_attribute("href")
                            except:
                                pass
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
            
            # Extract timestamp
            posted_at = None
            time_selectors = [
                "time",
                ".feed-shared-actor__sub-description time",
                ".feed-shared-actor__sub-description"
            ]
            
            for selector in time_selectors:
                try:
                    time_elem = await post_element.query_selector(selector)
                    if time_elem:
                        datetime_attr = await time_elem.get_attribute("datetime")
                        if datetime_attr:
                            posted_at = datetime_attr
                            break
                        else:
                            text = await time_elem.text_content()
                            if text and any(word in text.lower() for word in ['ago', 'min', 'hour', 'day', 'week']):
                                posted_at = text.strip()
                                break
                except:
                    continue
            
            # Extract engagement
            likes = 0
            comments = 0
            shares = 0
            
            # Reactions
            reaction_selectors = [
                ".social-details-social-counts__reactions-count",
                ".social-counts-reactions__count"
            ]
            
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
            
            # Comments
            comment_selectors = [
                ".social-details-social-counts__comments",
                ".social-counts-comments__count"
            ]
            
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
            
            # Extract hashtags
            hashtags = []
            if content:
                import re
                hashtag_pattern = r'#(\w+)'
                hashtags = re.findall(hashtag_pattern, content)
            
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
                "author_url": author_url,
                "author_headline": author_headline,
                "content": content,
                "posted_at": posted_at,
                "engagement": {
                    "likes": likes,
                    "comments": comments,
                    "shares": shares
                },
                "hashtags": hashtags,
                "media": {
                    "has_image": has_image,
                    "has_video": has_video,
                    "urls": media_urls
                },
                "extracted_at": datetime.now().isoformat(),
                "post_url": f"https://www.linkedin.com/posts/{urn}" if urn and urn.startswith("urn:") else None,
                "source": "playwright"
            }
            
            return post_data
            
        except Exception as e:
            print(f"   ⚠️  Error extracting post: {e}")
            return None
    
    def parse_count(self, text):
        """Parse engagement count from text"""
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
    
    async def scroll_and_extract_posts(self, target_posts=10, scroll_delay=2, max_scrolls=50, verbose=False):
        """Scroll through feed and extract posts using Playwright"""
        
        print(f"📱 Navigating to feed and extracting {target_posts} posts...")
        
        # Navigate to feed
        await self.page.goto("https://www.linkedin.com/feed/")
        await self.page.wait_for_load_state('networkidle')
        await asyncio.sleep(3)
        
        extracted_posts = []
        seen_urns = set()
        scroll_attempts = 0
        consecutive_empty_scrolls = 0
        
        print("🔍 Starting post extraction...")
        
        while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
            try:
                # Find all post elements
                posts = await self.page.query_selector_all('[data-id^="urn:li:activity"]')
                
                if not posts:
                    print("   ⚠️  No posts found, scrolling...")
                    await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    await asyncio.sleep(scroll_delay)
                    scroll_attempts += 1
                    consecutive_empty_scrolls += 1
                    continue
                
                new_posts_found = 0
                
                for i, post_element in enumerate(posts):
                    try:
                        urn = await post_element.get_attribute("data-id")
                        
                        # Skip if already processed
                        if urn in seen_urns:
                            continue
                        
                        seen_urns.add(urn)
                        
                        print(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                        
                        post_data = await self.extract_post_data_playwright(post_element)
                        
                        if post_data and post_data['content']:
                            extracted_posts.append(post_data)
                            new_posts_found += 1
                            
                            # Print preview if verbose
                            if verbose:
                                author = post_data['author'][:30] + "..." if len(post_data['author']) > 30 else post_data['author']
                                content_preview = post_data['content'][:80] + "..." if len(post_data['content']) > 80 else post_data['content']
                                print(f"      ✅ {author}: {content_preview}")
                            
                            # Stop if we have enough
                            if len(extracted_posts) >= target_posts:
                                break
                                
                    except Exception as e:
                        if verbose:
                            print(f"   ⚠️  Error processing post: {e}")
                        continue
                
                # If no new posts found, scroll
                if new_posts_found == 0:
                    consecutive_empty_scrolls += 1
                    print(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1}, empty: {consecutive_empty_scrolls})")
                    
                    # Try different scroll strategies
                    if consecutive_empty_scrolls > 5:
                        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight * 2)")
                    else:
                        await self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                    
                    await asyncio.sleep(scroll_delay)
                    scroll_attempts += 1
                    
                    # Refresh if too many empty scrolls
                    if consecutive_empty_scrolls > 10:
                        print("   🔄 Too many empty scrolls, refreshing page...")
                        await self.page.reload()
                        await asyncio.sleep(5)
                        consecutive_empty_scrolls = 0
                else:
                    scroll_attempts = 0
                    consecutive_empty_scrolls = 0
            
            except Exception as e:
                print(f"   ⚠️  Error during extraction: {e}")
                scroll_attempts += 1
                await asyncio.sleep(scroll_delay)
        
        print(f"\n✅ Extraction complete! Found {len(extracted_posts)} posts with content")
        return extracted_posts
    
    async def save_data(self, posts, output_file=None, post_count=None):
        """Save extracted posts"""
        
        if not post_count:
            post_count = len(posts)
        
        # Create organized directory structure
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        date_friendly = datetime.now().strftime("%Y-%m-%d_%H-%M")
        subfolder_name = f"posts_{post_count}_{date_friendly}_playwright"
        output_dir = Path("data") / subfolder_name
        
        if not output_file:
            output_file = output_dir / f"linkedin_feed_{timestamp}.json"
        else:
            output_file = output_dir / Path(output_file).name
        
        # Ensure directory exists
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save main data file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        
        print(f"📁 Data organized in: {output_dir}")
        print(f"   📄 Main data: {output_file.name}")
        
        return str(output_file)
    
    async def close(self):
        """Close browser and cleanup"""
        if self.page:
            await self.page.close()
        if self.context:
            await self.context.close()
        if self.browser:
            await self.browser.close()
        if hasattr(self, 'playwright'):
            await self.playwright.stop()

async def main():
    """Main function for Playwright scraper"""
    print("🚀 LinkedIn Playwright Scraper")
    print("=" * 50)
    
    # Parse arguments
    parser = argparse.ArgumentParser(description='LinkedIn Playwright Scraper')
    parser.add_argument('--posts', type=int, default=10, help='Number of posts to extract')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--scroll-delay', type=float, default=2.0, help='Delay between scrolls')
    
    args = parser.parse_args()
    
    scraper = LinkedInPlaywrightScraper(headless=args.headless)
    
    try:
        # Create browser
        if not await scraper.create_browser():
            return
        
        # Login
        if not await scraper.login_to_linkedin():
            return
        
        # Extract posts
        posts = await scraper.scroll_and_extract_posts(
            target_posts=args.posts,
            scroll_delay=args.scroll_delay,
            verbose=args.verbose
        )
        
        if posts:
            # Save data
            filename = await scraper.save_data(posts, post_count=args.posts)
            
            # Display results
            print(f"\n📊 EXTRACTION RESULTS:")
            print(f"📈 Total Posts: {len(posts)}")
            total_likes = sum(post['engagement']['likes'] for post in posts)
            total_comments = sum(post['engagement']['comments'] for post in posts)
            print(f"👍 Total Likes: {total_likes:,}")
            print(f"💬 Total Comments: {total_comments:,}")
            print(f"💾 Data saved to: {filename}")
        else:
            print("❌ No posts extracted")
    
    except Exception as e:
        print(f"❌ Playwright scraper error: {e}")
    
    finally:
        await scraper.close()

if __name__ == "__main__":
    asyncio.run(main()) 