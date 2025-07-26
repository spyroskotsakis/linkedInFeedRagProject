# indexes — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/indexes.html
**Word Count:** 75
**Links Count:** 94
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# `indexes`\#

**Index** is used to avoid writing duplicated content into the vectostore and to avoid over-writing content if it’s unchanged.

Indexes also :

  * Create knowledge graphs from data.

  * Support indexing workflows from LangChain data loaders to vectorstores.

Importantly, Index keeps on working even if the content being written is derived via a set of transformations from some source content \(e.g., indexing children documents that were derived from parent documents by chunking.\)

**Classes**

[`indexes.base.RecordManager`](https://python.langchain.com/api_reference/community/indexes/langchain_community.indexes.base.RecordManager.html#langchain_community.indexes.base.RecordManager "langchain_community.indexes.base.RecordManager")\(namespace\) | Abstract base class for a record manager.   ---|---