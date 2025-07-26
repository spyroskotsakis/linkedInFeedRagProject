# AzureCosmosDBMongoVCoreVectorSearch — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.AzureCosmosDBMongoVCoreVectorSearch.html
**Word Count:** 2303
**Links Count:** 286
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# AzureCosmosDBMongoVCoreVectorSearch\#

_class _langchain\_azure\_ai.vectorstores.azure\_cosmos\_db\_mongo\_vcore.AzureCosmosDBMongoVCoreVectorSearch\(

    _collection : Collection_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _index\_name : str = 'vectorSearchIndex'_,     _text\_key : str = 'textContent'_,     _embedding\_key : str = 'vectorContent'_,     _application\_name : str = 'langchainpy'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch)\#     

Azure Cosmos DB for MongoDB vCore vector store.

To use, you should have both: \- the `pymongo` python package installed \- a connection string associated with a MongoDB VCore Cluster

Example

. code-block:: python

> from langchain\_azure\_ai.vectorstores.azure\_cosmos\_db import AzureCosmosDBMongoVCoreVectorSearch from langchain.embeddings.openai import OpenAIEmbeddings from pymongo import MongoClient >  > mongo\_client = MongoClient\(“<YOUR-CONNECTION-STRING>”\) collection = mongo\_client\[“<db\_name>”\]\[“<collection\_name>”\] embeddings = OpenAIEmbeddings\(\) vectorstore = AzureCosmosDBMongoVCoreVectorSearch\(collection, embeddings\)

Constructor for AzureCosmosDBMongoVCoreVectorSearch.

Parameters:     

  * **collection** \(_Collection_\) – MongoDB collection to add the texts to.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **index\_name** \(_str_\) – Name of the Atlas Search index.

  * **text\_key** \(_str_\) – MongoDB field that will contain the text for each document.

  * **embedding\_key** \(_str_\) – MongoDB field that will contain the embedding for each document.

  * **application\_name** \(_str_\) – The user agent for telemetry

Attributes

`embeddings` | Returns the embeddings.   ---|---      Methods

`__init__`\(collection, embedding, \*\[, ...\]\) | Constructor for AzureCosmosDBMongoVCoreVectorSearch.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas\]\) | Used to Load Documents into the collection.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `create_filter_index`\(property\_to\_filter, ...\) | Creates a filter index.   `create_index`\(\[num\_lists, dimensions, ...\]\) | Creates an index using the index name specified at instance construction.   `delete`\(\[ids\]\) | Removes the documents with the list of documentIds provided from the collection.   `delete_document_by_id`\(\[document\_id\]\) | Removes a Specific Document by Id.   `delete_index`\(\) | Deletes the index specified during instance construction if it exists.   `from_connection_string`\(connection\_string, ...\) | Creates an Instance of AzureCosmosDBMongoVCoreVectorSearch from a Connection String.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Creates Azure CosmosDB MongoVCore Vector Store using the texts provided.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_collection`\(\) | Returns the collection.   `get_index_name`\(\) | Returns the index name.   `index_exists`\(\) | Verifies if the specified index name during instance construction exists on the collection.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Retrieves the similar docs.   `max_marginal_relevance_search_by_vector`\(...\) | Retrieves the docs with similarity scores.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, kind, ...\]\) | Returns a list of similar documents.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Returns a list of similar documents with their scores.      \_\_init\_\_\(

    _collection : Collection_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _index\_name : str = 'vectorSearchIndex'_,     _text\_key : str = 'textContent'_,     _embedding\_key : str = 'vectorContent'_,     _application\_name : str = 'langchainpy'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.__init__)\#     

Constructor for AzureCosmosDBMongoVCoreVectorSearch.

Parameters:     

  * **collection** \(_Collection_\) – MongoDB collection to add the texts to.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **index\_name** \(_str_\) – Name of the Atlas Search index.

  * **text\_key** \(_str_\) – MongoDB field that will contain the text for each document.

  * **embedding\_key** \(_str_\) – MongoDB field that will contain the embedding for each document.

  * **application\_name** \(_str_\) – The user agent for telemetry

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

    _texts : Iterable\[str\]_,     _metadatas : List\[Dict\[str, Any\]\] | None = None_,     _\*\* kwargs: Any_, \) → List[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.add_texts)\#     

Used to Load Documents into the collection.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_

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

create\_filter\_index\(

    _property\_to\_filter : str_,     _index\_name : str_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.create_filter_index)\#     

Creates a filter index.

Parameters:     

  * **property\_to\_filter** \(_str_\)

  * **index\_name** \(_str_\)

Return type:     

dict\[str, _Any_\]

create\_index\(

    _num\_lists : int = 100_,     _dimensions : int = 1536_,     _similarity : [CosmosDBSimilarityType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType") = CosmosDBSimilarityType.COS_,     _kind : str = 'vector-ivf'_,     _m : int = 16_,     _ef\_construction : int = 64_,     _max\_degree : int = 32_,     _l\_build : int = 50_,     _compression : [CosmosDBVectorSearchCompression](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression") | None = None_,     _pq\_compressed\_dims : int | None = None_,     _pq\_sample\_size : int | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.create_index)\#     

Creates an index using the index name specified at instance construction.

Setting the numLists parameter correctly is important for achieving     

good accuracy and performance. Since the vector store uses IVF as the indexing strategy, you should create the index only after you have loaded a large enough sample documents to ensure that the centroids for the respective buckets are faily distributed.

We recommend that numLists is set to documentCount/1000 for up     

to 1 million documents and to sqrt\(documentCount\) for more than 1 million documents. As the number of items in your database grows, you should tune numLists to be larger in order to achieve good latency performance for vector search.

If you’re experimenting with a new scenario or creating a small demo, you can start with numLists set to 1 to perform a brute-force search across all vectors. This should provide you with the most accurate results from the vector search, however be aware that the search speed and latency will be slow. After your initial setup, you should go ahead and tune the numLists parameter using the above guidance.

Parameters:     

  * **kind** \(_str_\) – 

Type of vector index to create. Possible options are:

>     * vector-ivf >  >     * vector-hnsw >  >     * vector-diskann

  * **num\_lists** \(_int_\) – This integer is the number of clusters that the inverted file \(IVF\) index uses to group the vector data. We recommend that numLists is set to documentCount/1000 for up to 1 million documents and to sqrt\(documentCount\) for more than 1 million documents. Using a numLists value of 1 is akin to performing brute-force search, which has limited performance

  * **dimensions** \(_int_\) – Number of dimensions for vector similarity. The maximum number of supported dimensions is 2000

  * **similarity** \([_CosmosDBSimilarityType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType")\) – 

Similarity metric to use with the IVF index.

Possible options are:          * CosmosDBSimilarityType.COS \(cosine distance\),

    * CosmosDBSimilarityType.L2 \(Euclidean distance\), and

    * CosmosDBSimilarityType.IP \(inner product\).

  * **m** \(_int_\) – The max number of connections per layer \(16 by default, minimum value is 2, maximum value is 100\). Higher m is suitable for datasets with high dimensionality and/or high accuracy requirements.

  * **ef\_construction** \(_int_\) – the size of the dynamic candidate list for constructing the graph \(64 by default, minimum value is 4, maximum value is 1000\). Higher ef\_construction will result in better index quality and higher accuracy, but it will also increase the time required to build the index. ef\_construction has to be at least 2 \* m

  * **max\_degree** \(_int_\) – Max number of neighbors. Default value is 32, range from 20 to 2048. Only vector-diskann search supports this for now.

  * **l\_build** \(_int_\) – l value for index building. Default value is 50, range from 10 to 500. Only vector-diskann search supports this for now.

  * **compression** \([_CosmosDBVectorSearchCompression_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression") _|__None_\) – compression type for vector indexes. Product quantization compression is only supported for DISKANN and half precision compression is only supported for IVF and HNSW for now.

  * **pq\_compressed\_dims** \(_int_ _|__None_\) – Number of dimensions after compression for product quantization. Must be less than original dimensions. Automatically calculated if omitted. Range: 1-8000.

  * **pq\_sample\_size** \(_int_ _|__None_\) – Number of samples for PQ centroid training. Higher value means better quality but longer build time. Default: 1000. Range: 1000-100000.

Returns:     

An object describing the created index

Return type:     

dict\[str, _Any_\]

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.delete)\#     

Removes the documents with the list of documentIds provided from the collection.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

bool | None

delete\_document\_by\_id\(

    _document\_id : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.delete_document_by_id)\#     

Removes a Specific Document by Id.

Parameters:     

**document\_id** \(_str_ _|__None_\) – The document identifier

Return type:     

None

delete\_index\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.delete_index)\#     

Deletes the index specified during instance construction if it exists.

Return type:     

None

_classmethod _from\_connection\_string\(

    _connection\_string : str_,     _namespace : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _application\_name : str = 'langchainpy'_,     _\*\* kwargs: Any_, \) → AzureCosmosDBMongoVCoreVectorSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.from_connection_string)\#     

Creates an Instance of AzureCosmosDBMongoVCoreVectorSearch from a Connection String.

Parameters:     

  * **connection\_string** \(_str_\) – The MongoDB vCore instance connection string

  * **namespace** \(_str_\) – The namespace \(database.collection\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – The embedding utility

  * **application\_name** \(_str_\) – The user agent for telemetry

  * **\*\*kwargs** \(_Any_\) – Dynamic keyword arguments

Returns:     

an instance of the vector store

Return type:     

AzureCosmosDBMongoVCoreVectorSearch

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _collection : Collection | None = None_,     _\*\* kwargs: Any_, \) → AzureCosmosDBMongoVCoreVectorSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.from_texts)\#     

Creates Azure CosmosDB MongoVCore Vector Store using the texts provided.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\)

  * **collection** \(_Optional_ _\[__Collection_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

AzureCosmosDBMongoVCoreVectorSearch

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

get\_collection\(\) → Collection[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.get_collection)\#     

Returns the collection.

Return type:     

Collection

get\_index\_name\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.get_index_name)\#     

Returns the index name.

Returns:     

Returns the index name

Return type:     

str

index\_exists\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.index_exists)\#     

Verifies if the specified index name during instance construction exists on the collection.

Returns:     

Returns True on success and False if no such index exists     

on the collection

Return type:     

bool

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _pre\_filter : Dict | None = None_,     _ef\_search : int = 40_,     _score\_threshold : float = 0.0_,     _l\_search : int = 40_,     _with\_embedding : bool = False_,     _oversampling : float | None = 1.0_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.max_marginal_relevance_search)\#     

Retrieves the similar docs.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **kind** \([_CosmosDBVectorSearchType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType")\)

  * **pre\_filter** \(_Dict_ _|__None_\)

  * **ef\_search** \(_int_\)

  * **score\_threshold** \(_float_\)

  * **l\_search** \(_int_\)

  * **with\_embedding** \(_bool_\)

  * **oversampling** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _pre\_filter : Dict | None = None_,     _ef\_search : int = 40_,     _score\_threshold : float = 0.0_,     _l\_search : int = 40_,     _with\_embedding : bool = False_,     _oversampling : float | None = 1.0_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.max_marginal_relevance_search_by_vector)\#     

Retrieves the docs with similarity scores.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **kind** \([_CosmosDBVectorSearchType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType")\)

  * **pre\_filter** \(_Dict_ _|__None_\)

  * **ef\_search** \(_int_\)

  * **score\_threshold** \(_float_\)

  * **l\_search** \(_int_\)

  * **with\_embedding** \(_bool_\)

  * **oversampling** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 4_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _pre\_filter : Dict | None = None_,     _ef\_search : int = 40_,     _score\_threshold : float = 0.0_,     _l\_search : int = 40_,     _with\_embedding : bool = False_,     _oversampling : float | None = 1.0_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.similarity_search)\#     

Returns a list of similar documents.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **kind** \([_CosmosDBVectorSearchType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType")\)

  * **pre\_filter** \(_Dict_ _|__None_\)

  * **ef\_search** \(_int_\)

  * **score\_threshold** \(_float_\)

  * **l\_search** \(_int_\)

  * **with\_embedding** \(_bool_\)

  * **oversampling** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 4_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _pre\_filter : Dict | None = None_,     _ef\_search : int = 40_,     _score\_threshold : float = 0.0_,     _l\_search : int = 40_,     _with\_embedding : bool = False_,     _oversampling : float | None = 1.0_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/azure_cosmos_db_mongo_vcore.html#AzureCosmosDBMongoVCoreVectorSearch.similarity_search_with_score)\#     

Returns a list of similar documents with their scores.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **kind** \([_CosmosDBVectorSearchType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType")\)

  * **pre\_filter** \(_Dict_ _|__None_\)

  * **ef\_search** \(_int_\)

  * **score\_threshold** \(_float_\)

  * **l\_search** \(_int_\)

  * **with\_embedding** \(_bool_\)

  * **oversampling** \(_float_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)