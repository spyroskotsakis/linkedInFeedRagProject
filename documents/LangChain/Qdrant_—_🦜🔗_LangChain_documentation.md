# Qdrant — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.qdrant.Qdrant.html
**Word Count:** 5421
**Links Count:** 529
**Scraped:** 2025-07-21 08:08:35
**Status:** completed

---

# Qdrant\#

_class _langchain\_community.vectorstores.qdrant.Qdrant\(

    _client : Any_,     _collection\_name : str_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _distance\_strategy : str = 'COSINE'_,     _vector\_name : str | None = None_,     _async\_client : Any | None = None_,     _embedding\_function : Callable | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant)\#     

Deprecated since version 0.0.37: Use `:class:`~langchain_qdrant.Qdrant`` instead. It will not be removed until langchain-community==1.0.

Qdrant vector store.

To use you should have the `qdrant-client` package installed.

Example               from qdrant_client import QdrantClient     from langchain_community.vectorstores import Qdrant          client = QdrantClient()     collection_name = "MyCollection"     qdrant = Qdrant(client, collection_name, embedding_function)     

Initialize with necessary components.

Attributes

`CONTENT_KEY` |    ---|---   `METADATA_KEY` |    `VECTOR_NAME` |    `embeddings` | Access the query embedding object if available.      Methods

`__init__`\(client, collection\_name\[, ...\]\) | Initialize with necessary components.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, batch\_size\]\) | Run more texts through the embeddings and add to the vectorstore.   `aconstruct_instance`\(texts, embedding\[, ...\]\) |    `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids, batch\_size\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Construct Qdrant wrapper from a list of texts.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. Defaults to 20. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :param filter: Filter by metadata. Defaults to None. :param search\_params: Additional search params :param score\_threshold: Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned. :param consistency: Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: - int - number of replicas to query, values should present in all queried replicas - 'majority' - query all replicas, but return values present in the majority of replicas - 'quorum' - query the majority of replicas, return values present in all of them - 'all' - query all replicas, and return values present in all replicas :param \*\*kwargs: Any other named arguments to pass through to AsyncQdrantClient.Search\(\).   `amax_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. Defaults to 20. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter\]\) | Return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs most similar to embedding vector.   `construct_instance`\(texts, embedding\[, ...\]\) |    `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_existing_collection`\(embedding, path, ...\) | Get instance of an existing Qdrant collection.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Construct Qdrant wrapper from a list of texts.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. Defaults to 20. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :param filter: Filter by metadata. Defaults to None. :param search\_params: Additional search params :param score\_threshold: Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned. :param consistency: Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: - int - number of replicas to query, values should present in all queried replicas - 'majority' - query all replicas, but return values present in the majority of replicas - 'quorum' - query the majority of replicas, return values present in all of them - 'all' - query all replicas, and return values present in all replicas :param \*\*kwargs: Any other named arguments to pass through to QdrantClient.search\(\).   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, ...\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector.      Parameters:     

  * **client** \(_Any_\)

  * **collection\_name** \(_str_\)

  * **embeddings** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **distance\_strategy** \(_str_\)

  * **vector\_name** \(_Optional_ _\[__str_ _\]_\)

  * **async\_client** \(_Optional_ _\[__Any_ _\]_\)

  * **embedding\_function** \(_Optional_ _\[__Callable_ _\]_\)

\_\_init\_\_\(

    _client : Any_,     _collection\_name : str_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _distance\_strategy : str = 'COSINE'_,     _vector\_name : str | None = None_,     _async\_client : Any | None = None_,     _embedding\_function : Callable | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.__init__)\#     

Initialize with necessary components.

Parameters:     

  * **client** \(_Any_\)

  * **collection\_name** \(_str_\)

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **distance\_strategy** \(_str_\)

  * **vector\_name** \(_str_ _|__None_\)

  * **async\_client** \(_Any_ _|__None_\)

  * **embedding\_function** \(_Callable_ _|__None_\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : Sequence\[str\] | None = None_,     _batch\_size : int = 64_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.aadd_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_Sequence_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts. Ids have to be uuid-like strings.

  * **batch\_size** \(_int_\) – How many vectors upload per-request. Default: 64

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async classmethod _aconstruct\_instance\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : float | None = None_,     _host : str | None = None_,     _path : str | None = None_,     _collection\_name : str | None = None_,     _distance\_func : str = 'Cosine'_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str | None = None_,     _shard\_number : int | None = None_,     _replication\_factor : int | None = None_,     _write\_consistency\_factor : int | None = None_,     _on\_disk\_payload : bool | None = None_,     _hnsw\_config : common\_types.HnswConfigDiff | None = None_,     _optimizers\_config : common\_types.OptimizersConfigDiff | None = None_,     _wal\_config : common\_types.WalConfigDiff | None = None_,     _quantization\_config : common\_types.QuantizationConfig | None = None_,     _init\_from : common\_types.InitFrom | None = None_,     _on\_disk : bool | None = None_,     _force\_recreate : bool = False_,     _\*\* kwargs: Any_, \) → Qdrant[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.aconstruct_instance)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **location** \(_Optional_ _\[__str_ _\]_\)

  * **url** \(_Optional_ _\[__str_ _\]_\)

  * **port** \(_Optional_ _\[__int_ _\]_\)

  * **grpc\_port** \(_int_\)

  * **prefer\_grpc** \(_bool_\)

  * **https** \(_Optional_ _\[__bool_ _\]_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **prefix** \(_Optional_ _\[__str_ _\]_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\)

  * **host** \(_Optional_ _\[__str_ _\]_\)

  * **path** \(_Optional_ _\[__str_ _\]_\)

  * **collection\_name** \(_Optional_ _\[__str_ _\]_\)

  * **distance\_func** \(_str_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **vector\_name** \(_Optional_ _\[__str_ _\]_\)

  * **shard\_number** \(_Optional_ _\[__int_ _\]_\)

  * **replication\_factor** \(_Optional_ _\[__int_ _\]_\)

  * **write\_consistency\_factor** \(_Optional_ _\[__int_ _\]_\)

  * **on\_disk\_payload** \(_Optional_ _\[__bool_ _\]_\)

  * **hnsw\_config** \(_Optional_ _\[__common\_types.HnswConfigDiff_ _\]_\)

  * **optimizers\_config** \(_Optional_ _\[__common\_types.OptimizersConfigDiff_ _\]_\)

  * **wal\_config** \(_Optional_ _\[__common\_types.WalConfigDiff_ _\]_\)

  * **quantization\_config** \(_Optional_ _\[__common\_types.QuantizationConfig_ _\]_\)

  * **init\_from** \(_Optional_ _\[__common\_types.InitFrom_ _\]_\)

  * **on\_disk** \(_Optional_ _\[__bool_ _\]_\)

  * **force\_recreate** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

Qdrant

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : Sequence\[str\] | None = None_,     _batch\_size : int = 64_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_Sequence_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts. Ids have to be uuid-like strings.

  * **batch\_size** \(_int_\) – How many vectors upload per-request. Default: 64

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.adelete)\#     

Delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool | None

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : Sequence\[str\] | None = None_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : float | None = None_,     _host : str | None = None_,     _path : str | None = None_,     _collection\_name : str | None = None_,     _distance\_func : str = 'Cosine'_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str | None = None_,     _batch\_size : int = 64_,     _shard\_number : int | None = None_,     _replication\_factor : int | None = None_,     _write\_consistency\_factor : int | None = None_,     _on\_disk\_payload : bool | None = None_,     _hnsw\_config : common\_types.HnswConfigDiff | None = None_,     _optimizers\_config : common\_types.OptimizersConfigDiff | None = None_,     _wal\_config : common\_types.WalConfigDiff | None = None_,     _quantization\_config : common\_types.QuantizationConfig | None = None_,     _init\_from : common\_types.InitFrom | None = None_,     _on\_disk : bool | None = None_,     _force\_recreate : bool = False_,     _\*\* kwargs: Any_, \) → Qdrant[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.afrom_texts)\#     

Construct Qdrant wrapper from a list of texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – A list of texts to be indexed in Qdrant.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – A subclass of Embeddings, responsible for text vectorization.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – An optional list of metadata. If provided it has to be of the same length as a list of texts.

  * **ids** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Optional list of ids to associate with the texts. Ids have to be uuid-like strings.

  * **location** \(_Optional_ _\[__str_ _\]_\) – If :memory: \- use in-memory Qdrant instance. If str \- use it as a url parameter. If None \- fallback to relying on host and port parameters.

  * **url** \(_Optional_ _\[__str_ _\]_\) – either host or str of “Optional\[scheme\], host, Optional\[port\], Optional\[prefix\]”. Default: None

  * **port** \(_Optional_ _\[__int_ _\]_\) – Port of the REST API interface. Default: 6333

  * **grpc\_port** \(_int_\) – Port of the gRPC interface. Default: 6334

  * **prefer\_grpc** \(_bool_\) – If true - use gPRC interface whenever possible in custom methods. Default: False

  * **https** \(_Optional_ _\[__bool_ _\]_\) – If true - use HTTPS\(SSL\) protocol. Default: None

  * **api\_key** \(_Optional_ _\[__str_ _\]_\) – API key for authentication in Qdrant Cloud. Default: None

  * **prefix** \(_Optional_ _\[__str_ _\]_\) – 

If not None - add prefix to the REST URL path. Example: service/v1 will result in

> <http://localhost:6333/service/v1>/\{qdrant-endpoint\} for REST API.

Default: None

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for REST and gRPC API requests. Default: 5.0 seconds for REST and unlimited for gRPC

  * **host** \(_Optional_ _\[__str_ _\]_\) – Host name of Qdrant service. If url and host are None, set to ‘localhost’. Default: None

  * **path** \(_Optional_ _\[__str_ _\]_\) – Path in which the vectors will be stored while using local mode. Default: None

  * **collection\_name** \(_Optional_ _\[__str_ _\]_\) – Name of the Qdrant collection to be used. If not provided, it will be created randomly. Default: None

  * **distance\_func** \(_str_\) – Distance function. One of: “Cosine” / “Euclid” / “Dot”. Default: “Cosine”

  * **content\_payload\_key** \(_str_\) – A payload key used to store the content of the document. Default: “page\_content”

  * **metadata\_payload\_key** \(_str_\) – A payload key used to store the metadata of the document. Default: “metadata”

  * **vector\_name** \(_Optional_ _\[__str_ _\]_\) – Name of the vector to be used internally in Qdrant. Default: None

  * **batch\_size** \(_int_\) – How many vectors upload per-request. Default: 64

  * **shard\_number** \(_Optional_ _\[__int_ _\]_\) – Number of shards in collection. Default is 1, minimum is 1.

  * **replication\_factor** \(_Optional_ _\[__int_ _\]_\) – Replication factor for collection. Default is 1, minimum is 1. Defines how many copies of each shard will be created. Have effect only in distributed mode.

  * **write\_consistency\_factor** \(_Optional_ _\[__int_ _\]_\) – Write consistency factor for collection. Default is 1, minimum is 1. Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact. Have effect only in distributed mode.

  * **on\_disk\_payload** \(_Optional_ _\[__bool_ _\]_\) – If true - point\`s payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by \(slightly\) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM.

  * **hnsw\_config** \(_Optional_ _\[__common\_types.HnswConfigDiff_ _\]_\) – Params for HNSW index

  * **optimizers\_config** \(_Optional_ _\[__common\_types.OptimizersConfigDiff_ _\]_\) – Params for optimizer

  * **wal\_config** \(_Optional_ _\[__common\_types.WalConfigDiff_ _\]_\) – Params for Write-Ahead-Log

  * **quantization\_config** \(_Optional_ _\[__common\_types.QuantizationConfig_ _\]_\) – Params for quantization, if None - quantization will be disabled

  * **init\_from** \(_Optional_ _\[__common\_types.InitFrom_ _\]_\) – Use data stored in another collection to initialize this collection

  * **force\_recreate** \(_bool_\) – Force recreating the collection

  * **\*\*kwargs** \(_Any_\) – Additional arguments passed directly into REST client initialization

  * **on\_disk** \(_Optional_ _\[__bool_ _\]_\)

Return type:     

Qdrant

This is a user-friendly interface that: 1\. Creates embeddings, one for each text 2\. Initializes the Qdrant database as an in-memory docstore by default

> \(and overridable to a remote docstore\)

  3. Adds the text embeddings to the Qdrant database

This is intended to be a quick way to get started.

Example               from langchain_community.vectorstores import Qdrant     from langchain_community.embeddings import OpenAIEmbeddings     embeddings = OpenAIEmbeddings()     qdrant = await Qdrant.afrom_texts(texts, embeddings, "localhost")     

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to AsyncQdrantClient.Search\(\).

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm.

> Defaults to 20.

Parameters:     

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to AsyncQdrantClient.Search\(\).

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

Returns:     

List of Documents selected by maximal marginal relevance and distance for each.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.amax_marginal_relevance_search_with_score_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm.

> Defaults to 20.

Parameters:     

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\)

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\)

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\)

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance and distance for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.asimilarity_search)\#     

Return docs most similar to query. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param filter: Filter by metadata. Defaults to None.

Returns:     

List of Documents most similar to the query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.asimilarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to AsyncQdrantClient.Search\(\).

Returns:     

List of Documents most similar to the query.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.asimilarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to AsyncQdrantClient.Search\(\).

Returns:     

List of documents most similar to the query text and distance for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.asimilarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to AsyncQdrantClient.Search\(\).

Returns:     

List of documents most similar to the query text and distance for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_classmethod _construct\_instance\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : float | None = None_,     _host : str | None = None_,     _path : str | None = None_,     _collection\_name : str | None = None_,     _distance\_func : str = 'Cosine'_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str | None = None_,     _shard\_number : int | None = None_,     _replication\_factor : int | None = None_,     _write\_consistency\_factor : int | None = None_,     _on\_disk\_payload : bool | None = None_,     _hnsw\_config : common\_types.HnswConfigDiff | None = None_,     _optimizers\_config : common\_types.OptimizersConfigDiff | None = None_,     _wal\_config : common\_types.WalConfigDiff | None = None_,     _quantization\_config : common\_types.QuantizationConfig | None = None_,     _init\_from : common\_types.InitFrom | None = None_,     _on\_disk : bool | None = None_,     _force\_recreate : bool = False_,     _\*\* kwargs: Any_, \) → Qdrant[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.construct_instance)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **location** \(_Optional_ _\[__str_ _\]_\)

  * **url** \(_Optional_ _\[__str_ _\]_\)

  * **port** \(_Optional_ _\[__int_ _\]_\)

  * **grpc\_port** \(_int_\)

  * **prefer\_grpc** \(_bool_\)

  * **https** \(_Optional_ _\[__bool_ _\]_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **prefix** \(_Optional_ _\[__str_ _\]_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\)

  * **host** \(_Optional_ _\[__str_ _\]_\)

  * **path** \(_Optional_ _\[__str_ _\]_\)

  * **collection\_name** \(_Optional_ _\[__str_ _\]_\)

  * **distance\_func** \(_str_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **vector\_name** \(_Optional_ _\[__str_ _\]_\)

  * **shard\_number** \(_Optional_ _\[__int_ _\]_\)

  * **replication\_factor** \(_Optional_ _\[__int_ _\]_\)

  * **write\_consistency\_factor** \(_Optional_ _\[__int_ _\]_\)

  * **on\_disk\_payload** \(_Optional_ _\[__bool_ _\]_\)

  * **hnsw\_config** \(_Optional_ _\[__common\_types.HnswConfigDiff_ _\]_\)

  * **optimizers\_config** \(_Optional_ _\[__common\_types.OptimizersConfigDiff_ _\]_\)

  * **wal\_config** \(_Optional_ _\[__common\_types.WalConfigDiff_ _\]_\)

  * **quantization\_config** \(_Optional_ _\[__common\_types.QuantizationConfig_ _\]_\)

  * **init\_from** \(_Optional_ _\[__common\_types.InitFrom_ _\]_\)

  * **on\_disk** \(_Optional_ _\[__bool_ _\]_\)

  * **force\_recreate** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

Qdrant

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.delete)\#     

Delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool | None

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

_classmethod _from\_existing\_collection\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _path : str_,     _collection\_name : str_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : float | None = None_,     _host : str | None = None_,     _\*\* kwargs: Any_, \) → Qdrant[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.from_existing_collection)\#     

Get instance of an existing Qdrant collection. This method will return the instance of the store without inserting any new embeddings

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **path** \(_str_\)

  * **collection\_name** \(_str_\)

  * **location** \(_str_ _|__None_\)

  * **url** \(_str_ _|__None_\)

  * **port** \(_int_ _|__None_\)

  * **grpc\_port** \(_int_\)

  * **prefer\_grpc** \(_bool_\)

  * **https** \(_bool_ _|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **prefix** \(_str_ _|__None_\)

  * **timeout** \(_float_ _|__None_\)

  * **host** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Qdrant_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : Sequence\[str\] | None = None_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : float | None = None_,     _host : str | None = None_,     _path : str | None = None_,     _collection\_name : str | None = None_,     _distance\_func : str = 'Cosine'_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str | None = None_,     _batch\_size : int = 64_,     _shard\_number : int | None = None_,     _replication\_factor : int | None = None_,     _write\_consistency\_factor : int | None = None_,     _on\_disk\_payload : bool | None = None_,     _hnsw\_config : common\_types.HnswConfigDiff | None = None_,     _optimizers\_config : common\_types.OptimizersConfigDiff | None = None_,     _wal\_config : common\_types.WalConfigDiff | None = None_,     _quantization\_config : common\_types.QuantizationConfig | None = None_,     _init\_from : common\_types.InitFrom | None = None_,     _on\_disk : bool | None = None_,     _force\_recreate : bool = False_,     _\*\* kwargs: Any_, \) → Qdrant[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.from_texts)\#     

Construct Qdrant wrapper from a list of texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – A list of texts to be indexed in Qdrant.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – A subclass of Embeddings, responsible for text vectorization.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – An optional list of metadata. If provided it has to be of the same length as a list of texts.

  * **ids** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Optional list of ids to associate with the texts. Ids have to be uuid-like strings.

  * **location** \(_Optional_ _\[__str_ _\]_\) – If :memory: \- use in-memory Qdrant instance. If str \- use it as a url parameter. If None \- fallback to relying on host and port parameters.

  * **url** \(_Optional_ _\[__str_ _\]_\) – either host or str of “Optional\[scheme\], host, Optional\[port\], Optional\[prefix\]”. Default: None

  * **port** \(_Optional_ _\[__int_ _\]_\) – Port of the REST API interface. Default: 6333

  * **grpc\_port** \(_int_\) – Port of the gRPC interface. Default: 6334

  * **prefer\_grpc** \(_bool_\) – If true - use gPRC interface whenever possible in custom methods. Default: False

  * **https** \(_Optional_ _\[__bool_ _\]_\) – If true - use HTTPS\(SSL\) protocol. Default: None

  * **api\_key** \(_Optional_ _\[__str_ _\]_\) – API key for authentication in Qdrant Cloud. Default: None

  * **prefix** \(_Optional_ _\[__str_ _\]_\) – 

If not None - add prefix to the REST URL path. Example: service/v1 will result in

> <http://localhost:6333/service/v1>/\{qdrant-endpoint\} for REST API.

Default: None

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for REST and gRPC API requests. Default: 5.0 seconds for REST and unlimited for gRPC

  * **host** \(_Optional_ _\[__str_ _\]_\) – Host name of Qdrant service. If url and host are None, set to ‘localhost’. Default: None

  * **path** \(_Optional_ _\[__str_ _\]_\) – Path in which the vectors will be stored while using local mode. Default: None

  * **collection\_name** \(_Optional_ _\[__str_ _\]_\) – Name of the Qdrant collection to be used. If not provided, it will be created randomly. Default: None

  * **distance\_func** \(_str_\) – Distance function. One of: “Cosine” / “Euclid” / “Dot”. Default: “Cosine”

  * **content\_payload\_key** \(_str_\) – A payload key used to store the content of the document. Default: “page\_content”

  * **metadata\_payload\_key** \(_str_\) – A payload key used to store the metadata of the document. Default: “metadata”

  * **vector\_name** \(_Optional_ _\[__str_ _\]_\) – Name of the vector to be used internally in Qdrant. Default: None

  * **batch\_size** \(_int_\) – How many vectors upload per-request. Default: 64

  * **shard\_number** \(_Optional_ _\[__int_ _\]_\) – Number of shards in collection. Default is 1, minimum is 1.

  * **replication\_factor** \(_Optional_ _\[__int_ _\]_\) – Replication factor for collection. Default is 1, minimum is 1. Defines how many copies of each shard will be created. Have effect only in distributed mode.

  * **write\_consistency\_factor** \(_Optional_ _\[__int_ _\]_\) – Write consistency factor for collection. Default is 1, minimum is 1. Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact. Have effect only in distributed mode.

  * **on\_disk\_payload** \(_Optional_ _\[__bool_ _\]_\) – If true - point\`s payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by \(slightly\) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM.

  * **hnsw\_config** \(_Optional_ _\[__common\_types.HnswConfigDiff_ _\]_\) – Params for HNSW index

  * **optimizers\_config** \(_Optional_ _\[__common\_types.OptimizersConfigDiff_ _\]_\) – Params for optimizer

  * **wal\_config** \(_Optional_ _\[__common\_types.WalConfigDiff_ _\]_\) – Params for Write-Ahead-Log

  * **quantization\_config** \(_Optional_ _\[__common\_types.QuantizationConfig_ _\]_\) – Params for quantization, if None - quantization will be disabled

  * **init\_from** \(_Optional_ _\[__common\_types.InitFrom_ _\]_\) – Use data stored in another collection to initialize this collection

  * **force\_recreate** \(_bool_\) – Force recreating the collection

  * **\*\*kwargs** \(_Any_\) – Additional arguments passed directly into REST client initialization

  * **on\_disk** \(_Optional_ _\[__bool_ _\]_\)

Return type:     

Qdrant

This is a user-friendly interface that: 1\. Creates embeddings, one for each text 2\. Initializes the Qdrant database as an in-memory docstore by default

> \(and overridable to a remote docstore\)

  3. Adds the text embeddings to the Qdrant database

This is intended to be a quick way to get started.

Example               from langchain_community.vectorstores import Qdrant     from langchain_community.embeddings import OpenAIEmbeddings     embeddings = OpenAIEmbeddings()     qdrant = Qdrant.from_texts(texts, embeddings, "localhost")     

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.max_marginal_relevance_search_with_score_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm.

> Defaults to 20.

Parameters:     

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

Returns:     

List of Documents selected by maximal marginal relevance and distance for each.

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

    _query : str_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

Returns:     

List of Documents most similar to the query.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

Returns:     

List of Documents most similar to the query.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.similarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

Returns:     

List of documents most similar to the query text and distance for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : MetadataFilter | None = None_,     _search\_params : common\_types.SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : common\_types.ReadConsistency | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/qdrant.html#Qdrant.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__MetadataFilter_ _\]_\) – Filter by metadata. Defaults to None.

  * **search\_params** \(_Optional_ _\[__common\_types.SearchParams_ _\]_\) – Additional search params

  * **offset** \(_int_\) – Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned.

  * **consistency** \(_Optional_ _\[__common\_types.ReadConsistency_ _\]_\) – 

Read consistency of the search. Defines how many replicas should be queried before returning the result. Values: \- int - number of replicas to query, values should present in all

> queried replicas

    * ’majority’ - query all replicas, but return values present in the     

majority of replicas

    * ’quorum’ - query the majority of replicas, return values present in     

all of them

    * ’all’ - query all replicas, and return values present in all replicas

  * **\*\*kwargs** \(_Any_\) – Any other named arguments to pass through to QdrantClient.search\(\)

Returns:     

List of documents most similar to the query text and distance for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using Qdrant

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

  * [Qdrant](https://python.langchain.com/docs/integrations/retrievers/self_query/qdrant_self_query/)

__On this page   *[/]: Positional-only parameter separator (PEP 570)