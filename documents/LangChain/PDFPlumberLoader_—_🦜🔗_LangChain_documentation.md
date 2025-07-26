# PDFPlumberLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PDFPlumberLoader.html
**Word Count:** 96
**Links Count:** 418
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# PDFPlumberLoader\#

_class _langchain\_community.document\_loaders.pdf.PDFPlumberLoader\(

    _file\_path : str | PurePath_,     _text\_kwargs : Mapping\[str, Any\] | None = None_,     _dedupe : bool = False_,     _headers : dict | None = None_,     _extract\_images : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PDFPlumberLoader)\#     

Load PDF files using pdfplumber.

Initialize with a file path.

Attributes

`source` |    ---|---      Methods

`__init__`\(file\_path\[, text\_kwargs, dedupe, ...\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load file.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\)

  * **text\_kwargs** \(_Mapping_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **dedupe** \(_bool_\)

  * **headers** \(_dict_ _|__None_\)

  * **extract\_images** \(_bool_\)

\_\_init\_\_\(

    _file\_path : str | PurePath_,     _text\_kwargs : Mapping\[str, Any\] | None = None_,     _dedupe : bool = False_,     _headers : dict | None = None_,     _extract\_images : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PDFPlumberLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\)

  * **text\_kwargs** \(_Mapping_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **dedupe** \(_bool_\)

  * **headers** \(_dict_ _|__None_\)

  * **extract\_images** \(_bool_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PDFPlumberLoader.load)\#     

Load file.

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

Examples using PDFPlumberLoader

  * [PDFPlumber](https://python.langchain.com/docs/integrations/document_loaders/pdfplumber/)

__On this page