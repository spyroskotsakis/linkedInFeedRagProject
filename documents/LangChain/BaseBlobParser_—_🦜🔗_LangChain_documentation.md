# BaseBlobParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html
**Word Count:** 119
**Links Count:** 119
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# BaseBlobParser\#

_class _langchain\_core.document\_loaders.base.BaseBlobParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/base.html#BaseBlobParser)\#     

Abstract interface for blob parsers.

A blob parser provides a way to parse raw data stored in a blob into one or more documents.

The parser can be composed with blob loaders, making it easy to reuse a parser independent of how the blob was originally loaded.

Methods

`lazy_parse`\(blob\) | Lazy parsing interface.   ---|---   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      _abstractmethod _lazy\_parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/base.html#BaseBlobParser.lazy_parse)\#     

Lazy parsing interface.

Subclasses are required to implement this method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

Generator of documents

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/base.html#BaseBlobParser.parse)\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using BaseBlobParser

  * [How to create a custom Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/)

__On this page