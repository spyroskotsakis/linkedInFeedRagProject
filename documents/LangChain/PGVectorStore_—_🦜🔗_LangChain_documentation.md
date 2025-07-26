# PGVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.vectorstores.PGVectorStore.html
**Word Count:** 2389
**Links Count:** 399
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# PGVectorStore\#

_class _langchain\_postgres.v2.vectorstores.PGVectorStore\(

    _key : object_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _vs : [AsyncPGVectorStore](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore.html#langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore "langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore)\#     

Postgres Vector Store class

PGVectorStore constructor. :param key: Prevent direct constructor usage. :type key: object :param engine: Connection pool engine for managing connections to Postgres database. :type engine: PGEngine :param vs: The async only VectorStore implementation :type vs: AsyncPGVectorStore

Raises:     

**Exception** – If called directly by user.

Parameters:     

  * **key** \(_object_\)

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\)

  * **vs** \([_AsyncPGVectorStore_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore.html#langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore "langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore")\)

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(key, engine, vs\) | PGVectorStore constructor.   ---|---   `aadd_documents`\(documents\[, ids\]\) | Embed documents and add to the table.   `aadd_embeddings`\(texts, embeddings\[, ...\]\) | Add data along with embeddings to the table.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Embed texts and add to the table.   `aapply_vector_index`\(index\[, name, concurrently\]\) | Create an index on the vector store table.   `add_documents`\(documents\[, ids\]\) | Embed documents and add to the table.   `add_embeddings`\(texts, embeddings\[, ...\]\) | Add data along with embeddings to the table.   `add_texts`\(texts\[, metadatas, ids\]\) | Embed texts and add to the table.   `adelete`\(\[ids\]\) | Delete records from the table.   `adrop_vector_index`\(\[index\_name\]\) | Drop the vector index.   `afrom_documents`\(documents, embedding, ...\[, ...\]\) | Create an PGVectorStore instance from documents.   `afrom_texts`\(texts, embedding, engine, table\_name\) | Create an PGVectorStore instance from texts.   `aget_by_ids`\(ids\) | Get documents by ids.   `ais_valid_index`\(\[index\_name\]\) | Check if index exists in the table.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs and distance scores selected using the maximal marginal relevance.   `apply_vector_index`\(index\[, name, concurrently\]\) | Create an index on the vector store table.   `areindex`\(\[index\_name\]\) | Re-index the vector store table.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter\]\) | Return docs selected by similarity search on query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs selected by vector similarity search.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, filter\]\) | Return docs and distance scores selected by similarity search on query.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs and distance scores selected by vector similarity search.   `create`\(engine, embedding\_service, table\_name\) | Create an PGVectorStore instance.   `create_sync`\(engine, embedding\_service, ...\) | Create an PGVectorStore instance.   `delete`\(\[ids\]\) | Delete records from the table.   `drop_vector_index`\(\[index\_name\]\) | Drop the vector index.   `from_documents`\(documents, embedding, engine, ...\) | Create an PGVectorStore instance from documents.   `from_texts`\(texts, embedding, engine, table\_name\) | Create an PGVectorStore instance from texts.   `get_by_ids`\(ids\) | Get documents by ids.   `get_table_name`\(\) |    `is_valid_index`\(\[index\_name\]\) | Check if index exists in the table.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs and distance scores selected using the maximal marginal relevance.   `reindex`\(\[index\_name\]\) | Re-index the vector store table.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Return docs selected by similarity search on query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs selected by vector similarity search.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, filter\]\) | Return docs and distance scores selected by similarity search on query.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs and distance scores selected by similarity search on vector.      \_\_init\_\_\(

    _key : object_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _vs : [AsyncPGVectorStore](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore.html#langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore "langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.__init__)\#     

PGVectorStore constructor. :param key: Prevent direct constructor usage. :type key: object :param engine: Connection pool engine for managing connections to Postgres database. :type engine: PGEngine :param vs: The async only VectorStore implementation :type vs: AsyncPGVectorStore

Raises:     

**Exception** – If called directly by user.

Parameters:     

  * **key** \(_object_\)

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\)

  * **vs** \([_AsyncPGVectorStore_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore.html#langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore "langchain_postgres.v2.async_vectorstore.AsyncPGVectorStore")\)

_async _aadd\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.aadd_documents)\#     

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

    _texts : Iterable\[str\]_,     _embeddings : list\[list\[float\]\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.aadd_embeddings)\#     

Add data along with embeddings to the table.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **embeddings** \(_list_ _\[__list_ _\[__float_ _\]__\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_list_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.aadd_texts)\#     

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

_async _aapply\_vector\_index\(

    _index : [BaseIndex](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html#langchain_postgres.v2.indexes.BaseIndex "langchain_postgres.v2.indexes.BaseIndex")_,     _name : str | None = None_,     _concurrently : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.aapply_vector_index)\#     

Create an index on the vector store table.

Parameters:     

  * **index** \([_BaseIndex_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html#langchain_postgres.v2.indexes.BaseIndex "langchain_postgres.v2.indexes.BaseIndex")\)

  * **name** \(_str_ _|__None_\)

  * **concurrently** \(_bool_\)

Return type:     

None

add\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.add_documents)\#     

Embed documents and add to the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

add\_embeddings\(

    _texts : Iterable\[str\]_,     _embeddings : list\[list\[float\]\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.add_embeddings)\#     

Add data along with embeddings to the table.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **embeddings** \(_list_ _\[__list_ _\[__float_ _\]__\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_list_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.add_texts)\#     

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

_async _adelete\(

    _ids : list | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.adelete)\#     

Delete records from the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

bool | None

_async _adrop\_vector\_index\(

    _index\_name : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.adrop_vector_index)\#     

Drop the vector index.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

None

_async classmethod _afrom\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _schema\_name : str = 'public'_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_,     _\*\* kwargs: Any_, \) → PGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.afrom_documents)\#     

Create an PGVectorStore instance from documents.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **schema\_name** \(_str_ _,__optional_\) – Name of the database schema. Defaults to “public”.

  * **ids** \(_list_ _|__None_\) – \(Optional\[list\]\): List of IDs to add to table records. Defaults to None.

  * **content\_column** \(_str_ _,__optional_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_ _,__optional_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]__,__optional_\) – Column\(s\) that represent a document’s metadata. Defaults to an empty list.

  * **ignore\_metadata\_columns** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_ _,__optional_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_ _,__optional_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Defaults to None.

  * **kwargs** \(_Any_\)

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Returns:     

PGVectorStore

Return type:     

_PGVectorStore_

_async classmethod _afrom\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _schema\_name : str = 'public'_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_,     _\*\* kwargs: Any_, \) → PGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.afrom_texts)\#     

Create an PGVectorStore instance from texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – Texts to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **schema\_name** \(_str_ _,__optional_\) – Name of the database schema. Defaults to “public”.

  * **metadatas** \(_Optional_ _\[__list_ _\[__dict_ _\]__\]__,__optional_\) – List of metadatas to add to table records. Defaults to None.

  * **ids** \(_list_ _|__None_\) – \(Optional\[list\]\): List of IDs to add to table records. Defaults to None.

  * **content\_column** \(_str_ _,__optional_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_ _,__optional_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]__,__optional_\) – Column\(s\) that represent a document’s metadata. Defaults to an empty list.

  * **ignore\_metadata\_columns** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_ _,__optional_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_ _,__optional_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Defaults to None.

  * **kwargs** \(_Any_\)

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Returns:     

PGVectorStore

Return type:     

_PGVectorStore_

_async _aget\_by\_ids\(

    _ids : Sequence\[str\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.aget_by_ids)\#     

Get documents by ids.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ais\_valid\_index\(

    _index\_name : str | None = None_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.ais_valid_index)\#     

Check if index exists in the table.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

bool

_async _amax\_marginal\_relevance\_search\(

    _query : str_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.amax_marginal_relevance_search)\#     

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

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.amax_marginal_relevance_search_by_vector)\#     

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

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.amax_marginal_relevance_search_with_score_by_vector)\#     

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

apply\_vector\_index\(

    _index : [BaseIndex](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html#langchain_postgres.v2.indexes.BaseIndex "langchain_postgres.v2.indexes.BaseIndex")_,     _name : str | None = None_,     _concurrently : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.apply_vector_index)\#     

Create an index on the vector store table.

Parameters:     

  * **index** \([_BaseIndex_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.BaseIndex.html#langchain_postgres.v2.indexes.BaseIndex "langchain_postgres.v2.indexes.BaseIndex")\)

  * **name** \(_str_ _|__None_\)

  * **concurrently** \(_bool_\)

Return type:     

None

_async _areindex\(

    _index\_name : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.areindex)\#     

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.asimilarity_search)\#     

Return docs selected by similarity search on query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.asimilarity_search_by_vector)\#     

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.asimilarity_search_with_score)\#     

Return docs and distance scores selected by similarity search on query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.asimilarity_search_with_score_by_vector)\#     

Return docs and distance scores selected by vector similarity search.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async classmethod _create\(

    _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _embedding\_service : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _table\_name : str_,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str | None = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \) → PGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.create)\#     

Create an PGVectorStore instance.

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

PGVectorStore

Return type:     

_PGVectorStore_

_classmethod _create\_sync\(

    _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _embedding\_service : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _table\_name : str_,     _schema\_name : str = 'public'_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_, \) → PGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.create_sync)\#     

Create an PGVectorStore instance.

Parameters:     

  * **key** \(_object_\) – Prevent direct constructor usage.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **embedding\_service** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **schema\_name** \(_str_ _,__optional_\) – Name of the database schema. Defaults to “public”.

  * **content\_column** \(_str_ _,__optional_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_ _,__optional_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]__,__optional_\) – Column\(s\) that represent a document’s metadata. Defaults to None.

  * **ignore\_metadata\_columns** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_ _,__optional_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_ _,__optional_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _,__optional_\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_ _,__optional_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_ _,__optional_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \(_Optional_ _\[_[_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") _\]__,__optional_\) – Index query option. Defaults to None.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Defaults to None.

Returns:     

PGVectorStore

Return type:     

_PGVectorStore_

delete\(

    _ids : list | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.delete)\#     

Delete records from the table.

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Parameters:     

  * **ids** \(_list_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

bool | None

drop\_vector\_index\(

    _index\_name : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.drop_vector_index)\#     

Drop the vector index.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

None

_classmethod _from\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _schema\_name : str = 'public'_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_,     _\*\* kwargs: Any_, \) → PGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.from_documents)\#     

Create an PGVectorStore instance from documents.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **schema\_name** \(_str_ _,__optional_\) – Name of the database schema. Defaults to “public”.

  * **ids** \(_list_ _|__None_\) – \(Optional\[list\]\): List of IDs to add to table records. Defaults to None.

  * **content\_column** \(_str_ _,__optional_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_ _,__optional_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]__,__optional_\) – Column\(s\) that represent a document’s metadata. Defaults to an empty list.

  * **ignore\_metadata\_columns** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_ _,__optional_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_ _,__optional_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Defaults to None.

  * **kwargs** \(_Any_\)

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Returns:     

PGVectorStore

Return type:     

_PGVectorStore_

_classmethod _from\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _engine : [PGEngine](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")_,     _table\_name : str_,     _schema\_name : str = 'public'_,     _metadatas : list\[dict\] | None = None_,     _ids : list | None = None_,     _content\_column : str = 'content'_,     _embedding\_column : str = 'embedding'_,     _metadata\_columns : list\[str\] | None = None_,     _ignore\_metadata\_columns : list\[str\] | None = None_,     _id\_column : str = 'langchain\_id'_,     _metadata\_json\_column : str = 'langchain\_metadata'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html#langchain_postgres.v2.indexes.DistanceStrategy "langchain_postgres.v2.indexes.DistanceStrategy") = DistanceStrategy.COSINE\_DISTANCE_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _index\_query\_options : [QueryOptions](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions") | None = None_,     _hybrid\_search\_config : [HybridSearchConfig](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig") | None = None_,     _\*\* kwargs: Any_, \) → PGVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.from_texts)\#     

Create an PGVectorStore instance from texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – Texts to add to the vector store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Text embedding model to use.

  * **engine** \([_PGEngine_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.engine.PGEngine.html#langchain_postgres.v2.engine.PGEngine "langchain_postgres.v2.engine.PGEngine")\) – Connection pool engine for managing connections to postgres database.

  * **table\_name** \(_str_\) – Name of an existing table.

  * **schema\_name** \(_str_ _,__optional_\) – Name of the database schema. Defaults to “public”.

  * **metadatas** \(_Optional_ _\[__list_ _\[__dict_ _\]__\]__,__optional_\) – List of metadatas to add to table records. Defaults to None.

  * **ids** \(_list_ _|__None_\) – \(Optional\[list\]\): List of IDs to add to table records. Defaults to None.

  * **content\_column** \(_str_ _,__optional_\) – Column that represent a Document’s page\_content. Defaults to “content”.

  * **embedding\_column** \(_str_ _,__optional_\) – Column for embedding vectors. The embedding is generated from the document value. Defaults to “embedding”.

  * **metadata\_columns** \(_list_ _\[__str_ _\]__,__optional_\) – Column\(s\) that represent a document’s metadata. Defaults to empty list.

  * **ignore\_metadata\_columns** \(_Optional_ _\[__list_ _\[__str_ _\]__\]__,__optional_\) – Column\(s\) to ignore in pre-existing tables for a document’s metadata. Can not be used with metadata\_columns. Defaults to None.

  * **id\_column** \(_str_ _,__optional_\) – Column that represents the Document’s id. Defaults to “langchain\_id”.

  * **metadata\_json\_column** \(_str_ _,__optional_\) – Column to store metadata as JSON. Defaults to “langchain\_metadata”.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – Distance strategy to use for vector similarity search. Defaults to COSINE\_DISTANCE.

  * **k** \(_int_\) – Number of Documents to return from search. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **index\_query\_options** \([_QueryOptions_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.QueryOptions.html#langchain_postgres.v2.indexes.QueryOptions "langchain_postgres.v2.indexes.QueryOptions")\) – Index query option.

  * **hybrid\_search\_config** \([_HybridSearchConfig_](https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html#langchain_postgres.v2.hybrid_search_config.HybridSearchConfig "langchain_postgres.v2.hybrid_search_config.HybridSearchConfig")\) – Hybrid search configuration. Defaults to None.

  * **kwargs** \(_Any_\)

Raises:     

**InvalidTextRepresentationError <asyncpg.exceptions.InvalidTextRepresentationError>** – if the ids data type does not match that of the id\_column.

Returns:     

PGVectorStore

Return type:     

_PGVectorStore_

get\_by\_ids\(

    _ids : Sequence\[str\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.get_by_ids)\#     

Get documents by ids.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_table\_name\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.get_table_name)\#     

Return type:     

str

is\_valid\_index\(

    _index\_name : str | None = None_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.is_valid_index)\#     

Check if index exists in the table.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

bool

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.max_marginal_relevance_search)\#     

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

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.max_marginal_relevance_search_by_vector)\#     

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

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _fetch\_k : int | None = None_,     _lambda\_mult : float | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.max_marginal_relevance_search_with_score_by_vector)\#     

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

reindex\(_index\_name : str | None = None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.reindex)\#     

Re-index the vector store table.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

None

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.similarity_search)\#     

Return docs selected by similarity search on query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.similarity_search_by_vector)\#     

Return docs selected by vector similarity search.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.similarity_search_with_score)\#     

Return docs and distance scores selected by similarity search on query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/vectorstores.html#PGVectorStore.similarity_search_with_score_by_vector)\#     

Return docs and distance scores selected by similarity search on vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page