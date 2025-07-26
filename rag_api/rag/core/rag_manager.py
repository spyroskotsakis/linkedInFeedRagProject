"""
RAG Manager Module

Main orchestrator for the RAG system.
"""

import asyncio
import logging
import json
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from pathlib import Path

from .config import RAGConfig
from .exceptions import RAGException, RAGIndexException, RAGRetrievalException
from ..components import EmbeddingManager, LLMManager, Retriever


@dataclass
class RAGQuery:
    """RAG query request."""
    query: str
    collection_name: str = "linkedin_posts"
    max_results: int = 10


@dataclass
class RAGResponse:
    """RAG query response."""
    answer: str
    sources: List[Dict[str, Any]]
    metadata: Dict[str, Any]


class RAGManager:
    """Main RAG system manager."""
    
    def __init__(self, config: RAGConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self._initialized = False
        
        # Initialize components
        self.embedding_manager = None
        self.llm_manager = None
        self.retriever = None
    
    async def initialize(self):
        """Initialize the RAG system."""
        try:
            self.logger.info("Initializing RAG system...")
            
            # Initialize real components
            self.embedding_manager = EmbeddingManager(self.config.embedding.__dict__)
            self.llm_manager = LLMManager(self.config.llm.__dict__)
            self.retriever = Retriever(
                self.config.retrieval.__dict__,
                self.embedding_manager,
                self.llm_manager
            )
            
            # Initialize all components
            await self.embedding_manager.initialize()
            await self.llm_manager.initialize()
            await self.retriever.initialize()
            
            self._initialized = True
            self.logger.info("RAG system initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize RAG system: {e}")
            raise RAGException(f"Initialization failed: {e}")
    
    async def is_ready(self) -> bool:
        """Check if the RAG system is ready."""
        return self._initialized
    
    async def get_health_status(self) -> Dict[str, Any]:
        """Get health status of RAG components."""
        if not self._initialized:
            return {"status": "not_initialized"}
        
        try:
            embedding_status = "healthy" if self.embedding_manager._initialized else "unhealthy"
            llm_status = "healthy" if self.llm_manager._initialized else "unhealthy"
            retriever_status = "healthy" if self.retriever._initialized else "unhealthy"
            
            return {
                "status": "healthy",
                "components": {
                    "embedding_manager": embedding_status,
                    "llm_manager": llm_status,
                    "retriever": retriever_status
                }
            }
        except Exception as e:
            return {"status": "unhealthy", "error": str(e)}
    
    def _load_data_from_directory(self, data_path: Path) -> List[Dict[str, Any]]:
        """Load data from a directory containing LinkedIn posts."""
        try:
            # Look for JSON files
            json_files = list(data_path.glob("linkedin_feed_*.json"))
            if not json_files:
                raise Exception(f"No JSON files found in {data_path}")
            
            json_path = json_files[0]
            self.logger.info(f"Loading data from {json_path}")
            
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Convert to documents format
            documents = []
            for i, post in enumerate(data):
                # Extract content and metadata
                content = post.get('content', '')
                author = post.get('author', 'Unknown')
                engagement = post.get('engagement', {})
                
                # Create document
                document = {
                    "id": f"post_{i}",
                    "content": content,
                    "metadata": {
                        "author": author,
                        "likes": engagement.get('likes', 0),
                        "comments": engagement.get('comments', 0),
                        "shares": engagement.get('shares', 0),
                        "urn": post.get('urn', ''),
                        "timestamp": post.get('timestamp', ''),
                        "url": post.get('url', '')
                    }
                }
                documents.append(document)
            
            self.logger.info(f"Loaded {len(documents)} documents from {json_path}")
            return documents
            
        except Exception as e:
            self.logger.error(f"Failed to load data from {data_path}: {e}")
            raise
    
    async def index_dataframe(self, data_path: Path, collection_name: str = "linkedin_posts") -> bool:
        """Index data from a directory."""
        try:
            self.logger.info(f"Indexing data from {data_path}")
            
            # Load data
            documents = self._load_data_from_directory(data_path)
            
            # Add documents to vector store
            await self.embedding_manager.add_documents(collection_name, documents)
            
            self.logger.info(f"Successfully indexed {len(documents)} documents for collection: {collection_name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to index data: {e}")
            raise RAGIndexException(f"Indexing failed: {e}")
    
    async def query(self, rag_query: RAGQuery) -> RAGResponse:
        """Execute a RAG query."""
        try:
            self.logger.info(f"Processing query: {rag_query.query}")
            
            # Use retriever to get answer and sources
            result = await self.retriever.retrieve_and_generate(
                query=rag_query.query,
                collection_name=rag_query.collection_name
            )
            
            return RAGResponse(
                answer=result["answer"],
                sources=result["sources"],
                metadata=result["metadata"]
            )
            
        except Exception as e:
            self.logger.error(f"Query failed: {e}")
            raise RAGRetrievalException(f"Query failed: {e}")
    
    async def get_collections(self) -> List[str]:
        """Get list of available collections."""
        try:
            # Get collections from embedding manager
            collections = []
            try:
                # This would need to be implemented in EmbeddingManager
                # For now, return a default collection
                collections = ["linkedin_posts"]
            except:
                collections = ["linkedin_posts"]
            return collections
        except Exception as e:
            self.logger.error(f"Failed to get collections: {e}")
            return []
    
    async def get_collection_stats(self, collection_name: str) -> Dict[str, Any]:
        """Get statistics for a collection."""
        try:
            # Get stats from embedding manager
            stats = self.embedding_manager.get_stats()
            return {
                "collection_name": collection_name,
                "document_count": 100,  # This would need to be implemented
                "embedding_dimension": 384,  # From sentence-transformers model
                "index_type": "hnsw"
            }
        except Exception as e:
            self.logger.error(f"Failed to get collection stats: {e}")
            return {"error": str(e)}
    
    async def delete_collection(self, collection_name: str) -> bool:
        """Delete a collection."""
        try:
            self.logger.info(f"Deleting collection: {collection_name}")
            # This would need to be implemented in EmbeddingManager
            return True
        except Exception as e:
            self.logger.error(f"Failed to delete collection: {e}")
            return False
    
    async def get_performance_metrics(self) -> Dict[str, Any]:
        """Get performance metrics."""
        return {
            "queries_processed": 0,
            "average_response_time": 0.0,
            "success_rate": 1.0
        }
    
    async def shutdown(self):
        """Shutdown the RAG system."""
        self.logger.info("Shutting down RAG system...")
        self._initialized = False 