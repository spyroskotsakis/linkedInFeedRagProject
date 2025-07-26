# InMemoryBaseStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryBaseStore.html
**Word Count:** 271
**Links Count:** 139
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# InMemoryBaseStore\#

_class _langchain\_core.stores.InMemoryBaseStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore)\#     

In-memory implementation of the BaseStore using a dictionary.

Initialize an empty store.

Methods

`__init__`\(\) | Initialize an empty store.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\[prefix\]\) | Async get an async iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\[prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.__init__)\#     

Initialize an empty store.

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.amdelete)\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → list\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.amget)\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[tuple\[str, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.amset)\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__str_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Returns:     

None

Return type:     

None

_async _ayield\_keys\(

    _prefix : str | None = None_, \) → AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.ayield_keys)\#     

Async get an async iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _,__optional_\) – The prefix to match. Defaults to None.

Yields:     

_AsyncIterator\[str\]_ – An async iterator over keys that match the given prefix.

Return type:     

_AsyncIterator_\[str\]

mdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → list\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

mset\(

    _key\_value\_pairs : Sequence\[tuple\[str, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__str_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Returns:     

None

Return type:     

None

yield\_keys\(

    _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryBaseStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _,__optional_\) – The prefix to match. Defaults to None.

Yields:     

_Iterator\[str\]_ – An iterator over keys that match the given prefix.

Return type:     

_Iterator_\[str\]

__On this page