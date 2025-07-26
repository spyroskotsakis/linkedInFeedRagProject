# PyPDFLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyPDFLoader.html
**Word Count:** 543
**Links Count:** 430
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# PyPDFLoader\#

_class _langchain\_community.document\_loaders.pdf.PyPDFLoader\(

    _file\_path : str | PurePath_,     _password : str | bytes | None = None_,     _headers : dict | None = None_,     _extract\_images : bool = False_,     _\*_ ,     _mode : Literal\['single', 'page'\] = 'page'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _pages\_delimiter : str = '\n\x0c'_,     _extraction\_mode : Literal\['plain', 'layout'\] = 'plain'_,     _extraction\_kwargs : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyPDFLoader)\#     

Load and parse a PDF file using ‘pypdf’ library.

> This class provides methods to load and parse PDF documents, supporting various configurations such as handling password-protected files, extracting images, and defining extraction mode. It integrates the pypdf library for PDF processing and offers both synchronous and asynchronous document loading. >  > Examples: >      >  > Setup: >      >      >     pip install -U langchain-community pypdf >      >  > Instantiate the loader: >      >      >     from langchain_community.document_loaders import PyPDFLoader >      >     loader = PyPDFLoader( >         file_path = "./example_data/layout-parser-paper.pdf", >         # headers = None >         # password = None, >         mode = "single", >         pages_delimiter = " >     

“,     

> > \# extract\_images = True, \# images\_parser = RapidOCRBlobParser\(\), >  > \)

Lazy load documents:               docs = []     docs_lazy = loader.lazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Load documents asynchronously:               docs = await loader.aload()     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – The path to the PDF file to be loaded.

  * **headers** \(_dict_ _|__None_\) – Optional headers to use for GET request to download a file from a web path.

  * **password** \(_str_ _|__bytes_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extraction\_mode** \(_Literal_ _\[__'plain'__,__'layout'__\]_\) – “plain” for legacy functionality, “layout” extract text in a fixed width format that closely adheres to the rendered layout in the source pdf

  * **extraction\_kwargs** \(_dict_ _|__None_\) – Optional additional parameters for the extraction process.

Returns:     

This method does not directly return data. Use the load, lazy\_load or aload methods to retrieve parsed documents with content and metadata.

Attributes

`source` |    ---|---      Methods

`__init__`\(file\_path\[, password, headers, ...\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load given path as pages.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | PurePath_,     _password : str | bytes | None = None_,     _headers : dict | None = None_,     _extract\_images : bool = False_,     _\*_ ,     _mode : Literal\['single', 'page'\] = 'page'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _pages\_delimiter : str = '\n\x0c'_,     _extraction\_mode : Literal\['plain', 'layout'\] = 'plain'_,     _extraction\_kwargs : dict | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyPDFLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – The path to the PDF file to be loaded.

  * **headers** \(_dict_ _|__None_\) – Optional headers to use for GET request to download a file from a web path.

  * **password** \(_str_ _|__bytes_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extraction\_mode** \(_Literal_ _\[__'plain'__,__'layout'__\]_\) – “plain” for legacy functionality, “layout” extract text in a fixed width format that closely adheres to the rendered layout in the source pdf

  * **extraction\_kwargs** \(_dict_ _|__None_\) – Optional additional parameters for the extraction process.

Returns:     

This method does not directly return data. Use the load, lazy\_load or aload methods to retrieve parsed documents with content and metadata.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#PyPDFLoader.lazy_load)\#     

Lazy load given path as pages. Insert image, if possible, between two paragraphs. In this way, a paragraph can be continued on the next page.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using PyPDFLoader

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [Azure Cosmos DB No SQL](https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db_no_sql/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Google Cloud Storage File](https://python.langchain.com/docs/integrations/document_loaders/google_cloud_storage_file/)

  * [Google Vertex AI Vector Search](https://python.langchain.com/docs/integrations/vectorstores/google_vertex_ai_vector_search/)

  * [How to load PDFs](https://python.langchain.com/docs/how_to/document_loader_pdf/)

  * [KDB.AI](https://python.langchain.com/docs/integrations/vectorstores/kdbai/)

  * [Merge Documents Loader](https://python.langchain.com/docs/integrations/document_loaders/merge_doc/)

  * [PyPDFLoader](https://python.langchain.com/docs/integrations/document_loaders/pypdfloader/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)