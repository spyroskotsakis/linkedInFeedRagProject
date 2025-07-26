# BlobLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html
**Word Count:** 62
**Links Count:** 108
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# BlobLoader\#

_class _langchain\_core.document\_loaders.blob\_loaders.BlobLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/blob_loaders.html#BlobLoader)\#     

Abstract interface for blob loaders implementation.

Implementer should be able to load raw content from a storage system according to some criteria and return the raw content lazily as a stream of blobs.

Methods

`yield_blobs`\(\) | A lazy loader for raw data represented by LangChain's Blob object.   ---|---      _abstractmethod _yield\_blobs\(\) → Iterable\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/blob_loaders.html#BlobLoader.yield_blobs)\#     

A lazy loader for raw data represented by LangChain’s Blob object.

Returns:     

A generator over blobs

Return type:     

Iterable\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\]

__On this page