# NotebookLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notebook.NotebookLoader.html
**Word Count:** 203
**Links Count:** 418
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# NotebookLoader\#

_class _langchain\_community.document\_loaders.notebook.NotebookLoader\(

    _path : str | Path_,     _include\_outputs : bool = False_,     _max\_output\_length : int = 10_,     _remove\_newline : bool = False_,     _traceback : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notebook.html#NotebookLoader)\#     

Load Jupyter notebook \(.ipynb\) files.

Initialize with a path.

Parameters:     

  * **path** \(_str_ _|__Path_\) – The path to load the notebook from.

  * **include\_outputs** \(_bool_\) – Whether to include the outputs of the cell. Defaults to False.

  * **max\_output\_length** \(_int_\) – Maximum length of the output to be displayed. Defaults to 10.

  * **remove\_newline** \(_bool_\) – Whether to remove newlines from the notebook. Defaults to False.

  * **traceback** \(_bool_\) – Whether to return a traceback of the error. Defaults to False.

Methods

`__init__`\(path\[, include\_outputs, ...\]\) | Initialize with a path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _path : str | Path_,     _include\_outputs : bool = False_,     _max\_output\_length : int = 10_,     _remove\_newline : bool = False_,     _traceback : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notebook.html#NotebookLoader.__init__)\#     

Initialize with a path.

Parameters:     

  * **path** \(_str_ _|__Path_\) – The path to load the notebook from.

  * **include\_outputs** \(_bool_\) – Whether to include the outputs of the cell. Defaults to False.

  * **max\_output\_length** \(_int_\) – Maximum length of the output to be displayed. Defaults to 10.

  * **remove\_newline** \(_bool_\) – Whether to remove newlines from the notebook. Defaults to False.

  * **traceback** \(_bool_\) – Whether to return a traceback of the error. Defaults to False.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notebook.html#NotebookLoader.load)\#     

Load documents.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using NotebookLoader

  * [Jupyter Notebook](https://python.langchain.com/docs/integrations/document_loaders/jupyter_notebook/)

__On this page