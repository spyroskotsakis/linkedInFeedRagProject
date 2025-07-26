# retrievers — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/retrievers.html
**Word Count:** 66
**Links Count:** 74
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# `retrievers`\#

**Retrievers** provide an interface to search and retrieve relevant documents from a data source.

Retrievers abstract the logic of querying underlying data stores \(such as vector stores, search engines, or databases\) and returning documents most relevant to a user’s query. They are commonly used to power search, question answering, and RAG \(Retrieval-Augmented Generation\) workflows.

**Class hierarchy:**               BaseRetriever --> VectorStoreRetriever --> <name>Retriever  # Example: AzureAISearchRetriever     

**Main helpers:**               Document, Query     

**Classes**

[`retrievers.azure_ai_search.AzureAISearchRetriever`](https://python.langchain.com/api_reference/azure_ai/retrievers/langchain_azure_ai.retrievers.azure_ai_search.AzureAISearchRetriever.html#langchain_azure_ai.retrievers.azure_ai_search.AzureAISearchRetriever "langchain_azure_ai.retrievers.azure_ai_search.AzureAISearchRetriever") | Azure AI Search service retriever.   ---|---   [`retrievers.azure_ai_search.AzureCognitiveSearchRetriever`](https://python.langchain.com/api_reference/azure_ai/retrievers/langchain_azure_ai.retrievers.azure_ai_search.AzureCognitiveSearchRetriever.html#langchain_azure_ai.retrievers.azure_ai_search.AzureCognitiveSearchRetriever "langchain_azure_ai.retrievers.azure_ai_search.AzureCognitiveSearchRetriever") | Azure Cognitive Search service retriever.