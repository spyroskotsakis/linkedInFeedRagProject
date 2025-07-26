"""
LLM Manager Component

Handles interactions with language models (Ollama, Azure OpenAI, etc.).
"""

import logging
import httpx
import json
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)


class LLMManager:
    """Manages language model interactions."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.provider = config.get("provider", "ollama")
        self.model = config.get("model", "mistral-nemo:12b")
        self.base_url = config.get("base_url", "http://host.docker.internal:11434")
        self.temperature = config.get("temperature", 0.1)
        self.max_tokens = config.get("max_tokens", 2048)
        self._initialized = False
    
    async def initialize(self):
        """Initialize the LLM manager."""
        try:
            logger.info(f"Initializing LLM manager with provider: {self.provider}")
            
            if self.provider == "ollama":
                await self._check_ollama_health()
            
            self._initialized = True
            logger.info("LLM manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize LLM manager: {e}")
            raise
    
    async def _check_ollama_health(self):
        """Check if Ollama is running and model is available."""
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                # Check if Ollama is running
                response = await client.get(f"{self.base_url}/api/tags")
                if response.status_code != 200:
                    raise Exception("Ollama is not responding")
                
                # Check if model is available
                models = response.json().get("models", [])
                model_names = [model.get("name", "") for model in models]
                
                if self.model not in model_names:
                    logger.warning(f"Model {self.model} not found in Ollama. Available models: {model_names}")
                    # Use first available model as fallback
                    if model_names:
                        self.model = model_names[0]
                        logger.info(f"Using fallback model: {self.model}")
                    else:
                        raise Exception("No models available in Ollama")
                
        except Exception as e:
            logger.warning(f"Ollama health check failed: {e}")
            logger.warning("Will use fallback response generation")
            # Don't raise exception, just log warning
    
    async def generate_response(self, prompt: str, context: str = "") -> str:
        """Generate a response using the LLM."""
        if not self._initialized:
            raise RuntimeError("LLM manager not initialized")
        
        try:
            if self.provider == "ollama":
                return await self._generate_ollama_response(prompt, context)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
                
        except Exception as e:
            logger.warning(f"Failed to generate response with LLM: {e}")
            logger.warning("Using fallback response")
            # Return a fallback response
            if context:
                return f"Based on the provided context, here's what I found: {prompt}. The context contains relevant information that could help answer your question."
            else:
                return f"I understand you're asking about: {prompt}. However, I couldn't connect to the language model to provide a detailed response."
    
    async def _generate_ollama_response(self, prompt: str, context: str = "") -> str:
        """Generate response using Ollama."""
        try:
            # Prepare the full prompt with context
            if context:
                full_prompt = f"""Context: {context}

Question: {prompt}

Please provide a helpful answer based on the context provided. If the context doesn't contain relevant information, say so."""
            else:
                full_prompt = prompt
            
            # Prepare request payload
            payload = {
                "model": self.model,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": self.temperature,
                    "num_predict": self.max_tokens
                }
            }
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json=payload
                )
                
                if response.status_code != 200:
                    raise Exception(f"Ollama API error: {response.status_code}")
                
                result = response.json()
                return result.get("response", "No response generated")
                
        except Exception as e:
            logger.error(f"Ollama response generation failed: {e}")
            raise
    
    async def generate_rag_response(self, query: str, retrieved_docs: List[Dict[str, Any]]) -> str:
        """Generate a RAG response based on retrieved documents."""
        if not self._initialized:
            raise RuntimeError("LLM manager not initialized")
        
        try:
            # Prepare context from retrieved documents
            context_parts = []
            for i, doc in enumerate(retrieved_docs, 1):
                content = doc.get("content", "")
                metadata = doc.get("metadata", {})
                author = metadata.get("author", "Unknown")
                
                context_parts.append(f"Document {i} (by {author}): {content}")
            
            context = "\n\n".join(context_parts)
            
            # Generate response
            prompt = f"Based on the following documents, please answer this question: {query}"
            
            return await self.generate_response(prompt, context)
            
        except Exception as e:
            logger.error(f"Failed to generate RAG response: {e}")
            raise
    
    def get_stats(self) -> Dict[str, Any]:
        """Get LLM manager statistics."""
        return {
            "provider": self.provider,
            "model": self.model,
            "initialized": self._initialized,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        } 