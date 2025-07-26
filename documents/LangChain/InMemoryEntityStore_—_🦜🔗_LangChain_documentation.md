# InMemoryEntityStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.InMemoryEntityStore.html
**Word Count:** 83
**Links Count:** 122
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# InMemoryEntityStore\#

_class _langchain.memory.entity.InMemoryEntityStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#InMemoryEntityStore)\#     

Bases: [`BaseEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html#langchain.memory.entity.BaseEntityStore "langchain.memory.entity.BaseEntityStore")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

In-memory Entity store.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _store _: dict\[str, str | None\]__ = \{\}_\#     

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#InMemoryEntityStore.clear)\#     

Delete all entities from store.

Return type:     

None

delete\(_key : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#InMemoryEntityStore.delete)\#     

Delete entity value from store.

Parameters:     

**key** \(_str_\)

Return type:     

None

exists\(_key : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#InMemoryEntityStore.exists)\#     

Check if entity exists in store.

Parameters:     

**key** \(_str_\)

Return type:     

bool

get\(

    _key : str_,     _default : str | None = None_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#InMemoryEntityStore.get)\#     

Get entity value from store.

Parameters:     

  * **key** \(_str_\)

  * **default** \(_str_ _|__None_\)

Return type:     

str | None

set\(_key : str_, _value : str | None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#InMemoryEntityStore.set)\#     

Set entity value in store.

Parameters:     

  * **key** \(_str_\)

  * **value** \(_str_ _|__None_\)

Return type:     

None

__On this page