#!/usr/bin/env python3
"""
Example script demonstrating programmatic usage of LinkedIn Feed Capture.

This script shows how to use the library components directly in your own code
for custom integration scenarios.
"""

import json
import os
from pathlib import Path

from linkedin_feed_capture.browser.driver import create_default_driver
from linkedin_feed_capture.auth.authenticator import LinkedInAuthenticator, AuthConfig
from linkedin_feed_capture.scraper.extractor import FeedExtractor, ExtractionConfig
from linkedin_feed_capture.scraper.scroll import ScrollConfig
from linkedin_feed_capture.scraper.parser import ParsingConfig
from linkedin_feed_capture.utils.logger import setup_logging, get_logger


def main():
    """Main example function."""
    
    # Setup logging
    setup_logging(
        log_level="INFO",
        log_format="console",
        enable_console=True,
    )
    
    logger = get_logger(__name__)
    logger.info("Starting LinkedIn feed capture example")
    
    # Configuration
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")
    
    if not email or not password:
        logger.error("Please set LINKEDIN_EMAIL and LINKEDIN_PASSWORD environment variables")
        return
    
    # Create browser driver
    logger.info("Creating browser driver...")
    driver = create_default_driver(
        headless=True,  # Set to False to see the browser
        enable_stealth=True,
        window_size=(1280, 900),
    )
    
    try:
        # Setup authentication
        logger.info("Setting up authentication...")
        auth_config = AuthConfig(
            email=email,
            password=password,
            cookie_path="./example_cookies.pkl",
            encryption_key=os.getenv("COOKIE_ENCRYPTION_KEY"),
        )
        
        authenticator = LinkedInAuthenticator(auth_config)
        
        # Authenticate
        logger.info("Authenticating with LinkedIn...")
        authenticated = authenticator.authenticate(driver)
        
        if not authenticated:
            logger.error("Authentication failed")
            return
        
        logger.info("Authentication successful!")
        
        # Configure extraction
        extraction_config = ExtractionConfig(
            target_posts=10,  # Small number for demo
            extraction_timeout=60,  # 1 minute timeout
            include_sponsored=False,
            deduplicate_posts=True,
            scroll_config=ScrollConfig(
                base_delay=1.5,  # Faster for demo
                max_scroll_attempts=20,
            ),
            parsing_config=ParsingConfig(
                extract_media=True,
                extract_hashtags=True,
                extract_mentions=True,
            ),
        )
        
        # Create extractor
        extractor = FeedExtractor(extraction_config)
        
        # Extract posts
        logger.info("Starting post extraction...")
        posts = extractor.extract_feed(driver)
        
        # Get extraction statistics
        stats = extractor.get_extraction_stats()
        logger.info("Extraction completed", **stats)
        
        # Process and display results
        logger.info(f"Successfully extracted {len(posts)} posts")
        
        # Save to file
        output_file = Path("example_posts.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            posts_data = [post.to_json_dict() for post in posts]
            json.dump(posts_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Posts saved to {output_file}")
        
        # Display sample posts
        print("\n" + "="*80)
        print("SAMPLE EXTRACTED POSTS")
        print("="*80)
        
        for i, post in enumerate(posts[:3], 1):  # Show first 3 posts
            print(f"\n--- Post {i} ---")
            print(f"Author: {post.author}")
            print(f"Posted: {post.posted_at}")
            print(f"Type: {post.post_type}")
            print(f"Likes: {post.metrics.likes}")
            print(f"Content: {post.content[:200]}...")
            if post.hashtags:
                print(f"Hashtags: {', '.join(post.hashtags)}")
            print(f"URL: {post.url}")
        
        print("\n" + "="*80)
        print(f"Complete data saved to: {output_file.absolute()}")
        print("="*80)
        
    except KeyboardInterrupt:
        logger.info("Extraction interrupted by user")
    except Exception as e:
        logger.error(f"Extraction failed: {e}", exc_info=True)
    finally:
        # Cleanup
        logger.info("Cleaning up...")
        driver.quit()


if __name__ == "__main__":
    main() 