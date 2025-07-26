# TiDBLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tidb.TiDBLoader.html
**Word Count:** 196
**Links Count:** 418
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# TiDBLoader\#

_class _langchain\_community.document\_loaders.tidb.TiDBLoader\(

    _connection\_string : str_,     _query : str_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_,     _engine\_args : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tidb.html#TiDBLoader)\#     

Load documents from TiDB.

Initialize TiDB document loader.

Parameters:     

  * **connection\_string** \(_str_\) – The connection string for the TiDB database, format: “mysql+pymysql://root@127.0.0.1:4000/test”.

  * **query** \(_str_\) – The query to run in TiDB.

  * **page\_content\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document page\_content, default\(None\) to all columns.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document metadata, default\(None\) to no columns.

  * **engine\_args** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Additional arguments to pass to sqlalchemy engine.

Methods

`__init__`\(connection\_string, query\[, ...\]\) | Initialize TiDB document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load TiDB data into document objects.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _connection\_string : str_,     _query : str_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_,     _engine\_args : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tidb.html#TiDBLoader.__init__)\#     

Initialize TiDB document loader.

Parameters:     

  * **connection\_string** \(_str_\) – The connection string for the TiDB database, format: “mysql+pymysql://root@127.0.0.1:4000/test”.

  * **query** \(_str_\) – The query to run in TiDB.

  * **page\_content\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document page\_content, default\(None\) to all columns.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document metadata, default\(None\) to no columns.

  * **engine\_args** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Additional arguments to pass to sqlalchemy engine.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tidb.html#TiDBLoader.lazy_load)\#     

Lazy load TiDB data into document objects.

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

Examples using TiDBLoader

  * [TiDB](https://python.langchain.com/docs/integrations/document_loaders/tidb/)

__On this page