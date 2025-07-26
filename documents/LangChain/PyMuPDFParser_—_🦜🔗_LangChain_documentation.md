# PyMuPDFParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyMuPDFParser.html
**Word Count:** 452
**Links Count:** 408
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# PyMuPDFParser\#

_class _langchain\_community.document\_loaders.parsers.pdf.PyMuPDFParser\(

    _text\_kwargs : dict\[str, Any\] | None = None_,     _extract\_images : bool = False_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _extract\_tables : Literal\['csv', 'markdown', 'html'\] | None = None_,     _extract\_tables\_settings : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyMuPDFParser)\#     

Parse a blob from a PDF using PyMuPDF library.

> This class provides methods to parse a blob from a PDF document, supporting various configurations such as handling password-protected PDFs, extracting images, and defining extraction mode. It integrates the ‘PyMuPDF’ library for PDF processing and offers synchronous blob parsing. >  > Examples: >      >  > Setup: >      >      >     pip install -U langchain-community pymupdf >      >  > Load a blob from a PDF file: >      >      >     from langchain_core.documents.base import Blob >      >     blob = Blob.from_path("./example_data/layout-parser-paper.pdf") >      >  > Instantiate the parser: >      >      >     from langchain_community.document_loaders.parsers import PyMuPDFParser >      >     parser = PyMuPDFParser( >         # password = None, >         mode = "single", >         pages_delimiter = " >     

“,     

> > \# images\_parser = TesseractBlobParser\(\), \# extract\_tables=”markdown”, \# extract\_tables\_settings=None, \# text\_kwargs=None, >  > \)

Lazily parse the blob:               docs = []     docs_lazy = parser.lazy_parse(blob)          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Initialize a parser based on PyMuPDF.

Parameters:     

  * **password** \(_Optional_ _\[__str_ _\]_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \(_Optional_ _\[_[_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _\]_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extract\_tables** \(_Union_ _\[__Literal_ _\[__'csv'__,__'markdown'__,__'html'__\]__,__None_ _\]_\) – Whether to extract tables in a specific format, such as “csv”, “markdown”, or “html”.

  * **extract\_tables\_settings** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional dictionary of settings for customizing table extraction.

  * **text\_kwargs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\)

Returns:     

This method does not directly return data. Use the parse or lazy\_parse methods to retrieve parsed documents with content and metadata.

Raises:     

  * **ValueError** – If the mode is not “single” or “page”.

  * **ValueError** – If the extract\_tables format is not “markdown”, “html”,

  * **or "csv".** – 

Methods

`__init__`\(\[text\_kwargs, extract\_images, ...\]\) | Initialize a parser based on PyMuPDF.   ---|---   `lazy_parse`\(blob\) | Lazy parsing interface.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _text\_kwargs : dict\[str, Any\] | None = None_,     _extract\_images : bool = False_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _extract\_tables : Literal\['csv', 'markdown', 'html'\] | None = None_,     _extract\_tables\_settings : dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyMuPDFParser.__init__)\#     

Initialize a parser based on PyMuPDF.

Parameters:     

  * **password** \(_str_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extract\_tables** \(_Literal_ _\[__'csv'__,__'markdown'__,__'html'__\]__|__None_\) – Whether to extract tables in a specific format, such as “csv”, “markdown”, or “html”.

  * **extract\_tables\_settings** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional dictionary of settings for customizing table extraction.

  * **text\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Returns:     

This method does not directly return data. Use the parse or lazy\_parse methods to retrieve parsed documents with content and metadata.

Raises:     

  * **ValueError** – If the mode is not “single” or “page”.

  * **ValueError** – If the extract\_tables format is not “markdown”, “html”,

  * **or "csv".** – 

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyMuPDFParser.lazy_parse)\#     

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)