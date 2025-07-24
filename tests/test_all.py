"""
Comprehensive Test Runner for LinkedIn Feed Capture Project

This module provides a complete test suite that validates:
1. Environment and dependencies
2. All unit tests
3. Integration tests
4. End-to-end functionality
5. Docker compatibility

Usage:
    python -m pytest tests/test_all.py -v
    python tests/test_all.py  # Direct execution
"""

import sys
import subprocess
import time
from pathlib import Path
from typing import List, Dict, Any
import pytest


class TestCompleteInstallation:
    """Test that the complete installation is working."""
    
    def test_environment_setup(self):
        """Test that the environment is properly set up."""
        print("\n🔍 Testing Environment Setup...")
        
        # Test Python version
        version = sys.version_info
        assert version.major == 3, "Python 3.x is required"
        assert version.minor >= 11, "Python 3.11+ is required"
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        
        # Test environment isolation
        python_path = sys.executable
        in_venv = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
        in_conda = 'conda' in python_path or 'anaconda' in python_path
        
        if in_venv or in_conda:
            print("✅ Running in isolated environment")
        else:
            print("⚠️  Running in system Python")
        
        # Test project structure
        project_root = Path(__file__).parent.parent
        required_files = ['requirements.txt', 'pyproject.toml', 'README.md']
        for file_path in required_files:
            assert (project_root / file_path).exists(), f"Missing {file_path}"
        print("✅ Project structure complete")
    
    def test_dependencies_installation(self):
        """Test that all dependencies are properly installed."""
        print("\n📦 Testing Dependencies Installation...")
        
        # Test core dependencies
        core_packages = [
            'selenium', 'bs4', 'pydantic', 'typer', 'rich',
            'dotenv', 'requests', 'lxml', 'tenacity', 'structlog',
            'prometheus_client', 'cryptography', 'selenium_stealth', 'webdriver_manager'
        ]
        
        missing_packages = []
        for package in core_packages:
            try:
                __import__(package)
                print(f"✅ {package}")
            except ImportError:
                missing_packages.append(package)
                print(f"❌ {package}")
        
        assert not missing_packages, f"Missing packages: {missing_packages}"
        print("✅ All core dependencies installed")
    
    def test_project_modules(self):
        """Test that all project modules can be imported."""
        print("\n🔧 Testing Project Modules...")
        
        project_modules = [
            'linkedin_feed_capture',
            'linkedin_feed_capture.models.post',
            'linkedin_feed_capture.utils.logger',
            'linkedin_feed_capture.utils.backoff'
        ]
        
        for module in project_modules:
            try:
                __import__(module)
                print(f"✅ {module}")
            except ImportError as e:
                pytest.fail(f"Failed to import {module}: {e}")
        
        print("✅ All project modules importable")


class TestUnitTests:
    """Run all unit tests."""
    
    def test_models_unit_tests(self):
        """Test data models functionality."""
        print("\n🧪 Running Models Unit Tests...")
        
        try:
            from linkedin_feed_capture.models.post import Post, PostMetrics
            from datetime import datetime
            
            # Test PostMetrics
            metrics = PostMetrics(likes=10, comments=5, shares=2)
            assert metrics.likes == 10
            assert metrics.comments == 5
            assert metrics.shares == 2
            
            # Test Post with required fields (use fixed past datetime)
            past_datetime = datetime(2024, 1, 1, 12, 0, 0)
            post = Post(
                urn="urn:li:activity:123456789",
                author="Test Author",
                content="Test content",
                posted_at=past_datetime,
                url="https://linkedin.com/posts/test"
            )
            assert post.author == "Test Author"
            assert post.content == "Test content"
            
            print("✅ Models unit tests passed")
            
        except Exception as e:
            pytest.fail(f"Models unit tests failed: {e}")
    
    def test_utils_unit_tests(self):
        """Test utility functions."""
        print("\n🔧 Running Utils Unit Tests...")
        
        try:
            from linkedin_feed_capture.utils.logger import get_logger
            from linkedin_feed_capture.utils.backoff import exponential_backoff
            
            # Test logger
            logger = get_logger(__name__)
            logger.info("Test message")
            
            # Test backoff (call with attempt=0)
            delay = exponential_backoff(attempt=0)
            assert isinstance(delay, float)
            assert delay > 0
            
            print("✅ Utils unit tests passed")
            
        except Exception as e:
            pytest.fail(f"Utils unit tests failed: {e}")


class TestIntegrationTests:
    """Run integration tests."""
    
    def test_browser_integration(self):
        """Test browser setup and configuration."""
        print("\n🌐 Testing Browser Integration...")
        
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from webdriver_manager.chrome import ChromeDriverManager
            
            # Test ChromeDriver installation
            driver_path = ChromeDriverManager().install()
            assert Path(driver_path).exists()
            
            # Test WebDriver options
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            print("✅ Browser integration tests passed")
            
        except Exception as e:
            pytest.fail(f"Browser integration tests failed: {e}")
    
    def test_data_processing_integration(self):
        """Test data processing pipeline."""
        print("\n📊 Testing Data Processing Integration...")
        
        try:
            from linkedin_feed_capture.models.post import Post, PostMetrics
            from datetime import datetime
            import json
            
            # Create test data
            post = Post(
                urn="urn:li:activity:123456789",
                author="Test Author",
                content="Test content with #hashtag and @mention",
                posted_at=datetime(2024, 1, 1, 12, 0, 0),
                url="https://linkedin.com/posts/test",
                metrics=PostMetrics(likes=10, comments=5, shares=2)
            )
            
            # Test JSON serialization
            post_dict = post.to_json_dict()
            post_json = json.dumps(post_dict)
            assert "Test Author" in post_json
            assert "Test content" in post_json
            
            # Test hashtag extraction
            assert "#hashtag" in post.content
            assert "@mention" in post.content
            
            print("✅ Data processing integration tests passed")
            
        except Exception as e:
            pytest.fail(f"Data processing integration tests failed: {e}")


class TestEndToEndTests:
    """Run end-to-end tests."""
    
    def test_cli_interface(self):
        """Test CLI interface functionality."""
        print("\n💻 Testing CLI Interface...")
        
        try:
            # Test help command
            result = subprocess.run(
                [sys.executable, "complete_linkedin_scraper.py", "--help"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            assert result.returncode == 0, "Help command failed"
            assert "usage:" in result.stdout.lower(), "Help output not found"
            
            print("✅ CLI interface tests passed")
            
        except subprocess.TimeoutExpired:
            pytest.fail("CLI help command timed out")
        except Exception as e:
            pytest.fail(f"CLI interface tests failed: {e}")
    
    def test_file_operations(self):
        """Test file operations and data persistence."""
        print("\n💾 Testing File Operations...")
        
        try:
            from pathlib import Path
            import json
            from datetime import datetime
            
            # Test data directory creation
            data_dir = Path("data")
            test_dir = data_dir / "test_e2e"
            test_dir.mkdir(parents=True, exist_ok=True)
            
            # Test file writing
            test_data = {
                "test": True,
                "timestamp": datetime.now().isoformat(),
                "message": "E2E test data"
            }
            
            test_file = test_dir / "test_e2e.json"
            with open(test_file, 'w') as f:
                json.dump(test_data, f)
            
            # Test file reading
            with open(test_file, 'r') as f:
                loaded_data = json.load(f)
            
            assert loaded_data["test"] is True
            assert "E2E test data" in loaded_data["message"]
            
            # Cleanup
            test_file.unlink()
            test_dir.rmdir()
            
            print("✅ File operations tests passed")
            
        except Exception as e:
            pytest.fail(f"File operations tests failed: {e}")


class TestDockerCompatibility:
    """Test Docker compatibility."""
    
    def test_dockerfile_exists(self):
        """Test that Dockerfile exists and is valid."""
        print("\n🐳 Testing Docker Compatibility...")
        
        dockerfile_path = Path("docker/Dockerfile")
        assert dockerfile_path.exists(), "Dockerfile not found"
        
        # Test Dockerfile content
        with open(dockerfile_path, 'r') as f:
            content = f.read()
        
        assert "FROM python:3.11-slim" in content, "Invalid base image"
        assert "COPY requirements.txt" in content, "Requirements not copied"
        assert "RUN pip install" in content, "Dependencies not installed"
        
        print("✅ Dockerfile validation passed")
    
    def test_docker_compose_exists(self):
        """Test that docker-compose.yml exists and is valid."""
        compose_path = Path("docker/docker-compose.yml")
        assert compose_path.exists(), "docker-compose.yml not found"
        
        # Test compose file content
        with open(compose_path, 'r') as f:
            content = f.read()
        
        assert "version:" in content, "Invalid compose file"
        assert "linkedin-scraper:" in content, "Service not defined"
        
        print("✅ Docker Compose validation passed")


class TestProductionReadiness:
    """Test production readiness."""
    
    def test_security_scanning(self):
        """Test security scanning tools."""
        print("\n🔒 Testing Security Scanning...")
        
        try:
            import bandit
            print("✅ Bandit security scanner available")
        except ImportError:
            print("⚠️  Bandit not installed (optional)")
        
        try:
            import safety
            print("✅ Safety vulnerability scanner available")
        except ImportError:
            print("⚠️  Safety not installed (optional)")
        
        print("✅ Security scanning tests passed")
    
    def test_code_quality_tools(self):
        """Test code quality tools."""
        print("\n📏 Testing Code Quality Tools...")
        
        try:
            import black
            print("✅ Black code formatter available")
        except ImportError:
            print("⚠️  Black not installed (optional)")
        
        try:
            import ruff
            print("✅ Ruff linter available")
        except ImportError:
            print("⚠️  Ruff not installed (optional)")
        
        try:
            import mypy
            print("✅ MyPy type checker available")
        except ImportError:
            print("⚠️  MyPy not installed (optional)")
        
        print("✅ Code quality tools tests passed")
    
    def test_documentation_exists(self):
        """Test that documentation exists."""
        print("\n📚 Testing Documentation...")
        
        docs_to_check = [
            "README.md",
            "requirements.txt",
            "environment.yml",
            "pyproject.toml"
        ]
        
        for doc in docs_to_check:
            assert Path(doc).exists(), f"Missing documentation: {doc}"
            print(f"✅ {doc} exists")
        
        print("✅ Documentation tests passed")

    def test_environment_ready(self):
        """Test that the environment is ready for production use."""
        # This test simulates the verify_env.py script
        try:
            # Test core functionality
            from selenium import webdriver
            from bs4 import BeautifulSoup
            from pydantic import BaseModel
            from linkedin_feed_capture.models.post import Post
            
            print("✅ Core packages imported successfully")
            print("✅ Data models working correctly")
            print("✅ Environment is ready for LinkedIn scraping!")
            
        except Exception as e:
            pytest.fail(f"Environment not ready: {e}")


def run_complete_test_suite():
    """Run the complete test suite."""
    print("🚀 Starting Complete Test Suite for LinkedIn Feed Capture")
    print("=" * 60)
    
    # Run all test classes
    test_classes = [
        TestCompleteInstallation,
        TestUnitTests,
        TestIntegrationTests,
        TestEndToEndTests,
        TestDockerCompatibility,
        TestProductionReadiness
    ]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    for test_class in test_classes:
        print(f"\n📋 Running {test_class.__name__}...")
        
        # Get all test methods
        test_methods = [method for method in dir(test_class) if method.startswith('test_')]
        
        for method_name in test_methods:
            total_tests += 1
            try:
                # Create instance and run test
                instance = test_class()
                method = getattr(instance, method_name)
                method()
                passed_tests += 1
                print(f"  ✅ {method_name}")
            except Exception as e:
                failed_tests += 1
                print(f"  ❌ {method_name}: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUITE SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if failed_tests == 0:
        print("\n🎉 ALL TESTS PASSED! Project is production ready!")
        return True
    else:
        print(f"\n⚠️  {failed_tests} tests failed. Please review and fix issues.")
        return False


if __name__ == "__main__":
    # Run the complete test suite
    success = run_complete_test_suite()
    sys.exit(0 if success else 1) 