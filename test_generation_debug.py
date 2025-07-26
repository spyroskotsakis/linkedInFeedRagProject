#!/usr/bin/env python3
"""
Debug generation request specifically
"""

import asyncio
import httpx
import json

async def test_generation_request():
    """Test the exact generation request that's failing."""
    base_url = "http://host.docker.internal:11434"
    
    print("Testing health check...")
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{base_url}/api/tags")
            print(f"Health check status: {response.status_code}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
    
    print("Testing generation request...")
    try:
        payload = {
            "model": "mistral-nemo:12b",
            "prompt": "Test prompt",
            "stream": False,
            "options": {
                "temperature": 0.1,
                "num_predict": 2048
            }
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{base_url}/api/generate",
                json=payload
            )
            
            print(f"Generation status: {response.status_code}")
            if response.status_code == 200:
                result = response.json()
                print(f"Response: {result.get('response', 'No response')[:100]}...")
                return True
            else:
                print(f"Error response: {response.text}")
                return False
                
    except Exception as e:
        print(f"Generation failed: {e}")
        print(f"Error type: {type(e)}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_generation_request())
    print(f"Success: {success}") 