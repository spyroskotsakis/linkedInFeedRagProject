# BaseIndex — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html
**Word Count:** 86
**Links Count:** 118
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# BaseIndex\#

_class _langchain\_postgres.v2.indexes.BaseIndex\(

    _name: str | None = None_,     _index\_type: str = 'base'_,     _distance\_strategy: ~langchain\_postgres.v2.indexes.DistanceStrategy = <factory>_,     _partial\_indexes: list\[str\] | None = None_,     _extension\_name: str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#BaseIndex)\#     

Abstract base class for defining vector indexes.

Parameters:     

  * **name** \(_str_ _|__None_\)

  * **index\_type** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **partial\_indexes** \(_list_ _\[__str_ _\]__|__None_\)

  * **extension\_name** \(_str_ _|__None_\)

name\#     

A human-readable name for the index. Defaults to None.

Type:     

Optional\[str\]

index\_type\#     

A string identifying the type of index. Defaults to “base”.

Type:     

str

distance\_strategy\#     

The strategy used to calculate distances between vectors in the index. Defaults to DistanceStrategy.COSINE\_DISTANCE.

Type:     

[DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")

partial\_indexes\#     

A list of names of partial indexes. Defaults to None.

Type:     

Optional\[list\[str\]\]

extension\_name\#     

The name of the extension to be created for the index, if any. Defaults to None.

Type:     

Optional\[str\]

Attributes

`extension_name` |    ---|---   `index_type` |    `name` |    `partial_indexes` |       Methods

`__init__`\(\[name, index\_type, ...\]\) |    ---|---   `get_index_function`\(\) |    `index_options`\(\) | Set index query options for vector store initialization.      \_\_init\_\_\(

    _name: str | None = None_,     _index\_type: str = 'base'_,     _distance\_strategy: ~langchain\_postgres.v2.indexes.DistanceStrategy = <factory>_,     _partial\_indexes: list\[str\] | None = None_,     _extension\_name: str | None = None_, \) → None\#     

Parameters:     

  * **name** \(_str_ _|__None_\)

  * **index\_type** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **partial\_indexes** \(_list_ _\[__str_ _\]__|__None_\)

  * **extension\_name** \(_str_ _|__None_\)

Return type:     

None

get\_index\_function\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#BaseIndex.get_index_function)\#     

Return type:     

str

_abstractmethod _index\_options\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#BaseIndex.index_options)\#     

Set index query options for vector store initialization.

Return type:     

str

__On this page