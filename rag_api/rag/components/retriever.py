"""
Retriever Component

Coordinates retrieval and generation for RAG operations.
"""

import logging
from typing import Dict, Any, List, Optional
from .embedding_manager import EmbeddingManager
from .llm_manager import LLMManager

logger = logging.getLogger(__name__)


class Retriever:
    """Coordinates RAG retrieval and generation."""
    
    def __init__(self, config: Dict[str, Any], embedding_manager: EmbeddingManager, llm_manager: LLMManager):
        self.config = config
        self.embedding_manager = embedding_manager
        self.llm_manager = llm_manager
        self.max_results = config.get("max_results", 10)  # Increased from 5 to 10
        self.similarity_threshold = config.get("similarity_threshold", 0.5)  # Lowered from 0.7 to 0.5
        self.min_docs_for_llm = config.get("min_docs_for_llm", 3)  # Minimum docs to send to LLM
        self._initialized = False
    
    async def initialize(self):
        """Initialize the retriever."""
        try:
            logger.info("Initializing retriever...")
            
            # Ensure embedding and LLM managers are initialized
            if not self.embedding_manager._initialized:
                await self.embedding_manager.initialize()
            
            if not self.llm_manager._initialized:
                await self.llm_manager.initialize()
            
            self._initialized = True
            logger.info("Retriever initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize retriever: {e}")
            raise
    
    def build_context(self, doc, i):
        meta = doc.get("metadata", {})
        return (
            f"Document {i}:\n"
            f"Author: {meta.get('author', 'Unknown')}\n"
            f"Content: {doc.get('content', '')}\n"
            f"Likes: {meta.get('likes', 0)}\n"
            f"Comments: {meta.get('comments', 0)}\n"
            f"Shares: {meta.get('shares', 0)}\n"
            f"Timestamp: {meta.get('timestamp', '')}\n"
            f"URL: {meta.get('url', '')}"
        )

    async def retrieve_and_generate(self, query: str, collection_name: str) -> Dict[str, Any]:
        """Retrieve relevant documents and generate a response."""
        if not self._initialized:
            raise RuntimeError("Retriever not initialized")
        
        try:
            logger.info(f"Processing query: {query}")
            
            # Step 1: Retrieve relevant documents
            retrieved_docs = await self.embedding_manager.search_similar(
                collection_name=collection_name,
                query=query,
                n_results=self.max_results
            )
            
            logger.info(f"Retrieved {len(retrieved_docs)} documents")
            
            # Step 2: Filter by similarity threshold
            filtered_docs = [
                doc for doc in retrieved_docs 
                if doc.get("distance", 1.0) <= self.similarity_threshold
            ]
            
            # Fallback: If no docs meet threshold, use top N docs anyway
            if not filtered_docs and retrieved_docs:
                logger.warning(f"No documents met similarity threshold ({self.similarity_threshold}). Using top {self.min_docs_for_llm} docs as fallback.")
                filtered_docs = retrieved_docs[:self.min_docs_for_llm]
            elif len(filtered_docs) < self.min_docs_for_llm and retrieved_docs:
                # If we have some docs but not enough, add more from retrieved
                additional_docs = [doc for doc in retrieved_docs if doc not in filtered_docs]
                filtered_docs.extend(additional_docs[:self.min_docs_for_llm - len(filtered_docs)])
                logger.info(f"Added {len(additional_docs[:self.min_docs_for_llm - len(filtered_docs)])} additional docs to meet minimum requirement")
            
            if not filtered_docs:
                logger.warning("No documents available at all")
                return {
                    "answer": "I couldn't find any relevant information in the available documents.",
                    "sources": [],
                    "metadata": {
                        "query": query,
                        "collection": collection_name,
                        "retrieved_count": len(retrieved_docs),
                        "filtered_count": 0
                    }
                }
            
            logger.info(f"Using {len(filtered_docs)} documents after filtering and fallback")
            
            # Step 3: Generate response using LLM
            try:
                context_parts = [self.build_context(doc, i+1) for i, doc in enumerate(filtered_docs)]
                context = "\n\n".join(context_parts)
                answer = await self.llm_manager.generate_response(
                    prompt=query,
                    context=context
                )
                logger.info("LLM manager generate_response completed successfully")
            except Exception as e:
                logger.error(f"LLM manager generate_response failed: {e}")
                logger.error(f"Error type: {type(e)}")
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                raise
            
            # Step 4: Prepare response
            sources = []
            for doc in filtered_docs:
                sources.append({
                    "content": doc.get("content", ""),
                    "metadata": doc.get("metadata", {}),
                    "similarity_score": 1.0 - doc.get("distance", 0.0)  # Convert distance to similarity
                })
            
            return {
                "answer": answer,
                "sources": sources,
                "metadata": {
                    "query": query,
                    "collection": collection_name,
                    "retrieved_count": len(retrieved_docs),
                    "filtered_count": len(filtered_docs),
                    "similarity_threshold": self.similarity_threshold
                }
            }
            
        except Exception as e:
            logger.error(f"Retrieve and generate failed: {e}")
            raise
    
    async def retrieve_only(self, query: str, collection_name: str) -> List[Dict[str, Any]]:
        """Retrieve documents without generating a response."""
        if not self._initialized:
            raise RuntimeError("Retriever not initialized")
        
        try:
            retrieved_docs = await self.embedding_manager.search_similar(
                collection_name=collection_name,
                query=query,
                n_results=self.max_results
            )
            
            # Convert to standard format
            results = []
            for doc in retrieved_docs:
                results.append({
                    "content": doc.get("content", ""),
                    "metadata": doc.get("metadata", {}),
                    "similarity_score": 1.0 - doc.get("distance", 0.0)
                })
            
            return results
            
        except Exception as e:
            logger.error(f"Retrieve only failed: {e}")
            raise
    
    def get_stats(self) -> Dict[str, Any]:
        """Get retriever statistics."""
        return {
            "max_results": self.max_results,
            "similarity_threshold": self.similarity_threshold,
            "initialized": self._initialized
        } 