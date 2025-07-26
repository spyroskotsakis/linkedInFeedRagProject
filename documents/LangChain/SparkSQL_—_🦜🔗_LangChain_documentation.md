# SparkSQL — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.spark_sql.SparkSQL.html
**Word Count:** 324
**Links Count:** 281
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# SparkSQL\#

_class _langchain\_community.utilities.spark\_sql.SparkSQL\(

    _spark\_session : SparkSession | None = None_,     _catalog : str | None = None_,     _schema : str | None = None_,     _ignore\_tables : List\[str\] | None = None_,     _include\_tables : List\[str\] | None = None_,     _sample\_rows\_in\_table\_info : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL)\#     

SparkSQL is a utility class for interacting with Spark SQL.

Initialize a SparkSQL object.

Parameters:     

  * **spark\_session** \(_Optional_ _\[__SparkSession_ _\]_\) – A SparkSession object. If not provided, one will be created.

  * **catalog** \(_Optional_ _\[__str_ _\]_\) – The catalog to use. If not provided, the default catalog will be used.

  * **schema** \(_Optional_ _\[__str_ _\]_\) – The schema to use. If not provided, the default schema will be used.

  * **ignore\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – A list of tables to ignore. If not provided, all tables will be used.

  * **include\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – A list of tables to include. If not provided, all tables will be used.

  * **sample\_rows\_in\_table\_info** \(_int_\) – The number of rows to include in the table info. Defaults to 3.

Methods

`__init__`\(\[spark\_session, catalog, schema, ...\]\) | Initialize a SparkSQL object.   ---|---   `from_uri`\(database\_uri\[, engine\_args\]\) | Creating a remote Spark Session via Spark connect.   `get_table_info`\(\[table\_names\]\) |    `get_table_info_no_throw`\(\[table\_names\]\) | Get information about specified tables.   `get_usable_table_names`\(\) | Get names of tables available.   `run`\(command\[, fetch\]\) |    `run_no_throw`\(command\[, fetch\]\) | Execute a SQL command and return a string representing the results.      \_\_init\_\_\(

    _spark\_session : SparkSession | None = None_,     _catalog : str | None = None_,     _schema : str | None = None_,     _ignore\_tables : List\[str\] | None = None_,     _include\_tables : List\[str\] | None = None_,     _sample\_rows\_in\_table\_info : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.__init__)\#     

Initialize a SparkSQL object.

Parameters:     

  * **spark\_session** \(_Optional_ _\[__SparkSession_ _\]_\) – A SparkSession object. If not provided, one will be created.

  * **catalog** \(_Optional_ _\[__str_ _\]_\) – The catalog to use. If not provided, the default catalog will be used.

  * **schema** \(_Optional_ _\[__str_ _\]_\) – The schema to use. If not provided, the default schema will be used.

  * **ignore\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – A list of tables to ignore. If not provided, all tables will be used.

  * **include\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – A list of tables to include. If not provided, all tables will be used.

  * **sample\_rows\_in\_table\_info** \(_int_\) – The number of rows to include in the table info. Defaults to 3.

_classmethod _from\_uri\(

    _database\_uri : str_,     _engine\_args : dict | None = None_,     _\*\* kwargs: Any_, \) → SparkSQL[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.from_uri)\#     

Creating a remote Spark Session via Spark connect. For example: SparkSQL.from\_uri\(“sc://localhost:15002”\)

Parameters:     

  * **database\_uri** \(_str_\)

  * **engine\_args** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_SparkSQL_

get\_table\_info\(

    _table\_names : List\[str\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.get_table_info)\#     

Parameters:     

**table\_names** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

get\_table\_info\_no\_throw\(

    _table\_names : List\[str\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.get_table_info_no_throw)\#     

Get information about specified tables.

Follows best practices as specified in: Rajkumar et al, 2022 \(<https://arxiv.org/abs/2204.00498>\)

If sample\_rows\_in\_table\_info, the specified number of sample rows will be appended to each table description. This can increase performance as demonstrated in the paper.

Parameters:     

**table\_names** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

get\_usable\_table\_names\(\) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.get_usable_table_names)\#     

Get names of tables available.

Return type:     

_Iterable_\[str\]

run\(_command : str_, _fetch : str = 'all'_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.run)\#     

Parameters:     

  * **command** \(_str_\)

  * **fetch** \(_str_\)

Return type:     

str

run\_no\_throw\(

    _command : str_,     _fetch : str = 'all'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/spark_sql.html#SparkSQL.run_no_throw)\#     

Execute a SQL command and return a string representing the results.

If the statement returns rows, a string of the results is returned. If the statement returns no rows, an empty string is returned.

If the statement throws an error, the error message is returned.

Parameters:     

  * **command** \(_str_\)

  * **fetch** \(_str_\)

Return type:     

str

Examples using SparkSQL

  * [Spark SQL Toolkit](https://python.langchain.com/docs/integrations/tools/spark_sql/)

__On this page