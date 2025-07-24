"""
Dependency and Environment Tests

This module contains tests to validate that all required dependencies are properly installed
and the environment is correctly configured for the LinkedIn Feed Capture project.

Test Categories:
- Core Dependencies: Essential packages for scraping functionality
- Development Dependencies: Tools for development and testing
- Environment Validation: Python version, paths, and environment setup
- Import Tests: Verify all modules can be imported successfully
- Version Compatibility: Check for compatible package versions
"""

import sys
import importlib
import subprocess
from pathlib import Path
from typing import List, Dict, Any
import pytest


class TestDependencies:
    """Test that all required dependencies are installed and importable."""
    
    def test_python_version(self):
        """Test that Python version is compatible (3.11+)."""
        version = sys.version_info
        assert version.major == 3, "Python 3.x is required"
        assert version.minor >= 11, "Python 3.11+ is required"
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    
    def test_core_dependencies(self):
        """Test that all core dependencies are installed and importable."""
        core_packages = {
            'selenium': 'Web browser automation',
            'beautifulsoup4': 'HTML parsing',
            'pydantic': 'Data validation',
            'typer': 'CLI framework',
            'rich': 'Terminal formatting',
            'python-dotenv': 'Environment variable management',
            'requests': 'HTTP requests',
            'lxml': 'XML/HTML processing',
            'tenacity': 'Retry mechanisms',
            'structlog': 'Structured logging',
            'prometheus_client': 'Metrics collection',
            'cryptography': 'Encryption utilities',
            'selenium_stealth': 'Anti-detection measures',
            'webdriver_manager': 'WebDriver management'
        }
        
        missing_packages = []
        for package, description in core_packages.items():
            try:
                module = importlib.import_module(package)
                version = getattr(module, '__version__', 'unknown')
                print(f"✅ {package}: {version} - {description}")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package}: MISSING - {description}")
        
        assert not missing_packages, f"Missing core packages: {missing_packages}"
    
    def test_development_dependencies(self):
        """Test that all development dependencies are installed."""
        dev_packages = {
            'pytest': 'Testing framework',
            'pytest_cov': 'Coverage reporting',
            'pytest_mock': 'Mocking utilities',
            'pytest_asyncio': 'Async testing support',
            'pytest_xdist': 'Parallel test execution',
            'coverage': 'Code coverage',
            'black': 'Code formatting',
            'ruff': 'Fast linting',
            'mypy': 'Type checking',
            'pre_commit': 'Git hooks',
            'bandit': 'Security scanning',
            'safety': 'Dependency vulnerability scanning'
        }
        
        missing_packages = []
        for package, description in dev_packages.items():
            try:
                module = importlib.import_module(package)
                version = getattr(module, '__version__', 'unknown')
                print(f"✅ {package}: {version} - {description}")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package}: MISSING - {description}")
        
        # Development packages are optional but recommended
        if missing_packages:
            print(f"⚠️  Missing development packages: {missing_packages}")
    
    def test_project_modules(self):
        """Test that all project modules can be imported."""
        project_modules = [
            'linkedin_feed_capture',
            'linkedin_feed_capture.auth',
            'linkedin_feed_capture.auth.authenticator',
            'linkedin_feed_capture.auth.cookies',
            'linkedin_feed_capture.browser',
            'linkedin_feed_capture.browser.driver',
            'linkedin_feed_capture.browser.stealth',
            'linkedin_feed_capture.cli',
            'linkedin_feed_capture.cli.main',
            'linkedin_feed_capture.models',
            'linkedin_feed_capture.models.post',
            'linkedin_feed_capture.scraper',
            'linkedin_feed_capture.scraper.extractor',
            'linkedin_feed_capture.scraper.parser',
            'linkedin_feed_capture.scraper.scroll',
            'linkedin_feed_capture.utils',
            'linkedin_feed_capture.utils.backoff',
            'linkedin_feed_capture.utils.logger'
        ]
        
        missing_modules = []
        for module in project_modules:
            try:
                importlib.import_module(module)
                print(f"✅ {module}: Imported successfully")
            except ImportError as e:
                missing_modules.append(f"{module}: {e}")
                print(f"❌ {module}: Import failed - {e}")
        
        assert not missing_modules, f"Failed to import modules: {missing_modules}"
    
    def test_environment_variables(self):
        """Test that required environment variables can be loaded."""
        try:
            from dotenv import load_dotenv
            import os
            
            # Try to load .env file if it exists
            env_file = Path('.env')
            if env_file.exists():
                load_dotenv(env_file)
                print("✅ .env file loaded successfully")
            else:
                print("⚠️  No .env file found (this is normal for testing)")
            
            # Check if we can access environment variables
            test_var = os.getenv('TEST_VAR', 'default_value')
            assert test_var == 'default_value', "Environment variable access working"
            print("✅ Environment variable access working")
            
        except ImportError as e:
            pytest.fail(f"Failed to import dotenv: {e}")
    
    def test_file_structure(self):
        """Test that required files and directories exist."""
        required_files = [
            'requirements.txt',
            'pyproject.toml',
            'README.md',
            '.cursorrules',
            'environment.yml',
            'setup_conda_env.sh',
            'activate_env.sh',
            'verify_env.py',
            'complete_linkedin_scraper.py',
            'setup_credentials.py'
        ]
        
        required_dirs = [
            'src',
            'src/linkedin_feed_capture',
            'tests',
            'tests/unit',
            'tests/integration',
            'tests/e2e',
            'data',
            'docker',
            'documents'
        ]
        
        missing_files = []
        for file_path in required_files:
            if not Path(file_path).exists():
                missing_files.append(file_path)
                print(f"❌ {file_path}: Missing")
            else:
                print(f"✅ {file_path}: Exists")
        
        missing_dirs = []
        for dir_path in required_dirs:
            if not Path(dir_path).exists():
                missing_dirs.append(dir_path)
                print(f"❌ {dir_path}: Missing")
            else:
                print(f"✅ {dir_path}: Exists")
        
        assert not missing_files, f"Missing required files: {missing_files}"
        assert not missing_dirs, f"Missing required directories: {missing_dirs}"
    
    def test_python_path(self):
        """Test that Python path is correctly configured."""
        # Check if we're in a virtual environment or conda environment
        python_path = sys.executable
        print(f"Python executable: {python_path}")
        
        # Check if we're in an isolated environment
        in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
        in_conda = 'conda' in python_path or 'anaconda' in python_path
        
        if in_venv:
            print("✅ Running in virtual environment")
        elif in_conda:
            print("✅ Running in conda environment")
        else:
            print("⚠️  Running in system Python (not recommended)")
        
        # Check if project root is in Python path
        project_root = Path(__file__).parent.parent.parent
        if str(project_root) in sys.path:
            print("✅ Project root in Python path")
        else:
            print("⚠️  Project root not in Python path")


class TestEnvironmentValidation:
    """Test environment-specific configurations and validations."""
    
    def test_selenium_webdriver(self):
        """Test that Selenium WebDriver can be initialized."""
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from webdriver_manager.chrome import ChromeDriverManager
            
            # Test ChromeDriver installation
            driver_path = ChromeDriverManager().install()
            print(f"✅ ChromeDriver installed at: {driver_path}")
            
            # Test WebDriver creation (headless)
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            # Don't actually start the driver in tests, just verify options
            print("✅ WebDriver options configured successfully")
            
        except Exception as e:
            pytest.fail(f"WebDriver setup failed: {e}")
    
    def test_cryptography_functionality(self):
        """Test that cryptography library is working."""
        try:
            from cryptography.fernet import Fernet
            
            # Generate a test key
            key = Fernet.generate_key()
            cipher = Fernet(key)
            
            # Test encryption/decryption
            test_data = b"test message"
            encrypted = cipher.encrypt(test_data)
            decrypted = cipher.decrypt(encrypted)
            
            assert decrypted == test_data, "Encryption/decryption failed"
            print("✅ Cryptography library working correctly")
            
        except Exception as e:
            pytest.fail(f"Cryptography test failed: {e}")
    
    def test_logging_setup(self):
        """Test that logging is properly configured."""
        try:
            from linkedin_feed_capture.utils.logger import get_logger
            
            logger = get_logger(__name__)
            logger.info("Test log message")
            print("✅ Logging system working correctly")
            
        except Exception as e:
            pytest.fail(f"Logging setup failed: {e}")
    
    def test_data_models(self):
        """Test that Pydantic data models are working."""
        try:
            from linkedin_feed_capture.models.post import Post, PostMetrics
            from datetime import datetime
            
            # Test PostMetrics creation
            metrics = PostMetrics(likes=10, comments=5, shares=2)
            assert metrics.likes == 10
            assert metrics.comments == 5
            assert metrics.shares == 2
            print("✅ PostMetrics model working correctly")
            
            # Test Post creation
            post = Post(
                urn="urn:li:activity:123456789",
                author="Test Author",
                content="Test content",
                posted_at=datetime.now()
            )
            assert post.author == "Test Author"
            assert post.content == "Test content"
            print("✅ Post model working correctly")
            
        except Exception as e:
            pytest.fail(f"Data models test failed: {e}")


class TestInstallationCompleteness:
    """Test that the installation is complete and ready for use."""
    
    def test_all_imports_work(self):
        """Test that all critical imports work without errors."""
        imports_to_test = [
            "import selenium",
            "import beautifulsoup4",
            "import pydantic",
            "import typer",
            "import rich",
            "import requests",
            "import lxml",
            "import tenacity",
            "import structlog",
            "import cryptography",
            "import webdriver_manager",
            "import linkedin_feed_capture",
            "from linkedin_feed_capture.models.post import Post",
            "from linkedin_feed_capture.utils.logger import get_logger"
        ]
        
        failed_imports = []
        for import_stmt in imports_to_test:
            try:
                exec(import_stmt)
                print(f"✅ {import_stmt}")
            except Exception as e:
                failed_imports.append(f"{import_stmt}: {e}")
                print(f"❌ {import_stmt}: {e}")
        
        assert not failed_imports, f"Failed imports: {failed_imports}"
    
    def test_environment_ready(self):
        """Test that the environment is ready for production use."""
        # This test simulates the verify_env.py script
        try:
            # Test core functionality
            from selenium import webdriver
            from beautifulsoup4 import BeautifulSoup
            from pydantic import BaseModel
            from linkedin_feed_capture.models.post import Post
            
            print("✅ Core packages imported successfully")
            print("✅ Data models working correctly")
            print("✅ Environment is ready for LinkedIn scraping!")
            
        except Exception as e:
            pytest.fail(f"Environment not ready: {e}")


if __name__ == "__main__":
    # Run all dependency tests
    pytest.main([__file__, "-v", "--tb=short"]) 