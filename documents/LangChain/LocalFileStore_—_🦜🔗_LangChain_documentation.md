# LocalFileStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/storage/langchain.storage.file_system.LocalFileStore.html
**Word Count:** 515
**Links Count:** 119
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# LocalFileStore\#

_class _langchain.storage.file\_system.LocalFileStore\(

    _root\_path : str | Path_,     _\*_ ,     _chmod\_file : int | None = None_,     _chmod\_dir : int | None = None_,     _update\_atime : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/file_system.html#LocalFileStore)\#     

BaseStore interface that works on the local file system.

Examples

Create a LocalFileStore instance and perform operations on it:               from langchain.storage import LocalFileStore          # Instantiate the LocalFileStore with the root path     file_store = LocalFileStore("/path/to/root")          # Set values for keys     file_store.mset([("key1", b"value1"), ("key2", b"value2")])          # Get values for keys     values = file_store.mget(["key1", "key2"])  # Returns [b"value1", b"value2"]          # Delete keys     file_store.mdelete(["key1"])          # Iterate over keys     for key in file_store.yield_keys():         print(key)  # noqa: T201     

Implement the BaseStore interface for the local file system.

Parameters:     

  * **root\_path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – The root path of the file store. All keys are interpreted as paths relative to this root.

  * **chmod\_file** \(_int_ _|__None_\) – \(optional, defaults to None\) If specified, sets permissions for newly created files, overriding the current umask if needed.

  * **chmod\_dir** \(_int_ _|__None_\) – \(optional, defaults to None\) If specified, sets permissions for newly created dirs, overriding the current umask if needed.

  * **update\_atime** \(_bool_\) – \(optional, defaults to False\) If True, updates the filesystem access time \(but not the modified time\) when a file is read. This allows MRU/LRU cache policies to be implemented for filesystems where access time updates are disabled.

Methods

`__init__`\(root\_path, \*\[, chmod\_file, ...\]\) | Implement the BaseStore interface for the local file system.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Delete the given keys and their associated values.   `mget`\(keys\) | Get the values associated with the given keys.   `mset`\(key\_value\_pairs\) | Set the values for the given keys.   `yield_keys`\(\[prefix\]\) | Get an iterator over keys that match the given prefix.      \_\_init\_\_\(

    _root\_path : str | Path_,     _\*_ ,     _chmod\_file : int | None = None_,     _chmod\_dir : int | None = None_,     _update\_atime : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/file_system.html#LocalFileStore.__init__)\#     

Implement the BaseStore interface for the local file system.

Parameters:     

  * **root\_path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – The root path of the file store. All keys are interpreted as paths relative to this root.

  * **chmod\_file** \(_int_ _|__None_\) – \(optional, defaults to None\) If specified, sets permissions for newly created files, overriding the current umask if needed.

  * **chmod\_dir** \(_int_ _|__None_\) – \(optional, defaults to None\) If specified, sets permissions for newly created dirs, overriding the current umask if needed.

  * **update\_atime** \(_bool_\) – \(optional, defaults to False\) If True, updates the filesystem access time \(but not the modified time\) when a file is read. This allows MRU/LRU cache policies to be implemented for filesystems where access time updates are disabled.

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

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/file_system.html#LocalFileStore.mdelete)\#     

Delete the given keys and their associated values.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys to delete.

Returns:     

None

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → list\[bytes | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/file_system.html#LocalFileStore.mget)\#     

Get the values associated with the given keys.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys.

Returns:     

A sequence of optional values associated with the keys. If a key is not found, the corresponding value will be None.

Return type:     

list\[bytes | None\]

mset\(

    _key\_value\_pairs : Sequence\[tuple\[str, bytes\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/file_system.html#LocalFileStore.mset)\#     

Set the values for the given keys.

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__tuple_ _\[__str_ _,__bytes_ _\]__\]_\) – A sequence of key-value pairs.

Returns:     

None

Return type:     

None

yield\_keys\(

    _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/storage/file_system.html#LocalFileStore.yield_keys)\#     

Get an iterator over keys that match the given prefix.

Parameters:     

**prefix** \(_Optional_ _\[__str_ _\]_\) – The prefix to match.

Returns:     

An iterator over keys that match the given prefix.

Return type:     

Iterator\[str\]

Examples using LocalFileStore

  * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)

  * [LocalFileStore](https://python.langchain.com/docs/integrations/stores/file_system/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)