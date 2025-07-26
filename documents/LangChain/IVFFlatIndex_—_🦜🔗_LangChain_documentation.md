# IVFFlatIndex — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.IVFFlatIndex.html
**Word Count:** 26
**Links Count:** 102
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# IVFFlatIndex\#

_class _langchain\_postgres.v2.indexes.IVFFlatIndex\(

    _name: Optional\[str\] = None_,     _index\_type: str = 'ivfflat'_,     _distance\_strategy: langchain\_postgres.v2.indexes.DistanceStrategy = <factory>_,     _partial\_indexes: Optional\[list\[str\]\] = None_,     _extension\_name: Optional\[str\] = None_,     _lists: int = 100_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#IVFFlatIndex)\#     

Attributes

`extension_name` |    ---|---   `index_type` |    `lists` |    `name` |    `partial_indexes` |       Methods

`__init__`\(\[name, index\_type, ...\]\) |    ---|---   `get_index_function`\(\) |    `index_options`\(\) | Set index query options for vector store initialization.      Parameters:     

  * **name** \(_str_ _|__None_\)

  * **index\_type** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **partial\_indexes** \(_list_ _\[__str_ _\]__|__None_\)

  * **extension\_name** \(_str_ _|__None_\)

  * **lists** \(_int_\)

\_\_init\_\_\(

    _name: str | None = None_,     _index\_type: str = 'ivfflat'_,     _distance\_strategy: ~langchain\_postgres.v2.indexes.DistanceStrategy = <factory>_,     _partial\_indexes: list\[str\] | None = None_,     _extension\_name: str | None = None_,     _lists: int = 100_, \) → None\#     

Parameters:     

  * **name** \(_str_ _|__None_\)

  * **index\_type** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **partial\_indexes** \(_list_ _\[__str_ _\]__|__None_\)

  * **extension\_name** \(_str_ _|__None_\)

  * **lists** \(_int_\)

Return type:     

None

get\_index\_function\(\) → str\#     

Return type:     

str

index\_options\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#IVFFlatIndex.index_options)\#     

Set index query options for vector store initialization.

Return type:     

str

__On this page