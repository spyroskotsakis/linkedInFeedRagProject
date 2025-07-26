# PyPDFParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyPDFParser.html
**Word Count:** 469
**Links Count:** 412
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# PyPDFParser\#

_class _langchain\_community.document\_loaders.parsers.pdf.PyPDFParser\(

    _password : str | bytes | None = None_,     _extract\_images : bool = False_,     _\*_ ,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _extraction\_mode : Literal\['plain', 'layout'\] = 'plain'_,     _extraction\_kwargs : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFParser)\#     

Parse a blob from a PDF using pypdf library.

> This class provides methods to parse a blob from a PDF document, supporting various configurations such as handling password-protected PDFs, extracting images. It integrates the ‘pypdf’ library for PDF processing and offers synchronous blob parsing. >  > Examples: >      >  > Setup: >      >      >     pip install -U langchain-community pypdf >      >  > Load a blob from a PDF file: >      >      >     from langchain_core.documents.base import Blob >      >     blob = Blob.from_path("./example_data/layout-parser-paper.pdf") >      >  > Instantiate the parser: >      >      >     from langchain_community.document_loaders.parsers import PyPDFParser >      >     parser = PyPDFParser( >         # password = None, >         mode = "single", >         pages_delimiter = " >     

“,     

> > \# images\_parser = TesseractBlobParser\(\), >  > \)

Lazily parse the blob:               docs = []     docs_lazy = parser.lazy_parse(blob)          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)     

Initialize a parser based on PyPDF.

Parameters:     

  * **password** \(_Optional_ _\[__Union_ _\[__str_ _,__bytes_ _\]__\]_\) – Optional password for opening encrypted PDFs.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **images\_parser** \(_Optional_ _\[_[_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _\]_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extraction\_mode** \(_Literal_ _\[__'plain'__,__'layout'__\]_\) – “plain” for legacy functionality, “layout” extract text in a fixed width format that closely adheres to the rendered layout in the source pdf.

  * **extraction\_kwargs** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional additional parameters for the extraction process.

Raises:     

**ValueError** – If the mode is not “single” or “page”.

Methods

`__init__`\(\[password, extract\_images, mode, ...\]\) | Initialize a parser based on PyPDF.   ---|---   `extract_images_from_page`\(page\) | Extract images from a PDF page and get the text using images\_to\_text.   `lazy_parse`\(blob\) | Lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _password : str | bytes | None = None_,     _extract\_images : bool = False_,     _\*_ ,     _mode : Literal\['single', 'page'\] = 'page'_,     _pages\_delimiter : str = '\n\x0c'_,     _images\_parser : [BaseImageBlobParser](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") | None = None_,     _images\_inner\_format : Literal\['text', 'markdown-img', 'html-img'\] = 'text'_,     _extraction\_mode : Literal\['plain', 'layout'\] = 'plain'_,     _extraction\_kwargs : dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFParser.__init__)\#     

Initialize a parser based on PyPDF.

Parameters:     

  * **password** \(_str_ _|__bytes_ _|__None_\) – Optional password for opening encrypted PDFs.

  * **extract\_images** \(_bool_\) – Whether to extract images from the PDF.

  * **mode** \(_Literal_ _\[__'single'__,__'page'__\]_\) – The extraction mode, either “single” for the entire document or “page” for page-wise extraction.

  * **pages\_delimiter** \(_str_\) – A string delimiter to separate pages in single-mode extraction.

  * **images\_parser** \([_BaseImageBlobParser_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.images.BaseImageBlobParser.html#langchain_community.document_loaders.parsers.images.BaseImageBlobParser "langchain_community.document_loaders.parsers.images.BaseImageBlobParser") _|__None_\) – Optional image blob parser.

  * **images\_inner\_format** \(_Literal_ _\[__'text'__,__'markdown-img'__,__'html-img'__\]_\) – The format for the parsed output. \- “text” = return the content as is \- “markdown-img” = wrap the content into an image markdown link, w/ link pointing to \(\!\[body\)\(\#\)\] \- “html-img” = wrap the content as the alt text of an tag and link to \(<img alt=”\{body\}” src=”\#”/>\)

  * **extraction\_mode** \(_Literal_ _\[__'plain'__,__'layout'__\]_\) – “plain” for legacy functionality, “layout” extract text in a fixed width format that closely adheres to the rendered layout in the source pdf.

  * **extraction\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional additional parameters for the extraction process.

Raises:     

**ValueError** – If the mode is not “single” or “page”.

extract\_images\_from\_page\(

    _page : pypdf.\_page.PageObject_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFParser.extract_images_from_page)\#     

Extract images from a PDF page and get the text using images\_to\_text.

Parameters:     

**page** \(_pypdf.\_page.PageObject_\) – The page object from which to extract images.

Returns:     

The extracted text from the images on the page.

Return type:     

str

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#PyPDFParser.lazy_parse)\#     

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