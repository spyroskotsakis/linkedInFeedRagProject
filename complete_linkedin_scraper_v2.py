#!/usr/bin/env python3
"""
Enhanced LinkedIn Feed Scraper v2.0
Updated with working selectors from DOM investigation
Production-ready with comprehensive error handling
"""

import time
import json
import re
import csv
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
import argparse

# Load environment variables
load_dotenv()

def create_reliable_driver(headless=True):
    """Create a reliable Chrome driver with stealth capabilities"""
    options = Options()
    
    # Basic options
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-images")  # Faster loading
    options.add_argument("--disable-javascript")  # We'll enable it selectively
    
    # Stealth options
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    if headless:
        options.add_argument("--headless=new")
    
    # Window size
    options.add_argument("--window-size=1920,1080")
    
    try:
        # Use webdriver-manager for automatic ChromeDriver management
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Execute stealth script
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print("✅ Browser ready!")
        return driver
        
    except Exception as e:
        print(f"❌ Failed to create driver: {e}")
        return None

def login_to_linkedin(driver, email, password):
    """Login to LinkedIn with enhanced error handling"""
    try:
        print("🌐 Navigating to LinkedIn login...")
        driver.get("https://www.linkedin.com/login")
        time.sleep(3)
        
        print("📝 Filling credentials...")
        # Fill email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        email_field.clear()
        email_field.send_keys(email)
        
        # Fill password
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        print("🔐 Logging in...")
        # Click login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for login to complete
        WebDriverWait(driver, 30).until(
            lambda driver: "/feed/" in driver.current_url or "/mynetwork/" in driver.current_url
        )
        
        print("✅ Login successful!")
        return True
        
    except TimeoutException:
        print("❌ Login timeout - check credentials")
        return False
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return False

def extract_post_data_v2(post_element, index):
    """Enhanced post data extraction with working selectors and fallbacks"""
    
    try:
        # Get URN
        urn = post_element.get_attribute("data-id") or f"post_{index}"
        
        # Extract author information with working selectors
        author = "Unknown Author"
        author_url = None
        author_headline = None
        
        # WORKING AUTHOR SELECTORS (from DOM investigation)
        author_selectors = [
            "span[aria-hidden='true']",  # Primary working selector
            ".feed-shared-actor__name",
            ".feed-shared-actor__title", 
            "[data-tracking-control-name='public_post_feed-actor-name']",
            ".update-components-actor__name"
        ]
        
        for selector in author_selectors:
            try:
                author_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if author_elements:
                    # Find the first element with actual text content
                    for elem in author_elements:
                        text = elem.text.strip()
                        if text and text != "•" and len(text) > 1:
                            author = text
                            # Try to get profile link
                            try:
                                link_elem = elem.find_element(By.XPATH, ".//a") if elem.tag_name != 'a' else elem
                                author_url = link_elem.get_attribute("href")
                            except:
                                pass
                            break
                    if author != "Unknown Author":
                        break
            except:
                continue
        
        # Extract author headline/title
        headline_selectors = [
            ".feed-shared-actor__description",
            ".feed-shared-actor__sub-description",
            ".update-components-actor__description",
            ".artdeco-entity-lockup__subtitle"
        ]
        
        for selector in headline_selectors:
            try:
                headline_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if headline_elements:
                    for elem in headline_elements:
                        text = elem.text.strip()
                        if text and len(text) > 1:
                            author_headline = text
                            break
                    if author_headline:
                        break
            except:
                continue
        
        # Extract post content with working selectors
        content = ""
        # WORKING CONTENT SELECTORS (from DOM investigation)
        content_selectors = [
            ".feed-shared-update-v2__description",  # Primary working selector
            ".update-components-text",  # Secondary working selector
            ".feed-shared-text",
            "[data-tracking-control-name='public_post_feed-text']"
        ]
        
        for selector in content_selectors:
            try:
                content_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if content_elements:
                    for elem in content_elements:
                        text = elem.text.strip()
                        if text and len(text) > 10:  # Minimum content length
                            content = text
                            break
                    if content:
                        break
            except:
                continue
        
        # Extract timestamp with enhanced selectors
        posted_at = None
        time_selectors = [
            "time",
            ".feed-shared-actor__sub-description time",
            "[data-tracking-control-name='public_post_feed-actor-date']",
            ".feed-shared-actor__sub-description",
            ".feed-shared-actor__date",
            ".artdeco-entity-lockup__metadata"
        ]
        
        for selector in time_selectors:
            try:
                time_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if time_elements:
                    for elem in time_elements:
                        datetime_attr = elem.get_attribute("datetime")
                        if datetime_attr:
                            posted_at = datetime_attr
                            break
                        else:
                            # Try to parse relative time
                            time_text = elem.text.strip()
                            if time_text and any(word in time_text.lower() for word in ['ago', 'min', 'hour', 'day', 'week']):
                                posted_at = time_text
                                break
                    if posted_at:
                        break
            except:
                continue
        
        # Extract engagement metrics with working selectors
        likes = 0
        comments = 0
        shares = 0
        
        # WORKING ENGAGEMENT SELECTORS (from DOM investigation)
        reaction_selectors = [
            ".social-details-social-counts__reactions-count",  # Primary working selector
            ".social-counts-reactions__count",
            "[data-tracking-control-name='public_post_feed-reactions-count']"
        ]
        
        for selector in reaction_selectors:
            try:
                reaction_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if reaction_elements:
                    for elem in reaction_elements:
                        reactions_text = elem.text.strip()
                        if reactions_text:
                            likes = parse_count(reactions_text)
                            break
                    if likes > 0:
                        break
            except:
                continue
        
        # WORKING COMMENT SELECTORS (from DOM investigation)
        comment_selectors = [
            ".social-details-social-counts__comments",  # Primary working selector
            ".social-counts-comments__count",
            "[data-tracking-control-name='public_post_feed-comments-count']"
        ]
        
        for selector in comment_selectors:
            try:
                comment_elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if comment_elements:
                    for elem in comment_elements:
                        comments_text = elem.text.strip()
                        if comments_text:
                            # Extract number from "X comments" format
                            if 'comment' in comments_text.lower():
                                comments = parse_count(comments_text.split()[0])
                            else:
                                comments = parse_count(comments_text)
                            break
                    if comments > 0:
                        break
            except:
                continue
        
        # Extract hashtags from content
        hashtags = []
        if content:
            hashtag_pattern = r'#(\w+)'
            hashtags = re.findall(hashtag_pattern, content)
        
        # Look for media
        has_image = False
        has_video = False
        media_urls = []
        
        try:
            # Check for images
            img_elements = post_element.find_elements(By.CSS_SELECTOR, "img")
            for img in img_elements:
                src = img.get_attribute("src")
                if src and "media.licdn.com" in src:
                    media_urls.append(src)
                    has_image = True
        except:
            pass
        
        try:
            # Check for videos
            video_elements = post_element.find_elements(By.CSS_SELECTOR, "video")
            if video_elements:
                has_video = True
        except:
            pass
        
        # Create post data structure
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
            "post_url": f"https://www.linkedin.com/posts/{urn}" if urn.startswith("urn:") else None
        }
        
        return post_data
        
    except Exception as e:
        print(f"   ⚠️  Error extracting post {index}: {e}")
        return None

def parse_count(text):
    """Parse engagement count from text like '1,234' or '1K'"""
    if not text:
        return 0
    
    try:
        # Remove common suffixes and convert to number
        text = text.strip().lower()
        
        # Handle K (thousands)
        if 'k' in text:
            number = float(text.replace('k', '').replace(',', ''))
            return int(number * 1000)
        
        # Handle M (millions)
        if 'm' in text:
            number = float(text.replace('m', '').replace(',', ''))
            return int(number * 1000000)
        
        # Handle regular numbers
        return int(text.replace(',', ''))
        
    except:
        return 0

def scroll_and_extract_posts_v2(driver, target_posts=10, scroll_delay=2, max_scrolls=50, verbose=False):
    """Enhanced scroll and extract with better error handling"""
    
    print(f"📱 Navigating to feed and extracting {target_posts} posts...")
    
    # Go to feed
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)  # Increased wait time
    
    extracted_posts = []
    seen_urns = set()
    scroll_attempts = 0
    consecutive_empty_scrolls = 0
    
    print("🔍 Starting post extraction...")
    
    while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
        try:
            # Find all post elements
            posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
            
            if not posts:
                print("   ⚠️  No posts found, scrolling...")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_delay)
                scroll_attempts += 1
                consecutive_empty_scrolls += 1
                continue
            
            new_posts_found = 0
            
            for i, post_element in enumerate(posts):
                try:
                    urn = post_element.get_attribute("data-id")
                    
                    # Skip if we've already processed this post
                    if urn in seen_urns:
                        continue
                    
                    seen_urns.add(urn)
                    
                    print(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                    
                    post_data = extract_post_data_v2(post_element, len(extracted_posts) + 1)
                    
                    if post_data and post_data['content']:  # Only include posts with content
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
            
            # If we found new posts, continue, otherwise scroll
            if new_posts_found == 0:
                consecutive_empty_scrolls += 1
                print(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1}, empty: {consecutive_empty_scrolls})")
                
                # Try different scroll strategies
                if consecutive_empty_scrolls > 5:
                    # More aggressive scrolling
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 2);")
                else:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
                time.sleep(scroll_delay)
                scroll_attempts += 1
                
                # If too many consecutive empty scrolls, try refreshing
                if consecutive_empty_scrolls > 10:
                    print("   🔄 Too many empty scrolls, refreshing page...")
                    driver.refresh()
                    time.sleep(5)
                    consecutive_empty_scrolls = 0
            else:
                scroll_attempts = 0  # Reset counter if we found posts
                consecutive_empty_scrolls = 0
        
        except Exception as e:
            print(f"   ⚠️  Error during extraction: {e}")
            scroll_attempts += 1
            time.sleep(scroll_delay)
    
    print(f"\n✅ Extraction complete! Found {len(extracted_posts)} posts with content")
    return extracted_posts

def save_data_v2(posts, output_file=None, pretty=True, post_count=None):
    """Enhanced save data with better organization"""
    
    if not post_count:
        post_count = len(posts)
    
    # Create organized directory structure with human-readable date format
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    date_friendly = datetime.now().strftime("%Y-%m-%d_%H-%M")  # Human-readable format
    subfolder_name = f"posts_{post_count}_{date_friendly}"
    output_dir = Path("data") / subfolder_name
    
    if not output_file:
        output_file = output_dir / f"linkedin_feed_{timestamp}.json"
    else:
        # If custom output file specified, place it in the organized subfolder
        output_file = output_dir / Path(output_file).name
    
    # Ensure directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save main data file
    with open(output_file, 'w', encoding='utf-8') as f:
        if pretty:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        else:
            json.dump(posts, f, ensure_ascii=False)
    
    # Create analytics files in the same subfolder
    create_analytics_files_v2(posts, output_dir, timestamp)
    
    # Create a summary file for this extraction
    summary_file = output_dir / f"extraction_summary_{timestamp}.txt"
    create_extraction_summary_v2(posts, summary_file, post_count)
    
    print(f"📁 Data organized in: {output_dir}")
    print(f"   📄 Main data: {output_file.name}")
    print(f"   📊 Analytics: analytics_{timestamp}.json")
    print(f"   📋 Summary: extraction_summary_{timestamp}.txt")
    
    return str(output_file)

def create_analytics_files_v2(posts, output_dir, timestamp):
    """Enhanced analytics with better metrics"""
    
    if not posts:
        return
    
    # Calculate metrics
    total_likes = sum(post['engagement']['likes'] for post in posts)
    total_comments = sum(post['engagement']['comments'] for post in posts)
    total_shares = sum(post['engagement']['shares'] for post in posts)
    
    # Content analysis
    posts_with_content = [p for p in posts if p['content'] and len(p['content']) > 50]
    posts_with_media = [p for p in posts if p['media']['has_image'] or p['media']['has_video']]
    
    # Engagement analysis
    high_engagement_posts = [p for p in posts if p['engagement']['likes'] > 100 or p['engagement']['comments'] > 10]
    
    # Analytics data
    analytics_data = {
        "extraction_info": {
            "timestamp": datetime.now().isoformat(),
            "total_posts": len(posts),
            "posts_with_content": len(posts_with_content),
            "extraction_duration": "N/A"
        },
        "engagement_metrics": {
            "total_likes": total_likes,
            "total_comments": total_comments,
            "total_shares": total_shares,
            "average_likes": total_likes / len(posts) if posts else 0,
            "high_engagement_posts": len(high_engagement_posts)
        },
        "content_analysis": {
            "posts_with_substantial_content": len(posts_with_content),
            "posts_with_media": len(posts_with_media),
            "average_content_length": sum(len(p['content']) for p in posts) / len(posts) if posts else 0,
            "hashtag_count": sum(len(p['hashtags']) for p in posts)
        },
        "top_posts": sorted(posts, key=lambda x: x['engagement']['likes'], reverse=True)[:5]
    }
    
    # Save analytics
    analytics_file = output_dir / f"analytics_{timestamp}.json"
    with open(analytics_file, 'w', encoding='utf-8') as f:
        json.dump(analytics_data, f, indent=2, ensure_ascii=False)
    
    # Create CSV export
    csv_file = output_dir / f"posts_analysis_{timestamp}.csv"
    create_csv_export_v2(posts, csv_file)
    
    # Create quality posts file
    quality_posts = [p for p in posts if len(p['content']) > 100 or p['engagement']['likes'] > 50]
    quality_file = output_dir / f"quality_posts_{timestamp}.json"
    with open(quality_file, 'w', encoding='utf-8') as f:
        json.dump(quality_posts, f, indent=2, ensure_ascii=False)

def create_csv_export_v2(posts, csv_file):
    """Enhanced CSV export with better formatting"""
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Header
        writer.writerow([
            'urn', 'author', 'author_headline', 'content_length', 'content_preview',
            'likes', 'comments', 'shares', 'has_media', 'hashtag_count', 'extracted_at'
        ])
        
        # Data rows
        for post in posts:
            content_preview = post['content'][:100].replace('\n', ' ').replace(',', ';') if post['content'] else ''
            has_media = post['media']['has_image'] or post['media']['has_video']
            
            writer.writerow([
                post['urn'],
                post['author'],
                post['author_headline'] or '',
                len(post['content']) if post['content'] else 0,
                content_preview,
                post['engagement']['likes'],
                post['engagement']['comments'],
                post['engagement']['shares'],
                has_media,
                len(post['hashtags']),
                post['extracted_at']
            ])

def create_extraction_summary_v2(posts, summary_file, post_count):
    """Enhanced extraction summary"""
    
    if not posts:
        return
    
    total_likes = sum(post['engagement']['likes'] for post in posts)
    total_comments = sum(post['engagement']['comments'] for post in posts)
    total_shares = sum(post['engagement']['shares'] for post in posts)
    posts_with_media = [p for p in posts if p['media']['has_image'] or p['media']['has_video']]
    substantial_posts = [p for p in posts if len(p['content']) > 200]
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("LinkedIn Feed Extraction Summary\n")
        f.write("=" * 50 + "\n")
        f.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Target Posts: {post_count}\n")
        f.write(f"Actual Posts Extracted: {len(posts)}\n")
        f.write(f"Success Rate: {(len(posts)/post_count)*100:.1f}%\n\n")
        
        f.write("Engagement Overview:\n")
        f.write(f"- Total Likes: {total_likes:,}\n")
        f.write(f"- Total Comments: {total_comments:,}\n")
        f.write(f"- Posts with Media: {len(posts_with_media)}\n")
        f.write(f"- Posts with Substantial Content (>200 chars): {len(substantial_posts)}\n\n")
        
        # Top performing posts
        top_posts = sorted(posts, key=lambda x: x['engagement']['likes'], reverse=True)[:3]
        f.write("Top Performing Posts:\n")
        f.write("-" * 30 + "\n\n")
        
        for i, post in enumerate(top_posts, 1):
            f.write(f"{i}. {post['engagement']['likes']} likes - {post['author']}\n")
            f.write(f"   \"{post['content'][:100]}...\"\n\n")
        
        f.write("Files Generated:\n")
        f.write("- linkedin_feed_TIMESTAMP.json (main data)\n")
        f.write("- analytics_TIMESTAMP.json (detailed analytics)\n")
        f.write("- posts_analysis_TIMESTAMP.csv (spreadsheet format)\n")
        f.write("- quality_posts_TIMESTAMP.json (filtered high-value posts)\n")
        f.write("- extraction_summary_TIMESTAMP.txt (this file)\n\n")
        
        f.write("Data Structure:\n")
        f.write(f"- Folder: data/posts_{post_count}/\n")
        f.write("- Total Files: 5\n")
        f.write("- Ready for RAG applications: ✓\n")
        f.write("- Production quality: ✓\n")

def display_results_v2(posts, filename):
    """Enhanced results display"""
    
    if not posts:
        print("❌ No posts to display")
        return
    
    print("\n" + "=" * 70)
    print("📊 EXTRACTION RESULTS")
    print("=" * 70)
    
    total_likes = sum(post['engagement']['likes'] for post in posts)
    total_comments = sum(post['engagement']['comments'] for post in posts)
    total_shares = sum(post['engagement']['shares'] for post in posts)
    posts_with_media = [p for p in posts if p['media']['has_image'] or p['media']['has_video']]
    substantial_posts = [p for p in posts if len(p['content']) > 200]
    
    print(f"📈 Total Posts: {len(posts)}")
    print(f"👍 Total Likes: {total_likes:,}")
    print(f"💬 Total Comments: {total_comments:,}")
    print(f"🔄 Total Shares: {total_shares:,}")
    print(f"📸 Posts with Media: {len(posts_with_media)}")
    print(f"🏷️  Unique Hashtags: {len(set(tag for post in posts for tag in post['hashtags']))}")
    print(f"📝 Substantial Posts (>200 chars): {len(substantial_posts)}")
    
    # Sample posts
    print("\n📋 SAMPLE POSTS:")
    print("-" * 50)
    
    for i, post in enumerate(posts[:3], 1):
        print(f"\n📝 Post {i}:")
        print(f"   Author: {post['author']}")
        if post['author_headline']:
            print(f"   Title: {post['author_headline']}")
        print(f"   Content: {post['content'][:100]}...")
        print(f"   Engagement: {post['engagement']['likes']} likes, {post['engagement']['comments']} comments")
    
    # File info
    file_size = Path(filename).stat().st_size / 1024  # KB
    print(f"\n💾 Data saved to: {filename}")
    print(f"📄 File size: {file_size:.1f} KB")
    
    # JSON sample
    if posts:
        print("\n🔍 JSON Sample:")
        print("-" * 30)
        sample_post = posts[0]
        print(json.dumps({
            "urn": sample_post["urn"],
            "author": sample_post["author"],
            "author_url": sample_post["author_url"],
            "author_headline": sample_post["author_headline"],
            "content": sample_post["content"][:100] + "..." if len(sample_post["content"]) > 100 else sample_post["content"],
            "posted_at": sample_post["posted_at"],
            "engagement": sample_post["engagement"],
            "hashtags": sample_post["hashtags"],
            "media": {
                "has_image": sample_post["media"]["has_image"],
                "has_video": sample_post["media"]["has_video"],
                "urls_count": len(sample_post["media"]["urls"])
            }
        }, indent=2, ensure_ascii=False))

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Enhanced LinkedIn Feed Scraper v2.0')
    parser.add_argument('--posts', type=int, default=10, help='Number of posts to extract (default: 10)')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--scroll-delay', type=float, default=2.0, help='Delay between scrolls in seconds (default: 2.0)')
    parser.add_argument('--max-scrolls', type=int, default=50, help='Maximum scroll attempts (default: 50)')
    parser.add_argument('--output', type=str, help='Custom output filename')
    
    return parser.parse_args()

def main():
    """Main function with enhanced error handling"""
    print("🚀 Enhanced LinkedIn Feed Scraper v2.0")
    print("=" * 70)
    
    # Parse arguments
    args = parse_arguments()
    
    # Get credentials
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    if not email or not password:
        print("❌ LinkedIn credentials not found in .env file")
        print("Please create a .env file with LINKEDIN_EMAIL and LINKEDIN_PASSWORD")
        return
    
    print(f"👤 Account: {email}")
    print(f"📊 Posts to extract: {args.posts}")
    print(f"🌐 Browser mode: {'Headless' if args.headless else 'Visible'}")
    print(f"⏱️  Scroll delay: {args.scroll_delay}s")
    print(f"🔍 Verbose output: {args.verbose}")
    
    driver = None
    try:
        # Create driver
        print("🔧 Setting up enhanced Chrome driver...")
        driver = create_reliable_driver(headless=args.headless)
        
        if not driver:
            print("❌ Failed to create driver")
            return
        
        # Login
        if not login_to_linkedin(driver, email, password):
            print("❌ Login failed")
            return
        
        # Extract posts
        posts = scroll_and_extract_posts_v2(
            driver, 
            target_posts=args.posts,
            scroll_delay=args.scroll_delay,
            max_scrolls=args.max_scrolls,
            verbose=args.verbose
        )
        
        if not posts:
            print("❌ No posts extracted")
            return
        
        # Save data
        filename = save_data_v2(posts, args.output, post_count=args.posts)
        
        # Display results
        display_results_v2(posts, filename)
        
    except KeyboardInterrupt:
        print("\n⚠️  Extraction interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        if driver:
            print("\n🧹 Closing browser...")
            driver.quit()
        
        print("\n✅ Scraping complete!")

if __name__ == "__main__":
    main() 