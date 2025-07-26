# ExactNearestNeighbor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.ExactNearestNeighbor.html
**Word Count:** 26
**Links Count:** 101
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# ExactNearestNeighbor\#

_class _langchain\_postgres.v2.indexes.ExactNearestNeighbor\(

    _name: Optional\[str\] = None_,     _index\_type: str = 'exactnearestneighbor'_,     _distance\_strategy: langchain\_postgres.v2.indexes.DistanceStrategy = <factory>_,     _partial\_indexes: Optional\[list\[str\]\] = None_,     _extension\_name: Optional\[str\] = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#ExactNearestNeighbor)\#     

Attributes

`extension_name` |    ---|---   `index_type` |    `name` |    `partial_indexes` |       Methods

`__init__`\(\[name, index\_type, ...\]\) |    ---|---   `get_index_function`\(\) |    `index_options`\(\) | Set index query options for vector store initialization.      Parameters:     

  * **name** \(_str_ _|__None_\)

  * **index\_type** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **partial\_indexes** \(_list_ _\[__str_ _\]__|__None_\)

  * **extension\_name** \(_str_ _|__None_\)

\_\_init\_\_\(

    _name: str | None = None_,     _index\_type: str = 'exactnearestneighbor'_,     _distance\_strategy: ~langchain\_postgres.v2.indexes.DistanceStrategy = <factory>_,     _partial\_indexes: list\[str\] | None = None_,     _extension\_name: str | None = None_, \) → None\#     

Parameters:     

  * **name** \(_str_ _|__None_\)

  * **index\_type** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **partial\_indexes** \(_list_ _\[__str_ _\]__|__None_\)

  * **extension\_name** \(_str_ _|__None_\)

Return type:     

None

get\_index\_function\(\) → str\#     

Return type:     

str

_abstractmethod _index\_options\(\) → str\#     

Set index query options for vector store initialization.

Return type:     

str

__On this page