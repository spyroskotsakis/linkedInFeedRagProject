# EncoderBackedStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/storage/langchain.storage.encoder_backed.EncoderBackedStore.html
**Word Count:** 186
**Links Count:** 125
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# EncoderBackedStore\#

_class _langchain.storage.encoder\_backed.EncoderBackedStore\(

    _store : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, Any\]_,     _key\_encoder : Callable\[\[K\], str\]_,     _value\_serializer : Callable\[\[V\], bytes\]_,     _value\_deserializer : Callable\[\[Any\], V\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore)\#     

Wraps a store with key and value encoders/decoders.

Examples that uses JSON for encoding/decoding:               import json          def key_encoder(key: int) -> str:         return json.dumps(key)          def value_serializer(value: float) -> str:         return json.dumps(value)          def value_deserializer(serialized_value: str) -> float:         return json.loads(serialized_value)          # Create an instance of the abstract store     abstract_store = MyCustomStore()          # Create an instance of the encoder-backed store     store = EncoderBackedStore(         store=abstract_store,         key_encoder=key_encoder,         value_serializer=value_serializer,         value_deserializer=value_deserializer     )          # Use the encoder-backed store methods     store.mset([(1, 3.14), (2, 2.718)])     values = store.mget([1, 2])  # Retrieves [3.14, 2.718]     store.mdelete([1, 2])  # Deletes the keys 1 and 2     

Initialize an EncodedStore.

Methods

`__init__`\(store, key\_encoder, ...\) | Initialize an EncodedStore.   ---|---   `amdelete`\(keys\) | Delete the given keys and their associated values.   `amget`\(keys\) | Get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      Parameters:     

  * **store** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__Any_ _\]_\)

  * **key\_encoder** \(_Callable_ _\[__\[__K_ _\]__,__str_ _\]_\)

  * **value\_serializer** \(_Callable_ _\[__\[__V_ _\]__,__bytes_ _\]_\)

  * **value\_deserializer** \(_Callable_ _\[__\[__Any_ _\]__,__V_ _\]_\)

\_\_init\_\_\(

    _store : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, Any\]_,     _key\_encoder : Callable\[\[K\], str\]_,     _value\_serializer : Callable\[\[V\], bytes\]_,     _value\_deserializer : Callable\[\[Any\], V\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.__init__)\#     

Initialize an EncodedStore.

Parameters:     

  * **store** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__Any_ _\]_\)

  * **key\_encoder** \(_Callable_ _\[__\[__K_ _\]__,__str_ _\]_\)

  * **value\_serializer** \(_Callable_ _\[__\[__V_ _\]__,__bytes_ _\]_\)

  * **value\_deserializer** \(_Callable_ _\[__\[__Any_ _\]__,__V_ _\]_\)

Return type:     

None

_async _amdelete\(

    _keys : Sequence\[K\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.amdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\)

Return type:     

None

_async _amget\(

    _keys : Sequence\[K\]_, \) → list\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.amget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\)

Return type:     

list\[_V_ | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[tuple\[K, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.amset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\)

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[K\] | AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.ayield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _|__None_\)

Return type:     

_AsyncIterator_\[_K_\] | _AsyncIterator_\[str\]

mdelete\(

    _keys : Sequence\[K\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\)

Return type:     

None

mget\(

    _keys : Sequence\[K\]_, \) → list\[V | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\)

Return type:     

list\[_V_ | None\]

mset\(

    _key\_value\_pairs : Sequence\[tuple\[K, V\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\)

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[K\] | Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/encoder_backed.html#EncoderBackedStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _|__None_\)

Return type:     

_Iterator_\[_K_\] | _Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)