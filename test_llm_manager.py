#!/usr/bin/env python3
"""
Test LLM Manager directly
"""

import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, '/app')

from rag.components.llm_manager import LLMManager

async def test_llm_manager():
    """Test LLM manager directly."""
    print("Testing LLM Manager...")
    
    # Create LLM manager with same config as RAG API
    config = {
        'provider': 'ollama',
        'model': 'mistral-nemo:12b',
        'base_url': 'http://host.docker.internal:11434',
        'temperature': 0.1,
        'max_tokens': 2048
    }
    
    manager = LLMManager(config)
    
    try:
        print("Initializing LLM manager...")
        await manager.initialize()
        print("✅ LLM Manager initialized successfully")
        
        print("Testing simple response generation...")
        response = await manager.generate_response("Hello, this is a test.")
        print(f"✅ Response: {response[:100]}...")
        
        print("Testing RAG response generation...")
        test_docs = [
            {
                "content": "n8n is a workflow automation tool that allows you to connect different services and automate tasks.",
                "metadata": {"author": "Test Author"}
            }
        ]
        
        rag_response = await manager.generate_rag_response("What is n8n?", test_docs)
        print(f"✅ RAG Response: {rag_response[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_llm_manager())
    print(f"Overall success: {success}")
    sys.exit(0 if success else 1) 