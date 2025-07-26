# MongoDBByteStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage/langchain_community.storage.mongodb.MongoDBByteStore.html
**Word Count:** 356
**Links Count:** 142
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# MongoDBByteStore\#

_class _langchain\_community.storage.mongodb.MongoDBByteStore\(

    _connection\_string : str_,     _db\_name : str_,     _collection\_name : str_,     _\*_ ,     _client\_kwargs : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/mongodb.html#MongoDBByteStore)\#     

BaseStore implementation using MongoDB as the underlying store.

Examples

Create a MongoDBByteStore instance and perform operations on it:               # Instantiate the MongoDBByteStore with a MongoDB connection     from langchain.storage import MongoDBByteStore          mongo_conn_str = "mongodb://localhost:27017/"     mongodb_store = MongoDBBytesStore(mongo_conn_str, db_name="test-db",                                  collection_name="test-collection")          # Set values for keys     mongodb_store.mset([("key1", "hello"), ("key2", "workd")])          # Get values for keys     values = mongodb_store.mget(["key1", "key2"])     # [bytes1, bytes1]          # Iterate over keys     for key in mongodb_store.yield_keys():         print(key)          # Delete keys     mongodb_store.mdelete(["key1", "key2"])     

Initialize the MongoDBStore with a MongoDB connection string.

Parameters:     

  * **connection\_string** \(_str_\) – MongoDB connection string

  * **db\_name** \(_str_\) – name to use

  * **collection\_name** \(_str_\) – collection name to use

  * **client\_kwargs** \(_dict_\) – Keyword arguments to pass to the Mongo client

Methods

`__init__`\(connection\_string, db\_name, ...\[, ...\]\) | Initialize the MongoDBStore with a MongoDB connection string.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given ids.   `mget`\(keys\) | Get the list of documents associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the given key-value pairs.   `yield_keys`\(\[prefix\]\) | Yield keys in the store.      \_\_init\_\_\(

    _connection\_string : str_,     _db\_name : str_,     _collection\_name : str_,     _\*_ ,     _client\_kwargs : dict | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/mongodb.html#MongoDBByteStore.__init__)\#     

Initialize the MongoDBStore with a MongoDB connection string.

Parameters:     

  * **connection\_string** \(_str_\) – MongoDB connection string

  * **db\_name** \(_str_\) – name to use

  * **collection\_name** \(_str_\) – collection name to use

  * **client\_kwargs** \(_dict_\) – Keyword arguments to pass to the Mongo client

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

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/mongodb.html#MongoDBByteStore.mdelete)\#     

Delete the given ids.

Parameters:     

**keys** \(_list_ _\[__str_ _\]_\) – A list of keys representing Document IDs..

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/mongodb.html#MongoDBByteStore.mget)\#     

Get the list of documents associated with the given keys.

Parameters:     

**keys** \(_list_ _\[__str_ _\]_\) – A list of keys representing Document IDs..

Returns:     

A list of Documents corresponding to the provided     

keys, where each Document is either retrieved successfully or represented as None if not found.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/mongodb.html#MongoDBByteStore.mset)\#     

Set the given key-value pairs.

Parameters:     

**key\_value\_pairs** \(_list_ _\[__tuple_ _\[__str_ _,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__\]_\) – A list of id-document pairs.

Return type:     

None

yield\_keys\(

    _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/storage/mongodb.html#MongoDBByteStore.yield_keys)\#     

Yield keys in the store.

Parameters:     

**prefix** \(_str_\) – prefix of keys to retrieve.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)