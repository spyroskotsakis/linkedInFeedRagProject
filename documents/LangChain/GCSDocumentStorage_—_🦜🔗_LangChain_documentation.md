# GCSDocumentStorage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/vectorstores/langchain_google_vertexai.vectorstores.document_storage.GCSDocumentStorage.html
**Word Count:** 343
**Links Count:** 121
**Scraped:** 2025-07-21 08:27:18
**Status:** completed

---

# GCSDocumentStorage\#

_class _langchain\_google\_vertexai.vectorstores.document\_storage.GCSDocumentStorage\(

    _bucket : Bucket_,     _prefix : str | None = 'documents'_,     _threaded =True_,     _n\_threads =8_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#GCSDocumentStorage)\#     

Stores documents in Google Cloud Storage. For each pair id, document\_text the name of the blob will be \{prefix\}/\{id\} stored in plain text format.

Constructor. :param bucket: Bucket where the documents will be stored. :param prefix: Prefix that is prepended to all document names.

Methods

`__init__`\(bucket\[, prefix, threaded, n\_threads\]\) | Constructor.   ---|---   `amdelete`\(keys\) | Async delete the given keys and their associated values.   `amget`\(keys\) | Async get the values associated with the given keys.   `amset`\(key\_value\_pairs\) | Async set the values for the given keys.   `ayield_keys`\(\*\[, prefix\]\) | Async get an iterator over keys that match the given prefix.   `mdelete`\(keys\) | Deletes a batch of documents by id.   `mget`\(keys\) | Gets a batch of documents by id.   `mset`\(key\_value\_pairs\) | Stores a series of documents using each keys   `yield_keys`\(\*\[, prefix\]\) | Yields the keys present in the storage.      Parameters:     

  * **bucket** \(_storage.Bucket_\)

  * **prefix** \(_Optional_ _\[__str_ _\]_\)

\_\_init\_\_\(

    _bucket : Bucket_,     _prefix : str | None = 'documents'_,     _threaded =True_,     _n\_threads =8_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#GCSDocumentStorage.__init__)\#     

Constructor. :param bucket: Bucket where the documents will be stored. :param prefix: Prefix that is prepended to all document names.

Parameters:     

  * **bucket** \(_Bucket_\)

  * **prefix** \(_str_ _|__None_\)

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

    _keys : Sequence\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#GCSDocumentStorage.mdelete)\#     

Deletes a batch of documents by id.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\) – List of ids for the text.

Return type:     

None

mget\(

    _keys : Sequence\[str\]_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#GCSDocumentStorage.mget)\#     

Gets a batch of documents by id. The default implementation only loops get\_by\_id. Subclasses that have faster ways to retrieve data by batch should implement this method. :param ids: List of ids for the text.

Returns:     

List of documents. If the key id is not found for any id record returns a     

None instead.

Parameters:     

**keys** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None\]

mset\(

    _key\_value\_pairs : Sequence\[Tuple\[str, [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#GCSDocumentStorage.mset)\#     

Stores a series of documents using each keys

Parameters:     

**key\_value\_pairs** \(_Sequence_ _\[__Tuple_ _\[__K_ _,__V_ _\]__\]_\) – A sequence of key-value pairs.

Return type:     

None

yield\_keys\(

    _\*_ ,     _prefix : str | None = None_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/vectorstores/document_storage.html#GCSDocumentStorage.yield_keys)\#     

Yields the keys present in the storage.

Parameters:     

**prefix** \(_str_ _|__None_\) – Ignored. Uses the prefix provided in the constructor.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)