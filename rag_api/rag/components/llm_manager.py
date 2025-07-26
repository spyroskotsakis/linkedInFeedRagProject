"""
LLM Manager Component

Handles interactions with language models (Ollama, Azure OpenAI, etc.).
"""

import os
import aiohttp
import asyncio
import logging
import json
from typing import Dict, Any, List, Optional

# Set logging level to DEBUG
logging.getLogger(__name__).setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)

OLLAMA_URLS = [
    os.getenv('OLLAMA_BASE_URL', 'http://host.docker.internal:11434'),
    'http://172.17.0.1:11434',
    'http://host-gateway:11434'
]

async def get_working_ollama_url():
    for url in OLLAMA_URLS:
        try:
            async with aiohttp.ClientSession() as client:
                async with client.get(f"{url}/api/tags", timeout=5) as resp:
                    if resp.status == 200:
                        logger.info(f"Ollama endpoint {url} is reachable.")
                        return url
        except Exception as e:
            logger.warning(f"Ollama endpoint {url} not reachable: {e}")
            continue
    raise RuntimeError("No working Ollama endpoint found")

class LLMManager:
    """Manages language model interactions."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.provider = config.get("provider", "ollama")
        self.model = config.get("model", "mistral-nemo:12b")
        self.temperature = config.get("temperature", 0.1)
        self.max_tokens = config.get("max_tokens", 2048)
        self.base_url = None
        self._initialized = False
    
    async def initialize(self):
        """Initialize the LLM manager."""
        try:
            logger.info(f"Initializing LLM manager with provider: {self.provider}")
            
            if self.provider == "ollama":
                self.base_url = await get_working_ollama_url()
                logger.info(f"Using Ollama endpoint: {self.base_url}")
            else:
                self.base_url = self.config.get("base_url")
            
            self._initialized = True
            logger.info("LLM manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize LLM manager: {e}")
            raise
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate a response using the LLM."""
        logger.info(f"generate_response called with prompt length: {len(prompt)}")
        logger.info(f"Context length: {len(context) if context else 0}")
        logger.info(f"LLM manager initialized: {self._initialized}")
        logger.info(f"Provider: {self.provider}")
        
        if not self._initialized:
            raise RuntimeError("LLM manager not initialized")
        
        try:
            if self.provider == "ollama":
                # Prepare the full prompt with context
                if context:
                    full_prompt = f"""Based on the following documents, please answer this question: {prompt}

Context:
{context}

Please provide a helpful and specific answer based on the information in the context."""
                else:
                    full_prompt = prompt
                
                logger.info(f"Calling Ollama with model: {self.model}")
                logger.info(f"Full prompt length: {len(full_prompt)} characters")
                
                payload = {
                    "model": self.model,
                    "prompt": full_prompt,
                    "stream": False,
                    "options": {
                        "temperature": self.temperature,
                        "num_predict": self.max_tokens
                    }
                }
                async with aiohttp.ClientSession() as client:
                    async with client.post(f"{self.base_url}/api/generate", json=payload, timeout=30) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            logger.error(f"Ollama API error {response.status}: {error_text}")
                            raise Exception(f"Ollama API error: {response.status}")
                        result = await response.json()
                        response_text = result.get("response", "No response generated")
                        logger.info(f"Generated response length: {len(response_text)} characters")
                        return response_text
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
    
    async def generate_rag_response(self, query: str, retrieved_docs: List[Dict[str, Any]]) -> str:
        """Generate a RAG response based on retrieved documents."""
        print(f"DEBUG: generate_rag_response called with query: {query}")
        print(f"DEBUG: Number of retrieved docs: {len(retrieved_docs)}")
        print(f"DEBUG: LLM manager initialized: {self._initialized}")
        
        logger.info(f"generate_rag_response called with query: {query}")
        logger.info(f"Number of retrieved docs: {len(retrieved_docs)}")
        logger.info(f"LLM manager initialized: {self._initialized}")
        
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
            print(f"DEBUG: Prepared context length: {len(context)}")
            logger.info(f"Prepared context length: {len(context)}")
            
            # Generate response
            prompt = f"Based on the following documents, please answer this question: {query}"
            print(f"DEBUG: Prepared prompt: {prompt}")
            logger.info(f"Prepared prompt: {prompt}")
            
            print("DEBUG: Calling generate_response...")
            logger.info("Calling generate_response...")
            return await self.generate_response(prompt, context)
            
        except Exception as e:
            print(f"DEBUG: Failed to generate RAG response: {e}")
            logger.error(f"Failed to generate RAG response: {e}")
            logger.error(f"Error type: {type(e)}")
            import traceback
            logger.error(f"Traceback: {traceback.format_exc()}")
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