# langchain-astradb: 0.6.1 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/index.html
**Word Count:** 116
**Links Count:** 94
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# langchain-astradb: 0.6.1\#

Astra DB integration for LangChain.

## [cache](https://python.langchain.com/api_reference/astradb/cache.html#langchain-astradb-cache)\#

**Classes**

[`cache.AstraDBCache`](https://python.langchain.com/api_reference/astradb/cache/langchain_astradb.cache.AstraDBCache.html#langchain_astradb.cache.AstraDBCache "langchain_astradb.cache.AstraDBCache")\(\*\[, collection\_name, ...\]\) | Cache that uses Astra DB as a backend.   ---|---   [`cache.AstraDBSemanticCache`](https://python.langchain.com/api_reference/astradb/cache/langchain_astradb.cache.AstraDBSemanticCache.html#langchain_astradb.cache.AstraDBSemanticCache "langchain_astradb.cache.AstraDBSemanticCache")\(\*\[, ...\]\) | Astra DB semantic cache.      ## [chat\_message\_histories](https://python.langchain.com/api_reference/astradb/chat_message_histories.html#langchain-astradb-chat-message-histories)\#

**Classes**

[`chat_message_histories.AstraDBChatMessageHistory`](https://python.langchain.com/api_reference/astradb/chat_message_histories/langchain_astradb.chat_message_histories.AstraDBChatMessageHistory.html#langchain_astradb.chat_message_histories.AstraDBChatMessageHistory "langchain_astradb.chat_message_histories.AstraDBChatMessageHistory")\(\*, ...\) | Chat message history that stores history in Astra DB.   ---|---      ## [document\_loaders](https://python.langchain.com/api_reference/astradb/document_loaders.html#langchain-astradb-document-loaders)\#

**Classes**

[`document_loaders.AstraDBLoader`](https://python.langchain.com/api_reference/astradb/document_loaders/langchain_astradb.document_loaders.AstraDBLoader.html#langchain_astradb.document_loaders.AstraDBLoader "langchain_astradb.document_loaders.AstraDBLoader")\(...\) | Load DataStax Astra DB documents.   ---|---      ## [storage](https://python.langchain.com/api_reference/astradb/storage.html#langchain-astradb-storage)\#

**Classes**

[`storage.AstraDBBaseStore`](https://python.langchain.com/api_reference/astradb/storage/langchain_astradb.storage.AstraDBBaseStore.html#langchain_astradb.storage.AstraDBBaseStore "langchain_astradb.storage.AstraDBBaseStore")\(\*args, \*\*kwargs\) | Base class for the DataStax Astra DB data store.   ---|---   [`storage.AstraDBByteStore`](https://python.langchain.com/api_reference/astradb/storage/langchain_astradb.storage.AstraDBByteStore.html#langchain_astradb.storage.AstraDBByteStore "langchain_astradb.storage.AstraDBByteStore")\(\*, collection\_name\) | ByteStore implementation using DataStax AstraDB as the underlying store.   [`storage.AstraDBStore`](https://python.langchain.com/api_reference/astradb/storage/langchain_astradb.storage.AstraDBStore.html#langchain_astradb.storage.AstraDBStore "langchain_astradb.storage.AstraDBStore")\(collection\_name, \*\[, ...\]\) | BaseStore implementation using DataStax AstraDB as the underlying store.      ## [utils](https://python.langchain.com/api_reference/astradb/utils.html#langchain-astradb-utils)\#

**Classes**

[`utils.astradb.AstraDBError`](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.AstraDBError.html#langchain_astradb.utils.astradb.AstraDBError "langchain_astradb.utils.astradb.AstraDBError") | An exception during Astra DB- \(Data API-\) related operations.   ---|---   [`utils.astradb.HybridSearchMode`](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.HybridSearchMode.html#langchain_astradb.utils.astradb.HybridSearchMode "langchain_astradb.utils.astradb.HybridSearchMode")\(value\) | Hybrid Search mode for a Vector Store collection.   [`utils.astradb.SetupMode`](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\(value\) | Setup mode for the Astra DB collection.      ## [vectorstores](https://python.langchain.com/api_reference/astradb/vectorstores.html#langchain-astradb-vectorstores)\#

**Classes**

[`vectorstores.AstraDBQueryResult`](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult")\(document, ...\) | The complete information contained in a vector store entry.   ---|---   [`vectorstores.AstraDBVectorStore`](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBVectorStore.html#langchain_astradb.vectorstores.AstraDBVectorStore "langchain_astradb.vectorstores.AstraDBVectorStore")\(\*, ...\[, ...\]\) | A vector store which uses DataStax Astra DB as backend.   [`vectorstores.AstraDBVectorStoreError`](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBVectorStoreError.html#langchain_astradb.vectorstores.AstraDBVectorStoreError "langchain_astradb.vectorstores.AstraDBVectorStoreError") | An exception during vector-store activities.   [`vectorstores.HybridLimitFactorPrescription`](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.HybridLimitFactorPrescription.html#langchain_astradb.vectorstores.HybridLimitFactorPrescription "langchain_astradb.vectorstores.HybridLimitFactorPrescription")\(...\) | A per-subsearch setting for the hybrid-search 'limit' factors.