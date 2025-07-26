"""
RAG Configuration Module

Handles configuration management for the RAG system.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from pathlib import Path


@dataclass
class EmbeddingConfig:
    """Configuration for text embeddings."""
    model_name: str = "all-MiniLM-L6-v2"
    batch_size: int = 32
    max_length: int = 512


@dataclass
class VectorStoreConfig:
    """Configuration for vector store."""
    persist_directory: str = "/app/vector_store"
    collection_name: str = "linkedin_posts"
    distance_metric: str = "cosine"


@dataclass
class LLMConfig:
    """Configuration for LLM providers."""
    provider: str = "ollama"  # "ollama" or "azure"
    model: str = "mistral-nemo:12b"
    temperature: float = 0.1
    max_tokens: int = 2048
    base_url: Optional[str] = None
    api_key: Optional[str] = None
    deployment: Optional[str] = None


@dataclass
class RetrievalConfig:
    """Configuration for retrieval."""
    top_k: int = 10
    similarity_threshold: float = 0.7
    rerank: bool = False


@dataclass
class RAGConfig:
    """Main RAG configuration."""
    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)
    vector_store: VectorStoreConfig = field(default_factory=VectorStoreConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    retrieval: RetrievalConfig = field(default_factory=RetrievalConfig)
    
    @classmethod
    def from_env(cls) -> 'RAGConfig':
        """Create configuration from environment variables."""
        config = cls()
        
        # Embedding configuration
        if os.getenv('RAG_EMBEDDING_MODEL'):
            config.embedding.model_name = os.getenv('RAG_EMBEDDING_MODEL')
        
        # Vector store configuration
        if os.getenv('RAG_VECTOR_STORE_PATH'):
            config.vector_store.persist_directory = os.getenv('RAG_VECTOR_STORE_PATH')
        
        # LLM configuration
        if os.getenv('RAG_LLM_PROVIDER'):
            config.llm.provider = os.getenv('RAG_LLM_PROVIDER')
        
        if os.getenv('OLLAMA_MODEL'):
            config.llm.model = os.getenv('OLLAMA_MODEL')
        
        if os.getenv('OLLAMA_BASE_URL'):
            config.llm.base_url = os.getenv('OLLAMA_BASE_URL')
        
        if os.getenv('AZURE_OPENAI_ENDPOINT'):
            config.llm.base_url = os.getenv('AZURE_OPENAI_ENDPOINT')
        
        if os.getenv('AZURE_OPENAI_API_KEY'):
            config.llm.api_key = os.getenv('AZURE_OPENAI_API_KEY')
        
        if os.getenv('AZURE_OPENAI_DEPLOYMENT'):
            config.llm.deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')
        
        if os.getenv('RAG_LLM_TEMPERATURE'):
            config.llm.temperature = float(os.getenv('RAG_LLM_TEMPERATURE'))
        
        if os.getenv('RAG_LLM_MAX_TOKENS'):
            config.llm.max_tokens = int(os.getenv('RAG_LLM_MAX_TOKENS'))
        
        # Retrieval configuration
        if os.getenv('RAG_MAX_RESULTS'):
            config.retrieval.top_k = int(os.getenv('RAG_MAX_RESULTS'))
        
        return config
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            'embedding': {
                'model_name': self.embedding.model_name,
                'batch_size': self.embedding.batch_size,
                'max_length': self.embedding.max_length
            },
            'vector_store': {
                'persist_directory': self.vector_store.persist_directory,
                'collection_name': self.vector_store.collection_name,
                'distance_metric': self.vector_store.distance_metric
            },
            'llm': {
                'provider': self.llm.provider,
                'model': self.llm.model,
                'temperature': self.llm.temperature,
                'max_tokens': self.llm.max_tokens,
                'base_url': self.llm.base_url,
                'deployment': self.llm.deployment
            },
            'retrieval': {
                'top_k': self.retrieval.top_k,
                'similarity_threshold': self.retrieval.similarity_threshold,
                'rerank': self.retrieval.rerank
            }
        } 