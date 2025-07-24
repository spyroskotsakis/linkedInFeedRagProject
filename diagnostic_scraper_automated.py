#!/usr/bin/env python3
"""
Automated Diagnostic LinkedIn Scraper - Phase 1.1
================================================

This automated version uses existing authentication and runs headless
to diagnose selector and DOM structure issues without manual intervention.
"""

import time
import json
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

class AutomatedDiagnosticScraper:
    """Automated diagnostic scraper using existing auth system"""
    
    def __init__(self):
        self.debug_log = []
        self.successful_selectors = {}
        
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
        if data and len(str(data)) < 200:
            print(f"   📋 {data}")
    
    def setup_driver(self):
        """Setup Chrome driver with stealth capabilities"""
        self.log_debug("Setting up automated diagnostic Chrome driver")
        
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            self.log_debug("Driver setup successful")
            return driver
        except Exception as e:
            self.log_debug(f"Driver setup failed: {e}")
            raise
    
    def login_with_credentials(self, driver):
        """Login using stored credentials"""
        self.log_debug("Attempting automated login")
        
        try:
            # Load credentials
            username = os.getenv('LINKEDIN_USERNAME', 'spyros.kotsakis@gmail.com')
            password = os.getenv('LINKEDIN_PASSWORD')
            
            if not password:
                self.log_debug("No password found in environment, trying credential files")
                try:
                    with open('.env', 'r') as f:
                        for line in f:
                            if line.startswith('LINKEDIN_PASSWORD='):
                                password = line.split('=', 1)[1].strip().strip('"\'')
                                break
                except:
                    pass
            
            if not password:
                self.log_debug("No password available, login will fail")
                return False
            
            # Navigate to login
            driver.get("https://www.linkedin.com/login")
            time.sleep(3)
            
            # Fill credentials
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = driver.find_element(By.ID, "password")
            
            username_field.send_keys(username)
            time.sleep(1)
            password_field.send_keys(password)
            time.sleep(1)
            
            # Submit
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            login_button.click()
            
            # Wait for successful login
            WebDriverWait(driver, 15).until(
                lambda d: "/feed" in d.current_url or "/checkpoint" in d.current_url
            )
            
            if "/feed" in driver.current_url:
                self.log_debug("✅ Login successful")
                return True
            else:
                self.log_debug("⚠️ Login redirected to checkpoint/challenge")
                return False
                
        except Exception as e:
            self.log_debug(f"❌ Login failed: {e}")
            return False
    
    def test_all_selectors_on_post(self, post_element, post_index):
        """Test comprehensive selector sets on a post"""
        
        self.log_debug(f"Testing selectors on post {post_index}")
        
        urn = post_element.get_attribute("data-id")
        self.log_debug(f"Post URN: {urn}")
        
        # Comprehensive selector sets based on current LinkedIn patterns
        selector_groups = {
            "author": [
                "span[aria-hidden='true']",
                ".feed-shared-actor__name",
                ".feed-shared-actor__title",
                ".update-components-actor__name",
                ".artdeco-entity-lockup__title",
                ".feed-shared-update-v2__actor-name",
                "[data-control-name='actor_name']",
                ".feed-shared-actor__meta a span",
                "h3 span[aria-hidden='true']",
                ".ember-view .visually-hidden"
            ],
            "content": [
                ".feed-shared-update-v2__description",
                ".feed-shared-text",
                ".update-components-text",
                ".feed-shared-inline-show-more-text",
                ".feed-shared-text__text-view",
                "[data-test-id='main-feed-activity-card__commentary']",
                ".activity-content-text",
                ".feed-shared-update-v2__description-wrapper",
                "div[data-test-id*='text']",
                ".feed-shared-update-v2__description .break-words"
            ],
            "engagement": [
                ".social-details-social-counts__reactions-count",
                ".social-counts-reactions__count",
                ".social-counts__reactions",
                ".feed-shared-social-action-bar__action-button span",
                "button[aria-label*='like'] span",
                ".social-counts-reactions",
                "[data-tracking-control-name*='reactions'] span"
            ]
        }
        
        results = {}
        
        for group_name, selectors in selector_groups.items():
            group_results = self._test_selector_group(post_element, group_name, selectors)
            results[group_name] = group_results
        
        # Get HTML structure sample
        try:
            html_sample = post_element.get_attribute("outerHTML")[:800]
            results["html_sample"] = html_sample
        except:
            results["html_sample"] = "Could not retrieve HTML"
        
        return {
            "urn": urn,
            "results": results
        }
    
    def _test_selector_group(self, post_element, group_name, selectors):
        """Test a group of selectors"""
        
        results = {}
        successful_count = 0
        
        for selector in selectors:
            try:
                elements = post_element.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    valid_texts = []
                    for elem in elements:
                        text = elem.text.strip()
                        if text and len(text) > 1 and text not in ["•", "..."]:
                            valid_texts.append(text)
                    
                    if valid_texts:
                        results[selector] = {
                            "success": True,
                            "count": len(elements),
                            "valid_count": len(valid_texts),
                            "sample_texts": valid_texts[:2]
                        }
                        successful_count += 1
                        
                        # Track globally successful selectors
                        if group_name not in self.successful_selectors:
                            self.successful_selectors[group_name] = {}
                        if selector not in self.successful_selectors[group_name]:
                            self.successful_selectors[group_name][selector] = 0
                        self.successful_selectors[group_name][selector] += 1
                        
                        self.log_debug(f"✅ {group_name} '{selector}': {valid_texts[:1]}")
                    else:
                        results[selector] = {
                            "success": False,
                            "count": len(elements),
                            "reason": "Elements found but no valid text"
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
                    "reason": f"Error: {str(e)}"
                }
        
        self.log_debug(f"{group_name} group: {successful_count}/{len(selectors)} selectors worked")
        return results
    
    def extract_posts_diagnostic(self, driver, target_posts=5):
        """Extract posts with diagnostic information"""
        
        self.log_debug(f"Starting diagnostic extraction for {target_posts} posts")
        
        # Navigate to feed
        driver.get("https://www.linkedin.com/feed/")
        time.sleep(5)
        
        # Find post elements
        post_elements = driver.find_elements(By.CSS_SELECTOR, '[data-id^="urn:li:activity"]')
        self.log_debug(f"Found {len(post_elements)} post elements in DOM")
        
        if not post_elements:
            self.log_debug("❌ No post elements found - possible login issue or DOM structure change")
            return []
        
        analyses = []
        
        for i, post_element in enumerate(post_elements[:target_posts]):
            try:
                self.log_debug(f"\n--- Analyzing Post {i+1} ---")
                
                # Scroll element into view
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", post_element)
                time.sleep(1)
                
                # Test selectors
                analysis = self.test_all_selectors_on_post(post_element, i+1)
                analyses.append(analysis)
                
                time.sleep(2)  # Delay between posts
                
            except Exception as e:
                self.log_debug(f"❌ Error analyzing post {i+1}: {e}")
                continue
        
        return analyses
    
    def generate_report(self, analyses):
        """Generate diagnostic report"""
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "total_posts_analyzed": len(analyses),
            "successful_selectors": self.successful_selectors,
            "analyses": analyses,
            "debug_log": self.debug_log[-50:],  # Last 50 log entries
            "recommendations": []
        }
        
        # Generate recommendations
        for group, selectors in self.successful_selectors.items():
            if selectors:
                best = max(selectors.items(), key=lambda x: x[1])
                report["recommendations"].append(
                    f"Best {group} selector: '{best[0]}' (worked {best[1]}/{len(analyses)} times)"
                )
            else:
                report["recommendations"].append(
                    f"⚠️ No working {group} selectors found"
                )
        
        return report
    
    def save_report(self, report):
        """Save diagnostic report"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON report
        json_file = f"data/diagnostic_automated_{timestamp}.json"
        Path(json_file).parent.mkdir(parents=True, exist_ok=True)
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        # Human-readable summary
        txt_file = f"data/diagnostic_automated_{timestamp}_summary.txt"
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write("Automated LinkedIn Scraper Diagnostic Report\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Analysis Date: {report['timestamp']}\n")
            f.write(f"Posts Analyzed: {report['total_posts_analyzed']}\n\n")
            
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
        
        self.log_debug(f"Reports saved: {json_file}, {txt_file}")
        return json_file, txt_file


def main():
    """Run automated diagnostic"""
    
    print("🚀 Automated LinkedIn Diagnostic Scraper")
    print("=" * 60)
    
    scraper = AutomatedDiagnosticScraper()
    
    try:
        # Setup driver
        driver = scraper.setup_driver()
        
        # Login
        login_success = scraper.login_with_credentials(driver)
        if not login_success:
            print("❌ Login failed - cannot proceed with diagnostic")
            return
        
        # Run diagnostic
        analyses = scraper.extract_posts_diagnostic(driver, target_posts=5)
        
        if not analyses:
            print("❌ No posts analyzed - possible structural issue")
            return
        
        # Generate and save report
        report = scraper.generate_report(analyses)
        json_file, txt_file = scraper.save_report(report)
        
        print(f"\n✅ Diagnostic complete!")
        print(f"📋 JSON Report: {json_file}")
        print(f"📄 Summary: {txt_file}")
        
        print(f"\n📊 Quick Summary:")
        for rec in report['recommendations']:
            print(f"  • {rec}")
        
    except Exception as e:
        print(f"❌ Diagnostic failed: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main() 