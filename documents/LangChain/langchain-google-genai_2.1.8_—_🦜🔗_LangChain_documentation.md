# langchain-google-genai: 2.1.8 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_genai/index.html
**Word Count:** 219
**Links Count:** 87
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# langchain-google-genai: 2.1.8\#

**LangChain Google Generative AI Integration**

This module integrates Google’s Generative AI models, specifically the Gemini series, with the LangChain framework. It provides classes for interacting with chat models and generating embeddings, leveraging Google’s advanced AI capabilities.

**Chat Models**

The `ChatGoogleGenerativeAI` class is the primary interface for interacting with Google’s Gemini chat models. It allows users to send and receive messages using a specified Gemini model, suitable for various conversational AI applications.

**LLMs**

The `GoogleGenerativeAI` class is the primary interface for interacting with Google’s Gemini LLMs. It allows users to generate text using a specified Gemini model.

**Embeddings**

The `GoogleGenerativeAIEmbeddings` class provides functionalities to generate embeddings using Google’s models. These embeddings can be used for a range of NLP tasks, including semantic analysis, similarity comparisons, and more.

**Installation**

To install the package, use pip:

**Using Chat Models**

After setting up your environment with the required API key, you can interact with the Google Gemini models.               from langchain_google_genai import ChatGoogleGenerativeAI          llm = ChatGoogleGenerativeAI(model="gemini-pro")     llm.invoke("Sing a ballad of LangChain.")     

**Using LLMs**

The package also supports generating text with Google’s models.               from langchain_google_genai import GoogleGenerativeAI          llm = GoogleGenerativeAI(model="gemini-pro")     llm.invoke("Once upon a time, a library called LangChain")     

**Embedding Generation**

The package also supports creating embeddings with Google’s models, useful for textual similarity and other NLP applications.               from langchain_google_genai import GoogleGenerativeAIEmbeddings          embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")     embeddings.embed_query("hello, world!")     

## [chat\_models](https://python.langchain.com/api_reference/google_genai/chat_models.html#langchain-google-genai-chat-models)\#

**Classes**

[`chat_models.ChatGoogleGenerativeAI`](https://python.langchain.com/api_reference/google_genai/chat_models/langchain_google_genai.chat_models.ChatGoogleGenerativeAI.html#langchain_google_genai.chat_models.ChatGoogleGenerativeAI "langchain_google_genai.chat_models.ChatGoogleGenerativeAI") | Google AI chat models integration.   ---|---   [`chat_models.ChatGoogleGenerativeAIError`](https://python.langchain.com/api_reference/google_genai/chat_models/langchain_google_genai.chat_models.ChatGoogleGenerativeAIError.html#langchain_google_genai.chat_models.ChatGoogleGenerativeAIError "langchain_google_genai.chat_models.ChatGoogleGenerativeAIError") | Custom exception class for errors associated with the Google GenAI API.      ## [embeddings](https://python.langchain.com/api_reference/google_genai/embeddings.html#langchain-google-genai-embeddings)\#

**Classes**

[`embeddings.GoogleGenerativeAIEmbeddings`](https://python.langchain.com/api_reference/google_genai/embeddings/langchain_google_genai.embeddings.GoogleGenerativeAIEmbeddings.html#langchain_google_genai.embeddings.GoogleGenerativeAIEmbeddings "langchain_google_genai.embeddings.GoogleGenerativeAIEmbeddings") | Google Generative AI Embeddings.   ---|---      ## [genai\_aqa](https://python.langchain.com/api_reference/google_genai/genai_aqa.html#langchain-google-genai-genai-aqa)\#

**Classes**

[`genai_aqa.AqaInput`](https://python.langchain.com/api_reference/google_genai/genai_aqa/langchain_google_genai.genai_aqa.AqaInput.html#langchain_google_genai.genai_aqa.AqaInput "langchain_google_genai.genai_aqa.AqaInput") | Input to GenAIAqa.invoke.   ---|---   [`genai_aqa.AqaOutput`](https://python.langchain.com/api_reference/google_genai/genai_aqa/langchain_google_genai.genai_aqa.AqaOutput.html#langchain_google_genai.genai_aqa.AqaOutput "langchain_google_genai.genai_aqa.AqaOutput") | Output from GenAIAqa.invoke.   [`genai_aqa.GenAIAqa`](https://python.langchain.com/api_reference/google_genai/genai_aqa/langchain_google_genai.genai_aqa.GenAIAqa.html#langchain_google_genai.genai_aqa.GenAIAqa "langchain_google_genai.genai_aqa.GenAIAqa") | Google's Attributed Question and Answering service.      ## [google\_vector\_store](https://python.langchain.com/api_reference/google_genai/google_vector_store.html#langchain-google-genai-google-vector-store)\#

**Classes**

[`google_vector_store.DoesNotExistsException`](https://python.langchain.com/api_reference/google_genai/google_vector_store/langchain_google_genai.google_vector_store.DoesNotExistsException.html#langchain_google_genai.google_vector_store.DoesNotExistsException "langchain_google_genai.google_vector_store.DoesNotExistsException")\(\*, ...\) |    ---|---   [`google_vector_store.GoogleVectorStore`](https://python.langchain.com/api_reference/google_genai/google_vector_store/langchain_google_genai.google_vector_store.GoogleVectorStore.html#langchain_google_genai.google_vector_store.GoogleVectorStore "langchain_google_genai.google_vector_store.GoogleVectorStore")\(\*, ...\) | Google GenerativeAI Vector Store.   [`google_vector_store.ServerSideEmbedding`](https://python.langchain.com/api_reference/google_genai/google_vector_store/langchain_google_genai.google_vector_store.ServerSideEmbedding.html#langchain_google_genai.google_vector_store.ServerSideEmbedding "langchain_google_genai.google_vector_store.ServerSideEmbedding")\(\) | Do nothing embedding model where the embedding is done by the server.      ## [llms](https://python.langchain.com/api_reference/google_genai/llms.html#langchain-google-genai-llms)\#

**Classes**

[`llms.GoogleGenerativeAI`](https://python.langchain.com/api_reference/google_genai/llms/langchain_google_genai.llms.GoogleGenerativeAI.html#langchain_google_genai.llms.GoogleGenerativeAI "langchain_google_genai.llms.GoogleGenerativeAI") | Google GenerativeAI models.   ---|---