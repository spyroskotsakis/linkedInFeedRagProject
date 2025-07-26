# DataStoreDocumentStorage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.document_storage.DataStoreDocumentStorage.html
**Word Count:** 302
**Links Count:** 121
**Scraped:** 2025-07-21 08:27:19
**Status:** completed

---

# DataStoreDocumentStorage\#

_class _langchain\_google\_vertexai.vectorstores.document\_storage.DataStoreDocumentStorage\(

    _datastore\_client : datastore.Client_,     _kind : str = 'document\_id'_,     _text\_property\_name : str = 'text'_,     _metadata\_property\_name : str = 'metadata'_,     _exclude\_from\_indexes : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#DataStoreDocumentStorage)\#     

Stores documents in Google Cloud DataStore.

Constructor. :param bucket: Bucket where the documents will be stored. :param prefix: Prefix that is prepended to all document names.

Methods

`__init__`\(datastore\_client\[, kind, ...\]\) | Constructor.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Deletes a sequence of documents by key.   `mget`\(keys\) | Gets a batch of documents by id.   `mset`\(key\_value\_pairs\) | Stores a series of documents using each keys   `yield_keys`\(\*\[, prefix\]\) | Yields the keys of all documents in the storage.      Parameters:     

  * **datastore\_client** \(_datastore.Client_\)

  * **kind** \(_str_\)

  * **text\_property\_name** \(_str_\)

  * **metadata\_property\_name** \(_str_\)

  * **exclude\_from\_indexes** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

\_\_init\_\_\(

    _datastore\_client : datastore.Client_,     _kind : str = 'document\_id'_,     _text\_property\_name : str = 'text'_,     _metadata\_property\_name : str = 'metadata'_,     _exclude\_from\_indexes : List\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#DataStoreDocumentStorage.__init__)\#     

Constructor. :param bucket: Bucket where the documents will be stored. :param prefix: Prefix that is prepended to all document names.

Parameters:     

  * **datastore\_client** \(_datastore.Client_\)

  * **kind** \(_str_\)

  * **text\_property\_name** \(_str_\)

  * **metadata\_property\_name** \(_str_\)

  * **exclude\_from\_indexes** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

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

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#DataStoreDocumentStorage.mdelete)\#     

Deletes a sequence of documents by key.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – A sequence of keys to delete.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#DataStoreDocumentStorage.mget)\#     

Gets a batch of documents by id. :param ids: List of ids for the text.

Returns:     

List of texts. If the key id is not found for any id record returns a None     

instead.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#DataStoreDocumentStorage.mset)\#     

Stores a series of documents using each keys

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__Tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#DataStoreDocumentStorage.yield_keys)\#     

Yields the keys of all documents in the storage.

Parameters:     

**prefix** \(_str_ _|__None_\) – Ignored

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)