"""
Unit tests for the data loader module.
"""

import pytest
import polars as pl
from pathlib import Path
from unittest.mock import patch, MagicMock
import json

from utils.data_loader import (
    get_export_dirs, 
    load_export, 
    get_export_metadata,
    validate_dataframe
)

class TestGetExportDirs:
    """Test cases for get_export_dirs function."""
    
    def test_get_export_dirs_no_data_directory(self, mock_streamlit):
        """Test handling when data directory doesn't exist."""
        with patch('utils.data_loader.DATA_DIR') as mock_dir:
            mock_dir.exists.return_value = False
            
            result = get_export_dirs()
            assert result == []
    
    def test_get_export_dirs_permission_error(self, mock_streamlit):
        """Test handling of permission errors."""
        with patch('utils.data_loader.DATA_DIR') as mock_dir:
            mock_dir.exists.return_value = True
            mock_dir.is_dir.return_value = True
            mock_dir.iterdir.side_effect = PermissionError("Access denied")
            
            result = get_export_dirs()
            assert result == []
    
    def test_get_export_dirs_success(self, mock_streamlit, temp_data_dir):
        """Test successful directory scanning."""
        with patch('utils.data_loader.DATA_DIR', Path(temp_data_dir) / "data"):
            result = get_export_dirs()
            assert len(result) == 1
            assert result[0].name == "posts_3_2024-01-15_12-30"

class TestLoadExport:
    """Test cases for load_export function."""
    
    def test_load_export_nonexistent_directory(self, mock_streamlit):
        """Test loading from non-existent directory."""
        result = load_export(Path("/nonexistent/path"))
        assert result.is_empty()
    
    def test_load_export_csv_conversion(self, mock_streamlit, temp_data_dir, sample_linkedin_data):
        """Test CSV to Parquet conversion."""
        export_dir = Path(temp_data_dir) / "data" / "posts_3_2024-01-15_12-30"
        
        result = load_export(export_dir)
        
        # Should have converted CSV to Parquet
        parquet_file = export_dir / "linkedin_feed.parquet"
        assert parquet_file.exists()
        
        # Should return data
        assert len(result) == 3
        assert "author" in result.columns
        assert "content" in result.columns
    
    def test_load_export_json_fallback(self, mock_streamlit, temp_data_dir):
        """Test JSON loading when CSV not available."""
        export_dir = Path(temp_data_dir) / "data" / "posts_3_2024-01-15_12-30" 
        
        # Remove CSV file to test JSON fallback
        csv_file = export_dir / "posts_analysis_20240115_123000.csv"
        csv_file.unlink()
        
        result = load_export(export_dir)
        
        assert len(result) == 3
        assert "author" in result.columns
    
    def test_load_export_invalid_json(self, mock_streamlit, temp_data_dir):
        """Test handling of invalid JSON."""
        export_dir = Path(temp_data_dir) / "data" / "posts_3_2024-01-15_12-30"
        
        # Remove CSV and create invalid JSON
        csv_file = export_dir / "posts_analysis_20240115_123000.csv" 
        csv_file.unlink()
        
        json_file = export_dir / "linkedin_feed_20240115_123000.json"
        with open(json_file, 'w') as f:
            f.write("invalid json content")
        
        result = load_export(export_dir)
        assert result.is_empty()

class TestGetExportMetadata:
    """Test cases for get_export_metadata function."""
    
    def test_get_export_metadata_nonexistent(self, mock_streamlit):
        """Test metadata for non-existent directory."""
        result = get_export_metadata(Path("/nonexistent"))
        
        assert result["name"] == "nonexistent"
        assert result["created"] is None
        assert result["file_count"] == 0
    
    def test_get_export_metadata_success(self, mock_streamlit, temp_data_dir):
        """Test successful metadata extraction."""
        export_dir = Path(temp_data_dir) / "data" / "posts_3_2024-01-15_12-30"
        
        result = get_export_metadata(export_dir)
        
        assert result["name"] == "posts_3_2024-01-15_12-30"
        assert result["file_count"] == 2  # JSON and CSV files
        assert result["has_json"] is True
        assert result["has_csv"] is True
        assert result["post_count"] == 3  # Extracted from directory name

class TestValidateDataframe:
    """Test cases for validate_dataframe function."""
    
    def test_validate_dataframe_empty(self, mock_streamlit):
        """Test validation of empty DataFrame."""
        df = pl.DataFrame()
        result = validate_dataframe(df)
        
        assert result["is_valid"] is False
        assert "error" in result
    
    def test_validate_dataframe_missing_columns(self, mock_streamlit):
        """Test validation with missing required columns."""
        df = pl.DataFrame({"other_column": [1, 2, 3]})
        result = validate_dataframe(df)
        
        assert result["is_valid"] is False
        assert len(result["missing_columns"]) == 3  # author, content, urn
        assert result["row_count"] == 3
    
    def test_validate_dataframe_success(self, mock_streamlit, sample_dataframe):
        """Test validation of valid DataFrame."""
        result = validate_dataframe(sample_dataframe)
        
        assert result["is_valid"] is True
        assert len(result["missing_columns"]) == 0
        assert result["row_count"] == 3
        assert result["column_count"] == 8
        assert "data_quality" in result
    
    def test_validate_dataframe_data_quality_metrics(self, mock_streamlit, sample_dataframe):
        """Test data quality metrics calculation."""
        result = validate_dataframe(sample_dataframe)
        
        assert "avg_content_length" in result["data_quality"]
        assert "unique_authors" in result["data_quality"]
        assert result["data_quality"]["unique_authors"] == 3

# Integration tests
@pytest.mark.integration
class TestDataLoaderIntegration:
    """Integration tests for data loader functionality."""
    
    def test_full_workflow(self, mock_streamlit, temp_data_dir):
        """Test complete data loading workflow."""
        # Get export directories
        with patch('utils.data_loader.DATA_DIR', Path(temp_data_dir) / "data"):
            export_dirs = get_export_dirs()
            assert len(export_dirs) == 1
            
            # Load export
            df = load_export(export_dirs[0])
            assert len(df) == 3
            
            # Validate data
            validation = validate_dataframe(df)
            assert validation["is_valid"] is True
            
            # Get metadata
            metadata = get_export_metadata(export_dirs[0])
            assert metadata["post_count"] == 3

# Performance tests  
@pytest.mark.slow
class TestDataLoaderPerformance:
    """Performance tests for data loader."""
    
    def test_large_dataset_loading(self, mock_streamlit, sample_linkedin_data):
        """Test loading performance with larger dataset."""
        # Create larger dataset
        large_data = sample_linkedin_data * 1000  # 3000 posts
        
        with patch('polars.read_csv') as mock_read_csv:
            mock_read_csv.return_value = pl.DataFrame(large_data)
            
            # This should complete within reasonable time
            import time
            start = time.time()
            
            # Mock the loading process
            df = pl.DataFrame(large_data)
            validation = validate_dataframe(df)
            
            elapsed = time.time() - start
            
            assert elapsed < 5.0  # Should complete within 5 seconds
            assert validation["row_count"] == 3000 