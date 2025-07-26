# Lantern — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.Lantern.html
**Word Count:** 2851
**Links Count:** 561
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# Lantern\#

_class _langchain\_community.vectorstores.lantern.Lantern\(

    _connection\_string : str_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy") = DistanceStrategy.COSINE_,     _collection\_name : str = 'langchain'_,     _collection\_metadata : dict | None = None_,     _pre\_delete\_collection : bool = False_,     _logger : Logger | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern)\#     

Postgres with the lantern extension as a vector store.

lantern uses sequential scan by default. but you can create a HNSW index using the create\_hnsw\_index method. \- connection\_string is a postgres connection string. \- embedding\_function any embedding function implementing

> langchain.embeddings.base.Embeddings interface.

  * collection\_name is the name of the collection to use. \(default: langchain\)          * NOTE: This is the name of the table in which embedding data will be stored     

The table will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * distance\_strategy is the distance strategy to use. \(default: EUCLIDEAN\)          * EUCLIDEAN is the euclidean distance.

    * COSINE is the cosine distance.

    * HAMMING is the hamming distance.

  * pre\_delete\_collection if True, will delete the collection if it exists.     

\(default: False\) \- Useful for testing.

Attributes

`distance_function` |    ---|---   `distance_strategy` |    `embeddings` | Access the query embedding object if available.      Methods

`__init__`\(connection\_string, embedding\_function\) |    ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(texts, embeddings, metadatas, ...\) |    `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `connect`\(\) |    `connection_string_from_db_params`\(driver, ...\) | Return connection string from database parameters.   `create_collection`\(\) |    `create_hnsw_extension`\(\) |    `create_hnsw_index`\(\[dims, m, ...\]\) | Create HNSW index on collection.   `create_tables_if_not_exists`\(\) |    `delete`\(\[ids\]\) | Delete vectors by ids or uuids.   `delete_collection`\(\) |    `drop_index`\(\) |    `drop_table`\(\) |    `drop_tables`\(\) |    `from_documents`\(documents, embedding\[, ...\]\) | Initialize a vector store with a set of documents.   `from_embeddings`\(text\_embeddings, embedding\) | Construct Lantern wrapper from raw documents and pre- generated embeddings.   `from_existing_index`\(embedding\[, ...\]\) | Get instance of an existing Lantern store.This method will return the instance of the store without inserting any new embeddings   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Initialize Lantern vectorstore from list of texts.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance   `max_marginal_relevance_search_with_score`\(query\) | Return docs selected using the maximal marginal relevance with score.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance with score   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, filter\]\) | Run similarity search with distance.   `similarity_search_with_score_by_vector`\(embedding\) |       Parameters:     

  * **connection\_string** \(_str_\)

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy")\)

  * **collection\_name** \(_str_\)

  * **collection\_metadata** \(_Optional_ _\[__dict_ _\]_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **logger** \(_Optional_ _\[__logging.Logger_ _\]_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

\_\_init\_\_\(

    _connection\_string : str_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy") = DistanceStrategy.COSINE_,     _collection\_name : str = 'langchain'_,     _collection\_metadata : dict | None = None_,     _pre\_delete\_collection : bool = False_,     _logger : Logger | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.__init__)\#     

Parameters:     

  * **connection\_string** \(_str_\)

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy")\)

  * **collection\_name** \(_str_\)

  * **collection\_metadata** \(_dict_ _|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **logger** \(_Logger_ _|__None_\)

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\)

Return type:     

None

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

    _texts : List\[str\]_,     _embeddings : List\[List\[float\]\]_,     _metadatas : List\[dict\]_,     _ids : List\[str\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.add_embeddings)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]_\)

  * **ids** \(_List_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

None

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of IDs associated with the texts.

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters. One of the kwargs should be ids which is a list of ids associated with the texts.

Returns:     

List of ids from adding the texts into the vectorstore.

Raises:     

  * **ValueError** – If the number of metadatas does not match the number of texts.

  * **ValueError** – If the number of ids does not match the number of texts.

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

_async _aget\_by\_ids\(_ids : Sequence\[str\]_, _/_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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

connect\(\) → Connection[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.connect)\#     

Return type:     

_Connection_

_classmethod _connection\_string\_from\_db\_params\(

    _driver : str_,     _host : str_,     _port : int_,     _database : str_,     _user : str_,     _password : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.connection_string_from_db_params)\#     

Return connection string from database parameters.

Parameters:     

  * **driver** \(_str_\)

  * **host** \(_str_\)

  * **port** \(_int_\)

  * **database** \(_str_\)

  * **user** \(_str_\)

  * **password** \(_str_\)

Return type:     

str

create\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.create_collection)\#     

Return type:     

None

create\_hnsw\_extension\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.create_hnsw_extension)\#     

Return type:     

None

create\_hnsw\_index\(

    _dims : int = 1536_,     _m : int = 16_,     _ef\_construction : int = 64_,     _ef\_search : int = 64_,     _\*\* \_kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.create_hnsw_index)\#     

Create HNSW index on collection.

Optional Keyword Args for HNSW Index:     

engine: “nmslib”, “faiss”, “lucene”; default: “nmslib”

ef: Size of the dynamic list used during k-NN searches. Higher values lead to more accurate but slower searches; default: 64

ef\_construction: Size of the dynamic list used during k-NN graph creation. Higher values lead to more accurate graph but slower indexing speed; default: 64

m: Number of bidirectional links created for each new element. Large impact on memory consumption. Between 2 and 100; default: 16

dims: Dimensions of the vectors in collection. default: 1536

Parameters:     

  * **dims** \(_int_\)

  * **m** \(_int_\)

  * **ef\_construction** \(_int_\)

  * **ef\_search** \(_int_\)

  * **\_kwargs** \(_Any_\)

Return type:     

None

create\_tables\_if\_not\_exists\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.create_tables_if_not_exists)\#     

Return type:     

None

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.delete)\#     

Delete vectors by ids or uuids.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\)

Return type:     

None

delete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.delete_collection)\#     

Return type:     

None

drop\_index\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.drop_index)\#     

Return type:     

None

drop\_table\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.drop_table)\#     

Return type:     

None

drop\_tables\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.drop_tables)\#     

Return type:     

None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*\* kwargs: Any_, \) → Lantern[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.from_documents)\#     

Initialize a vector store with a set of documents.

Postgres connection string is required “Either pass it as connection\_string parameter or set the LANTERN\_CONNECTION\_STRING environment variable.

  * connection\_string is a postgres connection string.

  * documents is list of `Document` to initialize the vector store with

  * embedding is `Embeddings` that will be used for     

embedding the text sent. If none is sent, then the multilingual Tensorflow Universal Sentence Encoder will be used.

  * collection\_name is the name of the collection to use. \(default: langchain\)          * NOTE: This is the name of the table in which embedding data will be stored     

The table will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * distance\_strategy is the distance strategy to use. \(default: EUCLIDEAN\)          * EUCLIDEAN is the euclidean distance.

    * COSINE is the cosine distance.

    * HAMMING is the hamming distance.

  * ids row ids to insert into collection.

  * pre\_delete\_collection if True, will delete the collection if it exists.     

\(default: False\) \- Useful for testing.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_Lantern_

_classmethod _from\_embeddings\(

    _text\_embeddings : List\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'langchain'_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy") = DistanceStrategy.COSINE_,     _\*\* kwargs: Any_, \) → Lantern[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.from_embeddings)\#     

Construct Lantern wrapper from raw documents and pre- generated embeddings.

Postgres connection string is required “Either pass it as connection\_string parameter or set the LANTERN\_CONNECTION\_STRING environment variable.

Order of elements for lists ids, text\_embeddings, metadatas should match, so each row will be associated with correct values.

  * connection\_string is fully populated connection string for postgres database

  * text\_embeddings is array with tuples \(text, embedding\)     

to insert into collection.

  * embedding is `Embeddings` that will be used for     

embedding the text sent. If none is sent, then the multilingual Tensorflow Universal Sentence Encoder will be used.

  * metadatas row metadata to insert into collection.

  * collection\_name is the name of the collection to use. \(default: langchain\)          * NOTE: This is the name of the table in which embedding data will be stored     

The table will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * ids row ids to insert into collection.

  * pre\_delete\_collection if True, will delete the collection if it exists.     

\(default: False\) \- Useful for testing.

  * distance\_strategy is the distance strategy to use. \(default: EUCLIDEAN\)          * EUCLIDEAN is the euclidean distance.

    * COSINE is the cosine distance.

    * HAMMING is the hamming distance.

Parameters:     

  * **text\_embeddings** \(_List_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy")\)

  * **kwargs** \(_Any_\)

Return type:     

_Lantern_

_classmethod _from\_existing\_index\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'langchain'_,     _pre\_delete\_collection : bool = False_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy") = DistanceStrategy.COSINE_,     _\*\* kwargs: Any_, \) → Lantern[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.from_existing_index)\#     

Get instance of an existing Lantern store.This method will return the instance of the store without inserting any new embeddings

Postgres connection string is required “Either pass it as connection\_string parameter or set the LANTERN\_CONNECTION\_STRING environment variable.

  * connection\_string is a postgres connection string.

  * embedding is `Embeddings` that will be used for     

embedding the text sent. If none is sent, then the multilingual Tensorflow Universal Sentence Encoder will be used.

  * collection\_name is the name of the collection to use. \(default: langchain\)          * NOTE: This is the name of the table in which embedding data will be stored     

The table will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * ids row ids to insert into collection.

  * pre\_delete\_collection if True, will delete the collection if it exists.     

\(default: False\) \- Useful for testing.

  * distance\_strategy is the distance strategy to use. \(default: EUCLIDEAN\)          * EUCLIDEAN is the euclidean distance.

    * COSINE is the cosine distance.

    * HAMMING is the hamming distance.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy")\)

  * **kwargs** \(_Any_\)

Return type:     

_Lantern_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*\* kwargs: Any_, \) → Lantern[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.from_texts)\#     

Initialize Lantern vectorstore from list of texts. The embeddings will be generated using embedding class provided.

Order of elements for lists ids, texts, metadatas should match, so each row will be associated with correct values.

Postgres connection string is required “Either pass it as connection\_string parameter or set the LANTERN\_CONNECTION\_STRING environment variable.

  * connection\_string is fully populated connection string for postgres database

  * texts texts to insert into collection.

  * embedding is `Embeddings` that will be used for     

embedding the text sent. If none is sent, then the multilingual Tensorflow Universal Sentence Encoder will be used.

  * metadatas row metadata to insert into collection.

  * collection\_name is the name of the collection to use. \(default: langchain\)          * NOTE: This is the name of the table in which embedding data will be stored     

The table will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * distance\_strategy is the distance strategy to use. \(default: EUCLIDEAN\)          * EUCLIDEAN is the euclidean distance.

    * COSINE is the cosine distance.

    * HAMMING is the hamming distance.

  * ids row ids to insert into collection.

  * pre\_delete\_collection if True, will delete the collection if it exists.     

\(default: False\) \- Useful for testing.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.lantern.DistanceStrategy.html#langchain_community.vectorstores.lantern.DistanceStrategy "langchain_community.vectorstores.lantern.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_Lantern_

get\_by\_ids\(_ids : Sequence\[str\]_, _/_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance     

to embedding vector.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **embedding** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.max_marginal_relevance_search_with_score)\#     

Return docs selected using the maximal marginal relevance with score.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal     

relevance to the query and score for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.max_marginal_relevance_search_with_score_by_vector)\#     

Return docs selected using the maximal marginal relevance with score     

to embedding vector.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal     

relevance to the query and score for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents most similar to the query vector.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.similarity_search_with_score)\#     

Run similarity search with distance.

Parameters:     

  * **\*args** – Arguments to pass to the search method.

  * **\*\*kwargs** – Arguments to pass to the search method.

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/lantern.html#Lantern.similarity_search_with_score_by_vector)\#     

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using Lantern

  * [Lantern](https://python.langchain.com/docs/integrations/vectorstores/lantern/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)