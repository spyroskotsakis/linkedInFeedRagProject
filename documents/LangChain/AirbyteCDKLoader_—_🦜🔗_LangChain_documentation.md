# AirbyteCDKLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airbyte.AirbyteCDKLoader.html
**Word Count:** 228
**Links Count:** 422
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# AirbyteCDKLoader\#

_class _langchain\_community.document\_loaders.airbyte.AirbyteCDKLoader\(

    _config : Mapping\[str, Any\]_,     _source\_class : Any_,     _stream\_name : str_,     _record\_handler : Callable\[\[Any, str | None\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _state : Any | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/airbyte.html#AirbyteCDKLoader)\#     

Load with an Airbyte source connector implemented using the CDK.

Initializes the loader.

Parameters:     

  * **config** \(_Mapping_ _\[__str_ _,__Any_ _\]_\) – The config to pass to the source connector.

  * **source\_class** \(_Any_\) – The source connector class.

  * **stream\_name** \(_str_\) – The name of the stream to load.

  * **record\_handler** \(_Callable_ _\[__\[__Any_ _,__str_ _|__None_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\) – A function that takes in a record and an optional id and returns a Document. If None, the record will be used as the document. Defaults to None.

  * **state** \(_Any_ _|__None_\) – The state to pass to the source connector. Defaults to None.

Attributes

`last_state` |    ---|---      Methods

`__init__`\(config, source\_class, stream\_name\) | Initializes the loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _config : Mapping\[str, Any\]_,     _source\_class : Any_,     _stream\_name : str_,     _record\_handler : Callable\[\[Any, str | None\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _state : Any | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/airbyte.html#AirbyteCDKLoader.__init__)\#     

Initializes the loader.

Parameters:     

  * **config** \(_Mapping_ _\[__str_ _,__Any_ _\]_\) – The config to pass to the source connector.

  * **source\_class** \(_Any_\) – The source connector class.

  * **stream\_name** \(_str_\) – The name of the stream to load.

  * **record\_handler** \(_Callable_ _\[__\[__Any_ _,__str_ _|__None_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\) – A function that takes in a record and an optional id and returns a Document. If None, the record will be used as the document. Defaults to None.

  * **state** \(_Any_ _|__None_\) – The state to pass to the source connector. Defaults to None.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/airbyte.html#AirbyteCDKLoader.lazy_load)\#     

A lazy loader for Documents.

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

Examples using AirbyteCDKLoader

  * [Airbyte CDK \(Deprecated\)](https://python.langchain.com/docs/integrations/document_loaders/airbyte_cdk/)

__On this page