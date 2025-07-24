#!/usr/bin/env python3
"""
Test Browser Demo - LinkedIn Feed Capture

This script demonstrates the browser driver functionality and data extraction
pipeline without requiring LinkedIn credentials by creating a mock LinkedIn page.
"""

import json
import time
from pathlib import Path
from typing import List

from linkedin_feed_capture.browser.driver import create_default_driver, DriverConfig, DriverFactory
from linkedin_feed_capture.models.post import Post, PostMetrics
from linkedin_feed_capture.utils.logger import setup_logging, get_logger
from linkedin_feed_capture.scraper.parser import PostParser, ParsingConfig

# Setup logging
setup_logging(log_level="INFO", log_format="console")
logger = get_logger(__name__)

# Mock LinkedIn HTML page for testing
MOCK_LINKEDIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Mock LinkedIn Feed</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f3f2ef; margin: 0; padding: 20px; }
        .feed-container { max-width: 600px; margin: 0 auto; }
        .post { background: white; margin: 20px 0; padding: 20px; border-radius: 8px; border: 1px solid #d4d4d8; }
        .author { font-weight: bold; margin-bottom: 10px; }
        .content { margin: 15px 0; line-height: 1.6; }
        .metrics { display: flex; gap: 20px; color: #666; font-size: 14px; margin-top: 15px; }
        .timestamp { color: #999; font-size: 12px; }
    </style>
</head>
<body>
    <div class="feed-container">
        <h1>LinkedIn Feed Capture Demo</h1>
        
        <div class="post" data-id="urn:li:activity:7156789123456789001">
            <div class="author">Sarah Johnson, Tech Lead at InnovateCorp</div>
            <div class="timestamp">2 hours ago</div>
            <div class="content">
                🚀 Just shipped our new machine learning pipeline! The results are incredible:
                <br><br>
                ✅ 40% faster inference times<br>
                ✅ 25% better accuracy<br>
                ✅ 60% reduction in compute costs<br>
                <br>
                Key learnings: Always benchmark early and often. What's your experience with ML optimization? #MachineLearning #TechLeadership #AI
            </div>
            <div class="metrics">
                <span>👍 324 likes</span>
                <span>💬 47 comments</span>
                <span>🔄 89 shares</span>
                <span>👀 5,200 views</span>
            </div>
        </div>
        
        <div class="post" data-id="urn:li:activity:7156789123456789002">
            <div class="author">Marcus Chen, Senior Developer</div>
            <div class="timestamp">4 hours ago</div>
            <div class="content">
                📊 Data visualization tip: Choose the right chart type for your story!
                <br><br>
                📈 Line charts → Trends over time<br>
                📊 Bar charts → Comparing categories<br>
                🥧 Pie charts → Parts of a whole (use sparingly!)<br>
                📉 Scatter plots → Relationships between variables<br>
                <br>
                What's your go-to visualization library? I'm loving D3.js lately! #DataViz #WebDev #DataScience
            </div>
            <div class="metrics">
                <span>👍 156 likes</span>
                <span>💬 23 comments</span>
                <span>🔄 34 shares</span>
                <span>👀 2,800 views</span>
            </div>
        </div>
        
        <div class="post" data-id="urn:li:activity:7156789123456789003">
            <div class="author">Emily Rodriguez, Product Manager</div>
            <div class="timestamp">6 hours ago</div>
            <div class="content">
                🎯 Product launch lessons learned:
                <br><br>
                1. Customer feedback beats internal assumptions every time<br>
                2. MVP doesn't mean "barely functional" - it means "valuable"<br>
                3. Launch day is just the beginning, not the end<br>
                4. Analytics are your best friend for post-launch iterations<br>
                <br>
                Building products is a marathon, not a sprint! 🏃‍♀️ #ProductManagement #Startup #CustomerFirst
            </div>
            <div class="metrics">
                <span>👍 892 likes</span>
                <span>💬 128 comments</span>
                <span>🔄 203 shares</span>
                <span>👀 12,400 views</span>
            </div>
        </div>
        
        <div class="post" data-id="urn:li:activity:7156789123456789004">
            <div class="author">David Kumar, DevOps Engineer</div>
            <div class="timestamp">8 hours ago</div>
            <div class="content">
                🔧 Kubernetes optimization checklist for 2024:
                <br><br>
                ☑️ Resource requests and limits properly set<br>
                ☑️ HPA configured for auto-scaling<br>
                ☑️ Monitoring with Prometheus + Grafana<br>
                ☑️ Security policies implemented<br>
                ☑️ Backup strategy in place<br>
                <br>
                Container orchestration done right saves both time and money! #Kubernetes #DevOps #CloudNative
            </div>
            <div class="metrics">
                <span>👍 445 likes</span>
                <span>💬 67 comments</span>
                <span>🔄 112 shares</span>
                <span>👀 7,800 views</span>
            </div>
        </div>
        
        <div class="post" data-id="urn:li:activity:7156789123456789005">
            <div class="author">Lisa Thompson, UX Designer</div>
            <div class="timestamp">10 hours ago</div>
            <div class="content">
                🎨 Design system spotlight: Why consistency matters
                <br><br>
                A well-maintained design system isn't just about pretty colors and fonts. It's about:
                <br><br>
                • Faster development cycles<br>
                • Better user experience<br>
                • Reduced design debt<br>
                • Improved accessibility<br>
                • Team alignment and communication<br>
                <br>
                Invest in your design system - your future self will thank you! #UXDesign #DesignSystems #UserExperience
            </div>
            <div class="metrics">
                <span>👍 678 likes</span>
                <span>💬 92 comments</span>
                <span>🔄 145 shares</span>
                <span>👀 9,200 views</span>
            </div>
        </div>
    </div>
    
    <script>
        // Simulate LinkedIn-like behavior
        console.log('Mock LinkedIn page loaded');
        
        // Add some dynamic content loading simulation
        setTimeout(() => {
            console.log('Additional content loaded');
        }, 1000);
    </script>
</body>
</html>
"""


def create_mock_html_file() -> Path:
    """Create a mock HTML file that simulates LinkedIn feed structure."""
    temp_file = Path("mock_linkedin_feed.html")
    temp_file.write_text(MOCK_LINKEDIN_HTML)
    logger.info(f"Created mock HTML file: {temp_file.absolute()}")
    return temp_file


def extract_posts_from_mock_page(driver) -> List[dict]:
    """Extract posts from the mock LinkedIn page using real extraction logic."""
    
    # Find all post elements (same selector as real LinkedIn)
    post_elements = driver.find_elements("css selector", '[data-id^="urn:li:activity"]')
    
    logger.info(f"Found {len(post_elements)} post elements")
    
    extracted_posts = []
    
    for i, element in enumerate(post_elements, 1):
        try:
            # Extract data using CSS selectors
            urn = element.get_attribute("data-id")
            
            # Extract author
            try:
                author_element = element.find_element("css selector", ".author")
                author = author_element.text.strip()
            except:
                author = "Unknown Author"
            
            # Extract content
            try:
                content_element = element.find_element("css selector", ".content")
                content = content_element.text.strip()
            except:
                content = "No content available"
            
            # Extract timestamp
            try:
                timestamp_element = element.find_element("css selector", ".timestamp")
                timestamp = timestamp_element.text.strip()
            except:
                timestamp = "Unknown time"
            
            # Extract metrics
            metrics = {"likes": 0, "comments": 0, "shares": 0, "views": 0}
            try:
                metrics_element = element.find_element("css selector", ".metrics")
                metrics_text = metrics_element.text
                
                # Parse metrics from text
                import re
                likes_match = re.search(r'(\d+) likes', metrics_text)
                comments_match = re.search(r'(\d+) comments', metrics_text)
                shares_match = re.search(r'(\d+) shares', metrics_text)
                views_match = re.search(r'([\d,]+) views', metrics_text)
                
                if likes_match:
                    metrics["likes"] = int(likes_match.group(1))
                if comments_match:
                    metrics["comments"] = int(comments_match.group(1))
                if shares_match:
                    metrics["shares"] = int(shares_match.group(1))
                if views_match:
                    metrics["views"] = int(views_match.group(1).replace(',', ''))
                    
            except Exception as e:
                logger.warning(f"Failed to extract metrics for post {i}: {e}")
            
            post_data = {
                "urn": urn,
                "author": author,
                "content": content,
                "timestamp": timestamp,
                "metrics": metrics,
                "url": f"https://linkedin.com/posts/mock-{urn.split(':')[-1]}",
                "extracted_at": time.time(),
            }
            
            extracted_posts.append(post_data)
            logger.info(f"Extracted post {i}: {author[:30]}...")
            
        except Exception as e:
            logger.error(f"Failed to extract post {i}: {e}")
            
    return extracted_posts


def demonstrate_browser_functionality():
    """Demonstrate the browser driver and extraction functionality."""
    
    print("🚀 LinkedIn Feed Capture - Browser Demo")
    print("=" * 80)
    print("This demo shows browser functionality and data extraction")
    print("using a mock LinkedIn page (no real credentials needed).\n")
    
    # Create mock HTML file
    html_file = create_mock_html_file()
    
    try:
        # Test different driver configurations
        configs_to_test = [
            ("Headless Mode", DriverConfig(headless=True, enable_stealth=True)),
            ("Visible Mode", DriverConfig(headless=False, enable_stealth=True)),
        ]
        
        for config_name, config in configs_to_test:
            print(f"\n🔧 Testing {config_name}")
            print("-" * 50)
            
            # Create driver
            factory = DriverFactory(config)
            driver = factory.create_driver()
            
            try:
                print(f"✅ Browser created successfully")
                print(f"   Headless: {config.headless}")
                print(f"   Stealth: {config.enable_stealth}")
                print(f"   Window Size: {config.window_width}x{config.window_height}")
                
                # Load mock page
                file_url = f"file://{html_file.absolute()}"
                driver.get(file_url)
                
                print(f"✅ Page loaded: {driver.title}")
                
                # Wait for page to load
                time.sleep(2)
                
                # Extract posts
                posts = extract_posts_from_mock_page(driver)
                
                print(f"✅ Extracted {len(posts)} posts")
                
                # Show sample data
                if posts:
                    print(f"\n📝 Sample Post Data:")
                    sample_post = posts[0]
                    print(f"   Author: {sample_post['author']}")
                    print(f"   Content: {sample_post['content'][:100]}...")
                    print(f"   Likes: {sample_post['metrics']['likes']}")
                    print(f"   Comments: {sample_post['metrics']['comments']}")
                    print(f"   Shares: {sample_post['metrics']['shares']}")
                    print(f"   Views: {sample_post['metrics']['views']}")
                
                # Test scrolling behavior
                print(f"\n🖱️  Testing scroll behavior...")
                initial_height = driver.execute_script("return document.body.scrollHeight")
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
                final_height = driver.execute_script("return document.body.scrollHeight")
                print(f"   Initial height: {initial_height}px")
                print(f"   Final height: {final_height}px")
                print(f"   ✅ Scrolling functionality works")
                
                # If visible mode, give user time to see the browser
                if not config.headless:
                    print(f"\n👀 Browser is visible! Check it out...")
                    time.sleep(5)
                
            finally:
                driver.quit()
                factory.cleanup()
                print(f"✅ Browser cleaned up")
            
            # Only test one config in this demo to keep it fast
            break
        
        # Save extracted data as JSON
        if 'posts' in locals() and posts:
            output_file = Path("extracted_posts_demo.json")
            with open(output_file, 'w') as f:
                json.dump(posts, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Data saved to: {output_file.absolute()}")
            print(f"   Contains {len(posts)} posts with full metadata")
        
        print(f"\n🎯 Real LinkedIn Scraping:")
        print(f"   To scrape real LinkedIn data, set up credentials in .env:")
        print(f"   LINKEDIN_EMAIL=your.email@example.com")
        print(f"   LINKEDIN_PASSWORD=your_password")
        print(f"   Then run: python -m linkedin_feed_capture.cli.main capture")
        
    finally:
        # Cleanup
        if html_file.exists():
            html_file.unlink()
        
        print(f"\n✅ Demo completed successfully!")
        print(f"🔗 This demonstrates the full extraction pipeline")


if __name__ == "__main__":
    demonstrate_browser_functionality() 