"""
Embedding management for the RAG system.
"""

import logging
from pathlib import Path
from typing import List, Optional, Dict, Any
import hashlib
import pickle
import streamlit as st

try:
    from sentence_transformers import SentenceTransformer
    import chromadb
    from chromadb.config import Settings
except ImportError as e:
    st.error(f"Missing required dependencies: {e}")
    st.info("Please install: pip install sentence-transformers chromadb")

logger = logging.getLogger(__name__)

class EmbeddingManager:
    """Manages embeddings and vector storage for LinkedIn posts."""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", persist_directory: str = ".chromadb"):
        self.model_name = model_name
        self.persist_directory = Path(persist_directory)
        self.persist_directory.mkdir(exist_ok=True)
        
        # Initialize embedding model
        self._model = None
        self._client = None
        self._collection = None
    
    @property
    def model(self) -> SentenceTransformer:
        """Lazy loading of the embedding model."""
        if self._model is None:
            try:
                self._model = SentenceTransformer(self.model_name)
                logger.info(f"Loaded embedding model: {self.model_name}")
            except Exception as e:
                logger.error(f"Failed to load embedding model: {e}")
                raise
        return self._model
    
    @property
    def client(self) -> chromadb.Client:
        """Lazy loading of ChromaDB client."""
        if self._client is None:
            try:
                self._client = chromadb.PersistentClient(
                    path=str(self.persist_directory),
                    settings=Settings(
                        anonymized_telemetry=False,
                        allow_reset=True
                    )
                )
                logger.info(f"Connected to ChromaDB at: {self.persist_directory}")
            except Exception as e:
                logger.error(f"Failed to connect to ChromaDB: {e}")
                raise
        return self._client
    
    def get_collection(self, collection_name: str = "linkedin_posts") -> chromadb.Collection:
        """Get or create a ChromaDB collection."""
        try:
            # Try to get existing collection
            collection = self.client.get_collection(collection_name)
            logger.info(f"Retrieved existing collection: {collection_name}")
        except ValueError:
            # Create new collection if it doesn't exist
            collection = self.client.create_collection(
                name=collection_name,
                metadata={"hnsw:space": "cosine"}
            )
            logger.info(f"Created new collection: {collection_name}")
        
        self._collection = collection
        return collection
    
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of text strings to embed
            
        Returns:
            List of embedding vectors
        """
        try:
            embeddings = self.model.encode(texts, convert_to_tensor=False, show_progress_bar=True)
            return embeddings.tolist()
        except Exception as e:
            logger.error(f"Failed to generate embeddings: {e}")
            raise
    
    def add_documents(self, 
                     texts: List[str], 
                     metadatas: List[Dict[str, Any]], 
                     ids: Optional[List[str]] = None,
                     collection_name: str = "linkedin_posts") -> None:
        """
        Add documents to the vector store.
        
        Args:
            texts: List of text content to embed and store
            metadatas: List of metadata dictionaries for each text
            ids: Optional list of document IDs
            collection_name: Name of the collection to store in
        """
        if not texts:
            logger.warning("No texts provided for embedding")
            return
        
        if len(texts) != len(metadatas):
            raise ValueError("Number of texts and metadatas must match")
        
        if ids and len(ids) != len(texts):
            raise ValueError("Number of IDs must match number of texts")
        
        try:
            # Generate IDs if not provided
            if not ids:
                ids = [hashlib.md5(text.encode()).hexdigest() for text in texts]
            
            # Get collection
            collection = self.get_collection(collection_name)
            
            # Generate embeddings
            st.info(f"Generating embeddings for {len(texts)} documents...")
            embeddings = self.embed_texts(texts)
            
            # Add to collection
            collection.add(
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas,
                ids=ids
            )
            
            logger.info(f"Added {len(texts)} documents to collection {collection_name}")
            st.success(f"Successfully indexed {len(texts)} posts!")
            
        except Exception as e:
            logger.error(f"Failed to add documents: {e}")
            st.error(f"Failed to index documents: {e}")
            raise
    
    def search(self, 
               query: str, 
               n_results: int = 8,
               collection_name: str = "linkedin_posts",
               where: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Search for similar documents.
        
        Args:
            query: Search query text
            n_results: Number of results to return
            collection_name: Name of the collection to search
            where: Optional metadata filter
            
        Returns:
            Dictionary with search results
        """
        try:
            collection = self.get_collection(collection_name)
            
            # Generate query embedding
            query_embedding = self.embed_texts([query])[0]
            
            # Perform search
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                where=where,
                include=["documents", "metadatas", "distances"]
            )
            
            logger.info(f"Search returned {len(results['documents'][0])} results")
            return results
            
        except Exception as e:
            logger.error(f"Search failed: {e}")
            raise
    
    def get_collection_stats(self, collection_name: str = "linkedin_posts") -> Dict[str, Any]:
        """
        Get statistics about a collection.
        
        Args:
            collection_name: Name of the collection
            
        Returns:
            Dictionary with collection statistics
        """
        try:
            collection = self.get_collection(collection_name)
            count = collection.count()
            
            return {
                "name": collection_name,
                "document_count": count,
                "embedding_model": self.model_name,
                "persist_directory": str(self.persist_directory)
            }
        except Exception as e:
            logger.error(f"Failed to get collection stats: {e}")
            return {}
    
    def delete_collection(self, collection_name: str = "linkedin_posts") -> None:
        """Delete a collection."""
        try:
            self.client.delete_collection(collection_name)
            logger.info(f"Deleted collection: {collection_name}")
        except Exception as e:
            logger.error(f"Failed to delete collection: {e}")
            raise
    
    def reset_database(self) -> None:
        """Reset the entire database (use with caution)."""
        try:
            self.client.reset()
            self._collection = None
            logger.info("Database reset successfully")
        except Exception as e:
            logger.error(f"Failed to reset database: {e}")
            raise

def prepare_documents_for_embedding(df) -> tuple[List[str], List[Dict[str, Any]], List[str]]:
    """
    Prepare LinkedIn posts for embedding.
    
    Args:
        df: Polars DataFrame with LinkedIn posts
        
    Returns:
        Tuple of (texts, metadatas, ids)
    """
    texts = []
    metadatas = []
    ids = []
    
    try:
        # Convert to pandas for easier iteration
        df_pandas = df.to_pandas()
        
        for idx, row in df_pandas.iterrows():
            # Create combined text for embedding
            text_parts = []
            
            # Author and content
            if 'author' in row and row['author']:
                text_parts.append(f"Author: {row['author']}")
            
            if 'content' in row and row['content']:
                text_parts.append(f"Content: {row['content']}")
            
            # Additional context
            if 'hashtags' in row and row['hashtags']:
                hashtags = row['hashtags'] if isinstance(row['hashtags'], str) else str(row['hashtags'])
                text_parts.append(f"Hashtags: {hashtags}")
            
            text = "\n".join(text_parts)
            
            if not text.strip():
                continue
            
            # Create metadata
            metadata = {
                "author": str(row.get('author', '')),
                "likes": int(row.get('likes', 0)) if row.get('likes') else 0,
                "comments": int(row.get('comments', 0)) if row.get('comments') else 0,
                "post_url": str(row.get('post_url', row.get('url', ''))),
                "source": "linkedin_scraper"
            }
            
            # Add optional fields
            optional_fields = ['posted_at', 'timestamp', 'urn', 'hashtags']
            for field in optional_fields:
                if field in row and row[field]:
                    metadata[field] = str(row[field])
            
            # Generate ID
            doc_id = row.get('urn', f"post_{idx}")
            if not isinstance(doc_id, str):
                doc_id = str(doc_id)
            
            texts.append(text)
            metadatas.append(metadata)
            ids.append(doc_id)
        
        logger.info(f"Prepared {len(texts)} documents for embedding")
        return texts, metadatas, ids
        
    except Exception as e:
        logger.error(f"Failed to prepare documents: {e}")
        raise

@st.cache_resource
def get_embedding_manager() -> EmbeddingManager:
    """Get cached embedding manager instance."""
    return EmbeddingManager()

def index_dataframe(df, collection_name: str = "linkedin_posts") -> bool:
    """
    Index a DataFrame in the vector store.
    
    Args:
        df: Polars DataFrame with LinkedIn posts
        collection_name: Name of the collection
        
    Returns:
        True if successful, False otherwise
    """
    try:
        manager = get_embedding_manager()
        texts, metadatas, ids = prepare_documents_for_embedding(df)
        
        if not texts:
            st.warning("No valid documents found for indexing")
            return False
        
        manager.add_documents(texts, metadatas, ids, collection_name)
        return True
        
    except Exception as e:
        logger.error(f"Failed to index DataFrame: {e}")
        st.error(f"Indexing failed: {e}")
        return False 