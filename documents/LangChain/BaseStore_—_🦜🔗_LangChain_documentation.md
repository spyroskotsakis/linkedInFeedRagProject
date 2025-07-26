# BaseStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html
**Word Count:** 449
**Links Count:** 136
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# BaseStore\#

_class _langchain\_core.stores.BaseStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore)\#     

Abstract interface for a key-value store.

This is an interface that’s meant to abstract away the details of different key-value stores. It provides a simple interface for getting, setting, and deleting key-value pairs.

The basic methods are mget, mset, and mdelete for getting, setting, and deleting multiple key-value pairs at once. The yield\_keys method is used to iterate over keys that match a given prefix.

The async versions of these methods are also provided, which are meant to be used in async contexts. The async methods are named with an a prefix, e.g., amget, amset, amdelete, and ayield\_keys.

By default, the amget, amset, amdelete, and ayield\_keys methods are implemented using the synchronous methods. If the store can natively support async operations, it should override these methods.

By design the methods only accept batches of keys and values, and not single keys or values. This is done to force user code to work with batches which will usually be more efficient by saving on round trips to the store.

Examples               from langchain.storage import BaseStore          class MyInMemoryStore(BaseStore[str, int]):              def __init__(self):             self.store = {}              def mget(self, keys):             return [self.store.get(key) for key in keys]              def mset(self, key_value_pairs):             for key, value in key_value_pairs:                 self.store[key] = value              def mdelete(self, keys):             for key in keys:                 if key in self.store:                     del self.store[key]              def yield_keys(self, prefix=None):             if prefix is None:                 yield from self.store.keys()             else:                 for key in self.store.keys():                     if key.startswith(prefix):                         yield key     

Methods

`amdelete`\(keys\) | Async delete the given keys and their associated values.   ---|---   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      _async _amdelete\(

    _keys : Sequence\[K\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.amdelete)\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[K\]_, \) → list\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.amget)\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[tuple\[K, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.amset)\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[K\] | AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.ayield_keys)\#     

Async get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_AsyncIterator_\[_K_\] | _AsyncIterator_\[str\]

_abstractmethod _mdelete\(

    _keys : Sequence\[K\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_abstractmethod _mget\(

    _keys : Sequence\[K\]_, \) → list\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

_abstractmethod _mset\(

    _key\_value\_pairs : Sequence\[tuple\[K, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_abstractmethod _yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[K\] | Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/stores.html#BaseStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_Iterator_\[_K_\] | _Iterator_\[str\]

Examples using BaseStore

  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)