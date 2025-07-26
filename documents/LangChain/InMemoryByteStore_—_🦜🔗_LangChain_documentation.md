# InMemoryByteStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/stores/langchain_core.stores.InMemoryByteStore.html
**Word Count:** 288
**Links Count:** 135
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# InMemoryByteStore\#

_class _langchain\_core.stores.InMemoryByteStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#InMemoryByteStore)\#     

In-memory store for bytes.

store\#     

The underlying dictionary that stores the key-value pairs.

Type:     

dict\[str, bytes\]

Examples               from langchain.storage import InMemoryByteStore          store = InMemoryByteStore()     store.mset([('key1', b'value1'), ('key2', b'value2')])     store.mget(['key1', 'key2'])     # [b'value1', b'value2']     store.mdelete(['key1'])     list(store.yield_keys())     # ['key2']     list(store.yield_keys(prefix='k'))     # ['key2']     

Initialize an empty store.

Methods

`__init__`\(\) | Initialize an empty store.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\[prefix\]\) | Async get an async iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\[prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(\) → None\#     

Initialize an empty store.

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[str\]_, \) → None\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → list\[V | None\]\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[tuple\[str, V\]\]_, \) → None\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__str_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Returns:     

None

Return type:     

None

_async _ayield\_keys\(

    _prefix : str | None = None_, \) → AsyncIterator\[str\]\#     

Async get an async iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _,__optional_\) – The prefix to match. Defaults to None.

Yields:     

_AsyncIterator\[str\]_ – An async iterator over keys that match the given prefix.

Return type:     

_AsyncIterator_\[str\]

mdelete\(

    _keys : Sequence\[str\]_, \) → None\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → list\[V | None\]\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

mset\(

    _key\_value\_pairs : Sequence\[tuple\[str, V\]\]_, \) → None\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__str_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Returns:     

None

Return type:     

None

yield\_keys\(

    _prefix : str | None = None_, \) → Iterator\[str\]\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _,__optional_\) – The prefix to match. Defaults to None.

Yields:     

_Iterator\[str\]_ – An iterator over keys that match the given prefix.

Return type:     

_Iterator_\[str\]

Examples using InMemoryByteStore

  * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [InMemoryByteStore](https://python.langchain.com/docs/integrations/stores/in_memory/)

__On this page