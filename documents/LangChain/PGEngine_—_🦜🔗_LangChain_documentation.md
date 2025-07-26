# PGEngine — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html
**Word Count:** 476
**Links Count:** 146
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# PGEngine\#

_class _langchain\_postgres.v2.engine.PGEngine\(

    _key : object_,     _pool : AsyncEngine_,     _loop : AbstractEventLoop | None_,     _thread : Thread | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine)\#     

A class for managing connections to a Postgres database.

PGEngine constructor.

Parameters:     

  * **key** \(_object_\) – Prevent direct constructor usage.

  * **pool** \(_AsyncEngine_\) – Async engine connection pool.

  * **loop** \(_Optional_ _\[__asyncio.AbstractEventLoop_ _\]_\) – Async event loop used to create the engine.

  * **thread** \(_Optional_ _\[__Thread_ _\]_\) – Thread used to create the engine async.

Raises:     

**Exception** – If the constructor is called directly by the user.

Methods

`__init__`\(key, pool, loop, thread\) | PGEngine constructor.   ---|---   `adrop_table`\(table\_name, \*\[, schema\_name\]\) |    `ainit_vectorstore_table`\(table\_name, ...\[, ...\]\) | Create a table for saving of vectors to be used with PGVectorStore.   `close`\(\) | Dispose of connection pool   `drop_table`\(table\_name, \*\[, schema\_name\]\) |    `from_connection_string`\(url, \*\*kwargs\) | Create an PGEngine instance from arguments   `from_engine`\(engine\[, loop\]\) | Create an PGEngine instance from an AsyncEngine.   `init_vectorstore_table`\(table\_name, ...\[, ...\]\) | Create a table for saving of vectors to be used with PGVectorStore.      \_\_init\_\_\(

    _key : object_,     _pool : AsyncEngine_,     _loop : AbstractEventLoop | None_,     _thread : Thread | None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.__init__)\#     

PGEngine constructor.

Parameters:     

  * **key** \(_object_\) – Prevent direct constructor usage.

  * **pool** \(_AsyncEngine_\) – Async engine connection pool.

  * **loop** \(_Optional_ _\[__asyncio.AbstractEventLoop_ _\]_\) – Async event loop used to create the engine.

  * **thread** \(_Optional_ _\[__Thread_ _\]_\) – Thread used to create the engine async.

Raises:     

**Exception** – If the constructor is called directly by the user.

Return type:     

None

_async _adrop\_table\(

    _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.adrop_table)\#     

Parameters:     

  * **table\_name** \(_str_\)

  * **schema\_name** \(_str_\)

Return type:     

None

_async _ainit\_vectorstore\_table\(

    _table\_name : str_,     _vector\_size : int_,     _\*_ ,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[[Column](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") | [ColumnDict](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict")\] | None = None_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _id\_column : str | [Column](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") | [ColumnDict](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict") = 'langchain\_id'_,     _overwrite\_existing : bool = False_,     _store\_metadata : bool = True_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.ainit_vectorstore_table)\#     

Create a table for saving of vectors to be used with PGVectorStore.

Parameters:     

  * **table\_name** \(_str_\) – The database table name.

  * **vector\_size** \(_int_\) – Vector size for the embedding model to be used.

  * **schema\_name** \(_str_\) – The schema name. Default: “public”.

  * **content\_column** \(_str_\) – Name of the column to store document content. Default: “page\_content”.

  * **embedding\_column** \(_str_\) – Name of the column to store vector embeddings. Default: “embedding”.

  * **metadata\_columns** \(_Optional_ _\[__list_ _\[__Union_ _\[_[_Column_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") _,_[_ColumnDict_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict") _\]__\]__\]_\) – A list of Columns to create for custom metadata. Default: None. Optional.

  * **metadata\_json\_column** \(_str_\) – The column to store extra metadata in JSON format. Default: “langchain\_metadata”. Optional.

  * **id\_column** \(_Union_ _\[__str_ _,_[_Column_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") _,_[_ColumnDict_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict") _\]_\) – Column to store ids. Default: “langchain\_id” column name with data type UUID. Optional.

  * **overwrite\_existing** \(_bool_\) – Whether to drop existing table. Default: False.

  * **store\_metadata** \(_bool_\) – Whether to store metadata in the table. Default: True.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Note that queries might be slow if the hybrid search column does not exist. For best hybrid search performance, consider creating a TSV column and adding GIN index. Default: None.

Return type:     

None

_async _close\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.close)\#     

Dispose of connection pool

Return type:     

None

drop\_table\(

    _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.drop_table)\#     

Parameters:     

  * **table\_name** \(_str_\)

  * **schema\_name** \(_str_\)

Return type:     

None

_classmethod _from\_connection\_string\(

    _url : str | URL_,     _\*\* kwargs: Any_, \) → PGEngine[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.from_connection_string)\#     

Create an PGEngine instance from arguments

Parameters:     

  * **url** \(_Optional_ _\[__str_ _\]_\) – the URL used to connect to a database. Use url or set other arguments.

  * **kwargs** \(_Any_\)

Raises:     

**ValueError** – If not all database url arguments are specified

Returns:     

PGEngine

Return type:     

_PGEngine_

_classmethod _from\_engine\(

    _engine : AsyncEngine_,     _loop : AbstractEventLoop | None = None_, \) → PGEngine[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.from_engine)\#     

Create an PGEngine instance from an AsyncEngine.

Parameters:     

  * **engine** \(_AsyncEngine_\)

  * **loop** \(_AbstractEventLoop_ _|__None_\)

Return type:     

_PGEngine_

init\_vectorstore\_table\(

    _table\_name : str_,     _vector\_size : int_,     _\*_ ,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[[Column](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") | [ColumnDict](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict")\] | None = None_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _id\_column : str | [Column](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") | [ColumnDict](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict") = 'langchain\_id'_,     _overwrite\_existing : bool = False_,     _store\_metadata : bool = True_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/engine.html#PGEngine.init_vectorstore_table)\#     

Create a table for saving of vectors to be used with PGVectorStore.

Parameters:     

  * **table\_name** \(_str_\) – The database table name.

  * **vector\_size** \(_int_\) – Vector size for the embedding model to be used.

  * **schema\_name** \(_str_\) – The schema name. Default: “public”.

  * **content\_column** \(_str_\) – Name of the column to store document content. Default: “page\_content”.

  * **embedding\_column** \(_str_\) – Name of the column to store vector embeddings. Default: “embedding”.

  * **metadata\_columns** \(_Optional_ _\[__list_ _\[__Union_ _\[_[_Column_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") _,_[_ColumnDict_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict") _\]__\]__\]_\) – A list of Columns to create for custom metadata. Default: None. Optional.

  * **metadata\_json\_column** \(_str_\) – The column to store extra metadata in JSON format. Default: “langchain\_metadata”. Optional.

  * **id\_column** \(_Union_ _\[__str_ _,_[_Column_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.Column.html#langchain_postgres.v2.engine.Column "langchain_postgres.v2.engine.Column") _,_[_ColumnDict_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.ColumnDict.html#langchain_postgres.v2.engine.ColumnDict "langchain_postgres.v2.engine.ColumnDict") _\]_\) – Column to store ids. Default: “langchain\_id” column name with data type UUID. Optional.

  * **overwrite\_existing** \(_bool_\) – Whether to drop existing table. Default: False.

  * **store\_metadata** \(_bool_\) – Whether to store metadata in the table. Default: True.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Note that queries might be slow if the hybrid search column does not exist. For best hybrid search performance, consider creating a TSV column and adding GIN index. Default: None.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)