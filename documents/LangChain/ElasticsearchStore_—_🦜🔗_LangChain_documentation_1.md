# ElasticsearchStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/vectorstores/langchain_elasticsearch.vectorstores.ElasticsearchStore.html
**Word Count:** 2626
**Links Count:** 273
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# ElasticsearchStore\#

_class _langchain\_elasticsearch.vectorstores.ElasticsearchStore\(

    _index\_name: str_,     _\*_ ,     _embedding: ~langchain\_core.embeddings.embeddings.Embeddings | None = None_,     _es\_connection: ~elasticsearch.Elasticsearch | None = None_,     _es\_url: str | None = None_,     _es\_cloud\_id: str | None = None_,     _es\_user: str | None = None_,     _es\_api\_key: str | None = None_,     _es\_password: str | None = None_,     _vector\_query\_field: str = 'vector'_,     _query\_field: str = 'text'_,     _distance\_strategy: ~typing.Literal\[DistanceStrategy.COSINE_,     _DistanceStrategy.DOT\_PRODUCT_ ,     _DistanceStrategy.EUCLIDEAN\_DISTANCE_ ,     _DistanceStrategy.MAX\_INNER\_PRODUCT\] | None = None_,     _strategy: ~langchain\_elasticsearch.\_utilities.BaseRetrievalStrategy | ~elasticsearch.helpers.vectorstore.\_sync.strategies.RetrievalStrategy = <langchain\_elasticsearch.\_utilities.ApproxRetrievalStrategy object>_,     _es\_params: ~typing.Dict\[str_,     _~typing.Any\] | None = None_,     _custom\_index\_settings: ~typing.Dict\[str_,     _~typing.Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/vectorstores.html#ElasticsearchStore)\#     

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`ApproxRetrievalStrategy`\(\[query\_model\_id, ...\]\) | Used to perform approximate nearest neighbor search using the HNSW algorithm.   ---|---   `BM25RetrievalStrategy`\(\[k1, b\]\) | Used to apply BM25 without vector search.   `ExactRetrievalStrategy`\(\) | Used to perform brute force / exact nearest neighbor search via script\_score.   `SparseVectorRetrievalStrategy`\(\[model\_id\]\) | Used to perform sparse vector search via text\_expansion.   `__init__`\(index\_name, \*\[, embedding, ...\]\) |    `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(text\_embeddings\[, metadatas, ...\]\) | Add the given texts and embeddings to the store.   `add_texts`\(texts\[, metadatas, ids, ...\]\) | Run more texts through the embeddings and add to the store.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `close`\(\) |    `connect_to_elasticsearch`\(\*\[, es\_url, ...\]\) |    `delete`\(\[ids, refresh\_indices\]\) | Delete documents from the Elasticsearch index.   `from_documents`\(documents\[, embedding, ...\]\) | Construct ElasticsearchStore wrapper from documents.   `from_texts`\(texts\[, embedding, metadatas, ...\]\) | Construct ElasticsearchStore wrapper from raw documents.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, fetch\_k, ...\]\) | Return Elasticsearch documents most similar to query.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_by_vector_with_relevance_scores`\(...\) | Return Elasticsearch documents most similar to query, along with scores.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return Elasticsearch documents most similar to query, along with scores.      Parameters:     

  * **index\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **es\_connection** \(_Elasticsearch_ _|__None_\)

  * **es\_url** \(_str_ _|__None_\)

  * **es\_cloud\_id** \(_str_ _|__None_\)

  * **es\_user** \(_str_ _|__None_\)

  * **es\_api\_key** \(_str_ _|__None_\)

  * **es\_password** \(_str_ _|__None_\)

  * **vector\_query\_field** \(_str_\)

  * **query\_field** \(_str_\)

  * **distance\_strategy** \(_Literal_ _\[__DistanceStrategy.COSINE_ _,__DistanceStrategy.DOT\_PRODUCT_ _,__DistanceStrategy.EUCLIDEAN\_DISTANCE_ _,__DistanceStrategy.MAX\_INNER\_PRODUCT_ _\]__|__None_\)

  * **strategy** \(_BaseRetrievalStrategy_ _|__RetrievalStrategy_\)

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **custom\_index\_settings** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

_static _ApproxRetrievalStrategy\(

    _query\_model\_id : str | None = None_,     _hybrid : bool | None = False_,     _rrf : dict | bool | None = True_, \) → ApproxRetrievalStrategy[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.ApproxRetrievalStrategy)\#     

Used to perform approximate nearest neighbor search using the HNSW algorithm.

At build index time, this strategy will create a dense vector field in the index and store the embedding vectors in the index.

At query time, the text will either be embedded using the provided embedding function or the query\_model\_id will be used to embed the text using the model deployed to Elasticsearch.

if query\_model\_id is used, do not provide an embedding function.

Parameters:     

  * **query\_model\_id** \(_str_ _|__None_\) – Optional. ID of the model to use to embed the query text within the stack. Requires embedding model to be deployed to Elasticsearch.

  * **hybrid** \(_bool_ _|__None_\) – Optional. If True, will perform a hybrid search using both the knn query and a text query. Defaults to False.

  * **rrf** \(_dict_ _|__bool_ _|__None_\) – 

Optional. rrf is Reciprocal Rank Fusion. When hybrid is True,

> and rrf is True, then rrf: \{\}. and rrf is False, then rrf is omitted. and isinstance\(rrf, dict\) is True, then pass in the dict values.

rrf could be passed for adjusting ‘rank\_constant’ and ‘window\_size’.

Return type:     

_ApproxRetrievalStrategy_

_static _BM25RetrievalStrategy\(

    _k1 : float | None = None_,     _b : float | None = None_, \) → BM25RetrievalStrategy[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.BM25RetrievalStrategy)\#     

Used to apply BM25 without vector search.

Parameters:     

  * **k1** \(_float_ _|__None_\) – Optional. This corresponds to the BM25 parameter, k1. Default is None, which uses the default setting of Elasticsearch.

  * **b** \(_float_ _|__None_\) – Optional. This corresponds to the BM25 parameter, b. Default is None, which uses the default setting of Elasticsearch.

Return type:     

_BM25RetrievalStrategy_

_static _ExactRetrievalStrategy\(\) → ExactRetrievalStrategy[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.ExactRetrievalStrategy)\#     

Used to perform brute force / exact nearest neighbor search via script\_score.

Return type:     

_ExactRetrievalStrategy_

_static _SparseVectorRetrievalStrategy\(

    _model\_id : str | None = None_, \) → SparseRetrievalStrategy[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.SparseVectorRetrievalStrategy)\#     

Used to perform sparse vector search via text\_expansion. Used for when you want to use ELSER model to perform document search.

At build index time, this strategy will create a pipeline that will embed the text using the ELSER model and store the resulting tokens in the index.

At query time, the text will be embedded using the ELSER model and the resulting tokens will be used to perform a text\_expansion query.

Parameters:     

**model\_id** \(_str_ _|__None_\) – Optional. Default is “.elser\_model\_1”. ID of the model to use to embed the query text within the stack. Requires embedding model to be deployed to Elasticsearch.

Return type:     

_SparseRetrievalStrategy_

\_\_init\_\_\(

    _index\_name: str_,     _\*_ ,     _embedding: ~langchain\_core.embeddings.embeddings.Embeddings | None = None_,     _es\_connection: ~elasticsearch.Elasticsearch | None = None_,     _es\_url: str | None = None_,     _es\_cloud\_id: str | None = None_,     _es\_user: str | None = None_,     _es\_api\_key: str | None = None_,     _es\_password: str | None = None_,     _vector\_query\_field: str = 'vector'_,     _query\_field: str = 'text'_,     _distance\_strategy: ~typing.Literal\[DistanceStrategy.COSINE_,     _DistanceStrategy.DOT\_PRODUCT_ ,     _DistanceStrategy.EUCLIDEAN\_DISTANCE_ ,     _DistanceStrategy.MAX\_INNER\_PRODUCT\] | None = None_,     _strategy: ~langchain\_elasticsearch.\_utilities.BaseRetrievalStrategy | ~elasticsearch.helpers.vectorstore.\_sync.strategies.RetrievalStrategy = <langchain\_elasticsearch.\_utilities.ApproxRetrievalStrategy object>_,     _es\_params: ~typing.Dict\[str_,     _~typing.Any\] | None = None_,     _custom\_index\_settings: ~typing.Dict\[str_,     _~typing.Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.__init__)\#     

Parameters:     

  * **index\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **es\_connection** \(_Elasticsearch_ _|__None_\)

  * **es\_url** \(_str_ _|__None_\)

  * **es\_cloud\_id** \(_str_ _|__None_\)

  * **es\_user** \(_str_ _|__None_\)

  * **es\_api\_key** \(_str_ _|__None_\)

  * **es\_password** \(_str_ _|__None_\)

  * **vector\_query\_field** \(_str_\)

  * **query\_field** \(_str_\)

  * **distance\_strategy** \(_Literal_ _\[__DistanceStrategy.COSINE_ _,__DistanceStrategy.DOT\_PRODUCT_ _,__DistanceStrategy.EUCLIDEAN\_DISTANCE_ _,__DistanceStrategy.MAX\_INNER\_PRODUCT_ _\]__|__None_\)

  * **strategy** \(_BaseRetrievalStrategy_ _|__RetrievalStrategy_\)

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **custom\_index\_settings** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

_async _aadd\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Async run more documents through the embeddings and add to the vectorstore.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

List of IDs of the added texts.

Raises:     

**ValueError** – If the number of IDs does not match the number of documents.

Return type:     

list\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _\*_ ,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Async run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_Optional_ _\[__list_ _\[__dict_ _\]__\]_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters.

Returns:     

List of ids from adding the texts into the vectorstore.

Raises:     

  * **ValueError** – If the number of metadatas does not match the number of texts.

  * **ValueError** – If the number of ids does not match the number of texts.

Return type:     

list\[str\]

add\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Add or update documents in the vectorstore.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **kwargs** \(_Any_\) – Additional keyword arguments. if kwargs contains ids and documents contain ids, the ids in the kwargs will receive precedence.

Returns:     

List of IDs of the added texts.

Raises:     

**ValueError** – If the number of ids does not match the number of documents.

Return type:     

list\[str\]

add\_embeddings\(

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _refresh\_indices : bool = True_,     _create\_index\_if\_not\_exists : bool = True_,     _bulk\_kwargs : Dict | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.add_embeddings)\#     

Add the given texts and embeddings to the store.

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\) – Iterable pairs of string and embedding to add to the store.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **refresh\_indices** \(_bool_\) – Whether to refresh the Elasticsearch indices after adding the texts.

  * **create\_index\_if\_not\_exists** \(_bool_\) – Whether to create the Elasticsearch index if it doesn’t already exist.

  * **\*bulk\_kwargs** \(_Dict_ _|__None_\) – 

Additional arguments to pass to Elasticsearch bulk. \- chunk\_size: Optional. Number of texts to add to the

> index at a time. Defaults to 500.

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the store.

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[Dict\[Any, Any\]\] | None = None_,     _ids : List\[str\] | None = None_,     _refresh\_indices : bool = True_,     _create\_index\_if\_not\_exists : bool = True_,     _bulk\_kwargs : Dict | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.add_texts)\#     

Run more texts through the embeddings and add to the store.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the store.

  * **metadatas** \(_List_ _\[__Dict_ _\[__Any_ _,__Any_ _\]__\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts.

  * **refresh\_indices** \(_bool_\) – Whether to refresh the Elasticsearch indices after adding the texts.

  * **create\_index\_if\_not\_exists** \(_bool_\) – Whether to create the Elasticsearch index if it doesn’t already exist.

  * **\*bulk\_kwargs** \(_Dict_ _|__None_\) – 

Additional arguments to pass to Elasticsearch bulk. \- chunk\_size: Optional. Number of texts to add to the

> index at a time. Defaults to 500.

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the store.

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None\#     

Async delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of ids to delete. If None, delete all. Default is None.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

_async classmethod _afrom\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*\* kwargs: Any_, \) → Self\#     

Async return VectorStore initialized from documents and embeddings.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

VectorStore initialized from documents and embeddings.

Return type:     

[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")

_async classmethod _afrom\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : list\[dict\] | None = None_,     _\*_ ,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → Self\#     

Async return VectorStore initialized from texts and embeddings.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of IDs associated with the texts.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

VectorStore initialized from texts and embeddings.

Return type:     

[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")

_async _aget\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async get documents by their IDs.

The returned documents are expected to have the ID field set to the ID of the document in the vector store.

Fewer documents may be returned than requested if some IDs are not found or if there are duplicated IDs.

Users should not assume that the order of the returned documents matches the order of the input IDs. Instead, users should rely on the ID field of the returned documents.

This method should **NOT** raise exceptions if no documents are found for some IDs.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\) – List of ids to retrieve.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Added in version 0.2.11.

_async _amax\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Default is 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Default is 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

as\_retriever\(

    _\*\* kwargs: Any_, \) → [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\#     

Return VectorStoreRetriever initialized from this VectorStore.

Parameters:     

**\*\*kwargs** \(_Any_\) – 

Keyword arguments to pass to the search function. Can include: search\_type \(Optional\[str\]\): Defines the type of search that

> the Retriever should perform. Can be “similarity” \(default\), “mmr”, or “similarity\_score\_threshold”.

search\_kwargs \(Optional\[Dict\]\): Keyword arguments to pass to the     

search function. Can include things like:     

k: Amount of documents to return \(Default: 4\) score\_threshold: Minimum relevance threshold

> for similarity\_score\_threshold

fetch\_k: Amount of documents to pass to MMR algorithm     

\(Default: 20\)

lambda\_mult: Diversity of results returned by MMR;     

1 for minimum diversity and 0 for maximum. \(Default: 0.5\)

filter: Filter by document metadata

Returns:     

Retriever class for VectorStore.

Return type:     

[VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")

Examples:               # Retrieve more documents with higher diversity     # Useful if your dataset has many similar documents     docsearch.as_retriever(         search_type="mmr",         search_kwargs={'k': 6, 'lambda_mult': 0.25}     )          # Fetch more documents for the MMR algorithm to consider     # But only return the top 5     docsearch.as_retriever(         search_type="mmr",         search_kwargs={'k': 5, 'fetch_k': 50}     )          # Only retrieve documents that have a relevance score     # Above a certain threshold     docsearch.as_retriever(         search_type="similarity_score_threshold",         search_kwargs={'score_threshold': 0.8}     )          # Only get the single most similar document from the dataset     docsearch.as_retriever(search_kwargs={'k': 1})          # Use a filter to only retrieve documents from a specific paper     docsearch.as_retriever(         search_kwargs={'filter': {'paper_title':'GPT-4 Technical Report'}}     )     

_async _asearch\(

    _query : str_,     _search\_type : str_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async return docs most similar to query using a specified search type.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **search\_type** \(_str_\) – Type of search to perform. Can be “similarity”, “mmr”, or “similarity\_score\_threshold”.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query.

Raises:     

**ValueError** – If search\_type is not one of “similarity”, “mmr”, or “similarity\_score\_threshold”.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query vector.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_with\_relevance\_scores\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Async return docs and relevance scores in the range \[0, 1\].

0 is dissimilar, 1 is most similar.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – 

kwargs to be passed to similarity search. Should include: score\_threshold: Optional, a floating point value between 0 to 1 to

> filter the resulting set of retrieved docs

Returns:     

List of Tuples of \(doc, similarity\_score\)

Return type:     

list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Async run similarity search with distance.

Parameters:     

  * **\*args** \(_Any_\) – Arguments to pass to the search method.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

close\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.close)\#     

Return type:     

None

_static _connect\_to\_elasticsearch\(

    _\*_ ,     _es\_url : str | None = None_,     _cloud\_id : str | None = None_,     _api\_key : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _es\_params : Dict\[str, Any\] | None = None_, \) → Elasticsearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.connect_to_elasticsearch)\#     

Parameters:     

  * **es\_url** \(_str_ _|__None_\)

  * **cloud\_id** \(_str_ _|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

_Elasticsearch_

delete\(

    _ids : List\[str\] | None = None_,     _refresh\_indices : bool | None = True_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.delete)\#     

Delete documents from the Elasticsearch index.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids of documents to delete.

  * **refresh\_indices** \(_bool_ _|__None_\) – Whether to refresh the index after deleting documents. Defaults to True.

  * **kwargs** \(_Any_\)

Return type:     

bool | None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _bulk\_kwargs : Dict | None = None_,     _\*\* kwargs: Any_, \) → ElasticsearchStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.from_documents)\#     

Construct ElasticsearchStore wrapper from documents.

Example               from langchain_elasticsearch.vectorstores import ElasticsearchStore     from langchain_openai import OpenAIEmbeddings          db = ElasticsearchStore.from_documents(         texts,         embeddings,         index_name="langchain-demo",         es_url="http://localhost:9200"     )     

Parameters:     

  * **texts** – List of texts to add to the Elasticsearch index.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – Embedding function to use to embed the texts. Do not provide if using a strategy that doesn’t require inference.

  * **metadatas** – Optional list of metadatas associated with the texts.

  * **index\_name** – Name of the Elasticsearch index to create.

  * **es\_url** – URL of the Elasticsearch instance to connect to.

  * **cloud\_id** – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** – Username to use when connecting to Elasticsearch.

  * **es\_password** – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** – API key to use when connecting to Elasticsearch.

  * **es\_connection** – Optional pre-existing Elasticsearch connection.

  * **vector\_query\_field** – Optional. Name of the field to store the embedding vectors in.

  * **query\_field** – Optional. Name of the field to store the texts in.

  * **bulk\_kwargs** \(_Dict_ _|__None_\) – Optional. Additional arguments to pass to Elasticsearch bulk.

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_ElasticsearchStore_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : List\[Dict\[str, Any\]\] | None = None_,     _bulk\_kwargs : Dict | None = None_,     _\*\* kwargs: Any_, \) → ElasticsearchStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.from_texts)\#     

Construct ElasticsearchStore wrapper from raw documents.

Example               from langchain_elasticsearch.vectorstores import ElasticsearchStore     from langchain_openai import OpenAIEmbeddings          db = ElasticsearchStore.from_texts(         texts,         // embeddings optional if using         // a strategy that doesn't require inference         embeddings,         index_name="langchain-demo",         es_url="http://localhost:9200"     )     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to add to the Elasticsearch index.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – Embedding function to use to embed the texts.

  * **metadatas** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **index\_name** – Name of the Elasticsearch index to create.

  * **es\_url** – URL of the Elasticsearch instance to connect to.

  * **cloud\_id** – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** – Username to use when connecting to Elasticsearch.

  * **es\_password** – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** – API key to use when connecting to Elasticsearch.

  * **es\_connection** – Optional pre-existing Elasticsearch connection.

  * **vector\_query\_field** – Optional. Name of the field to store the embedding vectors in.

  * **query\_field** – Optional. Name of the field to store the texts in.

  * **distance\_strategy** – Optional. Name of the distance strategy to use. Defaults to “COSINE”. can be one of “COSINE”, “EUCLIDEAN\_DISTANCE”, “DOT\_PRODUCT”, “MAX\_INNER\_PRODUCT”.

  * **bulk\_kwargs** \(_Dict_ _|__None_\) – Optional. Additional arguments to pass to Elasticsearch bulk.

  * **kwargs** \(_Any_\)

Return type:     

_ElasticsearchStore_

get\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Get documents by their IDs.

The returned documents are expected to have the ID field set to the ID of the document in the vector store.

Fewer documents may be returned than requested if some IDs are not found or if there are duplicated IDs.

Users should not assume that the order of the returned documents matches the order of the input IDs. Instead, users should rely on the ID field of the returned documents.

This method should **NOT** raise exceptions if no documents are found for some IDs.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\) – List of ids to retrieve.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Added in version 0.2.11.

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _fields : List\[str\] | None = None_,     _\*_ ,     _custom\_query : Callable\[\[Dict\[str, Any\], str | None\], Dict\[str, Any\]\] | None = None_,     _doc\_builder : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **fields** \(_List_ _\[__str_ _\]__|__None_\) – Other fields to get from elasticsearch source. These fields will be added to the document metadata.

  * **custom\_query** \(_Callable_ _\[__\[__Dict_ _\[__str_ _,__Any_ _\]__,__str_ _|__None_ _\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\)

  * **doc\_builder** \(_Callable_ _\[__\[__Dict_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

A list of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Default is 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

search\(

    _query : str_,     _search\_type : str_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs most similar to query using a specified search type.

Parameters:     

  * **query** \(_str_\) – Input text

  * **search\_type** \(_str_\) – Type of search to perform. Can be “similarity”, “mmr”, or “similarity\_score\_threshold”.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query.

Raises:     

**ValueError** – If search\_type is not one of “similarity”, “mmr”, or “similarity\_score\_threshold”.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 50_,     _filter : List\[dict\] | None = None_,     _\*_ ,     _custom\_query : Callable\[\[Dict\[str, Any\], str | None\], Dict\[str, Any\]\] | None = None_,     _doc\_builder : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.similarity_search)\#     

Return Elasticsearch documents most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to knn num\_candidates.

  * **filter** \(_List_ _\[__dict_ _\]__|__None_\) – Array of Elasticsearch filter clauses to apply to the query.

  * **custom\_query** \(_Callable_ _\[__\[__Dict_ _\[__str_ _,__Any_ _\]__,__str_ _|__None_ _\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\)

  * **doc\_builder** \(_Callable_ _\[__\[__Dict_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query, in descending order of similarity.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query vector.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\_with\_relevance\_scores\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : List\[Dict\] | None = None_,     _\*_ ,     _custom\_query : Callable\[\[Dict\[str, Any\], str | None\], Dict\[str, Any\]\] | None = None_,     _doc\_builder : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.similarity_search_by_vector_with_relevance_scores)\#     

Return Elasticsearch documents most similar to query, along with scores.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_List_ _\[__Dict_ _\]__|__None_\) – Array of Elasticsearch filter clauses to apply to the query.

  * **custom\_query** \(_Callable_ _\[__\[__Dict_ _\[__str_ _,__Any_ _\]__,__str_ _|__None_ _\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\)

  * **doc\_builder** \(_Callable_ _\[__\[__Dict_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the embedding and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_relevance\_scores\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Return docs and relevance scores in the range \[0, 1\].

0 is dissimilar, 1 is most similar.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – 

kwargs to be passed to similarity search. Should include: score\_threshold: Optional, a floating point value between 0 to 1 to

> filter the resulting set of retrieved docs.

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _filter : List\[dict\] | None = None_,     _\*_ ,     _custom\_query : Callable\[\[Dict\[str, Any\], str | None\], Dict\[str, Any\]\] | None = None_,     _doc\_builder : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/vectorstores.html#ElasticsearchStore.similarity_search_with_score)\#     

Return Elasticsearch documents most similar to query, along with scores.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_List_ _\[__dict_ _\]__|__None_\) – Array of Elasticsearch filter clauses to apply to the query.

  * **custom\_query** \(_Callable_ _\[__\[__Dict_ _\[__str_ _,__Any_ _\]__,__str_ _|__None_ _\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\)

  * **doc\_builder** \(_Callable_ _\[__\[__Dict_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)