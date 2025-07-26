# Table — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.Table.html
**Word Count:** 138
**Links Count:** 273
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# Table\#

_class _langchain\_community.utilities.cassandra\_database.Table[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#Table)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _clustering _: List\[Tuple\[str, str\]\]__\[Optional\]_\#     

_param _columns _: List\[Tuple\[str, str\]\]__\[Optional\]_\#     

_param _comment _: str | None_ _ = None_\#     

The comment associated with the table.

_param _indexes _: List\[Tuple\[str, str, str\]\]__\[Optional\]_\#     

_param _keyspace _: str_ _\[Required\]_\#     

The keyspace in which the table exists.

_param _partition _: List\[str\]__\[Optional\]_\#     

_param _table\_name _: str_ _\[Required\]_\#     

The name of the table.

_classmethod _from\_database\(

    _keyspace : str_,     _table\_name : str_,     _db : [CassandraDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase "langchain_community.utilities.cassandra_database.CassandraDatabase")_, \) → Table[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#Table.from_database)\#     

Parameters:     

  * **keyspace** \(_str_\)

  * **table\_name** \(_str_\)

  * **db** \([_CassandraDatabase_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase "langchain_community.utilities.cassandra_database.CassandraDatabase")\)

Return type:     

_Table_

as\_markdown\(

    _include\_keyspace : bool = True_,     _header\_level : int | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/cassandra_database.html#Table.as_markdown)\#     

Generates a Markdown representation of the Cassandra table schema, allowing for customizable header levels for the table name section.

Parameters:     

  * **include\_keyspace** \(_bool_\) – If True, includes the keyspace in the output. Defaults to True.

  * **header\_level** \(_int_ _|__None_\) – Specifies the markdown header level for the table name. If None, the table name is included without a header. Defaults to None \(no header level\).

Returns:     

A string in Markdown format detailing the table name \(with optional header level\), keyspace \(optional\), comment, columns, partition keys, clustering keys \(with optional clustering order\), and indexes.

Return type:     

str

__On this page