# PebbloTextLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pebblo.PebbloTextLoader.html
**Word Count:** 210
**Links Count:** 418
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# PebbloTextLoader\#

_class _langchain\_community.document\_loaders.pebblo.PebbloTextLoader\(

    _texts : Iterable\[str\]_,     _\*_ ,     _source : str | None = None_,     _ids : List\[str\] | None = None_,     _metadata : Dict\[str, Any\] | None = None_,     _metadatas : List\[Dict\[str, Any\]\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloTextLoader)\#     

Loader for text data.

Since PebbloSafeLoader is a wrapper around document loaders, this loader is used to load text data directly into Documents.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of text data.

  * **source** \(_str_ _|__None_\) – Source of the text data. Optional. Defaults to None.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of unique identifiers for each text. Optional. Defaults to None.

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Metadata for all texts. Optional. Defaults to None.

  * **metadatas** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – List of metadata for each text. Optional. Defaults to None.

Methods

`__init__`\(texts, \*\[, source, ids, metadata, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load text data into Documents.   `load`\(\) | Load text data into Documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _texts : Iterable\[str\]_,     _\*_ ,     _source : str | None = None_,     _ids : List\[str\] | None = None_,     _metadata : Dict\[str, Any\] | None = None_,     _metadatas : List\[Dict\[str, Any\]\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloTextLoader.__init__)\#     

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of text data.

  * **source** \(_str_ _|__None_\) – Source of the text data. Optional. Defaults to None.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of unique identifiers for each text. Optional. Defaults to None.

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Metadata for all texts. Optional. Defaults to None.

  * **metadatas** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – List of metadata for each text. Optional. Defaults to None.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloTextLoader.lazy_load)\#     

Lazy load text data into Documents.

Returns:     

Iterator of Documents

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pebblo.html#PebbloTextLoader.load)\#     

Load text data into Documents.

Returns:     

List of Documents

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)