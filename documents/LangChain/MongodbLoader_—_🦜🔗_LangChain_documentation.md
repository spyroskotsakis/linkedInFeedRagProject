# MongodbLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mongodb.MongodbLoader.html
**Word Count:** 296
**Links Count:** 419
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# MongodbLoader\#

_class _langchain\_community.document\_loaders.mongodb.MongodbLoader\(

    _connection\_string : str_,     _db\_name : str_,     _collection\_name : str_,     _\*_ ,     _filter\_criteria : Dict | None = None_,     _field\_names : Sequence\[str\] | None = None_,     _metadata\_names : Sequence\[str\] | None = None_,     _include\_db\_collection\_in\_metadata : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mongodb.html#MongodbLoader)\#     

Load MongoDB documents.

Initializes the MongoDB loader with necessary database connection details and configurations.

Parameters:     

  * **connection\_string** \(_str_\) – MongoDB connection URI.

  * **db\_name** \(_str_\) – Name of the database to connect to.

  * **collection\_name** \(_str_\) – Name of the collection to fetch documents from.

  * **filter\_criteria** \(_Optional_ _\[__Dict_ _\]_\) – MongoDB filter criteria for querying

  * **documents.** \(_extract from_\)

  * **field\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – List of field names to retrieve

  * **documents.**

  * **metadata\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Additional metadata fields to

  * **documents.**

  * **include\_db\_collection\_in\_metadata** \(_bool_\) – Flag to include database and

  * **metadata.** \(_collection names in_\)

Raises:     

  * **ImportError** – If the motor library is not installed.

  * **ValueError** – If any necessary argument is missing.

Methods

`__init__`\(connection\_string, db\_name, ...\[, ...\]\) | Initializes the MongoDB loader with necessary database connection details and configurations.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Asynchronously loads data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _connection\_string : str_,     _db\_name : str_,     _collection\_name : str_,     _\*_ ,     _filter\_criteria : Dict | None = None_,     _field\_names : Sequence\[str\] | None = None_,     _metadata\_names : Sequence\[str\] | None = None_,     _include\_db\_collection\_in\_metadata : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mongodb.html#MongodbLoader.__init__)\#     

Initializes the MongoDB loader with necessary database connection details and configurations.

Parameters:     

  * **connection\_string** \(_str_\) – MongoDB connection URI.

  * **db\_name** \(_str_\) – Name of the database to connect to.

  * **collection\_name** \(_str_\) – Name of the collection to fetch documents from.

  * **filter\_criteria** \(_Optional_ _\[__Dict_ _\]_\) – MongoDB filter criteria for querying

  * **documents.** \(_extract from_\)

  * **field\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – List of field names to retrieve

  * **documents.**

  * **metadata\_names** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Additional metadata fields to

  * **documents.**

  * **include\_db\_collection\_in\_metadata** \(_bool_\) – Flag to include database and

  * **metadata.** \(_collection names in_\)

Raises:     

  * **ImportError** – If the motor library is not installed.

  * **ValueError** – If any necessary argument is missing.

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mongodb.html#MongodbLoader.aload)\#     

Asynchronously loads data into Document objects.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mongodb.html#MongodbLoader.load)\#     

Load data into Document objects.

Attention:

This implementation starts an asyncio event loop which will only work if running in a sync env. In an async env, it should fail since there is already an event loop running.

This code should be updated to kick off the event loop from a separate thread if running within an async context.

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

Examples using MongodbLoader

  * [MongoDB](https://python.langchain.com/docs/integrations/document_loaders/mongodb/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)