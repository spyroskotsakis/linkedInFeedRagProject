"""
Embedding Manager Component

Handles text embedding generation using sentence-transformers.
"""

import logging
from typing import List, Dict, Any, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

logger = logging.getLogger(__name__)


class EmbeddingManager:
    """Manages text embeddings for the RAG system."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.model_name = config.get("model", "all-MiniLM-L6-v2")
        self.model = None
        self.vector_store = None
        self._initialized = False
    
    async def initialize(self):
        """Initialize the embedding model and vector store."""
        try:
            logger.info(f"Initializing embedding model: {self.model_name}")
            
            # Load the sentence transformer model
            self.model = SentenceTransformer(self.model_name)
            
            # Initialize ChromaDB
            self.vector_store = chromadb.PersistentClient(
                path=self.config.get("vector_store_path", "/app/vector_store"),
                settings=Settings(anonymized_telemetry=False)
            )
            
            self._initialized = True
            logger.info("Embedding manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize embedding manager: {e}")
            raise
    
    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for a single text."""
        if not self._initialized:
            raise RuntimeError("Embedding manager not initialized")
        
        try:
            embedding = self.model.encode(text)
            return embedding.tolist()
        except Exception as e:
            logger.error(f"Failed to generate embedding: {e}")
            raise
    
    def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts."""
        if not self._initialized:
            raise RuntimeError("Embedding manager not initialized")
        
        try:
            embeddings = self.model.encode(texts)
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Failed to generate batch embeddings: {e}")
            raise
    
    def get_collection(self, collection_name: str):
        """Get or create a ChromaDB collection."""
        if not self._initialized:
            raise RuntimeError("Embedding manager not initialized")
        
        try:
            # Try to get existing collection
            collection = self.vector_store.get_collection(collection_name)
        except:
            # Create new collection if it doesn't exist
            collection = self.vector_store.create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"}
            )
        
        return collection
    
    def build_full_text(self, doc):
        meta = doc.get("metadata", {})
        return (
            f"Author: {meta.get('author', '')}\n"
            f"Content: {doc.get('content', '')}\n"
            f"Likes: {meta.get('likes', 0)}\n"
            f"Comments: {meta.get('comments', 0)}\n"
            f"Shares: {meta.get('shares', 0)}\n"
            f"Timestamp: {meta.get('timestamp', '')}\n"
            f"URL: {meta.get('url', '')}"
        )

    async def add_documents(self, collection_name: str, documents: List[Dict[str, Any]]):
        """Add documents to the vector store."""
        if not self._initialized:
            raise RuntimeError("Embedding manager not initialized")
        
        try:
            collection = self.get_collection(collection_name)
            
            # Prepare data for ChromaDB
            texts = [self.build_full_text(doc) for doc in documents]
            metadatas = [doc.get("metadata", {}) for doc in documents]
            ids = [doc.get("id", f"doc_{i}") for i, doc in enumerate(documents)]
            
            # Generate embeddings
            embeddings = self.generate_embeddings_batch(texts)
            
            # Add to collection
            collection.add(
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas,
                ids=ids
            )
            
            logger.info(f"Added {len(documents)} documents to collection: {collection_name}")
            
        except Exception as e:
            logger.error(f"Failed to add documents: {e}")
            raise
    
    async def search_similar(self, collection_name: str, query: str, n_results: int = 5) -> List[Dict[str, Any]]:
        """Search for similar documents."""
        if not self._initialized:
            raise RuntimeError("Embedding manager not initialized")
        
        try:
            collection = self.get_collection(collection_name)
            
            # Generate query embedding
            query_embedding = self.generate_embedding(query)
            
            # Search
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results
            )
            
            # Format results
            formatted_results = []
            for i in range(len(results["documents"][0])):
                formatted_results.append({
                    "content": results["documents"][0][i],
                    "metadata": results["metadatas"][0][i],
                    "distance": results["distances"][0][i],
                    "id": results["ids"][0][i]
                })
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Failed to search similar documents: {e}")
            raise
    
    def get_stats(self) -> Dict[str, Any]:
        """Get embedding manager statistics."""
        return {
            "model": self.model_name,
            "initialized": self._initialized,
            "vector_store_path": self.config.get("vector_store_path", "/app/vector_store")
        } 