# SQLDatabase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html
**Word Count:** 747
**Links Count:** 314
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# SQLDatabase\#

_class _langchain\_community.utilities.sql\_database.SQLDatabase\(

    _engine : Engine_,     _schema : str | None = None_,     _metadata : MetaData | None = None_,     _ignore\_tables : List\[str\] | None = None_,     _include\_tables : List\[str\] | None = None_,     _sample\_rows\_in\_table\_info : int = 3_,     _indexes\_in\_table\_info : bool = False_,     _custom\_table\_info : dict | None = None_,     _view\_support : bool = False_,     _max\_string\_length : int = 300_,     _lazy\_table\_reflection : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase)\#     

SQLAlchemy wrapper around a database.

Create engine from database URI.

Attributes

`dialect` | Return string representation of dialect to use.   ---|---   `table_info` | Information about all tables in the database.      Methods

`__init__`\(engine\[, schema, metadata, ...\]\) | Create engine from database URI.   ---|---   `from_cnosdb`\(\[url, user, password, tenant, ...\]\) | Class method to create an SQLDatabase instance from a CnosDB connection.   `from_databricks`\(catalog, schema\[, host, ...\]\) |    `from_uri`\(database\_uri\[, engine\_args\]\) | Construct a SQLAlchemy engine from URI.   `get_context`\(\) | Return db context that you may want in agent prompt.   `get_table_info`\(\[table\_names, get\_col\_comments\]\) | Get information about specified tables.   `get_table_info_no_throw`\(\[table\_names\]\) | Get information about specified tables.   `get_table_names`\(\) |    `get_usable_table_names`\(\) | Get names of tables available.   `run`\(command\[, fetch, include\_columns, ...\]\) | Execute a SQL command and return a string representing the results.   `run_no_throw`\(command\[, fetch, ...\]\) | Execute a SQL command and return a string representing the results.      Parameters:     

  * **engine** \(_Engine_\)

  * **schema** \(_Optional_ _\[__str_ _\]_\)

  * **metadata** \(_Optional_ _\[__MetaData_ _\]_\)

  * **ignore\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **include\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **sample\_rows\_in\_table\_info** \(_int_\)

  * **indexes\_in\_table\_info** \(_bool_\)

  * **custom\_table\_info** \(_Optional_ _\[__dict_ _\]_\)

  * **view\_support** \(_bool_\)

  * **max\_string\_length** \(_int_\)

  * **lazy\_table\_reflection** \(_bool_\)

\_\_init\_\_\(

    _engine : Engine_,     _schema : str | None = None_,     _metadata : MetaData | None = None_,     _ignore\_tables : List\[str\] | None = None_,     _include\_tables : List\[str\] | None = None_,     _sample\_rows\_in\_table\_info : int = 3_,     _indexes\_in\_table\_info : bool = False_,     _custom\_table\_info : dict | None = None_,     _view\_support : bool = False_,     _max\_string\_length : int = 300_,     _lazy\_table\_reflection : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.__init__)\#     

Create engine from database URI.

Parameters:     

  * **engine** \(_Engine_\)

  * **schema** \(_str_ _|__None_\)

  * **metadata** \(_MetaData_ _|__None_\)

  * **ignore\_tables** \(_List_ _\[__str_ _\]__|__None_\)

  * **include\_tables** \(_List_ _\[__str_ _\]__|__None_\)

  * **sample\_rows\_in\_table\_info** \(_int_\)

  * **indexes\_in\_table\_info** \(_bool_\)

  * **custom\_table\_info** \(_dict_ _|__None_\)

  * **view\_support** \(_bool_\)

  * **max\_string\_length** \(_int_\)

  * **lazy\_table\_reflection** \(_bool_\)

_classmethod _from\_cnosdb\(

    _url : str = '127.0.0.1:8902'_,     _user : str = 'root'_,     _password : str = ''_,     _tenant : str = 'cnosdb'_,     _database : str = 'public'_, \) → SQLDatabase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.from_cnosdb)\#     

Class method to create an SQLDatabase instance from a CnosDB connection. This method requires the ‘cnos-connector’ package. If not installed, it can be added using pip install cnos-connector.

Parameters:     

  * **url** \(_str_\) – The HTTP connection host name and port number of the CnosDB service, excluding “<http://>” or “<https://>”, with a default value of “127.0.0.1:8902”.

  * **user** \(_str_\) – The username used to connect to the CnosDB service, with a default value of “root”.

  * **password** \(_str_\) – The password of the user connecting to the CnosDB service, with a default value of “”.

  * **tenant** \(_str_\) – The name of the tenant used to connect to the CnosDB service, with a default value of “cnosdb”.

  * **database** \(_str_\) – The name of the database in the CnosDB tenant.

Returns:     

An instance of SQLDatabase configured with the provided CnosDB connection details.

Return type:     

SQLDatabase

_classmethod _from\_databricks\(

    _catalog : str_,     _schema : str_,     _host : str | None = None_,     _api\_token : str | None = None_,     _warehouse\_id : str | None = None_,     _cluster\_id : str | None = None_,     _engine\_args : dict | None = None_,     _\*\* kwargs: Any_, \) → SQLDatabase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.from_databricks)\#     

Deprecated since version 0.3.18: For performing structured retrieval using Databricks SQL, see the latest best practices and recommended APIs at <https://docs.unitycatalog.io/ai/integrations/langchain/> instead It will not be removed until langchain-community==1.0.

Class method to create an SQLDatabase instance from a Databricks connection. This method requires the ‘databricks-sql-connector’ package. If not installed, it can be added using pip install databricks-sql-connector.

Parameters:     

  * **catalog** \(_str_\) – The catalog name in the Databricks database.

  * **schema** \(_str_\) – The schema name in the catalog.

  * **host** \(_Optional_ _\[__str_ _\]_\) – The Databricks workspace hostname, excluding ‘<https://>’ part. If not provided, it attempts to fetch from the environment variable ‘DATABRICKS\_HOST’. If still unavailable and if running in a Databricks notebook, it defaults to the current workspace hostname. Defaults to None.

  * **api\_token** \(_Optional_ _\[__str_ _\]_\) – The Databricks personal access token for accessing the Databricks SQL warehouse or the cluster. If not provided, it attempts to fetch from ‘DATABRICKS\_TOKEN’. If still unavailable and running in a Databricks notebook, a temporary token for the current user is generated. Defaults to None.

  * **warehouse\_id** \(_Optional_ _\[__str_ _\]_\) – The warehouse ID in the Databricks SQL. If provided, the method configures the connection to use this warehouse. Cannot be used with ‘cluster\_id’. Defaults to None.

  * **cluster\_id** \(_Optional_ _\[__str_ _\]_\) – The cluster ID in the Databricks Runtime. If provided, the method configures the connection to use this cluster. Cannot be used with ‘warehouse\_id’. If running in a Databricks notebook and both ‘warehouse\_id’ and ‘cluster\_id’ are None, it uses the ID of the cluster the notebook is attached to. Defaults to None.

  * **engine\_args** \(_Optional_ _\[__dict_ _\]_\) – The arguments to be used when connecting Databricks. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments for the from\_uri method.

Returns:     

An instance of SQLDatabase configured with the provided     

Databricks connection details.

Return type:     

SQLDatabase

Raises:     

**ValueError** – If ‘databricks-sql-connector’ is not found, or if both ‘warehouse\_id’ and ‘cluster\_id’ are provided, or if neither ‘warehouse\_id’ nor ‘cluster\_id’ are provided and it’s not executing inside a Databricks notebook.

_classmethod _from\_uri\(

    _database\_uri : str | URL_,     _engine\_args : dict | None = None_,     _\*\* kwargs: Any_, \) → SQLDatabase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.from_uri)\#     

Construct a SQLAlchemy engine from URI.

Parameters:     

  * **database\_uri** \(_str_ _|__URL_\)

  * **engine\_args** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_SQLDatabase_

get\_context\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_context)\#     

Return db context that you may want in agent prompt.

Return type:     

_Dict_\[str, _Any_\]

get\_table\_info\(

    _table\_names : List\[str\] | None = None_,     _get\_col\_comments : bool = False_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_table_info)\#     

Get information about specified tables.

Follows best practices as specified in: Rajkumar et al, 2022 \(<https://arxiv.org/abs/2204.00498>\)

If sample\_rows\_in\_table\_info, the specified number of sample rows will be appended to each table description. This can increase performance as demonstrated in the paper.

Parameters:     

  * **table\_names** \(_List_ _\[__str_ _\]__|__None_\)

  * **get\_col\_comments** \(_bool_\)

Return type:     

str

get\_table\_info\_no\_throw\(

    _table\_names : List\[str\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_table_info_no_throw)\#     

Get information about specified tables.

Follows best practices as specified in: Rajkumar et al, 2022 \(<https://arxiv.org/abs/2204.00498>\)

If sample\_rows\_in\_table\_info, the specified number of sample rows will be appended to each table description. This can increase performance as demonstrated in the paper.

Parameters:     

**table\_names** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

get\_table\_names\(\) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_table_names)\#     

Deprecated since version 0.0.1: Use `get_usable_table_names()` instead. It will not be removed until langchain-community==1.0.

Get names of tables available.

Return type:     

_Iterable_\[str\]

get\_usable\_table\_names\(\) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.get_usable_table_names)\#     

Get names of tables available.

Return type:     

_Iterable_\[str\]

run\(

    _command : str | Executable_,     _fetch : Literal\['all', 'one', 'cursor'\] = 'all'_,     _include\_columns : bool = False_,     _\*_ ,     _parameters : Dict\[str, Any\] | None = None_,     _execution\_options : Dict\[str, Any\] | None = None_, \) → str | Sequence\[Dict\[str, Any\]\] | Result\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.run)\#     

Execute a SQL command and return a string representing the results.

If the statement returns rows, a string of the results is returned. If the statement returns no rows, an empty string is returned.

Parameters:     

  * **command** \(_str_ _|__Executable_\)

  * **fetch** \(_Literal_ _\[__'all'__,__'one'__,__'cursor'__\]_\)

  * **include\_columns** \(_bool_\)

  * **parameters** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **execution\_options** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

str | _Sequence_\[_Dict_\[str, _Any_\]\] | _Result_\[_Any_\]

run\_no\_throw\(

    _command : str_,     _fetch : Literal\['all', 'one'\] = 'all'_,     _include\_columns : bool = False_,     _\*_ ,     _parameters : Dict\[str, Any\] | None = None_,     _execution\_options : Dict\[str, Any\] | None = None_, \) → str | Sequence\[Dict\[str, Any\]\] | Result\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/sql_database.html#SQLDatabase.run_no_throw)\#     

Execute a SQL command and return a string representing the results.

If the statement returns rows, a string of the results is returned. If the statement returns no rows, an empty string is returned.

If the statement throws an error, the error message is returned.

Parameters:     

  * **command** \(_str_\)

  * **fetch** \(_Literal_ _\[__'all'__,__'one'__\]_\)

  * **include\_columns** \(_bool_\)

  * **parameters** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **execution\_options** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

str | _Sequence_\[_Dict_\[str, _Any_\]\] | _Result_\[_Any_\]

Examples using SQLDatabase

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [CnosDB](https://python.langchain.com/docs/integrations/providers/cnosdb/)

  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)

  * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)

  * [How to do query validation as part of SQL question-answering](https://python.langchain.com/docs/how_to/sql_query_checking/)

  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)

  * [Rebuff](https://python.langchain.com/docs/integrations/providers/rebuff/)

  * [SQLDatabase Toolkit](https://python.langchain.com/docs/integrations/tools/sql_database/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)