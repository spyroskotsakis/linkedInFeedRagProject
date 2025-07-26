# FileSystemBlobLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.file_system.FileSystemBlobLoader.html
**Word Count:** 298
**Links Count:** 400
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# FileSystemBlobLoader\#

_class _langchain\_community.document\_loaders.blob\_loaders.file\_system.FileSystemBlobLoader\(

    _path : str | Path_,     _\*_ ,     _glob : str = '\*\*/\[\!.\]\*'_,     _exclude : Sequence\[str\] = \(\)_,     _suffixes : Sequence\[str\] | None = None_,     _show\_progress : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/file_system.html#FileSystemBlobLoader)\#     

Load blobs in the local file system.

Example:               from langchain_community.document_loaders.blob_loaders import FileSystemBlobLoader     loader = FileSystemBlobLoader("/path/to/directory")     for blob in loader.yield_blobs():         print(blob)  # noqa: T201     

Initialize with a path to directory and how to glob over it.

Parameters:     

  * **path** \(_str_ _|__Path_\) – Path to directory to load from or path to file to load. If a path to a file is provided, glob/exclude/suffixes are ignored.

  * **glob** \(_str_\) – Glob pattern relative to the specified path by default set to pick up all non-hidden files

  * **exclude** \(_Sequence_ _\[__str_ _\]_\) – patterns to exclude from results, use glob syntax

  * **suffixes** \(_Sequence_ _\[__str_ _\]__|__None_\) – Provide to keep only files with these suffixes Useful when wanting to keep files with different suffixes Suffixes must include the dot, e.g. “.txt”

  * **show\_progress** \(_bool_\) – If true, will show a progress bar as the files are loaded. This forces an iteration through all matching files to count them prior to loading them.

Examples

Methods

`__init__`\(path, \*\[, glob, exclude, suffixes, ...\]\) | Initialize with a path to directory and how to glob over it.   ---|---   `count_matching_files`\(\) | Count files that match the pattern without loading them.   `yield_blobs`\(\) | Yield blobs that match the requested pattern.      \_\_init\_\_\(

    _path : str | Path_,     _\*_ ,     _glob : str = '\*\*/\[\!.\]\*'_,     _exclude : Sequence\[str\] = \(\)_,     _suffixes : Sequence\[str\] | None = None_,     _show\_progress : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/file_system.html#FileSystemBlobLoader.__init__)\#     

Initialize with a path to directory and how to glob over it.

Parameters:     

  * **path** \(_str_ _|__Path_\) – Path to directory to load from or path to file to load. If a path to a file is provided, glob/exclude/suffixes are ignored.

  * **glob** \(_str_\) – Glob pattern relative to the specified path by default set to pick up all non-hidden files

  * **exclude** \(_Sequence_ _\[__str_ _\]_\) – patterns to exclude from results, use glob syntax

  * **suffixes** \(_Sequence_ _\[__str_ _\]__|__None_\) – Provide to keep only files with these suffixes Useful when wanting to keep files with different suffixes Suffixes must include the dot, e.g. “.txt”

  * **show\_progress** \(_bool_\) – If true, will show a progress bar as the files are loaded. This forces an iteration through all matching files to count them prior to loading them.

Return type:     

None

Examples

count\_matching\_files\(\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/file_system.html#FileSystemBlobLoader.count_matching_files)\#     

Count files that match the pattern without loading them.

Return type:     

int

yield\_blobs\(\) → Iterable\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/file_system.html#FileSystemBlobLoader.yield_blobs)\#     

Yield blobs that match the requested pattern.

Return type:     

_Iterable_\[[_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\]

Examples using FileSystemBlobLoader

  * [How to create a custom Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)