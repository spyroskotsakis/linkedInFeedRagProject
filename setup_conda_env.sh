#!/bin/bash

# LinkedIn Feed Capture - Conda Environment Setup Script
# This script automates the creation and setup of the conda environment
# for the LinkedIn Feed Capture project.

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
ENV_NAME="linkedin-feed-capture"
PYTHON_VERSION="3.11"

echo -e "${BLUE}"
echo "============================================================="
echo "🚀 LinkedIn Feed Capture - Conda Environment Setup"
echo "============================================================="
echo -e "${NC}"

# Function to print status messages
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${CYAN}ℹ️  $1${NC}"
}

# Check if conda is installed
check_conda() {
    print_info "Checking for conda installation..."
    if command -v conda &> /dev/null; then
        print_status "Conda is installed"
        conda --version
    else
        print_error "Conda is not installed. Please install Anaconda or Miniconda first."
        echo -e "${CYAN}Download from: https://docs.conda.io/en/latest/miniconda.html${NC}"
        exit 1
    fi
}

# Check if environment.yml exists
check_environment_file() {
    print_info "Checking for environment.yml..."
    if [[ -f "environment.yml" ]]; then
        print_status "environment.yml found"
    else
        print_error "environment.yml not found in current directory"
        exit 1
    fi
}

# Remove existing environment if it exists
remove_existing_env() {
    print_info "Checking for existing environment: $ENV_NAME"
    if conda env list | grep -q "^$ENV_NAME "; then
        print_warning "Environment $ENV_NAME already exists"
        read -p "Do you want to remove it and create a fresh one? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Removing existing environment..."
            conda env remove -n $ENV_NAME -y
            print_status "Existing environment removed"
        else
            print_info "Using existing environment"
            return 0
        fi
    fi
}

# Create conda environment
create_environment() {
    print_info "Creating conda environment from environment.yml..."
    if conda env create -f environment.yml; then
        print_status "Environment created successfully"
    else
        print_error "Failed to create environment"
        exit 1
    fi
}

# Validate environment
validate_environment() {
    print_info "Validating environment setup..."
    
    # Activate environment and run validation
    eval "$(conda shell.bash hook)"
    conda activate $ENV_NAME
    
    # Check Python version
    python_version=$(python --version 2>&1)
    print_status "Python version: $python_version"
    
    # Check key packages
    key_packages=("selenium" "beautifulsoup4" "pydantic" "typer" "pytest")
    
    for package in "${key_packages[@]}"; do
        if python -c "import $package" 2>/dev/null; then
            version=$(python -c "import $package; print(getattr($package, '__version__', 'unknown'))" 2>/dev/null || echo "unknown")
            print_status "$package: $version"
        else
            print_error "Package $package not found"
            exit 1
        fi
    done
    
    # Check selenium-stealth (pip package)
    if python -c "import selenium_stealth" 2>/dev/null; then
        print_status "selenium-stealth: installed"
    else
        print_error "selenium-stealth not found"
        exit 1
    fi
    
    # Check webdriver-manager (pip package)
    if python -c "import webdriver_manager" 2>/dev/null; then
        print_status "webdriver-manager: installed"
    else
        print_error "webdriver-manager not found"
        exit 1
    fi
}

# Setup pre-commit hooks
setup_precommit() {
    print_info "Setting up pre-commit hooks..."
    eval "$(conda shell.bash hook)"
    conda activate $ENV_NAME
    
    if [[ -f ".pre-commit-config.yaml" ]]; then
        pre-commit install
        print_status "Pre-commit hooks installed"
    else
        print_warning "No .pre-commit-config.yaml found, skipping pre-commit setup"
    fi
}

# Create activation script
create_activation_script() {
    print_info "Creating activation script..."
    
    cat > activate_env.sh << 'EOF'
#!/bin/bash
# LinkedIn Feed Capture Environment Activation Script

echo "🚀 Activating LinkedIn Feed Capture environment..."
eval "$(conda shell.bash hook)"
conda activate linkedin-feed-capture

echo "✅ Environment activated!"
echo "🔧 Available commands:"
echo "  python complete_linkedin_scraper.py --help"
echo "  python setup_credentials.py"
echo "  pytest tests/"
echo "  python simple_linkedin_test.py"
echo ""
echo "📁 Current environment: $(conda info --envs | grep '*' | awk '{print $1}')"
echo "🐍 Python version: $(python --version)"
EOF

    chmod +x activate_env.sh
    print_status "Created activate_env.sh script"
}

# Create verification script
create_verification_script() {
    print_info "Creating environment verification script..."
    
    cat > verify_env.py << 'EOF'
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
EOF

    print_status "Created verify_env.py script"
}

# Main execution
main() {
    echo -e "${PURPLE}Starting environment setup...${NC}"
    
    check_conda
    check_environment_file
    remove_existing_env
    create_environment
    validate_environment
    setup_precommit
    create_activation_script
    create_verification_script
    
    echo -e "${GREEN}"
    echo "============================================================="
    echo "🎉 Environment Setup Complete!"
    echo "============================================================="
    echo -e "${NC}"
    
    echo -e "${CYAN}📋 Next Steps:${NC}"
    echo "1. Activate environment:"
    echo -e "${YELLOW}   source activate_env.sh${NC}"
    echo ""
    echo "2. Set up credentials:"
    echo -e "${YELLOW}   python setup_credentials.py${NC}"
    echo ""
    echo "3. Run verification:"
    echo -e "${YELLOW}   python verify_env.py${NC}"
    echo ""
    echo "4. Test connection:"
    echo -e "${YELLOW}   python simple_linkedin_test.py${NC}"
    echo ""
    echo "5. Run scraper:"
    echo -e "${YELLOW}   python complete_linkedin_scraper.py --posts 5 --verbose${NC}"
    echo ""
    echo -e "${GREEN}✅ Production environment ready!${NC}"
}

# Run main function
main "$@" 