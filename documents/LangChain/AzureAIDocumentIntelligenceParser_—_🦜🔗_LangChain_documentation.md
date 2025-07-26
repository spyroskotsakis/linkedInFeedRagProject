# AzureAIDocumentIntelligenceParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.doc_intelligence.AzureAIDocumentIntelligenceParser.html
**Word Count:** 71
**Links Count:** 416
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# AzureAIDocumentIntelligenceParser\#

_class _langchain\_community.document\_loaders.parsers.doc\_intelligence.AzureAIDocumentIntelligenceParser\(

    _api\_endpoint : str_,     _api\_key : str | None = None_,     _api\_version : str | None = None_,     _api\_model : str = 'prebuilt-layout'_,     _mode : str = 'markdown'_,     _analysis\_features : List\[str\] | None = None_,     _azure\_credential : 'TokenCredential' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/doc_intelligence.html#AzureAIDocumentIntelligenceParser)\#     

Loads a PDF with Azure Document Intelligence \(formerly Forms Recognizer\).

Methods

`__init__`\(api\_endpoint\[, api\_key, ...\]\) |    ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.   `parse_bytes`\(bytes\_source\) |    `parse_url`\(url\) |       Parameters:     

  * **api\_endpoint** \(_str_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **api\_version** \(_Optional_ _\[__str_ _\]_\)

  * **api\_model** \(_str_\)

  * **mode** \(_str_\)

  * **analysis\_features** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **azure\_credential** \(_Optional_ _\[__'TokenCredential'__\]_\)

\_\_init\_\_\(

    _api\_endpoint : str_,     _api\_key : str | None = None_,     _api\_version : str | None = None_,     _api\_model : str = 'prebuilt-layout'_,     _mode : str = 'markdown'_,     _analysis\_features : List\[str\] | None = None_,     _azure\_credential : 'TokenCredential' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/doc_intelligence.html#AzureAIDocumentIntelligenceParser.__init__)\#     

Parameters:     

  * **api\_endpoint** \(_str_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **api\_version** \(_Optional_ _\[__str_ _\]_\)

  * **api\_model** \(_str_\)

  * **mode** \(_str_\)

  * **analysis\_features** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **azure\_credential** \(_Optional_ _\[__'TokenCredential'__\]_\)

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/doc_intelligence.html#AzureAIDocumentIntelligenceParser.lazy_parse)\#     

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

parse\_bytes\(

    _bytes\_source : bytes_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/doc_intelligence.html#AzureAIDocumentIntelligenceParser.parse_bytes)\#     

Parameters:     

**bytes\_source** \(_bytes_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\_url\(

    _url : str_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/doc_intelligence.html#AzureAIDocumentIntelligenceParser.parse_url)\#     

Parameters:     

**url** \(_str_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page