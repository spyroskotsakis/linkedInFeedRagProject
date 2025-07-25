"""
Unit tests for RAG components.
"""

import pytest
from unittest.mock import patch, MagicMock
from langchain.schema import Document

from rag.llm_factory import (
    LLMProviderFactory, 
    OllamaProvider, 
    AzureOpenAIProvider,
    get_llm,
    check_ollama
)
from rag.embeddings import (
    EmbeddingManager,
    prepare_documents_for_embedding,
    index_dataframe
)
from rag.retriever import (
    VectorRetriever,
    FeedVectorStore,
    get_retriever,
    search_posts,
    test_retriever
)
from rag.rag_graph import (
    build_rag_graph,
    run_rag_query,
    test_rag_workflow
)

class TestLLMProviders:
    """Test cases for LLM provider functionality."""
    
    def test_ollama_provider_unavailable(self, mock_streamlit):
        """Test OllamaProvider when service is unavailable."""
        with patch('rag.llm_factory.ollama.list') as mock_list:
            mock_list.side_effect = Exception("Connection failed")
            
            provider = OllamaProvider()
            assert provider.is_available() is False
    
    def test_ollama_provider_model_missing(self, mock_streamlit):
        """Test OllamaProvider when model is not available."""
        with patch('rag.llm_factory.ollama.list') as mock_list:
            mock_list.return_value = {"models": [{"name": "other-model:latest"}]}
            
            provider = OllamaProvider()
            assert provider.is_available() is False
    
    def test_ollama_provider_available(self, mock_streamlit):
        """Test OllamaProvider when model is available."""
        with patch('rag.llm_factory.ollama.list') as mock_list:
            mock_list.return_value = {"models": [{"name": "mistral-nemo:12b"}]}
            
            provider = OllamaProvider()
            assert provider.is_available() is True
    
    def test_ollama_health_check(self, mock_streamlit):
        """Test Ollama health check functionality."""
        with patch('rag.llm_factory.ollama.list') as mock_list, \
             patch('rag.llm_factory.ollama.chat') as mock_chat:
            
            mock_list.return_value = {"models": [{"name": "mistral-nemo:12b"}]}
            mock_chat.return_value = {"message": {"content": "Hello!"}}
            
            provider = OllamaProvider()
            result = provider.health_check()
            
            assert result["status"] == "healthy"
            assert result["model_available"] is True
            assert result["response_test"] is True
    
    def test_azure_provider_missing_config(self, mock_streamlit):
        """Test AzureOpenAIProvider without configuration."""
        with patch.dict('os.environ', {}, clear=True):
            provider = AzureOpenAIProvider()
            assert provider.is_available() is False
    
    def test_azure_provider_configured(self, mock_streamlit):
        """Test AzureOpenAIProvider with proper configuration."""
        env_vars = {
            'AZURE_OPENAI_ENDPOINT': 'https://test.openai.azure.com',
            'AZURE_OPENAI_API_KEY': 'test-key',
            'AZURE_OPENAI_DEPLOYMENT': 'gpt-4'
        }
        
        with patch.dict('os.environ', env_vars):
            provider = AzureOpenAIProvider()
            assert provider.is_available() is True
    
    def test_llm_factory_get_provider(self, mock_streamlit):
        """Test LLMProviderFactory provider retrieval."""
        factory = LLMProviderFactory()
        
        ollama_provider = factory.get_provider("ollama")
        assert isinstance(ollama_provider, OllamaProvider)
        
        azure_provider = factory.get_provider("azure")
        assert isinstance(azure_provider, AzureOpenAIProvider)
        
        with pytest.raises(ValueError):
            factory.get_provider("unknown")
    
    def test_check_ollama_function(self, mock_streamlit):
        """Test the check_ollama convenience function."""
        with patch('rag.llm_factory.ollama.list') as mock_list:
            mock_list.return_value = {"models": [{"name": "mistral-nemo:12b"}]}
            assert check_ollama() is True
            
            mock_list.side_effect = Exception("Connection failed")
            assert check_ollama() is False

@pytest.mark.rag
class TestEmbeddingManager:
    """Test cases for EmbeddingManager."""
    
    def test_embedding_manager_init(self, mock_streamlit, temp_chromadb):
        """Test EmbeddingManager initialization."""
        with patch('rag.embeddings.SentenceTransformer') as mock_st:
            manager = EmbeddingManager(persist_directory=temp_chromadb)
            assert manager.model_name == "all-MiniLM-L6-v2"
            assert manager.persist_directory.exists()
    
    def test_embed_texts(self, mock_streamlit, temp_chromadb):
        """Test text embedding functionality."""
        with patch('rag.embeddings.SentenceTransformer') as mock_st:
            mock_model = MagicMock()
            mock_model.encode.return_value = [[0.1, 0.2], [0.3, 0.4]]
            mock_st.return_value = mock_model
            
            manager = EmbeddingManager(persist_directory=temp_chromadb)
            embeddings = manager.embed_texts(["text1", "text2"])
            
            assert embeddings == [[0.1, 0.2], [0.3, 0.4]]
            mock_model.encode.assert_called_once()
    
    def test_prepare_documents_for_embedding(self, mock_streamlit, sample_dataframe):
        """Test document preparation for embedding."""
        texts, metadatas, ids = prepare_documents_for_embedding(sample_dataframe)
        
        assert len(texts) == 3
        assert len(metadatas) == 3
        assert len(ids) == 3
        
        # Check text format
        assert "Author: John Doe" in texts[0]
        assert "Content: Excited to share" in texts[0]
        
        # Check metadata
        assert metadatas[0]["author"] == "John Doe"
        assert metadatas[0]["likes"] == 45
        assert metadatas[0]["source"] == "linkedin_scraper"
        
        # Check IDs
        assert ids[0] == "urn:li:activity:123456"

class TestVectorRetriever:
    """Test cases for VectorRetriever."""
    
    def test_vector_retriever_init(self, mock_streamlit, mock_embedding_manager):
        """Test VectorRetriever initialization."""
        with patch('rag.retriever.get_embedding_manager', return_value=mock_embedding_manager):
            retriever = VectorRetriever("test_collection", {"k": 5})
            
            assert retriever.collection_name == "test_collection"
            assert retriever.search_kwargs["k"] == 5
    
    def test_get_relevant_documents(self, mock_streamlit, mock_embedding_manager):
        """Test document retrieval."""
        with patch('rag.retriever.get_embedding_manager', return_value=mock_embedding_manager):
            retriever = VectorRetriever()
            documents = retriever._get_relevant_documents("test query")
            
            assert len(documents) == 2
            assert isinstance(documents[0], Document)
            assert documents[0].page_content == "Sample document 1"
            assert documents[0].metadata["similarity_score"] == 0.9  # 1.0 - 0.1
    
    def test_feed_vector_store_similarity_search(self, mock_streamlit, mock_embedding_manager):
        """Test similarity search in FeedVectorStore."""
        with patch('rag.retriever.get_embedding_manager', return_value=mock_embedding_manager):
            store = FeedVectorStore()
            documents = store.similarity_search("test query", k=2)
            
            assert len(documents) == 2
            assert documents[0].metadata["similarity_score"] == 0.9
    
    def test_search_posts_with_filters(self, mock_streamlit, mock_embedding_manager):
        """Test post search with author and likes filters."""
        with patch('rag.retriever.get_embedding_manager', return_value=mock_embedding_manager):
            results = search_posts(
                "test query",
                filter_by_author="Test Author",
                min_likes=5
            )
            
            assert len(results) == 2
            assert "similarity_score" in results[0]
    
    def test_test_retriever_function(self, mock_streamlit, mock_embedding_manager):
        """Test the test_retriever utility function."""
        with patch('rag.retriever.get_embedding_manager', return_value=mock_embedding_manager):
            result = test_retriever()
            
            assert result["status"] == "success"
            assert "collection_stats" in result
            assert "sample_results" in result

@pytest.mark.rag 
class TestRAGGraph:
    """Test cases for RAG graph workflow."""
    
    def test_build_rag_graph(self, mock_streamlit):
        """Test RAG graph construction."""
        with patch('rag.rag_graph.get_retriever'), \
             patch('rag.rag_graph.get_configured_llm'):
            
            graph = build_rag_graph("test_collection")
            assert graph is not None
    
    def test_run_rag_query_success(self, mock_streamlit, mock_embedding_manager, mock_llm):
        """Test successful RAG query execution."""
        # Mock the retriever
        mock_retriever = MagicMock()
        mock_docs = [
            Document(
                page_content="Test content about AI",
                metadata={"author": "Expert", "similarity_score": 0.9}
            )
        ]
        mock_retriever._get_relevant_documents.return_value = mock_docs
        
        with patch('rag.rag_graph.get_retriever', return_value=mock_retriever), \
             patch('rag.rag_graph.get_configured_llm', return_value=mock_llm):
            
            result = run_rag_query("What is AI?")
            
            assert result["query"] == "What is AI?"
            assert "answer" in result
            assert result["document_count"] == 1
            assert result["confidence_score"] > 0
    
    def test_run_rag_query_no_documents(self, mock_streamlit, mock_llm):
        """Test RAG query when no documents are found."""
        mock_retriever = MagicMock()
        mock_retriever._get_relevant_documents.return_value = []
        
        with patch('rag.rag_graph.get_retriever', return_value=mock_retriever), \
             patch('rag.rag_graph.get_configured_llm', return_value=mock_llm):
            
            result = run_rag_query("Unknown topic")
            
            assert "couldn't find any relevant" in result["answer"]
            assert result["confidence_score"] == 0.0
    
    def test_run_rag_query_error_handling(self, mock_streamlit):
        """Test RAG query error handling."""
        with patch('rag.rag_graph.get_retriever', side_effect=Exception("Test error")):
            
            result = run_rag_query("Test query")
            
            assert "error" in result["answer"]
            assert result["error"] is not None
    
    def test_rag_workflow_testing(self, mock_streamlit, mock_embedding_manager, mock_llm):
        """Test the RAG workflow testing function."""
        mock_retriever = MagicMock()
        mock_retriever._get_relevant_documents.return_value = [
            Document(page_content="Test", metadata={"similarity_score": 0.8})
        ]
        
        with patch('rag.rag_graph.get_retriever', return_value=mock_retriever), \
             patch('rag.rag_graph.get_configured_llm', return_value=mock_llm):
            
            result = test_rag_workflow()
            
            assert result["total_tests"] == 3
            assert "successful_tests" in result
            assert len(result["results"]) == 3

# Integration tests
@pytest.mark.integration
@pytest.mark.rag
class TestRAGIntegration:
    """Integration tests for RAG components."""
    
    def test_embedding_to_retrieval_workflow(self, mock_streamlit, sample_dataframe, temp_chromadb):
        """Test complete workflow from embedding to retrieval."""
        with patch('rag.embeddings.SentenceTransformer') as mock_st, \
             patch('rag.embeddings.chromadb.PersistentClient') as mock_client:
            
            # Mock sentence transformer
            mock_model = MagicMock()
            mock_model.encode.return_value = [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
            mock_st.return_value = mock_model
            
            # Mock ChromaDB
            mock_collection = MagicMock()
            mock_client_instance = MagicMock()
            mock_client_instance.get_collection.return_value = mock_collection
            mock_client.return_value = mock_client_instance
            
            # Test document preparation and indexing
            texts, metadatas, ids = prepare_documents_for_embedding(sample_dataframe)
            assert len(texts) == 3
            
            # Test indexing
            manager = EmbeddingManager(persist_directory=temp_chromadb)
            manager.add_documents(texts, metadatas, ids)
            
            # Verify collection.add was called
            mock_collection.add.assert_called_once()

# Performance tests
@pytest.mark.slow
@pytest.mark.rag
class TestRAGPerformance:
    """Performance tests for RAG components."""
    
    def test_embedding_performance(self, mock_streamlit, temp_chromadb):
        """Test embedding performance with larger datasets."""
        with patch('rag.embeddings.SentenceTransformer') as mock_st:
            # Mock fast embedding generation
            mock_model = MagicMock()
            mock_model.encode.return_value = [[0.1] * 384] * 1000  # 1000 embeddings
            mock_st.return_value = mock_model
            
            manager = EmbeddingManager(persist_directory=temp_chromadb)
            
            import time
            start = time.time()
            embeddings = manager.embed_texts(["text"] * 1000)
            elapsed = time.time() - start
            
            assert len(embeddings) == 1000
            assert elapsed < 10.0  # Should complete within 10 seconds
    
    def test_retrieval_performance(self, mock_streamlit, mock_embedding_manager):
        """Test retrieval performance."""
        with patch('rag.retriever.get_embedding_manager', return_value=mock_embedding_manager):
            retriever = VectorRetriever()
            
            import time
            start = time.time()
            
            # Run multiple searches
            for i in range(100):
                documents = retriever._get_relevant_documents(f"query {i}")
            
            elapsed = time.time() - start
            assert elapsed < 5.0  # 100 searches should complete within 5 seconds 