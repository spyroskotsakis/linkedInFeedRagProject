# BS4HTMLParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.html.bs4.BS4HTMLParser.html
**Word Count:** 84
**Links Count:** 404
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# BS4HTMLParser\#

_class _langchain\_community.document\_loaders.parsers.html.bs4.BS4HTMLParser\(

    _\*_ ,     _features : str = 'lxml'_,     _get\_text\_separator : str = ''_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/html/bs4.html#BS4HTMLParser)\#     

Parse HTML files using Beautiful Soup.

Initialize a bs4 based HTML parser.

Methods

`__init__`\(\*\[, features, get\_text\_separator\]\) | Initialize a bs4 based HTML parser.   ---|---   `lazy_parse`\(blob\) | Load HTML document into document objects.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      Parameters:     

  * **features** \(_str_\)

  * **get\_text\_separator** \(_str_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _\*_ ,     _features : str = 'lxml'_,     _get\_text\_separator : str = ''_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/html/bs4.html#BS4HTMLParser.__init__)\#     

Initialize a bs4 based HTML parser.

Parameters:     

  * **features** \(_str_\)

  * **get\_text\_separator** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/html/bs4.html#BS4HTMLParser.lazy_parse)\#     

Load HTML document into document objects.

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