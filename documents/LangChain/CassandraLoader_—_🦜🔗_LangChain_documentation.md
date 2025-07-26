# CassandraLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.cassandra.CassandraLoader.html
**Word Count:** 412
**Links Count:** 419
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# CassandraLoader\#

_class _langchain\_community.document\_loaders.cassandra.CassandraLoader\(_table: Optional\[str\] = None, session: Optional\[Session\] = None, keyspace: Optional\[str\] = None, query: Union\[str, Statement, None\] = None, page\_content\_mapper: Callable\[\[Any\], str\] = <class 'str'>, metadata\_mapper: Callable\[\[Any\], dict\] = <function CassandraLoader.<lambda>>, \*, query\_parameters: Union\[dict, Sequence, None\] = None, query\_timeout: Optional\[float\] = <object object>, query\_trace: bool = False, query\_custom\_payload: Optional\[dict\] = None, query\_execution\_profile: Any = <object object>, query\_paging\_state: Any = None, query\_host: Optional\[Host\] = None, query\_execute\_as: Optional\[str\] = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cassandra.html#CassandraLoader)\#     

Document Loader for Apache Cassandra.

Parameters:     

  * **table** \(_Optional_ _\[__str_ _\]_\) – The table to load the data from. \(do not use together with the query parameter\)

  * **session** \(_Optional_ _\[__Session_ _\]_\) – The cassandra driver session. If not provided, the cassio resolved session will be used.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – The keyspace of the table. If not provided, the cassio resolved keyspace will be used.

  * **query** \(_Union_ _\[__str_ _,__Statement_ _,__None_ _\]_\) – The query used to load the data. \(do not use together with the table parameter\)

  * **page\_content\_mapper** \(_Callable_ _\[__\[__Any_ _\]__,__str_ _\]_\) – a function to convert a row to string page content. Defaults to the str representation of the row.

  * **metadata\_mapper** \(_Callable_ _\[__\[__Any_ _\]__,__dict_ _\]_\) – a function to convert a row to document metadata.

  * **query\_parameters** \(_Union_ _\[__dict_ _,__Sequence_ _,__None_ _\]_\) – The query parameters used when calling session.execute .

  * **query\_timeout** \(_Optional_ _\[__float_ _\]_\) – The query timeout used when calling session.execute .

  * **query\_trace** \(_bool_\) – Whether to use tracing when calling session.execute .

  * **query\_custom\_payload** \(_Optional_ _\[__dict_ _\]_\) – The query custom\_payload used when calling session.execute .

  * **query\_execution\_profile** \(_Any_\) – The query execution\_profile used when calling session.execute .

  * **query\_host** \(_Optional_ _\[__Host_ _\]_\) – The query host used when calling session.execute .

  * **query\_execute\_as** \(_Optional_ _\[__str_ _\]_\) – The query execute\_as used when calling session.execute .

  * **query\_paging\_state** \(_Any_\)

Methods

`__init__`\(\[table, session, keyspace, query, ...\]\) | Document Loader for Apache Cassandra.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(_table: Optional\[str\] = None, session: Optional\[Session\] = None, keyspace: Optional\[str\] = None, query: Union\[str, Statement, None\] = None, page\_content\_mapper: Callable\[\[Any\], str\] = <class 'str'>, metadata\_mapper: Callable\[\[Any\], dict\] = <function CassandraLoader.<lambda>>, \*, query\_parameters: Union\[dict, Sequence, None\] = None, query\_timeout: Optional\[float\] = <object object>, query\_trace: bool = False, query\_custom\_payload: Optional\[dict\] = None, query\_execution\_profile: Any = <object object>, query\_paging\_state: Any = None, query\_host: Optional\[Host\] = None, query\_execute\_as: Optional\[str\] = None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cassandra.html#CassandraLoader.__init__)\#     

Document Loader for Apache Cassandra.

Parameters:     

  * **table** \(_Optional_ _\[__str_ _\]_\) – The table to load the data from. \(do not use together with the query parameter\)

  * **session** \(_Optional_ _\[__Session_ _\]_\) – The cassandra driver session. If not provided, the cassio resolved session will be used.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – The keyspace of the table. If not provided, the cassio resolved keyspace will be used.

  * **query** \(_Union_ _\[__str_ _,__Statement_ _,__None_ _\]_\) – The query used to load the data. \(do not use together with the table parameter\)

  * **page\_content\_mapper** \(_Callable_ _\[__\[__Any_ _\]__,__str_ _\]_\) – a function to convert a row to string page content. Defaults to the str representation of the row.

  * **metadata\_mapper** \(_Callable_ _\[__\[__Any_ _\]__,__dict_ _\]_\) – a function to convert a row to document metadata.

  * **query\_parameters** \(_Union_ _\[__dict_ _,__Sequence_ _,__None_ _\]_\) – The query parameters used when calling session.execute .

  * **query\_timeout** \(_Optional_ _\[__float_ _\]_\) – The query timeout used when calling session.execute .

  * **query\_trace** \(_bool_\) – Whether to use tracing when calling session.execute .

  * **query\_custom\_payload** \(_Optional_ _\[__dict_ _\]_\) – The query custom\_payload used when calling session.execute .

  * **query\_execution\_profile** \(_Any_\) – The query execution\_profile used when calling session.execute .

  * **query\_host** \(_Optional_ _\[__Host_ _\]_\) – The query host used when calling session.execute .

  * **query\_execute\_as** \(_Optional_ _\[__str_ _\]_\) – The query execute\_as used when calling session.execute .

  * **query\_paging\_state** \(_Any_\)

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cassandra.html#CassandraLoader.alazy_load)\#     

A lazy loader for Documents.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/cassandra.html#CassandraLoader.lazy_load)\#     

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

Examples using CassandraLoader

  * [Cassandra](https://python.langchain.com/docs/integrations/document_loaders/cassandra/)

__On this page