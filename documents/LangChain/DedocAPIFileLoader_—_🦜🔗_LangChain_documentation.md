# DedocAPIFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.dedoc.DedocAPIFileLoader.html
**Word Count:** 655
**Links Count:** 424
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# DedocAPIFileLoader\#

_class _langchain\_community.document\_loaders.dedoc.DedocAPIFileLoader\(

    _file\_path : str_,     _\*_ ,     _url : str = 'http://0.0.0.0:1231'_,     _split : str = 'document'_,     _with\_tables : bool = True_,     _with\_attachments : str | bool = False_,     _recursion\_deep\_attachments : int = 10_,     _pdf\_with\_text\_layer : str = 'auto\_tabby'_,     _language : str = 'rus+eng'_,     _pages : str = ':'_,     _is\_one\_column\_document : str = 'auto'_,     _document\_orientation : str = 'auto'_,     _need\_header\_footer\_analysis : str | bool = False_,     _need\_binarization : str | bool = False_,     _need\_pdf\_table\_analysis : str | bool = True_,     _delimiter : str | None = None_,     _encoding : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/dedoc.html#DedocAPIFileLoader)\#     

Load files using dedoc API. The file loader automatically detects the file type \(even with the wrong extension\). By default, the loader makes a call to the locally hosted dedoc API. More information about dedoc API can be found in dedoc documentation:

> <https://dedoc.readthedocs.io/en/latest/dedoc_api_usage/api.html>

Please see the documentation of DedocBaseLoader to get more details.

Setup:     

You don’t need to install dedoc library for using this loader. Instead, the dedoc API needs to be run. You may use Docker container for this purpose. Please see dedoc documentation for more details:

> <https://dedoc.readthedocs.io/en/latest/getting_started/installation.html#install-and-run-dedoc-using-docker>               docker pull dedocproject/dedoc     docker run -p 1231:1231     

Instantiate:                    from langchain_community.document_loaders import DedocAPIFileLoader          loader = DedocAPIFileLoader(         file_path="example.pdf",         # url=...,         # split=...,         # with_tables=...,         # pdf_with_text_layer=...,         # pages=...,         # ...     )     

Load:                    docs = loader.load()     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Some text     {         'file_name': 'example.pdf',         'file_type': 'application/pdf',         # ...     }     

Lazy load:                    docs = []     docs_lazy = loader.lazy_load()          for doc in docs_lazy:         docs.append(doc)     print(docs[0].page_content[:100])     print(docs[0].metadata)                    Some text     {         'file_name': 'example.pdf',         'file_type': 'application/pdf',         # ...     }     

Initialize with file path, API url and parsing parameters.

Parameters:     

  * **file\_path** \(_str_\) – path to the file for processing

  * **url** \(_str_\) – URL to call dedoc API

  * **split** \(_str_\) – 

type of document splitting into parts \(each part is returned separately\), default value “document” “document”: document is returned as a single langchain Document object

> \(don’t split\)

”page”: split document into pages \(works for PDF, DJVU, PPTX, PPT, ODP\) “node”: split document into tree nodes \(title nodes, list item nodes,

> raw text nodes\)

”line”: split document into lines

  * **with\_tables** \(_bool_\) – add tables to the result - each table is returned as a single langchain Document object

  * **dedoc** \(_Parameters used for document parsing via_\) – 

\(<https://dedoc.readthedocs.io/en/latest/parameters/parameters.html>\):

with\_attachments: enable attached files extraction recursion\_deep\_attachments: recursion level for attached files

> extraction, works only when with\_attachments==True

pdf\_with\_text\_layer: type of handler for parsing PDF documents,     

available options \[“true”, “false”, “tabby”, “auto”, “auto\_tabby” \(default\)\]

language: language of the document for PDF without a textual layer and     

images, available options \[“eng”, “rus”, “rus+eng” \(default\)\], the list of languages can be extended, please see <https://dedoc.readthedocs.io/en/latest/tutorials/add_new_language.html>

pages: page slice to define the reading range for parsing PDF documents is\_one\_column\_document: detect number of columns for PDF without

> a textual layer and images, available options \[“true”, “false”, “auto” \(default\)\]

document\_orientation: fix document orientation \(90, 180, 270 degrees\)     

for PDF without a textual layer and images, available options \[“auto” \(default\), “no\_change”\]

need\_header\_footer\_analysis: remove headers and footers from the output     

result for parsing PDF and images

need\_binarization: clean pages background \(binarize\) for PDF without a     

textual layer and images

need\_pdf\_table\_analysis: parse tables for PDF without a textual layer     

and images

delimiter: column separator for CSV, TSV files encoding: encoding of TXT, CSV, TSV

  * **with\_attachments** \(_str_ _|__bool_\)

  * **recursion\_deep\_attachments** \(_int_\)

  * **pdf\_with\_text\_layer** \(_str_\)

  * **language** \(_str_\)

  * **pages** \(_str_\)

  * **is\_one\_column\_document** \(_str_\)

  * **document\_orientation** \(_str_\)

  * **need\_header\_footer\_analysis** \(_str_ _|__bool_\)

  * **need\_binarization** \(_str_ _|__bool_\)

  * **need\_pdf\_table\_analysis** \(_str_ _|__bool_\)

  * **delimiter** \(_str_ _|__None_\)

  * **encoding** \(_str_ _|__None_\)

Methods

`__init__`\(file\_path, \*\[, url, split, ...\]\) | Initialize with file path, API url and parsing parameters.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazily load documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str_,     _\*_ ,     _url : str = 'http://0.0.0.0:1231'_,     _split : str = 'document'_,     _with\_tables : bool = True_,     _with\_attachments : str | bool = False_,     _recursion\_deep\_attachments : int = 10_,     _pdf\_with\_text\_layer : str = 'auto\_tabby'_,     _language : str = 'rus+eng'_,     _pages : str = ':'_,     _is\_one\_column\_document : str = 'auto'_,     _document\_orientation : str = 'auto'_,     _need\_header\_footer\_analysis : str | bool = False_,     _need\_binarization : str | bool = False_,     _need\_pdf\_table\_analysis : str | bool = True_,     _delimiter : str | None = None_,     _encoding : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/dedoc.html#DedocAPIFileLoader.__init__)\#     

Initialize with file path, API url and parsing parameters.

Parameters:     

  * **file\_path** \(_str_\) – path to the file for processing

  * **url** \(_str_\) – URL to call dedoc API

  * **split** \(_str_\) – 

type of document splitting into parts \(each part is returned separately\), default value “document” “document”: document is returned as a single langchain Document object

> \(don’t split\)

”page”: split document into pages \(works for PDF, DJVU, PPTX, PPT, ODP\) “node”: split document into tree nodes \(title nodes, list item nodes,

> raw text nodes\)

”line”: split document into lines

  * **with\_tables** \(_bool_\) – add tables to the result - each table is returned as a single langchain Document object

  * **dedoc** \(_Parameters used for document parsing via_\) – 

\(<https://dedoc.readthedocs.io/en/latest/parameters/parameters.html>\):

with\_attachments: enable attached files extraction recursion\_deep\_attachments: recursion level for attached files

> extraction, works only when with\_attachments==True

pdf\_with\_text\_layer: type of handler for parsing PDF documents,     

available options \[“true”, “false”, “tabby”, “auto”, “auto\_tabby” \(default\)\]

language: language of the document for PDF without a textual layer and     

images, available options \[“eng”, “rus”, “rus+eng” \(default\)\], the list of languages can be extended, please see <https://dedoc.readthedocs.io/en/latest/tutorials/add_new_language.html>

pages: page slice to define the reading range for parsing PDF documents is\_one\_column\_document: detect number of columns for PDF without

> a textual layer and images, available options \[“true”, “false”, “auto” \(default\)\]

document\_orientation: fix document orientation \(90, 180, 270 degrees\)     

for PDF without a textual layer and images, available options \[“auto” \(default\), “no\_change”\]

need\_header\_footer\_analysis: remove headers and footers from the output     

result for parsing PDF and images

need\_binarization: clean pages background \(binarize\) for PDF without a     

textual layer and images

need\_pdf\_table\_analysis: parse tables for PDF without a textual layer     

and images

delimiter: column separator for CSV, TSV files encoding: encoding of TXT, CSV, TSV

  * **with\_attachments** \(_str_ _|__bool_\)

  * **recursion\_deep\_attachments** \(_int_\)

  * **pdf\_with\_text\_layer** \(_str_\)

  * **language** \(_str_\)

  * **pages** \(_str_\)

  * **is\_one\_column\_document** \(_str_\)

  * **document\_orientation** \(_str_\)

  * **need\_header\_footer\_analysis** \(_str_ _|__bool_\)

  * **need\_binarization** \(_str_ _|__bool_\)

  * **need\_pdf\_table\_analysis** \(_str_ _|__bool_\)

  * **delimiter** \(_str_ _|__None_\)

  * **encoding** \(_str_ _|__None_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/dedoc.html#DedocAPIFileLoader.lazy_load)\#     

Lazily load documents.

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

Examples using DedocAPIFileLoader

  * [Dedoc](https://python.langchain.com/docs/integrations/document_loaders/dedoc/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)