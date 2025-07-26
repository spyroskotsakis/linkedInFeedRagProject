# PDFPlumberParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PDFPlumberParser.html
**Word Count:** 95
**Links Count:** 404
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# PDFPlumberParser\#

_class _langchain\_community.document\_loaders.parsers.pdf.PDFPlumberParser\(

    _text\_kwargs : Mapping\[str, Any\] | None = None_,     _dedupe : bool = False_,     _extract\_images : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PDFPlumberParser)\#     

Parse PDF with PDFPlumber.

Initialize the parser.

Parameters:     

  * **text\_kwargs** \(_Optional_ _\[__Mapping_ _\[__str_ _,__Any_ _\]__\]_\) – Keyword arguments to pass to `pdfplumber.Page.extract_text()`

  * **dedupe** \(_bool_\) – Avoiding the error of duplicate characters if dedupe=True.

  * **extract\_images** \(_bool_\)

Methods

`__init__`\(\[text\_kwargs, dedupe, extract\_images\]\) | Initialize the parser.   ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _text\_kwargs : Mapping\[str, Any\] | None = None_,     _dedupe : bool = False_,     _extract\_images : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PDFPlumberParser.__init__)\#     

Initialize the parser.

Parameters:     

  * **text\_kwargs** \(_Mapping_ _\[__str_ _,__Any_ _\]__|__None_\) – Keyword arguments to pass to `pdfplumber.Page.extract_text()`

  * **dedupe** \(_bool_\) – Avoiding the error of duplicate characters if dedupe=True.

  * **extract\_images** \(_bool_\)

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PDFPlumberParser.lazy_parse)\#     

Lazily parse the blob.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

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