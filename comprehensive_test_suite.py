#!/usr/bin/env python3
"""
Comprehensive Test Suite for LinkedIn Feed Scraper
Validates all three phases and ensures production readiness
"""

import asyncio
import json
import time
import logging
from datetime import datetime
from pathlib import Path
import subprocess
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('comprehensive_test_suite.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ComprehensiveTestSuite:
    """Comprehensive test suite for LinkedIn scraper validation"""
    
    def __init__(self):
        self.test_results = {}
        self.start_time = time.time()
        
    def test_phase_1_dom_investigation(self):
        """Test Phase 1: DOM Investigation"""
        logger.info("🧪 TESTING PHASE 1: DOM INVESTIGATION")
        logger.info("=" * 50)
        
        try:
            # Run DOM investigation
            result = subprocess.run([
                sys.executable, "dom_investigation.py"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ DOM investigation completed successfully")
                
                # Check if results file was created
                results_files = list(Path(".").glob("dom_investigation_results_*.json"))
                if results_files:
                    logger.info(f"✅ Investigation results saved: {results_files[0].name}")
                    
                    # Analyze results
                    with open(results_files[0], 'r') as f:
                        data = json.load(f)
                    
                    working_selectors = 0
                    total_selectors = 0
                    
                    for post in data:
                        for category, selectors in post["selectors_tested"].items():
                            for selector, info in selectors.items():
                                total_selectors += 1
                                if isinstance(info, dict) and info.get("found", False):
                                    working_selectors += 1
                    
                    success_rate = (working_selectors / total_selectors * 100) if total_selectors > 0 else 0
                    logger.info(f"📊 Selector Success Rate: {success_rate:.1f}%")
                    
                    self.test_results["phase_1"] = {
                        "status": "PASS",
                        "success_rate": success_rate,
                        "working_selectors": working_selectors,
                        "total_selectors": total_selectors
                    }
                else:
                    logger.error("❌ No investigation results file found")
                    self.test_results["phase_1"] = {"status": "FAIL", "error": "No results file"}
            else:
                logger.error(f"❌ DOM investigation failed: {result.stderr}")
                self.test_results["phase_1"] = {"status": "FAIL", "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            logger.error("❌ DOM investigation timed out")
            self.test_results["phase_1"] = {"status": "FAIL", "error": "Timeout"}
        except Exception as e:
            logger.error(f"❌ DOM investigation error: {e}")
            self.test_results["phase_1"] = {"status": "FAIL", "error": str(e)}
    
    def test_phase_2_enhanced_scraper(self):
        """Test Phase 2: Enhanced Scraper with Updated Selectors"""
        logger.info("🧪 TESTING PHASE 2: ENHANCED SCRAPER")
        logger.info("=" * 50)
        
        try:
            # Run enhanced scraper
            result = subprocess.run([
                sys.executable, "complete_linkedin_scraper_v2.py", "--posts", "3", "--verbose"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ Enhanced scraper completed successfully")
                
                # Check if data was saved
                data_dirs = list(Path("data").glob("posts_*_*"))
                if data_dirs:
                    latest_dir = max(data_dirs, key=lambda x: x.stat().st_mtime)
                    logger.info(f"✅ Data saved in: {latest_dir}")
                    
                    # Check for required files
                    json_files = list(latest_dir.glob("*.json"))
                    txt_files = list(latest_dir.glob("*.txt"))
                    
                    if json_files and txt_files:
                        logger.info(f"✅ Generated {len(json_files)} JSON files and {len(txt_files)} text files")
                        
                        # Analyze data quality
                        with open(json_files[0], 'r') as f:
                            data = json.load(f)
                        
                        posts_with_content = sum(1 for post in data if post.get('content') and len(post['content']) > 10)
                        posts_with_author = sum(1 for post in data if post.get('author') and post['author'] != "Unknown Author")
                        
                        content_success_rate = (posts_with_content / len(data) * 100) if data else 0
                        author_success_rate = (posts_with_author / len(data) * 100) if data else 0
                        
                        logger.info(f"📊 Content Success Rate: {content_success_rate:.1f}%")
                        logger.info(f"📊 Author Success Rate: {author_success_rate:.1f}%")
                        
                        self.test_results["phase_2"] = {
                            "status": "PASS",
                            "content_success_rate": content_success_rate,
                            "author_success_rate": author_success_rate,
                            "total_posts": len(data),
                            "posts_with_content": posts_with_content,
                            "posts_with_author": posts_with_author
                        }
                    else:
                        logger.error("❌ Required output files not found")
                        self.test_results["phase_2"] = {"status": "FAIL", "error": "Missing output files"}
                else:
                    logger.error("❌ No data directory created")
                    self.test_results["phase_2"] = {"status": "FAIL", "error": "No data directory"}
            else:
                logger.error(f"❌ Enhanced scraper failed: {result.stderr}")
                self.test_results["phase_2"] = {"status": "FAIL", "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            logger.error("❌ Enhanced scraper timed out")
            self.test_results["phase_2"] = {"status": "FAIL", "error": "Timeout"}
        except Exception as e:
            logger.error(f"❌ Enhanced scraper error: {e}")
            self.test_results["phase_2"] = {"status": "FAIL", "error": str(e)}
    
    def test_phase_3_production_scraper(self):
        """Test Phase 3: Production Scraper"""
        logger.info("🧪 TESTING PHASE 3: PRODUCTION SCRAPER")
        logger.info("=" * 50)
        
        try:
            # Run production scraper
            result = subprocess.run([
                sys.executable, "production_scraper.py", "--posts", "3", "--method", "selenium", "--verbose"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ Production scraper completed successfully")
                
                # Check if data was saved
                data_dirs = list(Path("data").glob("posts_*_production"))
                if data_dirs:
                    latest_dir = max(data_dirs, key=lambda x: x.stat().st_mtime)
                    logger.info(f"✅ Production data saved in: {latest_dir}")
                    
                    # Check for comprehensive output
                    json_files = list(latest_dir.glob("*.json"))
                    txt_files = list(latest_dir.glob("*.txt"))
                    
                    if json_files:
                        with open(json_files[0], 'r') as f:
                            data = json.load(f)
                        
                        # Validate production data structure
                        if "metadata" in data and "posts" in data and "analytics" in data:
                            logger.info("✅ Production data structure validated")
                            
                            metadata = data["metadata"]
                            posts = data["posts"]
                            analytics = data["analytics"]
                            
                            success_rate = metadata.get("success_rate", 0)
                            error_count = metadata.get("error_count", 0)
                            total_posts = len(posts)
                            
                            logger.info(f"📊 Production Success Rate: {success_rate:.1f}%")
                            logger.info(f"📊 Error Count: {error_count}")
                            logger.info(f"📊 Total Posts: {total_posts}")
                            
                            self.test_results["phase_3"] = {
                                "status": "PASS",
                                "success_rate": success_rate,
                                "error_count": error_count,
                                "total_posts": total_posts,
                                "has_metadata": True,
                                "has_analytics": True
                            }
                        else:
                            logger.error("❌ Invalid production data structure")
                            self.test_results["phase_3"] = {"status": "FAIL", "error": "Invalid data structure"}
                    else:
                        logger.error("❌ No production output files found")
                        self.test_results["phase_3"] = {"status": "FAIL", "error": "No output files"}
                else:
                    logger.error("❌ No production data directory created")
                    self.test_results["phase_3"] = {"status": "FAIL", "error": "No data directory"}
            else:
                logger.error(f"❌ Production scraper failed: {result.stderr}")
                self.test_results["phase_3"] = {"status": "FAIL", "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            logger.error("❌ Production scraper timed out")
            self.test_results["phase_3"] = {"status": "FAIL", "error": "Timeout"}
        except Exception as e:
            logger.error(f"❌ Production scraper error: {e}")
            self.test_results["phase_3"] = {"status": "FAIL", "error": str(e)}
    
    def test_network_interceptor(self):
        """Test Network Interceptor (Phase 3 Advanced)"""
        logger.info("🧪 TESTING NETWORK INTERCEPTOR")
        logger.info("=" * 50)
        
        try:
            # Run network interceptor
            result = subprocess.run([
                sys.executable, "network_interceptor.py"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ Network interceptor completed successfully")
                
                # Check if network capture file was created
                capture_files = list(Path(".").glob("network_capture_*.json"))
                if capture_files:
                    logger.info(f"✅ Network capture saved: {capture_files[0].name}")
                    
                    with open(capture_files[0], 'r') as f:
                        data = json.load(f)
                    
                    total_posts = data.get("total_posts", 0)
                    network_logs = data.get("network_logs_count", 0)
                    graphql_responses = data.get("graphql_responses_count", 0)
                    
                    logger.info(f"📊 Network Posts Captured: {total_posts}")
                    logger.info(f"📊 Network Logs: {network_logs}")
                    logger.info(f"📊 GraphQL Responses: {graphql_responses}")
                    
                    self.test_results["network_interceptor"] = {
                        "status": "PASS",
                        "total_posts": total_posts,
                        "network_logs": network_logs,
                        "graphql_responses": graphql_responses
                    }
                else:
                    logger.warning("⚠️  No network capture file found")
                    self.test_results["network_interceptor"] = {"status": "WARNING", "error": "No capture file"}
            else:
                logger.warning(f"⚠️  Network interceptor failed: {result.stderr}")
                self.test_results["network_interceptor"] = {"status": "WARNING", "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            logger.warning("⚠️  Network interceptor timed out")
            self.test_results["network_interceptor"] = {"status": "WARNING", "error": "Timeout"}
        except Exception as e:
            logger.warning(f"⚠️  Network interceptor error: {e}")
            self.test_results["network_interceptor"] = {"status": "WARNING", "error": str(e)}
    
    def test_playwright_scraper(self):
        """Test Playwright Scraper (Phase 3 Alternative)"""
        logger.info("🧪 TESTING PLAYWRIGHT SCRAPER")
        logger.info("=" * 50)
        
        try:
            # Check if playwright is installed
            try:
                import playwright
                logger.info("✅ Playwright is installed")
            except ImportError:
                logger.warning("⚠️  Playwright not installed, skipping test")
                self.test_results["playwright_scraper"] = {"status": "SKIP", "reason": "Not installed"}
                return
            
            # Run playwright scraper
            result = subprocess.run([
                sys.executable, "playwright_scraper.py", "--posts", "3"
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode == 0:
                logger.info("✅ Playwright scraper completed successfully")
                
                # Check if data was saved
                data_dirs = list(Path("data").glob("posts_*_playwright"))
                if data_dirs:
                    latest_dir = max(data_dirs, key=lambda x: x.stat().st_mtime)
                    logger.info(f"✅ Playwright data saved in: {latest_dir}")
                    
                    json_files = list(latest_dir.glob("*.json"))
                    if json_files:
                        with open(json_files[0], 'r') as f:
                            data = json.load(f)
                        
                        total_posts = len(data)
                        posts_with_content = sum(1 for post in data if post.get('content') and len(post['content']) > 10)
                        success_rate = (posts_with_content / total_posts * 100) if total_posts > 0 else 0
                        
                        logger.info(f"📊 Playwright Success Rate: {success_rate:.1f}%")
                        logger.info(f"📊 Total Posts: {total_posts}")
                        
                        self.test_results["playwright_scraper"] = {
                            "status": "PASS",
                            "success_rate": success_rate,
                            "total_posts": total_posts,
                            "posts_with_content": posts_with_content
                        }
                    else:
                        logger.error("❌ No Playwright output files found")
                        self.test_results["playwright_scraper"] = {"status": "FAIL", "error": "No output files"}
                else:
                    logger.error("❌ No Playwright data directory created")
                    self.test_results["playwright_scraper"] = {"status": "FAIL", "error": "No data directory"}
            else:
                logger.error(f"❌ Playwright scraper failed: {result.stderr}")
                self.test_results["playwright_scraper"] = {"status": "FAIL", "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            logger.error("❌ Playwright scraper timed out")
            self.test_results["playwright_scraper"] = {"status": "FAIL", "error": "Timeout"}
        except Exception as e:
            logger.error(f"❌ Playwright scraper error: {e}")
            self.test_results["playwright_scraper"] = {"status": "FAIL", "error": str(e)}
    
    def test_environment_setup(self):
        """Test environment setup and dependencies"""
        logger.info("🧪 TESTING ENVIRONMENT SETUP")
        logger.info("=" * 50)
        
        try:
            # Test required packages
            required_packages = [
                "selenium", "webdriver_manager", "python-dotenv", 
                "requests", "beautifulsoup4", "pydantic"
            ]
            
            missing_packages = []
            for package in required_packages:
                try:
                    __import__(package.replace("-", "_"))
                    logger.info(f"✅ {package} is installed")
                except ImportError:
                    missing_packages.append(package)
                    logger.error(f"❌ {package} is missing")
            
            # Test environment variables
            email = os.getenv('LINKEDIN_EMAIL')
            password = os.getenv('LINKEDIN_PASSWORD')
            
            if email and password:
                logger.info("✅ LinkedIn credentials found")
                credentials_status = "PASS"
            else:
                logger.error("❌ LinkedIn credentials missing")
                credentials_status = "FAIL"
            
            # Test data directory
            data_dir = Path("data")
            if data_dir.exists():
                logger.info("✅ Data directory exists")
                data_dir_status = "PASS"
            else:
                logger.warning("⚠️  Data directory does not exist")
                data_dir_status = "WARNING"
            
            self.test_results["environment_setup"] = {
                "status": "PASS" if not missing_packages and credentials_status == "PASS" else "FAIL",
                "missing_packages": missing_packages,
                "credentials_status": credentials_status,
                "data_dir_status": data_dir_status
            }
            
        except Exception as e:
            logger.error(f"❌ Environment setup test error: {e}")
            self.test_results["environment_setup"] = {"status": "FAIL", "error": str(e)}
    
    def generate_test_report(self):
        """Generate comprehensive test report"""
        logger.info("📊 GENERATING COMPREHENSIVE TEST REPORT")
        logger.info("=" * 50)
        
        # Calculate overall statistics
        total_tests = len(self.test_results)
        passed_tests = sum(1 for result in self.test_results.values() if result.get("status") == "PASS")
        failed_tests = sum(1 for result in self.test_results.values() if result.get("status") == "FAIL")
        warning_tests = sum(1 for result in self.test_results.values() if result.get("status") in ["WARNING", "SKIP"])
        
        overall_success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
        
        # Generate report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = f"comprehensive_test_report_{timestamp}.json"
        
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "test_duration": time.time() - self.start_time,
            "overall_statistics": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": failed_tests,
                "warning_tests": warning_tests,
                "overall_success_rate": overall_success_rate
            },
            "test_results": self.test_results,
            "production_readiness": {
                "phase_1_complete": self.test_results.get("phase_1", {}).get("status") == "PASS",
                "phase_2_complete": self.test_results.get("phase_2", {}).get("status") == "PASS",
                "phase_3_complete": self.test_results.get("phase_3", {}).get("status") == "PASS",
                "environment_ready": self.test_results.get("environment_setup", {}).get("status") == "PASS",
                "production_ready": overall_success_rate >= 80
            }
        }
        
        # Save report
        with open(report_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        # Print summary
        logger.info(f"\n📊 COMPREHENSIVE TEST SUMMARY")
        logger.info("=" * 50)
        logger.info(f"Total Tests: {total_tests}")
        logger.info(f"Passed: {passed_tests}")
        logger.info(f"Failed: {failed_tests}")
        logger.info(f"Warnings/Skips: {warning_tests}")
        logger.info(f"Overall Success Rate: {overall_success_rate:.1f}%")
        logger.info(f"Production Ready: {'✅ YES' if overall_success_rate >= 80 else '❌ NO'}")
        logger.info(f"Report saved to: {report_file}")
        
        # Print detailed results
        logger.info(f"\n📋 DETAILED RESULTS:")
        logger.info("-" * 30)
        for test_name, result in self.test_results.items():
            status = result.get("status", "UNKNOWN")
            status_icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
            logger.info(f"{status_icon} {test_name}: {status}")
            
            if "success_rate" in result:
                logger.info(f"   Success Rate: {result['success_rate']:.1f}%")
            if "error" in result:
                logger.info(f"   Error: {result['error']}")
        
        return report_file

def main():
    """Run comprehensive test suite"""
    logger.info("🚀 COMPREHENSIVE TEST SUITE")
    logger.info("=" * 70)
    logger.info("Testing all three phases and production readiness")
    
    test_suite = ComprehensiveTestSuite()
    
    try:
        # Run all tests
        test_suite.test_environment_setup()
        test_suite.test_phase_1_dom_investigation()
        test_suite.test_phase_2_enhanced_scraper()
        test_suite.test_phase_3_production_scraper()
        test_suite.test_network_interceptor()
        test_suite.test_playwright_scraper()
        
        # Generate report
        report_file = test_suite.generate_test_report()
        
        logger.info(f"\n🎉 COMPREHENSIVE TEST SUITE COMPLETE!")
        logger.info(f"📄 Detailed report: {report_file}")
        
    except Exception as e:
        logger.error(f"❌ Test suite error: {e}")
        import traceback
        logger.error(traceback.format_exc())

if __name__ == "__main__":
    main() 