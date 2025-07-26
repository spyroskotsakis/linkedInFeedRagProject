# CloudVisionParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/vision/langchain_google_community.vision.CloudVisionParser.html
**Word Count:** 90
**Links Count:** 113
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# CloudVisionParser\#

_class _langchain\_google\_community.vision.CloudVisionParser\(_project : str | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/vision.html#CloudVisionParser)\#     

Methods

`__init__`\(\[project\]\) |    ---|---   `lazy_parse`\(blob\) | Lazy parsing interface.   `load`\(gcs\_uri\) | Loads an image from GCS path to a Document, only the text.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      Parameters:     

**project** \(_str_ _|__None_\)

\_\_init\_\_\(_project : str | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/vision.html#CloudVisionParser.__init__)\#     

Parameters:     

**project** \(_str_ _|__None_\)

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/vision.html#CloudVisionParser.lazy_parse)\#     

Lazy parsing interface.

Subclasses are required to implement this method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

Generator of documents

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(

    _gcs\_uri : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/vision.html#CloudVisionParser.load)\#     

Loads an image from GCS path to a Document, only the text.

Parameters:     

**gcs\_uri** \(_str_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

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