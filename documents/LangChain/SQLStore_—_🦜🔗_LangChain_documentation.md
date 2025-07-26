# SQLStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.SQLStore.html
**Word Count:** 344
**Links Count:** 156
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# SQLStore\#

_class _langchain\_community.storage.sql.SQLStore\(

    _\*_ ,     _namespace : str_,     _db\_url : str | Path | None = None_,     _engine : Engine | AsyncEngine | None = None_,     _engine\_kwargs : Dict\[str, Any\] | None = None_,     _async\_mode : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore)\#     

BaseStore interface that works on an SQL database.

Examples

Create a SQLStore instance and perform operations on it:               from langchain_community.storage import SQLStore          # Instantiate the SQLStore with the root path     sql_store = SQLStore(namespace="test", db_url="sqlite://:memory:")          # Set values for keys     sql_store.mset([("key1", b"value1"), ("key2", b"value2")])          # Get values for keys     values = sql_store.mget(["key1", "key2"])  # Returns [b"value1", b"value2"]          # Delete keys     sql_store.mdelete(["key1"])          # Iterate over keys     for key in sql_store.yield_keys():         print(key)     

Methods

`__init__`\(\*, namespace\[, db\_url, engine, ...\]\) |    ---|---   `acreate_schema`\(\) |    `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `create_schema`\(\) |    `drop`\(\) |    `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      Parameters:     

  * **namespace** \(_str_\)

  * **db\_url** \(_str_ _|__Path_ _|__None_\)

  * **engine** \(_Engine_ _|__AsyncEngine_ _|__None_\)

  * **engine\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **async\_mode** \(_bool_ _|__None_\)

\_\_init\_\_\(

    _\*_ ,     _namespace : str_,     _db\_url : str | Path | None = None_,     _engine : Engine | AsyncEngine | None = None_,     _engine\_kwargs : Dict\[str, Any\] | None = None_,     _async\_mode : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.__init__)\#     

Parameters:     

  * **namespace** \(_str_\)

  * **db\_url** \(_str_ _|__Path_ _|__None_\)

  * **engine** \(_Engine_ _|__AsyncEngine_ _|__None_\)

  * **engine\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **async\_mode** \(_bool_ _|__None_\)

_async _acreate\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.acreate_schema)\#     

Return type:     

None

_async _amdelete\(_keys : Sequence\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.amdelete)\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.amget)\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[bytes | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.amset)\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.ayield_keys)\#     

Async get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_AsyncIterator_\[str\]

create\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.create_schema)\#     

Return type:     

None

drop\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.drop)\#     

Return type:     

None

mdelete\(_keys : Sequence\[str\]_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[bytes | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/sql.html#SQLStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)