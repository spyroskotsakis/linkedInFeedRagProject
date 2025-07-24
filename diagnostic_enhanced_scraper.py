#!/usr/bin/env python3
"""
Enhanced Diagnostic LinkedIn Scraper
=====================================

This version extends the working complete_linkedin_scraper.py with comprehensive
diagnostic capabilities to identify why posts are extracted with empty content.
"""

import time
import json
import re
import os
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DiagnosticEnhancedScraper:
    """Enhanced scraper with diagnostic capabilities"""
    
    def __init__(self):
        self.debug_log = []
        self.successful_selectors = {}
        self.failed_extractions = []
        
    def log_debug(self, message, post_urn=None, data=None):
        """Enhanced logging with post context"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "message": message,
            "post_urn": post_urn,
            "data": data
        }
        self.debug_log.append(log_entry)
        
        urn_info = f" [{post_urn}]" if post_urn else ""
        print(f"🔍 [{timestamp}]{urn_info} {message}")
        if data and len(str(data)) < 300:
            print(f"   📋 {data}")

    def setup_driver(self, headless=True):
        """Setup Chrome driver with enhanced stealth"""
        self.log_debug("Setting up enhanced diagnostic Chrome driver")
        
        options = Options()
        
        if headless:
            options.add_argument("--headless=new")
        
        # Enhanced stealth configuration
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        # Additional anti-detection measures
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
            
            self.log_debug("Enhanced driver setup successful")
            return driver
            
        except Exception as e:
            self.log_debug(f"Driver setup failed: {e}")
            raise

    def login_with_credentials(self, driver):
        """Enhanced login with better error handling"""
        self.log_debug("Starting enhanced login process")
        
        try:
            # Use existing credentials
            username = 'spyros.kotsakis@gmail.com'
            
            # Try to get password from environment or .env file
            password = os.getenv('LINKEDIN_PASSWORD')
            if not password:
                try:
                    with open('.env', 'r') as f:
                        content = f.read()
                        for line in content.split('\n'):
                            if line.startswith('LINKEDIN_PASSWORD='):
                                password = line.split('=', 1)[1].strip().strip('"\'')
                                break
                except:
                    pass
            
            if not password:
                self.log_debug("❌ No password available")
                return False
            
            # Navigate to login page
            driver.get("https://www.linkedin.com/login")
            time.sleep(3)
            
            # Fill credentials with human-like delays
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = driver.find_element(By.ID, "password")
            
            # Type with human-like delays
            for char in username:
                username_field.send_keys(char)
                time.sleep(0.05 + (0.1 * (time.time() % 1)))  # Random delay
            
            time.sleep(1)
            
            for char in password:
                password_field.send_keys(char)
                time.sleep(0.05 + (0.1 * (time.time() % 1)))  # Random delay
            
            time.sleep(2)
            
            # Submit form
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for redirect and handle potential challenges
            start_time = time.time()
            while time.time() - start_time < 30:  # 30 second timeout
                current_url = driver.current_url
                
                if "/feed" in current_url:
                    self.log_debug("✅ Login successful - redirected to feed")
                    return True
                elif "/checkpoint" in current_url or "/challenge" in current_url:
                    self.log_debug("⚠️ Security challenge detected")
                    return False
                elif "/login" in current_url:
                    # Check for error messages
                    try:
                        error_elem = driver.find_element(By.CSS_SELECTOR, ".form__label--error")
                        error_text = error_elem.text
                        self.log_debug(f"❌ Login error: {error_text}")
                        return False
                    except:
                        pass
                
                time.sleep(1)
            
            self.log_debug("❌ Login timeout")
            return False
            
        except Exception as e:
            self.log_debug(f"❌ Login failed with exception: {e}")
            return False

    def extract_post_data_diagnostic(self, post_element, index):
        """Enhanced post extraction with comprehensive diagnostics"""
        
        # Get URN first
        urn = post_element.get_attribute("data-id") or f"post_{index}"
        self.log_debug(f"Starting diagnostic extraction", urn)
        
        extraction_results = {
            "urn": urn,
            "author": "Unknown Author",
            "content": "",
            "engagement": {"likes": 0, "comments": 0, "shares": 0},
            "diagnostics": {
                "selectors_tested": {},
                "html_sample": "",
                "element_visible": False,
                "element_in_viewport": False
            }
        }
        
        try:
            # Check element visibility
            extraction_results["diagnostics"]["element_visible"] = post_element.is_displayed()
            
            # Check if element is in viewport
            location = post_element.location_once_scrolled_into_view
            extraction_results["diagnostics"]["element_in_viewport"] = location is not None
            
            # Get HTML sample for analysis
            try:
                html_sample = post_element.get_attribute("outerHTML")[:1000]
                extraction_results["diagnostics"]["html_sample"] = html_sample
            except:
                pass
            
            # Test author selectors
            author_selectors = [
                ("span[aria-hidden='true']", "Primary working selector"),
                (".feed-shared-actor__name", "Standard actor name"),
                (".feed-shared-actor__title", "Actor title"),
                (".update-components-actor__name", "Update components"),
                (".artdeco-entity-lockup__title", "Entity lockup"),
                ("h3 span[aria-hidden='true']", "H3 nested span"),
                (".feed-shared-actor__meta a span", "Meta link span")
            ]
            
            author_results = self._test_selector_group(post_element, "author", author_selectors, urn)
            extraction_results["diagnostics"]["selectors_tested"]["author"] = author_results
            
            # Extract author using best selector
            for selector, description in author_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    for elem in elements:
                        text = elem.text.strip()
                        if text and text != "•" and len(text) > 1:
                            extraction_results["author"] = text
                            self.log_debug(f"✅ Author found: {text}", urn)
                            break
                    if extraction_results["author"] != "Unknown Author":
                        break
                except:
                    continue
            
            # Test content selectors
            content_selectors = [
                (".feed-shared-update-v2__description", "Standard description"),
                (".feed-shared-text", "Shared text"),
                (".update-components-text", "Update components text"),
                (".feed-shared-inline-show-more-text", "Show more text"),
                ("[data-test-id='main-feed-activity-card__commentary']", "Commentary test ID"),
                (".activity-content-text", "Activity content"),
                (".feed-shared-text__text-view", "Text view"),
                (".feed-shared-update-v2__description .break-words", "Break words")
            ]
            
            content_results = self._test_selector_group(post_element, "content", content_selectors, urn)
            extraction_results["diagnostics"]["selectors_tested"]["content"] = content_results
            
            # Extract content using best selector
            for selector, description in content_selectors:
                try:
                    elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                    for elem in elements:
                        text = elem.text.strip()
                        if text and len(text) > 10:
                            extraction_results["content"] = text
                            self.log_debug(f"✅ Content found: {text[:50]}...", urn)
                            break
                    if extraction_results["content"]:
                        break
                except:
                    continue
            
            # Test engagement selectors
            engagement_selectors = [
                (".social-details-social-counts__reactions-count", "Reactions count"),
                (".social-counts-reactions__count", "Social counts"),
                ("button[aria-label*='like'] span", "Like button span"),
                (".feed-shared-social-action-bar__action-button span", "Action button"),
                (".social-counts__reactions", "Social reactions")
            ]
            
            engagement_results = self._test_selector_group(post_element, "engagement", engagement_selectors, urn)
            extraction_results["diagnostics"]["selectors_tested"]["engagement"] = engagement_results
            
            # Record if extraction was successful
            has_content = len(extraction_results["content"]) > 0
            has_author = extraction_results["author"] != "Unknown Author"
            
            if not has_content or not has_author:
                self.failed_extractions.append({
                    "urn": urn,
                    "missing_content": not has_content,
                    "missing_author": not has_author,
                    "diagnostics": extraction_results["diagnostics"]
                })
                self.log_debug(f"⚠️ Incomplete extraction - Content: {has_content}, Author: {has_author}", urn)
            else:
                self.log_debug(f"✅ Complete extraction", urn)
            
            return extraction_results
            
        except Exception as e:
            self.log_debug(f"❌ Extraction failed: {e}", urn)
            extraction_results["diagnostics"]["extraction_error"] = str(e)
            return extraction_results

    def _test_selector_group(self, post_element, group_name, selectors, urn):
        """Test a group of selectors and record results"""
        
        results = {}
        successful_count = 0
        
        for selector, description in selectors:
            try:
                elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                
                if elements:
                    valid_texts = []
                    for elem in elements:
                        text = elem.text.strip()
                        if text and len(text) > 1 and text not in ["•", "...", "more"]:
                            valid_texts.append(text)
                    
                    if valid_texts:
                        results[selector] = {
                            "success": True,
                            "description": description,
                            "element_count": len(elements),
                            "valid_texts": valid_texts[:2],  # First 2 valid texts
                            "element_visible": elements[0].is_displayed() if elements else False
                        }
                        successful_count += 1
                        
                        # Track globally successful selectors
                        if group_name not in self.successful_selectors:
                            self.successful_selectors[group_name] = {}
                        if selector not in self.successful_selectors[group_name]:
                            self.successful_selectors[group_name][selector] = 0
                        self.successful_selectors[group_name][selector] += 1
                        
                    else:
                        results[selector] = {
                            "success": False,
                            "description": description,
                            "element_count": len(elements),
                            "reason": "Elements found but no valid text"
                        }
                else:
                    results[selector] = {
                        "success": False,
                        "description": description,
                        "element_count": 0,
                        "reason": "No elements found"
                    }
                    
            except Exception as e:
                results[selector] = {
                    "success": False,
                    "description": description,
                    "element_count": 0,
                    "reason": f"Selector error: {str(e)}"
                }
        
        self.log_debug(f"{group_name} selectors: {successful_count}/{len(selectors)} worked", urn)
        return results

    def scroll_and_extract_posts_diagnostic(self, driver, target_posts=5, scroll_delay=3, max_scrolls=20):
        """Enhanced scrolling and extraction with diagnostics"""
        
        self.log_debug(f"Starting diagnostic extraction for {target_posts} posts")
        
        # Navigate to feed
        driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)  # Extended wait for feed to load
        
        extracted_posts = []
        seen_urns = set()
        scroll_attempts = 0
        
        while len(extracted_posts) < target_posts and scroll_attempts < max_scrolls:
            # Find all post elements
            posts = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
            self.log_debug(f"Found {len(posts)} post elements in DOM")
            
            new_posts_found = 0
            
            for i, post_element in enumerate(posts):
                try:
                    urn = post_element.get_attribute("data-id")
                    
                    if urn in seen_urns:
                        continue
                    
                    seen_urns.add(urn)
                    
                    self.log_debug(f"Processing post {len(extracted_posts) + 1}/{target_posts}", urn)
                    
                    # Scroll to element and wait for it to load
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", post_element)
                    time.sleep(2)  # Wait for content to load
                    
                    # Extract with diagnostics
                    post_data = self.extract_post_data_diagnostic(post_element, len(extracted_posts) + 1)
                    
                    if post_data:
                        extracted_posts.append(post_data)
                        new_posts_found += 1
                        
                        # Show progress
                        content_preview = post_data['content'][:60] + "..." if post_data['content'] else "[NO CONTENT]"
                        print(f"      ✅ {post_data['author']}: {content_preview}")
                        
                        if len(extracted_posts) >= target_posts:
                            break
                            
                except Exception as e:
                    self.log_debug(f"Error processing post: {e}", urn if 'urn' in locals() else None)
                    continue
            
            # Scroll if no new posts found
            if new_posts_found == 0:
                self.log_debug(f"Scrolling for more posts (attempt {scroll_attempts + 1})")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(scroll_delay)
                scroll_attempts += 1
            else:
                scroll_attempts = 0  # Reset if we found posts
        
        self.log_debug(f"Extraction complete! Found {len(extracted_posts)} posts")
        return extracted_posts

    def generate_diagnostic_report(self, posts):
        """Generate comprehensive diagnostic report"""
        
        timestamp = datetime.now().isoformat()
        
        # Calculate statistics
        total_posts = len(posts)
        posts_with_content = sum(1 for p in posts if p['content'])
        posts_with_author = sum(1 for p in posts if p['author'] != 'Unknown Author')
        
        report = {
            "timestamp": timestamp,
            "extraction_summary": {
                "total_posts": total_posts,
                "posts_with_content": posts_with_content,
                "posts_with_author": posts_with_author,
                "success_rate_content": round(posts_with_content / total_posts * 100, 1) if total_posts > 0 else 0,
                "success_rate_author": round(posts_with_author / total_posts * 100, 1) if total_posts > 0 else 0
            },
            "successful_selectors": self.successful_selectors,
            "failed_extractions": self.failed_extractions,
            "posts_data": posts,
            "debug_log": self.debug_log[-100:],  # Last 100 entries
            "recommendations": []
        }
        
        # Generate recommendations
        for group, selectors in self.successful_selectors.items():
            if selectors:
                best = max(selectors.items(), key=lambda x: x[1])
                report["recommendations"].append(
                    f"Best {group} selector: '{best[0]}' (worked {best[1]}/{total_posts} times)"
                )
            else:
                report["recommendations"].append(
                    f"⚠️ No working {group} selectors found"
                )
        
        return report

    def save_diagnostic_report(self, report):
        """Save comprehensive diagnostic report"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Create data directory if it doesn't exist
        Path("data").mkdir(exist_ok=True)
        
        # Save JSON report
        json_file = f"data/diagnostic_enhanced_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Save human-readable summary
        txt_file = f"data/diagnostic_enhanced_{timestamp}_summary.txt"
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write("Enhanced LinkedIn Scraper Diagnostic Report\n")
            f.write("=" * 70 + "\n\n")
            f.write(f"Analysis Date: {report['timestamp']}\n")
            f.write(f"Total Posts Analyzed: {report['extraction_summary']['total_posts']}\n")
            f.write(f"Posts with Content: {report['extraction_summary']['posts_with_content']}\n")
            f.write(f"Posts with Author: {report['extraction_summary']['posts_with_author']}\n")
            f.write(f"Content Success Rate: {report['extraction_summary']['success_rate_content']}%\n")
            f.write(f"Author Success Rate: {report['extraction_summary']['success_rate_author']}%\n\n")
            
            f.write("RECOMMENDATIONS:\n")
            f.write("-" * 20 + "\n")
            for rec in report['recommendations']:
                f.write(f"• {rec}\n")
            
            f.write("\nSUCCESSFUL SELECTORS BY CATEGORY:\n")
            f.write("-" * 40 + "\n")
            for group, selectors in report['successful_selectors'].items():
                f.write(f"\n{group.upper()}:\n")
                if selectors:
                    sorted_selectors = sorted(selectors.items(), key=lambda x: x[1], reverse=True)
                    for selector, count in sorted_selectors:
                        f.write(f"  ✅ {selector} (worked {count} times)\n")
                else:
                    f.write(f"  ❌ No working selectors found\n")
            
            f.write(f"\nFAILED EXTRACTIONS: {len(report['failed_extractions'])}\n")
            f.write("-" * 20 + "\n")
            for failure in report['failed_extractions'][:5]:  # Show first 5
                f.write(f"URN: {failure['urn']}\n")
                f.write(f"  Missing Content: {failure['missing_content']}\n")
                f.write(f"  Missing Author: {failure['missing_author']}\n\n")
        
        print(f"📋 Reports saved: {json_file}, {txt_file}")
        return json_file, txt_file


def main():
    """Run enhanced diagnostic extraction"""
    
    print("🚀 Enhanced LinkedIn Diagnostic Scraper")
    print("=" * 70)
    
    scraper = DiagnosticEnhancedScraper()
    
    try:
        # Setup driver (visible for debugging)
        driver = scraper.setup_driver(headless=True)
        
        # Login
        login_success = scraper.login_with_credentials(driver)
        if not login_success:
            print("❌ Login failed - cannot proceed with diagnostic")
            return
        
        # Run diagnostic extraction
        posts = scraper.scroll_and_extract_posts_diagnostic(
            driver, 
            target_posts=5, 
            scroll_delay=3, 
            max_scrolls=15
        )
        
        if not posts:
            print("❌ No posts extracted")
            return
        
        # Generate and save report
        report = scraper.generate_diagnostic_report(posts)
        json_file, txt_file = scraper.save_diagnostic_report(report)
        
        print(f"\n✅ Enhanced diagnostic complete!")
        print(f"📊 Results: {report['extraction_summary']['posts_with_content']}/{report['extraction_summary']['total_posts']} posts had content")
        print(f"📋 Check {txt_file} for detailed analysis")
        
        # Show quick recommendations
        print(f"\n📝 Quick Recommendations:")
        for rec in report['recommendations']:
            print(f"  • {rec}")
        
    except Exception as e:
        print(f"❌ Enhanced diagnostic failed: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main() 