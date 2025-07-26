# MimeTypeBasedParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.generic.MimeTypeBasedParser.html
**Word Count:** 269
**Links Count:** 412
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# MimeTypeBasedParser\#

_class _langchain\_community.document\_loaders.parsers.generic.MimeTypeBasedParser\(

    _handlers : Mapping\[str, [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\]_,     _\*_ ,     _fallback\_parser : [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/generic.html#MimeTypeBasedParser)\#     

Parser that uses mime-types to parse a blob.

This parser is useful for simple pipelines where the mime-type is sufficient to determine how to parse a blob.

To use, configure handlers based on mime-types and pass them to the initializer.

Example               from langchain_community.document_loaders.parsers.generic import MimeTypeBasedParser          parser = MimeTypeBasedParser(         handlers={             "application/pdf": ...,         },         fallback_parser=...,     )     

Define a parser that uses mime-types to determine how to parse a blob.

Parameters:     

  * **handlers** \(_Mapping_ _\[__str_ _,_[_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") _\]_\) – A mapping from mime-types to functions that take a blob, parse it and return a document.

  * **fallback\_parser** \([_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") _|__None_\) – A fallback\_parser parser to use if the mime-type is not found in the handlers. If provided, this parser will be used to parse blobs with all mime-types not found in the handlers. If not provided, a ValueError will be raised if the mime-type is not found in the handlers.

Methods

`__init__`\(handlers, \*\[, fallback\_parser\]\) | Define a parser that uses mime-types to determine how to parse a blob.   ---|---   `lazy_parse`\(blob\) | Load documents from a blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _handlers : Mapping\[str, [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\]_,     _\*_ ,     _fallback\_parser : [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/generic.html#MimeTypeBasedParser.__init__)\#     

Define a parser that uses mime-types to determine how to parse a blob.

Parameters:     

  * **handlers** \(_Mapping_ _\[__str_ _,_[_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") _\]_\) – A mapping from mime-types to functions that take a blob, parse it and return a document.

  * **fallback\_parser** \([_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") _|__None_\) – A fallback\_parser parser to use if the mime-type is not found in the handlers. If provided, this parser will be used to parse blobs with all mime-types not found in the handlers. If not provided, a ValueError will be raised if the mime-type is not found in the handlers.

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/generic.html#MimeTypeBasedParser.lazy_parse)\#     

Load documents from a blob.

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)