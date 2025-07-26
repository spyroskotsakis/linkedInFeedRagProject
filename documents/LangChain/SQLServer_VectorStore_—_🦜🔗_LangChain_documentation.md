# SQLServer_VectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.SQLServer_VectorStore.html
**Word Count:** 2604
**Links Count:** 244
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# SQLServer\_VectorStore\#

_class _langchain\_sqlserver.vectorstores.SQLServer\_VectorStore\(

    _\*_ ,     _connection : Connection | None = None_,     _connection\_string : str_,     _db\_schema : str | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _embedding\_length : int_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _table\_name : str = 'sqlserver\_vectorstore'_,     _batch\_size : int = 100_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore)\#     

SQL Server Vector Store.

This class provides a vector store interface for adding texts and performing     

similarity searches on the texts in SQL Server.

Initialize the SQL Server vector store.

Parameters:     

  * **connection** \(_Optional_ _\[__Connection_ _\]_\) – Optional SQLServer connection.

  * **connection\_string** \(_str_\) – SQLServer connection string. If the connection string does not contain a username & password or TrustedConnection=yes, Entra ID authentication is used. SQL Server ODBC connection string can be retrieved from the Connection strings pane of the database in Azure portal. Sample connection string format: \- “Driver=<drivername>;Server=<servername>;Database=<dbname>; Uid=<username>;Pwd=<password>;TrustServerCertificate=no;” \- “mssql+pyodbc://username:password@servername/dbname?other\_params”

  * **db\_schema** \(_Optional_ _\[__str_ _\]_\) – The schema in which the vector store will be created. This schema must exist and the user must have permissions to the schema.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy")\) – The distance strategy to use for comparing embeddings. Default value is COSINE. Available options are: \- COSINE \- DOT \- EUCLIDEAN

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **embedding\_length** \(_int_\) – The length \(dimension\) of the vectors to be stored in the table. Note that only vectors of same size can be added to the vector store.

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\) – Relevance score funtion to be used. Optional param, defaults to None.

  * **table\_name** \(_str_\) – The name of the table to use for storing embeddings. Default value is sqlserver\_vectorstore.

  * **batch\_size** \(_int_\) – Number of documents/texts to be inserted at once to Db, max 419.

Attributes

`batch_size` | batch\_size property for SQLServer\_VectorStore class.   ---|---   `distance_strategy` | distance\_strategy property for SQLServer\_VectorStore class.   `embeddings` | embeddings property for SQLServer\_VectorStore class.      Methods

`__init__`\(\*\[, connection, db\_schema, ...\]\) | Initialize the SQL Server vector store.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | add\_texts function for SQLServer\_VectorStore class.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `delete`\(\[ids\]\) | Delete embeddings in the vectorstore by the ids.   `drop`\(\) | Drops every table created during initialization of vector store.   `from_documents`\(documents, embedding\[, ...\]\) | Create a SQL Server vectorStore initialized from texts and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a SQL Server vectorStore initialized from texts and embeddings.   `get_by_ids`\(ids, /\) | Get documents by their IDs from the vectorstore.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k\]\) | Return docs most similar to given query.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to the embedding vector.   `similarity_search_by_vector_with_score`\(embedding\) | Similarity search by vector with score.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k\]\) | Similarity search with score.      \_\_init\_\_\(

    _\*_ ,     _connection : Connection | None = None_,     _connection\_string : str_,     _db\_schema : str | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _embedding\_length : int_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _table\_name : str = 'sqlserver\_vectorstore'_,     _batch\_size : int = 100_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.__init__)\#     

Initialize the SQL Server vector store.

Parameters:     

  * **connection** \(_Connection_ _|__None_\) – Optional SQLServer connection.

  * **connection\_string** \(_str_\) – SQLServer connection string. If the connection string does not contain a username & password or TrustedConnection=yes, Entra ID authentication is used. SQL Server ODBC connection string can be retrieved from the Connection strings pane of the database in Azure portal. Sample connection string format: \- “Driver=<drivername>;Server=<servername>;Database=<dbname>; Uid=<username>;Pwd=<password>;TrustServerCertificate=no;” \- “mssql+pyodbc://username:password@servername/dbname?other\_params”

  * **db\_schema** \(_str_ _|__None_\) – The schema in which the vector store will be created. This schema must exist and the user must have permissions to the schema.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy")\) – The distance strategy to use for comparing embeddings. Default value is COSINE. Available options are: \- COSINE \- DOT \- EUCLIDEAN

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **embedding\_length** \(_int_\) – The length \(dimension\) of the vectors to be stored in the table. Note that only vectors of same size can be added to the vector store.

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\) – Relevance score funtion to be used. Optional param, defaults to None.

  * **table\_name** \(_str_\) – The name of the table to use for storing embeddings. Default value is sqlserver\_vectorstore.

  * **batch\_size** \(_int_\) – Number of documents/texts to be inserted at once to Db, max 419.

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

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.add_texts)\#     

add\_texts function for SQLServer\_VectorStore class.

Compute the embeddings for the input texts and store embeddings     

in the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add into the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – List of metadatas \(python dicts\) associated with the input texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of IDs for the input texts.

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters.

Returns:     

List of IDs generated from adding the texts into the vectorstore.

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

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.delete)\#     

Delete embeddings in the vectorstore by the ids.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of IDs to delete. If None, delete all. Default is None. No data is deleted if empty list is provided.

  * **kwargs** \(_Any_\) – vectorstore specific parameters.

Returns:     

Optional\[bool\]

Return type:     

bool | None

drop\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.drop)\#     

Drops every table created during initialization of vector store.

Return type:     

None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _connection\_string : str = ''_,     _embedding\_length : int = 0_,     _table\_name : str = 'sqlserver\_vectorstore'_,     _db\_schema : str | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 100_,     _\*\* kwargs: Any_, \) → SQLServer\_VectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.from_documents)\#     

Create a SQL Server vectorStore initialized from texts and embeddings.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **connection\_string** \(_str_\) – SQLServer connection string. If the connection string does not contain a username & password or TrustedConnection=yes, Entra ID authentication is used. SQL Server ODBC connection string can be retrieved from the Connection strings pane of the database in Azure portal. Sample connection string format: \- “Driver=<drivername>;Server=<servername>;Database=<dbname>; Uid=<username>;Pwd=<password>;TrustServerCertificate=no;” \- “mssql+pyodbc://username:password@servername/dbname?other\_params”

  * **embedding\_length** \(_int_\) – The length \(dimension\) of the vectors to be stored in the table. Note that only vectors of same size can be added to the vector store.

  * **table\_name** \(_str_\) – The name of the table to use for storing embeddings. Default value is sqlserver\_vectorstore.

  * **db\_schema** \(_str_ _|__None_\) – The schema in which the vector store will be created. This schema must exist and the user must have permissions to the schema.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy")\) – The distance strategy to use for comparing embeddings. Default value is COSINE. Available options are: \- COSINE \- DOT \- EUCLIDEAN

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of IDs for the input texts.

  * **batch\_size** \(_int_\) – Number of documents to be inserted at once to Db, max MAX\_BATCH\_SIZE.

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters.

Returns:     

A SQL Server vectorstore.

Return type:     

SQLServer\_VectorStore

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _connection\_string : str = ''_,     _embedding\_length : int = 0_,     _table\_name : str = 'sqlserver\_vectorstore'_,     _db\_schema : str | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 100_,     _\*\* kwargs: Any_, \) → SQLServer\_VectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.from_texts)\#     

Create a SQL Server vectorStore initialized from texts and embeddings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Iterable of strings to add into the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas \(python dicts\) associated with the input texts.

  * **connection\_string** \(_str_\) – SQLServer connection string. If the connection string does not contain a username & password or TrustedConnection=yes, Entra ID authentication is used. SQL Server ODBC connection string can be retrieved from the Connection strings pane of the database in Azure portal. Sample connection string format: \- “Driver=<drivername>;Server=<servername>;Database=<dbname>; Uid=<username>;Pwd=<password>;TrustServerCertificate=no;” \- “mssql+pyodbc://username:password@servername/dbname?other\_params”

  * **embedding\_length** \(_int_\) – The length \(dimension\) of the vectors to be stored in the table. Note that only vectors of same size can be added to the vector store.

  * **table\_name** \(_str_\) – The name of the table to use for storing embeddings.

  * **db\_schema** \(_str_ _|__None_\) – The schema in which the vector store will be created. This schema must exist and the user must have permissions to the schema.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/sqlserver/vectorstores/langchain_sqlserver.vectorstores.DistanceStrategy.html#langchain_sqlserver.vectorstores.DistanceStrategy "langchain_sqlserver.vectorstores.DistanceStrategy")\) – The distance strategy to use for comparing embeddings. Default value is COSINE. Available options are: \- COSINE \- DOT \- EUCLIDEAN

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of IDs for the input texts.

  * **batch\_size** \(_int_\) – Number of texts to be inserted at once to Db, max MAX\_BATCH\_SIZE.

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters.

Returns:     

A SQL Server vectorstore.

Return type:     

SQLServer\_VectorStore

get\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.get_by_ids)\#     

Get documents by their IDs from the vectorstore.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\) – List of IDs to retrieve.

Returns:     

List of Documents

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

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

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.max_marginal_relevance_search_by_vector)\#     

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

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.similarity_search)\#     

Return docs most similar to given query.

Parameters:     

  * **query** \(_str_\) – Text to look up the most similar embedding to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Values for filtering on metadata during similarity search.

Returns:     

List of Documents most similar to the query provided.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.similarity_search_by_vector)\#     

Return docs most similar to the embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Values for filtering on metadata during similarity search.

Returns:     

List of Documents most similar to the embedding provided.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\_with\_score\(

    _embedding : List\[float\]_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.similarity_search_by_vector_with_score)\#     

Similarity search by vector with score.

Run similarity search with distance, given an embedding     

and return docs most similar to the embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Values for filtering on metadata during similarity search.

Returns:     

List of tuple of Document and an accompanying score in order of similarity to the embedding provided. Note that, a smaller score implies greater similarity.

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

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_sqlserver/vectorstores.html#SQLServer_VectorStore.similarity_search_with_score)\#     

Similarity search with score.

Run similarity search with distance and     

return docs most similar to the embedding vector.

Parameters:     

  * **query** \(_str_\) – Text to look up the most similar embedding to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Values for filtering on metadata during similarity search.

Returns:     

List of tuple of Document and an accompanying score in order of similarity to the query provided. Note that, a smaller score implies greater similarity.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)