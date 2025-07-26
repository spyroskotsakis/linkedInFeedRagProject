# BibtexLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.bibtex.BibtexLoader.html
**Word Count:** 282
**Links Count:** 423
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# BibtexLoader\#

_class _langchain\_community.document\_loaders.bibtex.BibtexLoader\(

    _file\_path : str_,     _\*_ ,     _parser : [BibtexparserWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bibtex.BibtexparserWrapper.html#langchain_community.utilities.bibtex.BibtexparserWrapper "langchain_community.utilities.bibtex.BibtexparserWrapper") | None = None_,     _max\_docs : int | None = None_,     _max\_content\_chars : int | None = 4000_,     _load\_extra\_metadata : bool = False_,     _file\_pattern : str = '\[^:\]+\\\\.pdf'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/bibtex.html#BibtexLoader)\#     

Load a bibtex file.

Each document represents one entry from the bibtex file.

If a PDF file is present in the file bibtex field, the original PDF is loaded into the document text. If no such file entry is present, the abstract field is used instead.

Initialize the BibtexLoader.

Parameters:     

  * **file\_path** \(_str_\) – Path to the bibtex file.

  * **parser** \([_BibtexparserWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bibtex.BibtexparserWrapper.html#langchain_community.utilities.bibtex.BibtexparserWrapper "langchain_community.utilities.bibtex.BibtexparserWrapper") _|__None_\) – The parser to use. If None, a default parser is used.

  * **max\_docs** \(_int_ _|__None_\) – Max number of associated documents to load. Use -1 means no limit.

  * **max\_content\_chars** \(_int_ _|__None_\) – Maximum number of characters to load from the PDF.

  * **load\_extra\_metadata** \(_bool_\) – Whether to load extra metadata from the PDF.

  * **file\_pattern** \(_str_\) – Regex pattern to match the file name in the bibtex.

Methods

`__init__`\(file\_path, \*\[, parser, max\_docs, ...\]\) | Initialize the BibtexLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load bibtex file using bibtexparser and get the article texts plus the article metadata.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str_,     _\*_ ,     _parser : [BibtexparserWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bibtex.BibtexparserWrapper.html#langchain_community.utilities.bibtex.BibtexparserWrapper "langchain_community.utilities.bibtex.BibtexparserWrapper") | None = None_,     _max\_docs : int | None = None_,     _max\_content\_chars : int | None = 4000_,     _load\_extra\_metadata : bool = False_,     _file\_pattern : str = '\[^:\]+\\\\.pdf'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/bibtex.html#BibtexLoader.__init__)\#     

Initialize the BibtexLoader.

Parameters:     

  * **file\_path** \(_str_\) – Path to the bibtex file.

  * **parser** \([_BibtexparserWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.bibtex.BibtexparserWrapper.html#langchain_community.utilities.bibtex.BibtexparserWrapper "langchain_community.utilities.bibtex.BibtexparserWrapper") _|__None_\) – The parser to use. If None, a default parser is used.

  * **max\_docs** \(_int_ _|__None_\) – Max number of associated documents to load. Use -1 means no limit.

  * **max\_content\_chars** \(_int_ _|__None_\) – Maximum number of characters to load from the PDF.

  * **load\_extra\_metadata** \(_bool_\) – Whether to load extra metadata from the PDF.

  * **file\_pattern** \(_str_\) – Regex pattern to match the file name in the bibtex.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/bibtex.html#BibtexLoader.lazy_load)\#     

Load bibtex file using bibtexparser and get the article texts plus the article metadata. See <https://bibtexparser.readthedocs.io/en/master/>

Returns:     

a list of documents with the document.page\_content in text format

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

Examples using BibtexLoader

  * [BibTeX](https://python.langchain.com/docs/integrations/document_loaders/bibtex/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)