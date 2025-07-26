# DocumentIntelligenceLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.DocumentIntelligenceLoader.html
**Word Count:** 259
**Links Count:** 422
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# DocumentIntelligenceLoader\#

_class _langchain\_community.document\_loaders.pdf.DocumentIntelligenceLoader\(

    _file\_path : str | PurePath_,     _client : Any_,     _model : str = 'prebuilt-document'_,     _headers : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#DocumentIntelligenceLoader)\#     

Load a PDF with Azure Document Intelligence

Initialize the object for file processing with Azure Document Intelligence \(formerly Form Recognizer\).

This constructor initializes a DocumentIntelligenceParser object to be used for parsing files using the Azure Document Intelligence API. The load method generates a Document node including metadata \(source blob and page number\) for each page.

## Parameters:\#

file\_pathstr     

The path to the file that needs to be parsed.

client: Any     

A DocumentAnalysisClient to perform the analysis of the blob

modelstr     

The model name or ID to be used for form recognition in Azure.

## Examples:\#               >>> obj = DocumentIntelligenceLoader(     ...     file_path="path/to/file",     ...     client=client,     ...     model="prebuilt-document"     ... )     

Attributes

`source` |    ---|---      Methods

`__init__`\(file\_path, client\[, model, headers\]\) | Initialize the object for file processing with Azure Document Intelligence \(formerly Form Recognizer\).   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load given path as pages.   `load`\(\) | Load given path as pages.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | PurePath_,     _client : Any_,     _model : str = 'prebuilt-document'_,     _headers : dict | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#DocumentIntelligenceLoader.__init__)\#     

Initialize the object for file processing with Azure Document Intelligence \(formerly Form Recognizer\).

This constructor initializes a DocumentIntelligenceParser object to be used for parsing files using the Azure Document Intelligence API. The load method generates a Document node including metadata \(source blob and page number\) for each page.

### Parameters:\#

file\_pathstr     

The path to the file that needs to be parsed.

client: Any     

A DocumentAnalysisClient to perform the analysis of the blob

modelstr     

The model name or ID to be used for form recognition in Azure.

### Examples:\#               >>> obj = DocumentIntelligenceLoader(     ...     file_path="path/to/file",     ...     client=client,     ...     model="prebuilt-document"     ... )     

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\)

  * **client** \(_Any_\)

  * **model** \(_str_\)

  * **headers** \(_dict_ _|__None_\)

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#DocumentIntelligenceLoader.lazy_load)\#     

Lazy load given path as pages.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#DocumentIntelligenceLoader.load)\#     

Load given path as pages.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\)

  * **client** \(_Any_\)

  * **model** \(_str_\)

  * **headers** \(_dict_ _|__None_\)

__On this page