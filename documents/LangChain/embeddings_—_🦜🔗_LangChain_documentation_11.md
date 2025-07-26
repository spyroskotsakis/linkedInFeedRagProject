# embeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/embeddings.html
**Word Count:** 42
**Links Count:** 83
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# `embeddings`\#

**Embedding models** are wrappers around embedding models from different APIs and services.

**Embedding models** can be LLMs or not.

**Class hierarchy:**               Embeddings --> <name>Embeddings  # Examples: OpenAIEmbeddings, HuggingFaceEmbeddings     

**Classes**

[`embeddings.cache.CacheBackedEmbeddings`](https://python.langchain.com/api_reference/langchain/embeddings/langchain.embeddings.cache.CacheBackedEmbeddings.html#langchain.embeddings.cache.CacheBackedEmbeddings "langchain.embeddings.cache.CacheBackedEmbeddings")\(...\) | Interface for caching results from embedding models.   ---|---      **Functions**

[`embeddings.base.init_embeddings`](https://python.langchain.com/api_reference/langchain/embeddings/langchain.embeddings.base.init_embeddings.html#langchain.embeddings.base.init_embeddings "langchain.embeddings.base.init_embeddings")\(model, \*\[, ...\]\) | Initialize an embeddings model from a model name and optional provider.   ---|---