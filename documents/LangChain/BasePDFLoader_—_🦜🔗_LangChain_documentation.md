# BasePDFLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.BasePDFLoader.html
**Word Count:** 177
**Links Count:** 416
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# BasePDFLoader\#

_class _langchain\_community.document\_loaders.pdf.BasePDFLoader\(

    _file\_path : str | PurePath_,     _\*_ ,     _headers : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#BasePDFLoader)\#     

Base Loader class for PDF files.

If the file is a web path, it will download it to a temporary file, use it, then     

clean up the temporary file after completion.

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – Either a local, S3 or web path to a PDF file.

  * **headers** \(_dict_ _|__None_\) – Headers to use for GET request to download a file from a web path.

Attributes

`source` |    ---|---      Methods

`__init__`\(file\_path, \*\[, headers\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | PurePath_,     _\*_ ,     _headers : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#BasePDFLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – Either a local, S3 or web path to a PDF file.

  * **headers** \(_dict_ _|__None_\) – Headers to use for GET request to download a file from a web path.

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

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)