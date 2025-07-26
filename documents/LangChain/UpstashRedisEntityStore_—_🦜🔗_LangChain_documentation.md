# UpstashRedisEntityStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.UpstashRedisEntityStore.html
**Word Count:** 108
**Links Count:** 122
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# UpstashRedisEntityStore\#

_class _langchain.memory.entity.UpstashRedisEntityStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#UpstashRedisEntityStore)\#     

Bases: [`BaseEntityStore`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html#langchain.memory.entity.BaseEntityStore "langchain.memory.entity.BaseEntityStore")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Upstash Redis backed Entity store.

Entities get a TTL of 1 day by default, and that TTL is extended by 3 days every time the entity is read back.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#UpstashRedisEntityStore.clear)\#     

Delete all entities from store.

Return type:     

None

delete\(_key : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#UpstashRedisEntityStore.delete)\#     

Delete entity value from store.

Parameters:     

**key** \(_str_\)

Return type:     

None

exists\(_key : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#UpstashRedisEntityStore.exists)\#     

Check if entity exists in store.

Parameters:     

**key** \(_str_\)

Return type:     

bool

get\(

    _key : str_,     _default : str | None = None_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#UpstashRedisEntityStore.get)\#     

Get entity value from store.

Parameters:     

  * **key** \(_str_\)

  * **default** \(_str_ _|__None_\)

Return type:     

str | None

set\(

    _key : str_,     _value : str | None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#UpstashRedisEntityStore.set)\#     

Set entity value in store.

Parameters:     

  * **key** \(_str_\)

  * **value** \(_str_ _|__None_\)

Return type:     

None

_property _full\_key\_prefix _: str_\#     

__On this page