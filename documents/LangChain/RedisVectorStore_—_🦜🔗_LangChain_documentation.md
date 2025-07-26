# RedisVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/vectorstores/langchain_redis.vectorstores.RedisVectorStore.html
**Word Count:** 3030
**Links Count:** 252
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# RedisVectorStore\#

_class _langchain\_redis.vectorstores.RedisVectorStore\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _config : [RedisConfig](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") | None = None_,     _ttl : int | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore)\#     

Redis vector store integration.

Setup:     

Install `langchain-redis` and running the Redis docker container.               pip install -qU langchain-redis     docker run -p 6379:6379 redis/redis-stack-server:latest     

Key init args — indexing params:     

index\_name: str     

Name of the index to create.

embedding: Embeddings     

Embedding function to use.

distance\_metric: str     

Distance metric to use for similarity search. Default is “COSINE”.

indexing\_algorithm: str     

Indexing algorithm to use. Default is “FLAT”.

vector\_datatype: str     

Data type of the vector. Default is “FLOAT32”.

Key init args — client params:     

redis\_url: Optional\[str\]     

URL of the Redis instance to connect to.

redis\_client: Optional\[Redis\]     

Pre-existing Redis connection.

ttl: Optional\[int\]     

Time-to-live for the Redis keys.

Instantiate:                    from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings          vector_store = RedisVectorStore(         index_name="langchain-demo",         embedding=OpenAIEmbeddings(),         redis_url="redis://localhost:6379",     )     

You can also connect to an existing Redis instance by passing in a pre-existing Redis connection via the redis\_client argument.

Instantiate from existing connection:                    from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings     from redis import Redis          redis_client = Redis.from_url("redis://localhost:6379")          store = RedisVectorStore(         embedding=OpenAIEmbeddings(),         index_name="langchain-demo",         redis_client=redis_client     )     

Add Documents:                    from langchain_core.documents import Document          document_1 = Document(page_content="foo", metadata={"baz": "bar"})     document_2 = Document(page_content="bar", metadata={"foo": "baz"})     document_3 = Document(page_content="to be deleted")          documents = [document_1, document_2, document_3]     ids = ["1", "2", "3"]     vector_store.add_documents(documents=documents, ids=ids)     

Delete Documents:                    vector_store.delete(ids=["3"])     

Search:                    results = vector_store.similarity_search(query="foo", k=1)     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * foo [{'baz': 'bar'}]     

Search with filter:                    from redisvl.query.filter import Tag          results = vector_store.similarity_search(         query="foo",         k=1,         filter=Tag("baz") == "bar"     )     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * foo [{'baz': 'bar'}]     

Search with score:                    results = vector_store.similarity_search_with_score(query="foo", k=1)     for doc, score in results:         print(f"* [SIM={score:.3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.916] foo [{'baz': 'bar'}]     

Use as Retriever:                    retriever = vector_store.as_retriever(         search_type="mmr",         search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},     )     retriever.get_relevant_documents("foo")                    [Document(page_content='foo', metadata={'baz': 'bar'})]     

Initialize the RedisVectorStore.

Parameters:     

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – The Embeddings instance used for this store.

  * **config** \(_Optional_ _\[_[_RedisConfig_](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") _\]_\) – Optional RedisConfig object. If not provided, a new one will be created from kwargs.

  * **ttl** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for Redis keys.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments for RedisConfig if config is not provided.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---   `index` |    `key_prefix` |       Methods

`__init__`\(embeddings\[, config, ttl\]\) | Initialize the RedisVectorStore.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, keys\]\) | Add text documents to the vector store.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `convert_vector`\(obj\) |    `delete`\(\[ids\]\) | Delete ids from the vector store.   `from_documents`\(documents, embedding\[, ...\]\) | Create a RedisVectorStore from a list of Documents.   `from_existing_index`\(index\_name, embedding, ...\) | Create a RedisVectorStore from an existing Redis Search Index.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a RedisVectorStore from a list of texts.   `get_by_ids`\(ids\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, sort\_by\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return documents most similar to query string, along with scores.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector.      \_\_init\_\_\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _config : [RedisConfig](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") | None = None_,     _ttl : int | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.__init__)\#     

Initialize the RedisVectorStore.

Parameters:     

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – The Embeddings instance used for this store.

  * **config** \([_RedisConfig_](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") _|__None_\) – Optional RedisConfig object. If not provided, a new one will be created from kwargs.

  * **ttl** \(_int_ _|__None_\) – Optional time-to-live for Redis keys.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments for RedisConfig if config is not provided.

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

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[Dict\[str, Any\]\] | None = None_,     _keys : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.add_texts)\#     

Add text documents to the vector store.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vector store.

  * **metadatas** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional list of metadata dicts associated with the texts.

  * **keys** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of keys to associate with the documents.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments: \- ids: Optional list of ids to associate with the documents. \- refresh\_indices: Whether to refresh the Redis indices after adding the texts. Defaults to True. \- create\_index\_if\_not\_exists: Whether to create the Redis index if it doesn’t already exist. Defaults to True. \- batch\_size: Optional. Number of texts to add to the index at a time. Defaults to 1000.

Returns:     

List of ids from adding the texts into the vector store.

Return type:     

_List_\[str\]

Example               from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings          vector_store = RedisVectorStore(         index_name="langchain-demo",         embedding=OpenAIEmbeddings(),         redis_url="redis://localhost:6379",     )          texts = [         "The quick brown fox jumps over the lazy dog",         "Hello world",         "Machine learning is fascinating"     ]     metadatas = [         {"source": "book", "page": 1},         {"source": "greeting", "language": "english"},         {"source": "article", "topic": "AI"}     ]          ids = vector_store.add_texts(         texts=texts,         metadatas=metadatas,         batch_size=2     )          print(f"Added documents with ids: {ids}")     

Note

  * If metadatas is provided, it must have the same length as texts.

  * If keys is provided, it must have the same length as texts.

  * The batch\_size parameter can be used to control the number of

documents added in each batch, which can be useful for managing memory usage when adding a large number of documents.

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

convert\_vector\(

    _obj : dict_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.convert_vector)\#     

Parameters:     

**obj** \(_dict_\)

Return type:     

_List_\[float\]

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.delete)\#     

Delete ids from the vector store.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids of the documents to delete.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments \(not used in the current implementation\).

Returns:     

True if one or more keys are deleted, False otherwise

Return type:     

Optional\[bool\]

Example               from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings          vector_store = RedisVectorStore(         index_name="langchain-demo",         embedding=OpenAIEmbeddings(),         redis_url="redis://localhost:6379",     )          # Assuming documents with these ids exist in the store     ids_to_delete = ["doc1", "doc2", "doc3"]          result = vector_store.delete(ids=ids_to_delete)     if result:       print("Documents were succesfully deleted")     else:       print("No Documents were deleted")     

Note

  * If ids is None or an empty list, the method returns False.

  * If the number of actually deleted keys differs from the number of keys submitted for deletion the method returns False

  * The method uses the drop\_keys functionality from RedisVL to delete the keys from Redis.

  * Keys are constructed by prefixing each id with the key\_prefix specified in the configuration.

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _config : [RedisConfig](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") | None = None_,     _return\_keys : bool = False_,     _\*\* kwargs: Any_, \) → RedisVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.from_documents)\#     

Create a RedisVectorStore from a list of Documents.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of Document objects to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embeddings object to use for encoding the documents.

  * **config** \([_RedisConfig_](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") _|__None_\) – Optional RedisConfig object. If not provided, one will be created from kwargs.

  * **return\_keys** \(_bool_\) – Whether to return the keys of the added documents.

  * **\*\*kwargs** \(_Any_\) – 

Additional keyword arguments to pass to RedisConfig if config     

is not provided.

Common kwargs include: \- index\_name: Name of the Redis index to create. \- redis\_url: URL of the Redis instance to connect to. \- distance\_metric: Distance metric to use for similarity search.

> Default is “COSINE”.

    * indexing\_algorithm: Indexing algorithm to use. Default is “FLAT”.

Returns:     

A new RedisVectorStore instance with the documents added.

Return type:     

RedisVectorStore

Example               from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings     from langchain_core.documents import Document          documents = [         Document(           page_content="The quick brown fox",           metadata={"animal": "fox"}         ),         Document(           page_content="jumps over the lazy dog",           metadata={"animal": "dog"}         )     ]          embeddings = OpenAIEmbeddings()          vector_store = RedisVectorStore.from_documents(         documents=documents,         embedding=embeddings,         index_name="animal-docs",         redis_url="redis://localhost:6379"     )          # Now you can use the vector_store for similarity search     results = vector_store.similarity_search("quick animal", k=1)     print(results[0].page_content)     

Note

  * This method creates a new RedisVectorStore instance and adds the provided documents to it.

  * The method extracts the text content and metadata from each Document object.

  * If a RedisConfig object is not provided, one will be created using the additional kwargs passed to this method.

  * The embedding function is used to convert the document text into vector representations for efficient similarity search.

_classmethod _from\_existing\_index\(

    _index\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*\* kwargs: Any_, \) → RedisVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.from_existing_index)\#     

Create a RedisVectorStore from an existing Redis Search Index.

This method allows you to connect to an already existing index in Redis, which can be useful for continuing work with previously created indexes or for connecting to indexes created outside of this client.

Parameters:     

  * **index\_name** \(_str_\) – Name of the existing index to use.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use for encoding queries.

  * **\*\*kwargs** \(_Any_\) – 

Additional keyword arguments to pass to RedisConfig. Common kwargs include: \- redis\_url: URL of the Redis instance to connect to. \- redis\_client: Pre-existing Redis client to use. \- vector\_query\_field: Name of the field containing the vector

> representations.

    * content\_field: Name of the field containing the document content.

Returns:     

A new RedisVectorStore instance connected to the     

existing index.

Return type:     

RedisVectorStore

Example               from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings     from redis import Redis          embeddings = OpenAIEmbeddings()          # Connect to an existing index     vector_store = RedisVectorStore.from_existing_index(         index_name="my-existing-index",         embedding=embeddings,         redis_url="redis://localhost:6379",         vector_query_field="embedding",         content_field="text"     )          # Now you can use the vector_store for similarity search     results = vector_store.similarity_search("AI and machine learning", k=1)     print(results[0].page_content)     

Note

  * This method assumes that the index already exists in Redis.

  * The embedding function provided should be compatible with the embeddings

stored in the existing index. \- If you’re using custom field names for vectors or content in your

> existing index, make sure to specify them using vector\_query\_field and content\_field respectively.

  * This method is useful for scenarios where you want to reuse an     

existing index, such as when the index was created by another process or when you want to use the same index across different sessions or applications.

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[Dict\[str, Any\]\] | None = None_,     _config : [RedisConfig](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") | None = None_,     _keys : List\[str\] | None = None_,     _return\_keys : bool = False_,     _\*\* kwargs: Any_, \) → RedisVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.from_texts)\#     

Create a RedisVectorStore from a list of texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use for encoding the texts.

  * **metadatas** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional list of metadata dicts associated with the texts.

  * **config** \([_RedisConfig_](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") _|__None_\) – Optional RedisConfig object. If not provided, one will be created from kwargs.

  * **keys** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of keys to associate with the documents.

  * **return\_keys** \(_bool_\) – Whether to return the keys of the added documents.

  * **\*\*kwargs** \(_Any_\) – 

Additional keyword arguments to pass to RedisConfig if config is not provided. Commonly used kwargs include: \- index\_name: Name of the Redis index to create. \- redis\_url: URL of the Redis instance to connect to. \- distance\_metric: Distance metric to use for similarity search.

> Default is “COSINE”.

    * indexing\_algorithm: Indexing algorithm to use. Default is “FLAT”.

Returns:     

A new RedisVectorStore instance with the texts added.

Return type:     

RedisVectorStore

Example               from langchain_redis import RedisVectorStore     from langchain_openai import OpenAIEmbeddings          texts = [         "The quick brown fox jumps over the lazy dog",         "Hello world",         "Machine learning is fascinating"     ]     metadatas = [         {"source": "book", "page": 1},         {"source": "greeting", "language": "english"},         {"source": "article", "topic": "AI"}     ]          embeddings = OpenAIEmbeddings()          vector_store = RedisVectorStore.from_texts(         texts=texts,         embedding=embeddings,         metadatas=metadatas,         index_name="langchain-demo",         redis_url="redis://localhost:6379",         distance_metric="COSINE"     )          # Now you can use the vector_store for similarity search     results = vector_store.similarity_search("AI and machine learning", k=1)     print(results[0].page_content)     

Note

  * This method creates a new RedisVectorStore instance and adds the     

provided texts to it.

  * If metadatas is provided, it must have the same length as texts.

  * If keys is provided, it must have the same length as texts.

  * The return\_keys parameter determines whether the method returns just the

RedisVectorStore instance or a tuple of \(RedisVectorStore, List\[str\]\) where the second element is the list of keys for the added documents.

get\_by\_ids\(

    _ids : Sequence\[str\]_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.get_by_ids)\#     

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

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Added in version 0.1.2.

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments to pass to the search function.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments to pass to the search function.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _filter : FilterExpression | None = None_,     _sort\_by : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_FilterExpression_ _|__None_\) – Optional filter expression to apply.

  * **sort\_by** \(_str_ _|__None_\) – Optional sort\_by expression to apply.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments to pass to the search function.

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : FilterExpression | None = None_,     _sort\_by : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_FilterExpression_ _|__None_\) – Optional filter expression to apply.

  * **sort\_by** \(_str_ _|__None_\) – Optional sort\_by expression to apply.

  * **\*\*kwargs** \(_Any_\) – 

Other keyword arguments: \- return\_metadata: Whether to return metadata. Defaults to True. \- distance\_threshold: Optional distance threshold for filtering results. \- return\_all: Whether to return all data in the Hash/JSON including

> non-indexed fields

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

    _query : str_,     _k : int = 4_,     _filter : FilterExpression | None = None_,     _sort\_by : str | None = None_,     _\*\* kwargs: Any_, \) → Sequence\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.similarity_search_with_score)\#     

Return documents most similar to query string, along with scores.

> Args: >      >  > query: Text to look up documents similar to. k: Number of Documents to return. Defaults to 4. filter: Optional filter expression to apply to the query. sort\_by: Optional sort\_by expression to apply to the query. \*\*kwargs: Other keyword arguments to pass to the search function: >
>>   * custom\_query: Optional callable that can be used >>      >>  >> to customize the query. >>  >>   * doc\_builder: Optional callable to customize Document creation. >>  >>   * return\_metadata: Whether to return metadata. Defaults to True. >>  >>   * distance\_threshold: Optional distance threshold for filtering results. >>  >>   * return\_all: Whether to return all data in the Hash/JSON including >>  >> 

>>  >> non-indexed fields. Defaults to False. >  > Returns: >      >  > List of tuples of \(Document, score\) most similar to the query. >  > Example: >      >      >      >     from langchain_redis import RedisVectorStore >     from langchain_openai import OpenAIEmbeddings >      >     vector_store = RedisVectorStore( >         index_name="langchain-demo", >         embedding=OpenAIEmbeddings(), >         redis_url="redis://localhost:6379", >     ) >      >     results = vector_store.similarity_search_with_score( >         "What is machine learning?", >         k=2, >         filter=None >     ) >      >     for doc, score in results: >         print(f"Score: {score}") >         print(f"Content: {doc.page_content}") >         print(f"Metadata: {doc.metadata} >     

“\)

> Note: >      >  >   * The method returns scores along with documents. Lower scores indicate >  > 

>  > higher similarity. \- The actual search is performed using the vector representation of the >
>> query, which is why an embedding function must be provided during initialization. >  >   * The filter parameter allows for additional filtering of results based on metadata. >  >   * If return\_all is set to True, all fields stored in Redis will be returned, which may include non-indexed fields. >  > 

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **filter** \(_FilterExpression_ _|__None_\)

  * **sort\_by** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[_Any_\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : FilterExpression | None = None_,     _sort\_by : str | None = None_,     _\*\* kwargs: Any_, \) → Sequence\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/vectorstores.html#RedisVectorStore.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_FilterExpression_ _|__None_\) – Optional filter expression to apply.

  * **sort\_by** \(_str_ _|__None_\) – Optional sort\_by expression to apply.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments: with\_vectors: Whether to return document vectors. Defaults to False. return\_metadata: Whether to return metadata. Defaults to True. distance\_threshold: Optional distance threshold for filtering results.

Returns:     

List of tuples of Documents most similar to the query vector, score, and optionally the document vector.

Return type:     

_Sequence_\[_Any_\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)