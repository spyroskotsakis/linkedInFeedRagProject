# AstraDBBaseStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBBaseStore.html
**Word Count:** 325
**Links Count:** 152
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# AstraDBBaseStore\#

_class _langchain\_community.storage.astradb.AstraDBBaseStore\(_\* args: Any_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore)\#     

Base class for the DataStax AstraDB data store.

Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `decode_value`\(value\) | Decodes value from Astra DB   `encode_value`\(value\) | Encodes value for Astra DB   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.__init__)\#     

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.amdelete)\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → List\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.amget)\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.amset)\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.ayield_keys)\#     

Async get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_AsyncIterator_\[str\]

_abstractmethod _decode\_value\(

    _value : Any_, \) → V | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.decode_value)\#     

Decodes value from Astra DB

Parameters:     

**value** \(_Any_\)

Return type:     

_V_ | None

_abstractmethod _encode\_value\(

    _value : V | None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.encode_value)\#     

Encodes value for Astra DB

Parameters:     

**value** \(_V_ _|__None_\)

Return type:     

_Any_

mdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[_V_ | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBBaseStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)