# SQLiteEntityStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.SQLiteEntityStore.html
**Word Count:** 105
**Links Count:** 128
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# SQLiteEntityStore\#

_class _langchain.memory.entity.SQLiteEntityStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#SQLiteEntityStore)\#     

Bases: [`BaseEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html#langchain.memory.entity.BaseEntityStore "langchain.memory.entity.BaseEntityStore")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

SQLite-backed Entity store with safe query construction.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _conn _: Any_ _ = None_\#     

_param _session\_id _: str_ _ = 'default'_\#     

_param _table\_name _: str_ _ = 'memory\_store'_\#     

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#SQLiteEntityStore.clear)\#     

Delete all entities from store.

Return type:     

None

delete\(_key : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#SQLiteEntityStore.delete)\#     

Deletes a key-value pair, safely quoting the table name.

Parameters:     

**key** \(_str_\)

Return type:     

None

exists\(_key : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#SQLiteEntityStore.exists)\#     

Checks for the existence of a key, safely quoting the table name.

Parameters:     

**key** \(_str_\)

Return type:     

bool

get\(

    _key : str_,     _default : str | None = None_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#SQLiteEntityStore.get)\#     

Retrieves a value, safely quoting the table name.

Parameters:     

  * **key** \(_str_\)

  * **default** \(_str_ _|__None_\)

Return type:     

str | None

set\(_key : str_, _value : str | None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#SQLiteEntityStore.set)\#     

Inserts or replaces a value, safely quoting the table name.

Parameters:     

  * **key** \(_str_\)

  * **value** \(_str_ _|__None_\)

Return type:     

None

_property _full\_table\_name _: str_\#     

__On this page