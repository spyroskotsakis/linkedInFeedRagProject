#!/usr/bin/env python3
"""
Debug httpx connection issue
"""

import asyncio
import httpx
import logging

logging.basicConfig(level=logging.DEBUG)

async def test_httpx_connection():
    """Test httpx connection to Ollama."""
    url = "http://host.docker.internal:11434/api/tags"
    
    print(f"Testing connection to: {url}")
    
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            print("Making request...")
            response = await client.get(url)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            return True
    except Exception as e:
        print(f"Error: {e}")
        print(f"Error type: {type(e)}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_httpx_connection())
    print(f"Success: {success}") 