# PyPDFium2Parser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyPDFium2Parser.html
**Word Count:** 442
**Links Count:** 408
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# PyPDFium2Parser\#

_class _langchain\_community.document\_loaders.parsers.pdf.PyPDFium2Parser\(

    _extract\_images : bool = False_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFium2Parser)\#     

Parse a blob from a PDF using PyPDFium2 library.

> This class provides methods to parse a blob from a PDF document, supporting various configurations such as handling password-protected PDFs, extracting images, and defining extraction mode. It integrates the ‘PyPDFium2’ library for PDF processing and offers synchronous blob parsing. >  > Examples: >      >  > Setup: >      >      >     pip install -U langchain-community pypdfium2 >      >  > Load a blob from a PDF file: >      >      >     from langchain_core.documents.base import Blob >      >     blob = Blob.from_path("./example_data/layout-parser-paper.pdf") >      >  > Instantiate the parser: >      >      >     from langchain_community.document_loaders.parsers import PyPDFium2Parser >      >     parser = PyPDFium2Parser( >         # password=None, >         mode="page", >         pages_delimiter=" >     

“,     

> > \# extract\_images = True, \# images\_to\_text = convert\_images\_to\_text\_with\_tesseract\(\), >  > \)

Lazily parse the blob:               docs = []     docs_lazy = parser.lazy_parse(blob)          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Initialize a parser based on PyPDFium2.

Parameters:     

  * **password** \(_Optional_ _\[__str_ _\]_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \(_Optional_ _\[_[_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _\]_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extraction\_mode** – “plain” for legacy functionality, “layout” for experimental layout mode functionality

  * **extraction\_kwargs** – Optional additional parameters for the extraction process.

Returns:     

This method does not directly return data. Use the parse or lazy\_parse methods to retrieve parsed documents with content and metadata.

Raises:     

**ValueError** – If the mode is not “single” or “page”.

Methods

`__init__`\(\[extract\_images, password, mode, ...\]\) | Initialize a parser based on PyPDFium2.   ---|---   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _extract\_images : bool = False_,     _\*_ ,     _password : str | None = None_,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFium2Parser.__init__)\#     

Initialize a parser based on PyPDFium2.

Parameters:     

  * **password** \(_str_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extraction\_mode** – “plain” for legacy functionality, “layout” for experimental layout mode functionality

  * **extraction\_kwargs** – Optional additional parameters for the extraction process.

Returns:     

This method does not directly return data. Use the parse or lazy\_parse methods to retrieve parsed documents with content and metadata.

Raises:     

**ValueError** – If the mode is not “single” or “page”.

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFium2Parser.lazy_parse)\#     

Lazily parse the blob. Insert image, if possible, between two paragraphs. In this way, a paragraph can be continued on the next page.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – The blob to parse.

Raises:     

**ImportError** – If the pypdf package is not found.

Yields:     

An iterator over the parsed documents.

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