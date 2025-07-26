#!/usr/bin/env python3
"""
Ollama Connectivity Test Script

Tests Ollama connectivity from within Docker containers to ensure
the RAG system can reliably connect to Ollama on the host.
"""

import asyncio
import httpx
import json
import logging
import sys
import time
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class OllamaTestResult:
    """Result of an Ollama connectivity test."""
    test_name: str
    success: bool
    error: Optional[str] = None
    response_time: Optional[float] = None
    details: Optional[Dict[str, Any]] = None


class OllamaConnectivityTester:
    """Test Ollama connectivity from Docker containers."""
    
    def __init__(self, base_url: str = "http://host.docker.internal:11434"):
        self.base_url = base_url
        self.timeout = 30.0
        self.results: List[OllamaTestResult] = []
    
    async def test_ollama_health(self) -> OllamaTestResult:
        """Test basic Ollama health endpoint."""
        start_time = time.time()
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    data = response.json()
                    models = data.get("models", [])
                    model_names = [model.get("name", "") for model in models]
                    
                    return OllamaTestResult(
                        test_name="Ollama Health Check",
                        success=True,
                        response_time=response_time,
                        details={
                            "status_code": response.status_code,
                            "available_models": model_names,
                            "total_models": len(models)
                        }
                    )
                else:
                    return OllamaTestResult(
                        test_name="Ollama Health Check",
                        success=False,
                        response_time=response_time,
                        error=f"HTTP {response.status_code}: {response.text}"
                    )
                    
        except Exception as e:
            response_time = time.time() - start_time
            return OllamaTestResult(
                test_name="Ollama Health Check",
                success=False,
                response_time=response_time,
                error=str(e)
            )
    
    async def test_model_availability(self, model_name: str = "llama3.1:8b") -> OllamaTestResult:
        """Test if a specific model is available."""
        start_time = time.time()
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    data = response.json()
                    models = data.get("models", [])
                    model_names = [model.get("name", "") for model in models]
                    
                    if model_name in model_names:
                        # Find the specific model details
                        model_details = next(
                            (model for model in models if model.get("name") == model_name),
                            None
                        )
                        
                        return OllamaTestResult(
                            test_name=f"Model Availability: {model_name}",
                            success=True,
                            response_time=response_time,
                            details={
                                "model_found": True,
                                "model_details": model_details
                            }
                        )
                    else:
                        return OllamaTestResult(
                            test_name=f"Model Availability: {model_name}",
                            success=False,
                            response_time=response_time,
                            error=f"Model '{model_name}' not found. Available models: {model_names}",
                            details={
                                "model_found": False,
                                "available_models": model_names
                            }
                        )
                else:
                    return OllamaTestResult(
                        test_name=f"Model Availability: {model_name}",
                        success=False,
                        response_time=response_time,
                        error=f"HTTP {response.status_code}: {response.text}"
                    )
                    
        except Exception as e:
            response_time = time.time() - start_time
            return OllamaTestResult(
                test_name=f"Model Availability: {model_name}",
                success=False,
                response_time=response_time,
                error=str(e)
            )
    
    async def test_model_generation(self, model_name: str = "llama3.1:8b") -> OllamaTestResult:
        """Test if a model can generate responses."""
        start_time = time.time()
        try:
            payload = {
                "model": model_name,
                "prompt": "Hello, this is a test. Please respond with 'Test successful' if you can see this message.",
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 50
                }
            }
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload
                )
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    data = response.json()
                    generated_text = data.get("response", "")
                    
                    return OllamaTestResult(
                        test_name=f"Model Generation: {model_name}",
                        success=True,
                        response_time=response_time,
                        details={
                            "generated_text": generated_text,
                            "response_length": len(generated_text),
                            "model_used": model_name
                        }
                    )
                else:
                    return OllamaTestResult(
                        test_name=f"Model Generation: {model_name}",
                        success=False,
                        response_time=response_time,
                        error=f"HTTP {response.status_code}: {response.text}"
                    )
                    
        except Exception as e:
            response_time = time.time() - start_time
            return OllamaTestResult(
                test_name=f"Model Generation: {model_name}",
                success=False,
                response_time=response_time,
                error=str(e)
            )
    
    async def test_general_knowledge_generation(self, model_name: str = "llama3.1:8b") -> OllamaTestResult:
        """Test if the LLM can answer a general knowledge question."""
        start_time = time.time()
        try:
            payload = {
                "model": model_name,
                "prompt": "What is the capital of France?",
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 20
                }
            }
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload
                )
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    data = response.json()
                    generated_text = data.get("response", "")
                    
                    # Check if the answer contains 'Paris'
                    success = "paris" in generated_text.lower()
                    
                    return OllamaTestResult(
                        test_name=f"General Knowledge Generation: {model_name}",
                        success=success,
                        response_time=response_time,
                        details={
                            "generated_text": generated_text,
                            "response_length": len(generated_text),
                            "model_used": model_name
                        },
                        error=None if success else f"Expected 'Paris' in response, got: {generated_text}"
                    )
                else:
                    return OllamaTestResult(
                        test_name=f"General Knowledge Generation: {model_name}",
                        success=False,
                        response_time=response_time,
                        error=f"HTTP {response.status_code}: {response.text}"
                    )
        except Exception as e:
            response_time = time.time() - start_time
            return OllamaTestResult(
                test_name=f"General Knowledge Generation: {model_name}",
                success=False,
                response_time=response_time,
                error=str(e)
            )
    
    async def test_network_connectivity(self) -> OllamaTestResult:
        """Test basic network connectivity to Ollama host."""
        start_time = time.time()
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{self.base_url}/api/tags")
                response_time = time.time() - start_time
                
                return OllamaTestResult(
                    test_name="Network Connectivity",
                    success=response.status_code == 200,
                    response_time=response_time,
                    details={
                        "status_code": response.status_code,
                        "base_url": self.base_url
                    }
                )
                
        except Exception as e:
            response_time = time.time() - start_time
            return OllamaTestResult(
                test_name="Network Connectivity",
                success=False,
                response_time=response_time,
                error=str(e)
            )
    
    async def test_rag_integration(self) -> OllamaTestResult:
        """Test RAG-style prompt generation."""
        start_time = time.time()
        try:
            # Simulate a RAG-style prompt
            context = "This is a test context about AI and machine learning."
            query = "What is artificial intelligence?"
            
            full_prompt = f"""Context: {context}

Question: {query}

Please provide a helpful answer based on the context provided. If the context doesn't contain relevant information, say so."""
            
            payload = {
                "model": "llama3.1:8b",
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": 100
                }
            }
            
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload
                )
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    data = response.json()
                    generated_text = data.get("response", "")
                    
                    return OllamaTestResult(
                        test_name="RAG Integration Test",
                        success=True,
                        response_time=response_time,
                        details={
                            "generated_text": generated_text,
                            "response_length": len(generated_text),
                            "prompt_length": len(full_prompt)
                        }
                    )
                else:
                    return OllamaTestResult(
                        test_name="RAG Integration Test",
                        success=False,
                        response_time=response_time,
                        error=f"HTTP {response.status_code}: {response.text}"
                    )
                    
        except Exception as e:
            response_time = time.time() - start_time
            return OllamaTestResult(
                test_name="RAG Integration Test",
                success=False,
                response_time=response_time,
                error=str(e)
            )
    
    async def run_all_tests(self) -> List[OllamaTestResult]:
        """Run all connectivity tests."""
        logger.info("🚀 Starting Ollama connectivity tests...")
        logger.info(f"📡 Testing connection to: {self.base_url}")
        
        tests = [
            self.test_network_connectivity(),
            self.test_ollama_health(),
            self.test_model_availability(),
            self.test_model_generation(),
            self.test_general_knowledge_generation(),
            self.test_rag_integration()
        ]
        
        results = await asyncio.gather(*tests, return_exceptions=True)
        
        # Handle any exceptions
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                results[i] = OllamaTestResult(
                    test_name=f"Test {i+1}",
                    success=False,
                    error=str(result)
                )
        
        self.results = results
        return results
    
    def print_results(self):
        """Print test results in a formatted way."""
        print("\n" + "="*80)
        print("🔍 OLLAMA CONNECTIVITY TEST RESULTS")
        print("="*80)
        
        total_tests = len(self.results)
        passed_tests = sum(1 for result in self.results if result.success)
        failed_tests = total_tests - passed_tests
        
        print(f"\n📊 Summary:")
        print(f"   Total Tests: {total_tests}")
        print(f"   ✅ Passed: {passed_tests}")
        print(f"   ❌ Failed: {failed_tests}")
        print(f"   Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        print(f"\n🔧 Configuration:")
        print(f"   Base URL: {self.base_url}")
        print(f"   Timeout: {self.timeout}s")
        
        print(f"\n📋 Detailed Results:")
        print("-" * 80)
        
        for result in self.results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            print(f"\n{status} {result.test_name}")
            
            if result.response_time:
                print(f"   ⏱️  Response Time: {result.response_time:.3f}s")
            
            if result.error:
                print(f"   🚨 Error: {result.error}")
            
            if result.details:
                print(f"   📝 Details:")
                for key, value in result.details.items():
                    if isinstance(value, str) and len(value) > 100:
                        print(f"      {key}: {value[:100]}...")
                    else:
                        print(f"      {key}: {value}")
        
        print("\n" + "="*80)
        
        if failed_tests == 0:
            print("🎉 All tests passed! Ollama connectivity is working correctly.")
        else:
            print("⚠️  Some tests failed. Please check the error messages above.")
        
        print("="*80 + "\n")
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate a detailed test report."""
        total_tests = len(self.results)
        passed_tests = sum(1 for result in self.results if result.success)
        
        return {
            "summary": {
                "total_tests": total_tests,
                "passed_tests": passed_tests,
                "failed_tests": total_tests - passed_tests,
                "success_rate": (passed_tests/total_tests)*100 if total_tests > 0 else 0
            },
            "configuration": {
                "base_url": self.base_url,
                "timeout": self.timeout
            },
            "results": [
                {
                    "test_name": result.test_name,
                    "success": result.success,
                    "error": result.error,
                    "response_time": result.response_time,
                    "details": result.details
                }
                for result in self.results
            ],
            "timestamp": time.time(),
            "recommendations": self._generate_recommendations()
        }
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on test results."""
        recommendations = []
        
        # Check for network connectivity issues
        network_test = next((r for r in self.results if "Network Connectivity" in r.test_name), None)
        if network_test and not network_test.success:
            recommendations.append("🔧 Check Docker network configuration - ensure host.docker.internal is accessible")
            recommendations.append("🔧 Verify Ollama is running on the host machine")
            recommendations.append("🔧 Check firewall settings that might block port 11434")
        
        # Check for model availability issues
        model_test = next((r for r in self.results if "Model Availability" in r.test_name), None)
        if model_test and not model_test.success:
            recommendations.append("📦 Pull the required model: ollama pull llama3.1:8b")
            recommendations.append("📦 Check available models: ollama list")
        
        # Check for generation issues
        generation_test = next((r for r in self.results if "Model Generation" in r.test_name), None)
        if generation_test and not generation_test.success:
            recommendations.append("⚡ Check if the model is fully loaded and ready")
            recommendations.append("⚡ Verify sufficient system resources (RAM, CPU)")
        
        if not recommendations:
            recommendations.append("✅ All systems operational - no recommendations needed")
        
        return recommendations


async def main():
    """Main test function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Test Ollama connectivity from Docker")
    parser.add_argument(
        "--base-url",
        default="http://host.docker.internal:11434",
        help="Ollama base URL (default: http://host.docker.internal:11434)"
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=30.0,
        help="Request timeout in seconds (default: 30.0)"
    )
    parser.add_argument(
        "--model",
        default="mistral-nemo:12b",
        help="Model to test (default: mistral-nemo:12b)"
    )
    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate detailed JSON report"
    )
    
    args = parser.parse_args()
    
    # Create tester
    tester = OllamaConnectivityTester(base_url=args.base_url)
    tester.timeout = args.timeout
    
    # Run tests
    results = await tester.run_all_tests()
    
    # Print results
    tester.print_results()
    
    # Generate report if requested
    if args.report:
        report = tester.generate_report()
        report_file = f"ollama_connectivity_report_{int(time.time())}.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"📄 Detailed report saved to: {report_file}")
    
    # Exit with appropriate code
    failed_tests = sum(1 for result in results if not result.success)
    sys.exit(1 if failed_tests > 0 else 0)


if __name__ == "__main__":
    asyncio.run(main()) 