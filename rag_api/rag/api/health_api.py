"""
Health API Module

Health monitoring endpoints for the RAG system.
"""

import asyncio
from typing import Dict, Any, Optional
from datetime import datetime

from ..core.rag_manager import RAGManager


class HealthAPI:
    """Health monitoring API for RAG system."""
    
    async def get_health_status(self, rag_manager: Optional[RAGManager] = None) -> Dict[str, Any]:
        """Get comprehensive health status."""
        try:
            # Basic system health
            health_status = {
                "overall_status": "healthy",
                "components": {},
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0"
            }
            
            # RAG Manager health
            if rag_manager:
                try:
                    rag_health = await rag_manager.get_health_status()
                    health_status["components"]["rag_manager"] = {
                        "status": rag_health.get("status", "unknown"),
                        "details": rag_health
                    }
                except Exception as e:
                    health_status["components"]["rag_manager"] = {
                        "status": "unhealthy",
                        "error": str(e)
                    }
            else:
                health_status["components"]["rag_manager"] = {
                    "status": "not_initialized",
                    "message": "RAG manager not available"
                }
            
            # System readiness
            if rag_manager:
                try:
                    is_ready = await rag_manager.is_ready()
                    health_status["components"]["system_ready"] = {
                        "status": "healthy" if is_ready else "unhealthy",
                        "ready": is_ready
                    }
                except Exception as e:
                    health_status["components"]["system_ready"] = {
                        "status": "unhealthy",
                        "error": str(e)
                    }
            
            # Determine overall status
            component_statuses = [
                comp.get("status", "unknown") 
                for comp in health_status["components"].values()
            ]
            
            if all(status == "healthy" for status in component_statuses):
                health_status["overall_status"] = "healthy"
            elif any(status == "unhealthy" for status in component_statuses):
                health_status["overall_status"] = "unhealthy"
            else:
                health_status["overall_status"] = "degraded"
            
            return health_status
            
        except Exception as e:
            return {
                "overall_status": "unhealthy",
                "components": {"health_check": {"status": "unhealthy", "error": str(e)}},
                "timestamp": datetime.now().isoformat(),
                "version": "1.0.0"
            }
    
    async def check_system_ready(self, rag_manager: Optional[RAGManager] = None) -> Dict[str, Any]:
        """Check if the system is ready to handle requests."""
        try:
            if not rag_manager:
                return {"ready": False, "reason": "RAG manager not initialized"}
            
            is_ready = await rag_manager.is_ready()
            return {
                "ready": is_ready,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "ready": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    async def get_performance_metrics(self, rag_manager: Optional[RAGManager] = None) -> Dict[str, Any]:
        """Get performance metrics."""
        try:
            if not rag_manager:
                return {"error": "RAG manager not available"}
            
            metrics = await rag_manager.get_performance_metrics()
            return {
                "metrics": metrics,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            } 