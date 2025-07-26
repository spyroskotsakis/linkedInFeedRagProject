# BaseImageBlobParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html
**Word Count:** 94
**Links Count:** 400
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# BaseImageBlobParser\#

_class _langchain\_community.document\_loaders.parsers.images.BaseImageBlobParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#BaseImageBlobParser)\#     

Abstract base class for parsing image blobs into text.

Methods

`lazy_parse`\(blob\) | Lazily parse a blob and yields Documents containing the parsed content.   ---|---   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#BaseImageBlobParser.lazy_parse)\#     

Lazily parse a blob and yields Documents containing the parsed content.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – The blob to be parsed.

Yields:     

_Document_ – A document containing the parsed content and metadata.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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

__On this page