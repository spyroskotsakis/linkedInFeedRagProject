# CassandraDatabase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html
**Word Count:** 313
**Links Count:** 290
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# CassandraDatabase\#

_class _langchain\_community.utilities.cassandra\_database.CassandraDatabase\(

    _session : Session | None = None_,     _exclude\_tables : List\[str\] | None = None_,     _include\_tables : List\[str\] | None = None_,     _cassio\_init\_kwargs : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase)\#     

Apache Cassandra® database wrapper.

Methods

`__init__`\(\[session, exclude\_tables, ...\]\) |    ---|---   `fetch_all`\(query, \*\*kwargs\) |    `fetch_one`\(query, \*\*kwargs\) |    `format_keyspace_to_markdown`\(keyspace\[, tables\]\) | Generates a markdown representation of the schema for a specific keyspace by iterating over all tables within that keyspace and calling their as\_markdown method.   `format_schema_to_markdown`\(\) | Generates a markdown representation of the schema for all keyspaces and tables within the CassandraDatabase instance.   `get_context`\(\) | Return db context that you may want in agent prompt.   `get_keyspace_tables`\(keyspace\) | Get the Table objects for the specified keyspace.   `get_table_data`\(keyspace, table, predicate, limit\) | Get data from the specified table in the specified keyspace.   `run`\(query\[, fetch\]\) | Execute a CQL query and return the results.      Parameters:     

  * **session** \(_Optional_ _\[__Session_ _\]_\)

  * **exclude\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **include\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **cassio\_init\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

\_\_init\_\_\(

    _session : Session | None = None_,     _exclude\_tables : List\[str\] | None = None_,     _include\_tables : List\[str\] | None = None_,     _cassio\_init\_kwargs : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.__init__)\#     

Parameters:     

  * **session** \(_Optional_ _\[__Session_ _\]_\)

  * **exclude\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **include\_tables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **cassio\_init\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

fetch\_all\(

    _query : str_,     _\*\* kwargs: Any_, \) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.fetch_all)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

list

fetch\_one\(

    _query : str_,     _\*\* kwargs: Any_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.fetch_one)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Dict_\[str, _Any_\]

format\_keyspace\_to\_markdown\(

    _keyspace : str_,     _tables : List\[[Table](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table")\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.format_keyspace_to_markdown)\#     

Generates a markdown representation of the schema for a specific keyspace by iterating over all tables within that keyspace and calling their as\_markdown method.

Parameters:     

  * **keyspace** \(_str_\) – The name of the keyspace to generate markdown documentation for.

  * **tables** \(_List_ _\[_[_Table_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table") _\]__|__None_\) – list of tables in the keyspace; it will be resolved if not provided.

Returns:     

A string containing the markdown representation of the specified keyspace schema.

Return type:     

str

format\_schema\_to\_markdown\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.format_schema_to_markdown)\#     

Generates a markdown representation of the schema for all keyspaces and tables within the CassandraDatabase instance. This method utilizes the format\_keyspace\_to\_markdown method to create markdown sections for each keyspace, assembling them into a comprehensive schema document.

Iterates through each keyspace in the database, utilizing format\_keyspace\_to\_markdown to generate markdown for each keyspace’s schema, including details of its tables. These sections are concatenated to form a single markdown document that represents the schema of the entire database or the subset of keyspaces that have been resolved in this instance.

Returns:     

A markdown string that documents the schema of all resolved keyspaces and their tables within this CassandraDatabase instance. This includes keyspace names, table names, comments, columns, partition keys, clustering keys, and indexes for each table.

Return type:     

str

get\_context\(\) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.get_context)\#     

Return db context that you may want in agent prompt.

Return type:     

_Dict_\[str, _Any_\]

get\_keyspace\_tables\(

    _keyspace : str_, \) → List\[[Table](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.get_keyspace_tables)\#     

Get the Table objects for the specified keyspace.

Parameters:     

**keyspace** \(_str_\)

Return type:     

_List_\[[_Table_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html#langchain_community.utilities.cassandra_database.Table "langchain_community.utilities.cassandra_database.Table")\]

get\_table\_data\(

    _keyspace : str_,     _table : str_,     _predicate : str_,     _limit : int_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.get_table_data)\#     

Get data from the specified table in the specified keyspace.

Parameters:     

  * **keyspace** \(_str_\)

  * **table** \(_str_\)

  * **predicate** \(_str_\)

  * **limit** \(_int_\)

Return type:     

str

run\(

    _query : str_,     _fetch : str = 'all'_,     _\*\* kwargs: Any_, \) → list | Dict\[str, Any\] | ResultSet[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#CassandraDatabase.run)\#     

Execute a CQL query and return the results.

Parameters:     

  * **query** \(_str_\)

  * **fetch** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

Union\[list, Dict\[str, Any\], ResultSet\]

Examples using CassandraDatabase

  * [Cassandra Database Toolkit](https://python.langchain.com/docs/integrations/tools/cassandra_database/)

__On this page