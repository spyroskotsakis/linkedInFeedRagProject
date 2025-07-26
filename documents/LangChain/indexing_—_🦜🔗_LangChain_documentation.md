# indexing — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/indexing.html
**Word Count:** 97
**Links Count:** 114
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# `indexing`\#

Code to help indexing data into a vectorstore.

This package contains helper logic to help deal with indexing data into a vectorstore while avoiding duplicated content and over-writing content if it’s unchanged.

**Classes**

[`indexing.api.IndexingException`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.IndexingException.html#langchain_core.indexing.api.IndexingException "langchain_core.indexing.api.IndexingException") | Raised when an indexing operation fails.   ---|---   [`indexing.api.IndexingResult`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.IndexingResult.html#langchain_core.indexing.api.IndexingResult "langchain_core.indexing.api.IndexingResult") | Return a detailed a breakdown of the result of the indexing operation.   [`indexing.base.DeleteResponse`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.DeleteResponse.html#langchain_core.indexing.base.DeleteResponse "langchain_core.indexing.base.DeleteResponse") | A generic response for delete operation.   [`indexing.base.DocumentIndex`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.DocumentIndex.html#langchain_core.indexing.base.DocumentIndex "langchain_core.indexing.base.DocumentIndex") |    [`indexing.base.InMemoryRecordManager`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.InMemoryRecordManager.html#langchain_core.indexing.base.InMemoryRecordManager "langchain_core.indexing.base.InMemoryRecordManager")\(namespace\) | An in-memory record manager for testing purposes.   [`indexing.base.RecordManager`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.RecordManager.html#langchain_core.indexing.base.RecordManager "langchain_core.indexing.base.RecordManager")\(namespace\) | Abstract base class representing the interface for a record manager.   [`indexing.base.UpsertResponse`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.UpsertResponse.html#langchain_core.indexing.base.UpsertResponse "langchain_core.indexing.base.UpsertResponse") | A generic response for upsert operations.   [`indexing.in_memory.InMemoryDocumentIndex`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.in_memory.InMemoryDocumentIndex.html#langchain_core.indexing.in_memory.InMemoryDocumentIndex "langchain_core.indexing.in_memory.InMemoryDocumentIndex") |       **Functions**

[`indexing.api.aindex`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.aindex.html#langchain_core.indexing.api.aindex "langchain_core.indexing.api.aindex")\(docs\_source, ...\[, ...\]\) | Async index data from the loader into the vector store.   ---|---   [`indexing.api.index`](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.index.html#langchain_core.indexing.api.index "langchain_core.indexing.api.index")\(docs\_source, ...\[, ...\]\) | Index data from the loader into the vector store.