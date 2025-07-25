"""
LLM Provider Factory for switching between Ollama and Azure OpenAI.
"""

import os
import logging
from typing import Dict, Any, Optional, Union
import streamlit as st
from abc import ABC, abstractmethod

try:
    from langchain_openai import AzureChatOpenAI
    from langchain_community.llms import Ollama
    import ollama
except ImportError as e:
    st.error(f"Missing required dependencies: {e}")
    st.info("Please install: pip install langchain-openai langchain-community ollama")

logger = logging.getLogger(__name__)

class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if the provider is available and configured."""
        pass
    
    @abstractmethod
    def get_llm(self, **kwargs):
        """Get the LLM instance."""
        pass
    
    @abstractmethod
    def health_check(self) -> Dict[str, Any]:
        """Perform a health check on the provider."""
        pass

class OllamaProvider(LLMProvider):
    """Ollama local LLM provider."""
    
    def __init__(self, model: str = "mistral-nemo:12b", base_url: str = "http://127.0.0.1:11434"):
        self.model = model
        self.base_url = base_url
    
    def is_available(self) -> bool:
        """Check if Ollama is running and model is available."""
        try:
            models = ollama.list()
            available_models = [m["name"] for m in models.get("models", [])]
            return any(self.model in model_name for model_name in available_models)
        except Exception as e:
            logger.warning(f"Ollama not available: {e}")
            return False
    
    def get_llm(self, **kwargs):
        """Get Ollama LLM instance."""
        return Ollama(
            model=self.model,
            base_url=self.base_url,
            temperature=kwargs.get("temperature", 0.1),
            **kwargs
        )
    
    def health_check(self) -> Dict[str, Any]:
        """Perform health check on Ollama."""
        try:
            models = ollama.list()
            model_available = any(self.model in m["name"] for m in models.get("models", []))
            
            # Test generation
            if model_available:
                response = ollama.chat(
                    model=self.model,
                    messages=[{"role": "user", "content": "Hello"}],
                )
                success = bool(response.get("message", {}).get("content"))
            else:
                success = False
            
            return {
                "status": "healthy" if success else "unhealthy",
                "model": self.model,
                "base_url": self.base_url,
                "model_available": model_available,
                "response_test": success
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "model": self.model,
                "base_url": self.base_url
            }

class AzureOpenAIProvider(LLMProvider):
    """Azure OpenAI provider."""
    
    def __init__(self):
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    
    def is_available(self) -> bool:
        """Check if Azure OpenAI credentials are configured."""
        return bool(self.endpoint and self.api_key and self.deployment)
    
    def get_llm(self, **kwargs):
        """Get Azure OpenAI LLM instance."""
        if not self.is_available():
            raise ValueError("Azure OpenAI not properly configured. Check environment variables.")
        
        return AzureChatOpenAI(
            azure_endpoint=self.endpoint,
            azure_deployment=self.deployment,
            api_version=self.api_version,
            api_key=self.api_key,
            temperature=kwargs.get("temperature", 0.1),
            **kwargs
        )
    
    def health_check(self) -> Dict[str, Any]:
        """Perform health check on Azure OpenAI."""
        try:
            if not self.is_available():
                return {
                    "status": "misconfigured",
                    "error": "Missing required environment variables",
                    "required": ["AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_DEPLOYMENT"]
                }
            
            llm = self.get_llm()
            response = llm.invoke("Hello")
            
            return {
                "status": "healthy",
                "endpoint": self.endpoint,
                "deployment": self.deployment,
                "api_version": self.api_version,
                "response_test": bool(response.content if hasattr(response, 'content') else response)
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e),
                "endpoint": self.endpoint,
                "deployment": self.deployment
            }

class LLMProviderFactory:
    """Factory for creating and managing LLM providers."""
    
    def __init__(self):
        self.providers = {
            "ollama": OllamaProvider(),
            "azure": AzureOpenAIProvider()
        }
    
    def get_provider(self, provider_name: str) -> LLMProvider:
        """Get a provider instance."""
        if provider_name not in self.providers:
            raise ValueError(f"Unknown provider: {provider_name}. Available: {list(self.providers.keys())}")
        
        return self.providers[provider_name]
    
    def get_llm(self, provider_name: str, **kwargs):
        """Get an LLM instance from the specified provider."""
        provider = self.get_provider(provider_name)
        
        if not provider.is_available():
            raise ValueError(f"Provider {provider_name} is not available or not configured")
        
        return provider.get_llm(**kwargs)
    
    def get_available_providers(self) -> Dict[str, bool]:
        """Get availability status of all providers."""
        return {
            name: provider.is_available() 
            for name, provider in self.providers.items()
        }
    
    def health_check_all(self) -> Dict[str, Dict[str, Any]]:
        """Perform health check on all providers."""
        return {
            name: provider.health_check()
            for name, provider in self.providers.items()
        }

# Global factory instance
_factory = LLMProviderFactory()

def get_llm(provider: str = "ollama", **kwargs):
    """
    Convenience function to get an LLM instance.
    
    Args:
        provider: Provider name ("ollama" or "azure")
        **kwargs: Additional arguments for the LLM
        
    Returns:
        LLM instance
    """
    return _factory.get_llm(provider, **kwargs)

def check_ollama() -> bool:
    """
    Quick check if Ollama is available with mistral-nemo model.
    
    Returns:
        True if Ollama is available and configured
    """
    try:
        provider = _factory.get_provider("ollama")
        return provider.is_available()
    except Exception:
        return False

def get_provider_factory() -> LLMProviderFactory:
    """Get the global LLM provider factory instance."""
    return _factory

# Session state integration for Streamlit
def get_session_llm_config() -> Dict[str, Any]:
    """Get LLM configuration from Streamlit session state."""
    if "llm_config" not in st.session_state:
        st.session_state.llm_config = {
            "provider": "ollama",
            "temperature": 0.1,
            "max_tokens": 2048
        }
    return st.session_state.llm_config

def update_session_llm_config(config: Dict[str, Any]) -> None:
    """Update LLM configuration in session state."""
    st.session_state.llm_config.update(config)

def get_configured_llm():
    """Get LLM instance based on current session configuration."""
    config = get_session_llm_config()
    provider = config.pop("provider")
    return get_llm(provider, **config) 