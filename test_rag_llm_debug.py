#!/usr/bin/env python3
"""
Debug RAG LLM connection issue
"""

import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, '/app')

from rag.components.llm_manager import LLMManager
from rag.components.embedding_manager import EmbeddingManager
from rag.components.retriever import Retriever

async def test_rag_llm_connection():
    """Test LLM connection in the exact same context as RAG system."""
    print("Testing LLM connection in RAG context...")
    
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
        'max_results': 10,
        'similarity_threshold': 0.5,
        'min_docs_for_llm': 3
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
        
        # Test LLM manager directly with a simple prompt
        print("Testing LLM manager with simple prompt...")
        response = await llm_manager.generate_response("Hello, this is a test.")
        print(f"✅ LLM response: {response[:100]}...")
        
        # Test LLM manager with context (like in RAG)
        print("Testing LLM manager with context...")
        test_context = "This is a test context about n8n workflow automation."
        response_with_context = await llm_manager.generate_response(
            "What is n8n?", 
            context=test_context
        )
        print(f"✅ LLM response with context: {response_with_context[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_rag_llm_connection())
    print(f"Overall success: {success}")
    sys.exit(0 if success else 1) 