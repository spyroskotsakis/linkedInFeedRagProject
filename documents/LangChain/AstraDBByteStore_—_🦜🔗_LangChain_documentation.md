# AstraDBByteStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/storage/langchain_astradb.storage.AstraDBByteStore.html
**Word Count:** 873
**Links Count:** 116
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBByteStore\#

_class _langchain\_astradb.storage.AstraDBByteStore\(

    _\*_ ,     _collection\_name : str_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/storage.html#AstraDBByteStore)\#     

ByteStore implementation using DataStax AstraDB as the underlying store.

The bytes values are converted to base64 encoded strings Documents in the AstraDB collection will have the format

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Methods

`__init__`\(\*, collection\_name\[, token, ...\]\) | ByteStore implementation using DataStax AstraDB as the underlying store.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `decode_value`\(value\) | Decodes value from Astra DB.   `encode_value`\(value\) | Encodes value for Astra DB.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(

    _\*_ ,     _collection\_name : str_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/storage.html#AstraDBByteStore.__init__)\#     

ByteStore implementation using DataStax AstraDB as the underlying store.

The bytes values are converted to base64 encoded strings Documents in the AstraDB collection will have the format

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

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

    _keys : Sequence\[str\]_, \) → list\[V | None\]\#     

Async get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[tuple\[str, V\]\]_, \) → None\#     

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

    _value : Any_, \) → bytes | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/storage.html#AstraDBByteStore.decode_value)\#     

Decodes value from Astra DB.

Parameters:     

**value** \(_Any_\)

Return type:     

bytes | None

encode\_value\(

    _value : bytes | None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/storage.html#AstraDBByteStore.encode_value)\#     

Encodes value for Astra DB.

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

    _keys : Sequence\[str\]_, \) → list\[V | None\]\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[_V_ | None\]

mset\(

    _key\_value\_pairs : Sequence\[tuple\[str, V\]\]_, \) → None\#     

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