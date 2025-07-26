#!/usr/bin/env python3
"""
RAG API Service - Production Ready

FastAPI-based RAG service with Ollama and Azure OpenAI support.
"""

import os
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path
import json

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

from rag.core.rag_manager import RAGManager, RAGQuery, RAGResponse
from rag.core.config import RAGConfig
from rag.api.health_api import HealthAPI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="LinkedIn Feed RAG API",
    description="Production-ready RAG service for LinkedIn post analysis",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global RAG manager instance
rag_manager: Optional[RAGManager] = None
health_api = HealthAPI()

# Pydantic models
class QueryRequest(BaseModel):
    query: str = Field(..., description="Search query")
    collection_name: Optional[str] = Field("linkedin_posts", description="Collection to search")
    max_results: Optional[int] = Field(10, description="Maximum number of results")

class IndexRequest(BaseModel):
    data_path: str = Field(..., description="Path to data directory")
    collection_name: Optional[str] = Field("linkedin_posts", description="Collection name")

class ConfigRequest(BaseModel):
    provider: str = Field(..., description="LLM provider: 'ollama' or 'azure'")
    model: Optional[str] = Field(None, description="Model name")
    temperature: Optional[float] = Field(0.1, description="Temperature for generation")
    max_tokens: Optional[int] = Field(2048, description="Maximum tokens")

class HealthResponse(BaseModel):
    status: str
    components: Dict[str, Any]
    timestamp: str

@app.on_event("startup")
async def startup_event():
    """Initialize RAG manager on startup."""
    global rag_manager
    
    try:
        # Load configuration from environment
        config = RAGConfig.from_env()
        
        # Initialize RAG manager
        rag_manager = RAGManager(config)
        await rag_manager.initialize()
        
        logger.info("✅ RAG API service started successfully")
        
    except Exception as e:
        logger.error(f"❌ Failed to initialize RAG manager: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    global rag_manager
    
    if rag_manager:
        await rag_manager.shutdown()
        logger.info("🔄 RAG API service shutdown complete")

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "LinkedIn Feed RAG API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    try:
        health_status = await health_api.get_health_status(rag_manager)
        return HealthResponse(
            status="healthy" if health_status["overall_status"] == "healthy" else "unhealthy",
            components=health_status["components"],
            timestamp=health_status["timestamp"]
        )
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return HealthResponse(
            status="unhealthy",
            components={"error": str(e)},
            timestamp=health_status.get("timestamp", "")
        )

@app.get("/ready")
async def readiness_check():
    """Readiness check endpoint."""
    if not rag_manager or not await rag_manager.is_ready():
        raise HTTPException(status_code=503, detail="Service not ready")
    return {"status": "ready"}

@app.post("/query")
async def query_rag(request: QueryRequest):
    """Query the RAG system."""
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        # Create RAG query
        rag_query = RAGQuery(
            query=request.query,
            collection_name=request.collection_name,
            max_results=request.max_results
        )
        
        # Execute query
        response = await rag_manager.query(rag_query)
        
        return {
            "query": request.query,
            "answer": response.answer,
            "sources": response.sources,
            "metadata": response.metadata
        }
        
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")

@app.post("/index")
async def index_data(request: IndexRequest, background_tasks: BackgroundTasks):
    """Index data from a directory."""
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        data_path = Path(request.data_path)
        if not data_path.exists():
            raise HTTPException(status_code=404, detail=f"Data path not found: {request.data_path}")
        
        # Start indexing in background
        background_tasks.add_task(
            rag_manager.index_dataframe,
            data_path,
            request.collection_name
        )
        
        return {
            "message": "Indexing started",
            "data_path": str(data_path),
            "collection": request.collection_name
        }
        
    except Exception as e:
        logger.error(f"Indexing failed: {e}")
        raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")

@app.get("/collections")
async def list_collections():
    """List available collections."""
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        collections = await rag_manager.get_collections()
        return {"collections": collections}
        
    except Exception as e:
        logger.error(f"Failed to list collections: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to list collections: {str(e)}")

@app.get("/collections/{collection_name}/stats")
async def get_collection_stats(collection_name: str):
    """Get collection statistics."""
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        stats = await rag_manager.get_collection_stats(collection_name)
        return {"collection": collection_name, "stats": stats}
        
    except Exception as e:
        logger.error(f"Failed to get collection stats: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get collection stats: {str(e)}")

@app.delete("/collections/{collection_name}")
async def delete_collection(collection_name: str):
    """Delete a collection."""
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        await rag_manager.delete_collection(collection_name)
        return {"message": f"Collection '{collection_name}' deleted successfully"}
        
    except Exception as e:
        logger.error(f"Failed to delete collection: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to delete collection: {str(e)}")

@app.post("/config")
async def update_config(request: ConfigRequest):
    """Update RAG configuration."""
    global rag_manager
    
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        # For now, return success without actually updating config
        # TODO: Implement proper configuration update mechanism
        logger.info(f"Config update requested: provider={request.provider}, model={request.model}, temperature={request.temperature}")
        
        return {
            "message": "Configuration update request received",
            "provider": request.provider,
            "model": request.model,
            "temperature": request.temperature,
            "max_tokens": request.max_tokens,
            "note": "Configuration updates will be implemented in a future version"
        }
        
    except Exception as e:
        logger.error(f"Failed to update config: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to update config: {str(e)}")

@app.get("/metrics")
async def get_metrics():
    """Get performance metrics."""
    if not rag_manager:
        raise HTTPException(status_code=503, detail="RAG service not initialized")
    
    try:
        metrics = await rag_manager.get_performance_metrics()
        return {"metrics": metrics}
        
    except Exception as e:
        logger.error(f"Failed to get metrics: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get metrics: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="info"
    ) 