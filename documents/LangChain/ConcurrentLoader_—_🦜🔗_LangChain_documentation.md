# ConcurrentLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.concurrent.ConcurrentLoader.html
**Word Count:** 261
**Links Count:** 438
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# ConcurrentLoader\#

_class _langchain\_community.document\_loaders.concurrent.ConcurrentLoader\(

    _blob\_loader : [BlobLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")_,     _blob\_parser : [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")_,     _num\_workers : int = 4_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/concurrent.html#ConcurrentLoader)\#     

Load and pars Documents concurrently.

A generic document loader.

Parameters:     

  * **blob\_loader** \([_BlobLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")\) – A blob loader which knows how to yield blobs

  * **blob\_parser** \([_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\) – A blob parser which knows how to parse blobs into documents

  * **num\_workers** \(_int_\)

Methods

`__init__`\(blob\_loader, blob\_parser\[, num\_workers\]\) | A generic document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `from_filesystem`\(path, \*\[, glob, exclude, ...\]\) | Create a concurrent generic document loader using a filesystem blob loader.   `get_parser`\(\*\*kwargs\) | Override this method to associate a default parser with the class.   `lazy_load`\(\) | Load documents lazily with concurrent parsing.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load all documents and split them into sentences.      \_\_init\_\_\(

    _blob\_loader : [BlobLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")_,     _blob\_parser : [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")_,     _num\_workers : int = 4_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/concurrent.html#ConcurrentLoader.__init__)\#     

A generic document loader.

Parameters:     

  * **blob\_loader** \([_BlobLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")\) – A blob loader which knows how to yield blobs

  * **blob\_parser** \([_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\) – A blob parser which knows how to parse blobs into documents

  * **num\_workers** \(_int_\)

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

_classmethod _from\_filesystem\(

    _path : str | Path_,     _\*_ ,     _glob : str = '\*\*/\[\!.\]\*'_,     _exclude : Sequence\[str\] = \(\)_,     _suffixes : Sequence\[str\] | None = None_,     _show\_progress : bool = False_,     _parser : Literal\['default'\] | [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") = 'default'_,     _num\_workers : int = 4_,     _parser\_kwargs : dict | None = None_, \) → ConcurrentLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/concurrent.html#ConcurrentLoader.from_filesystem)\#     

Create a concurrent generic document loader using a filesystem blob loader.

Parameters:     

  * **path** \(_str_ _|__Path_\) – The path to the directory to load documents from.

  * **glob** \(_str_\) – The glob pattern to use to find documents.

  * **suffixes** \(_Sequence_ _\[__str_ _\]__|__None_\) – The suffixes to use to filter documents. If None, all files matching the glob will be loaded.

  * **exclude** \(_Sequence_ _\[__str_ _\]_\) – A list of patterns to exclude from the loader.

  * **show\_progress** \(_bool_\) – Whether to show a progress bar or not \(requires tqdm\). Proxies to the file system loader.

  * **parser** \(_Literal_ _\[__'default'__\]__|__~langchain\_core.document\_loaders.base.BaseBlobParser_\) – A blob parser which knows how to parse blobs into documents

  * **num\_workers** \(_int_\) – Max number of concurrent workers to use.

  * **parser\_kwargs** \(_dict_ _|__None_\) – Keyword arguments to pass to the parser.

Return type:     

_ConcurrentLoader_

_static _get\_parser\(

    _\*\* kwargs: Any_, \) → [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\#     

Override this method to associate a default parser with the class.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

[_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/concurrent.html#ConcurrentLoader.lazy_load)\#     

Load documents lazily with concurrent parsing.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load all documents and split them into sentences.

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\)

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using ConcurrentLoader

  * [Concurrent Loader](https://python.langchain.com/docs/integrations/document_loaders/concurrent/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)