# CacheBackedEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/embeddings/langchain.embeddings.cache.CacheBackedEmbeddings.html
**Word Count:** 547
**Links Count:** 134
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# CacheBackedEmbeddings\#

_class _langchain.embeddings.cache.CacheBackedEmbeddings\(

    _underlying\_embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _document\_embedding\_store : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, list\[float\]\]_,     _\*_ ,     _batch\_size : int | None = None_,     _query\_embedding\_store : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, list\[float\]\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings)\#     

Interface for caching results from embedding models.

The interface allows works with any store that implements the abstract store interface accepting keys of type str and values of list of floats.

If need be, the interface can be extended to accept other implementations of the value serializer and deserializer, as well as the key encoder.

Note that by default only document embeddings are cached. To cache query embeddings too, pass in a query\_embedding\_store to constructor.

Examples

Initialize the embedder.

Parameters:     

  * **underlying\_embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – the embedder to use for computing embeddings.

  * **document\_embedding\_store** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__list_ _\[__float_ _\]__\]_\) – The store to use for caching document embeddings.

  * **batch\_size** \(_Optional_ _\[__int_ _\]_\) – The number of documents to embed between store updates.

  * **query\_embedding\_store** \(_Optional_ _\[_[_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__list_ _\[__float_ _\]__\]__\]_\) – The store to use for caching query embeddings. If `None`, query embeddings are not cached.

Methods

`__init__`\(underlying\_embeddings, ...\[, ...\]\) | Initialize the embedder.   ---|---   `aembed_documents`\(texts\) | Embed a list of texts.   `aembed_query`\(text\) | Embed query text.   `embed_documents`\(texts\) | Embed a list of texts.   `embed_query`\(text\) | Embed query text.   `from_bytes_store`\(underlying\_embeddings, ...\) | On-ramp that adds the necessary serialization and encoding to the store.      \_\_init\_\_\(

    _underlying\_embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _document\_embedding\_store : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, list\[float\]\]_,     _\*_ ,     _batch\_size : int | None = None_,     _query\_embedding\_store : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, list\[float\]\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings.__init__)\#     

Initialize the embedder.

Parameters:     

  * **underlying\_embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – the embedder to use for computing embeddings.

  * **document\_embedding\_store** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__list_ _\[__float_ _\]__\]_\) – The store to use for caching document embeddings.

  * **batch\_size** \(_int_ _|__None_\) – The number of documents to embed between store updates.

  * **query\_embedding\_store** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__list_ _\[__float_ _\]__\]__|__None_\) – The store to use for caching query embeddings. If `None`, query embeddings are not cached.

Return type:     

None

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings.aembed_documents)\#     

Embed a list of texts.

The method first checks the cache for the embeddings. If the embeddings are not found, the method uses the underlying embedder to embed the documents and stores the results in the cache.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – A list of texts to embed.

Returns:     

A list of embeddings for the given texts.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings.aembed_query)\#     

Embed query text.

By default, this method does not cache queries. To enable caching, set the `cache_query` parameter to `True` when initializing the embedder.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

The embedding for the given text.

Return type:     

list\[float\]

embed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings.embed_documents)\#     

Embed a list of texts.

The method first checks the cache for the embeddings. If the embeddings are not found, the method uses the underlying embedder to embed the documents and stores the results in the cache.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – A list of texts to embed.

Returns:     

A list of embeddings for the given texts.

Return type:     

list\[list\[float\]\]

embed\_query\(_text : str_\) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings.embed_query)\#     

Embed query text.

By default, this method does not cache queries. To enable caching, set the `cache_query` parameter to `True` when initializing the embedder.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

The embedding for the given text.

Return type:     

list\[float\]

_classmethod _from\_bytes\_store\(

    _underlying\_embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _document\_embedding\_cache : [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, bytes\]_,     _\*_ ,     _namespace : str = ''_,     _batch\_size : int | None = None_,     _query\_embedding\_cache : bool | [BaseStore](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore")\[str, bytes\] = False_,     _key\_encoder : Callable\[\[str\], str\] | Literal\['sha1', 'blake2b', 'sha256', 'sha512'\] = 'sha1'_, \) → CacheBackedEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/embeddings/cache.html#CacheBackedEmbeddings.from_bytes_store)\#     

On-ramp that adds the necessary serialization and encoding to the store.

Parameters:     

  * **underlying\_embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – The embedder to use for embedding.

  * **document\_embedding\_cache** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__bytes_ _\]_\) – The cache to use for storing document embeddings.

  * **\***

  * **namespace** \(_str_\)

  * **batch\_size** \(_int_ _|__None_\)

  * **query\_embedding\_cache** \(_bool_ _|_[_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__bytes_ _\]_\)

  * **key\_encoder** \(_Callable_ _\[__\[__str_ _\]__,__str_ _\]__|__Literal_ _\[__'sha1'__,__'blake2b'__,__'sha256'__,__'sha512'__\]_\)

Return type:     

_CacheBackedEmbeddings_

:param : :param namespace: The namespace to use for document cache.

> This namespace is used to avoid collisions with other caches. For example, set it to the name of the embedding model used.

Parameters:     

  * **batch\_size** \(_int_ _|__None_\) – The number of documents to embed between store updates.

  * **query\_embedding\_cache** \(_bool_ _|_[_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__bytes_ _\]_\) – The cache to use for storing query embeddings. True to use the same cache as document embeddings. False to not cache query embeddings.

  * **key\_encoder** \(_Callable_ _\[__\[__str_ _\]__,__str_ _\]__|__Literal_ _\[__'sha1'__,__'blake2b'__,__'sha256'__,__'sha512'__\]_\) – 

Optional callable to encode keys. If not provided, a default encoder using SHA-1 will be used. SHA-1 is not collision-resistant, and a motivated attacker could craft two different texts that hash to the same cache key.

New applications should use one of the alternative encoders or provide a custom and strong key encoder function to avoid this risk.

If you change a key encoder in an existing cache, consider just creating a new cache, to avoid \(the potential for\) collisions with existing keys or having duplicate keys for the same text in the cache.

  * **underlying\_embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **document\_embedding\_cache** \([_BaseStore_](https://python.langchain.com/api_reference/core/stores/langchain_core.stores.BaseStore.html#langchain_core.stores.BaseStore "langchain_core.stores.BaseStore") _\[__str_ _,__bytes_ _\]_\)

  * **namespace** \(_str_\)

Returns:     

An instance of CacheBackedEmbeddings that uses the provided cache.

Return type:     

_CacheBackedEmbeddings_

Examples using CacheBackedEmbeddings

  * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)