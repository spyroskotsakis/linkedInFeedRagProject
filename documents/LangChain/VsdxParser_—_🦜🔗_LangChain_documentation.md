# VsdxParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.vsdx.VsdxParser.html
**Word Count:** 164
**Links Count:** 413
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# VsdxParser\#

_class _langchain\_community.document\_loaders.parsers.vsdx.VsdxParser[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/vsdx.html#VsdxParser)\#     

Parser for vsdx files.

Methods

`get_pages_content`\(zfile, source\) | Get the content of the pages of a vsdx file.   ---|---   `get_relationships`\(page, zfile, filelist, ...\) | Get the relationships of a page and the relationships of its relationships, etc.   `lazy_parse`\(blob\) | Retrieve the contents of pages from a .vsdx file and insert them into documents, one document per page.   `parse`\(blob\) | Parse a vsdx file.      get\_pages\_content\(

    _zfile : ZipFile_,     _source : str_, \) → List\[Tuple\[int, str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/vsdx.html#VsdxParser.get_pages_content)\#     

Get the content of the pages of a vsdx file.

zfile\#     

The vsdx file under zip format.

Type:     

zipfile.ZipFile

source\#     

The path of the vsdx file.

Type:     

str

Returns:     

A list of tuples containing the page number, the name of the page and the content of the page for each page of the vsdx file.

Return type:     

list\[tuple\[int, str, str\]\]

Parameters:     

  * **zfile** \(_ZipFile_\)

  * **source** \(_str_\)

get\_relationships\(

    _page : str_,     _zfile : ZipFile_,     _filelist : List\[str\]_,     _pagexml\_rels : List\[dict\]_, \) → Set\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/vsdx.html#VsdxParser.get_relationships)\#     

Get the relationships of a page and the relationships of its relationships, etc… recursively. Pages are based on other pages \(ex: background page\), so we need to get all the relationships to get all the content of a single page.

Parameters:     

  * **page** \(_str_\)

  * **zfile** \(_ZipFile_\)

  * **filelist** \(_List_ _\[__str_ _\]_\)

  * **pagexml\_rels** \(_List_ _\[__dict_ _\]_\)

Return type:     

_Set_\[str\]

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/vsdx.html#VsdxParser.lazy_parse)\#     

Retrieve the contents of pages from a .vsdx file and insert them into documents, one document per page.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/vsdx.html#VsdxParser.parse)\#     

Parse a vsdx file.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page