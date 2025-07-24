#!/bin/bash
# LinkedIn Feed Capture Environment Activation Script

echo "🚀 Activating LinkedIn Feed Capture environment..."
eval "$(conda shell.bash hook)"
conda activate linkedin-feed-capture

echo "✅ Environment activated!"
echo "🔧 Available commands:"
echo "  🌟 python complete_linkedin_scraper_enhanced_fast.py --help  # PRIMARY RECOMMENDATION"
echo "  python complete_linkedin_scraper.py --help                  # Standard (limited)"
echo "  python setup_credentials.py"
echo "  pytest tests/"
echo "  python simple_linkedin_test.py"
echo ""
echo "📁 Current environment: $(conda info --envs | grep '*' | awk '{print $1}')"
echo "🐍 Python version: $(python --version)"
