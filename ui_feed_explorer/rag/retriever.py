"""
Vector retriever for the RAG system.
"""

import logging
from typing import List, Dict, Any, Optional
import streamlit as st
from .embeddings import get_embedding_manager

try:
    from langchain_core.documents import Document
    from langchain_core.retrievers import BaseRetriever
except ImportError as e:
    try:
        # Fallback for older versions
        from langchain.schema import Document
        from langchain.retrievers.base import BaseRetriever
    except ImportError:
        st.error(f"Missing required dependencies: {e}")
        st.info("Please install: pip install langchain langchain-core")

logger = logging.getLogger(__name__)

class VectorRetriever(BaseRetriever):
    """Custom retriever using ChromaDB for LinkedIn posts."""
    
    def __init__(self, 
                 collection_name: str = "linkedin_posts",
                 search_kwargs: Optional[Dict[str, Any]] = None):
        self.collection_name = collection_name
        self.search_kwargs = search_kwargs or {"k": 8}
        self.embedding_manager = get_embedding_manager()
    
    def _get_relevant_documents(self, query: str) -> List[Document]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: Search query string
            
        Returns:
            List of relevant Document objects
        """
        try:
            # Get search parameters
            k = self.search_kwargs.get("k", 8)
            where_filter = self.search_kwargs.get("where")
            
            # Perform vector search
            results = self.embedding_manager.search(
                query=query,
                n_results=k,
                collection_name=self.collection_name,
                where=where_filter
            )
            
            # Convert to LangChain Documents
            documents = []
            
            if results and "documents" in results and results["documents"]:
                docs = results["documents"][0]  # ChromaDB returns nested lists
                metadatas = results.get("metadatas", [{}])[0]
                distances = results.get("distances", [0.0])[0]
                
                for i, doc_text in enumerate(docs):
                    metadata = metadatas[i] if i < len(metadatas) else {}
                    distance = distances[i] if i < len(distances) else 0.0
                    
                    # Add similarity score (convert distance to similarity)
                    metadata["similarity_score"] = 1.0 - distance
                    metadata["search_query"] = query
                    
                    document = Document(
                        page_content=doc_text,
                        metadata=metadata
                    )
                    documents.append(document)
            
            logger.info(f"Retrieved {len(documents)} relevant documents for query: {query}")
            return documents
            
        except Exception as e:
            logger.error(f"Error retrieving documents: {e}")
            return []
    
    async def _aget_relevant_documents(self, query: str) -> List[Document]:
        """Async version of _get_relevant_documents."""
        return self._get_relevant_documents(query)

class FeedVectorStore:
    """Vector store wrapper for LinkedIn feed data."""
    
    def __init__(self, collection_name: str = "linkedin_posts"):
        self.collection_name = collection_name
        self.embedding_manager = get_embedding_manager()
    
    def similarity_search(self, 
                         query: str, 
                         k: int = 8,
                         filter: Optional[Dict[str, Any]] = None) -> List[Document]:
        """
        Perform similarity search and return documents.
        
        Args:
            query: Search query
            k: Number of documents to return
            filter: Optional metadata filter
            
        Returns:
            List of relevant documents
        """
        try:
            results = self.embedding_manager.search(
                query=query,
                n_results=k,
                collection_name=self.collection_name,
                where=filter
            )
            
            documents = []
            
            if results and "documents" in results:
                docs = results["documents"][0]
                metadatas = results.get("metadatas", [{}])[0]
                distances = results.get("distances", [0.0])[0]
                
                for i, doc_text in enumerate(docs):
                    metadata = metadatas[i] if i < len(metadatas) else {}
                    distance = distances[i] if i < len(distances) else 0.0
                    
                    metadata["similarity_score"] = 1.0 - distance
                    
                    documents.append(Document(
                        page_content=doc_text,
                        metadata=metadata
                    ))
            
            return documents
            
        except Exception as e:
            logger.error(f"Similarity search failed: {e}")
            return []
    
    def similarity_search_with_score(self, 
                                   query: str, 
                                   k: int = 8,
                                   filter: Optional[Dict[str, Any]] = None) -> List[tuple[Document, float]]:
        """
        Perform similarity search and return documents with scores.
        
        Args:
            query: Search query
            k: Number of documents to return
            filter: Optional metadata filter
            
        Returns:
            List of (document, score) tuples
        """
        try:
            results = self.embedding_manager.search(
                query=query,
                n_results=k,
                collection_name=self.collection_name,
                where=filter
            )
            
            documents_with_scores = []
            
            if results and "documents" in results:
                docs = results["documents"][0]
                metadatas = results.get("metadatas", [{}])[0]
                distances = results.get("distances", [0.0])[0]
                
                for i, doc_text in enumerate(docs):
                    metadata = metadatas[i] if i < len(metadatas) else {}
                    distance = distances[i] if i < len(distances) else 0.0
                    similarity_score = 1.0 - distance
                    
                    metadata["similarity_score"] = similarity_score
                    
                    document = Document(
                        page_content=doc_text,
                        metadata=metadata
                    )
                    
                    documents_with_scores.append((document, similarity_score))
            
            return documents_with_scores
            
        except Exception as e:
            logger.error(f"Similarity search with score failed: {e}")
            return []

def create_vector_store(collection_name: str = "linkedin_posts") -> FeedVectorStore:
    """
    Create a vector store for the specified collection.
    
    Args:
        collection_name: Name of the ChromaDB collection
        
    Returns:
        FeedVectorStore instance
    """
    return FeedVectorStore(collection_name)

def get_retriever(collection_name: str = "linkedin_posts", 
                 search_kwargs: Optional[Dict[str, Any]] = None) -> VectorRetriever:
    """
    Get a configured retriever for the specified collection.
    
    Args:
        collection_name: Name of the ChromaDB collection
        search_kwargs: Search configuration parameters
        
    Returns:
        VectorRetriever instance
    """
    return VectorRetriever(collection_name, search_kwargs)

def search_posts(query: str, 
                collection_name: str = "linkedin_posts",
                k: int = 8,
                filter_by_author: Optional[str] = None,
                min_likes: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Search LinkedIn posts with optional filters.
    
    Args:
        query: Search query
        collection_name: Collection name
        k: Number of results
        filter_by_author: Optional author filter
        min_likes: Optional minimum likes filter
        
    Returns:
        List of search results with metadata
    """
    try:
        # Build filter
        where_filter = {}
        if filter_by_author:
            where_filter["author"] = {"$eq": filter_by_author}
        if min_likes is not None:
            where_filter["likes"] = {"$gte": min_likes}
        
        vector_store = create_vector_store(collection_name)
        documents = vector_store.similarity_search(
            query=query,
            k=k,
            filter=where_filter if where_filter else None
        )
        
        # Convert to dictionaries for easier handling
        results = []
        for doc in documents:
            result = {
                "content": doc.page_content,
                "metadata": doc.metadata,
                "similarity_score": doc.metadata.get("similarity_score", 0.0)
            }
            results.append(result)
        
        return results
        
    except Exception as e:
        logger.error(f"Post search failed: {e}")
        return []

def test_retriever(collection_name: str = "linkedin_posts") -> Dict[str, Any]:
    """
    Test the retriever functionality.
    
    Args:
        collection_name: Collection to test
        
    Returns:
        Test results dictionary
    """
    try:
        retriever = get_retriever(collection_name)
        
        # Test query
        test_query = "artificial intelligence machine learning"
        results = retriever._get_relevant_documents(test_query)
        
        # Get collection stats
        embedding_manager = get_embedding_manager()
        stats = embedding_manager.get_collection_stats(collection_name)
        
        return {
            "status": "success",
            "collection_stats": stats,
            "test_query": test_query,
            "results_count": len(results),
            "sample_results": [
                {
                    "content_preview": doc.page_content[:100] + "..." if len(doc.page_content) > 100 else doc.page_content,
                    "similarity_score": doc.metadata.get("similarity_score", 0.0),
                    "author": doc.metadata.get("author", "Unknown")
                }
                for doc in results[:3]  # Show first 3 results
            ]
        }
        
    except Exception as e:
        logger.error(f"Retriever test failed: {e}")
        return {
            "status": "error",
            "error": str(e)
        } 