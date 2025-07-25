"""
Pytest configuration and fixtures for UI Feed Explorer tests.
"""

import pytest
import tempfile
import shutil
from pathlib import Path
import polars as pl
import json
from unittest.mock import MagicMock, patch
import os

@pytest.fixture
def sample_linkedin_data():
    """Sample LinkedIn post data for testing."""
    return [
        {
            "urn": "urn:li:activity:123456",
            "author": "John Doe", 
            "content": "Excited to share my thoughts on artificial intelligence and machine learning trends in 2024!",
            "likes": 45,
            "comments": 8,
            "shares": 3,
            "posted_at": "2024-01-15T10:30:00Z",
            "hashtags": "#AI #MachineLearning #Technology",
            "url": "https://linkedin.com/posts/activity-123456"
        },
        {
            "urn": "urn:li:activity:789012",
            "author": "Jane Smith",
            "content": "Career advice for new graduates: Focus on continuous learning and building meaningful connections.",
            "likes": 67,
            "comments": 12,
            "shares": 5,
            "posted_at": "2024-01-14T14:45:00Z", 
            "hashtags": "#Career #Advice #GradLife",
            "url": "https://linkedin.com/posts/activity-789012"
        },
        {
            "urn": "urn:li:activity:345678",
            "author": "Tech Leader",
            "content": "The future of work is remote-first. Companies need to adapt their culture and processes accordingly.",
            "likes": 89,
            "comments": 24,
            "shares": 11,
            "posted_at": "2024-01-13T09:15:00Z",
            "hashtags": "#RemoteWork #FutureOfWork #WorkCulture", 
            "url": "https://linkedin.com/posts/activity-345678"
        }
    ]

@pytest.fixture
def sample_dataframe(sample_linkedin_data):
    """Polars DataFrame with sample data."""
    return pl.DataFrame(sample_linkedin_data)

@pytest.fixture
def temp_data_dir(sample_linkedin_data):
    """Create temporary data directory with sample exports."""
    temp_dir = tempfile.mkdtemp()
    data_dir = Path(temp_dir) / "data"
    data_dir.mkdir()
    
    # Create a sample export directory
    export_dir = data_dir / "posts_3_2024-01-15_12-30"
    export_dir.mkdir()
    
    # Create sample files
    json_file = export_dir / "linkedin_feed_20240115_123000.json"
    with open(json_file, 'w') as f:
        json.dump(sample_linkedin_data, f)
    
    csv_file = export_dir / "posts_analysis_20240115_123000.csv"
    df = pl.DataFrame(sample_linkedin_data)
    df.write_csv(csv_file)
    
    yield temp_dir
    
    # Cleanup
    shutil.rmtree(temp_dir)

@pytest.fixture
def mock_embedding_manager():
    """Mock embedding manager for testing."""
    mock = MagicMock()
    mock.embed_texts.return_value = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    mock.search.return_value = {
        "documents": [["Sample document 1", "Sample document 2"]],
        "metadatas": [[{"author": "Test Author", "likes": 10}, {"author": "Another Author", "likes": 20}]],
        "distances": [[0.1, 0.2]]
    }
    mock.get_collection_stats.return_value = {
        "name": "test_collection",
        "document_count": 100,
        "embedding_model": "test-model"
    }
    return mock

@pytest.fixture
def mock_llm():
    """Mock LLM for testing."""
    mock = MagicMock()
    mock.invoke.return_value = MagicMock(content="This is a test response from the LLM.")
    return mock

@pytest.fixture
def mock_streamlit():
    """Mock Streamlit components for testing."""
    with patch('streamlit.cache_data') as mock_cache, \
         patch('streamlit.cache_resource') as mock_resource, \
         patch('streamlit.session_state', {}) as mock_session:
        
        # Make cache decorators pass through
        mock_cache.side_effect = lambda *args, **kwargs: lambda func: func
        mock_resource.side_effect = lambda *args, **kwargs: lambda func: func
        
        yield {
            'cache_data': mock_cache,
            'cache_resource': mock_resource,
            'session_state': mock_session
        }

@pytest.fixture
def temp_chromadb():
    """Temporary ChromaDB instance for testing."""
    temp_dir = tempfile.mkdtemp()
    
    # Set environment variable for test database
    original_path = os.environ.get('CHROMADB_PATH')
    os.environ['CHROMADB_PATH'] = temp_dir
    
    yield temp_dir
    
    # Cleanup
    if original_path:
        os.environ['CHROMADB_PATH'] = original_path
    else:
        os.environ.pop('CHROMADB_PATH', None)
    
    shutil.rmtree(temp_dir)

@pytest.fixture
def mock_file_system():
    """Mock file system operations."""
    with patch('pathlib.Path.exists') as mock_exists, \
         patch('pathlib.Path.is_dir') as mock_is_dir, \
         patch('pathlib.Path.iterdir') as mock_iterdir:
        
        yield {
            'exists': mock_exists,
            'is_dir': mock_is_dir,
            'iterdir': mock_iterdir
        }

# Test configuration
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )
    config.addinivalue_line(
        "markers", "rag: mark test as RAG-related"
    )
    config.addinivalue_line(
        "markers", "ui: mark test as UI component test"
    ) 