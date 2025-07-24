#!/usr/bin/env python3
"""
LinkedIn HTML Data Schema Enhancement Analyzer

This script analyzes captured HTML from LinkedIn posts to identify additional 
data fields that could enhance our current post schema beyond URLs.
"""

import json
import re
from bs4 import BeautifulSoup
from collections import defaultdict, Counter
import urllib.parse
from pathlib import Path

def analyze_post_html(post_data):
    """Analyze a single post's HTML for extractable data fields."""
    
    if not post_data.get("html_data", {}).get("complete_html"):
        return {}
    
    html = post_data["html_data"]["complete_html"]
    soup = BeautifulSoup(html, 'html.parser')
    
    analysis = {
        "media_content": analyze_media_content(soup),
        "author_metadata": analyze_author_metadata(soup),
        "engagement_details": analyze_engagement_details(soup),
        "post_metadata": analyze_post_metadata(soup),
        "content_structure": analyze_content_structure(soup),
        "interaction_elements": analyze_interaction_elements(soup),
        "tracking_data": analyze_tracking_data(soup),
        "accessibility_data": analyze_accessibility_data(soup)
    }
    
    return analysis

def analyze_media_content(soup):
    """Extract media-related data."""
    media_data = {
        "videos": [],
        "images": [],
        "articles": [],
        "documents": [],
        "polls": []
    }
    
    # Video content
    video_containers = soup.find_all(class_=re.compile(r'video|media-player'))
    for video in video_containers:
        video_data = {}
        
        # Video URL
        video_elem = video.find('video')
        if video_elem and video_elem.get('src'):
            video_data["url"] = video_elem.get('src')
        
        # Poster/thumbnail
        poster = video_elem.get('poster') if video_elem else None
        if poster:
            video_data["thumbnail"] = poster
            
        # Duration
        duration_elem = video.find(class_=re.compile(r'duration|time'))
        if duration_elem:
            video_data["duration"] = duration_elem.get_text(strip=True)
            
        if video_data:
            media_data["videos"].append(video_data)
    
    # Images
    image_containers = soup.find_all(class_=re.compile(r'update-components-image'))
    for img_container in image_containers:
        img = img_container.find('img')
        if img and img.get('src'):
            img_data = {
                "url": img.get('src'),
                "alt": img.get('alt', ''),
                "width": img.get('width'),
                "height": img.get('height')
            }
            media_data["images"].append(img_data)
    
    # Articles/Links
    article_containers = soup.find_all(class_=re.compile(r'update-components-article'))
    for article in article_containers:
        article_data = {}
        
        # Article URL
        link = article.find('a', href=True)
        if link:
            article_data["url"] = link.get('href')
        
        # Title
        title = article.find(class_=re.compile(r'title'))
        if title:
            article_data["title"] = title.get_text(strip=True)
            
        # Description/subtitle
        subtitle = article.find(class_=re.compile(r'subtitle'))
        if subtitle:
            article_data["description"] = subtitle.get_text(strip=True)
            
        # Domain
        domain = article.find(class_=re.compile(r'domain|source'))
        if domain:
            article_data["domain"] = domain.get_text(strip=True)
            
        if article_data:
            media_data["articles"].append(article_data)
    
    return media_data

def analyze_author_metadata(soup):
    """Extract detailed author information."""
    author_data = {}
    
    # Author container
    actor_container = soup.find(class_=re.compile(r'update-components-actor'))
    if not actor_container:
        return author_data
    
    # Profile URL
    profile_link = actor_container.find('a', href=True)
    if profile_link:
        href = profile_link.get('href')
        author_data["profile_url"] = href
        
        # Extract profile ID from URL
        profile_match = re.search(r'/in/([^/?]+)', href)
        if profile_match:
            author_data["profile_id"] = profile_match.group(1)
    
    # Avatar image
    avatar_img = actor_container.find('img')
    if avatar_img:
        author_data["avatar_url"] = avatar_img.get('src', '')
    
    # Verification status
    verified_icon = actor_container.find('svg', {'data-test-icon': 'verified-small'})
    author_data["is_verified"] = verified_icon is not None
    
    # Premium status
    premium_icon = actor_container.find('svg', class_=re.compile(r'premium'))
    author_data["is_premium"] = premium_icon is not None
    
    # Connection status (Following, 1st, 2nd, etc.)
    connection_elem = actor_container.find(class_=re.compile(r'supplementary-actor-info'))
    if connection_elem:
        connection_text = connection_elem.get_text(strip=True)
        author_data["connection_status"] = connection_text
        
        # Extract following status
        author_data["is_following"] = "Following" in connection_text
        
        # Extract connection degree
        if "1st" in connection_text:
            author_data["connection_degree"] = "1st"
        elif "2nd" in connection_text:
            author_data["connection_degree"] = "2nd"
        elif "3rd" in connection_text:
            author_data["connection_degree"] = "3rd"
    
    # Job title/description
    description_elem = actor_container.find(class_=re.compile(r'actor__description'))
    if description_elem:
        author_data["job_title"] = description_elem.get_text(strip=True)
    
    # Company information (if available in links)
    company_links = actor_container.find_all('a', href=re.compile(r'/company/'))
    if company_links:
        companies = []
        for link in company_links:
            company_data = {
                "name": link.get_text(strip=True),
                "url": link.get('href')
            }
            companies.append(company_data)
        author_data["companies"] = companies
    
    return author_data

def analyze_engagement_details(soup):
    """Extract detailed engagement information."""
    engagement_data = {
        "reaction_types": [],
        "reaction_breakdown": {},
        "social_proof": {}
    }
    
    # Reaction icons and types
    reaction_icons = soup.find_all('img', class_=re.compile(r'reactions-icon'))
    for icon in reaction_icons:
        reaction_type = icon.get('data-test-reactions-icon-type')
        if reaction_type:
            engagement_data["reaction_types"].append(reaction_type.lower())
    
    # Social proof text (e.g., "John Smith and 15 others")
    social_proof_elem = soup.find(class_=re.compile(r'social-proof'))
    if social_proof_elem:
        social_proof_text = social_proof_elem.get_text(strip=True)
        engagement_data["social_proof"]["text"] = social_proof_text
        
        # Extract names from social proof
        names = re.findall(r'([A-Z][a-z]+ [A-Z][a-z]+)', social_proof_text)
        if names:
            engagement_data["social_proof"]["named_reactors"] = names
    
    # Detailed engagement counts
    engagement_buttons = soup.find_all('button', {'aria-label': re.compile(r'\d+\s+(comment|repost|reaction)')})
    for button in engagement_buttons:
        aria_label = button.get('aria-label', '')
        
        # Extract numbers and type
        count_match = re.search(r'(\d+)\s+(comment|repost|reaction)', aria_label)
        if count_match:
            count = int(count_match.group(1))
            engagement_type = count_match.group(2)
            engagement_data["reaction_breakdown"][engagement_type] = count
    
    return engagement_data

def analyze_post_metadata(soup):
    """Extract post metadata."""
    metadata = {}
    
    # Post type (suggested, promoted, etc.)
    header = soup.find(class_=re.compile(r'update-components-header'))
    if header:
        header_text = header.get_text(strip=True)
        if header_text:
            metadata["post_type"] = header_text.lower()
    
    # Edit status
    sub_description = soup.find(class_=re.compile(r'actor__sub-description'))
    if sub_description:
        sub_text = sub_description.get_text(strip=True)
        metadata["is_edited"] = "Edited" in sub_text
        
        # Privacy/visibility
        if "Visible to anyone" in sub_text:
            metadata["visibility"] = "public"
        elif "connections" in sub_text.lower():
            metadata["visibility"] = "connections"
        else:
            metadata["visibility"] = "unknown"
    
    # Language detection (from dir attribute)
    text_container = soup.find(class_=re.compile(r'update-components-text'))
    if text_container:
        dir_attr = text_container.get('dir')
        if dir_attr:
            metadata["text_direction"] = dir_attr
    
    return metadata

def analyze_content_structure(soup):
    """Analyze content structure and formatting."""
    structure = {
        "has_external_links": False,
        "external_links": [],
        "linkedin_mentions": [],
        "hashtags": [],
        "line_breaks": 0,
        "formatting_elements": []
    }
    
    # Find main content area
    content_area = soup.find(class_=re.compile(r'update-components-text'))
    if not content_area:
        return structure
    
    # External links
    external_links = content_area.find_all('a', href=re.compile(r'http[s]?://(?!.*linkedin\.com)'))
    if external_links:
        structure["has_external_links"] = True
        for link in external_links:
            link_data = {
                "url": link.get('href'),
                "text": link.get_text(strip=True),
                "title": link.get('title', '')
            }
            structure["external_links"].append(link_data)
    
    # LinkedIn company/profile mentions
    linkedin_links = content_area.find_all('a', href=re.compile(r'linkedin\.com/(company|in)/'))
    for link in linkedin_links:
        mention_data = {
            "url": link.get('href'),
            "name": link.get_text(strip=True),
            "type": "company" if "/company/" in link.get('href') else "profile"
        }
        structure["linkedin_mentions"].append(mention_data)
    
    # Hashtags
    hashtag_links = content_area.find_all('a', href=re.compile(r'hashtag|keywords='))
    for hashtag in hashtag_links:
        hashtag_text = hashtag.get_text(strip=True)
        if hashtag_text.startswith('#'):
            structure["hashtags"].append(hashtag_text)
    
    # Line breaks
    line_breaks = content_area.find_all('br')
    structure["line_breaks"] = len(line_breaks)
    
    # Formatting elements
    formatting_tags = ['strong', 'em', 'b', 'i']
    for tag in formatting_tags:
        elements = content_area.find_all(tag)
        if elements:
            structure["formatting_elements"].append(tag)
    
    return structure

def analyze_interaction_elements(soup):
    """Analyze interaction elements available."""
    interactions = {
        "has_follow_button": False,
        "available_reactions": [],
        "can_comment": False,
        "can_repost": False,
        "can_send_message": False
    }
    
    # Follow button
    follow_button = soup.find('button', class_=re.compile(r'follow'))
    interactions["has_follow_button"] = follow_button is not None
    
    # Available reaction types
    reaction_menu = soup.find(class_=re.compile(r'reactions-menu'))
    if reaction_menu:
        # LinkedIn typically has: Like, Celebrate, Support, Love, Insightful, Funny
        interactions["available_reactions"] = ["like", "celebrate", "support", "love", "insightful", "funny"]
    
    # Comment functionality
    comment_button = soup.find('button', {'aria-label': re.compile(r'comment', re.I)})
    interactions["can_comment"] = comment_button is not None
    
    # Repost functionality
    repost_button = soup.find('button', class_=re.compile(r'reshare|repost'))
    interactions["can_repost"] = repost_button is not None
    
    # Send message functionality
    send_button = soup.find('button', {'aria-label': re.compile(r'send.*message', re.I)})
    interactions["can_send_message"] = send_button is not None
    
    return interactions

def analyze_tracking_data(soup):
    """Extract tracking and analytics data."""
    tracking = {}
    
    # Tracking IDs from data attributes
    tracking_elem = soup.find(attrs={"data-view-tracking-scope": True})
    if tracking_elem:
        tracking_scope = tracking_elem.get("data-view-tracking-scope")
        try:
            tracking_data = json.loads(tracking_scope)
            if tracking_data and len(tracking_data) > 0:
                breadcrumb = tracking_data[0].get("breadcrumb", {})
                tracking["tracking_id"] = breadcrumb.get("trackingId")
                tracking["request_id"] = breadcrumb.get("requestId")
                tracking["module_key"] = breadcrumb.get("moduleKey")
        except:
            pass
    
    # Finite scroll item index
    finite_scroll = soup.find(attrs={"data-finite-scroll-hotkey-item": True})
    if finite_scroll:
        tracking["feed_position"] = finite_scroll.get("data-finite-scroll-hotkey-item")
    
    return tracking

def analyze_accessibility_data(soup):
    """Extract accessibility-related data."""
    accessibility = {
        "aria_labels": [],
        "alt_texts": [],
        "visually_hidden_content": []
    }
    
    # ARIA labels
    aria_elements = soup.find_all(attrs={"aria-label": True})
    for elem in aria_elements[:10]:  # Limit to prevent overwhelming data
        aria_label = elem.get("aria-label")
        if aria_label and len(aria_label) < 200:  # Reasonable length
            accessibility["aria_labels"].append(aria_label)
    
    # Alt texts
    images = soup.find_all('img', alt=True)
    for img in images:
        alt_text = img.get('alt')
        if alt_text and alt_text.strip():
            accessibility["alt_texts"].append(alt_text)
    
    # Visually hidden content (often contains important semantic info)
    hidden_elements = soup.find_all(class_=re.compile(r'visually-hidden'))
    for elem in hidden_elements[:5]:  # Limit to most relevant
        hidden_text = elem.get_text(strip=True)
        if hidden_text and len(hidden_text) < 100:
            accessibility["visually_hidden_content"].append(hidden_text)
    
    return accessibility

def generate_enhancement_recommendations(analysis_results):
    """Generate recommendations for schema enhancements based on analysis."""
    
    recommendations = {
        "high_priority": [],
        "medium_priority": [],
        "low_priority": [],
        "implementation_notes": []
    }
    
    # Analyze frequency of extractable fields
    field_frequency = defaultdict(int)
    
    for post_analysis in analysis_results:
        # Count available fields
        if post_analysis.get("media_content", {}).get("videos"):
            field_frequency["video_content"] += 1
        if post_analysis.get("media_content", {}).get("images"):
            field_frequency["image_content"] += 1
        if post_analysis.get("media_content", {}).get("articles"):
            field_frequency["article_links"] += 1
        if post_analysis.get("author_metadata", {}).get("is_verified"):
            field_frequency["author_verification"] += 1
        if post_analysis.get("author_metadata", {}).get("profile_url"):
            field_frequency["author_profile_url"] += 1
        if post_analysis.get("engagement_details", {}).get("reaction_types"):
            field_frequency["reaction_types"] += 1
        if post_analysis.get("content_structure", {}).get("external_links"):
            field_frequency["external_links"] += 1
        if post_analysis.get("content_structure", {}).get("linkedin_mentions"):
            field_frequency["linkedin_mentions"] += 1
        if post_analysis.get("post_metadata", {}).get("visibility"):
            field_frequency["post_visibility"] += 1
    
    total_posts = len(analysis_results)
    
    # High priority (>70% of posts have this data)
    high_threshold = total_posts * 0.7
    for field, count in field_frequency.items():
        if count >= high_threshold:
            recommendations["high_priority"].append({
                "field": field,
                "frequency": f"{count}/{total_posts} ({count/total_posts*100:.1f}%)",
                "description": get_field_description(field)
            })
    
    # Medium priority (30-70% of posts)
    medium_threshold = total_posts * 0.3
    for field, count in field_frequency.items():
        if medium_threshold <= count < high_threshold:
            recommendations["medium_priority"].append({
                "field": field,
                "frequency": f"{count}/{total_posts} ({count/total_posts*100:.1f}%)",
                "description": get_field_description(field)
            })
    
    # Low priority (<30% of posts)
    for field, count in field_frequency.items():
        if count < medium_threshold:
            recommendations["low_priority"].append({
                "field": field,
                "frequency": f"{count}/{total_posts} ({count/total_posts*100:.1f}%)",
                "description": get_field_description(field)
            })
    
    # Implementation notes
    recommendations["implementation_notes"] = [
        "High priority fields should be added to the main schema",
        "Medium priority fields could be optional/nullable fields",
        "Low priority fields might be better in a separate metadata object",
        "Consider rate limits when extracting author profile data",
        "Video/image URLs may be temporary and require re-validation"
    ]
    
    return recommendations

def get_field_description(field):
    """Get description for each field type."""
    descriptions = {
        "video_content": "Video URLs, thumbnails, duration - valuable for media analysis",
        "image_content": "Image URLs and metadata - essential for visual content",
        "article_links": "Shared article/link metadata - important for content analysis",
        "author_verification": "Author verification status - useful for credibility scoring",
        "author_profile_url": "Direct author profile URL - enables profile enrichment",
        "reaction_types": "Specific reaction types (like, love, etc.) - richer engagement data",
        "external_links": "External links shared in posts - valuable for link analysis",
        "linkedin_mentions": "Company/profile mentions - useful for network analysis",
        "post_visibility": "Post visibility settings - important for reach analysis"
    }
    return descriptions.get(field, "Additional metadata field")

def main():
    """Main analysis function."""
    print("🔍 LinkedIn HTML Schema Enhancement Analyzer")
    print("=" * 60)
    
    # Find the most recent HTML testing data
    data_dir = Path("data")
    html_dirs = [d for d in data_dir.iterdir() if d.is_dir() and "html_testing" in d.name]
    
    if not html_dirs:
        print("❌ No HTML testing data found in data/ directory")
        return
    
    # Get most recent directory
    latest_dir = max(html_dirs, key=lambda x: x.stat().st_mtime)
    
    # Find JSON file
    json_files = list(latest_dir.glob("*.json"))
    main_json = [f for f in json_files if "html_testing" in f.name and "analysis" not in f.name]
    
    if not main_json:
        print("❌ No main HTML testing JSON file found")
        return
    
    json_file = main_json[0]
    print(f"📂 Analyzing: {json_file}")
    
    # Load data
    with open(json_file, 'r', encoding='utf-8') as f:
        posts_data = json.load(f)
    
    print(f"📊 Found {len(posts_data)} posts to analyze")
    print()
    
    # Analyze each post
    analysis_results = []
    for i, post in enumerate(posts_data, 1):
        print(f"   Analyzing post {i}/{len(posts_data)}...")
        analysis = analyze_post_html(post)
        analysis_results.append(analysis)
    
    print()
    
    # Generate recommendations
    print("🚀 Generating schema enhancement recommendations...")
    recommendations = generate_enhancement_recommendations(analysis_results)
    
    # Save detailed analysis
    analysis_output = {
        "summary": {
            "total_posts_analyzed": len(posts_data),
            "analysis_timestamp": json_file.stat().st_mtime,
            "source_file": str(json_file)
        },
        "detailed_analysis": analysis_results,
        "recommendations": recommendations
    }
    
    output_file = latest_dir / f"schema_enhancement_analysis_{json_file.stem.split('_')[-1]}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_output, f, indent=2, ensure_ascii=False)
    
    # Print summary
    print()
    print("📋 SCHEMA ENHANCEMENT RECOMMENDATIONS")
    print("=" * 60)
    
    print("\n🔥 HIGH PRIORITY FIELDS (>70% of posts):")
    for rec in recommendations["high_priority"]:
        print(f"   • {rec['field']}: {rec['frequency']}")
        print(f"     {rec['description']}")
    
    print("\n⚡ MEDIUM PRIORITY FIELDS (30-70% of posts):")
    for rec in recommendations["medium_priority"]:
        print(f"   • {rec['field']}: {rec['frequency']}")
        print(f"     {rec['description']}")
    
    print("\n💡 LOW PRIORITY FIELDS (<30% of posts):")
    for rec in recommendations["low_priority"]:
        print(f"   • {rec['field']}: {rec['frequency']}")
        print(f"     {rec['description']}")
    
    print(f"\n💾 Detailed analysis saved to: {output_file}")
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main() 