# GCSFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.gcs_file.GCSFileLoader.html
**Word Count:** 258
**Links Count:** 421
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# GCSFileLoader\#

_class _langchain\_community.document\_loaders.gcs\_file.GCSFileLoader\(

    _project\_name : str_,     _bucket : str_,     _blob : str_,     _loader\_func : Callable\[\[str\], [BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gcs_file.html#GCSFileLoader)\#     

Deprecated since version 0.0.32: Use `:class:`~langchain_google_community.GCSFileLoader`` instead. It will not be removed until langchain-community==1.0.

Load from GCS file.

Initialize with bucket and key name.

Parameters:     

  * **project\_name** \(_str_\) – The name of the project to load

  * **bucket** \(_str_\) – The name of the GCS bucket.

  * **blob** \(_str_\) – The name of the GCS blob to load.

  * **loader\_func** \(_Callable_ _\[__\[__str_ _\]__,_[_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _\]__|__None_\) – A loader function that instantiates a loader based on a file\_path argument. If nothing is provided, the UnstructuredFileLoader is used.

Examples

To use an alternative PDF loader: >> from from langchain\_community.document\_loaders import PyPDFLoader >> loader = GCSFileLoader\(…, loader\_func=PyPDFLoader\)

To use UnstructuredFileLoader with additional arguments: >> loader = GCSFileLoader\(…, >> loader\_func=lambda x: UnstructuredFileLoader\(x, mode=”elements”\)\)

Methods

`__init__`\(project\_name, bucket, blob\[, ...\]\) | Initialize with bucket and key name.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _project\_name : str_,     _bucket : str_,     _blob : str_,     _loader\_func : Callable\[\[str\], [BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gcs_file.html#GCSFileLoader.__init__)\#     

Initialize with bucket and key name.

Parameters:     

  * **project\_name** \(_str_\) – The name of the project to load

  * **bucket** \(_str_\) – The name of the GCS bucket.

  * **blob** \(_str_\) – The name of the GCS blob to load.

  * **loader\_func** \(_Callable_ _\[__\[__str_ _\]__,_[_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _\]__|__None_\) – A loader function that instantiates a loader based on a file\_path argument. If nothing is provided, the UnstructuredFileLoader is used.

Examples

To use an alternative PDF loader: >> from from langchain\_community.document\_loaders import PyPDFLoader >> loader = GCSFileLoader\(…, loader\_func=PyPDFLoader\)

To use UnstructuredFileLoader with additional arguments: >> loader = GCSFileLoader\(…, >> loader\_func=lambda x: UnstructuredFileLoader\(x, mode=”elements”\)\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gcs_file.html#GCSFileLoader.load)\#     

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

__On this page