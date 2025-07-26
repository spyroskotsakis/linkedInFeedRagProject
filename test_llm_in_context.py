#!/usr/bin/env python3
"""
Test LLM in the same async context as RAG system
"""

import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, '/app')

from rag.components.llm_manager import LLMManager
from rag.components.embedding_manager import EmbeddingManager
from rag.components.retriever import Retriever

async def test_in_rag_context():
    """Test LLM manager in the same context as RAG system."""
    print("Testing LLM manager in RAG context...")
    
    # Create the same components as RAG system
    embedding_config = {
        'model_name': 'all-MiniLM-L6-v2',
        'vector_store_path': '/app/vector_store'
    }
    
    llm_config = {
        'provider': 'ollama',
        'model': 'mistral-nemo:12b',
        'base_url': 'http://host.docker.internal:11434',
        'temperature': 0.1,
        'max_tokens': 2048
    }
    
    retrieval_config = {
        'max_results': 5,
        'similarity_threshold': 0.7
    }
    
    try:
        # Initialize components in the same order as RAG system
        print("Initializing embedding manager...")
        embedding_manager = EmbeddingManager(embedding_config)
        await embedding_manager.initialize()
        
        print("Initializing LLM manager...")
        llm_manager = LLMManager(llm_config)
        await llm_manager.initialize()
        
        print("Initializing retriever...")
        retriever = Retriever(retrieval_config, embedding_manager, llm_manager)
        await retriever.initialize()
        
        print("✅ All components initialized successfully")
        
        # Test LLM manager directly
        print("Testing LLM manager directly...")
        response = await llm_manager.generate_response("Test prompt")
        print(f"✅ Direct LLM response: {response[:100]}...")
        
        # Test RAG response generation
        print("Testing RAG response generation...")
        test_docs = [
            {
                "content": "n8n is a workflow automation tool that allows you to connect different services and automate tasks.",
                "metadata": {"author": "Test Author"}
            }
        ]
        
        rag_response = await llm_manager.generate_rag_response("What is n8n?", test_docs)
        print(f"✅ RAG response: {rag_response[:100]}...")
        
        # Test through retriever (simulating the actual RAG flow)
        print("Testing through retriever...")
        # Note: This will fail because we don't have a collection, but it will test the LLM call
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_in_rag_context())
    print(f"Overall success: {success}")
    sys.exit(0 if success else 1) 