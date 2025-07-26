# PyMuPDFLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyMuPDFLoader.html
**Word Count:** 532
**Links Count:** 423
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# PyMuPDFLoader\#

_class _langchain\_community.document\_loaders.pdf.PyMuPDFLoader\(

    _file\_path : str | PurePath_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _extract\_images : bool = False_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _extract\_tables : Literal\['csv', 'markdown', 'html'\] | None = None_,     _headers : dict | None = None_,     _extract\_tables\_settings : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyMuPDFLoader)\#     

Load and parse a PDF file using ‘PyMuPDF’ library.

> This class provides methods to load and parse PDF documents, supporting various configurations such as handling password-protected files, extracting tables, extracting images, and defining extraction mode. It integrates the PyMuPDF library for PDF processing and offers both synchronous and asynchronous document loading. >  > Examples: >      >  > Setup: >      >      >     pip install -U langchain-community pymupdf >      >  > Instantiate the loader: >      >      >     from langchain_community.document_loaders import PyMuPDFLoader >      >     loader = PyMuPDFLoader( >         file_path = "./example_data/layout-parser-paper.pdf", >         # headers = None >         # password = None, >         mode = "single", >         pages_delimiter = " >     

“,     

> > \# extract\_images = True, \# images\_parser = TesseractBlobParser\(\), \# extract\_tables = “markdown”, \# extract\_tables\_settings = None, >  > \)

Lazy load documents:               docs = []     docs_lazy = loader.lazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Load documents asynchronously:               docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – The path to the PDF file to be loaded.

  * **headers** \(_dict_ _|__None_\) – Optional headers to use for GET request to download a file from a web path.

  * **password** \(_str_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extract\_tables** \(_Literal_ _\[__'csv'__,__'markdown'__,__'html'__\]__|__None_\) – Whether to extract tables in a specific format, such as “csv”, “markdown”, or “html”.

  * **extract\_tables\_settings** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional dictionary of settings for customizing table extraction.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments for customizing text extraction behavior.

Returns:     

This method does not directly return data. Use the load, lazy\_load, or aload methods to retrieve parsed documents with content and metadata.

Raises:     

**ValueError** – If the mode argument is not one of “single” or “page”.

Attributes

`source` |    ---|---      Methods

`__init__`\(file\_path, \*\[, password, mode, ...\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\*\*kwargs\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | PurePath_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _extract\_images : bool = False_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _extract\_tables : Literal\['csv', 'markdown', 'html'\] | None = None_,     _headers : dict | None = None_,     _extract\_tables\_settings : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyMuPDFLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – The path to the PDF file to be loaded.

  * **headers** \(_dict_ _|__None_\) – Optional headers to use for GET request to download a file from a web path.

  * **password** \(_str_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extract\_tables** \(_Literal_ _\[__'csv'__,__'markdown'__,__'html'__\]__|__None_\) – Whether to extract tables in a specific format, such as “csv”, “markdown”, or “html”.

  * **extract\_tables\_settings** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional dictionary of settings for customizing table extraction.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments for customizing text extraction behavior.

Returns:     

This method does not directly return data. Use the load, lazy\_load, or aload methods to retrieve parsed documents with content and metadata.

Raises:     

**ValueError** – If the mode argument is not one of “single” or “page”.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyMuPDFLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(

    _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyMuPDFLoader.load)\#     

Load data into Document objects.

Parameters:     

**kwargs** \(_Any_\)

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

Examples using PyMuPDFLoader

  * [PyMuPDF](https://python.langchain.com/docs/integrations/document_loaders/pymupdf/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)