# langchain-nvidia-ai-endpoints: 0.3.12 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/nvidia_ai_endpoints/index.html
**Word Count:** 271
**Links Count:** 94
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# langchain-nvidia-ai-endpoints: 0.3.12\#

**NOTE: You can \`import langchain\_nvidia\` instead.**

**LangChain NVIDIA AI Foundation Model Playground Integration**

This comprehensive module integrates NVIDIA’s state-of-the-art AI Foundation Models, featuring advanced models for conversational AI and semantic embeddings, into the LangChain framework. It provides robust classes for seamless interaction with NVIDIA’s AI models, particularly tailored for enriching conversational experiences and enhancing semantic understanding in various applications.

**Features:**

  1. **Chat Models \(\`ChatNVIDIA\`\):** This class serves as the primary interface for interacting with NVIDIA’s Foundation chat models. Users can effortlessly utilize NVIDIA’s advanced models like ‘Mistral’ to engage in rich, context-aware conversations, applicable across diverse domains from customer support to interactive storytelling.

  2. **Semantic Embeddings \(\`NVIDIAEmbeddings\`\):** The module offers capabilities to generate sophisticated embeddings using NVIDIA’s AI models. These embeddings are instrumental for tasks like semantic analysis, text similarity assessments, and contextual understanding, significantly enhancing the depth of NLP applications.

**Installation:**

Install this module easily using pip:

``python pip install langchain-nvidia-ai-endpoints ``

\#\# Utilizing Chat Models:

After setting up the environment, interact with NVIDIA AI Foundation models: \`\`\`python from langchain\_nvidia\_ai\_endpoints import ChatNVIDIA

ai\_chat\_model = ChatNVIDIA\(model=”meta/llama2-70b”\) response = ai\_chat\_model.invoke\(“Tell me about the LangChain integration.”\) \`\`\`

\# Generating Semantic Embeddings:

Use NVIDIA’s models for creating embeddings, useful in various NLP tasks:

\`\`\`python from langchain\_nvidia\_ai\_endpoints import NVIDIAEmbeddings

embed\_model = NVIDIAEmbeddings\(model=”nvolveqa\_40k”\) embedding\_output = embed\_model.embed\_query\(“Exploring AI capabilities.”\) \`\`\`

## [callbacks](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks.html#langchain-nvidia-ai-endpoints-callbacks)\#

**Classes**

[`callbacks.UsageCallbackHandler`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler.html#langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler "langchain_nvidia_ai_endpoints.callbacks.UsageCallbackHandler")\(\) | Callback Handler that tracks OpenAI info.   ---|---      **Functions**

[`callbacks.get_token_cost_for_model`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model.html#langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model "langchain_nvidia_ai_endpoints.callbacks.get_token_cost_for_model")\(...\[, ...\]\) | Get the cost in USD for a given model and number of tokens.   ---|---   [`callbacks.get_usage_callback`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.get_usage_callback.html#langchain_nvidia_ai_endpoints.callbacks.get_usage_callback "langchain_nvidia_ai_endpoints.callbacks.get_usage_callback")\(\[price\_map, ...\]\) | Get the OpenAI callback handler in a context manager.   [`callbacks.standardize_model_name`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/callbacks/langchain_nvidia_ai_endpoints.callbacks.standardize_model_name.html#langchain_nvidia_ai_endpoints.callbacks.standardize_model_name "langchain_nvidia_ai_endpoints.callbacks.standardize_model_name")\(model\_name\) | Standardize the model name to a format that can be used in the OpenAI API.      ## [chat\_models](https://python.langchain.com/api_reference/nvidia_ai_endpoints/chat_models.html#langchain-nvidia-ai-endpoints-chat-models)\#

**Classes**

[`chat_models.ChatNVIDIA`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/chat_models/langchain_nvidia_ai_endpoints.chat_models.ChatNVIDIA.html#langchain_nvidia_ai_endpoints.chat_models.ChatNVIDIA "langchain_nvidia_ai_endpoints.chat_models.ChatNVIDIA") | NVIDIA chat model.   ---|---      ## [embeddings](https://python.langchain.com/api_reference/nvidia_ai_endpoints/embeddings.html#langchain-nvidia-ai-endpoints-embeddings)\#

**Classes**

[`embeddings.NVIDIAEmbeddings`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/embeddings/langchain_nvidia_ai_endpoints.embeddings.NVIDIAEmbeddings.html#langchain_nvidia_ai_endpoints.embeddings.NVIDIAEmbeddings "langchain_nvidia_ai_endpoints.embeddings.NVIDIAEmbeddings") | Client to NVIDIA embeddings models.   ---|---      ## [llm](https://python.langchain.com/api_reference/nvidia_ai_endpoints/llm.html#langchain-nvidia-ai-endpoints-llm)\#

**Classes**

[`llm.NVIDIA`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/llm/langchain_nvidia_ai_endpoints.llm.NVIDIA.html#langchain_nvidia_ai_endpoints.llm.NVIDIA "langchain_nvidia_ai_endpoints.llm.NVIDIA") | LangChain LLM that uses the Completions API with NVIDIA NIMs.   ---|---      ## [reranking](https://python.langchain.com/api_reference/nvidia_ai_endpoints/reranking.html#langchain-nvidia-ai-endpoints-reranking)\#

**Classes**

[`reranking.NVIDIARerank`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/reranking/langchain_nvidia_ai_endpoints.reranking.NVIDIARerank.html#langchain_nvidia_ai_endpoints.reranking.NVIDIARerank "langchain_nvidia_ai_endpoints.reranking.NVIDIARerank") | LangChain Document Compressor that uses the NVIDIA NeMo Retriever Reranking API.   ---|---   [`reranking.Ranking`](https://python.langchain.com/api_reference/nvidia_ai_endpoints/reranking/langchain_nvidia_ai_endpoints.reranking.Ranking.html#langchain_nvidia_ai_endpoints.reranking.Ranking "langchain_nvidia_ai_endpoints.reranking.Ranking") | Create a new model by parsing and validating input data from keyword arguments.