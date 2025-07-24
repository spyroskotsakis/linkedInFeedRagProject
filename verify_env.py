#!/usr/bin/env python3
"""
Environment Verification Script
Validates that all required packages are installed and working correctly.
"""

import sys
import subprocess
from pathlib import Path

def check_package(package_name, import_name=None):
    """Check if a package is installed and importable."""
    import_name = import_name or package_name
    try:
        module = __import__(import_name.replace('-', '_'))
        version = getattr(module, '__version__', 'unknown')
        print(f"✅ {package_name}: {version}")
        return True
    except ImportError:
        print(f"❌ {package_name}: NOT FOUND")
        return False

def main():
    print("🔍 LinkedIn Feed Capture - Environment Verification")
    print("=" * 50)
    
    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"🐍 Python: {python_version}")
    
    # Check environment
    python_path = sys.executable
    if "linkedin-feed-capture" in python_path:
        print("✅ Conda Environment: linkedin-feed-capture")
    else:
        print("❌ Wrong Environment: NOT in linkedin-feed-capture")
        print(f"   Current path: {python_path}")
    
    # Required packages
    packages = [
        ("selenium", "selenium"),
        ("beautifulsoup4", "bs4"),
        ("pydantic", "pydantic"), 
        ("typer", "typer"),
        ("rich", "rich"),
        ("python-dotenv", "dotenv"),
        ("requests", "requests"),
        ("lxml", "lxml"),
        ("tenacity", "tenacity"),
        ("structlog", "structlog"),
        ("prometheus-client", "prometheus_client"),
        ("cryptography", "cryptography"),
        ("selenium-stealth", "selenium_stealth"),
        ("webdriver-manager", "webdriver_manager"),
        ("pytest", "pytest"),
        ("pytest-cov", "pytest_cov"),
    ]
    
    all_good = True
    for package_name, import_name in packages:
        if not check_package(package_name, import_name):
            all_good = False
    
    print("\n" + "=" * 50)
    if all_good:
        print("🎉 All packages verified successfully!")
        print("✅ Environment is ready for LinkedIn scraping!")
    else:
        print("❌ Some packages are missing or not working correctly.")
        print("🔧 Try running: conda env update -f environment.yml")
        sys.exit(1)

if __name__ == "__main__":
    main()
