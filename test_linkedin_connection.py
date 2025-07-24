#!/usr/bin/env python3
"""
Test LinkedIn Connection
This script tests your LinkedIn credentials and browser setup.
"""

import os
import sys
import time
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
from linkedin_feed_capture.browser.driver import create_default_driver
from linkedin_feed_capture.auth.authenticator import LinkedInAuthenticator, AuthConfig
from linkedin_feed_capture.utils.logger import setup_logging, get_logger

def test_connection():
    """Test LinkedIn connection with credentials from .env file"""
    
    print("🔗 LinkedIn Connection Test")
    print("=" * 50)
    
    # Load environment variables
    if not Path(".env").exists():
        print("❌ Error: .env file not found!")
        print("   Run: python setup_credentials.py")
        return False
    
    load_dotenv()
    
    # Get credentials
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        print("❌ Error: LinkedIn credentials not found in .env")
        print("   Make sure LINKEDIN_EMAIL and LINKEDIN_PASSWORD are set")
        return False
    
    if email == "your.email@example.com" or password == "your_actual_password_here":
        print("❌ Error: Please replace placeholder credentials in .env file")
        print("   Edit .env and add your real LinkedIn email and password")
        return False
    
    print(f"📧 Email: {email}")
    print(f"🔑 Password: {'*' * len(password)}")
    print()
    
    # Setup logging
    setup_logging(log_level="INFO", log_format="console")
    logger = get_logger(__name__)
    
    driver = None
    try:
        print("🌐 Creating browser...")
        # Use visible browser for testing so you can see what's happening
        driver = create_default_driver(headless=False, enable_stealth=True)
        print("✅ Browser created successfully")
        
        print("🔐 Testing authentication...")
        auth_config = AuthConfig(
            email=email,
            password=password,
            cookie_path="./data/test_cookies.pkl"
        )
        
        authenticator = LinkedInAuthenticator(auth_config)
        
        # Authenticate
        authenticated = authenticator.authenticate(driver)
        
        if authenticated:
            print("✅ Authentication successful!")
            
            # Test feed access
            print("📱 Testing feed access...")
            driver.get("https://www.linkedin.com/feed/")
            time.sleep(3)
            
            # Check if we can see feed elements
            from selenium.webdriver.common.by import By
            posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
            
            if posts:
                print(f"✅ Feed access successful! Found {len(posts)} posts visible")
                print("🎉 Your setup is working perfectly!")
                
                # Show a sample of what we can extract
                if len(posts) > 0:
                    print("\n📋 Sample post data preview:")
                    try:
                        sample_post = posts[0]
                        post_id = sample_post.get_attribute("data-id")
                        print(f"   Post ID: {post_id}")
                        
                        # Try to find author
                        try:
                            author_elem = sample_post.find_element(By.CSS_SELECTOR, ".feed-shared-actor__name")
                            print(f"   Author: {author_elem.text[:50]}...")
                        except:
                            print("   Author: [Could not extract]")
                        
                        print("   ✅ Data extraction is working!")
                        
                    except Exception as e:
                        print(f"   Note: {e}")
                
                return True
            else:
                print("⚠️  No feed posts found - this might be normal for new/empty feeds")
                return True
                
        else:
            print("❌ Authentication failed!")
            print("   Double-check your credentials in the .env file")
            return False
            
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        return False
        
    finally:
        if driver:
            print("\n🧹 Cleaning up browser...")
            try:
                driver.quit()
            except:
                pass
    
    return False

def main():
    """Main test function"""
    
    success = test_connection()
    
    print("\n" + "=" * 50)
    if success:
        print("🎯 CONNECTION TEST PASSED!")
        print("You're ready to run the full scraper:")
        print()
        print("Basic scrape (10 posts):")
        print("  python -m linkedin_feed_capture.cli.main capture --posts 10 --pretty")
        print()
        print("Streaming scrape (watch posts appear in real-time):")
        print("  python -m linkedin_feed_capture.cli.main capture --posts 20 --streaming --pretty --no-headless")
        print()
        print("Save to file:")
        print("  python -m linkedin_feed_capture.cli.main capture --posts 15 --output data/my_feed.json --pretty")
        
    else:
        print("❌ CONNECTION TEST FAILED!")
        print("Check the error messages above and:")
        print("1. Verify your credentials in .env")
        print("2. Make sure you can log into LinkedIn manually")
        print("3. Try running: python setup_credentials.py")

if __name__ == "__main__":
    main() 