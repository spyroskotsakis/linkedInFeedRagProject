# CassandraByteStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage/langchain_community.storage.cassandra.CassandraByteStore.html
**Word Count:** 465
**Links Count:** 169
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# CassandraByteStore\#

_class _langchain\_community.storage.cassandra.CassandraByteStore\(

    _table : str_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore)\#     

A ByteStore implementation using Cassandra as the backend.

Parameters:     

  * **table** \(_str_\) – The name of the table to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – A Cassandra session object. If not provided, it will be resolved from the cassio config.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – The keyspace to use. If not provided, it will be resolved from the cassio config.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – The setup mode to use. Default is SYNC \(SetupMode.SYNC\).

Methods

`__init__`\(table, \*\[, session, keyspace, ...\]\) |    ---|---   `aensure_db_setup`\(\) | Ensure that the DB setup is finished.   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `ensure_db_setup`\(\) | Ensure that the DB setup is finished.   `get_delete_statement`\(\) | Get the prepared delete statement for the table.   `get_insert_statement`\(\) | Get the prepared insert statement for the table.   `get_select_statement`\(\) | Get the prepared select statement for the table.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(

    _table : str_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.__init__)\#     

Parameters:     

  * **table** \(_str_\)

  * **session** \(_Optional_ _\[__Session_ _\]_\)

  * **keyspace** \(_Optional_ _\[__str_ _\]_\)

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\)

Return type:     

None

_async _aensure\_db\_setup\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.aensure_db_setup)\#     

Ensure that the DB setup is finished. If not, wait for it.

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.amdelete)\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.amget)\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[bytes | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.amset)\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.ayield_keys)\#     

Async get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_AsyncIterator_\[str\]

ensure\_db\_setup\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.ensure_db_setup)\#     

Ensure that the DB setup is finished. If not, raise a ValueError.

Return type:     

None

get\_delete\_statement\(\) → PreparedStatement[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.get_delete_statement)\#     

Get the prepared delete statement for the table. If not available, prepare it.

Returns:     

The prepared statement.

Return type:     

PreparedStatement

get\_insert\_statement\(\) → PreparedStatement[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.get_insert_statement)\#     

Get the prepared insert statement for the table. If not available, prepare it.

Returns:     

The prepared statement.

Return type:     

PreparedStatement

get\_select\_statement\(\) → PreparedStatement[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.get_select_statement)\#     

Get the prepared select statement for the table. If not available, prepare it.

Returns:     

The prepared statement.

Return type:     

PreparedStatement

mdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[bytes | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/cassandra.html#CassandraByteStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_Iterator_\[str\]

Examples using CassandraByteStore

  * [CassandraByteStore](https://python.langchain.com/docs/integrations/stores/cassandra/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)