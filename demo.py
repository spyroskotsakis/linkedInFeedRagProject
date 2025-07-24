#!/usr/bin/env python3
"""
Demo script for LinkedIn Feed Capture

This script demonstrates the data models and core functionality
without requiring actual LinkedIn authentication or browser setup.
"""

import json
from datetime import datetime, timezone, timedelta
from typing import List

from linkedin_feed_capture.models.post import Post, PostMetrics
from linkedin_feed_capture.utils.logger import setup_logging, get_logger
from linkedin_feed_capture.utils.backoff import exponential_backoff, with_retries, RetryConfig

# Setup logging
setup_logging(log_level="INFO", log_format="console")
logger = get_logger(__name__)

def create_sample_posts() -> List[Post]:
    """Create sample LinkedIn posts to demonstrate the data model."""
    
    posts = []
    
    # Sample post 1: High engagement tech post
    metrics1 = PostMetrics(likes=1250, comments=89, shares=156, views=15000)
    post1 = Post(
        urn="urn:li:activity:7156789123456789012",
        author="Tech Industry Expert",
        content="🚀 Just launched our new AI-powered platform! The response has been incredible. "
                "Key lessons learned: 1) User feedback is gold 2) Iterate quickly 3) Focus on value. "
                "What's your experience with AI tools? #AI #TechInnovation #Startup",
        posted_at=datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(hours=2),
        url="https://linkedin.com/posts/tech-expert_ai-innovation-startup-activity-7156789123456789012",
        metrics=metrics1,
        hashtags=["AI", "TechInnovation", "Startup"],
        mentions=[],
        media_urls=["https://media.licdn.com/dms/image/sample-tech-post.jpg"],
        company_name="TechCorp Inc."
    )
    posts.append(post1)
    
    # Sample post 2: Career advice post
    metrics2 = PostMetrics(likes=456, comments=67, shares=23, views=5600)
    post2 = Post(
        urn="urn:li:activity:7156789123456789013",
        author="Career Coach Sarah",
        content="📈 5 signs you're ready for a promotion:\n\n"
                "✅ You're consistently exceeding expectations\n"
                "✅ You're mentoring others\n"
                "✅ You're driving initiatives beyond your role\n"
                "✅ You're getting positive feedback from stakeholders\n"
                "✅ You're thinking strategically about the business\n\n"
                "Don't wait for permission to step up! 💪 #CareerGrowth #Leadership",
        posted_at=datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(hours=4),
        url="https://linkedin.com/posts/career-coach_growth-leadership-activity-7156789123456789013",
        metrics=metrics2,
        hashtags=["CareerGrowth", "Leadership"],
        mentions=[],
        media_urls=[],
        company_name=None
    )
    posts.append(post2)
    
    # Sample post 3: Industry news with lower engagement
    metrics3 = PostMetrics(likes=89, comments=12, shares=4, views=980)
    post3 = Post(
        urn="urn:li:activity:7156789123456789014",
        author="Industry Analyst Mike",
        content="📊 New market research shows 73% of companies are investing in automation this year. "
                "The biggest drivers? Cost reduction (45%) and efficiency gains (38%). "
                "Interesting to see sustainability coming in third at 17%. #MarketResearch #Automation",
        posted_at=datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(hours=6),
        url="https://linkedin.com/posts/analyst-mike_research-automation-activity-7156789123456789014",
        metrics=metrics3,
        hashtags=["MarketResearch", "Automation"],
        mentions=[],
        media_urls=[],
        company_name="Research Firm LLC"
    )
    posts.append(post3)
    
    return posts

def analyze_posts(posts: List[Post]) -> None:
    """Analyze and display post metrics."""
    
    logger.info(f"Analyzing {len(posts)} LinkedIn posts...")
    
    print("\n" + "="*80)
    print("🔍 LINKEDIN FEED ANALYSIS")
    print("="*80)
    
    total_engagement = 0
    total_views = 0
    
    for i, post in enumerate(posts, 1):
        print(f"\n📝 POST {i}")
        print("-" * 50)
        print(f"Author: {post.author}")
        print(f"Company: {post.company_name or 'Personal'}")
        print(f"Content: {post.content[:100]}{'...' if len(post.content) > 100 else ''}")
        print(f"Posted: {post.posted_at.strftime('%Y-%m-%d %H:%M')}")
        print(f"URL: {post.url}")
        
        # Metrics
        engagement_rate = post.get_engagement_rate()
        total_engagement += post.metrics.likes + post.metrics.comments + post.metrics.shares
        if post.metrics.views:
            total_views += post.metrics.views
            
        print(f"\n📊 Metrics:")
        print(f"  👍 Likes: {post.metrics.likes:,}")
        print(f"  💬 Comments: {post.metrics.comments:,}")
        print(f"  🔄 Shares: {post.metrics.shares:,}")
        print(f"  👀 Views: {post.metrics.views:,}" if post.metrics.views else "  👀 Views: N/A")
        print(f"  📈 Engagement Rate: {engagement_rate:.2f}%")
        
        # Features
        print(f"\n🏷️  Features:")
        print(f"  Hashtags: {', '.join(post.hashtags) if post.hashtags else 'None'}")
        print(f"  Has Media: {'Yes' if post.has_media() else 'No'}")
        print(f"  Company Post: {'Yes' if post.is_company_post() else 'No'}")
        
        # JSON representation
        print(f"\n📄 JSON Preview:")
        json_data = post.to_json_dict()
        print(json.dumps(json_data, indent=2, default=str)[:300] + "...")
    
    # Summary
    print(f"\n{'='*80}")
    print("📈 SUMMARY STATISTICS")
    print("="*80)
    print(f"Total Posts: {len(posts)}")
    print(f"Total Engagement: {total_engagement:,}")
    print(f"Total Views: {total_views:,}")
    print(f"Average Engagement per Post: {total_engagement / len(posts):.1f}")
    print(f"Top Performing Post: {max(posts, key=lambda p: p.get_engagement_rate()).author}")
    
    # Hashtag analysis
    all_hashtags = []
    for post in posts:
        all_hashtags.extend(post.hashtags)
    
    if all_hashtags:
        from collections import Counter
        hashtag_counts = Counter(all_hashtags)
        print(f"\n🏷️  Top Hashtags:")
        for hashtag, count in hashtag_counts.most_common(5):
            print(f"  #{hashtag}: {count}")

def demo_retry_mechanism():
    """Demonstrate the retry and backoff functionality."""
    
    print(f"\n{'='*80}")
    print("🔄 RETRY MECHANISM DEMO")
    print("="*80)
    
    # Simulate a flaky function that fails a few times
    attempt_count = 0
    
    @with_retries(RetryConfig(max_retries=4, base_delay=0.1))
    def flaky_linkedin_api():
        nonlocal attempt_count
        attempt_count += 1
        
        if attempt_count <= 2:
            logger.warning(f"Attempt {attempt_count}: Simulating rate limit error...")
            raise ConnectionError("LinkedIn rate limit exceeded")
        else:
            logger.info(f"Attempt {attempt_count}: Success!")
            return {"status": "success", "posts_remaining": 100}
    
    try:
        result = flaky_linkedin_api()
        print(f"✅ API call succeeded: {result}")
    except Exception as e:
        print(f"❌ API call failed: {e}")
    
    # Demonstrate exponential backoff delays
    print(f"\n⏱️  Exponential Backoff Delays:")
    for i in range(5):
        delay = exponential_backoff(i, base_delay=1.0, max_delay=60.0)
        print(f"  Attempt {i+1}: {delay:.2f} seconds")

def main():
    """Main demo function."""
    
    print("🚀 LinkedIn Feed Capture - Demo")
    print("=" * 80)
    print("This demo shows the data models and functionality")
    print("without requiring actual LinkedIn authentication.\n")
    
    # Create sample posts
    logger.info("Creating sample LinkedIn posts...")
    posts = create_sample_posts()
    
    # Analyze posts
    analyze_posts(posts)
    
    # Demo retry mechanism
    demo_retry_mechanism()
    
    print(f"\n{'='*80}")
    print("✅ Demo completed successfully!")
    print("💡 To run with real data, use: python -m linkedin_feed_capture.cli.main capture")
    print("📝 See README.md for setup instructions with LinkedIn credentials")
    print("="*80)

if __name__ == "__main__":
    main() 