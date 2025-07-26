# BaseEntityStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.entity.BaseEntityStore.html
**Word Count:** 86
**Links Count:** 119
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# BaseEntityStore\#

_class _langchain.memory.entity.BaseEntityStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#BaseEntityStore)\#     

Bases: `BaseModel`, `ABC`

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Abstract base class for Entity store.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod _clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#BaseEntityStore.clear)\#     

Delete all entities from store.

Return type:     

None

_abstractmethod _delete\(_key : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#BaseEntityStore.delete)\#     

Delete entity value from store.

Parameters:     

**key** \(_str_\)

Return type:     

None

_abstractmethod _exists\(_key : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#BaseEntityStore.exists)\#     

Check if entity exists in store.

Parameters:     

**key** \(_str_\)

Return type:     

bool

_abstractmethod _get\(

    _key : str_,     _default : str | None = None_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#BaseEntityStore.get)\#     

Get entity value from store.

Parameters:     

  * **key** \(_str_\)

  * **default** \(_str_ _|__None_\)

Return type:     

str | None

_abstractmethod _set\(_key : str_, _value : str | None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/entity.html#BaseEntityStore.set)\#     

Set entity value in store.

Parameters:     

  * **key** \(_str_\)

  * **value** \(_str_ _|__None_\)

Return type:     

None

__On this page