"""
RAG Health Monitor Module

Health monitoring for RAG system components.
"""

import time
import asyncio
from dataclasses import dataclass
from typing import Dict, Any, List, Callable, Optional
from datetime import datetime


@dataclass
class HealthCheck:
    """Health check result."""
    name: str
    status: str  # "healthy", "unhealthy", "unknown"
    message: str
    details: Dict[str, Any] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
        if self.details is None:
            self.details = {}


@dataclass
class HealthStatus:
    """Overall health status."""
    overall_status: str
    components: Dict[str, HealthCheck]
    timestamp: datetime
    version: str = "1.0.0"


class RAGHealthMonitor:
    """Health monitor for RAG system."""
    
    def __init__(self):
        self.health_checks: Dict[str, Callable] = {}
        self.monitoring = False
        self._stop_monitoring = False
    
    def register_health_check(self, name: str, check_func: Callable):
        """Register a health check function."""
        self.health_checks[name] = check_func
    
    async def run_health_checks(self) -> Dict[str, HealthCheck]:
        """Run all registered health checks."""
        results = {}
        
        for name, check_func in self.health_checks.items():
            try:
                if asyncio.iscoroutinefunction(check_func):
                    result = await check_func()
                else:
                    result = check_func()
                
                if isinstance(result, HealthCheck):
                    results[name] = result
                else:
                    # Convert simple result to HealthCheck
                    status = "healthy" if result else "unhealthy"
                    results[name] = HealthCheck(
                        name=name,
                        status=status,
                        message=f"Health check {name} completed",
                        details={"result": result}
                    )
                    
            except Exception as e:
                results[name] = HealthCheck(
                    name=name,
                    status="unhealthy",
                    message=f"Health check failed: {str(e)}",
                    details={"error": str(e)}
                )
        
        return results
    
    async def get_health_status(self) -> HealthStatus:
        """Get overall health status."""
        components = await self.run_health_checks()
        
        # Determine overall status
        if not components:
            overall_status = "unknown"
        elif all(check.status == "healthy" for check in components.values()):
            overall_status = "healthy"
        elif any(check.status == "unhealthy" for check in components.values()):
            overall_status = "unhealthy"
        else:
            overall_status = "degraded"
        
        return HealthStatus(
            overall_status=overall_status,
            components=components,
            timestamp=datetime.now()
        )
    
    def start_monitoring(self, interval: int = 30):
        """Start background health monitoring."""
        if self.monitoring:
            return
        
        self.monitoring = True
        self._stop_monitoring = False
        
        async def monitoring_loop():
            while not self._stop_monitoring:
                try:
                    await self.run_health_checks()
                    await asyncio.sleep(interval)
                except Exception as e:
                    print(f"Health monitoring error: {e}")
                    await asyncio.sleep(interval)
        
        asyncio.create_task(monitoring_loop())
    
    def stop_monitoring(self):
        """Stop background health monitoring."""
        self._stop_monitoring = True
        self.monitoring = False 