#!/usr/bin/env python3
"""
LinkedIn Network Interceptor
Phase 3: Intercept GraphQL API calls for more reliable data extraction
"""

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

class LinkedInNetworkInterceptor:
    """Intercept LinkedIn GraphQL API calls for enhanced data extraction"""
    
    def __init__(self, headless=False):
        self.driver = None
        self.network_logs = []
        self.graphql_responses = []
        self.headless = headless
        
    def create_driver_with_logging(self):
        """Create Chrome driver with network logging enabled"""
        options = Options()
        
        # Basic options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        
        # Enable performance logging
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        
        # Stealth options
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        if self.headless:
            options.add_argument("--headless=new")
        
        # Window size
        options.add_argument("--window-size=1920,1080")
        
        try:
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            
            # Execute stealth script
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            print("✅ Network interceptor ready!")
            return True
            
        except Exception as e:
            print(f"❌ Failed to create driver: {e}")
            return False
    
    def login_to_linkedin(self):
        """Login to LinkedIn"""
        email = os.getenv('LINKEDIN_EMAIL')
        password = os.getenv('LINKEDIN_PASSWORD')
        
        if not email or not password:
            print("❌ LinkedIn credentials not found in .env file")
            return False
        
        try:
            print("🌐 Navigating to LinkedIn login...")
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(3)
            
            print("📝 Filling credentials...")
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
            
            print("🔐 Logging in...")
            # Click login
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for login to complete
            WebDriverWait(self.driver, 30).until(
                lambda driver: "/feed/" in driver.current_url or "/mynetwork/" in driver.current_url
            )
            
            print("✅ Login successful!")
            return True
            
        except Exception as e:
            print(f"❌ Login failed: {e}")
            return False
    
    def start_network_logging(self):
        """Start capturing network logs"""
        print("📡 Starting network logging...")
        self.network_logs = []
        self.graphql_responses = []
    
    def capture_network_logs(self):
        """Capture network logs from browser"""
        try:
            logs = self.driver.get_log("performance")
            for log in logs:
                try:
                    log_entry = json.loads(log["message"])
                    self.network_logs.append(log_entry)
                    
                    # Look for GraphQL responses
                    if "message" in log_entry:
                        message = log_entry["message"]
                        if "method" in message and message["method"] == "Network.responseReceived":
                            if "response" in message["params"]:
                                response = message["params"]["response"]
                                if "url" in response and "linkedin.com" in response["url"]:
                                    if "graphql" in response["url"].lower() or "voyager" in response["url"].lower():
                                        self.graphql_responses.append(response)
                except:
                    continue
                    
        except Exception as e:
            print(f"⚠️  Error capturing network logs: {e}")
    
    def extract_feed_data_from_graphql(self):
        """Extract feed data from GraphQL responses"""
        feed_posts = []
        
        for response in self.graphql_responses:
            try:
                if "body" in response:
                    body = response["body"]
                    if isinstance(body, str):
                        data = json.loads(body)
                        
                        # Look for feed data in GraphQL response
                        if "data" in data:
                            feed_data = self.parse_graphql_feed_data(data["data"])
                            if feed_data:
                                feed_posts.extend(feed_data)
                                
            except Exception as e:
                print(f"⚠️  Error parsing GraphQL response: {e}")
                continue
        
        return feed_posts
    
    def parse_graphql_feed_data(self, data):
        """Parse feed data from GraphQL response structure"""
        posts = []
        
        try:
            # Common LinkedIn GraphQL feed structures
            feed_paths = [
                "feed",
                "socialActivityFeed",
                "activities",
                "elements",
                "included"
            ]
            
            for path in feed_paths:
                if path in data:
                    feed_items = data[path]
                    if isinstance(feed_items, list):
                        for item in feed_items:
                            if isinstance(item, dict):
                                post = self.extract_post_from_graphql_item(item)
                                if post:
                                    posts.append(post)
                    break
                    
        except Exception as e:
            print(f"⚠️  Error parsing GraphQL feed data: {e}")
        
        return posts
    
    def extract_post_from_graphql_item(self, item):
        """Extract post data from GraphQL item"""
        try:
            post = {
                "urn": item.get("id") or item.get("urn"),
                "author": "Unknown",
                "content": "",
                "posted_at": None,
                "engagement": {
                    "likes": 0,
                    "comments": 0,
                    "shares": 0
                },
                "hashtags": [],
                "media": {
                    "has_image": False,
                    "has_video": False,
                    "urls": []
                },
                "extracted_at": datetime.now().isoformat(),
                "source": "graphql"
            }
            
            # Extract author information
            if "actor" in item:
                actor = item["actor"]
                if isinstance(actor, dict):
                    post["author"] = actor.get("name") or actor.get("title") or "Unknown"
                elif isinstance(actor, str):
                    post["author"] = actor
            
            # Extract content
            if "commentary" in item:
                commentary = item["commentary"]
                if isinstance(commentary, dict):
                    post["content"] = commentary.get("text") or ""
                elif isinstance(commentary, str):
                    post["content"] = commentary
            
            # Extract timestamp
            if "created" in item:
                created = item["created"]
                if isinstance(created, dict):
                    post["posted_at"] = created.get("time") or created.get("value")
                elif isinstance(created, (int, str)):
                    post["posted_at"] = created
            
            # Extract engagement
            if "socialDetail" in item:
                social_detail = item["socialDetail"]
                if isinstance(social_detail, dict):
                    post["engagement"]["likes"] = social_detail.get("totalSocialActivityCounts", {}).get("numLikes", 0)
                    post["engagement"]["comments"] = social_detail.get("totalSocialActivityCounts", {}).get("numComments", 0)
                    post["engagement"]["shares"] = social_detail.get("totalSocialActivityCounts", {}).get("numShares", 0)
            
            # Extract media
            if "media" in item:
                media = item["media"]
                if isinstance(media, list):
                    for media_item in media:
                        if isinstance(media_item, dict):
                            if media_item.get("type") == "image":
                                post["media"]["has_image"] = True
                                if "url" in media_item:
                                    post["media"]["urls"].append(media_item["url"])
                            elif media_item.get("type") == "video":
                                post["media"]["has_video"] = True
                                if "url" in media_item:
                                    post["media"]["urls"].append(media_item["url"])
            
            # Only return posts with content
            if post["content"] and len(post["content"]) > 10:
                return post
                
        except Exception as e:
            print(f"⚠️  Error extracting post from GraphQL item: {e}")
        
        return None
    
    def navigate_and_capture(self, target_posts=10, scroll_delay=2):
        """Navigate to feed and capture network data"""
        print(f"📱 Navigating to feed and capturing {target_posts} posts...")
        
        # Navigate to feed
        self.driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)
        
        # Start network logging
        self.start_network_logging()
        
        posts_found = 0
        scroll_attempts = 0
        max_scrolls = 50
        
        while posts_found < target_posts and scroll_attempts < max_scrolls:
            # Capture network logs
            self.capture_network_logs()
            
            # Extract posts from GraphQL data
            graphql_posts = self.extract_feed_data_from_graphql()
            
            if graphql_posts:
                posts_found = len(graphql_posts)
                print(f"📊 Found {posts_found} posts from GraphQL data")
                
                if posts_found >= target_posts:
                    break
            
            # Scroll for more content
            print(f"   🖱️  Scrolling for more posts... (attempt {scroll_attempts + 1})")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_delay)
            scroll_attempts += 1
        
        # Final capture
        self.capture_network_logs()
        
        # Extract final posts
        final_posts = self.extract_feed_data_from_graphql()
        
        print(f"\n✅ Network capture complete! Found {len(final_posts)} posts")
        return final_posts
    
    def save_network_data(self, posts, filename=None):
        """Save captured network data"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"network_capture_{timestamp}.json"
        
        data = {
            "timestamp": datetime.now().isoformat(),
            "total_posts": len(posts),
            "network_logs_count": len(self.network_logs),
            "graphql_responses_count": len(self.graphql_responses),
            "posts": posts,
            "metadata": {
                "capture_method": "network_interception",
                "version": "1.0"
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Network data saved to: {filename}")
        return filename
    
    def close(self):
        """Close the driver"""
        if self.driver:
            self.driver.quit()

def main():
    """Test network interceptor"""
    print("🔍 LINKEDIN NETWORK INTERCEPTOR")
    print("=" * 50)
    
    interceptor = LinkedInNetworkInterceptor(headless=False)
    
    try:
        # Create driver
        if not interceptor.create_driver_with_logging():
            return
        
        # Login
        if not interceptor.login_to_linkedin():
            return
        
        # Navigate and capture
        posts = interceptor.navigate_and_capture(target_posts=5, scroll_delay=2)
        
        if posts:
            # Save data
            filename = interceptor.save_network_data(posts)
            
            # Display results
            print(f"\n📊 CAPTURED {len(posts)} POSTS:")
            print("=" * 30)
            for i, post in enumerate(posts[:3], 1):
                print(f"\nPost {i}:")
                print(f"  Author: {post['author']}")
                print(f"  Content: {post['content'][:100]}...")
                print(f"  Engagement: {post['engagement']['likes']} likes, {post['engagement']['comments']} comments")
        else:
            print("❌ No posts captured from network data")
    
    except Exception as e:
        print(f"❌ Network interceptor error: {e}")
    
    finally:
        interceptor.close()

if __name__ == "__main__":
    main() 