# SQLDatabaseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sql_database.SQLDatabaseLoader.html
**Word Count:** 412
**Links Count:** 429
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# SQLDatabaseLoader\#

_class _langchain\_community.document\_loaders.sql\_database.SQLDatabaseLoader\(

    _query : str | Select_,     _db : [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")_,     _\*_ ,     _parameters : Dict\[str, Any\] | None = None_,     _page\_content\_mapper : Callable\[\[...\], str\] | None = None_,     _metadata\_mapper : Callable\[\[...\], Dict\[str, Any\]\] | None = None_,     _source\_columns : Sequence\[str\] | None = None_,     _include\_rownum\_into\_metadata : bool = False_,     _include\_query\_into\_metadata : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sql_database.html#SQLDatabaseLoader)\#     

Load documents by querying database tables supported by SQLAlchemy.

For talking to the database, the document loader uses the SQLDatabase utility from the LangChain integration toolkit.

Each document represents one row of the result.

Parameters:     

  * **query** \(_str_ _|__Select_\) – The query to execute.

  * **db** \([_SQLDatabase_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")\) – A LangChain SQLDatabase, wrapping an SQLAlchemy engine.

  * **sqlalchemy\_kwargs** – More keyword arguments for SQLAlchemy’s create\_engine.

  * **parameters** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Parameters to pass to the query.

  * **page\_content\_mapper** \(_Callable_ _\[__\[__...__\]__,__str_ _\]__|__None_\) – Optional. Function to convert a row into a string to use as the page\_content of the document. By default, the loader serializes the whole row into a string, including all columns.

  * **metadata\_mapper** \(_Callable_ _\[__\[__...__\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional. Function to convert a row into a dictionary to use as the metadata of the document. By default, no columns are selected into the metadata dictionary.

  * **source\_columns** \(_Sequence_ _\[__str_ _\]__|__None_\) – Optional. The names of the columns to use as the source within the metadata dictionary.

  * **include\_rownum\_into\_metadata** \(_bool_\) – Optional. Whether to include the row number into the metadata dictionary. Default: False.

  * **include\_query\_into\_metadata** \(_bool_\) – Optional. Whether to include the query expression into the metadata dictionary. Default: False.

Methods

`__init__`\(query, db, \*\[, parameters, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `metadata_default_mapper`\(row\[, column\_names\]\) | A reasonable default function to convert a record into a "metadata" dictionary.   `page_content_default_mapper`\(row\[, column\_names\]\) | A reasonable default function to convert a record into a "page content" string.      \_\_init\_\_\(

    _query : str | Select_,     _db : [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")_,     _\*_ ,     _parameters : Dict\[str, Any\] | None = None_,     _page\_content\_mapper : Callable\[\[...\], str\] | None = None_,     _metadata\_mapper : Callable\[\[...\], Dict\[str, Any\]\] | None = None_,     _source\_columns : Sequence\[str\] | None = None_,     _include\_rownum\_into\_metadata : bool = False_,     _include\_query\_into\_metadata : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sql_database.html#SQLDatabaseLoader.__init__)\#     

Parameters:     

  * **query** \(_str_ _|__Select_\) – The query to execute.

  * **db** \([_SQLDatabase_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")\) – A LangChain SQLDatabase, wrapping an SQLAlchemy engine.

  * **sqlalchemy\_kwargs** – More keyword arguments for SQLAlchemy’s create\_engine.

  * **parameters** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Parameters to pass to the query.

  * **page\_content\_mapper** \(_Callable_ _\[__\[__...__\]__,__str_ _\]__|__None_\) – Optional. Function to convert a row into a string to use as the page\_content of the document. By default, the loader serializes the whole row into a string, including all columns.

  * **metadata\_mapper** \(_Callable_ _\[__\[__...__\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional. Function to convert a row into a dictionary to use as the metadata of the document. By default, no columns are selected into the metadata dictionary.

  * **source\_columns** \(_Sequence_ _\[__str_ _\]__|__None_\) – Optional. The names of the columns to use as the source within the metadata dictionary.

  * **include\_rownum\_into\_metadata** \(_bool_\) – Optional. Whether to include the row number into the metadata dictionary. Default: False.

  * **include\_query\_into\_metadata** \(_bool_\) – Optional. Whether to include the query expression into the metadata dictionary. Default: False.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sql_database.html#SQLDatabaseLoader.lazy_load)\#     

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

_static _metadata\_default\_mapper\(

    _row : RowMapping_,     _column\_names : List\[str\] | None = None_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sql_database.html#SQLDatabaseLoader.metadata_default_mapper)\#     

A reasonable default function to convert a record into a “metadata” dictionary.

Parameters:     

  * **row** \(_RowMapping_\)

  * **column\_names** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_Dict_\[str, _Any_\]

_static _page\_content\_default\_mapper\(

    _row : RowMapping_,     _column\_names : List\[str\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/sql_database.html#SQLDatabaseLoader.page_content_default_mapper)\#     

A reasonable default function to convert a record into a “page content” string.

Parameters:     

  * **row** \(_RowMapping_\)

  * **column\_names** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)