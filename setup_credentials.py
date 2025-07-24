#!/usr/bin/env python3
"""
LinkedIn Feed Capture - Credential Setup
This script helps you configure your LinkedIn credentials securely.
"""

import os
from pathlib import Path

def create_env_file():
    """Create .env file with proper template"""
    
    env_content = """# LinkedIn Feed Capture Configuration
# REPLACE THE VALUES BELOW WITH YOUR ACTUAL LINKEDIN CREDENTIALS

# LinkedIn Authentication (REQUIRED - Replace with your credentials)
LINKEDIN_EMAIL=your.email@example.com
LINKEDIN_PASSWORD=your_actual_password_here

# Optional Configuration (you can leave these as-is)
COOKIE_PATH=./data/cookies.pkl
COOKIE_ENCRYPTION_KEY=linkedin_scraper_key_2024

# Scraping Configuration
MAX_POSTS=20
SCROLL_DELAY_MS=2500

# Logging
LOG_LEVEL=INFO
LOG_FILE=./logs/linkedin_scraper.log

# Browser Configuration  
HEADLESS=false
STEALTH_MODE=true
"""

    env_file = Path(".env")
    env_file.write_text(env_content)
    
    print("✅ Created .env file")
    print(f"📁 Location: {env_file.absolute()}")
    print()
    print("🔐 NEXT STEPS:")
    print("1. Open the .env file in your editor")
    print("2. Replace 'your.email@example.com' with your LinkedIn email") 
    print("3. Replace 'your_actual_password_here' with your LinkedIn password")
    print("4. Save the file")
    print("5. Run: python test_linkedin_connection.py")
    print()
    print("⚠️  SECURITY NOTE:")
    print("   - The .env file contains your password in plain text")
    print("   - Never commit this file to version control") 
    print("   - The .gitignore should already exclude it")

def show_current_config():
    """Show current configuration status"""
    
    print("🔍 Current Configuration Status:")
    print("=" * 50)
    
    env_file = Path(".env")
    if env_file.exists():
        print("✅ .env file exists")
        
        # Check if credentials are filled
        content = env_file.read_text()
        if "your.email@example.com" in content:
            print("❌ LinkedIn email not configured (still has placeholder)")
        else:
            print("✅ LinkedIn email configured")
            
        if "your_actual_password_here" in content:
            print("❌ LinkedIn password not configured (still has placeholder)")
        else:
            print("✅ LinkedIn password configured")
    else:
        print("❌ .env file does not exist")
    
    # Check directories
    data_dir = Path("data")
    logs_dir = Path("logs")
    
    if data_dir.exists():
        print("✅ Data directory exists")
    else:
        print("❌ Data directory missing")
        
    if logs_dir.exists():
        print("✅ Logs directory exists") 
    else:
        print("❌ Logs directory missing")

def main():
    """Main setup function"""
    
    print("🚀 LinkedIn Feed Capture - Credential Setup")
    print("=" * 60)
    print()
    
    # Create necessary directories
    Path("data").mkdir(exist_ok=True)
    Path("logs").mkdir(exist_ok=True)
    print("✅ Created data and logs directories")
    
    # Show current status
    show_current_config()
    print()
    
    # Ask user what to do
    env_file = Path(".env")
    if env_file.exists():
        choice = input("📝 .env file already exists. Recreate it? (y/N): ").lower()
        if choice in ['y', 'yes']:
            create_env_file()
        else:
            print("📋 Using existing .env file")
    else:
        create_env_file()
    
    print()
    print("🎯 READY TO PROCEED:")
    print("Once you've added your credentials to .env, you can:")
    print("1. Test connection: python test_linkedin_connection.py")
    print("2. Run scraper: python -m linkedin_feed_capture.cli.main capture --posts 10")
    print("3. Stream results: python -m linkedin_feed_capture.cli.main capture --posts 20 --streaming --pretty")

if __name__ == "__main__":
    main() 