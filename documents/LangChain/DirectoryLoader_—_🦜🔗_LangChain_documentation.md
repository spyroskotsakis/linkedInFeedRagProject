# DirectoryLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.directory.DirectoryLoader.html
**Word Count:** 421
**Links Count:** 432
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# DirectoryLoader\#

_class _langchain\_community.document\_loaders.directory.DirectoryLoader\(

    _path: str_,     _glob: ~typing.List\[str\] | ~typing.Tuple\[str\] | str = '\*\*/\[\!.\]\*'_,     _silent\_errors: bool = False_,     _load\_hidden: bool = False_,     _loader\_cls: ~typing.Type\[~langchain\_community.document\_loaders.unstructured.UnstructuredFileLoader\] | ~typing.Type\[~langchain\_community.document\_loaders.text.TextLoader\] | ~typing.Type\[~langchain\_community.document\_loaders.html\_bs.BSHTMLLoader\] | ~typing.Type\[~langchain\_community.document\_loaders.csv\_loader.CSVLoader\] = <class 'langchain\_community.document\_loaders.unstructured.UnstructuredFileLoader'>_,     _loader\_kwargs: dict | None = None_,     _recursive: bool = False_,     _show\_progress: bool = False_,     _use\_multithreading: bool = False_,     _max\_concurrency: int = 4_,     _\*_ ,     _exclude: ~typing.Sequence\[str\] | str = \(\)_,     _sample\_size: int = 0_,     _randomize\_sample: bool = False_,     _sample\_seed: int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/directory.html#DirectoryLoader)\#     

Load from a directory.

Initialize with a path to directory and how to glob over it.

Parameters:     

  * **path** \(_str_\) – Path to directory.

  * **glob** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _\]__|__str_\) – A glob pattern or list of glob patterns to use to find files. Defaults to “\*\*/\[\!.\]\*” \(all files except hidden\).

  * **exclude** \(_Sequence_ _\[__str_ _\]__|__str_\) – A pattern or list of patterns to exclude from results. Use glob syntax.

  * **silent\_errors** \(_bool_\) – Whether to silently ignore errors. Defaults to False.

  * **load\_hidden** \(_bool_\) – Whether to load hidden files. Defaults to False.

  * **loader\_cls** \(_Type_ _\[_[_UnstructuredFileLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredFileLoader.html#langchain_community.document_loaders.unstructured.UnstructuredFileLoader "langchain_community.document_loaders.unstructured.UnstructuredFileLoader") _\]__|__Type_ _\[_[_TextLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.text.TextLoader.html#langchain_community.document_loaders.text.TextLoader "langchain_community.document_loaders.text.TextLoader") _\]__|__Type_ _\[_[_BSHTMLLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html#langchain_community.document_loaders.html_bs.BSHTMLLoader "langchain_community.document_loaders.html_bs.BSHTMLLoader") _\]__|__Type_ _\[_[_CSVLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.csv_loader.CSVLoader.html#langchain_community.document_loaders.csv_loader.CSVLoader "langchain_community.document_loaders.csv_loader.CSVLoader") _\]_\) – Loader class to use for loading files. Defaults to UnstructuredFileLoader.

  * **loader\_kwargs** \(_dict_ _|__None_\) – Keyword arguments to pass to loader\_cls. Defaults to None.

  * **recursive** \(_bool_\) – Whether to recursively search for files. Defaults to False.

  * **show\_progress** \(_bool_\) – Whether to show a progress bar. Defaults to False.

  * **use\_multithreading** \(_bool_\) – Whether to use multithreading. Defaults to False.

  * **max\_concurrency** \(_int_\) – The maximum number of threads to use. Defaults to 4.

  * **sample\_size** \(_int_\) – The maximum number of files you would like to load from the directory.

  * **randomize\_sample** \(_bool_\) – Shuffle the files to get a random sample.

  * **sample\_seed** \(_int_ _|__None_\) – set the seed of the random shuffle for reproducibility.

Examples

Methods

`__init__`\(path\[, glob, silent\_errors, ...\]\) | Initialize with a path to directory and how to glob over it.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load documents lazily.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _path: str_,     _glob: ~typing.List\[str\] | ~typing.Tuple\[str\] | str = '\*\*/\[\!.\]\*'_,     _silent\_errors: bool = False_,     _load\_hidden: bool = False_,     _loader\_cls: ~typing.Type\[~langchain\_community.document\_loaders.unstructured.UnstructuredFileLoader\] | ~typing.Type\[~langchain\_community.document\_loaders.text.TextLoader\] | ~typing.Type\[~langchain\_community.document\_loaders.html\_bs.BSHTMLLoader\] | ~typing.Type\[~langchain\_community.document\_loaders.csv\_loader.CSVLoader\] = <class 'langchain\_community.document\_loaders.unstructured.UnstructuredFileLoader'>_,     _loader\_kwargs: dict | None = None_,     _recursive: bool = False_,     _show\_progress: bool = False_,     _use\_multithreading: bool = False_,     _max\_concurrency: int = 4_,     _\*_ ,     _exclude: ~typing.Sequence\[str\] | str = \(\)_,     _sample\_size: int = 0_,     _randomize\_sample: bool = False_,     _sample\_seed: int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/directory.html#DirectoryLoader.__init__)\#     

Initialize with a path to directory and how to glob over it.

Parameters:     

  * **path** \(_str_\) – Path to directory.

  * **glob** \(_List_ _\[__str_ _\]__|__Tuple_ _\[__str_ _\]__|__str_\) – A glob pattern or list of glob patterns to use to find files. Defaults to “\*\*/\[\!.\]\*” \(all files except hidden\).

  * **exclude** \(_Sequence_ _\[__str_ _\]__|__str_\) – A pattern or list of patterns to exclude from results. Use glob syntax.

  * **silent\_errors** \(_bool_\) – Whether to silently ignore errors. Defaults to False.

  * **load\_hidden** \(_bool_\) – Whether to load hidden files. Defaults to False.

  * **loader\_cls** \(_Type_ _\[_[_UnstructuredFileLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredFileLoader.html#langchain_community.document_loaders.unstructured.UnstructuredFileLoader "langchain_community.document_loaders.unstructured.UnstructuredFileLoader") _\]__|__Type_ _\[_[_TextLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.text.TextLoader.html#langchain_community.document_loaders.text.TextLoader "langchain_community.document_loaders.text.TextLoader") _\]__|__Type_ _\[_[_BSHTMLLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.html_bs.BSHTMLLoader.html#langchain_community.document_loaders.html_bs.BSHTMLLoader "langchain_community.document_loaders.html_bs.BSHTMLLoader") _\]__|__Type_ _\[_[_CSVLoader_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.csv_loader.CSVLoader.html#langchain_community.document_loaders.csv_loader.CSVLoader "langchain_community.document_loaders.csv_loader.CSVLoader") _\]_\) – Loader class to use for loading files. Defaults to UnstructuredFileLoader.

  * **loader\_kwargs** \(_dict_ _|__None_\) – Keyword arguments to pass to loader\_cls. Defaults to None.

  * **recursive** \(_bool_\) – Whether to recursively search for files. Defaults to False.

  * **show\_progress** \(_bool_\) – Whether to show a progress bar. Defaults to False.

  * **use\_multithreading** \(_bool_\) – Whether to use multithreading. Defaults to False.

  * **max\_concurrency** \(_int_\) – The maximum number of threads to use. Defaults to 4.

  * **sample\_size** \(_int_\) – The maximum number of files you would like to load from the directory.

  * **randomize\_sample** \(_bool_\) – Shuffle the files to get a random sample.

  * **sample\_seed** \(_int_ _|__None_\) – set the seed of the random shuffle for reproducibility.

Examples

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/directory.html#DirectoryLoader.lazy_load)\#     

Load documents lazily.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/directory.html#DirectoryLoader.load)\#     

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

Examples using DirectoryLoader

  * [Apache Doris](https://python.langchain.com/docs/integrations/vectorstores/apache_doris/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [How to load documents from a directory](https://python.langchain.com/docs/how_to/document_loader_directory/)

  * [StarRocks](https://python.langchain.com/docs/integrations/vectorstores/starrocks/)

__On this page