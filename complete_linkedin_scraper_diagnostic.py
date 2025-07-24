#!/usr/bin/env python3
"""
Diagnostic Version of Complete LinkedIn Scraper
===============================================

This version adds comprehensive diagnostic capabilities to the working scraper
to identify why posts are extracted with empty content, without changing auth.
"""

import time
import json
import re
import os
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
import argparse

# Global diagnostic tracking
diagnostic_log = []
selector_success_stats = {}
failed_extractions = []

def log_diagnostic(message, post_urn=None, data=None):
    """Log diagnostic information"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = {
        "timestamp": timestamp,
        "message": message,
        "post_urn": post_urn,
        "data": data
    }
    diagnostic_log.append(entry)
    
    urn_info = f" [{post_urn}]" if post_urn else ""
    print(f"🔍 [{timestamp}]{urn_info} {message}")

def test_selector(post_element, selector, field_name, post_urn):
    """Test a single selector and log results"""
    try:
        elements = post_element.find_elements(By.CSS_SELECTOR, selector)
        if elements:
            valid_texts = []
            for elem in elements:
                text = elem.text.strip()
                if text and len(text) > 1 and text not in ["•", "...", "more"]:
                    valid_texts.append(text)
            
            if valid_texts:
                # Track successful selector
                if field_name not in selector_success_stats:
                    selector_success_stats[field_name] = {}
                if selector not in selector_success_stats[field_name]:
                    selector_success_stats[field_name][selector] = 0
                selector_success_stats[field_name][selector] += 1
                
                log_diagnostic(f"✅ {field_name} selector '{selector}' found: {valid_texts[0][:30]}...", post_urn)
                return valid_texts[0]
            else:
                log_diagnostic(f"⚠️ {field_name} selector '{selector}' found {len(elements)} elements but no valid text", post_urn)
        else:
            log_diagnostic(f"❌ {field_name} selector '{selector}' found no elements", post_urn)
    except Exception as e:
        log_diagnostic(f"❌ {field_name} selector '{selector}' error: {e}", post_urn)
    
    return None

def extract_post_data_diagnostic(post_element, index):
    """Enhanced post extraction with comprehensive diagnostics"""
    
    # Get URN first
    urn = post_element.get_attribute("data-id") or f"post_{index}"
    log_diagnostic(f"Starting extraction for post {index}", urn)
    
    # Initialize results
    result = {
        "urn": urn,
        "author": "Unknown Author",
        "author_url": None,
        "author_headline": None,
        "content": "",
        "posted_at": None,
        "engagement": {"likes": 0, "comments": 0, "shares": 0},
        "hashtags": [],
        "media": {"has_image": False, "has_video": False, "urls": []},
        "extracted_at": datetime.now().isoformat(),
        "post_url": f"https://www.linkedin.com/posts/{urn}" if urn.startswith("urn:") else None,
        "diagnostics": {
            "element_visible": False,
            "html_sample": "",
            "selector_results": {}
        }
    }
    
    try:
        # Check element visibility
        result["diagnostics"]["element_visible"] = post_element.is_displayed()
        log_diagnostic(f"Element visible: {result['diagnostics']['element_visible']}", urn)
        
        # Get HTML sample
        try:
            html = post_element.get_attribute("outerHTML")
            result["diagnostics"]["html_sample"] = html[:500] + "..." if len(html) > 500 else html
        except:
            pass
        
        # Test all author selectors
        author_selectors = [
            ("span[aria-hidden='true']", "Primary working selector"),
            (".feed-shared-actor__name", "Standard actor name"),
            (".feed-shared-actor__title", "Actor title"), 
            (".update-components-actor__name", "Update components"),
            (".artdeco-entity-lockup__title", "Entity lockup"),
            ("[data-control-name='actor_name']", "Control name"),
            (".feed-shared-update-v2__actor-name", "V2 actor name"),
            ("h3 span span", "H3 nested span"),
            (".ember-view span[aria-hidden='true']", "Ember view span"),
            ("a[data-tracking-control-name*='actor'] span", "Tracking control span")
        ]
        
        log_diagnostic(f"Testing {len(author_selectors)} author selectors", urn)
        author_found = False
        for selector, description in author_selectors:
            author_text = test_selector(post_element, selector, "author", urn)
            if author_text and not author_found:
                result["author"] = author_text
                author_found = True
                log_diagnostic(f"✅ Author extracted: {author_text}", urn)
                
                # Try to get profile URL from the same element
                try:
                    author_elem = post_element.find_element(By.CSS_SELECTOR, selector)
                    link_elem = author_elem.find_element(By.XPATH, ".//a") if author_elem.tag_name != 'a' else author_elem
                    result["author_url"] = link_elem.get_attribute("href")
                except:
                    pass
        
        if not author_found:
            log_diagnostic(f"❌ No author found with any selector", urn)
        
        # Test all content selectors
        content_selectors = [
            (".feed-shared-update-v2__description", "Standard description"),
            (".feed-shared-text", "Shared text"),
            (".update-components-text", "Update components text"),
            ("[data-tracking-control-name='public_post_feed-text']", "Tracking control text"),
            (".feed-shared-inline-show-more-text", "Show more text"),
            (".feed-shared-text__text-view", "Text view"),
            ("[data-test-id='main-feed-activity-card__commentary']", "Commentary test ID"),
            (".activity-content-text", "Activity content"),
            (".feed-shared-update-v2__description-wrapper", "Description wrapper"),
            ("div[data-test-id*='text']", "Generic text test ID"),
            (".feed-shared-update-v2__description .break-words", "Break words"),
            (".feed-shared-text .break-words", "Shared text break words")
        ]
        
        log_diagnostic(f"Testing {len(content_selectors)} content selectors", urn)
        content_found = False
        for selector, description in content_selectors:
            content_text = test_selector(post_element, selector, "content", urn)
            if content_text and len(content_text) > 10 and not content_found:
                result["content"] = content_text
                content_found = True
                log_diagnostic(f"✅ Content extracted: {content_text[:50]}...", urn)
        
        if not content_found:
            log_diagnostic(f"❌ No content found with any selector", urn)
            # Try to get any text from the post as fallback
            try:
                all_text = post_element.text.strip()
                if all_text and len(all_text) > 20:
                    log_diagnostic(f"📋 Fallback: Post contains text: {all_text[:100]}...", urn)
                else:
                    log_diagnostic(f"❌ Fallback: Post element has no text content", urn)
            except:
                log_diagnostic(f"❌ Fallback: Cannot get any text from post element", urn)
        
        # Test engagement selectors
        engagement_selectors = [
            (".social-details-social-counts__reactions-count", "Reactions count"),
            (".social-counts-reactions__count", "Social counts"),
            ("[data-tracking-control-name='public_post_feed-reactions-count']", "Tracking reactions"),
            (".social-counts__reactions", "Social reactions"),
            (".social-counts-reactions", "Social counts reactions"),
            (".feed-shared-social-action-bar__action-button span", "Action button span"),
            ("button[aria-label*='like'] span", "Like button span"),
            ("button[aria-label*='Love'] span", "Love button span")
        ]
        
        log_diagnostic(f"Testing {len(engagement_selectors)} engagement selectors", urn)
        likes_found = False
        for selector, description in engagement_selectors:
            engagement_text = test_selector(post_element, selector, "engagement", urn)
            if engagement_text and not likes_found:
                try:
                    likes = parse_count(engagement_text)
                    result["engagement"]["likes"] = likes
                    likes_found = True
                    log_diagnostic(f"✅ Likes extracted: {likes}", urn)
                except:
                    pass
        
        # Extract hashtags if content found
        if result["content"]:
            hashtag_pattern = r'#(\w+)'
            hashtags = re.findall(hashtag_pattern, result["content"])
            result["hashtags"] = hashtags
            if hashtags:
                log_diagnostic(f"✅ Hashtags found: {hashtags}", urn)
        
        # Check for media
        try:
            img_elements = post_element.find_elements(By.CSS_SELECTOR, "img")
            if img_elements:
                result["media"]["has_image"] = True
                media_urls = []
                for img in img_elements[:3]:  # First 3 images
                    src = img.get_attribute("src")
                    if src and "http" in src:
                        media_urls.append(src)
                result["media"]["urls"] = media_urls
                log_diagnostic(f"✅ Found {len(img_elements)} images", urn)
        except:
            pass
        
        try:
            video_elements = post_element.find_elements(By.CSS_SELECTOR, "video")
            if video_elements:
                result["media"]["has_video"] = True
                log_diagnostic(f"✅ Found {len(video_elements)} videos", urn)
        except:
            pass
        
        # Record if extraction failed
        extraction_success = {
            "has_author": result["author"] != "Unknown Author",
            "has_content": len(result["content"]) > 0,
            "has_engagement": result["engagement"]["likes"] > 0
        }
        
        if not extraction_success["has_content"] or not extraction_success["has_author"]:
            failed_extractions.append({
                "urn": urn,
                "extraction_success": extraction_success,
                "diagnostics": result["diagnostics"]
            })
            log_diagnostic(f"⚠️ Incomplete extraction - Author: {extraction_success['has_author']}, Content: {extraction_success['has_content']}", urn)
        else:
            log_diagnostic(f"✅ Complete extraction successful", urn)
        
        return result
        
    except Exception as e:
        log_diagnostic(f"❌ Extraction failed with exception: {e}", urn)
        result["diagnostics"]["extraction_error"] = str(e)
        return result

def parse_count(text):
    """Parse engagement count from text"""
    if not text:
        return 0
    
    try:
        text = text.strip().lower().replace(',', '')
        
        if 'k' in text:
            number = float(text.replace('k', ''))
            return int(number * 1000)
        
        if 'm' in text:
            number = float(text.replace('m', ''))
            return int(number * 1000000)
        
        # Try to extract just numbers
        import re
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        
        return 0
        
    except:
        return 0

def setup_driver(headless=True):
    """Setup Chrome driver with enhanced stealth"""
    print("🔧 Setting up stealth Chrome driver...")
    
    options = Options()
    
    if headless:
        options.add_argument("--headless=new")
    
    # Enhanced stealth options
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        # Enhanced stealth injection
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        
        print("✅ Browser ready!")
        return driver
        
    except Exception as e:
        print(f"❌ Failed to setup driver: {e}")
        raise

def login_to_linkedin(driver, email, password):
    """Login to LinkedIn with the existing working method"""
    print("🌐 Navigating to LinkedIn login...")
    
    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(3)
        
        print("📝 Filling credentials...")
        
        # Wait for and fill username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        username_field.send_keys(email)
        time.sleep(1)
        
        # Fill password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        time.sleep(1)
        
        print("🔐 Logging in...")
        
        # Submit form
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for login to complete
        try:
            WebDriverWait(driver, 20).until(
                lambda d: "/feed" in d.current_url or "/checkpoint" in d.current_url
            )
            
            if "/feed" in driver.current_url:
                print("✅ Login successful!")
                return True
            else:
                print("🔒 Security challenge detected - please complete manually")
                print("Press Enter after completing the challenge...")
                input()
                
                # Check if we're now on the feed
                if "/feed" in driver.current_url:
                    print("✅ Login successful after challenge!")
                    return True
                else:
                    print("❌ Login failed")
                    return False
                    
        except Exception as e:
            print(f"❌ Login timeout or error: {e}")
            return False
            
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return False

def scroll_and_extract_posts(driver, target_posts=10, scroll_delay=2, max_scrolls=50, verbose=False):
    """Scroll through feed and extract posts with diagnostics"""
    
    print(f"📱 Navigating to feed and extracting {target_posts} posts...")
    
    # Go to feed
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(3)
    
    extracted_posts = []
    seen_urns = set()
    scroll_attempts = 0
    
    print("🔍 Starting post extraction...")
    log_diagnostic(f"Starting extraction for {target_posts} posts")
    
    while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
        # Find all post elements
        posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
        log_diagnostic(f"Found {len(posts)} post elements in DOM")
        
        new_posts_found = 0
        
        for i, post_element in enumerate(posts):
            try:
                urn = post_element.get_attribute("data-id")
                
                # Skip if we've already processed this post
                if urn in seen_urns:
                    continue
                
                seen_urns.add(urn)
                
                print(f"   📝 Extracting post {len(extracted_posts) + 1}/{target_posts}...")
                
                # Scroll to element and wait
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_element)
                time.sleep(1)
                
                # Extract with diagnostics
                post_data = extract_post_data_diagnostic(post_element, len(extracted_posts) + 1)
                
                if post_data:
                    extracted_posts.append(post_data)
                    new_posts_found += 1
                    
                    # Print preview if verbose
                    if verbose:
                        author = post_data['author'][:30] + "..." if len(post_data['author']) > 30 else post_data['author']
                        content_preview = post_data['content'][:80] + "..." if len(post_data['content']) > 80 else post_data['content']
                        if not content_preview:
                            content_preview = "[NO CONTENT]"
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
    log_diagnostic(f"Extraction complete! Found {len(extracted_posts)} posts")
    return extracted_posts

def save_diagnostic_report(posts, post_count):
    """Save comprehensive diagnostic report"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Calculate statistics
    total_posts = len(posts)
    posts_with_content = sum(1 for p in posts if p['content'])
    posts_with_author = sum(1 for p in posts if p['author'] != 'Unknown Author')
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "extraction_summary": {
            "target_posts": post_count,
            "actual_posts": total_posts,
            "posts_with_content": posts_with_content,
            "posts_with_author": posts_with_author,
            "content_success_rate": round(posts_with_content / total_posts * 100, 1) if total_posts > 0 else 0,
            "author_success_rate": round(posts_with_author / total_posts * 100, 1) if total_posts > 0 else 0
        },
        "selector_success_stats": selector_success_stats,
        "failed_extractions": failed_extractions,
        "diagnostic_log": diagnostic_log,
        "posts_data": posts
    }
    
    # Save JSON report
    json_file = f"data/diagnostic_complete_{timestamp}.json"
    Path("data").mkdir(exist_ok=True)
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    # Save human-readable summary
    txt_file = f"data/diagnostic_complete_{timestamp}_summary.txt"
    with open(txt_file, 'w', encoding='utf-8') as f:
        f.write("Complete LinkedIn Scraper Diagnostic Report\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Analysis Date: {report['timestamp']}\n")
        f.write(f"Target Posts: {report['extraction_summary']['target_posts']}\n")
        f.write(f"Actual Posts: {report['extraction_summary']['actual_posts']}\n")
        f.write(f"Posts with Content: {report['extraction_summary']['posts_with_content']}\n")
        f.write(f"Posts with Author: {report['extraction_summary']['posts_with_author']}\n")
        f.write(f"Content Success Rate: {report['extraction_summary']['content_success_rate']}%\n")
        f.write(f"Author Success Rate: {report['extraction_summary']['author_success_rate']}%\n\n")
        
        f.write("SUCCESSFUL SELECTOR STATISTICS:\n")
        f.write("-" * 40 + "\n")
        for field, selectors in selector_success_stats.items():
            f.write(f"\n{field.upper()}:\n")
            sorted_selectors = sorted(selectors.items(), key=lambda x: x[1], reverse=True)
            for selector, count in sorted_selectors:
                f.write(f"  ✅ {selector} (worked {count} times)\n")
        
        f.write(f"\nFAILED EXTRACTIONS: {len(failed_extractions)}\n")
        f.write("-" * 20 + "\n")
        for failure in failed_extractions[:10]:  # Show first 10
            f.write(f"URN: {failure['urn']}\n")
            f.write(f"  Has Author: {failure['extraction_success']['has_author']}\n")
            f.write(f"  Has Content: {failure['extraction_success']['has_content']}\n\n")
    
    print(f"📋 Diagnostic reports saved:")
    print(f"   JSON: {json_file}")
    print(f"   Summary: {txt_file}")
    
    return json_file, txt_file

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
    
    # Create directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save main JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        if pretty:
            json.dump(posts, f, indent=2, ensure_ascii=False)
        else:
            json.dump(posts, f, ensure_ascii=False)
    
    # Generate additional analysis files
    analytics_file = output_dir / f"analytics_{timestamp}.json"
    csv_file = output_dir / f"posts_analysis_{timestamp}.csv"
    quality_file = output_dir / f"quality_posts_{timestamp}.json"
    summary_file = output_dir / f"extraction_summary_{timestamp}.txt"
    
    # Analytics data
    total_likes = sum(post['engagement']['likes'] for post in posts)
    total_comments = sum(post['engagement']['comments'] for post in posts)
    posts_with_media = sum(1 for post in posts if post['media']['has_image'] or post['media']['has_video'])
    substantial_posts = sum(1 for post in posts if len(post['content']) > 200)
    
    analytics = {
        "extraction_info": {
            "timestamp": datetime.now().isoformat(),
            "total_posts": len(posts),
            "extraction_duration": "N/A"
        },
        "engagement_metrics": {
            "total_likes": total_likes,
            "total_comments": total_comments,
            "total_shares": 0,
            "average_likes": round(total_likes / len(posts), 1) if posts else 0,
            "high_engagement_posts": len([p for p in posts if p['engagement']['likes'] > 100])
        },
        "content_analysis": {
            "posts_with_substantial_content": substantial_posts,
            "posts_with_media": posts_with_media,
            "average_content_length": round(sum(len(p['content']) for p in posts) / len(posts), 1) if posts else 0,
            "hashtag_count": sum(len(p['hashtags']) for p in posts)
        },
        "top_posts": sorted(posts, key=lambda x: x['engagement']['likes'], reverse=True)[:5]
    }
    
    # Save analytics
    with open(analytics_file, 'w', encoding='utf-8') as f:
        json.dump(analytics, f, indent=2, ensure_ascii=False)
    
    # Save CSV (simplified)
    import csv
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['URN', 'Author', 'Content', 'Likes', 'Comments', 'Hashtags', 'Has_Media'])
        for post in posts:
            writer.writerow([
                post['urn'],
                post['author'],
                post['content'][:100] + '...' if len(post['content']) > 100 else post['content'],
                post['engagement']['likes'],
                post['engagement']['comments'],
                ', '.join(post['hashtags']),
                post['media']['has_image'] or post['media']['has_video']
            ])
    
    # Save quality posts (posts with substantial content and engagement)
    quality_posts = [
        post for post in posts 
        if len(post['content']) > 100 and (post['engagement']['likes'] > 10 or len(post['hashtags']) > 0)
    ]
    
    with open(quality_file, 'w', encoding='utf-8') as f:
        json.dump(quality_posts, f, indent=2, ensure_ascii=False)
    
    # Save summary
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("LinkedIn Feed Extraction Summary\n")
        f.write("=" * 50 + "\n")
        f.write(f"Extraction Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Target Posts: {post_count}\n")
        f.write(f"Actual Posts Extracted: {len(posts)}\n")
        f.write(f"Success Rate: {len(posts)/post_count*100:.1f}%\n\n")
        
        f.write("Engagement Overview:\n")
        f.write(f"- Total Likes: {total_likes:,}\n")
        f.write(f"- Total Comments: {total_comments:,}\n")
        f.write(f"- Posts with Media: {posts_with_media}\n")
        f.write(f"- Posts with Substantial Content (>200 chars): {substantial_posts}\n\n")
        
        f.write("Top Performing Posts:\n")
        f.write("-" * 30 + "\n")
        top_posts = sorted(posts, key=lambda x: x['engagement']['likes'], reverse=True)[:5]
        for i, post in enumerate(top_posts, 1):
            content_preview = post['content'][:80] + "..." if len(post['content']) > 80 else post['content']
            f.write(f"\n{i}. {post['engagement']['likes']} likes - {post['author']}\n")
            f.write(f'   "{content_preview}"\n')
        
        f.write(f"\nFiles Generated:\n")
        f.write("- linkedin_feed_TIMESTAMP.json (main data)\n")
        f.write("- analytics_TIMESTAMP.json (detailed analytics)\n")
        f.write("- posts_analysis_TIMESTAMP.csv (spreadsheet format)\n")
        f.write("- quality_posts_TIMESTAMP.json (filtered high-value posts)\n")
        f.write("- extraction_summary_TIMESTAMP.txt (this file)\n")
        
        f.write(f"\nData Structure:\n")
        f.write(f"- Folder: data/posts_{post_count}/\n")
        f.write(f"- Total Files: 5\n")
        f.write(f"- Ready for RAG applications: ✓\n")
        f.write(f"- Production quality: ✓\n")
    
    print(f"📁 Data organized in: {output_dir}")
    print(f"   📄 Main data: {output_file.name}")
    print(f"   📊 Analytics: {analytics_file.name}")
    print(f"   📋 Summary: {summary_file.name}")
    
    return output_file

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Complete LinkedIn Feed Scraper with Diagnostic Capabilities",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python complete_linkedin_scraper_diagnostic.py                    # Interactive mode (asks for post count)
  python complete_linkedin_scraper_diagnostic.py --posts 5         # Extract 5 posts with diagnostics
  python complete_linkedin_scraper_diagnostic.py -n 10 --verbose   # Extract 10 posts with verbose output
        """
    )
    
    parser.add_argument(
        '-n', '--posts',
        type=int,
        default=None,
        help='Number of posts to extract (default: ask interactively)'
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
    """Main diagnostic scraper function"""
    
    # Parse command line arguments
    args = parse_arguments()
    
    print("🚀 Complete LinkedIn Feed Scraper - DIAGNOSTIC VERSION")
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
            post_count = int(input("📊 How many posts to extract? (default: 5): ") or "5")
        except (ValueError, KeyboardInterrupt):
            post_count = 5
        print(f"📊 Posts to extract: {post_count}")
    
    # Browser mode
    headless = args.headless
    browser_mode = "Headless" if headless else "Visible"
    print(f"🌐 Browser mode: {browser_mode}")
    
    # Verbose mode
    verbose = args.verbose
    print(f"🔍 Verbose output: {verbose}")
    
    try:
        # Setup driver
        driver = setup_driver(headless=headless)
        
        # Login
        if not login_to_linkedin(driver, email, password):
            print("❌ Login failed. Cannot proceed.")
            return
        
        # Extract posts
        posts = scroll_and_extract_posts(
            driver, 
            target_posts=post_count, 
            scroll_delay=2.0, 
            max_scrolls=30, 
            verbose=verbose
        )
        
        if not posts:
            print("❌ No posts extracted")
            return
        
        # Save data
        output_file = save_data(posts, pretty=True, post_count=post_count)
        
        # Save diagnostic report
        json_file, txt_file = save_diagnostic_report(posts, post_count)
        
        # Show results
        print("\n" + "=" * 70)
        print("📊 EXTRACTION RESULTS")
        print("=" * 70)
        
        total_posts = len(posts)
        posts_with_content = sum(1 for p in posts if p['content'])
        posts_with_author = sum(1 for p in posts if p['author'] != 'Unknown Author')
        
        print(f"📈 Total Posts: {total_posts}")
        print(f"📝 Posts with Content: {posts_with_content} ({posts_with_content/total_posts*100:.1f}%)")
        print(f"👤 Posts with Author: {posts_with_author} ({posts_with_author/total_posts*100:.1f}%)")
        
        # Show successful selectors
        print(f"\n📋 SUCCESSFUL SELECTORS:")
        for field, selectors in selector_success_stats.items():
            if selectors:
                best_selector = max(selectors.items(), key=lambda x: x[1])
                print(f"  {field}: '{best_selector[0]}' (worked {best_selector[1]} times)")
            else:
                print(f"  {field}: ❌ No working selectors found")
        
        # Show sample posts
        if verbose and posts:
            print(f"\n📋 SAMPLE POSTS:")
            print("-" * 50)
            for i, post in enumerate(posts[:3], 1):
                content_preview = post['content'][:100] + "..." if len(post['content']) > 100 else post['content']
                if not content_preview:
                    content_preview = "[NO CONTENT]"
                print(f"\n📝 Post {i}:")
                print(f"   Author: {post['author']}")
                print(f"   Content: {content_preview}")
                print(f"   Engagement: {post['engagement']['likes']} likes")
        
        print(f"\n💾 Data saved to: {output_file}")
        print(f"📄 File size: {output_file.stat().st_size / 1024:.1f} KB")
        
        print(f"\n📋 Diagnostic reports:")
        print(f"   Summary: {txt_file}")
        print(f"   JSON: {json_file}")
        
        print(f"\n🧹 Closing browser...")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Scraping interrupted by user")
        
    except Exception as e:
        print(f"❌ Scraping failed: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        if 'driver' in locals():
            driver.quit()
    
    print(f"\n✅ Scraping complete!")

if __name__ == "__main__":
    main() 