# AsyncPGVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore.html
**Word Count:** 2570
**Links Count:** 357
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# AsyncPGVectorStore\#

_class _langchain\_postgres.v2.async\_vectorstore.AsyncPGVectorStore\(

    _key : object_,     _engine : AsyncEngine_,     _embedding\_service : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str | None = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore)\#     

Postgres Vector Store class

AsyncPGVectorStore constructor. :param key: Prevent direct constructor usage. :type key: object :param engine: Connection pool engine for managing connections to postgres database. :type engine: PGEngine :param embedding\_service: Text embedding model to use. :type embedding\_service: Embeddings :param table\_name: Name of the existing table or the table to be created. :type table\_name: str :param schema\_name: Name of the database schema. Defaults to “public”. :type schema\_name: str, optional :param content\_column: Column that represent a Document’s page\_content. Defaults to “content”. :type content\_column: str :param embedding\_column: Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”. :type embedding\_column: str :param metadata\_columns: Column\(s\) that represent a document’s metadata. :type metadata\_columns: list\[str\] :param id\_column: Column that represents the Document’s id. Defaults to “langchain\_id”. :type id\_column: str :param metadata\_json\_column: Column to store metadata as JSON. Defaults to “langchain\_metadata”. :type metadata\_json\_column: str :param distance\_strategy: Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE. :type distance\_strategy: DistanceStrategy :param k: Number of Documents to return from search. Defaults to 4. :type k: int :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. :type fetch\_k: int :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :type lambda\_mult: float :param index\_query\_options: Index query option. :type index\_query\_options: QueryOptions :param hybrid\_search\_config: Hybrid search configuration. Defaults to None. :type hybrid\_search\_config: HybridSearchConfig

Raises:     

**Exception** – If called directly by user.

Parameters:     

  * **key** \(_object_\)

  * **engine** \(_AsyncEngine_\)

  * **embedding\_service** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **table\_name** \(_str_\)

  * **schema\_name** \(_str_\)

  * **content\_column** \(_str_\)

  * **embedding\_column** \(_str_\)

  * **metadata\_columns** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **id\_column** \(_str_\)

  * **metadata\_json\_column** \(_Optional_ _\[__str_ _\]_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **index\_query\_options** \(_Optional_ _\[_[_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") _\]_\)

  * **hybrid\_search\_config** \(_Optional_ _\[_[_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") _\]_\)

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(key, engine, embedding\_service, ...\) | AsyncPGVectorStore constructor.   ---|---   `aadd_documents`\(documents\[, ids\]\) | Embed documents and add to the table.   `aadd_embeddings`\(texts, embeddings\[, ...\]\) | Add data along with embeddings to the table.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Embed texts and add to the table.   `aapply_hybrid_search_index`\(\[concurrently\]\) | Creates a TSV index in the vector store table if possible.   `aapply_vector_index`\(index\[, name, concurrently\]\) | Create index in the vector store table.   `add_documents`\(documents\[, ids\]\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Delete records from the table.   `adrop_vector_index`\(\[index\_name\]\) | Drop the vector index.   `afrom_documents`\(documents, embedding, ...\[, ...\]\) | Create an AsyncPGVectorStore instance from documents.   `afrom_texts`\(texts, embedding, engine, ...\[, ...\]\) | Create an AsyncPGVectorStore instance from texts.   `aget_by_ids`\(ids\) | Get documents by ids.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs and distance scores selected using the maximal marginal relevance.   `areindex`\(\[index\_name\]\) | Re-index the vector store table.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter\]\) | Return docs selected by similarity search on query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs selected by vector similarity search.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, filter\]\) | Return docs and distance scores selected by similarity search on query.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs and distance scores selected by vector similarity search.   `create`\(engine, embedding\_service, table\_name, \*\) | Create an AsyncPGVectorStore instance.   `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `from_documents`\(documents, embedding, engine, ...\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding, engine, table\_name\) | Return VectorStore initialized from texts and embeddings.   `get_by_ids`\(ids\) | Get documents by their IDs.   `is_valid_index`\(\[index\_name\]\) | Check if index exists in the table.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score_by_vector`\(...\) |    `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, filter\]\) | Run similarity search with distance.   `similarity_search_with_score_by_vector`\(embedding\) |       \_\_init\_\_\(

    _key : object_,     _engine : AsyncEngine_,     _embedding\_service : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str | None = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.__init__)\#     

AsyncPGVectorStore constructor. :param key: Prevent direct constructor usage. :type key: object :param engine: Connection pool engine for managing connections to postgres database. :type engine: PGEngine :param embedding\_service: Text embedding model to use. :type embedding\_service: Embeddings :param table\_name: Name of the existing table or the table to be created. :type table\_name: str :param schema\_name: Name of the database schema. Defaults to “public”. :type schema\_name: str, optional :param content\_column: Column that represent a Document’s page\_content. Defaults to “content”. :type content\_column: str :param embedding\_column: Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”. :type embedding\_column: str :param metadata\_columns: Column\(s\) that represent a document’s metadata. :type metadata\_columns: list\[str\] :param id\_column: Column that represents the Document’s id. Defaults to “langchain\_id”. :type id\_column: str :param metadata\_json\_column: Column to store metadata as JSON. Defaults to “langchain\_metadata”. :type metadata\_json\_column: str :param distance\_strategy: Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE. :type distance\_strategy: DistanceStrategy :param k: Number of Documents to return from search. Defaults to 4. :type k: int :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. :type fetch\_k: int :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :type lambda\_mult: float :param index\_query\_options: Index query option. :type index\_query\_options: QueryOptions :param hybrid\_search\_config: Hybrid search configuration. Defaults to None. :type hybrid\_search\_config: HybridSearchConfig

Raises:     

**Exception** – If called directly by user.

Parameters:     

  * **key** \(_object_\)

  * **engine** \(_AsyncEngine_\)

  * **embedding\_service** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **table\_name** \(_str_\)

  * **schema\_name** \(_str_\)

  * **content\_column** \(_str_\)

  * **embedding\_column** \(_str_\)

  * **metadata\_columns** \(_list_ _\[__str_ _\]__|__None_\)

  * **id\_column** \(_str_\)

  * **metadata\_json\_column** \(_str_ _|__None_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy")\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") _|__None_\)

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") _|__None_\)

_async _aadd\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.aadd_documents)\#     

Embed documents and add to the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

_async _aadd\_embeddings\(

    _texts : Iterable\[str\]_,     _embeddings : list\[list\[float\]\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.aadd_embeddings)\#     

Add data along with embeddings to the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **embeddings** \(_list_ _\[__list_ _\[__float_ _\]__\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.aadd_texts)\#     

Embed texts and add to the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

_async _aapply\_hybrid\_search\_index\(

    _concurrently : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.aapply_hybrid_search_index)\#     

Creates a TSV index in the vector store table if possible.

Parameters:     

**concurrently** \(_bool_\)

Return type:     

None

_async _aapply\_vector\_index\(

    _index : [BaseIndex](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html#langchain_postgres.v2.indexes.BaseIndex "langchain_postgres.v2.indexes.BaseIndex")_,     _name : str | None = None_,     _\*_ ,     _concurrently : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.aapply_vector_index)\#     

Create index in the vector store table.

Parameters:     

  * **index** \([_BaseIndex_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html#langchain_postgres.v2.indexes.BaseIndex "langchain_postgres.v2.indexes.BaseIndex")\)

  * **name** \(_str_ _|__None_\)

  * **concurrently** \(_bool_\)

Return type:     

None

add\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.add_documents)\#     

Add or update documents in the vectorstore.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **kwargs** \(_Any_\) – Additional keyword arguments. if kwargs contains ids and documents contain ids, the ids in the kwargs will receive precedence.

  * **ids** \(_list_ _|__None_\)

Returns:     

List of IDs of the added texts.

Raises:     

**ValueError** – If the number of ids does not match the number of documents.

Return type:     

list\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_list_ _|__None_\) – Optional list of IDs associated with the texts.

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters. One of the kwargs should be ids which is a list of ids associated with the texts.

Returns:     

List of ids from adding the texts into the vectorstore.

Raises:     

  * **ValueError** – If the number of metadatas does not match the number of texts.

  * **ValueError** – If the number of ids does not match the number of texts.

Return type:     

list\[str\]

_async _adelete\(

    _ids : list | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.adelete)\#     

Delete records from the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

bool | None

_async _adrop\_vector\_index\(

    _index\_name : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.adrop_vector_index)\#     

Drop the vector index.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

None

_async classmethod _afrom\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_,     _\*\* kwargs: Any_, \) → AsyncPGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.afrom_documents)\#     

Create an AsyncPGVectorStore instance from documents.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **metadatas** \(_Optional_ _\[__list_ _\[__dict_ _\]__\]_\) – List of metadatas to add to table records.

  * **ids** \(_list_ _|__None_\) – \(Optional\[list\[str\]\]\): List of IDs to add to table records.

  * **content\_column** \(_str_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]_\) – Column\(s\) that represent a document’s metadata.

  * **ignore\_metadata\_columns** \(_list_ _\[__str_ _\]_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **schema\_name** \(_str_\)

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") _|__None_\)

  * **kwargs** \(_Any_\)

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Returns:     

AsyncPGVectorStore

Return type:     

_AsyncPGVectorStore_

_async classmethod _afrom\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_,     _\*\* kwargs: Any_, \) → AsyncPGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.afrom_texts)\#     

Create an AsyncPGVectorStore instance from texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – Texts to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **metadatas** \(_Optional_ _\[__list_ _\[__dict_ _\]__\]_\) – List of metadatas to add to table records.

  * **ids** \(_list_ _|__None_\) – \(Optional\[list\[str\]\]\): List of IDs to add to table records.

  * **content\_column** \(_str_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]_\) – Column\(s\) that represent a document’s metadata.

  * **ignore\_metadata\_columns** \(_list_ _\[__str_ _\]_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **schema\_name** \(_str_\)

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") _|__None_\)

  * **kwargs** \(_Any_\)

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Returns:     

AsyncPGVectorStore

Return type:     

_AsyncPGVectorStore_

_async _aget\_by\_ids\(

    _ids : Sequence\[str\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.aget_by_ids)\#     

Get documents by ids.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\(

    _query : str_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **fetch\_k** \(_int_ _|__None_\)

  * **lambda\_mult** \(_float_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **fetch\_k** \(_int_ _|__None_\)

  * **lambda\_mult** \(_float_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.amax_marginal_relevance_search_with_score_by_vector)\#     

Return docs and distance scores selected using the maximal marginal relevance.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **fetch\_k** \(_int_ _|__None_\)

  * **lambda\_mult** \(_float_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _areindex\(

    _index\_name : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.areindex)\#     

Re-index the vector store table.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

None

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.asimilarity_search)\#     

Return docs selected by similarity search on query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.asimilarity_search_by_vector)\#     

Return docs selected by vector similarity search.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.asimilarity_search_with_score)\#     

Return docs and distance scores selected by similarity search on query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.asimilarity_search_with_score_by_vector)\#     

Return docs and distance scores selected by vector similarity search.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async classmethod _create\(

    _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _embedding\_service : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _table\_name : str_,     _\*_ ,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str | None = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \) → AsyncPGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.create)\#     

Create an AsyncPGVectorStore instance.

Parameters:     

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **embedding\_service** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **schema\_name** \(_str_ _,__optional_\) – Name of the database schema. Defaults to “public”.

  * **content\_column** \(_str_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]_\) – Column\(s\) that represent a document’s metadata.

  * **ignore\_metadata\_columns** \(_list_ _\[__str_ _\]_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Defaults to None.

Returns:     

AsyncPGVectorStore

Return type:     

_AsyncPGVectorStore_

delete\(

    _ids : list | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.delete)\#     

Delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_list_ _|__None_\) – List of ids to delete. If None, delete all. Default is None.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

_classmethod _from\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _\*\* kwargs: Any_, \) → AsyncPGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.from_documents)\#     

Return VectorStore initialized from documents and embeddings.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\)

  * **table\_name** \(_str_\)

  * **ids** \(_list_ _|__None_\)

  * **content\_column** \(_str_\)

  * **embedding\_column** \(_str_\)

  * **metadata\_columns** \(_list_ _\[__str_ _\]__|__None_\)

  * **ignore\_metadata\_columns** \(_list_ _\[__str_ _\]__|__None_\)

  * **id\_column** \(_str_\)

  * **metadata\_json\_column** \(_str_\)

Returns:     

VectorStore initialized from documents and embeddings.

Return type:     

[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")

_classmethod _from\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _\*\* kwargs: Any_, \) → AsyncPGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.from_texts)\#     

Return VectorStore initialized from texts and embeddings.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** \(_list_ _|__None_\) – Optional list of IDs associated with the texts.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\)

  * **table\_name** \(_str_\)

  * **content\_column** \(_str_\)

  * **embedding\_column** \(_str_\)

  * **metadata\_columns** \(_list_ _\[__str_ _\]__|__None_\)

  * **ignore\_metadata\_columns** \(_list_ _\[__str_ _\]__|__None_\)

  * **id\_column** \(_str_\)

  * **metadata\_json\_column** \(_str_\)

Returns:     

VectorStore initialized from texts and embeddings.

Return type:     

[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")

get\_by\_ids\(

    _ids : Sequence\[str\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.get_by_ids)\#     

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

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Added in version 0.2.11.

_async _is\_valid\_index\(

    _index\_name : str | None = None_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.is_valid_index)\#     

Check if index exists in the table.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

bool

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _|__None_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_ _|__None_\) – Number of Documents to fetch to pass to MMR algorithm. Default is 20.

  * **lambda\_mult** \(_float_ _|__None_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_ _|__None_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_ _|__None_\) – Number of Documents to fetch to pass to MMR algorithm. Default is 20.

  * **lambda\_mult** \(_float_ _|__None_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.max_marginal_relevance_search_with_score_by_vector)\#     

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **fetch\_k** \(_int_ _|__None_\)

  * **lambda\_mult** \(_float_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_ _|__None_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents most similar to the query.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_ _|__None_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents most similar to the query vector.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.similarity_search_with_score)\#     

Run similarity search with distance.

Parameters:     

  * **\*args** – Arguments to pass to the search method.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/async_vectorstore.html#AsyncPGVectorStore.similarity_search_with_score_by_vector)\#     

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)