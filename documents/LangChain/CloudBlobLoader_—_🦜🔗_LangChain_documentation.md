# CloudBlobLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blob_loaders.cloud_blob_loader.CloudBlobLoader.html
**Word Count:** 404
**Links Count:** 407
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# CloudBlobLoader\#

_class _langchain\_community.document\_loaders.blob\_loaders.cloud\_blob\_loader.CloudBlobLoader\(

    _url : str | AnyPath_,     _\*_ ,     _glob : str = '\*\*/\[\!.\]\*'_,     _exclude : Sequence\[str\] = \(\)_,     _suffixes : Sequence\[str\] | None = None_,     _show\_progress : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/cloud_blob_loader.html#CloudBlobLoader)\#     

Load blobs from cloud URL or file:.

Example:               loader = CloudBlobLoader("s3://mybucket/id")          for blob in loader.yield_blobs():         print(blob)     

Initialize with a url and how to glob over it.

Use \[CloudPathLib\]\(<https://cloudpathlib.drivendata.org/>\).

Parameters:     

  * **url** \(_str_ _|__AnyPath_\) – Cloud URL to load from. Supports s3://, az://, gs://, file:// schemes. If no scheme is provided, it is assumed to be a local file. If a path to a file is provided, glob/exclude/suffixes are ignored.

  * **glob** \(_str_\) – Glob pattern relative to the specified path by default set to pick up all non-hidden files

  * **exclude** \(_Sequence_ _\[__str_ _\]_\) – patterns to exclude from results, use glob syntax

  * **suffixes** \(_Sequence_ _\[__str_ _\]__|__None_\) – Provide to keep only files with these suffixes Useful when wanting to keep files with different suffixes Suffixes must include the dot, e.g. “.txt”

  * **show\_progress** \(_bool_\) – If true, will show a progress bar as the files are loaded. This forces an iteration through all matching files to count them prior to loading them.

Examples

Methods

`__init__`\(url, \*\[, glob, exclude, suffixes, ...\]\) | Initialize with a url and how to glob over it.   ---|---   `count_matching_files`\(\) | Count files that match the pattern without loading them.   `from_path`\(path, \*\[, encoding, mime\_type, ...\]\) | Load the blob from a path like object.   `yield_blobs`\(\) | Yield blobs that match the requested pattern.      \_\_init\_\_\(

    _url : str | AnyPath_,     _\*_ ,     _glob : str = '\*\*/\[\!.\]\*'_,     _exclude : Sequence\[str\] = \(\)_,     _suffixes : Sequence\[str\] | None = None_,     _show\_progress : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/cloud_blob_loader.html#CloudBlobLoader.__init__)\#     

Initialize with a url and how to glob over it.

Use \[CloudPathLib\]\(<https://cloudpathlib.drivendata.org/>\).

Parameters:     

  * **url** \(_str_ _|__AnyPath_\) – Cloud URL to load from. Supports s3://, az://, gs://, file:// schemes. If no scheme is provided, it is assumed to be a local file. If a path to a file is provided, glob/exclude/suffixes are ignored.

  * **glob** \(_str_\) – Glob pattern relative to the specified path by default set to pick up all non-hidden files

  * **exclude** \(_Sequence_ _\[__str_ _\]_\) – patterns to exclude from results, use glob syntax

  * **suffixes** \(_Sequence_ _\[__str_ _\]__|__None_\) – Provide to keep only files with these suffixes Useful when wanting to keep files with different suffixes Suffixes must include the dot, e.g. “.txt”

  * **show\_progress** \(_bool_\) – If true, will show a progress bar as the files are loaded. This forces an iteration through all matching files to count them prior to loading them.

Return type:     

None

Examples

count\_matching\_files\(\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/cloud_blob_loader.html#CloudBlobLoader.count_matching_files)\#     

Count files that match the pattern without loading them.

Return type:     

int

_classmethod _from\_path\(

    _path : AnyPath_,     _\*_ ,     _encoding : str = 'utf-8'_,     _mime\_type : str | None = None_,     _guess\_type : bool = True_,     _metadata : dict | None = None_, \) → [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/cloud_blob_loader.html#CloudBlobLoader.from_path)\#     

Load the blob from a path like object.

Parameters:     

  * **path** \(_AnyPath_\) – path like object to file to be read Supports s3://, az://, gs://, file:// schemes. If no scheme is provided, it is assumed to be a local file.

  * **encoding** \(_str_\) – Encoding to use if decoding the bytes into a string

  * **mime\_type** \(_str_ _|__None_\) – if provided, will be set as the mime-type of the data

  * **guess\_type** \(_bool_\) – If True, the mimetype will be guessed from the file extension, if a mime-type was not provided

  * **metadata** \(_dict_ _|__None_\) – Metadata to associate with the blob

Returns:     

Blob instance

Return type:     

[_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")

yield\_blobs\(\) → Iterable\[[Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blob_loaders/cloud_blob_loader.html#CloudBlobLoader.yield_blobs)\#     

Yield blobs that match the requested pattern.

Return type:     

_Iterable_\[[_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)