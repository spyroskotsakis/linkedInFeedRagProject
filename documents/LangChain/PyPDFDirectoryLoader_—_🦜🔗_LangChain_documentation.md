# PyPDFDirectoryLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyPDFDirectoryLoader.html
**Word Count:** 420
**Links Count:** 422
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# PyPDFDirectoryLoader\#

_class _langchain\_community.document\_loaders.pdf.PyPDFDirectoryLoader\(

    _path : str | PurePath_,     _glob : str = '\*\*/\[\!.\]\*.pdf'_,     _silent\_errors : bool = False_,     _load\_hidden : bool = False_,     _recursive : bool = False_,     _extract\_images : bool = False_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _headers : dict | None = None_,     _extraction\_mode : Literal\['plain', 'layout'\] = 'plain'_,     _extraction\_kwargs : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyPDFDirectoryLoader)\#     

Load and parse a directory of PDF files using ‘pypdf’ library.

This class provides methods to load and parse multiple PDF documents in a directory, supporting options for recursive search, handling password-protected files, extracting images, and defining extraction modes. It integrates the pypdf library for PDF processing and offers synchronous document loading.

Examples

Setup:               pip install -U langchain-community pypdf     

Instantiate the loader:               from langchain_community.document_loaders import PyPDFDirectoryLoader          loader = PyPDFDirectoryLoader(         path = "./example_data/",         glob = "**/[!.]*.pdf",         silent_errors = False,         load_hidden = False,         recursive = False,         extract_images = False,         password = None,         mode = "page",         images_to_text = None,         headers = None,         extraction_mode = "plain",         # extraction_kwargs = None,     )     

Load documents:               docs = loader.load()     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Load documents asynchronously:               docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Initialize with a directory path.

Parameters:     

  * **path** \(_str_ _|__PurePath_\) – The path to the directory containing PDF files to be loaded.

  * **glob** \(_str_\) – The glob pattern to match files in the directory.

  * **silent\_errors** \(_bool_\) – Whether to log errors instead of raising them.

  * **load\_hidden** \(_bool_\) – Whether to include hidden files in the search.

  * **recursive** \(_bool_\) – Whether to search subdirectories recursively.

  * **extract\_images** \(_bool_\) – Whether to extract images from PDFs.

  * **password** \(_str_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for extracting the entire document or “page” for page-wise extraction.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser..

  * **headers** \(_dict_ _|__None_\) – Optional headers to use for GET request to download a file from a web path.

  * **extraction\_mode** \(_Literal_ _\[__'plain'__,__'layout'__\]_\) – “plain” for legacy functionality, “layout” for experimental layout mode functionality

  * **extraction\_kwargs** \(_dict_ _|__None_\) – Optional additional parameters for the extraction process.

Returns:     

This method does not directly return data. Use the load method to retrieve parsed documents with content and metadata.

Methods

`__init__`\(path\[, glob, silent\_errors, ...\]\) | Initialize with a directory path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _path : str | PurePath_,     _glob : str = '\*\*/\[\!.\]\*.pdf'_,     _silent\_errors : bool = False_,     _load\_hidden : bool = False_,     _recursive : bool = False_,     _extract\_images : bool = False_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _headers : dict | None = None_,     _extraction\_mode : Literal\['plain', 'layout'\] = 'plain'_,     _extraction\_kwargs : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyPDFDirectoryLoader.__init__)\#     

Initialize with a directory path.

Parameters:     

  * **path** \(_str_ _|__PurePath_\) – The path to the directory containing PDF files to be loaded.

  * **glob** \(_str_\) – The glob pattern to match files in the directory.

  * **silent\_errors** \(_bool_\) – Whether to log errors instead of raising them.

  * **load\_hidden** \(_bool_\) – Whether to include hidden files in the search.

  * **recursive** \(_bool_\) – Whether to search subdirectories recursively.

  * **extract\_images** \(_bool_\) – Whether to extract images from PDFs.

  * **password** \(_str_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for extracting the entire document or “page” for page-wise extraction.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser..

  * **headers** \(_dict_ _|__None_\) – Optional headers to use for GET request to download a file from a web path.

  * **extraction\_mode** \(_Literal_ _\[__'plain'__,__'layout'__\]_\) – “plain” for legacy functionality, “layout” for experimental layout mode functionality

  * **extraction\_kwargs** \(_dict_ _|__None_\) – Optional additional parameters for the extraction process.

Returns:     

This method does not directly return data. Use the load method to retrieve parsed documents with content and metadata.

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

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyPDFDirectoryLoader.load)\#     

Load data into Document objects.

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

Examples using PyPDFDirectoryLoader

  * [PyPDFDirectoryLoader](https://python.langchain.com/docs/integrations/document_loaders/pypdfdirectory/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)