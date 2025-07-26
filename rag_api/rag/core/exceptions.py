"""
RAG Exceptions Module

Custom exceptions for the RAG system.
"""

from typing import Dict, Any


class RAGException(Exception):
    """Base exception for RAG system."""
    
    def __init__(self, message: str, details: Dict[str, Any] = None):
        super().__init__(message)
        self.message = message
        self.details = details or {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for API responses."""
        return {
            'error': self.__class__.__name__,
            'message': self.message,
            'details': self.details
        }


class RAGHealthException(RAGException):
    """Exception for health check failures."""
    pass


class RAGConfigException(RAGException):
    """Exception for configuration errors."""
    pass


class RAGEmbeddingException(RAGException):
    """Exception for embedding generation failures."""
    pass


class RAGRetrievalException(RAGException):
    """Exception for retrieval failures."""
    pass


class RAGLLMException(RAGException):
    """Exception for LLM-related failures."""
    pass


class RAGIndexException(RAGException):
    """Exception for indexing failures."""
    pass 