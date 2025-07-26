# UpstashRedisByteStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisByteStore.html
**Word Count:** 220
**Links Count:** 141
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# UpstashRedisByteStore\#

_class _langchain\_community.storage.upstash\_redis.UpstashRedisByteStore\(

    _\*_ ,     _client : Any = None_,     _url : str | None = None_,     _token : str | None = None_,     _ttl : int | None = None_,     _namespace : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisByteStore)\#     

BaseStore implementation using Upstash Redis as the underlying store to store raw bytes.

Methods

`__init__`\(\*\[, client, url, token, ttl, namespace\]\) |    ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given keys.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the given key-value pairs.   `yield_keys`\(\*\[, prefix\]\) | Yield keys in the store.      Parameters:     

  * **client** \(_Any_\)

  * **url** \(_str_ _|__None_\)

  * **token** \(_str_ _|__None_\)

  * **ttl** \(_int_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

\_\_init\_\_\(

    _\*_ ,     _client : Any = None_,     _url : str | None = None_,     _token : str | None = None_,     _ttl : int | None = None_,     _namespace : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisByteStore.__init__)\#     

Parameters:     

  * **client** \(_Any_\)

  * **url** \(_str_ _|__None_\)

  * **token** \(_str_ _|__None_\)

  * **ttl** \(_int_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[K\]_, \) → None\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[K\]_, \) → list\[V | None\]\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[tuple\[K, V\]\]_, \) → None\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[K\] | AsyncIterator\[str\]\#     

Async get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_AsyncIterator_\[_K_\] | _AsyncIterator_\[str\]

mdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisByteStore.mdelete)\#     

Delete the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisByteStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

_List_\[bytes | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisByteStore.mset)\#     

Set the given key-value pairs.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__Tuple_ _\[__str_ _,__bytes_ _\]__\]_\)

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/upstash_redis.html#UpstashRedisByteStore.yield_keys)\#     

Yield keys in the store.

Parameters:     

**prefix** \(_str_ _|__None_\)

Return type:     

_Iterator_\[str\]

Examples using UpstashRedisByteStore

  * [UpstashRedisByteStore](https://python.langchain.com/docs/integrations/stores/upstash_redis/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)