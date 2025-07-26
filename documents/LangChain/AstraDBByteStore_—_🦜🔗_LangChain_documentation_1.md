# AstraDBByteStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBByteStore.html
**Word Count:** 584
**Links Count:** 152
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# AstraDBByteStore\#

_class _langchain\_community.storage.astradb.AstraDBByteStore\(

    _collection\_name : str_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : [AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") | None = None_,     _namespace : str | None = None_,     _\*_ ,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBByteStore)\#     

Deprecated since version 0.0.22: Use `:class:`~langchain_astradb.AstraDBByteStore`` instead. It will not be removed until langchain-community==1.0.

ByteStore implementation using DataStax AstraDB as the underlying store.

The bytes values are converted to base64 encoded strings Documents in the AstraDB collection will have the format               {       "_id": "<key>",       "value": "<byte64 string value>"     }     

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

Methods

`__init__`\(collection\_name\[, token, ...\]\) | ByteStore implementation using DataStax AstraDB as the underlying store.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `decode_value`\(value\) | Decodes value from Astra DB   `encode_value`\(value\) | Encodes value for Astra DB   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(

    _collection\_name : str_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : [AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") | None = None_,     _namespace : str | None = None_,     _\*_ ,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBByteStore.__init__)\#     

ByteStore implementation using DataStax AstraDB as the underlying store.

The bytes values are converted to base64 encoded strings Documents in the AstraDB collection will have the format               {       "_id": "<key>",       "value": "<byte64 string value>"     }     

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[str\]_, \) → None\#     

Async delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → List\[V | None\]\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, V\]\]_, \) → None\#     

Async set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[str\]\#     

Async get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_AsyncIterator_\[str\]

decode\_value\(

    _value : Any_, \) → bytes | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBByteStore.decode_value)\#     

Decodes value from Astra DB

Parameters:     

**value** \(_Any_\)

Return type:     

bytes | None

encode\_value\(

    _value : bytes | None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/astradb.html#AstraDBByteStore.encode_value)\#     

Encodes value for Astra DB

Parameters:     

**value** \(_bytes_ _|__None_\)

Return type:     

_Any_

mdelete\(

    _keys : Sequence\[str\]_, \) → None\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[V | None\]\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[_V_ | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, V\]\]_, \) → None\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\]\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)