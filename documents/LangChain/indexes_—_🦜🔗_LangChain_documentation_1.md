# indexes — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/indexes.html
**Word Count:** 78
**Links Count:** 83
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# `indexes`\#

**Index** is used to avoid writing duplicated content into the vectostore and to avoid over-writing content if it’s unchanged.

Indexes also :

  * Create knowledge graphs from data.

  * Support indexing workflows from LangChain data loaders to vectorstores.

Importantly, Index keeps on working even if the content being written is derived via a set of transformations from some source content \(e.g., indexing children documents that were derived from parent documents by chunking.\)

**Classes**

[`indexes.vectorstore.VectorStoreIndexWrapper`](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper") | Wrapper around a vectorstore for easy access.   ---|---   [`indexes.vectorstore.VectorstoreIndexCreator`](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html#langchain.indexes.vectorstore.VectorstoreIndexCreator "langchain.indexes.vectorstore.VectorstoreIndexCreator") | Logic for creating indexes.