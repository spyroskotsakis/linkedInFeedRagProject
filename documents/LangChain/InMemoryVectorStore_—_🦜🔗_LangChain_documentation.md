# InMemoryVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.base.InMemoryVectorStore.html
**Word Count:** 3212
**Links Count:** 310
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# InMemoryVectorStore\#

_class _langchain\_aws.vectorstores.inmemorydb.base.InMemoryVectorStore\(

    _redis\_url : str_,     _index\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index\_schema : Dict\[str, List\[Dict\[str, str\]\]\] | str | PathLike | None = None_,     _vector\_schema : Dict\[str, str | int\] | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _key\_prefix : str | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore)\#     

InMemoryVectorStore vector database.

To use, you should have the `redis` python package installed for AWS MemoryDB               

Once running, you can connect to the MemoryDB server with the following url schemas: \- redis://<host>:<port> \# simple connection \- redis://<username>:<password>@<host>:<port> \# connection with authentication \- rediss://<host>:<port> \# connection with SSL \- rediss://<username>:<password>@<host>:<port> \# connection with SSL and auth

Examples:

The following examples show various ways to use the Redis VectorStore with LangChain.

For all the following examples assume we have the following imports:               from langchain_aws.vectorstores import InMemoryVectorStore     

Initialize, create index, and load Documents                    from langchain_aws.vectorstores import InMemoryVectorStore          rds = InMemoryVectorStore.from_documents(         documents, # a list of Document objects from loaders or created         embeddings, # an Embeddings object         redis_url="redis://cluster_endpoint:6379",     )     

Initialize, create index, and load Documents with metadata                    rds = InMemoryVectorStore.from_texts(         texts, # a list of strings         metadata, # a list of metadata dicts         embeddings, # an Embeddings object         redis_url="redis://cluster_endpoint:6379",     )     

Initialize, create index, and load Documents with metadata and return keys

>  >     rds, keys = InMemoryVectorStore.from_texts_return_keys( >         texts, # a list of strings >         metadata, # a list of metadata dicts >         embeddings, # an Embeddings object >         redis_url="redis://cluster_endpoint:6379", >     ) >     

For use cases where the index needs to stay alive, you can initialize with an index name such that it’s easier to reference later

>  >     rds = InMemoryVectorStore.from_texts( >         texts, # a list of strings >         metadata, # a list of metadata dicts >         embeddings, # an Embeddings object >         index_name="my-index", >         redis_url="redis://cluster_endpoint:6379", >     ) >     

Initialize and connect to an existing index \(from above\)

>  >     # must pass in schema and key_prefix from another index >     existing_rds = InMemoryVectorStore.from_existing_index( >         embeddings, # an Embeddings object >         index_name="my-index", >         schema=rds.schema, # schema dumped from another index >         key_prefix=rds.key_prefix, # key prefix from another index >         redis_url="redis://cluster_endpoint:6379", >     ) >     

Advanced examples:

Custom vector schema can be supplied to change the way that MemoryDB creates the underlying vector schema. This is useful for production use cases where you want to optimize the vector schema for your use case. ex. using HNSW instead of FLAT \(knn\) which is the default

>  >     vector_schema = { >         "algorithm": "HNSW" >     } >      >     rds = InMemoryVectorStore.from_texts( >         texts, # a list of strings >         metadata, # a list of metadata dicts >         embeddings, # an Embeddings object >         vector_schema=vector_schema, >         redis_url="redis://cluster_endpoint:6379", >     ) >     

Custom index schema can be supplied to change the way that the metadata is indexed. This is useful for you would like to use the hybrid querying \(filtering\) capability of MemoryDB.

By default, this implementation will automatically generate the index schema according to the following rules:

>   * All strings are indexed as text fields >  >   * All numbers are indexed as numeric fields >  >   * All lists of strings are indexed as tag fields \(joined by >      >  > langchain\_aws.vectorstores.inmemorydb.constants.INMEMORYDB\_TAG\_SEPARATOR\) >  >   * All None values are not indexed but still stored in MemoryDB these are >      >  > not retrievable through the interface here, but the raw MemoryDB client can be used to retrieve them. >  >   * All other types are not indexed >  > 

To override these rules, you can pass in a custom index schema like the following

>  >     tag: >         - name: credit_score >     text: >         - name: user >         - name: job >     

Typically, the `credit_score` field would be a text field since it’s a string, however, we can override this behavior by specifying the field type as shown with the yaml config \(can also be a dictionary\) above and the code below.

>  >     rds = InMemoryVectorStore.from_texts( >         texts, # a list of strings >         metadata, # a list of metadata dicts >         embeddings, # an Embeddings object >         index_schema="path/to/index_schema.yaml", # can also be a dictionary >         redis_url="redis://cluster_endpoint:6379", >     ) >     

When connecting to an existing index where a custom schema has been applied, it’s important to pass in the same schema to the `from_existing_index` method. Otherwise, the schema for newly added samples will be incorrect and metadata will not be returned.

Initialize MemoryDB vector store with necessary components.

Attributes

`DEFAULT_VECTOR_SCHEMA` |    ---|---   `embeddings` | Access the query embedding object if available.   `schema` | Return the schema of the index.      Methods

`__init__`\(redis\_url, index\_name, embedding\[, ...\]\) | Initialize MemoryDB vector store with necessary components.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, embeddings, ...\]\) | Add more texts to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `delete`\(\[ids\]\) | Delete a InMemoryVectorStore entry.   `drop_index`\(index\_name, delete\_documents, ...\) | Drop a InMemoryVectorStore search index.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_existing_index`\(embedding, index\_name, ...\) | Connect to an existing InMemoryVectorStore index.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a InMemoryVectorStore vectorstore from a list of texts.   `from_texts_return_keys`\(texts, embedding\[, ...\]\) | Create a InMemoryVectorStore vectorstore from raw documents.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, ...\]\) | Run similarity search   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Run similarity search between a query vector and the indexed vectors.   `similarity_search_limit_score`\(query\[, k, ...\]\) |    `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Run similarity search with **vector distance**.   `write_schema`\(path\) | Write the schema to a yaml file.      Parameters:     

  * **redis\_url** \(_str_\)

  * **index\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **index\_schema** \(_Optional_ _\[__Union_ _\[__Dict_ _\[__str_ _,__ListOfDict_ _\]__,__str_ _,__os.PathLike_ _\]__\]_\)

  * **vector\_schema** \(_Optional_ _\[__Dict_ _\[__str_ _,__Union_ _\[__str_ _,__int_ _\]__\]__\]_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

  * **key\_prefix** \(_Optional_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _redis\_url : str_,     _index\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index\_schema : Dict\[str, List\[Dict\[str, str\]\]\] | str | PathLike | None = None_,     _vector\_schema : Dict\[str, str | int\] | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _key\_prefix : str | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.__init__)\#     

Initialize MemoryDB vector store with necessary components.

Parameters:     

  * **redis\_url** \(_str_\)

  * **index\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **index\_schema** \(_Dict_ _\[__str_ _,__List_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__\]__|__str_ _|__PathLike_ _|__None_\)

  * **vector\_schema** \(_Dict_ _\[__str_ _,__str_ _|__int_ _\]__|__None_\)

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\)

  * **key\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _embeddings : List\[List\[float\]\] | None = None_,     _batch\_size : int = 1000_,     _clean\_metadata : bool = True_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.add_texts)\#     

Add more texts to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings/text to add to the vectorstore.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – Optional list of metadatas. Defaults to None.

  * **embeddings** \(_Optional_ _\[__List_ _\[__List_ _\[__float_ _\]__\]__\]__,__optional_\) – Optional pre-generated embeddings. Defaults to None.

  * **keys** \(_List_ _\[__str_ _\]__\) or_ _ids_ _\(__List_ _\[__str_ _\]_\) – Identifiers of entries. Defaults to None.

  * **batch\_size** \(_int_ _,__optional_\) – Batch size to use for writes. Defaults to 1000.

  * **clean\_metadata** \(_bool_\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids added to the vectorstore

Return type:     

List\[str\]

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

    _\*\* kwargs: Any_, \) → [InMemoryVectorStoreRetriever](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.base.InMemoryVectorStoreRetriever.html#langchain_aws.vectorstores.inmemorydb.base.InMemoryVectorStoreRetriever "langchain_aws.vectorstores.inmemorydb.base.InMemoryVectorStoreRetriever")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.as_retriever)\#     

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

_static _delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.delete)\#     

Delete a InMemoryVectorStore entry.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids \(keys in redis\) to delete.

  * **redis\_url** – Redis connection url. This should be passed in the kwargs or set as an environment variable: redis\_url.

  * **kwargs** \(_Any_\)

Returns:     

Whether or not the deletions were successful.

Return type:     

bool

Raises:     

  * **ValueError** – If the redis python package is not installed.

  * **ValueError** – If the ids \(keys in redis\) are not provided

_static _drop\_index\(

    _index\_name : str_,     _delete\_documents : bool_,     _\*\* kwargs: Any_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.drop_index)\#     

Drop a InMemoryVectorStore search index.

Parameters:     

  * **index\_name** \(_str_\) – Name of the index to drop.

  * **delete\_documents** \(_bool_\) – Whether to drop the associated documents.

  * **kwargs** \(_Any_\)

Returns:     

Whether or not the drop was successful.

Return type:     

bool

_classmethod _from\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*\* kwargs: Any_, \) → Self\#     

Return VectorStore initialized from documents and embeddings.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

VectorStore initialized from documents and embeddings.

Return type:     

[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")

_classmethod _from\_existing\_index\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index\_name : str_,     _schema : Dict\[str, List\[Dict\[str, str\]\]\] | str | PathLike_,     _key\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → InMemoryVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.from_existing_index)\#     

Connect to an existing InMemoryVectorStore index.

Example               from langchain_aws.vectorstores import InMemoryVectorStore          embeddings = OpenAIEmbeddings()          # must pass in schema and key_prefix from another index     existing_rds = InMemoryVectorStore.from_existing_index(         embeddings,         index_name="my-index",         schema=rds.schema, # schema dumped from another index         key_prefix=rds.key_prefix, # key prefix from another index         redis_url="redis://username:password@cluster_endpoint:6379",     )     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding model class \(i.e. OpenAIEmbeddings\) for embedding queries.

  * **index\_name** \(_str_\) – Name of the index to connect to.

  * **schema** \(_Union_ _\[__Dict_ _\[__str_ _,__str_ _\]__,__str_ _,__os.PathLike_ _,__Dict_ _\[__str_ _,__ListOfDict_ _\]__\]_\) – Schema of the index and the vector schema. Can be a dict, or path to yaml file.

  * **key\_prefix** \(_Optional_ _\[__str_ _\]_\) – Prefix to use for all keys in

  * **associated** \(_InMemoryVectorStore_\) – with this index.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments to pass to the Redis client.

Returns:     

InMemoryVectorStore VectorStore instance.

Return type:     

InMemoryVectorStore

Raises:     

  * **ValueError** – If the index does not exist.

  * **ImportError** – If the redis python package is not installed.

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _index\_name : str | None = None_,     _index\_schema : Dict\[str, List\[Dict\[str, str\]\]\] | str | PathLike | None = None_,     _vector\_schema : Dict\[str, str | int\] | None = None_,     _\*\* kwargs: Any_, \) → InMemoryVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.from_texts)\#     

Create a InMemoryVectorStore vectorstore from a list of texts.

This is a user-friendly interface that:     

  1. Embeds documents.

  2. Creates a new InMemoryVectorStore index if it doesn’t already exist

  3. Adds the documents to the newly created InMemoryVectorStore index.

This method will generate schema based on the metadata passed in if the index\_schema is not defined. If the index\_schema is defined, it will compare against the generated schema and warn if there are differences. If you are purposefully defining the schema for the metadata, then you can ignore that warning.

To examine the schema options, initialize an instance of this class and print out the schema using the InMemoryVectorStore.schema\` property. This will include the content and content\_vector classes which are always present in the langchain schema.

Example               from langchain_aws.vectorstores import InMemoryVectorStore                     embeddings = OpenAIEmbeddings()     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding model class \(i.e. OpenAIEmbeddings\) for embedding queries.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – Optional list of metadata dicts to add to the vectorstore. Defaults to None.

  * **index\_name** \(_Optional_ _\[__str_ _\]__,__optional_\) – Optional name of the index to create or add to. Defaults to None.

  * **\(****Optional****\[****Union****\[****Dict****\[****str** \(_index\_schema_\) – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **ListOfDict****\]** – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **str** – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **os.PathLike****\]****\]** – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **index\_schema** \(_Dict_ _\[__str_ _,__List_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__\]__|__str_ _|__PathLike_ _|__None_\)

  * **vector\_schema** \(_Dict_ _\[__str_ _,__str_ _|__int_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_InMemoryVectorStore_

:paramoptional\):     

Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

Parameters:     

  * **vector\_schema** \(_Optional_ _\[__Dict_ _\[__str_ _,__Union_ _\[__str_ _,__int_ _\]__\]__\]__,__optional_\) – Optional vector schema to use. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments to pass to the

  * **client.** \(_InMemoryVectorStore_\)

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **index\_name** \(_str_ _|__None_\)

  * **index\_schema** \(_Dict_ _\[__str_ _,__List_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__\]__|__str_ _|__PathLike_ _|__None_\)

Returns:     

InMemoryVectorStore VectorStore instance.

Return type:     

InMemoryVectorStore

Raises:     

  * **ValueError** – If the number of metadatas does not match the number of texts.

  * **ImportError** – If the redis python package is not installed.

_classmethod _from\_texts\_return\_keys\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _index\_name : str | None = None_,     _index\_schema : Dict\[str, List\[Dict\[str, str\]\]\] | str | PathLike | None = None_,     _vector\_schema : Dict\[str, str | int\] | None = None_,     _\*\* kwargs: Any_, \) → Tuple\[InMemoryVectorStore, List\[str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.from_texts_return_keys)\#     

Create a InMemoryVectorStore vectorstore from raw documents.

This is a user-friendly interface that:     

  1. Embeds documents.

  2. Creates a new InMemoryVectorStore index if it doesn’t already exist

  3. Adds the documents to the newly created InMemoryVectorStore index.

  4. Returns the keys of the newly created documents once stored.

This method will generate schema based on the metadata passed in if the index\_schema is not defined. If the index\_schema is defined, it will compare against the generated schema and warn if there are differences. If you are purposefully defining the schema for the metadata, then you can ignore that warning.

To examine the schema options, initialize an instance of this class and print out the schema using the InMemoryVectorStore.schema\` property. This will include the content and content\_vector classes which are always present in the langchain schema.

Example               from langchain_aws.vectorstores import InMemoryVectorStore                     embeddings = OpenAIEmbeddings()     redis, keys = InMemoryVectorStore.from_texts_return_keys(         texts,         embeddings,         redis_url="redis://cluster_endpoint:6379"     )     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embeddings to use for the vectorstore.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – Optional list of metadata dicts to add to the vectorstore. Defaults to None.

  * **index\_name** \(_Optional_ _\[__str_ _\]__,__optional_\) – Optional name of the index to create or add to. Defaults to None.

  * **\(****Optional****\[****Union****\[****Dict****\[****str** \(_index\_schema_\) – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **ListOfDict****\]** – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **str** – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **os.PathLike****\]****\]** – optional\): Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

  * **index\_schema** \(_Dict_ _\[__str_ _,__List_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__\]__|__str_ _|__PathLike_ _|__None_\)

  * **vector\_schema** \(_Dict_ _\[__str_ _,__str_ _|__int_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Tuple_\[_InMemoryVectorStore_, _List_\[str\]\]

:paramoptional\):     

Optional fields to index within the metadata. Overrides generated schema. Defaults to None.

Parameters:     

  * **vector\_schema** \(_Optional_ _\[__Dict_ _\[__str_ _,__Union_ _\[__str_ _,__int_ _\]__\]__\]__,__optional_\) – Optional vector schema to use. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – 

Additional keyword arguments to pass to the Redis client.

Returns:

  * **Tuple****\[****InMemoryVectorStore**

  * **List****\[****str****\]****\]**

  * **of** \(_Tuple_ _of_ _the InMemoryVectorStore instance and the keys_\)

  * **documents.** \(_the newly created_\)

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **index\_name** \(_str_ _|__None_\)

  * **index\_schema** \(_Dict_ _\[__str_ _,__List_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__\]__|__str_ _|__PathLike_ _|__None_\)

Raises:     

**ValueError** – If the number of metadatas does not match the number of texts.

Return type:     

_Tuple_\[_InMemoryVectorStore_, _List_\[str\]\]

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : [InMemoryDBFilterExpression](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") | None = None_,     _return\_metadata : bool = True_,     _distance\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \([_InMemoryDBFilterExpression_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") _,__optional_\) – Optional metadata filter. Defaults to None.

  * **return\_metadata** \(_bool_ _,__optional_\) – Whether to return metadata. Defaults to True.

  * **distance\_threshold** \(_Optional_ _\[__float_ _\]__,__optional_\) – Maximum vector distance between selected documents and the query vector. Defaults to None.

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

    _query : str_,     _k : int = 4_,     _filter : [InMemoryDBFilterExpression](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") | None = None_,     _return\_metadata : bool = True_,     _distance\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.similarity_search)\#     

Run similarity search

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filter** \([_InMemoryDBFilterExpression_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") _,__optional_\) – Optional metadata filter. Defaults to None.

  * **return\_metadata** \(_bool_ _,__optional_\) – Whether to return metadata. Defaults to True.

  * **distance\_threshold** \(_Optional_ _\[__float_ _\]__,__optional_\) – Maximum vector distance between selected documents and the query vector. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query     

text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : [InMemoryDBFilterExpression](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") | None = None_,     _return\_metadata : bool = True_,     _distance\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.similarity_search_by_vector)\#     

Run similarity search between a query vector and the indexed vectors.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – The query vector for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filter** \([_InMemoryDBFilterExpression_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") _,__optional_\) – Optional metadata filter. Defaults to None.

  * **return\_metadata** \(_bool_ _,__optional_\) – Whether to return metadata. Defaults to True.

  * **distance\_threshold** \(_Optional_ _\[__float_ _\]__,__optional_\) – Maximum vector distance between selected documents and the query vector. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query     

text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_limit\_score\(

    _query : str_,     _k : int = 4_,     _score\_threshold : float = 0.2_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.similarity_search_limit_score)\#     

Deprecated since version 0.0.1: Use `1)()` instead.

Returns the most similar indexed documents to the query text within the score\_threshold range.

Deprecated: Use similarity\_search with distance\_threshold instead.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **score\_threshold** \(_float_\) – The minimum matching _distance_ required for a document to be considered a match. Defaults to 0.2.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text     

including the match score for each document.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Note

If there are no documents that satisfy the score\_threshold value, an empty list is returned.

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

    _query : str_,     _k : int = 4_,     _filter : [InMemoryDBFilterExpression](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") | None = None_,     _return\_metadata : bool = True_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.similarity_search_with_score)\#     

Run similarity search with **vector distance**.

The “scores” returned from this function are the raw vector distances from the query vector. For similarity scores, use `similarity_search_with_relevance_scores`.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filter** \([_InMemoryDBFilterExpression_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression") _,__optional_\) – Optional metadata filter. Defaults to None.

  * **return\_metadata** \(_bool_ _,__optional_\) – Whether to return metadata. Defaults to True.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are     

most similar to the query with the distance for each document.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

write\_schema\(

    _path : str | PathLike_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/base.html#InMemoryVectorStore.write_schema)\#     

Write the schema to a yaml file.

Parameters:     

**path** \(_str_ _|__PathLike_\)

Return type:     

None

Examples using InMemoryVectorStore

  * [AI21Embeddings](https://python.langchain.com/docs/integrations/text_embedding/ai21/)

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Amazon MemoryDB](https://python.langchain.com/docs/integrations/vectorstores/memorydb/)

  * [AzureOpenAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/azureopenai/)

  * [CohereEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/cohere/)

  * [FireworksEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/fireworks/)

  * [How to convert Runnables as Tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)

  * [MistralAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/mistralai/)

  * [NomicEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/nomic/)

  * [OllamaEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/ollama/)

  * [OpenAIEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/openai/)

  * [TogetherEmbeddings](https://python.langchain.com/docs/integrations/text_embedding/together/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)