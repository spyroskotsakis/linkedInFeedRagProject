# UnstructuredLakeFSLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.lakefs.UnstructuredLakeFSLoader.html
**Word Count:** 87
**Links Count:** 416
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# UnstructuredLakeFSLoader\#

_class _langchain\_community.document\_loaders.lakefs.UnstructuredLakeFSLoader\(

    _url : str_,     _repo : str_,     _ref : str = 'main'_,     _path : str = ''_,     _presign : bool = True_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#UnstructuredLakeFSLoader)\#     

Load from lakeFS as unstructured data.

Initialize UnstructuredLakeFSLoader.

Args:

Parameters:     

  * **lakefs\_access\_key**

  * **lakefs\_secret\_key**

  * **lakefs\_endpoint**

  * **repo** \(_str_\)

  * **ref** \(_str_\)

  * **url** \(_str_\)

  * **path** \(_str_\)

  * **presign** \(_bool_\)

  * **unstructured\_kwargs** \(_Any_\)

Methods

`__init__`\(url, repo\[, ref, path, presign\]\) | Initialize UnstructuredLakeFSLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _url : str_,     _repo : str_,     _ref : str = 'main'_,     _path : str = ''_,     _presign : bool = True_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/lakefs.html#UnstructuredLakeFSLoader.__init__)\#     

Initialize UnstructuredLakeFSLoader.

Args:

Parameters:     

  * **lakefs\_access\_key**

  * **lakefs\_secret\_key**

  * **lakefs\_endpoint**

  * **repo** \(_str_\)

  * **ref** \(_str_\)

  * **url** \(_str_\)

  * **path** \(_str_\)

  * **presign** \(_bool_\)

  * **unstructured\_kwargs** \(_Any_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load file.

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

__On this page