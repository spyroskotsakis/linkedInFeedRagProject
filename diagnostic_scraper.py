#!/usr/bin/env python3
"""
Diagnostic LinkedIn Scraper - Phase 1.1
========================================

This diagnostic version helps identify why posts are extracted with empty content.
It logs DOM structure, tests multiple selectors, and provides detailed debugging info.
"""

import time
import json
import re
from datetime import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DiagnosticLinkedInScraper:
    """Diagnostic scraper to identify selector and DOM issues"""
    
    def __init__(self):
        self.debug_log = []
        self.successful_selectors = {}
        self.failed_selectors = {}
        
    def log_debug(self, message, data=None):
        """Add debug message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "message": message,
            "data": data
        }
        self.debug_log.append(log_entry)
        print(f"🔍 [{timestamp}] {message}")
        if data:
            print(f"   📋 {data}")
    
    def setup_driver(self, headless=True):
        """Setup Chrome driver with debug capabilities"""
        self.log_debug("Setting up diagnostic Chrome driver")
        
        options = Options()
        if headless:
            options.add_argument("--headless=new")
        
        # Standard stealth options
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            
            # Remove webdriver property
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            self.log_debug("Driver setup successful")
            return driver
            
        except Exception as e:
            self.log_debug(f"Driver setup failed: {e}")
            raise
    
    def test_selectors_on_post(self, driver, post_element, post_index):
        """Test all possible selectors on a single post element"""
        
        self.log_debug(f"Testing selectors on post {post_index}")
        
        # Get the URN first
        urn = post_element.get_attribute("data-id")
        self.log_debug(f"Post URN: {urn}")
        
        # Test author selectors
        author_selectors = [
            "span[aria-hidden='true']",  # From working version
            ".feed-shared-actor__name",
            ".feed-shared-actor__title", 
            ".update-components-actor__name",
            ".artdeco-entity-lockup__title",
            ".feed-shared-update-v2__actor-name",
            "[data-control-name='actor_name']",
            "h3 span span",  # Alternative structure
            ".ember-view span[aria-hidden='true']",
            "a[data-tracking-control-name*='actor'] span"
        ]
        
        author_results = self._test_selector_group(post_element, "author", author_selectors)
        
        # Test content selectors
        content_selectors = [
            ".feed-shared-update-v2__description",
            ".feed-shared-text",
            ".update-components-text",
            "[data-tracking-control-name='public_post_feed-text']",
            ".feed-shared-inline-show-more-text",
            ".feed-shared-text__text-view",
            "[data-test-id='main-feed-activity-card__commentary']",
            ".activity-content-text",
            ".feed-shared-update-v2__description-wrapper",
            "div[data-test-id*='text']"
        ]
        
        content_results = self._test_selector_group(post_element, "content", content_selectors)
        
        # Test engagement selectors
        engagement_selectors = [
            ".social-details-social-counts__reactions-count",
            ".social-counts-reactions__count", 
            "[data-tracking-control-name='public_post_feed-reactions-count']",
            ".social-counts__reactions",
            ".social-counts-reactions",
            ".feed-shared-social-action-bar__action-button span",
            "button[aria-label*='like'] span",
            "button[aria-label*='Love'] span"
        ]
        
        engagement_results = self._test_selector_group(post_element, "engagement", engagement_selectors)
        
        # Get full HTML structure for analysis
        try:
            full_html = post_element.get_attribute("outerHTML")
            # Save snippet for analysis (first 500 chars)
            html_snippet = full_html[:500] + "..." if len(full_html) > 500 else full_html
            self.log_debug(f"HTML structure snippet", html_snippet)
        except Exception as e:
            self.log_debug(f"Failed to get HTML structure: {e}")
        
        return {
            "urn": urn,
            "author_results": author_results,
            "content_results": content_results,
            "engagement_results": engagement_results
        }
    
    def _test_selector_group(self, post_element, group_name, selectors):
        """Test a group of selectors and return results"""
        
        results = {}
        successful_selectors = []
        
        for selector in selectors:
            try:
                elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    texts = []
                    for elem in elements:
                        text = elem.text.strip()
                        if text and len(text) > 1:
                            texts.append(text)
                    
                    if texts:
                        results[selector] = {
                            "success": True,
                            "count": len(elements),
                            "texts": texts[:3],  # First 3 results
                        }
                        successful_selectors.append(selector)
                        self.log_debug(f"✅ {group_name} selector '{selector}' found {len(texts)} results: {texts[:2]}")
                    else:
                        results[selector] = {
                            "success": False,
                            "count": len(elements),
                            "reason": "Elements found but no text content"
                        }
                else:
                    results[selector] = {
                        "success": False,
                        "count": 0,
                        "reason": "No elements found"
                    }
                    
            except Exception as e:
                results[selector] = {
                    "success": False,
                    "count": 0,
                    "reason": f"Selector error: {e}"
                }
        
        # Track globally successful selectors
        if group_name not in self.successful_selectors:
            self.successful_selectors[group_name] = {}
        
        for selector in successful_selectors:
            if selector not in self.successful_selectors[group_name]:
                self.successful_selectors[group_name][selector] = 0
            self.successful_selectors[group_name][selector] += 1
        
        return results
    
    def wait_for_post_content(self, driver, post_element, timeout=10):
        """Wait for post content to be fully loaded"""
        
        self.log_debug("Waiting for post content to load")
        
        try:
            # Wait for any text content to appear in the post
            WebDriverWait(driver, timeout).until(
                lambda d: len(post_element.text.strip()) > 10
            )
            self.log_debug("✅ Post content loaded")
            return True
        except:
            self.log_debug("⚠️ Timeout waiting for post content")
            return False
    
    def scroll_to_element(self, driver, element):
        """Scroll to make element visible and wait"""
        
        try:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(1)  # Wait for scroll to complete
            self.log_debug("✅ Scrolled to element")
        except Exception as e:
            self.log_debug(f"⚠️ Failed to scroll to element: {e}")
    
    def extract_posts_diagnostic(self, driver, target_posts=5, verbose=True):
        """Extract posts with full diagnostic information"""
        
        self.log_debug(f"Starting diagnostic extraction for {target_posts} posts")
        
        # Navigate to feed
        driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)  # Extended wait for feed to load
        
        posts_analyzed = []
        seen_urns = set()
        
        # Find all post elements
        post_elements = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
        self.log_debug(f"Found {len(post_elements)} post elements in DOM")
        
        for i, post_element in enumerate(post_elements[:target_posts]):
            self.log_debug(f"\n--- Analyzing Post {i+1} ---")
            
            # Scroll to post and wait
            self.scroll_to_element(driver, post_element)
            
            # Wait for content to load
            self.wait_for_post_content(driver, post_element)
            
            # Test all selectors
            analysis = self.test_selectors_on_post(driver, post_element, i+1)
            posts_analyzed.append(analysis)
            
            # Add delay between posts
            time.sleep(2)
        
        return posts_analyzed
    
    def generate_diagnostic_report(self, analyses):
        """Generate comprehensive diagnostic report"""
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_posts_analyzed": len(analyses),
            "debug_log": self.debug_log,
            "successful_selectors_summary": self.successful_selectors,
            "post_analyses": analyses,
            "recommendations": self._generate_recommendations()
        }
        
        return report
    
    def _generate_recommendations(self):
        """Generate recommendations based on analysis"""
        
        recommendations = []
        
        # Analyze successful selectors
        for group_name, selectors in self.successful_selectors.items():
            if selectors:
                best_selector = max(selectors.items(), key=lambda x: x[1])
                recommendations.append(f"Best {group_name} selector: '{best_selector[0]}' (worked {best_selector[1]} times)")
            else:
                recommendations.append(f"⚠️ No working {group_name} selectors found - DOM structure may have changed")
        
        return recommendations
    
    def save_diagnostic_report(self, report, filename=None):
        """Save diagnostic report to file"""
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data/diagnostic_report_{timestamp}.json"
        
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        self.log_debug(f"Diagnostic report saved to {filename}")
        
        # Also save a readable summary
        summary_file = filename.replace('.json', '_summary.txt')
        self._save_readable_summary(report, summary_file)
        
        return filename
    
    def _save_readable_summary(self, report, filename):
        """Save human-readable summary"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("LinkedIn Scraper Diagnostic Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Analysis Date: {report['timestamp']}\n")
            f.write(f"Posts Analyzed: {report['total_posts_analyzed']}\n\n")
            
            f.write("Recommendations:\n")
            f.write("-" * 20 + "\n")
            for rec in report['recommendations']:
                f.write(f"• {rec}\n")
            
            f.write("\nSuccessful Selectors Summary:\n")
            f.write("-" * 30 + "\n")
            for group, selectors in report['successful_selectors_summary'].items():
                f.write(f"\n{group.upper()}:\n")
                if selectors:
                    for selector, count in sorted(selectors.items(), key=lambda x: x[1], reverse=True):
                        f.write(f"  ✅ {selector} (worked {count} times)\n")
                else:
                    f.write(f"  ❌ No working selectors found\n")
        
        self.log_debug(f"Readable summary saved to {filename}")

def main():
    """Run diagnostic extraction"""
    
    print("🚀 LinkedIn Diagnostic Scraper - Phase 1.1")
    print("=" * 60)
    
    scraper = DiagnosticLinkedInScraper()
    
    try:
        # Setup driver
        driver = scraper.setup_driver(headless=False)  # Use visible browser for better debugging
        
        # Login - use existing cookies if available
        print("🔐 Please ensure you're logged into LinkedIn in this browser window")
        print("Press Enter when ready to start extraction...")
        input()
        
        # Run diagnostic extraction
        analyses = scraper.extract_posts_diagnostic(driver, target_posts=5, verbose=True)
        
        # Generate and save report
        report = scraper.generate_diagnostic_report(analyses)
        report_file = scraper.save_diagnostic_report(report)
        
        print(f"\n✅ Diagnostic complete! Report saved to {report_file}")
        print(f"📋 Check the summary file for human-readable results")
        
        # Print quick summary
        print("\n📊 Quick Summary:")
        for rec in report['recommendations']:
            print(f"  • {rec}")
        
    except Exception as e:
        print(f"❌ Diagnostic failed: {e}")
        
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main() 