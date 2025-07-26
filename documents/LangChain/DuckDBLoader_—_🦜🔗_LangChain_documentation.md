# DuckDBLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.duckdb_loader.DuckDBLoader.html
**Word Count:** 235
**Links Count:** 418
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# DuckDBLoader\#

_class _langchain\_community.document\_loaders.duckdb\_loader.DuckDBLoader\(

    _query : str_,     _database : str = ':memory:'_,     _read\_only : bool = False_,     _config : Dict\[str, str\] | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/duckdb_loader.html#DuckDBLoader)\#     

Load from DuckDB.

Each document represents one row of the result. The page\_content\_columns are written into the page\_content of the document. The metadata\_columns are written into the metadata of the document. By default, all columns are written into the page\_content and none into the metadata.

Parameters:     

  * **query** \(_str_\) – The query to execute.

  * **database** \(_str_\) – The database to connect to. Defaults to “:memory:”.

  * **read\_only** \(_bool_\) – Whether to open the database in read-only mode. Defaults to False.

  * **config** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – A dictionary of configuration options to pass to the database. Optional.

  * **page\_content\_columns** \(_List_ _\[__str_ _\]__|__None_\) – The columns to write into the page\_content of the document. Optional.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – The columns to write into the metadata of the document. Optional.

Methods

`__init__`\(query\[, database, read\_only, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _database : str = ':memory:'_,     _read\_only : bool = False_,     _config : Dict\[str, str\] | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/duckdb_loader.html#DuckDBLoader.__init__)\#     

Parameters:     

  * **query** \(_str_\) – The query to execute.

  * **database** \(_str_\) – The database to connect to. Defaults to “:memory:”.

  * **read\_only** \(_bool_\) – Whether to open the database in read-only mode. Defaults to False.

  * **config** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – A dictionary of configuration options to pass to the database. Optional.

  * **page\_content\_columns** \(_List_ _\[__str_ _\]__|__None_\) – The columns to write into the page\_content of the document. Optional.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – The columns to write into the metadata of the document. Optional.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/duckdb_loader.html#DuckDBLoader.load)\#     

Load data into Document objects.

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

Examples using DuckDBLoader

  * [DuckDB](https://python.langchain.com/docs/integrations/document_loaders/duckdb/)

__On this page