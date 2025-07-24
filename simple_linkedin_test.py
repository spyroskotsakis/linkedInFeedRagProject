#!/usr/bin/env python3
"""
Simple LinkedIn Connection Test with Auto-managed Driver
This test automatically handles ChromeDriver version management.
"""

import os
import time
from pathlib import Path
from dotenv import load_dotenv

# Import selenium and webdriver manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def create_simple_driver():
    """Create a simple Chrome driver with auto-managed driver"""
    
    print("🔧 Setting up Chrome driver...")
    
    # Chrome options
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=en-US,en;q=0.9") 
    options.add_argument("--window-size=1280,900")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Use webdriver-manager to auto-install compatible driver
    service = Service(ChromeDriverManager().install())
    
    driver = webdriver.Chrome(service=service, options=options)
    
    # Remove webdriver flag
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def test_linkedin_access():
    """Test LinkedIn access with credentials"""
    
    print("🚀 Simple LinkedIn Connection Test")
    print("=" * 60)
    
    # Load credentials
    load_dotenv()
    email = os.getenv("LINKEDIN_EMAIL") 
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        print("❌ Error: No credentials found in .env file")
        return False
    
    print(f"📧 Testing with: {email}")
    print(f"🔑 Password: {'*' * len(password)}")
    
    driver = None
    
    try:
        # Create driver
        driver = create_simple_driver()
        print("✅ Chrome driver created successfully!")
        
        # Go to LinkedIn login
        print("🌐 Navigating to LinkedIn...")
        driver.get("https://www.linkedin.com/login")
        
        # Wait for login form
        wait = WebDriverWait(driver, 10)
        
        print("📝 Filling login form...")
        
        # Find and fill email
        email_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        email_field.clear()
        email_field.send_keys(email)
        
        # Find and fill password
        password_field = driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        print("🔐 Submitting login...")
        
        # Submit form
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        # Wait for redirect
        print("⏳ Waiting for authentication...")
        time.sleep(5)
        
        # Check if we're logged in
        current_url = driver.current_url
        
        if "feed" in current_url or "dashboard" in current_url:
            print("✅ Login successful!")
            
            # Try to go to feed
            if "feed" not in current_url:
                print("📱 Navigating to feed...")
                driver.get("https://www.linkedin.com/feed/")
                time.sleep(3)
            
            # Look for posts
            print("🔍 Looking for feed posts...")
            posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
            
            if posts:
                print(f"🎉 SUCCESS! Found {len(posts)} posts in your feed!")
                
                # Show sample post data
                if len(posts) > 0:
                    print("\n📋 Sample post preview:")
                    sample = posts[0]
                    post_id = sample.get_attribute("data-id")
                    print(f"   Post URN: {post_id}")
                    
                    # Try to extract some basic info
                    try:
                        # Look for author name
                        author_selectors = [
                            ".feed-shared-actor__name",
                            ".feed-shared-actor__title",
                            "[data-tracking-control-name='public_post_feed-actor-name']"
                        ]
                        
                        author = "Unknown"
                        for selector in author_selectors:
                            try:
                                author_elem = sample.find_element(By.CSS_SELECTOR, selector)
                                author = author_elem.text.strip()
                                if author:
                                    break
                            except:
                                continue
                        
                        print(f"   Author: {author}")
                        
                        # Look for post content
                        content_selectors = [
                            ".feed-shared-update-v2__description",
                            ".feed-shared-text",
                            "[data-tracking-control-name='public_post_feed-text']"
                        ]
                        
                        content = ""
                        for selector in content_selectors:
                            try:
                                content_elem = sample.find_element(By.CSS_SELECTOR, selector)
                                content = content_elem.text.strip()
                                if content:
                                    break
                            except:
                                continue
                        
                        if content:
                            preview = content[:100] + "..." if len(content) > 100 else content
                            print(f"   Content: {preview}")
                        
                        print("   ✅ Data extraction working!")
                        
                    except Exception as e:
                        print(f"   Note: {e}")
                
                return True
            else:
                print("⚠️  No posts found - your feed might be empty")
                return True
                
        elif "challenge" in current_url or "checkpoint" in current_url:
            print("🔒 LinkedIn security challenge detected")
            print("   You may need to verify your account manually")
            print("   Check the browser window for instructions")
            time.sleep(10)  # Give user time to see
            return False
            
        else:
            print("❌ Login failed - unexpected redirect")
            print(f"   Current URL: {current_url}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
        
    finally:
        if driver:
            print("\n🧹 Closing browser...")
            try:
                driver.quit()
            except:
                pass

def main():
    """Run the test"""
    
    success = test_linkedin_access()
    
    print("\n" + "=" * 60)
    
    if success:
        print("🎯 CONNECTION TEST PASSED!")
        print("\nYou're ready to run the full scraper:")
        print()
        print("🔥 RECOMMENDED COMMANDS:")
        print()
        print("1. Quick test (5 posts):")
        print("   python -m linkedin_feed_capture.cli.main capture --posts 5 --pretty --no-headless")
        print()
        print("2. Medium scrape (15 posts to file):")
        print("   python -m linkedin_feed_capture.cli.main capture --posts 15 --output data/my_feed.json --pretty")
        print()
        print("3. Streaming demo (watch posts appear live):")
        print("   python -m linkedin_feed_capture.cli.main capture --posts 10 --streaming --pretty --no-headless")
        print()
        print("✨ Ready to see your LinkedIn data!")
        
    else:
        print("❌ CONNECTION TEST FAILED!")
        print("\nTroubleshooting:")
        print("1. Check your LinkedIn credentials in .env")
        print("2. Make sure you can log in manually at linkedin.com")
        print("3. If there's a security challenge, complete it manually first")

if __name__ == "__main__":
    main() 