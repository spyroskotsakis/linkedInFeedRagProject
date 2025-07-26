# DocumentIntelligenceParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.DocumentIntelligenceParser.html
**Word Count:** 73
**Links Count:** 404
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# DocumentIntelligenceParser\#

_class _langchain\_community.document\_loaders.parsers.pdf.DocumentIntelligenceParser\(_client : Any_, _model : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#DocumentIntelligenceParser)\#     

Loads a PDF with Azure Document Intelligence \(formerly Form Recognizer\) and chunks at character level.

Methods

`__init__`\(client, model\) |    ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      Parameters:     

  * **client** \(_Any_\)

  * **model** \(_str_\)

\_\_init\_\_\(

    _client : Any_,     _model : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#DocumentIntelligenceParser.__init__)\#     

Parameters:     

  * **client** \(_Any_\)

  * **model** \(_str_\)

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#DocumentIntelligenceParser.lazy_parse)\#     

Lazily parse the blob.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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