# TesseractBlobParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.TesseractBlobParser.html
**Word Count:** 117
**Links Count:** 403
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# TesseractBlobParser\#

_class _langchain\_community.document\_loaders.parsers.images.TesseractBlobParser\(

    _\*_ ,     _langs : Iterable\[str\] = \('eng',\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#TesseractBlobParser)\#     

Parse for extracting text from images using the Tesseract OCR library.

Initialize the TesseractBlobParser.

Parameters:     

**langs** \(_list_ _\[__str_ _\]_\) – The languages to use for OCR.

Methods

`__init__`\(\*\[, langs\]\) | Initialize the TesseractBlobParser.   ---|---   `lazy_parse`\(blob\) | Lazily parse a blob and yields Documents containing the parsed content.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _\*_ ,     _langs : Iterable\[str\] = \('eng',\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/images.html#TesseractBlobParser.__init__)\#     

Initialize the TesseractBlobParser.

Parameters:     

**langs** \(_list_ _\[__str_ _\]_\) – The languages to use for OCR.

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)