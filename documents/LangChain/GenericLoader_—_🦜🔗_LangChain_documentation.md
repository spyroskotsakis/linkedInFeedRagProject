# GenericLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.generic.GenericLoader.html
**Word Count:** 379
**Links Count:** 443
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# GenericLoader\#

_class _langchain\_community.document\_loaders.generic.GenericLoader\(

    _blob\_loader : [BlobLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")_,     _blob\_parser : [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/generic.html#GenericLoader)\#     

Generic Document Loader.

A generic document loader that allows combining an arbitrary blob loader with a blob parser.

Examples

Parse a specific PDF file:                from langchain_community.document_loaders import GenericLoader      from langchain_community.document_loaders.parsers.pdf import PyPDFParser           # Recursively load all text files in a directory.      loader = GenericLoader.from_filesystem(          "my_lovely_pdf.pdf",          parser=PyPDFParser()      )          .. code-block:: python               from langchain_community.document_loaders import GenericLoader          from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader                    loader = GenericLoader.from_filesystem(              path="path/to/directory",              glob="**/[!.]*",              suffixes=[".pdf"],              show_progress=True,          )               docs = loader.lazy_load()          next(docs)     

Example instantiations to change which files are loaded:               # Recursively load all text files in a directory.     loader = GenericLoader.from_filesystem("/path/to/dir", glob="**/*.txt")          # Recursively load all non-hidden files in a directory.     loader = GenericLoader.from_filesystem("/path/to/dir", glob="**/[!.]*")          # Load all files in a directory without recursion.     loader = GenericLoader.from_filesystem("/path/to/dir", glob="*")     

Example instantiations to change which parser is used:               from langchain_community.document_loaders.parsers.pdf import PyPDFParser          # Recursively load all text files in a directory.     loader = GenericLoader.from_filesystem(         "/path/to/dir",         glob="**/*.pdf",         parser=PyPDFParser()     )     

A generic document loader.

Parameters:     

  * **blob\_loader** \([_BlobLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")\) – A blob loader which knows how to yield blobs

  * **blob\_parser** \([_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\) – A blob parser which knows how to parse blobs into documents

Methods

`__init__`\(blob\_loader, blob\_parser\) | A generic document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `from_filesystem`\(path, \*\[, glob, exclude, ...\]\) | Create a generic document loader using a filesystem blob loader.   `get_parser`\(\*\*kwargs\) | Override this method to associate a default parser with the class.   `lazy_load`\(\) | Load documents lazily.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load all documents and split them into sentences.      \_\_init\_\_\(

    _blob\_loader : [BlobLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")_,     _blob\_parser : [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/generic.html#GenericLoader.__init__)\#     

A generic document loader.

Parameters:     

  * **blob\_loader** \([_BlobLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.blob_loaders.BlobLoader.html#langchain_core.document_loaders.blob_loaders.BlobLoader "langchain_core.document_loaders.blob_loaders.BlobLoader")\) – A blob loader which knows how to yield blobs

  * **blob\_parser** \([_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")\) – A blob parser which knows how to parse blobs into documents

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

    _path : str | Path_,     _\*_ ,     _glob : str = '\*\*/\[\!.\]\*'_,     _exclude : Sequence\[str\] = \(\)_,     _suffixes : Sequence\[str\] | None = None_,     _show\_progress : bool = False_,     _parser : Literal\['default'\] | [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser") = 'default'_,     _parser\_kwargs : dict | None = None_, \) → GenericLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/generic.html#GenericLoader.from_filesystem)\#     

Create a generic document loader using a filesystem blob loader.

Parameters:     

  * **path** \(_str_ _|__Path_\) – 

The path to the directory to load documents from OR the path to a single file to load. If this is a file, glob, exclude, suffixes

> will be ignored.

  * **glob** \(_str_\) – The glob pattern to use to find documents.

  * **suffixes** \(_Sequence_ _\[__str_ _\]__|__None_\) – The suffixes to use to filter documents. If None, all files matching the glob will be loaded.

  * **exclude** \(_Sequence_ _\[__str_ _\]_\) – A list of patterns to exclude from the loader.

  * **show\_progress** \(_bool_\) – Whether to show a progress bar or not \(requires tqdm\). Proxies to the file system loader.

  * **parser** \(_Literal_ _\[__'default'__\]__|__~langchain\_core.document\_loaders.base.BaseBlobParser_\) – A blob parser which knows how to parse blobs into documents, will instantiate a default parser if not provided. The default can be overridden by either passing a parser or setting the class attribute blob\_parser \(the latter should be used with inheritance\).

  * **parser\_kwargs** \(_dict_ _|__None_\) – Keyword arguments to pass to the parser.

Returns:     

A generic document loader.

Return type:     

_GenericLoader_

_static _get\_parser\(

    _\*\* kwargs: Any_, \) → [BaseBlobParser](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/generic.html#GenericLoader.get_parser)\#     

Override this method to associate a default parser with the class.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

[_BaseBlobParser_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseBlobParser.html#langchain_core.document_loaders.base.BaseBlobParser "langchain_core.document_loaders.base.BaseBlobParser")

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/generic.html#GenericLoader.lazy_load)\#     

Load documents lazily. Use this when working at a large scale.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/generic.html#GenericLoader.load_and_split)\#     

Load all documents and split them into sentences.

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\)

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using GenericLoader

  * [Grobid](https://python.langchain.com/docs/integrations/document_loaders/grobid/)

  * [How to create a custom Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/)

  * [Source Code](https://python.langchain.com/docs/integrations/document_loaders/source_code/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)