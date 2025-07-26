# GrobidParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.grobid.GrobidParser.html
**Word Count:** 86
**Links Count:** 411
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# GrobidParser\#

_class _langchain\_community.document\_loaders.parsers.grobid.GrobidParser\(

    _segment\_sentences : bool_,     _grobid\_server : str = 'http://localhost:8070/api/processFulltextDocument'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/grobid.html#GrobidParser)\#     

Load article PDF files using Grobid.

Methods

`__init__`\(segment\_sentences\[, grobid\_server\]\) |    ---|---   `lazy_parse`\(blob\) | Lazy parsing interface.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.   `process_xml`\(file\_path, xml\_data, ...\) | Process the XML file from Grobin.      Parameters:     

  * **segment\_sentences** \(_bool_\)

  * **grobid\_server** \(_str_\)

\_\_init\_\_\(

    _segment\_sentences : bool_,     _grobid\_server : str = 'http://localhost:8070/api/processFulltextDocument'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/grobid.html#GrobidParser.__init__)\#     

Parameters:     

  * **segment\_sentences** \(_bool_\)

  * **grobid\_server** \(_str_\)

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/grobid.html#GrobidParser.lazy_parse)\#     

Lazy parsing interface.

Subclasses are required to implement this method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

Generator of documents

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

process\_xml\(

    _file\_path : str_,     _xml\_data : str_,     _segment\_sentences : bool_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/grobid.html#GrobidParser.process_xml)\#     

Process the XML file from Grobin.

Parameters:     

  * **file\_path** \(_str_\)

  * **xml\_data** \(_str_\)

  * **segment\_sentences** \(_bool_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using GrobidParser

  * [Grobid](https://python.langchain.com/docs/integrations/document_loaders/grobid/)

__On this page