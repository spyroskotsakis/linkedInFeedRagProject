# RapidOCRBlobParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.RapidOCRBlobParser.html
**Word Count:** 107
**Links Count:** 405
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# RapidOCRBlobParser\#

_class _langchain\_community.document\_loaders.parsers.images.RapidOCRBlobParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#RapidOCRBlobParser)\#     

Parser for extracting text from images using the RapidOCR library.

ocr\#     

The RapidOCR instance for performing OCR.

Initializes the RapidOCRBlobParser.

Methods

`__init__`\(\) | Initializes the RapidOCRBlobParser.   ---|---   `lazy_parse`\(blob\) | Lazily parse a blob and yields Documents containing the parsed content.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#RapidOCRBlobParser.__init__)\#     

Initializes the RapidOCRBlobParser.

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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