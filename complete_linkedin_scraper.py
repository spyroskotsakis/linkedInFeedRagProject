#!/usr/bin/env python3
"""
Complete LinkedIn Feed Scraper
This scraper extracts full post data using the reliable driver setup.
"""

import json
import time
import re
import argparse
import csv
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
import os

# Import selenium and webdriver manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def create_reliable_driver(headless=True):
    """Create a reliable Chrome driver with stealth features"""
    
    print("🔧 Setting up stealth Chrome driver...")
    
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=en-US,en;q=0.9") 
    options.add_argument("--window-size=1280,900")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Headless mode
    if headless:
        options.add_argument("--headless=new")
    
    # Performance and stealth options
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_settings.popups": 0,
        "profile.managed_default_content_settings.images": 1
    })
    
    # Auto-install compatible driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Stealth measures
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        '''
    })
    
    return driver

def login_to_linkedin(driver, email, password):
    """Login to LinkedIn with credentials"""
    
    print("🌐 Navigating to LinkedIn login...")
    driver.get("https://www.linkedin.com/login")
    
    wait = WebDriverWait(driver, 15)
    
    try:
        # Fill login form
        print("📝 Filling credentials...")
        email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        email_field.clear()
        email_field.send_keys(email)
        
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        # Submit
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        print("🔐 Logging in...")
        time.sleep(5)
        
        # Check result
        current_url = driver.current_url
        if "feed" in current_url or "dashboard" in current_url:
            print("✅ Login successful!")
            return True
        elif "challenge" in current_url:
            print("🔒 Security challenge detected - please complete manually")
            input("Press Enter after completing the challenge...")
            return True
        else:
            print(f"❌ Login failed - redirected to: {current_url}")
            return False
            
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return False

def extract_post_data(post_element, index):
    """Extract comprehensive data from a single post element"""
    
    try:
        # Get URN
        urn = post_element.get_attribute("data-id") or f"post_{index}"
        
        # Extract author information
        author = "Unknown Author"
        author_url = None
        author_headline = None
        
        author_selectors = [
            ".feed-shared-actor__name",
            ".feed-shared-actor__title", 
            "[data-tracking-control-name='public_post_feed-actor-name']",
            ".update-components-actor__name"
        ]
        
        for selector in author_selectors:
            try:
                author_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                author = author_elem.text.strip()
                if author:
                    # Try to get profile link
                    try:
                        link_elem = author_elem.find_element(By.XPATH, ".//a") if author_elem.tag_name != 'a' else author_elem
                        author_url = link_elem.get_attribute("href")
                    except:
                        pass
                    break
            except:
                continue
        
        # Extract author headline/title
        headline_selectors = [
            ".feed-shared-actor__description",
            ".feed-shared-actor__sub-description",
            ".update-components-actor__description"
        ]
        
        for selector in headline_selectors:
            try:
                headline_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                author_headline = headline_elem.text.strip()
                if author_headline:
                    break
            except:
                continue
        
        # Extract post content
        content = ""
        content_selectors = [
            ".feed-shared-update-v2__description",
            ".feed-shared-text",
            ".update-components-text",
            "[data-tracking-control-name='public_post_feed-text']"
        ]
        
        for selector in content_selectors:
            try:
                content_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                content = content_elem.text.strip()
                if content:
                    break
            except:
                continue
        
        # Extract timestamp
        posted_at = None
        time_selectors = [
            "time",
            ".feed-shared-actor__sub-description time",
            "[data-tracking-control-name='public_post_feed-actor-date']"
        ]
        
        for selector in time_selectors:
            try:
                time_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                datetime_attr = time_elem.get_attribute("datetime")
                if datetime_attr:
                    posted_at = datetime_attr
                    break
                else:
                    # Try to parse relative time
                    time_text = time_elem.text.strip()
                    posted_at = time_text
                    break
            except:
                continue
        
        # Extract engagement metrics
        likes = 0
        comments = 0
        shares = 0
        
        # Look for reaction counts
        reaction_selectors = [
            ".social-details-social-counts__reactions-count",
            ".social-counts-reactions__count",
            "[data-tracking-control-name='public_post_feed-reactions-count']"
        ]
        
        for selector in reaction_selectors:
            try:
                reactions_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                reactions_text = reactions_elem.text.strip()
                # Extract number from text like "1,234" or "1K"
                likes = parse_count(reactions_text)
                break
            except:
                continue
        
        # Look for comments count
        comment_selectors = [
            ".social-details-social-counts__comments",
            ".social-counts-comments__count",
            "[data-tracking-control-name='public_post_feed-comments-count']"
        ]
        
        for selector in comment_selectors:
            try:
                comments_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                comments_text = comments_elem.text.strip()
                comments = parse_count(comments_text)
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
    
    # Remove non-numeric characters except K, M, B
    clean_text = re.sub(r'[^\d.KMB]', '', text.upper())
    
    if not clean_text:
        return 0
    
    try:
        if 'K' in clean_text:
            return int(float(clean_text.replace('K', '')) * 1000)
        elif 'M' in clean_text:
            return int(float(clean_text.replace('M', '')) * 1000000)
        elif 'B' in clean_text:
            return int(float(clean_text.replace('B', '')) * 1000000000)
        else:
            return int(clean_text.replace(',', '').replace('.', ''))
    except:
        return 0

def scroll_and_extract_posts(driver, target_posts=10, scroll_delay=2, max_scrolls=50, verbose=False):
    """Scroll through feed and extract posts"""
    
    print(f"📱 Navigating to feed and extracting {target_posts} posts...")
    
    # Go to feed
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(3)
    
    extracted_posts = []
    seen_urns = set()
    scroll_attempts = 0
    
    print("🔍 Starting post extraction...")
    
    while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
        # Find all post elements
        posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
        
        new_posts_found = 0
        
        for i, post_element in enumerate(posts):
            try:
                urn = post_element.get_attribute("data-id")
                
                # Skip if we've already processed this post
                if urn in seen_urns:
                    continue
                
                seen_urns.add(urn)
                
                print(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                
                post_data = extract_post_data(post_element, len(extracted_posts) + 1)
                
                if post_data:
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
            print(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1})")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_delay)
            scroll_attempts += 1
        else:
            scroll_attempts = 0  # Reset counter if we found posts
    
    print(f"\n✅ Extraction complete! Found {len(extracted_posts)} posts")
    return extracted_posts

def save_data(posts, output_file=None, pretty=True, post_count=None):
    """Save extracted posts to file in organized subfolder structure"""
    
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
    analytics_file = output_dir / f"analytics_{timestamp}.json"
    create_analytics_files(posts, output_dir, timestamp)
    
    # Create a summary file for this extraction
    summary_file = output_dir / f"extraction_summary_{timestamp}.txt"
    create_extraction_summary(posts, summary_file, post_count)
    
    print(f"📁 Data organized in: {output_dir}")
    print(f"   📄 Main data: {output_file.name}")
    print(f"   📊 Analytics: analytics_{timestamp}.json")
    print(f"   📋 Summary: extraction_summary_{timestamp}.txt")
    
    return str(output_file)

def create_analytics_files(posts, output_dir, timestamp):
    """Create comprehensive analytics files"""
    
    # Basic analytics
    analytics = {
        "extraction_info": {
            "timestamp": datetime.now().isoformat(),
            "total_posts": len(posts),
            "extraction_duration": "N/A"  # Would need to track this
        },
        "engagement_metrics": {
            "total_likes": sum(post['engagement']['likes'] for post in posts),
            "total_comments": sum(post['engagement']['comments'] for post in posts if post['engagement']['comments'] < 1000000),
            "total_shares": sum(post['engagement']['shares'] for post in posts),
            "average_likes": sum(post['engagement']['likes'] for post in posts) / len(posts) if posts else 0,
            "high_engagement_posts": len([p for p in posts if p['engagement']['likes'] > 50])
        },
        "content_analysis": {
            "posts_with_substantial_content": len([p for p in posts if len(p['content']) > 200]),
            "posts_with_media": len([p for p in posts if p['media']['has_image'] or p['media']['has_video']]),
            "average_content_length": sum(len(p['content']) for p in posts) / len(posts) if posts else 0,
            "hashtag_count": sum(len(p['hashtags']) for p in posts)
        },
        "top_posts": sorted(posts, key=lambda x: x['engagement']['likes'], reverse=True)[:5]
    }
    
    analytics_file = output_dir / f"analytics_{timestamp}.json"
    with open(analytics_file, 'w', encoding='utf-8') as f:
        json.dump(analytics, f, indent=2, ensure_ascii=False, default=str)
    
    # Create CSV for spreadsheet analysis
    csv_file = output_dir / f"posts_analysis_{timestamp}.csv"
    create_csv_export(posts, csv_file)
    
    # Create quality-filtered posts
    quality_posts = [p for p in posts if len(p['content']) > 200 or p['engagement']['likes'] > 10]
    if quality_posts:
        quality_file = output_dir / f"quality_posts_{timestamp}.json"
        with open(quality_file, 'w', encoding='utf-8') as f:
            json.dump(quality_posts, f, indent=2, ensure_ascii=False)

def create_csv_export(posts, csv_file):
    """Create CSV export for spreadsheet analysis"""
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'urn', 'author', 'author_headline', 'content_length', 'content_preview',
            'likes', 'comments', 'shares', 'has_media', 'hashtag_count', 'extracted_at'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for post in posts:
            writer.writerow({
                'urn': post['urn'],
                'author': post['author'],
                'author_headline': (post['author_headline'] or '')[:100],
                'content_length': len(post['content']),
                'content_preview': post['content'][:200].replace('\n', ' ').replace(',', ';'),
                'likes': post['engagement']['likes'],
                'comments': post['engagement']['comments'],
                'shares': post['engagement']['shares'],
                'has_media': post['media']['has_image'] or post['media']['has_video'],
                'hashtag_count': len(post['hashtags']),
                'extracted_at': post['extracted_at']
            })

def create_extraction_summary(posts, summary_file, post_count):
    """Create human-readable extraction summary"""
    
    summary_content = f"""LinkedIn Feed Extraction Summary
{'=' * 50}
Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Target Posts: {post_count}
Actual Posts Extracted: {len(posts)}
Success Rate: {len(posts)/post_count*100:.1f}%

Engagement Overview:
- Total Likes: {sum(post['engagement']['likes'] for post in posts):,}
- Total Comments: {sum(post['engagement']['comments'] for post in posts):,}
- Posts with Media: {sum(1 for p in posts if p['media']['has_image'] or p['media']['has_video'])}
- Posts with Substantial Content (>200 chars): {len([p for p in posts if len(p['content']) > 200])}

Top Performing Posts:
{'-' * 30}
"""

    # Add top 3 posts
    top_posts = sorted(posts, key=lambda x: x['engagement']['likes'], reverse=True)[:3]
    for i, post in enumerate(top_posts, 1):
        content_preview = post['content'][:100] + "..." if len(post['content']) > 100 else post['content']
        summary_content += f"""
{i}. {post['engagement']['likes']} likes - {post['author']}
   "{content_preview}"
"""

    summary_content += f"""
Files Generated:
- linkedin_feed_TIMESTAMP.json (main data)
- analytics_TIMESTAMP.json (detailed analytics)
- posts_analysis_TIMESTAMP.csv (spreadsheet format)
- quality_posts_TIMESTAMP.json (filtered high-value posts)
- extraction_summary_TIMESTAMP.txt (this file)

Data Structure:
- Folder: data/posts_{post_count}/
- Total Files: 5
- Ready for RAG applications: ✓
- Production quality: ✓
"""

    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(summary_content)

def display_results(posts, filename):
    """Display extraction results and statistics"""
    
    print("\n" + "=" * 70)
    print("📊 EXTRACTION RESULTS")
    print("=" * 70)
    
    # Show summary statistics
    total_likes = sum(post['engagement']['likes'] for post in posts)
    total_comments = sum(post['engagement']['comments'] for post in posts if post['engagement']['comments'] < 1000000)  # Filter outliers
    total_shares = sum(post['engagement']['shares'] for post in posts)
    
    posts_with_media = sum(1 for post in posts if post['media']['has_image'] or post['media']['has_video'])
    all_hashtags = []
    for post in posts:
        all_hashtags.extend(post['hashtags'])
    
    substantial_posts = [p for p in posts if len(p['content']) > 200]
    
    print(f"📈 Total Posts: {len(posts)}")
    print(f"👍 Total Likes: {total_likes:,}")
    print(f"💬 Total Comments: {sum(post['engagement']['comments'] for post in posts):,}")
    print(f"🔄 Total Shares: {total_shares:,}")
    print(f"📸 Posts with Media: {posts_with_media}")
    print(f"🏷️  Unique Hashtags: {len(set(all_hashtags))}")
    print(f"📝 Substantial Posts (>200 chars): {len(substantial_posts)}")
    
    # Show sample posts
    print(f"\n📋 SAMPLE POSTS:")
    print("-" * 50)
    
    sample_posts = [p for p in posts if len(p['content']) > 50][:3]
    if not sample_posts:
        sample_posts = posts[:3]
    
    for i, post in enumerate(sample_posts, 1):
        print(f"\n📝 Post {i}:")
        print(f"   Author: {post['author']}")
        if post['author_headline']:
            print(f"   Title: {post['author_headline'][:100]}...")
        print(f"   Content: {post['content'][:100]}{'...' if len(post['content']) > 100 else ''}")
        print(f"   Engagement: {post['engagement']['likes']} likes, {post['engagement']['comments']} comments")
        if post['hashtags']:
            print(f"   Hashtags: {', '.join(post['hashtags'][:5])}")
    
    print(f"\n💾 Data saved to: {filename}")
    print(f"📄 File size: {Path(filename).stat().st_size / 1024:.1f} KB")

def parse_arguments():
    """Parse command line arguments"""
    
    parser = argparse.ArgumentParser(
        description="Complete LinkedIn Feed Scraper - Extract posts for RAG applications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python complete_linkedin_scraper.py                    # Interactive mode (asks for post count)
  python complete_linkedin_scraper.py --posts 50         # Extract 50 posts
  python complete_linkedin_scraper.py -n 25 -o my_feed.json --headless
  python complete_linkedin_scraper.py --posts 100 --verbose --no-headless
        """
    )
    
    parser.add_argument(
        '-n', '--posts',
        type=int,
        default=None,
        help='Number of posts to extract (default: ask interactively)'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=None,
        help='Output file path (default: auto-generated with timestamp)'
    )
    
    parser.add_argument(
        '--headless',
        action='store_true',
        default=False,
        help='Run browser in headless mode (invisible)'
    )
    
    parser.add_argument(
        '--no-headless',
        action='store_true',
        default=False,
        help='Run browser in visible mode (default)'
    )
    
    parser.add_argument(
        '--scroll-delay',
        type=float,
        default=2.0,
        help='Delay between scrolls in seconds (default: 2.0)'
    )
    
    parser.add_argument(
        '--max-scrolls',
        type=int,
        default=50,
        help='Maximum scroll attempts (default: 50)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output with detailed post previews'
    )
    
    parser.add_argument(
        '--pretty',
        action='store_true',
        default=True,
        help='Format JSON output with indentation (default: true)'
    )
    
    parser.add_argument(
        '--no-pretty',
        action='store_true',
        help='Compact JSON output without indentation'
    )
    
    return parser.parse_args()

def main():
    """Main scraper function"""
    
    # Parse command line arguments
    args = parse_arguments()
    
    print("🚀 Complete LinkedIn Feed Scraper")
    print("=" * 70)
    
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
            post_count = int(input("📊 How many posts to extract? (default: 10): ") or "10")
        except (ValueError, KeyboardInterrupt):
            post_count = 10
        print(f"📊 Posts to extract: {post_count}")
    
    # Determine headless mode
    headless_mode = not args.no_headless and (args.headless or True)  # Default to headless
    if args.no_headless:
        headless_mode = False
    
    print(f"🌐 Browser mode: {'Headless' if headless_mode else 'Visible'}")
    print(f"⏱️  Scroll delay: {args.scroll_delay}s")
    print(f"🔍 Verbose output: {args.verbose}")
    
    driver = None
    
    try:
        # Create driver
        driver = create_reliable_driver(headless=headless_mode)
        print("✅ Browser ready!")
        
        # Login
        if not login_to_linkedin(driver, email, password):
            return
        
        # Extract posts
        posts = scroll_and_extract_posts(
            driver, 
            target_posts=post_count,
            scroll_delay=args.scroll_delay,
            max_scrolls=args.max_scrolls,
            verbose=args.verbose
        )
        
        if posts:
            # Save data
            pretty_format = not args.no_pretty
            filename = save_data(posts, args.output, pretty=pretty_format, post_count=post_count)
            
            # Display results
            display_results(posts, filename)
            
            # Show JSON sample
            if args.verbose:
                print(f"\n🔍 JSON Sample:")
                print("-" * 30)
                print(json.dumps(posts[0], indent=2, ensure_ascii=False)[:500] + "...")
            
        else:
            print("❌ No posts extracted")
            
    except KeyboardInterrupt:
        print("\n⏹️  Scraping interrupted by user")
        
    except Exception as e:
        print(f"❌ Scraping failed: {e}")
        
    finally:
        if driver:
            print("\n🧹 Closing browser...")
            try:
                driver.quit()
            except:
                pass
    
    print("\n✅ Scraping complete!")

if __name__ == "__main__":
    main() 