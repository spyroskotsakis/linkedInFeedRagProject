# PGVector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.PGVector.html
**Word Count:** 2815
**Links Count:** 395
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# PGVector\#

_class _langchain\_postgres.vectorstores.PGVector\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _connection : None | Engine | str | AsyncEngine = None_,     _embedding\_length : int | None = None_,     _collection\_name : str = 'langchain'_,     _collection\_metadata : dict | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _pre\_delete\_collection : bool = False_,     _logger : Logger | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _engine\_args : dict\[str, Any\] | None = None_,     _use\_jsonb : bool = True_,     _create\_extension : bool = True_,     _async\_mode : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector)\#     

Postgres vector store integration.

Setup:     

Install `langchain_postgres` and run the docker container.               pip install -qU langchain-postgres     docker run --name pgvector-container -e POSTGRES_USER=langchain -e POSTGRES_PASSWORD=langchain -e POSTGRES_DB=langchain -p 6024:5432 -d pgvector/pgvector:pg16     

Key init args — indexing params:     

collection\_name: str     

Name of the collection.

embeddings: Embeddings     

Embedding function to use.

Key init args — client params:     

connection: Union\[None, DBConnection, Engine, AsyncEngine, str\]     

Connection string or engine.

Instantiate:                    from langchain_postgres.vectorstores import PGVector     from langchain_openai import OpenAIEmbeddings          # See docker command above to launch a postgres instance with pgvector enabled.     connection = "postgresql+psycopg://langchain:langchain@localhost:6024/langchain"  # Uses psycopg3!     collection_name = "my_docs"          vector_store = PGVector(         embeddings=OpenAIEmbeddings(model="text-embedding-3-large"),         collection_name=collection_name,         connection=connection,         use_jsonb=True,     )     

Add Documents:                    from langchain_core.documents import Document          document_1 = Document(page_content="foo", metadata={"baz": "bar"})     document_2 = Document(page_content="thud", metadata={"bar": "baz"})     document_3 = Document(page_content="i will be deleted :(")          documents = [document_1, document_2, document_3]     ids = ["1", "2", "3"]     vector_store.add_documents(documents=documents, ids=ids)     

Delete Documents:                    vector_store.delete(ids=["3"])     

Search:                    results = vector_store.similarity_search(query="thud",k=1)     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'bar': 'baz'}]     

Search with filter:                    results = vector_store.similarity_search(query="thud",k=1,filter={"bar": "baz"})     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'bar': 'baz'}]     

Search with score:                    results = vector_store.similarity_search_with_score(query="qux",k=1)     for doc, score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.499243] foo [{'baz': 'bar'}]     

Async:                    # add documents     # await vector_store.aadd_documents(documents=documents, ids=ids)          # delete documents     # await vector_store.adelete(ids=["3"])          # search     # results = vector_store.asimilarity_search(query="thud",k=1)          # search with score     results = await vector_store.asimilarity_search_with_score(query="qux",k=1)     for doc,score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.499243] foo [{'baz': 'bar'}]     

Use as Retriever:                    retriever = vector_store.as_retriever(         search_type="mmr",         search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},     )     retriever.invoke("thud")                    [Document(metadata={'bar': 'baz'}, page_content='thud')]     

Initialize the PGVector store. For an async version, use PGVector.acreate\(\) instead.

Parameters:     

  * **connection** \(_Union_ _\[__None_ _,__DBConnection_ _,__Engine_ _,__AsyncEngine_ _,__str_ _\]_\) – Postgres connection string or \(async\)engine.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **embedding\_length** \(_Optional_ _\[__int_ _\]_\) – The length of the embedding vector. \(default: None\) NOTE: This is not mandatory. Defining it will prevent vectors of any other size to be added to the embeddings table but, without it, the embeddings can’t be indexed.

  * **collection\_name** \(_str_\) – The name of the collection to use. \(default: langchain\) NOTE: This is not the name of the table, but the name of the collection. The tables will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\) – The distance strategy to use. \(default: COSINE\)

  * **pre\_delete\_collection** \(_bool_\) – If True, will delete the collection if it exists. \(default: False\). Useful for testing.

  * **engine\_args** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\) – SQLAlchemy’s create engine arguments.

  * **use\_jsonb** \(_bool_\) – Use JSONB instead of JSON for metadata. \(default: True\) Strongly discouraged from using JSON as it’s not as efficient for querying. It’s provided here for backwards compatibility with older versions, and will be removed in the future.

  * **create\_extension** \(_bool_\) – If True, will create the vector extension if it doesn’t exist. disabling creation is useful when using ReadOnly Databases.

  * **collection\_metadata** \(_Optional_ _\[__dict_ _\]_\)

  * **logger** \(_Optional_ _\[__logging.Logger_ _\]_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

  * **async\_mode** \(_bool_\)

Attributes

`distance_strategy` |    ---|---   `embeddings` | Access the query embedding object if available.      Methods

`__init__`\(embeddings, \*\[, connection, ...\]\) | Initialize the PGVector store.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_embeddings`\(texts, embeddings\[, ...\]\) | Async add embeddings to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `acreate_collection`\(\) |    `acreate_tables_if_not_exists`\(\) |    `acreate_vector_extension`\(\) |    `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(texts, embeddings\[, ...\]\) | Add embeddings to the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids, collection\_only\]\) | Async delete vectors by ids or uuids.   `adelete_collection`\(\) |    `adrop_tables`\(\) |    `afrom_documents`\(documents, embedding\[, ...\]\) | Return VectorStore initialized from documents and embeddings.   `afrom_embeddings`\(text\_embeddings, embedding\) | Construct PGVector wrapper from raw documents and pre- generated embeddings.   `afrom_existing_index`\(embedding, \*\[, ...\]\) | Get instance of an existing PGVector store.This method will return the instance of the store without inserting any new embeddings   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Return VectorStore initialized from documents and embeddings.   `aget_by_ids`\(ids, /\) | Get documents by ids.   `aget_collection`\(session\) |    `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance   `amax_marginal_relevance_search_with_score`\(query\) | Return docs selected using the maximal marginal relevance with score.   `amax_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance with score   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter\]\) | Run similarity search with PGVector with distance.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, filter\]\) | Return docs most similar to query.   `asimilarity_search_with_score_by_vector`\(...\) |    `connection_string_from_db_params`\(driver, ...\) | Return connection string from database parameters.   `create_collection`\(\) |    `create_tables_if_not_exists`\(\) |    `create_vector_extension`\(\) |    `delete`\(\[ids, collection\_only\]\) | Delete vectors by ids or uuids.   `delete_collection`\(\) |    `drop_tables`\(\) |    `from_documents`\(documents, embedding, \*\[, ...\]\) | Return VectorStore initialized from documents and embeddings.   `from_embeddings`\(text\_embeddings, embedding, \*\) | Construct PGVector wrapper from raw documents and embeddings.   `from_existing_index`\(embedding, \*\[, ...\]\) | Get instance of an existing PGVector store.This method will return the instance of the store without inserting any new embeddings   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Return VectorStore initialized from documents and embeddings.   `get_by_ids`\(ids, /\) | Get documents by ids.   `get_collection`\(session\) |    `get_connection_string`\(kwargs\) |    `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance   `max_marginal_relevance_search_with_score`\(query\) | Return docs selected using the maximal marginal relevance with score.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance with score   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Run similarity search with PGVector with distance.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, filter\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) |       \_\_init\_\_\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _connection : None | Engine | str | AsyncEngine = None_,     _embedding\_length : int | None = None_,     _collection\_name : str = 'langchain'_,     _collection\_metadata : dict | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _pre\_delete\_collection : bool = False_,     _logger : Logger | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _engine\_args : dict\[str, Any\] | None = None_,     _use\_jsonb : bool = True_,     _create\_extension : bool = True_,     _async\_mode : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.__init__)\#     

Initialize the PGVector store. For an async version, use PGVector.acreate\(\) instead.

Parameters:     

  * **connection** \(_None_ _|__Engine_ _|__str_ _|__AsyncEngine_\) – Postgres connection string or \(async\)engine.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **embedding\_length** \(_int_ _|__None_\) – The length of the embedding vector. \(default: None\) NOTE: This is not mandatory. Defining it will prevent vectors of any other size to be added to the embeddings table but, without it, the embeddings can’t be indexed.

  * **collection\_name** \(_str_\) – The name of the collection to use. \(default: langchain\) NOTE: This is not the name of the table, but the name of the collection. The tables will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\) – The distance strategy to use. \(default: COSINE\)

  * **pre\_delete\_collection** \(_bool_\) – If True, will delete the collection if it exists. \(default: False\). Useful for testing.

  * **engine\_args** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – SQLAlchemy’s create engine arguments.

  * **use\_jsonb** \(_bool_\) – Use JSONB instead of JSON for metadata. \(default: True\) Strongly discouraged from using JSON as it’s not as efficient for querying. It’s provided here for backwards compatibility with older versions, and will be removed in the future.

  * **create\_extension** \(_bool_\) – If True, will create the vector extension if it doesn’t exist. disabling creation is useful when using ReadOnly Databases.

  * **collection\_metadata** \(_dict_ _|__None_\)

  * **logger** \(_Logger_ _|__None_\)

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\)

  * **async\_mode** \(_bool_\)

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

_async _aadd\_embeddings\(

    _texts : Sequence\[str\]_,     _embeddings : List\[List\[float\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.aadd_embeddings)\#     

Async add embeddings to the vectorstore.

Parameters:     

  * **texts** \(_Sequence_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\) – List of list of embedding vectors.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – List of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids for the texts. If not provided, will generate a new id for each text.

  * **kwargs** \(_Any_\) – vectorstore specific parameters

Return type:     

_List_\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.aadd_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids for the texts. If not provided, will generate a new id for each text.

  * **kwargs** \(_Any_\) – vectorstore specific parameters

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async _acreate\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.acreate_collection)\#     

Return type:     

None

_async _acreate\_tables\_if\_not\_exists\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.acreate_tables_if_not_exists)\#     

Return type:     

None

_async _acreate\_vector\_extension\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.acreate_vector_extension)\#     

Return type:     

None

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

    _texts : Sequence\[str\]_,     _embeddings : List\[List\[float\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.add_embeddings)\#     

Add embeddings to the vectorstore.

Parameters:     

  * **texts** \(_Sequence_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\) – List of list of embedding vectors.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – List of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids for the documents. If not provided, will generate a new id for each document.

  * **kwargs** \(_Any_\) – vectorstore specific parameters

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids for the texts. If not provided, will generate a new id for each text.

  * **kwargs** \(_Any_\) – vectorstore specific parameters

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _collection\_only : bool = False_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.adelete)\#     

Async delete vectors by ids or uuids.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **collection\_only** \(_bool_\) – Only delete ids in the collection.

  * **kwargs** \(_Any_\)

Return type:     

None

_async _adelete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.adelete_collection)\#     

Return type:     

None

_async _adrop\_tables\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.adrop_tables)\#     

Return type:     

None

_async classmethod _afrom\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*_ ,     _use\_jsonb : bool = True_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.afrom_documents)\#     

Return VectorStore initialized from documents and embeddings. Postgres connection string is required “Either pass it as a parameter or set the PGVECTOR\_CONNECTION\_STRING environment variable.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **use\_jsonb** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

_async classmethod _afrom\_embeddings\(

    _text\_embeddings : List\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.afrom_embeddings)\#     

Construct PGVector wrapper from raw documents and pre- generated embeddings.

Return VectorStore initialized from documents and embeddings. Postgres connection string is required “Either pass it as a parameter or set the PGVECTOR\_CONNECTION\_STRING environment variable.

Example               from langchain_community.vectorstores import PGVector     from langchain_community.embeddings import OpenAIEmbeddings     embeddings = OpenAIEmbeddings()     text_embeddings = embeddings.embed_documents(texts)     text_embedding_pairs = list(zip(texts, text_embeddings))     faiss = PGVector.from_embeddings(text_embedding_pairs, embeddings)     

Parameters:     

  * **text\_embeddings** \(_List_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

_async classmethod _afrom\_existing\_index\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _pre\_delete\_collection : bool = False_,     _connection : Engine | str | None = None_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.afrom_existing_index)\#     

Get instance of an existing PGVector store.This method will return the instance of the store without inserting any new embeddings

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **pre\_delete\_collection** \(_bool_\)

  * **connection** \(_Engine_ _|__str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

_async classmethod _afrom\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*_ ,     _use\_jsonb : bool = True_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.afrom_texts)\#     

Return VectorStore initialized from documents and embeddings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **use\_jsonb** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

_async _aget\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.aget_by_ids)\#     

Get documents by ids.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aget\_collection\(

    _session : AsyncSession_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.aget_collection)\#     

Parameters:     

**session** \(_AsyncSession_\)

Return type:     

_Any_

_async _amax\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.amax_marginal_relevance_search)\#     

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

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.amax_marginal_relevance_search_by_vector)\#     

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

_async _amax\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.amax_marginal_relevance_search_with_score)\#     

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

_async _amax\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.amax_marginal_relevance_search_with_score_by_vector)\#     

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.asimilarity_search)\#     

Run similarity search with PGVector with distance.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.asimilarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query vector.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.asimilarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

Returns:     

List of Documents most similar to the query and score for each.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.asimilarity_search_with_score_by_vector)\#     

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_classmethod _connection\_string\_from\_db\_params\(

    _driver : str_,     _host : str_,     _port : int_,     _database : str_,     _user : str_,     _password : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.connection_string_from_db_params)\#     

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

create\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.create_collection)\#     

Return type:     

None

create\_tables\_if\_not\_exists\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.create_tables_if_not_exists)\#     

Return type:     

None

create\_vector\_extension\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.create_vector_extension)\#     

Return type:     

None

delete\(

    _ids : List\[str\] | None = None_,     _collection\_only : bool = False_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.delete)\#     

Delete vectors by ids or uuids.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **collection\_only** \(_bool_\) – Only delete ids in the collection.

  * **kwargs** \(_Any_\)

Return type:     

None

delete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.delete_collection)\#     

Return type:     

None

drop\_tables\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.drop_tables)\#     

Return type:     

None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _connection : Engine | str | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _use\_jsonb : bool = True_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.from_documents)\#     

Return VectorStore initialized from documents and embeddings.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **connection** \(_Engine_ _|__str_ _|__None_\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **use\_jsonb** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

_classmethod _from\_embeddings\(

    _text\_embeddings : List\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.from_embeddings)\#     

Construct PGVector wrapper from raw documents and embeddings.

Parameters:     

  * **text\_embeddings** \(_List_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\) – List of tuples of text and embeddings.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embeddings object.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **collection\_name** \(_str_\) – Name of the collection.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\) – Distance strategy to use.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids for the documents. If not provided, will generate a new id for each document.

  * **pre\_delete\_collection** \(_bool_\) – If True, will delete the collection if it exists. **Attention** : This will delete all the documents in the existing collection.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

PGVector instance.

Return type:     

PGVector

Example               from langchain_postgres.vectorstores import PGVector     from langchain_openai.embeddings import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     text_embeddings = embeddings.embed_documents(texts)     text_embedding_pairs = list(zip(texts, text_embeddings))     vectorstore = PGVector.from_embeddings(text_embedding_pairs, embeddings)     

_classmethod _from\_existing\_index\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _pre\_delete\_collection : bool = False_,     _connection : Engine | str | None = None_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.from_existing_index)\#     

Get instance of an existing PGVector store.This method will return the instance of the store without inserting any new embeddings

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **pre\_delete\_collection** \(_bool_\)

  * **connection** \(_Engine_ _|__str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _collection\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _use\_jsonb : bool = True_,     _\*\* kwargs: Any_, \) → PGVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.from_texts)\#     

Return VectorStore initialized from documents and embeddings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/postgres/vectorstores/langchain_postgres.vectorstores.DistanceStrategy.html#langchain_postgres.vectorstores.DistanceStrategy "langchain_postgres.vectorstores.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **use\_jsonb** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_PGVector_

get\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.get_by_ids)\#     

Get documents by ids.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _\]_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_collection\(

    _session : Session_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.get_collection)\#     

Parameters:     

**session** \(_Session_\)

Return type:     

_Any_

_classmethod _get\_connection\_string\(

    _kwargs : Dict\[str, Any\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.get_connection_string)\#     

Parameters:     

**kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

str

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.max_marginal_relevance_search)\#     

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

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.max_marginal_relevance_search_by_vector)\#     

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.max_marginal_relevance_search_with_score)\#     

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

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.max_marginal_relevance_search_with_score_by_vector)\#     

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.similarity_search)\#     

Run similarity search with PGVector with distance.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.similarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

Returns:     

List of Documents most similar to the query and score for each.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/vectorstores.html#PGVector.similarity_search_with_score_by_vector)\#     

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using PGVector

  * [PGVector](https://python.langchain.com/docs/integrations/providers/pgvector/)

  * [PGVector \(Postgres\)](https://python.langchain.com/docs/integrations/retrievers/self_query/pgvector_self_query/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)