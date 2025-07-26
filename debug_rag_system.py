#!/usr/bin/env python3
"""
Debug RAG System - Comprehensive Testing Script

This script tests the RAG system step by step to identify where issues occur.
It tests data loading, indexing, and querying separately.
"""

import asyncio
import httpx
import json
import os
from pathlib import Path
import polars as pl
from typing import Dict, Any, List

# Configuration
RAG_API_URL = "http://localhost:8000"  # RAG API is using host network mode
DATA_DIR = Path("data")
TEST_QUERY = "find me posts about openAI"

class RAGDebugger:
    """Debug class for testing RAG system components."""
    
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.client = httpx.AsyncClient(timeout=30.0)
    
    async def test_api_health(self) -> Dict[str, Any]:
        """Test RAG API health endpoint."""
        print("🔍 Testing RAG API Health...")
        try:
            response = await self.client.get(f"{self.api_url}/health")
            result = response.json()
            print(f"✅ Health Check: {result}")
            return result
        except Exception as e:
            print(f"❌ Health Check Failed: {e}")
            return {"error": str(e)}
    
    async def test_api_ready(self) -> Dict[str, Any]:
        """Test RAG API ready endpoint."""
        print("🔍 Testing RAG API Ready...")
        try:
            response = await self.client.get(f"{self.api_url}/ready")
            result = response.json()
            print(f"✅ Ready Check: {result}")
            return result
        except Exception as e:
            print(f"❌ Ready Check Failed: {e}")
            return {"error": str(e)}
    
    def test_data_loading(self) -> Dict[str, Any]:
        """Test data loading from files."""
        print("🔍 Testing Data Loading...")
        
        # Find data files
        export_dirs = [d for d in DATA_DIR.iterdir() if d.is_dir() and d.name.startswith("posts_")]
        
        if not export_dirs:
            print("❌ No data directories found!")
            return {"error": "No data directories found"}
        
        selected_dir = export_dirs[0]  # Use first available
        print(f"📁 Using data directory: {selected_dir}")
        
        # Check for JSON files
        json_files = list(selected_dir.glob("linkedin_feed_*.json"))
        if not json_files:
            print("❌ No JSON files found!")
            return {"error": "No JSON files found"}
        
        json_path = json_files[0]
        print(f"📄 Using JSON file: {json_path}")
        
        # Load and analyze data
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"✅ Loaded {len(data)} posts from JSON")
            
            # Analyze content for test query
            content_samples = []
            openai_mentions = []
            
            for i, post in enumerate(data[:10]):  # Check first 10 posts
                content = post.get('content', '').lower()
                content_samples.append(content[:100] + "..." if len(content) > 100 else content)
                
                if 'openai' in content or 'open ai' in content:
                    openai_mentions.append({
                        'index': i,
                        'content': content[:200] + "..." if len(content) > 200 else content
                    })
            
            print(f"📊 Content samples (first 10 posts):")
            for i, sample in enumerate(content_samples):
                print(f"  {i+1}. {sample}")
            
            print(f"🎯 Found {len(openai_mentions)} posts mentioning OpenAI:")
            for mention in openai_mentions:
                print(f"  Post {mention['index']+1}: {mention['content']}")
            
            return {
                "success": True,
                "total_posts": len(data),
                "openai_mentions": len(openai_mentions),
                "content_samples": content_samples,
                "openai_posts": openai_mentions
            }
            
        except Exception as e:
            print(f"❌ Data loading failed: {e}")
            return {"error": str(e)}
    
    async def test_data_indexing(self, data_path: str) -> Dict[str, Any]:
        """Test data indexing in RAG system."""
        print("🔍 Testing Data Indexing...")
        try:
            payload = {
                "data_path": data_path,
                "collection_name": "test_collection"
            }
            
            print(f"📤 Sending indexing request: {payload}")
            response = await self.client.post(f"{self.api_url}/index", json=payload)
            result = response.json()
            
            print(f"✅ Indexing Response: {result}")
            return result
            
        except Exception as e:
            print(f"❌ Indexing failed: {e}")
            return {"error": str(e)}
    
    async def test_rag_query(self, query: str, collection_name: str = "test_collection") -> Dict[str, Any]:
        """Test RAG query functionality."""
        print(f"🔍 Testing RAG Query: '{query}'")
        try:
            payload = {
                "query": query,
                "collection_name": collection_name,
                "max_results": 5
            }
            
            print(f"📤 Sending query request: {payload}")
            response = await self.client.post(f"{self.api_url}/query", json=payload)
            result = response.json()
            
            print(f"✅ Query Response: {result}")
            return result
            
        except Exception as e:
            print(f"❌ Query failed: {e}")
            return {"error": str(e)}
    
    async def test_collections(self) -> Dict[str, Any]:
        """Test collections endpoint."""
        print("🔍 Testing Collections...")
        try:
            response = await self.client.get(f"{self.api_url}/collections")
            result = response.json()
            
            print(f"✅ Collections: {result}")
            return result
            
        except Exception as e:
            print(f"❌ Collections failed: {e}")
            return {"error": str(e)}
    
    async def test_collection_stats(self, collection_name: str) -> Dict[str, Any]:
        """Test collection statistics."""
        print(f"🔍 Testing Collection Stats for '{collection_name}'...")
        try:
            response = await self.client.get(f"{self.api_url}/collections/{collection_name}/stats")
            result = response.json()
            
            print(f"✅ Collection Stats: {result}")
            return result
            
        except Exception as e:
            print(f"❌ Collection stats failed: {e}")
            return {"error": str(e)}
    
    async def run_comprehensive_test(self):
        """Run comprehensive RAG system test."""
        print("🚀 Starting Comprehensive RAG System Debug Test")
        print("=" * 60)
        
        # Test 1: API Health
        print("\n1️⃣ Testing API Health...")
        health_result = await self.test_api_health()
        
        # Test 2: API Ready
        print("\n2️⃣ Testing API Ready...")
        ready_result = await self.test_api_ready()
        
        # Test 3: Data Loading
        print("\n3️⃣ Testing Data Loading...")
        data_result = self.test_data_loading()
        
        if data_result.get("error"):
            print("❌ Data loading failed, stopping tests")
            return
        
        # Test 4: Collections
        print("\n4️⃣ Testing Collections...")
        collections_result = await self.test_collections()
        
        # Test 5: Data Indexing
        print("\n5️⃣ Testing Data Indexing...")
        # Find the data path
        export_dirs = [d for d in DATA_DIR.iterdir() if d.is_dir() and d.name.startswith("posts_")]
        if export_dirs:
            data_path = str(export_dirs[0])
            indexing_result = await self.test_data_indexing(data_path)
        else:
            print("❌ No data directory found for indexing")
            indexing_result = {"error": "No data directory"}
        
        # Test 6: Collection Stats
        print("\n6️⃣ Testing Collection Stats...")
        stats_result = await self.test_collection_stats("test_collection")
        
        # Test 7: RAG Query
        print("\n7️⃣ Testing RAG Query...")
        query_result = await self.test_rag_query(TEST_QUERY, "test_collection")
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        tests = [
            ("API Health", health_result),
            ("API Ready", ready_result),
            ("Data Loading", data_result),
            ("Collections", collections_result),
            ("Data Indexing", indexing_result),
            ("Collection Stats", stats_result),
            ("RAG Query", query_result)
        ]
        
        for test_name, result in tests:
            if result.get("error"):
                print(f"❌ {test_name}: FAILED - {result['error']}")
            else:
                print(f"✅ {test_name}: PASSED")
        
        # Specific analysis for query results
        if not query_result.get("error"):
            print(f"\n🔍 Query Analysis for '{TEST_QUERY}':")
            if "answer" in query_result:
                print(f"📝 Answer: {query_result['answer']}")
            if "sources" in query_result:
                print(f"📚 Sources: {len(query_result['sources'])} found")
                for i, source in enumerate(query_result['sources'][:3]):
                    print(f"  Source {i+1}: {source.get('content', '')[:100]}...")
            else:
                print("⚠️ No sources found in response")
        
        await self.client.aclose()

async def main():
    """Main function."""
    debugger = RAGDebugger(RAG_API_URL)
    await debugger.run_comprehensive_test()

if __name__ == "__main__":
    asyncio.run(main()) 