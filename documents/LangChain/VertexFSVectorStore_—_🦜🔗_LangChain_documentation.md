# VertexFSVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/bq_storage_vectorstores/langchain_google_community.bq_storage_vectorstores.featurestore.VertexFSVectorStore.html
**Word Count:** 2307
**Links Count:** 327
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# VertexFSVectorStore\#

_class _langchain\_google\_community.bq\_storage\_vectorstores.featurestore.VertexFSVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/featurestore.html#VertexFSVectorStore)\#     

Bases: `BaseBigQueryVectorStore`

A vector store implementation that utilizes BigQuery Storage and Vertex AI Feature Store.

This class provides efficient storage, using BigQuery as the underlining source of truth and retrieval of documents with vector embeddings within Vertex AI Feature Store. It is particularly indicated for low latency serving. It supports similarity search, filtering and getting nearest neighbor by id. Optionally, this class can leverage a BigQuery Vector Search for batch serving through the to\_bq\_vector\_store method.

embedding\#     

Embedding model for generating and comparing embeddings.

project\_id\#     

Google Cloud Project ID where BigQuery resources are located.

dataset\_name\#     

BigQuery dataset name.

table\_name\#     

BigQuery table name.

location\#     

BigQuery region/location.

content\_field\#     

Name of the column storing document content \(default: “content”\).

embedding\_field\#     

Name of the column storing text embeddings \(default: “embedding”\).

doc\_id\_field\#     

Name of the column storing document IDs \(default: “doc\_id”\).

credentials\#     

Optional Google Cloud credentials object.

embedding\_dimension\#     

Dimension of the embedding vectors \(inferred if not provided\).

online\_store\_name\#     

Name of the Vertex AI Feature Store online store. Defaults to the dataset name.

Type:     

str, optional

online\_store\_location\#     

Location of the online store. Default to “location” parameter.

Type:     

str, optional

view\_name\#     

Name of the Feature View. Defaults to the table name.

Type:     

str, optional

cron\_schedule\#     

Cron schedule for data syncing.

Type:     

str, optional

algorithm\_config\#     

Algorithm configuration for indexing.

Type:     

Any, optional

filter\_columns\#     

Columns to use for filtering.

Type:     

List\[str\], optional

crowding\_column\#     

Column to use for crowding.

Type:     

str, optional

distance\_measure\_type\#     

Distance measure type \(default: DOT\_PRODUCT\_DISTANCE\).

Type:     

str, optional

enable\_private\_service\_connect\#     

Whether to enable Private Service Connect for the online store at creation time. Defaults to False.

Type:     

bool, optional

transport \(Optional\[Union\[str, FeatureOnlineStoreServiceTransport,     

Callable\[…, FeatureOnlineStoreServiceTransport\]\]\]\): Transport configuration for API requests. Can be a transport instance, string identifier, or callable that returns a transport. Required when using Private Service Connect for querying. Example:

> \`\`\`python import grpc from google.cloud.aiplatform\_v1.services.feature\_online\_store\_service. transports.grpc import FeatureOnlineStoreServiceGrpcTransport >  > transport = FeatureOnlineStoreServiceGrpcTransport\( >      >  > channel=grpc.insecure\_channel\(“10.128.0.1:10002”\) >  > \) vertex\_fs = VertexFSVectorStore\( >
>> transport=transport, Your other params…. >  > \) vertex\_fs.similarity\_search\(“My query”\) \`\`\`

project\_allowlist\#     

Only needed when enable\_private\_service\_connect is set to true. List of projects allowed to access the online store. Required at creation time. Defaults to empty list.

Type:     

List\[str\], optional

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _algorithm\_config _: Any | None_ _ = None_\#     

_param _content\_field _: str_ _ = 'content'_\#     

_param _credentials _: Any | None_ _ = None_\#     

_param _cron\_schedule _: str | None_ _ = None_\#     

_param _crowding\_column _: str | None_ _ = None_\#     

_param _dataset\_name _: str_ _\[Required\]_\#     

_param _distance\_measure\_type _: str | None_ _ = None_\#     

_param _doc\_id\_field _: str_ _ = 'doc\_id'_\#     

_param _embedding _: [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_ _\[Required\]_\#     

_param _embedding\_dimension _: int | None_ _ = None_\#     

_param _embedding\_field _: str_ _ = 'embedding'_\#     

_param _enable\_private\_service\_connect _: bool_ _ = False_\#     

_param _extra\_fields _: Dict\[str, str\] | None_ _ = None_\#     

_param _feature\_view _: Any_ _ = None_\#     

_param _filter\_columns _: List\[str\] | None_ _ = None_\#     

_param _location _: str_ _\[Required\]_\#     

_param _online\_store _: Any_ _ = None_\#     

_param _online\_store\_location _: str | None_ _ = None_\#     

_param _online\_store\_name _: str | None_ _ = None_\#     

_param _project\_allowlist _: List\[str\]__ = \[\]_\#     

_param _project\_id _: str_ _\[Required\]_\#     

_param _table\_name _: str_ _\[Required\]_\#     

_param _table\_schema _: Any_ _ = None_\#     

_param _temp\_dataset\_name _: str | None_ _ = None_\#     

_param _transport _: Any_ _ = None_\#     

_param _view\_name _: str | None_ _ = None_\#     

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

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*\* kwargs: Any_, \) → VertexFSVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/featurestore.html#VertexFSVectorStore.from_texts)\#     

Return VectorStore initialized from input texts

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of strings to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – An embedding model instance for text to vector transformations.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadata records associated with the texts. \(ie \[\{“url”: “www.myurl1.com”, “title”: “title1”\}, \{“url”: “www.myurl2.com”, “title”: “title2”\}\]\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_VertexFSVectorStore_

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

    _texts : List\[str\]_,     _metadatas : List\[dict\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadata records associated with the texts. \(ie \[\{“url”: “www.myurl1.com”, “title”: “title1”\}, \{“url”: “www.myurl2.com”, “title”: “title2”\}\]\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

add\_texts\_with\_embeddings\(

    _texts : List\[str\]_,     _embs : List\[List\[float\]\]_,     _metadatas : List\[dict\] | None = None_, \) → List\[str\]\#     

Add precomputed embeddings and relative texts / metadatas to the vectorstore.

Parameters:     

  * **ids** – List of unique ids in string format

  * **texts** \(_List_ _\[__str_ _\]_\) – List of strings to add to the vectorstore.

  * **embs** \(_List_ _\[__List_ _\[__float_ _\]__\]_\) – List of lists of floats with text embeddings for texts.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadata records associated with the texts. \(ie \[\{“url”: “www.myurl1.com”, “title”: “title1”\}, \{“url”: “www.myurl2.com”, “title”: “title2”\}\]\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None\#     

Delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

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

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None\#     

Delete documents by record IDs

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

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

get\_documents\(

    _ids : List\[str\] | None_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/featurestore.html#VertexFSVectorStore.get_documents)\#     

Search documents by their ids or metadata values. :param ids: List of ids of documents to retrieve from the vectorstore. :param filter: Filter on metadata properties, e.g.

> \{ >      >  > “str\_property”: “foo”, “int\_property”: 123 >  > \}

Returns:     

List of ids from adding the texts into the vectorstore.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 5_,     _fetch\_k : int = 25_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **\*\*kwargs** \(_Any_\)

  * **query** \(_str_\) – search query text.

  * **filter** – 

Filter on metadata properties, e.g. \{

> ”str\_property”: “foo”, “int\_property”: 123

\}

  * **k** \(_int_\) – Number of Documents to return. Defaults to 5.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 5_,     _fetch\_k : int = 25_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **filter** – 

Filter on metadata properties, e.g. \{

> ”str\_property”: “foo”, “int\_property”: 123

\}

  * **k** \(_int_\) – Number of Documents to return. Defaults to 5.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **kwargs** \(_Any_\)

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

search\_neighbors\_by\_ids\(

    _ids : List\[str\]_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[List\[List\[Any\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/featurestore.html#VertexFSVectorStore.search_neighbors_by_ids)\#     

Searches for neighboring entities in a Vertex Feature Store based on     

their IDs and optional filter on metadata

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]_\) – A list of string identifiers representing the entities to search for.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – 

\(Optional\) A dictionary specifying filter criteria for document on metadata properties, e.g.

> \{ >      >  > “str\_property”: “foo”, “int\_property”: 123 >  > \}

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_List_\[_List_\[_Any_\]\]\]

similarity\_search\(

    _query : str_,     _k : int = 5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Search for top k docs most similar to input query.

Parameters:     

  * **query** \(_str_\) – search query to search documents with.

  * **filter** – \(Optional\) A dictionary specifying filtering criteria for the documents. Ie. \{“title”: “mytitle”\}

  * **k** \(_int_\) – \(Optional\) The number of top-ranking similar documents to return per embedding. Defaults to 5.

  * **kwargs** \(_Any_\)

Returns:     

Return docs most similar to input query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **filter** – \(Optional\) A dictionary specifying filtering criteria for the documents. Ie. \{“title”: “mytitle”\}

  * **k** \(_int_\) – \(Optional\) The number of top-ranking similar documents to return per embedding. Defaults to 5.

  * **kwargs** \(_Any_\)

Returns:     

Return docs most similar to embedding vector.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\_with\_score\(

    _embedding : List\[float\]_,     _filter : Dict\[str, Any\] | None = None_,     _k : int = 5_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Return docs most similar to embedding vector with scores.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – \(Optional\) A dictionary specifying filtering criteria for the documents. Ie. \{“title”: “mytitle”\}

  * **k** \(_int_\) – \(Optional\) The number of top-ranking similar documents to return per embedding. Defaults to 5.

Returns:     

Return docs most similar to embedding vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_by\_vectors\(

    _embeddings : List\[List\[float\]\]_,     _filter : Dict\[str, Any\] | None = None_,     _k : int = 5_,     _with\_scores : bool = False_,     _with\_embeddings : bool = False_,     _\*\* kwargs: Any_, \) → Any\#     

Core similarity search function. Handles a list of embedding vectors, optionally returning scores and embeddings.

Parameters:     

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\) – A list of embedding vectors, where each vector is a list of floats.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – \(Optional\) A dictionary specifying filtering criteria for the documents. Ie. \{“title”: “mytitle”\}

  * **k** \(_int_\) – \(Optional\) The number of top-ranking similar documents to return per embedding. Defaults to 5.

  * **with\_scores** \(_bool_\) – \(Optional\) If True, include similarity scores in the result for each matched document. Defaults to False.

  * **with\_embeddings** \(_bool_\) – \(Optional\) If True, include the matched document’s embedding vector in the result. Defaults to False.

  * **kwargs** \(_Any_\)

Returns:     

A list of k documents for each embedding in embeddings

Return type:     

_Any_

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

    _query : str_,     _filter : Dict\[str, Any\] | None = None_,     _k : int = 5_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Search for top k docs most similar to input query, returns both docs and scores.

Parameters:     

  * **query** \(_str_\) – search query to search documents with.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – \(Optional\) A dictionary specifying filtering criteria for the documents. Ie. \{“title”: “mytitle”\}

  * **k** \(_int_\) – \(Optional\) The number of top-ranking similar documents to return per embedding. Defaults to 5.

  * **kwargs** \(_Any_\)

Returns:     

Return docs most similar to input query along with scores.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

sync\_data\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/featurestore.html#VertexFSVectorStore.sync_data)\#     

Sync the data from the BigQuery source into the Executor source

Return type:     

None

to\_bq\_vector\_store\(

    _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bq_storage_vectorstores/featurestore.html#VertexFSVectorStore.to_bq_vector_store)\#     

Converts the current object’s parameters into a BigQueryVectorStore instance.

This method combines the base parameters of the current object to create a     

BigQueryVectorStore object.

Parameters:     

**\*\*kwargs** \(_Any_\) – Additional keyword arguments to be passed to the \` BigQueryVectorStore\` constructor. These override any matching parameters in the base object.

Returns:     

An initialized BigQueryVectorStore object ready     

for vector search operations.

Return type:     

[BigQueryVectorStore](https://python.langchain.com/api_reference/google_community/bq_storage_vectorstores/langchain_google_community.bq_storage_vectorstores.bigquery.BigQueryVectorStore.html#langchain_google_community.bq_storage_vectorstores.bigquery.BigQueryVectorStore "langchain_google_community.bq_storage_vectorstores.bigquery.BigQueryVectorStore")

Raises:     

**ValueError** – If any of the combined parameters are invalid for initializing a BigQueryVectorStore.

_property _embeddings _: [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None_\#     

Access the query embedding object if available.

_property _full\_table\_id _: str_\#     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)