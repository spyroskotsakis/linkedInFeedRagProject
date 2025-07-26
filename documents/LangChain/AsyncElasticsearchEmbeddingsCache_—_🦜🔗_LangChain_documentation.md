# AsyncElasticsearchEmbeddingsCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/cache/langchain_elasticsearch.cache.AsyncElasticsearchEmbeddingsCache.html
**Word Count:** 690
**Links Count:** 129
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# AsyncElasticsearchEmbeddingsCache\#

_class _langchain\_elasticsearch.cache.AsyncElasticsearchEmbeddingsCache\(

    _index\_name : str_,     _store\_input : bool = True_,     _metadata : Dict\[str, Any\] | None = None_,     _namespace : str | None = None_,     _maximum\_duplicates\_allowed : int = 1_,     _\*_ ,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _es\_params : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/cache.html#AsyncElasticsearchEmbeddingsCache)\#     

Initialize the Elasticsearch cache store by specifying the index/alias to use and determining which additional information \(like input, input parameters, and any other metadata\) should be stored in the cache. Provide a namespace to organize the cache.

Parameters:     

  * **index\_name** \(_str_\) – The name of the index or the alias to use for the cache. If they do not exist an index is created, according to the default mapping defined by the mapping property.

  * **store\_input** \(_bool_\) – Whether to store the input in the cache. Default to True.

  * **metadata** \(_Optional_ _\[__dict_ _\]_\) – Additional metadata to store in the cache, for filtering purposes. This must be JSON serializable in an Elasticsearch document. Default to None.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – A namespace to use for the cache.

  * **maximum\_duplicates\_allowed** \(_int_\) – Defines the maximum number of duplicate keys permitted. Must be used in scenarios where the same key appears across multiple indices that share the same alias. Default to 1.

  * **es\_url** \(_str_ _|__None_\) – URL of the Elasticsearch instance to connect to.

  * **es\_cloud\_id** \(_str_ _|__None_\) – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** \(_str_ _|__None_\) – Username to use when connecting to Elasticsearch.

  * **es\_password** \(_str_ _|__None_\) – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** \(_str_ _|__None_\) – API key to use when connecting to Elasticsearch.

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Other parameters for the Elasticsearch client.

Attributes

`mapping` | Get the default mapping for the index.   ---|---      Methods

`__init__`\(index\_name\[, store\_input, ...\]\) | Initialize the Elasticsearch cache store by specifying the index/alias to use and determining which additional information \(like input, input parameters, and any other metadata\) should be stored in the cache.   ---|---   `amdelete`\(keys\) | Delete the given keys and their associated values.   `amget`\(keys\) | Get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.   `build_document`\(text\_input, vector\) | Build the Elasticsearch document for storing a single embedding   `decode_vector`\(data\) | Decode the base64 string to vector data as bytes.   `encode_vector`\(data\) | Encode the vector data as bytes to as a base64 string.   `is_alias`\(\) |    `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\*\[, prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(

    _index\_name : str_,     _store\_input : bool = True_,     _metadata : Dict\[str, Any\] | None = None_,     _namespace : str | None = None_,     _maximum\_duplicates\_allowed : int = 1_,     _\*_ ,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _es\_params : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.__init__)\#     

Initialize the Elasticsearch cache store by specifying the index/alias to use and determining which additional information \(like input, input parameters, and any other metadata\) should be stored in the cache. Provide a namespace to organize the cache.

Parameters:     

  * **index\_name** \(_str_\) – The name of the index or the alias to use for the cache. If they do not exist an index is created, according to the default mapping defined by the mapping property.

  * **store\_input** \(_bool_\) – Whether to store the input in the cache. Default to True.

  * **metadata** \(_Optional_ _\[__dict_ _\]_\) – Additional metadata to store in the cache, for filtering purposes. This must be JSON serializable in an Elasticsearch document. Default to None.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – A namespace to use for the cache.

  * **maximum\_duplicates\_allowed** \(_int_\) – Defines the maximum number of duplicate keys permitted. Must be used in scenarios where the same key appears across multiple indices that share the same alias. Default to 1.

  * **es\_url** \(_str_ _|__None_\) – URL of the Elasticsearch instance to connect to.

  * **es\_cloud\_id** \(_str_ _|__None_\) – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** \(_str_ _|__None_\) – Username to use when connecting to Elasticsearch.

  * **es\_password** \(_str_ _|__None_\) – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** \(_str_ _|__None_\) – API key to use when connecting to Elasticsearch.

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Other parameters for the Elasticsearch client.

_async _amdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.amdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

None

_async _amget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.amget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

_List_\[bytes | None\]

_async _amset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.amset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__Tuple_ _\[__str_ _,__bytes_ _\]__\]_\)

Return type:     

None

_async _ayield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → AsyncIterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.ayield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_ _|__None_\)

Return type:     

_AsyncIterator_\[str\]

build\_document\(

    _text\_input : str_,     _vector : bytes_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.build_document)\#     

Build the Elasticsearch document for storing a single embedding

Parameters:     

  * **text\_input** \(_str_\)

  * **vector** \(_bytes_\)

Return type:     

_Dict_\[str, _Any_\]

_static _decode\_vector\(

    _data : str_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.decode_vector)\#     

Decode the base64 string to vector data as bytes.

Parameters:     

**data** \(_str_\)

Return type:     

bytes

_static _encode\_vector\(

    _data : bytes_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.encode_vector)\#     

Encode the vector data as bytes to as a base64 string.

Parameters:     

**data** \(_bytes_\)

Return type:     

str

_async _is\_alias\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/cache.html#AsyncElasticsearchEmbeddingsCache.is_alias)\#     

Return type:     

bool

mdelete\(

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/cache.html#AsyncElasticsearchEmbeddingsCache.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/cache.html#AsyncElasticsearchEmbeddingsCache.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__K_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

_List_\[bytes | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/cache.html#AsyncElasticsearchEmbeddingsCache.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/cache.html#AsyncElasticsearchEmbeddingsCache.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_str_\) – The prefix to match.

Yields:     

_Iterator\[K | str\]_ – An iterator over keys that match the given prefix. This method is allowed to return an iterator over either K or str depending on what makes more sense for the given store.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)