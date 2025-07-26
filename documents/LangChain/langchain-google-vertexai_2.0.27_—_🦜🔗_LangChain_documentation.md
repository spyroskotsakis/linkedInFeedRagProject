# langchain-google-vertexai: 2.0.27 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/index.html
**Word Count:** 409
**Links Count:** 138
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# langchain-google-vertexai: 2.0.27\#

**LangChain Google Generative AI Integration**

This module contains the LangChain integrations for Vertex AI service - Google foundational models, third-party foundational modela available on Vertex Model Garden and.

**Supported integrations**

  1. Google’s foundational models: `Gemini` family, `Codey`, embeddings - `ChatVertexAI`, `VertexAI`, `VertexAIEmbeddings`.

  2. Other Google’s foundational models: Imagen - `VertexAIImageCaptioning`, `VertexAIImageCaptioningChat`, `VertexAIImageEditorChat`, `VertexAIImageGeneratorChat`, `VertexAIVisualQnAChat`.

  3. Third-party foundational models available as a an API \(mdel-as-a-service\) on Vertex Model Garden \(Mistral, Llama, Anthropic\) - `model_garden.ChatAnthropicVertex`, `model_garden_maas.VertexModelGardenLlama`, `model_garden_maas.VertexModelGardenMistral`.

  4. Third-party foundational models deployed on Vertex AI endpoints from Vertex Model Garden or Huggingface - `VertexAIModelGarden`.

  5. Gemma deployed on Vertex AI endpoints or locally - `GemmaChatLocalHF`, `GemmaChatLocalKaggle`, `GemmaChatVertexAIModelGarden`, `GemmaLocalHF`, `GemmaLocalKaggle`, `GemmaVertexAIModelGarden`.

  6. Vector Search on Vertex AI - `VectorSearchVectorStore`, `VectorSearchVectorStoreDatastore`, `VectorSearchVectorStoreGCS`.

  7. Vertex AI evaluators for generative AI - `VertexPairWiseStringEvaluator`, `VertexStringEvaluator`.

Take a look at detailed documentation for each class for further details.

**Installation**

You need to enable required Google Cloud APIs \(depending on the integration you’re using\) and set up credentials by either:     

  * Having credentials configured for your environment \(gcloud, workload identity, etc…\)

  * Storing the path to a service account JSON file as the `GOOGLE_APPLICATION_CREDENTIALS` environment variable

This codebase uses the `google.auth` library which first looks for the application credentials variable mentioned above, and then looks for system-level auth.

**More information:**

  * [Credential types](https://cloud.google.com/docs/authentication/application-default-credentials#GAC)

  * `google.auth` [API reference](https://googleapis.dev/python/google-auth/latest/reference/google.auth.html#module-google.auth)

## [callbacks](https://python.langchain.com/api_reference/google_vertexai/callbacks.html#langchain-google-vertexai-callbacks)\#

**Classes**

[`callbacks.VertexAICallbackHandler`](https://python.langchain.com/api_reference/google_vertexai/callbacks/langchain_google_vertexai.callbacks.VertexAICallbackHandler.html#langchain_google_vertexai.callbacks.VertexAICallbackHandler "langchain_google_vertexai.callbacks.VertexAICallbackHandler")\(\) | Callback Handler that tracks VertexAI info.   ---|---      ## [chains](https://python.langchain.com/api_reference/google_vertexai/chains.html#langchain-google-vertexai-chains)\#

**Functions**

[`chains.create_structured_runnable`](https://python.langchain.com/api_reference/google_vertexai/chains/langchain_google_vertexai.chains.create_structured_runnable.html#langchain_google_vertexai.chains.create_structured_runnable "langchain_google_vertexai.chains.create_structured_runnable")\(function, ...\) | Create a runnable sequence that uses OpenAI functions.   ---|---   [`chains.get_output_parser`](https://python.langchain.com/api_reference/google_vertexai/chains/langchain_google_vertexai.chains.get_output_parser.html#langchain_google_vertexai.chains.get_output_parser "langchain_google_vertexai.chains.get_output_parser")\(functions\) | Get the appropriate function output parser given the user functions.      ## [chat\_models](https://python.langchain.com/api_reference/google_vertexai/chat_models.html#langchain-google-vertexai-chat-models)\#

**Classes**

[`chat_models.ChatVertexAI`](https://python.langchain.com/api_reference/google_vertexai/chat_models/langchain_google_vertexai.chat_models.ChatVertexAI.html#langchain_google_vertexai.chat_models.ChatVertexAI "langchain_google_vertexai.chat_models.ChatVertexAI") | Google Cloud Vertex AI chat model integration.   ---|---      ## [embeddings](https://python.langchain.com/api_reference/google_vertexai/embeddings.html#langchain-google-vertexai-embeddings)\#

**Classes**

[`embeddings.GoogleEmbeddingModelType`](https://python.langchain.com/api_reference/google_vertexai/embeddings/langchain_google_vertexai.embeddings.GoogleEmbeddingModelType.html#langchain_google_vertexai.embeddings.GoogleEmbeddingModelType "langchain_google_vertexai.embeddings.GoogleEmbeddingModelType")\(value\) |    ---|---   [`embeddings.GoogleEmbeddingModelVersion`](https://python.langchain.com/api_reference/google_vertexai/embeddings/langchain_google_vertexai.embeddings.GoogleEmbeddingModelVersion.html#langchain_google_vertexai.embeddings.GoogleEmbeddingModelVersion "langchain_google_vertexai.embeddings.GoogleEmbeddingModelVersion")\(value\) |    [`embeddings.VertexAIEmbeddings`](https://python.langchain.com/api_reference/google_vertexai/embeddings/langchain_google_vertexai.embeddings.VertexAIEmbeddings.html#langchain_google_vertexai.embeddings.VertexAIEmbeddings "langchain_google_vertexai.embeddings.VertexAIEmbeddings") | Google Cloud VertexAI embedding models.      ## [evaluators](https://python.langchain.com/api_reference/google_vertexai/evaluators.html#langchain-google-vertexai-evaluators)\#

**Classes**

[`evaluators.evaluation.VertexPairWiseStringEvaluator`](https://python.langchain.com/api_reference/google_vertexai/evaluators/langchain_google_vertexai.evaluators.evaluation.VertexPairWiseStringEvaluator.html#langchain_google_vertexai.evaluators.evaluation.VertexPairWiseStringEvaluator "langchain_google_vertexai.evaluators.evaluation.VertexPairWiseStringEvaluator")\(...\) | Evaluate the perplexity of a predicted string.   ---|---   [`evaluators.evaluation.VertexStringEvaluator`](https://python.langchain.com/api_reference/google_vertexai/evaluators/langchain_google_vertexai.evaluators.evaluation.VertexStringEvaluator.html#langchain_google_vertexai.evaluators.evaluation.VertexStringEvaluator "langchain_google_vertexai.evaluators.evaluation.VertexStringEvaluator")\(...\) | Evaluate the perplexity of a predicted string.      ## [functions\_utils](https://python.langchain.com/api_reference/google_vertexai/functions_utils.html#langchain-google-vertexai-functions-utils)\#

**Classes**

[`functions_utils.PydanticFunctionsOutputParser`](https://python.langchain.com/api_reference/google_vertexai/functions_utils/langchain_google_vertexai.functions_utils.PydanticFunctionsOutputParser.html#langchain_google_vertexai.functions_utils.PydanticFunctionsOutputParser "langchain_google_vertexai.functions_utils.PydanticFunctionsOutputParser") | Parse an output as a pydantic object.   ---|---      ## [gemma](https://python.langchain.com/api_reference/google_vertexai/gemma.html#langchain-google-vertexai-gemma)\#

**Classes**

[`gemma.GemmaChatLocalHF`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.GemmaChatLocalHF.html#langchain_google_vertexai.gemma.GemmaChatLocalHF "langchain_google_vertexai.gemma.GemmaChatLocalHF") |    ---|---   [`gemma.GemmaChatLocalKaggle`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.GemmaChatLocalKaggle.html#langchain_google_vertexai.gemma.GemmaChatLocalKaggle "langchain_google_vertexai.gemma.GemmaChatLocalKaggle") | Needed for mypy typing to recognize model\_name as a valid arg.   [`gemma.GemmaChatVertexAIModelGarden`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.GemmaChatVertexAIModelGarden.html#langchain_google_vertexai.gemma.GemmaChatVertexAIModelGarden "langchain_google_vertexai.gemma.GemmaChatVertexAIModelGarden") | Needed for mypy typing to recognize model\_name as a valid arg.   [`gemma.GemmaLocalHF`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.GemmaLocalHF.html#langchain_google_vertexai.gemma.GemmaLocalHF "langchain_google_vertexai.gemma.GemmaLocalHF") | Local gemma model loaded from HuggingFace.   [`gemma.GemmaLocalKaggle`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.GemmaLocalKaggle.html#langchain_google_vertexai.gemma.GemmaLocalKaggle "langchain_google_vertexai.gemma.GemmaLocalKaggle") | Local gemma chat model loaded from Kaggle.   [`gemma.GemmaVertexAIModelGarden`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.GemmaVertexAIModelGarden.html#langchain_google_vertexai.gemma.GemmaVertexAIModelGarden "langchain_google_vertexai.gemma.GemmaVertexAIModelGarden") | Create a new model by parsing and validating input data from keyword arguments.      **Functions**

[`gemma.gemma_messages_to_prompt`](https://python.langchain.com/api_reference/google_vertexai/gemma/langchain_google_vertexai.gemma.gemma_messages_to_prompt.html#langchain_google_vertexai.gemma.gemma_messages_to_prompt "langchain_google_vertexai.gemma.gemma_messages_to_prompt")\(history\) | Converts a list of messages to a chat prompt for Gemma.   ---|---      ## [llms](https://python.langchain.com/api_reference/google_vertexai/llms.html#langchain-google-vertexai-llms)\#

**Classes**

[`llms.VertexAI`](https://python.langchain.com/api_reference/google_vertexai/llms/langchain_google_vertexai.llms.VertexAI.html#langchain_google_vertexai.llms.VertexAI "langchain_google_vertexai.llms.VertexAI") | Google Vertex AI large language models.   ---|---      ## [model\_garden](https://python.langchain.com/api_reference/google_vertexai/model_garden.html#langchain-google-vertexai-model-garden)\#

**Classes**

[`model_garden.CacheUsageMetadata`](https://python.langchain.com/api_reference/google_vertexai/model_garden/langchain_google_vertexai.model_garden.CacheUsageMetadata.html#langchain_google_vertexai.model_garden.CacheUsageMetadata "langchain_google_vertexai.model_garden.CacheUsageMetadata") |    ---|---   [`model_garden.ChatAnthropicVertex`](https://python.langchain.com/api_reference/google_vertexai/model_garden/langchain_google_vertexai.model_garden.ChatAnthropicVertex.html#langchain_google_vertexai.model_garden.ChatAnthropicVertex "langchain_google_vertexai.model_garden.ChatAnthropicVertex") | Create a new model by parsing and validating input data from keyword arguments.   [`model_garden.VertexAIModelGarden`](https://python.langchain.com/api_reference/google_vertexai/model_garden/langchain_google_vertexai.model_garden.VertexAIModelGarden.html#langchain_google_vertexai.model_garden.VertexAIModelGarden "langchain_google_vertexai.model_garden.VertexAIModelGarden") | Large language models served from Vertex AI Model Garden.      ## [model\_garden\_maas](https://python.langchain.com/api_reference/google_vertexai/model_garden_maas.html#langchain-google-vertexai-model-garden-maas)\#

**Classes**

[`model_garden_maas.llama.VertexModelGardenLlama`](https://python.langchain.com/api_reference/google_vertexai/model_garden_maas/langchain_google_vertexai.model_garden_maas.llama.VertexModelGardenLlama.html#langchain_google_vertexai.model_garden_maas.llama.VertexModelGardenLlama "langchain_google_vertexai.model_garden_maas.llama.VertexModelGardenLlama") | Integration for Llama 3.1 on Google Cloud Vertex AI Model-as-a-Service.   ---|---   [`model_garden_maas.mistral.VertexModelGardenMistral`](https://python.langchain.com/api_reference/google_vertexai/model_garden_maas/langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral.html#langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral "langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral") | Create a new model by parsing and validating input data from keyword arguments.      ## [utils](https://python.langchain.com/api_reference/google_vertexai/utils.html#langchain-google-vertexai-utils)\#

**Functions**

[`utils.create_context_cache`](https://python.langchain.com/api_reference/google_vertexai/utils/langchain_google_vertexai.utils.create_context_cache.html#langchain_google_vertexai.utils.create_context_cache "langchain_google_vertexai.utils.create_context_cache")\(model, messages\) | Creates a cache for content in some model.   ---|---      ## [vectorstores](https://python.langchain.com/api_reference/google_vertexai/vectorstores.html#langchain-google-vertexai-vectorstores)\#

**Classes**

[`vectorstores.document_storage.DataStoreDocumentStorage`](https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.document_storage.DataStoreDocumentStorage.html#langchain_google_vertexai.vectorstores.document_storage.DataStoreDocumentStorage "langchain_google_vertexai.vectorstores.document_storage.DataStoreDocumentStorage")\(...\) | Stores documents in Google Cloud DataStore.   ---|---   [`vectorstores.document_storage.DocumentStorage`](https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.document_storage.DocumentStorage.html#langchain_google_vertexai.vectorstores.document_storage.DocumentStorage "langchain_google_vertexai.vectorstores.document_storage.DocumentStorage")\(\) | Abstract interface of a key, text storage for retrieving documents.   [`vectorstores.document_storage.GCSDocumentStorage`](https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.document_storage.GCSDocumentStorage.html#langchain_google_vertexai.vectorstores.document_storage.GCSDocumentStorage "langchain_google_vertexai.vectorstores.document_storage.GCSDocumentStorage")\(bucket\) | Stores documents in Google Cloud Storage.   [`vectorstores.vectorstores.VectorSearchVectorStore`](https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStore.html#langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStore "langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStore")\(...\) | VertexAI VectorStore that handles the search and indexing using Vector Search and stores the documents in Google Cloud Storage.   [`vectorstores.vectorstores.VectorSearchVectorStoreDatastore`](https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStoreDatastore.html#langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStoreDatastore "langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStoreDatastore")\(...\) | VectorSearch with DatasTore document storage.   [`vectorstores.vectorstores.VectorSearchVectorStoreGCS`](https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStoreGCS.html#langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStoreGCS "langchain_google_vertexai.vectorstores.vectorstores.VectorSearchVectorStoreGCS")\(...\) | Alias of VectorSearchVectorStore for consistency with the rest of vector stores with different document storage backends.      ## [vision\_models](https://python.langchain.com/api_reference/google_vertexai/vision_models.html#langchain-google-vertexai-vision-models)\#

**Classes**

[`vision_models.VertexAIImageCaptioning`](https://python.langchain.com/api_reference/google_vertexai/vision_models/langchain_google_vertexai.vision_models.VertexAIImageCaptioning.html#langchain_google_vertexai.vision_models.VertexAIImageCaptioning "langchain_google_vertexai.vision_models.VertexAIImageCaptioning") | Implementation of the Image Captioning model as an LLM.   ---|---   [`vision_models.VertexAIImageCaptioningChat`](https://python.langchain.com/api_reference/google_vertexai/vision_models/langchain_google_vertexai.vision_models.VertexAIImageCaptioningChat.html#langchain_google_vertexai.vision_models.VertexAIImageCaptioningChat "langchain_google_vertexai.vision_models.VertexAIImageCaptioningChat") | Implementation of the Image Captioning model as a chat.   [`vision_models.VertexAIImageEditorChat`](https://python.langchain.com/api_reference/google_vertexai/vision_models/langchain_google_vertexai.vision_models.VertexAIImageEditorChat.html#langchain_google_vertexai.vision_models.VertexAIImageEditorChat "langchain_google_vertexai.vision_models.VertexAIImageEditorChat") | Given an image and a prompt, edits the image.   [`vision_models.VertexAIImageGeneratorChat`](https://python.langchain.com/api_reference/google_vertexai/vision_models/langchain_google_vertexai.vision_models.VertexAIImageGeneratorChat.html#langchain_google_vertexai.vision_models.VertexAIImageGeneratorChat "langchain_google_vertexai.vision_models.VertexAIImageGeneratorChat") | Generates an image from a prompt.   [`vision_models.VertexAIVisualQnAChat`](https://python.langchain.com/api_reference/google_vertexai/vision_models/langchain_google_vertexai.vision_models.VertexAIVisualQnAChat.html#langchain_google_vertexai.vision_models.VertexAIVisualQnAChat "langchain_google_vertexai.vision_models.VertexAIVisualQnAChat") | Chat implementation of a visual QnA model