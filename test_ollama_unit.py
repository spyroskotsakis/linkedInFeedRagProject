#!/usr/bin/env python3
"""
Ollama Connectivity Unit Test

Simple unit test to verify Ollama connectivity from Docker containers.
Can be run regularly to monitor system health.
"""

import asyncio
import httpx
import json
import sys
import time
from typing import Dict, Any


class OllamaUnitTest:
    """Simple unit test for Ollama connectivity."""
    
    def __init__(self, base_url: str = "http://host.docker.internal:11434"):
        self.base_url = base_url
        self.timeout = 10.0
    
    async def test_connectivity(self) -> Dict[str, Any]:
        """Run basic connectivity test."""
        start_time = time.time()
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                # Test 1: Basic connectivity
                response = await client.get(f"{self.base_url}/api/tags")
                response_time = time.time() - start_time
                
                if response.status_code != 200:
                    return {
                        "success": False,
                        "error": f"HTTP {response.status_code}",
                        "response_time": response_time,
                        "details": "Failed to connect to Ollama"
                    }
                
                # Test 2: Check model availability
                data = response.json()
                models = data.get("models", [])
                model_names = [model.get("name", "") for model in models]
                
                if "mistral-nemo:12b" not in model_names:
                    return {
                        "success": False,
                        "error": "Required model not found",
                        "response_time": response_time,
                        "details": f"Available models: {model_names}"
                    }
                
                # Test 3: Simple generation test
                payload = {
                    "model": "mistral-nemo:12b",
                    "prompt": "Test",
                    "stream": False,
                    "options": {
                        "temperature": 0.1,
                        "num_predict": 10
                    }
                }
                
                gen_response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload
                )
                
                if gen_response.status_code != 200:
                    return {
                        "success": False,
                        "error": f"Generation failed: HTTP {gen_response.status_code}",
                        "response_time": response_time,
                        "details": "Model cannot generate responses"
                    }
                
                return {
                    "success": True,
                    "response_time": response_time,
                    "details": {
                        "available_models": len(models),
                        "required_model_found": True,
                        "generation_working": True
                    }
                }
                
        except Exception as e:
            response_time = time.time() - start_time
            return {
                "success": False,
                "error": str(e),
                "response_time": response_time,
                "details": "Connection failed"
            }
    
    def print_result(self, result: Dict[str, Any]):
        """Print test result in a simple format."""
        if result["success"]:
            print(f"✅ Ollama connectivity test PASSED ({result['response_time']:.3f}s)")
            print(f"   📊 Available models: {result['details']['available_models']}")
            print(f"   🤖 Required model: Found")
            print(f"   ⚡ Generation: Working")
        else:
            print(f"❌ Ollama connectivity test FAILED ({result['response_time']:.3f}s)")
            print(f"   🚨 Error: {result['error']}")
            if 'details' in result and isinstance(result['details'], str):
                print(f"   📝 Details: {result['details']}")


async def main():
    """Main test function."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Ollama connectivity unit test")
    parser.add_argument(
        "--base-url",
        default="http://host.docker.internal:11434",
        help="Ollama base URL"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Quiet mode - only show pass/fail"
    )
    
    args = parser.parse_args()
    
    # Run test
    tester = OllamaUnitTest(base_url=args.base_url)
    result = await tester.test_connectivity()
    
    if not args.quiet:
        tester.print_result(result)
    else:
        # Quiet mode - just print pass/fail
        if result["success"]:
            print("PASS")
        else:
            print("FAIL")
    
    # Exit with appropriate code
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    asyncio.run(main()) 