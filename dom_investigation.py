#!/usr/bin/env python3
"""
LinkedIn DOM Investigation Script
Phase 1: Analyze current LinkedIn DOM structure and find working selectors
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_investigation_driver():
    """Create a non-headless driver for DOM investigation"""
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--window-size=1920,1080")
    
    # Use webdriver-manager for ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Execute stealth script
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def login_to_linkedin(driver):
    """Login to LinkedIn"""
    email = os.getenv('LINKEDIN_EMAIL')
    password = os.getenv('LINKEDIN_PASSWORD')
    
    if not email or not password:
        print("❌ LinkedIn credentials not found in .env file")
        return False
    
    try:
        print("🌐 Navigating to LinkedIn login...")
        driver.get("https://www.linkedin.com/login")
        time.sleep(3)
        
        # Fill email
        email_field = driver.find_element(By.ID, "username")
        email_field.send_keys(email)
        
        # Fill password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        
        # Click login
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        
        # Wait for login to complete
        WebDriverWait(driver, 30).until(
            EC.url_contains("/feed/") or EC.url_contains("/mynetwork/")
        )
        
        print("✅ Login successful!")
        return True
        
    except Exception as e:
        print(f"❌ Login failed: {e}")
        return False

def investigate_post_structure(driver):
    """Investigate the structure of LinkedIn posts"""
    print("🔍 Investigating LinkedIn post structure...")
    
    # Navigate to feed
    driver.get("https://www.linkedin.com/feed/")
    time.sleep(5)
    
    # Find post elements
    posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
    print(f"📊 Found {len(posts)} posts")
    
    if not posts:
        print("❌ No posts found!")
        return None
    
    # Analyze first few posts
    investigation_results = []
    
    for i, post in enumerate(posts[:5]):  # Analyze first 5 posts
        print(f"\n🔍 Analyzing Post {i+1}:")
        
        post_data = {
            "post_index": i+1,
            "urn": post.get_attribute("data-id"),
            "selectors_tested": {}
        }
        
        # Test author selectors
        author_selectors = [
            ".feed-shared-actor__name",
            ".feed-shared-actor__title",
            "[data-tracking-control-name='public_post_feed-actor-name']",
            ".update-components-actor__name",
            ".feed-shared-actor__title-link",
            ".feed-shared-actor__name-link",
            "span[aria-hidden='true']",
            ".artdeco-entity-lockup__title",
            ".artdeco-entity-lockup__subtitle"
        ]
        
        post_data["selectors_tested"]["author"] = {}
        for selector in author_selectors:
            try:
                elements = post.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    text = elements[0].text.strip()
                    post_data["selectors_tested"]["author"][selector] = {
                        "found": True,
                        "text": text,
                        "count": len(elements)
                    }
                    print(f"   ✅ Author selector '{selector}': '{text}'")
                else:
                    post_data["selectors_tested"]["author"][selector] = {
                        "found": False,
                        "text": None,
                        "count": 0
                    }
            except Exception as e:
                post_data["selectors_tested"]["author"][selector] = {
                    "found": False,
                    "error": str(e)
                }
        
        # Test content selectors
        content_selectors = [
            ".feed-shared-update-v2__description",
            ".feed-shared-text",
            ".update-components-text",
            "[data-tracking-control-name='public_post_feed-text']",
            ".feed-shared-update-v2__description-wrapper",
            ".feed-shared-text__text-view",
            ".feed-shared-update-v2__description-text",
            ".artdeco-entity-lockup__description"
        ]
        
        post_data["selectors_tested"]["content"] = {}
        for selector in content_selectors:
            try:
                elements = post.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    text = elements[0].text.strip()
                    post_data["selectors_tested"]["content"][selector] = {
                        "found": True,
                        "text": text[:100] + "..." if len(text) > 100 else text,
                        "count": len(elements)
                    }
                    print(f"   ✅ Content selector '{selector}': '{text[:50]}...'")
                else:
                    post_data["selectors_tested"]["content"][selector] = {
                        "found": False,
                        "text": None,
                        "count": 0
                    }
            except Exception as e:
                post_data["selectors_tested"]["content"][selector] = {
                    "found": False,
                    "error": str(e)
                }
        
        # Test timestamp selectors
        time_selectors = [
            "time",
            ".feed-shared-actor__sub-description time",
            "[data-tracking-control-name='public_post_feed-actor-date']",
            ".feed-shared-actor__sub-description",
            ".feed-shared-actor__date",
            ".artdeco-entity-lockup__metadata"
        ]
        
        post_data["selectors_tested"]["timestamp"] = {}
        for selector in time_selectors:
            try:
                elements = post.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    text = elements[0].text.strip()
                    datetime_attr = elements[0].get_attribute("datetime")
                    post_data["selectors_tested"]["timestamp"][selector] = {
                        "found": True,
                        "text": text,
                        "datetime": datetime_attr,
                        "count": len(elements)
                    }
                    print(f"   ✅ Time selector '{selector}': '{text}' (datetime: {datetime_attr})")
                else:
                    post_data["selectors_tested"]["timestamp"][selector] = {
                        "found": False,
                        "text": None,
                        "datetime": None,
                        "count": 0
                    }
            except Exception as e:
                post_data["selectors_tested"]["timestamp"][selector] = {
                    "found": False,
                    "error": str(e)
                }
        
        # Test engagement selectors
        engagement_selectors = [
            ".social-details-social-counts__reactions-count",
            ".social-counts-reactions__count",
            "[data-tracking-control-name='public_post_feed-reactions-count']",
            ".social-details-social-counts__comments",
            ".social-counts-comments__count",
            "[data-tracking-control-name='public_post_feed-comments-count']",
            ".social-details-social-counts__shares",
            ".social-counts-shares__count"
        ]
        
        post_data["selectors_tested"]["engagement"] = {}
        for selector in engagement_selectors:
            try:
                elements = post.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    text = elements[0].text.strip()
                    post_data["selectors_tested"]["engagement"][selector] = {
                        "found": True,
                        "text": text,
                        "count": len(elements)
                    }
                    print(f"   ✅ Engagement selector '{selector}': '{text}'")
                else:
                    post_data["selectors_tested"]["engagement"][selector] = {
                        "found": False,
                        "text": None,
                        "count": 0
                    }
            except Exception as e:
                post_data["selectors_tested"]["engagement"][selector] = {
                    "found": False,
                    "error": str(e)
                }
        
        investigation_results.append(post_data)
    
    return investigation_results

def save_investigation_results(results):
    """Save investigation results to file"""
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"dom_investigation_results_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"📄 Investigation results saved to: {filename}")
    return filename

def main():
    """Main investigation function"""
    print("🔍 LINKEDIN DOM INVESTIGATION")
    print("=" * 50)
    
    driver = None
    try:
        # Create driver
        driver = create_investigation_driver()
        print("✅ Browser ready for investigation")
        
        # Login
        if not login_to_linkedin(driver):
            print("❌ Cannot proceed without login")
            return
        
        # Investigate post structure
        results = investigate_post_structure(driver)
        
        if results:
            # Save results
            filename = save_investigation_results(results)
            print(f"\n✅ DOM investigation complete! Results saved to {filename}")
            
            # Print summary
            print("\n📊 INVESTIGATION SUMMARY:")
            print("=" * 30)
            for i, post in enumerate(results):
                print(f"\nPost {i+1}:")
                for category, selectors in post["selectors_tested"].items():
                    working = sum(1 for s in selectors.values() if isinstance(s, dict) and s.get("found", False))
                    total = len(selectors)
                    print(f"  {category}: {working}/{total} selectors working")
        else:
            print("❌ Investigation failed - no results")
    
    except Exception as e:
        print(f"❌ Investigation error: {e}")
    
    finally:
        if driver:
            print("\n🧹 Closing browser...")
            driver.quit()

if __name__ == "__main__":
    main() 