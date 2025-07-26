# AstraDBVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBVectorStore.html
**Word Count:** 8374
**Links Count:** 454
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBVectorStore\#

_class _langchain\_astradb.vectorstores.AstraDBVectorStore\(

    _\*_ ,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _environment : str | None = None_,     _namespace : str | None = None_,     _metric : str | None = None_,     _batch\_size : int | None = None_,     _bulk\_insert\_batch\_concurrency : int | None = None_,     _bulk\_insert\_overwrite\_concurrency : int | None = None_,     _bulk\_delete\_concurrency : int | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") | None = None_,     _pre\_delete\_collection : bool = False_,     _metadata\_indexing\_include : Iterable\[str\] | None = None_,     _metadata\_indexing\_exclude : Iterable\[str\] | None = None_,     _collection\_indexing\_policy : dict\[str, Any\] | None = None_,     _collection\_vector\_service\_options : VectorServiceOptions | None = None_,     _collection\_embedding\_api\_key : str | EmbeddingHeadersProvider | None = None_,     _content\_field : str | None = None_,     _ignore\_invalid\_documents : bool = False_,     _autodetect\_collection : bool = False_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _component\_name : str = 'langchain\_vectorstore'_,     _api\_options : APIOptions | None = None_,     _collection\_rerank : CollectionRerankOptions | RerankServiceOptions | None = None_,     _collection\_reranking\_api\_key : str | RerankingHeadersProvider | None = None_,     _collection\_lexical : str | dict\[str, Any\] | CollectionLexicalOptions | None = None_,     _hybrid\_search : [HybridSearchMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.HybridSearchMode.html#langchain_astradb.utils.astradb.HybridSearchMode "langchain_astradb.utils.astradb.HybridSearchMode") | None = None_,     _hybrid\_limit\_factor : float | None | dict\[str, float\] | [HybridLimitFactorPrescription](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.HybridLimitFactorPrescription.html#langchain_astradb.vectorstores.HybridLimitFactorPrescription "langchain_astradb.vectorstores.HybridLimitFactorPrescription") = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore)\#     

A vector store which uses DataStax Astra DB as backend.

Setup:     

Install the `langchain-astradb` package and head to the [AstraDB website](https://astra.datastax.com), create an account, create a new database and [create an application token](https://docs.datastax.com/en/astra-db-serverless/administration/manage-application-tokens.html).               pip install -qU langchain-astradb     

Key init args — indexing params:     

collection\_name: str     

Name of the collection.

embedding: Embeddings     

Embedding function to use.

Key init args — client params:     

api\_endpoint: str     

Astra DB API endpoint.

token: str     

API token for Astra DB usage.

namespace: Optional\[str\]     

Namespace \(aka keyspace\) where the collection is created

Instantiate:     

Get your API endpoint and application token from the dashboard of your database.

Create a vector store and provide a LangChain embedding object for working with it:               import getpass          from langchain_astradb import AstraDBVectorStore     from langchain_openai import OpenAIEmbeddings          ASTRA_DB_API_ENDPOINT = getpass.getpass("ASTRA_DB_API_ENDPOINT = ")     ASTRA_DB_APPLICATION_TOKEN = getpass.getpass("ASTRA_DB_APPLICATION_TOKEN = ")          vector_store = AstraDBVectorStore(         collection_name="astra_vector_langchain",         embedding=OpenAIEmbeddings(),         api_endpoint=ASTRA_DB_API_ENDPOINT,         token=ASTRA_DB_APPLICATION_TOKEN,     )     

\(Vectorize\) Create a vector store where the embedding vector computation happens entirely on the server-side, using the [vectorize](https://docs.datastax.com/en/astra-db-serverless/databases/embedding-generation.html) feature:               import getpass     from astrapy.info import VectorServiceOptions          from langchain_astradb import AstraDBVectorStore          ASTRA_DB_API_ENDPOINT = getpass.getpass("ASTRA_DB_API_ENDPOINT = ")     ASTRA_DB_APPLICATION_TOKEN = getpass.getpass("ASTRA_DB_APPLICATION_TOKEN = ")          vector_store = AstraDBVectorStore(         collection_name="astra_vectorize_langchain",         api_endpoint=ASTRA_DB_API_ENDPOINT,         token=ASTRA_DB_APPLICATION_TOKEN,         collection_vector_service_options=VectorServiceOptions(             provider="nvidia",             model_name="NV-Embed-QA",             # authentication=...,  # needed by some providers/models         ),     )     

\(Hybrid\) The underlying Astra DB typically supports hybrid search \(i.e. lexical + vector ANN\) to boost the results’ accuracy. This is provisioned and used automatically when available. For manual control, use the `collection_rerank` and `collection_lexical` constructor parameters:               import getpass     from astrapy.info import (         CollectionLexicalOptions,         CollectionRerankOptions,         RerankServiceOptions,         VectorServiceOptions,     )          from langchain_astradb import AstraDBVectorStore          ASTRA_DB_API_ENDPOINT = getpass.getpass("ASTRA_DB_API_ENDPOINT = ")     ASTRA_DB_APPLICATION_TOKEN = getpass.getpass("ASTRA_DB_APPLICATION_TOKEN = ")          vector_store = AstraDBVectorStore(         collection_name="astra_vectorize_langchain",         # embedding=...,  # needed unless using 'vectorize'         api_endpoint=ASTRA_DB_API_ENDPOINT,         token=ASTRA_DB_APPLICATION_TOKEN,         collection_vector_service_options=VectorServiceOptions(...),  # see above         collection_lexical=CollectionLexicalOptions(analyzer="standard"),         collection_rerank=CollectionRerankOptions(             service=RerankServiceOptions(                 provider="nvidia",                 model_name="nvidia/llama-3.2-nv-rerankqa-1b-v2",             ),         ),         collection_reranking_api_key=...,  # if needed by the model/setup     )     

Hybrid-related server upgrades may introduce a mismatch between the store defaults and a pre-existing collection: in case one such mismatch is reported \(as a Data API “EXISTING\_COLLECTION\_DIFFERENT\_SETTINGS” error\), the options to resolve are: \(1\) use autodetect mode, \(2\) switch to `setup_mode` “OFF”, or \(3\) explicitly specify lexical and/or rerank settings in the vector store constructor, to match the existing collection configuration. See [here](https://github.com/langchain-ai/langchain-datastax/blob/main/libs/astradb/README.md#collection-defaults-mismatch) for more details.

\(Autodetect\) Let the vector store figure out the configuration \(including vectorize and document encoding scheme on DB\), by inspection of an existing collection:               import getpass          from langchain_astradb import AstraDBVectorStore          ASTRA_DB_API_ENDPOINT = getpass.getpass("ASTRA_DB_API_ENDPOINT = ")     ASTRA_DB_APPLICATION_TOKEN = getpass.getpass("ASTRA_DB_APPLICATION_TOKEN = ")          vector_store = AstraDBVectorStore(         collection_name="astra_existing_collection",         # embedding=...,  # needed unless using 'vectorize'         api_endpoint=ASTRA_DB_API_ENDPOINT,         token=ASTRA_DB_APPLICATION_TOKEN,         autodetect_collection=True,     )     

\(Non-Astra DB\) This class can also target a non-Astra DB database, such as a self-deployed HCD, through the Data API:               import getpass          from astrapy.authentication import UsernamePasswordTokenProvider          from langchain_astradb import AstraDBVectorStore          vector_store = AstraDBVectorStore(         collection_name="astra_existing_collection",         # embedding=...,  # needed unless using 'vectorize'         api_endpoint="http://localhost:8181",         token=UsernamePasswordTokenProvider(             username="user",             password="pwd",         ),         collection_vector_service_options=...,  # if 'vectorize'     )     

Add Documents:                    from langchain_core.documents import Document          document_1 = Document(page_content="foo", metadata={"baz": "bar"})     document_2 = Document(page_content="thud", metadata={"bar": "baz"})     document_3 = Document(page_content="i will be deleted :(")          documents = [document_1, document_2, document_3]     ids = ["1", "2", "3"]     vector_store.add_documents(documents=documents, ids=ids)     

Delete Documents:                    vector_store.delete(ids=["3"])     

Search:                    results = vector_store.similarity_search(query="thud",k=1)     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    thud [{'bar': 'baz'}]     

Search with filter:                    results = vector_store.similarity_search(query="thud",k=1,filter={"bar": "baz"})     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    thud [{'bar': 'baz'}]     

Search with score:                    results = vector_store.similarity_search_with_score(query="qux",k=1)     for doc, score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    [SIM=0.916135] foo [{'baz': 'bar'}]     

Async:                    # add documents     await vector_store.aadd_documents(documents=documents, ids=ids)          # delete documents     await vector_store.adelete(ids=["3"])          # search     results = vector_store.asimilarity_search(query="thud",k=1)          # search with score     results = await vector_store.asimilarity_search_with_score(query="qux",k=1)     for doc,score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    [SIM=0.916135] foo [{'baz': 'bar'}]     

Use as Retriever:                    retriever = vector_store.as_retriever(         search_type="similarity_score_threshold",         search_kwargs={"k": 1, "score_threshold": 0.5},     )     retriever.invoke("thud")                    [Document(metadata={'bar': 'baz'}, page_content='thud')]     

A vector store which uses DataStax Astra DB as backend.

For more on Astra DB, visit <https://docs.datastax.com/en/astra-db-serverless/index.html>

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – the embeddings function or service to use. This enables client-side embedding functions or calls to external embedding providers. If `embedding` is passed, then `collection_vector_service_options` can not be provided.

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of `astrapy.authentication.TokenProvider`. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as `https://<DB-ID>-us-east1.apps.astra.datastax.com`. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in `astrapy.constants.Environment` enum class.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **metric** \(_str_ _|__None_\) – similarity function to use out of those available in Astra DB. If left out, it will use Astra DB API’s defaults \(i.e. “cosine” - but, for performance reasons, “dot\_product” is suggested if embeddings are normalized to one\).

  * **batch\_size** \(_int_ _|__None_\) – Size of document chunks for each individual insertion API request. If not provided, astrapy defaults are applied.

  * **bulk\_insert\_batch\_concurrency** \(_int_ _|__None_\) – Number of threads or coroutines to insert batches concurrently.

  * **bulk\_insert\_overwrite\_concurrency** \(_int_ _|__None_\) – Number of threads or coroutines in a batch to insert pre-existing entries.

  * **bulk\_delete\_concurrency** \(_int_ _|__None_\) – Number of threads or coroutines for multiple-entry deletes.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") _|__None_\) – mode used to create the collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **metadata\_indexing\_include** \(_Iterable_ _\[__str_ _\]__|__None_\) – an allowlist of the specific metadata subfields that should be indexed for later filtering in searches.

  * **metadata\_indexing\_exclude** \(_Iterable_ _\[__str_ _\]__|__None_\) – a denylist of the specific metadata subfields that should not be indexed for later filtering in searches.

  * **collection\_indexing\_policy** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – a full “indexing” specification for what fields should be indexed for later filtering in searches. This dict must conform to to the API specifications \(see <https://docs.datastax.com/en/astra-db-serverless/api-reference/collections.html#the-indexing-option>\)

  * **collection\_vector\_service\_options** \(_VectorServiceOptions_ _|__None_\) – specifies the use of server-side embeddings within Astra DB. If passing this parameter, `embedding` cannot be provided.

  * **collection\_embedding\_api\_key** \(_str_ _|__EmbeddingHeadersProvider_ _|__None_\) – for usage of server-side embeddings within Astra DB. With this parameter one can supply an API Key that will be passed to Astra DB with each data request. This parameter can be either a string or a subclass of `astrapy.authentication.EmbeddingHeadersProvider`. This is useful when the service is configured for the collection, but no corresponding secret is stored within Astra’s key management system.

  * **content\_field** \(_str_ _|__None_\) – name of the field containing the textual content in the documents when saved on Astra DB. For vectorize collections, this cannot be specified; for non-vectorize collection, defaults to “content”. The special value “\*” can be passed only if autodetect\_collection=True. In this case, the actual name of the key for the textual content is guessed by inspection of a few documents from the collection, under the assumption that the longer strings are the most likely candidates. Please understand the limitations of this method and get some understanding of your data before passing `"*"` for this parameter.

  * **ignore\_invalid\_documents** \(_bool_\) – if False \(default\), exceptions are raised when a document is found on the Astra DB collection that does not have the expected shape. If set to True, such results from the database are ignored and a warning is issued. Note that in this case a similarity search may end up returning fewer results than the required `k`.

  * **autodetect\_collection** \(_bool_\) – if True, turns on autodetect behavior. The store will look for an existing collection of the provided name and infer the store settings from it. Default is False. In autodetect mode, `content_field` can be given as `"*"`, meaning that an attempt will be made to determine it by inspection \(unless vectorize is enabled, in which case `content_field` is ignored\). In autodetect mode, the store not only determines whether embeddings are client- or server-side, but - most importantly - switches automatically between “nested” and “flat” representations of documents on DB \(i.e. having the metadata key-value pairs grouped in a `metadata` field or spread at the documents’ top-level\). The former scheme is the native mode of the AstraDBVectorStore; the store resorts to the latter in case of vector collections populated with external means \(such as a third-party data import tool\) before applying an AstraDBVectorStore to them. Note that the following parameters cannot be used if this is True: `metric`, `setup_mode`, `metadata_indexing_include`, `metadata_indexing_exclude`, `collection_indexing_policy`, `collection_vector_service_options`.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **component\_name** \(_str_\) – the string identifying this specific component in the stack of usage info passed as the User-Agent string to the Data API. Defaults to “langchain\_vectorstore”, but can be overridden if this component actually serves as the building block for another component \(such as when the vector store is used within a `GraphRetriever`\).

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

  * **collection\_rerank** \(_CollectionRerankOptions_ _|__RerankServiceOptions_ _|__None_\) – providing reranking settings is necessary to run hybrid searches for similarity. This parameter can be an instance of the astrapy classes CollectionRerankOptions or `RerankServiceOptions`.

  * **collection\_reranking\_api\_key** \(_str_ _|__RerankingHeadersProvider_ _|__None_\) – for usage of server-side reranking services within Astra DB. With this parameter one can supply an API Key that will be passed to Astra DB with each data request. This parameter can be either a string or a subclass of `astrapy.authentication.RerankingHeadersProvider`. This is useful when the service is configured for the collection, but no corresponding secret is stored within Astra’s key management system.

  * **collection\_lexical** \(_str_ _|__dict_ _\[__str_ _,__Any_ _\]__|__CollectionLexicalOptions_ _|__None_\) – configuring a lexical analyzer is necessary to run lexical and hybrid searches. This parameter can be a string or dict, which is then passed as-is for the “analyzer” field of a createCollection’s “$lexical.analyzer” value, or a ready-made astrapy CollectionLexicalOptions object.

  * **hybrid\_search** \([_HybridSearchMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.HybridSearchMode.html#langchain_astradb.utils.astradb.HybridSearchMode "langchain_astradb.utils.astradb.HybridSearchMode") _|__None_\) – whether similarity searches should be run as Hybrid searches or not. Values are DEFAULT, ON or OFF. In case of DEFAULT, searches are performed as permitted by the collection configuration, with a preference for hybrid search. Forcing this setting to ON for a non-hybrid-enabled collection would result in a server error when running searches.

  * **hybrid\_limit\_factor** \(_float_ _|__None_ _|__dict_ _\[__str_ _,__float_ _\]__|_[_HybridLimitFactorPrescription_](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.HybridLimitFactorPrescription.html#langchain_astradb.vectorstores.HybridLimitFactorPrescription "langchain_astradb.vectorstores.HybridLimitFactorPrescription")\) – subsearch “limit” specification for hybrid searches. If omitted, hybrid searches do not specify it and leave the Data API to use its defaults. If a floating-point positive number is provided: each subsearch participating in the hybrid search \(i.e. both the vector-based ANN and the lexical-based\) will be requested to fecth up to int\(k\*hybrid\_limit\_factor\) items, where k is the desired result count from the whole search. If a HybridLimitFactorPrescription is provided \(see the class docstring for details\), separate factors are applied to the vector and the lexical subsearches. Alternatively, a simple dictionary with keys “$lexical” and “$vector” achieves the same effect.

Note

For concurrency in synchronous `add_texts()`:, as a rule of thumb, on a typical client machine it is suggested to keep the quantity bulk\_insert\_batch\_concurrency \* bulk\_insert\_overwrite\_concurrency much below 1000 to avoid exhausting the client multithreading/networking resources. The hardcoded defaults are somewhat conservative to meet most machines’ specs, but a sensible choice to test may be:

  * bulk\_insert\_batch\_concurrency = 80

  * bulk\_insert\_overwrite\_concurrency = 10

A bit of experimentation is required to nail the best results here, depending on both the machine/network specs and the expected workload \(specifically, how often a write is an update of an existing id\). Remember you can pass concurrency settings to individual calls to `add_texts()` and `add_documents()` as well.

Attributes

`embeddings` | Accesses the supplied embeddings object.   ---|---      Methods

`__init__`\(\*, collection\_name\[, embedding, ...\]\) | A vector store which uses DataStax Astra DB as backend.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, ...\]\) | Run texts through the embeddings and add them to the vectorstore.   `aclear`\(\) | Empty the collection of all its stored entries.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids, ...\]\) | Run texts through the embeddings and add them to the vectorstore.   `adelete`\(\[ids, concurrency\]\) | Delete by vector ids.   `adelete_by_document_id`\(document\_id\) | Remove a single document from the store, given its document ID.   `adelete_by_metadata_filter`\(filter\) | Delete all documents matching a certain metadata filtering condition.   `adelete_collection`\(\) | Completely delete the collection from the database.   `afrom_documents`\(documents\[, embedding\]\) | Create an Astra DB vectorstore from a document list.   `afrom_texts`\(texts\[, embedding, metadatas, ids\]\) | Create an Astra DB vectorstore from raw texts.   `aget_by_document_id`\(document\_id\) | Retrieve a single document from the store, given its document ID.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `ametadata_search`\(\[filter, n\]\) | Get documents via a metadata search.   `arun_query`\(\) | Execute a generic query on stored documents, returning Documents+other info.   `arun_query_raw`\(\) | Execute a generic query on stored documents, returning Astra DB documents.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter, ...\]\) | Return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `asimilarity_search_with_embedding`\(query\[, ...\]\) | Return docs most similar to the query with embedding.   `asimilarity_search_with_embedding_by_vector`\(...\) | Return docs most similar to embedding vector with embedding.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query with score.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs most similar to embedding vector with score.   `asimilarity_search_with_score_id`\(query\[, k, ...\]\) | Return docs most similar to the query with score and id.   `asimilarity_search_with_score_id_by_vector`\(...\) | Return docs most similar to embedding vector with score and id.   `aupdate_metadata`\(id\_to\_metadata, \*\[, ...\]\) | Add/overwrite the metadata of existing documents.   `clear`\(\) | Empty the collection of all its stored entries.   `copy`\(\*\[, token, ext\_callers, ...\]\) | Create a copy, possibly with changed attributes.   `delete`\(\[ids, concurrency\]\) | Delete by vector ids.   `delete_by_document_id`\(document\_id\) | Remove a single document from the store, given its document ID.   `delete_by_metadata_filter`\(filter\) | Delete all documents matching a certain metadata filtering condition.   `delete_collection`\(\) | Completely delete the collection from the database.   `filter_to_query`\(filter\_dict\) | Prepare a query for use on DB based on metadata filter.   `from_documents`\(documents\[, embedding\]\) | Create an Astra DB vectorstore from a document list.   `from_texts`\(texts\[, embedding, metadatas, ids\]\) | Create an Astra DB vectorstore from raw texts.   `full_decode_astra_db_found_document`\(...\) | Decode an Astra DB document in full, i.e. into Document+embedding/similarity.   `full_decode_astra_db_reranked_result`\(...\) | Full-decode an Astra DB find-and-rerank hit \(Document+embedding/similarity\).   `get_by_document_id`\(document\_id\) | Retrieve a single document from the store, given its document ID.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `metadata_search`\(\[filter, n\]\) | Get documents via a metadata search.   `run_query`\(\) | Execute a generic query on stored documents, returning Documents+other info.   `run_query_raw`\(\) | Execute a generic query on stored documents, returning Astra DB documents.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, ...\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_embedding`\(query\[, k, ...\]\) | Return docs most similar to the query with embedding.   `similarity_search_with_embedding_by_vector`\(...\) | Return docs most similar to embedding vector with embedding.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query with score.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector with score.   `similarity_search_with_score_id`\(query\[, k, ...\]\) | Return docs most similar to the query with score and id.   `similarity_search_with_score_id_by_vector`\(...\) | Return docs most similar to embedding vector with score and id.   `update_metadata`\(id\_to\_metadata, \*\[, ...\]\) | Add/overwrite the metadata of existing documents.      \_\_init\_\_\(

    _\*_ ,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _environment : str | None = None_,     _namespace : str | None = None_,     _metric : str | None = None_,     _batch\_size : int | None = None_,     _bulk\_insert\_batch\_concurrency : int | None = None_,     _bulk\_insert\_overwrite\_concurrency : int | None = None_,     _bulk\_delete\_concurrency : int | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") | None = None_,     _pre\_delete\_collection : bool = False_,     _metadata\_indexing\_include : Iterable\[str\] | None = None_,     _metadata\_indexing\_exclude : Iterable\[str\] | None = None_,     _collection\_indexing\_policy : dict\[str, Any\] | None = None_,     _collection\_vector\_service\_options : VectorServiceOptions | None = None_,     _collection\_embedding\_api\_key : str | EmbeddingHeadersProvider | None = None_,     _content\_field : str | None = None_,     _ignore\_invalid\_documents : bool = False_,     _autodetect\_collection : bool = False_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _component\_name : str = 'langchain\_vectorstore'_,     _api\_options : APIOptions | None = None_,     _collection\_rerank : CollectionRerankOptions | RerankServiceOptions | None = None_,     _collection\_reranking\_api\_key : str | RerankingHeadersProvider | None = None_,     _collection\_lexical : str | dict\[str, Any\] | CollectionLexicalOptions | None = None_,     _hybrid\_search : [HybridSearchMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.HybridSearchMode.html#langchain_astradb.utils.astradb.HybridSearchMode "langchain_astradb.utils.astradb.HybridSearchMode") | None = None_,     _hybrid\_limit\_factor : float | None | dict\[str, float\] | [HybridLimitFactorPrescription](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.HybridLimitFactorPrescription.html#langchain_astradb.vectorstores.HybridLimitFactorPrescription "langchain_astradb.vectorstores.HybridLimitFactorPrescription") = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.__init__)\#     

A vector store which uses DataStax Astra DB as backend.

For more on Astra DB, visit <https://docs.datastax.com/en/astra-db-serverless/index.html>

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – the embeddings function or service to use. This enables client-side embedding functions or calls to external embedding providers. If `embedding` is passed, then `collection_vector_service_options` can not be provided.

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of `astrapy.authentication.TokenProvider`. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as `https://<DB-ID>-us-east1.apps.astra.datastax.com`. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in `astrapy.constants.Environment` enum class.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **metric** \(_str_ _|__None_\) – similarity function to use out of those available in Astra DB. If left out, it will use Astra DB API’s defaults \(i.e. “cosine” - but, for performance reasons, “dot\_product” is suggested if embeddings are normalized to one\).

  * **batch\_size** \(_int_ _|__None_\) – Size of document chunks for each individual insertion API request. If not provided, astrapy defaults are applied.

  * **bulk\_insert\_batch\_concurrency** \(_int_ _|__None_\) – Number of threads or coroutines to insert batches concurrently.

  * **bulk\_insert\_overwrite\_concurrency** \(_int_ _|__None_\) – Number of threads or coroutines in a batch to insert pre-existing entries.

  * **bulk\_delete\_concurrency** \(_int_ _|__None_\) – Number of threads or coroutines for multiple-entry deletes.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") _|__None_\) – mode used to create the collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **metadata\_indexing\_include** \(_Iterable_ _\[__str_ _\]__|__None_\) – an allowlist of the specific metadata subfields that should be indexed for later filtering in searches.

  * **metadata\_indexing\_exclude** \(_Iterable_ _\[__str_ _\]__|__None_\) – a denylist of the specific metadata subfields that should not be indexed for later filtering in searches.

  * **collection\_indexing\_policy** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – a full “indexing” specification for what fields should be indexed for later filtering in searches. This dict must conform to to the API specifications \(see <https://docs.datastax.com/en/astra-db-serverless/api-reference/collections.html#the-indexing-option>\)

  * **collection\_vector\_service\_options** \(_VectorServiceOptions_ _|__None_\) – specifies the use of server-side embeddings within Astra DB. If passing this parameter, `embedding` cannot be provided.

  * **collection\_embedding\_api\_key** \(_str_ _|__EmbeddingHeadersProvider_ _|__None_\) – for usage of server-side embeddings within Astra DB. With this parameter one can supply an API Key that will be passed to Astra DB with each data request. This parameter can be either a string or a subclass of `astrapy.authentication.EmbeddingHeadersProvider`. This is useful when the service is configured for the collection, but no corresponding secret is stored within Astra’s key management system.

  * **content\_field** \(_str_ _|__None_\) – name of the field containing the textual content in the documents when saved on Astra DB. For vectorize collections, this cannot be specified; for non-vectorize collection, defaults to “content”. The special value “\*” can be passed only if autodetect\_collection=True. In this case, the actual name of the key for the textual content is guessed by inspection of a few documents from the collection, under the assumption that the longer strings are the most likely candidates. Please understand the limitations of this method and get some understanding of your data before passing `"*"` for this parameter.

  * **ignore\_invalid\_documents** \(_bool_\) – if False \(default\), exceptions are raised when a document is found on the Astra DB collection that does not have the expected shape. If set to True, such results from the database are ignored and a warning is issued. Note that in this case a similarity search may end up returning fewer results than the required `k`.

  * **autodetect\_collection** \(_bool_\) – if True, turns on autodetect behavior. The store will look for an existing collection of the provided name and infer the store settings from it. Default is False. In autodetect mode, `content_field` can be given as `"*"`, meaning that an attempt will be made to determine it by inspection \(unless vectorize is enabled, in which case `content_field` is ignored\). In autodetect mode, the store not only determines whether embeddings are client- or server-side, but - most importantly - switches automatically between “nested” and “flat” representations of documents on DB \(i.e. having the metadata key-value pairs grouped in a `metadata` field or spread at the documents’ top-level\). The former scheme is the native mode of the AstraDBVectorStore; the store resorts to the latter in case of vector collections populated with external means \(such as a third-party data import tool\) before applying an AstraDBVectorStore to them. Note that the following parameters cannot be used if this is True: `metric`, `setup_mode`, `metadata_indexing_include`, `metadata_indexing_exclude`, `collection_indexing_policy`, `collection_vector_service_options`.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **component\_name** \(_str_\) – the string identifying this specific component in the stack of usage info passed as the User-Agent string to the Data API. Defaults to “langchain\_vectorstore”, but can be overridden if this component actually serves as the building block for another component \(such as when the vector store is used within a `GraphRetriever`\).

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

  * **collection\_rerank** \(_CollectionRerankOptions_ _|__RerankServiceOptions_ _|__None_\) – providing reranking settings is necessary to run hybrid searches for similarity. This parameter can be an instance of the astrapy classes CollectionRerankOptions or `RerankServiceOptions`.

  * **collection\_reranking\_api\_key** \(_str_ _|__RerankingHeadersProvider_ _|__None_\) – for usage of server-side reranking services within Astra DB. With this parameter one can supply an API Key that will be passed to Astra DB with each data request. This parameter can be either a string or a subclass of `astrapy.authentication.RerankingHeadersProvider`. This is useful when the service is configured for the collection, but no corresponding secret is stored within Astra’s key management system.

  * **collection\_lexical** \(_str_ _|__dict_ _\[__str_ _,__Any_ _\]__|__CollectionLexicalOptions_ _|__None_\) – configuring a lexical analyzer is necessary to run lexical and hybrid searches. This parameter can be a string or dict, which is then passed as-is for the “analyzer” field of a createCollection’s “$lexical.analyzer” value, or a ready-made astrapy CollectionLexicalOptions object.

  * **hybrid\_search** \([_HybridSearchMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.HybridSearchMode.html#langchain_astradb.utils.astradb.HybridSearchMode "langchain_astradb.utils.astradb.HybridSearchMode") _|__None_\) – whether similarity searches should be run as Hybrid searches or not. Values are DEFAULT, ON or OFF. In case of DEFAULT, searches are performed as permitted by the collection configuration, with a preference for hybrid search. Forcing this setting to ON for a non-hybrid-enabled collection would result in a server error when running searches.

  * **hybrid\_limit\_factor** \(_float_ _|__None_ _|__dict_ _\[__str_ _,__float_ _\]__|_[_HybridLimitFactorPrescription_](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.HybridLimitFactorPrescription.html#langchain_astradb.vectorstores.HybridLimitFactorPrescription "langchain_astradb.vectorstores.HybridLimitFactorPrescription")\) – subsearch “limit” specification for hybrid searches. If omitted, hybrid searches do not specify it and leave the Data API to use its defaults. If a floating-point positive number is provided: each subsearch participating in the hybrid search \(i.e. both the vector-based ANN and the lexical-based\) will be requested to fecth up to int\(k\*hybrid\_limit\_factor\) items, where k is the desired result count from the whole search. If a HybridLimitFactorPrescription is provided \(see the class docstring for details\), separate factors are applied to the vector and the lexical subsearches. Alternatively, a simple dictionary with keys “$lexical” and “$vector” achieves the same effect.

Return type:     

None

Note

For concurrency in synchronous `add_texts()`:, as a rule of thumb, on a typical client machine it is suggested to keep the quantity bulk\_insert\_batch\_concurrency \* bulk\_insert\_overwrite\_concurrency much below 1000 to avoid exhausting the client multithreading/networking resources. The hardcoded defaults are somewhat conservative to meet most machines’ specs, but a sensible choice to test may be:

  * bulk\_insert\_batch\_concurrency = 80

  * bulk\_insert\_overwrite\_concurrency = 10

A bit of experimentation is required to nail the best results here, depending on both the machine/network specs and the expected workload \(specifically, how often a write is an update of an existing id\). Remember you can pass concurrency settings to individual calls to `add_texts()` and `add_documents()` as well.

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

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*_ ,     _batch\_size : int | None = None_,     _batch\_concurrency : int | None = None_,     _overwrite\_concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.aadd_texts)\#     

Run texts through the embeddings and add them to the vectorstore.

If passing explicit ids, those entries whose id is in the store already will be replaced.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of ids.

  * **batch\_size** \(_int_ _|__None_\) – Size of document chunks for each individual insertion API request. If not provided, defaults to the vector-store overall defaults \(which in turn falls to astrapy defaults\).

  * **batch\_concurrency** \(_int_ _|__None_\) – number of simultaneous coroutines to process insertion batches concurrently. Defaults to the vector-store overall setting if not provided.

  * **overwrite\_concurrency** \(_int_ _|__None_\) – number of simultaneous coroutines to process pre-existing documents in each batch. Defaults to the vector-store overall setting if not provided.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Return type:     

list\[str\]

Note

The allowed field names for the metadata document attributes must obey certain rules \(such as: keys cannot start with a dollar sign and cannot be empty\). See [Naming Conventions](https://docs.datastax.com/en/astra-db-serverless/api-reference/dataapiclient.html#naming-conventions) for details.

Returns:     

The list of ids of the added texts.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_list_ _\[__str_ _\]__|__None_\)

  * **batch\_size** \(_int_ _|__None_\)

  * **batch\_concurrency** \(_int_ _|__None_\)

  * **overwrite\_concurrency** \(_int_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.aclear)\#     

Empty the collection of all its stored entries.

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

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*_ ,     _batch\_size : int | None = None_,     _batch\_concurrency : int | None = None_,     _overwrite\_concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.add_texts)\#     

Run texts through the embeddings and add them to the vectorstore.

If passing explicit ids, those entries whose id is in the store already will be replaced.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of ids.

  * **batch\_size** \(_int_ _|__None_\) – Size of document chunks for each individual insertion API request. If not provided, defaults to the vector-store overall defaults \(which in turn falls to astrapy defaults\).

  * **batch\_concurrency** \(_int_ _|__None_\) – number of threads to process insertion batches concurrently. Defaults to the vector-store overall setting if not provided.

  * **overwrite\_concurrency** \(_int_ _|__None_\) – number of threads to process pre-existing documents in each batch. Defaults to the vector-store overall setting if not provided.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Return type:     

list\[str\]

Note

The allowed field names for the metadata document attributes must obey certain rules \(such as: keys cannot start with a dollar sign and cannot be empty\). See [Naming Conventions](https://docs.datastax.com/en/astra-db-serverless/api-reference/dataapiclient.html#naming-conventions) for details.

Returns:     

The list of ids of the added texts.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_list_ _\[__str_ _\]__|__None_\)

  * **batch\_size** \(_int_ _|__None_\)

  * **batch\_concurrency** \(_int_ _|__None_\)

  * **overwrite\_concurrency** \(_int_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str\]

_async _adelete\(

    _ids : list\[str\] | None = None_,     _concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.adelete)\#     

Delete by vector ids.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **concurrency** \(_int_ _|__None_\) – max number of simultaneous coroutines for single-doc delete requests. Defaults to vector-store overall setting.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

True if deletion is \(entirely\) successful, False otherwise.

Return type:     

bool | None

_async _adelete\_by\_document\_id\(

    _document\_id : str_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.adelete_by_document_id)\#     

Remove a single document from the store, given its document ID.

Parameters:     

**document\_id** \(_str_\) – The document ID

Returns:     

True if a document has indeed been deleted, False if ID not found.

Return type:     

bool

_async _adelete\_by\_metadata\_filter\(

    _filter : dict\[str, Any\]_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.adelete_by_metadata_filter)\#     

Delete all documents matching a certain metadata filtering condition.

This operation does not use the vector embeddings in any way, it simply removes all documents whose metadata match the provided condition.

Parameters:     

**filter** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Filter on the metadata to apply. The filter cannot be empty.

Returns:     

A number expressing the amount of deleted documents.

Return type:     

int

_async _adelete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.adelete_collection)\#     

Completely delete the collection from the database.

Completely delete the collection from the database \(as opposed to `aclear()`, which empties it only\). Stored data is lost and unrecoverable, resources are freed. Use with caution.

Return type:     

None

_async classmethod _afrom\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _\*\* kwargs: Any_, \) → AstraDBVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.afrom_documents)\#     

Create an Astra DB vectorstore from a document list.

Utility method that defers to `afrom_texts()` \(see that one\).

Args: see `afrom_texts()`, except here you have to supply `documents`     

in place of `texts` and `metadatas`.

Returns:     

an `AstraDBVectorStore` vectorstore.

Parameters:     

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

AstraDBVectorStore

_async classmethod _afrom\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AstraDBVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.afrom_texts)\#     

Create an Astra DB vectorstore from raw texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – the texts to insert.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – embedding function to use.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – metadata dicts for the texts.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – ids to associate to the texts.

  * **\*\*kwargs** \(_Any_\) – you can pass any argument that you would to `aadd_texts()` and/or to the `AstraDBVectorStore` constructor \(see these methods for details\). These arguments will be routed to the respective methods as they are.

Returns:     

an `AstraDBVectorStore` vectorstore.

Return type:     

AstraDBVectorStore

_async _aget\_by\_document\_id\(

    _document\_id : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.aget_by_document_id)\#     

Retrieve a single document from the store, given its document ID.

Parameters:     

**document\_id** \(_str_\) – The document ID

Returns:     

The the document if it exists. Otherwise None.

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ametadata\_search\(

    _filter : dict\[str, Any\] | None = None_,     _n : int = 5_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.ametadata_search)\#     

Get documents via a metadata search.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – the metadata to query for.

  * **n** \(_int_\) – the maximum number of documents to return.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _arun\_query\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[False\] = False_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → AsyncIterable\[[AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.arun_query)\# _async _arun\_query\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[True\]_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → tuple\[list\[float\] | None, AsyncIterable\[[AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult")\]\]     

Execute a generic query on stored documents, returning Documents+other info.

The return value has a variable format, depending on whether the ‘sort vector’ is requested back from the server.

Only the n parameter is required. Omitting all other parameters results in a query that matches each and every document found on the collection.

The method does not expose a projection directly, which is instead automatically determined based on the invocation options.

The returned Document objects are codec-independent.

Parameters:     

  * **n** – amount of items to return. Fewer items than n may be returned if the collection has not enough matches.

  * **ids** – a list of document IDs to restrict the query to. If this is supplied, only document with an ID among the provided one will match. If further query filters are provided \(i.e. metadata\), matches must satisfy both requirements.

  * **filter** – a metadata filtering part. If provided, it must refer to metadata keys by their bare name \(such as \{“key”: 123\}\). This filter can combine nested conditions with “$or”/”$and” connectors, for example: \- \{“tag”: “a”\} \- \{“$or”: \[\{“tag”: “a”\}, “label”: “b”\]\} \- \{“$and”: \[\{“tag”: \{“$in”: \[“a”, “z”\]\}\}, “label”: “b”\]\}

  * **sort** – a ‘sort’ clause for the query, such as \{“$vector”: \[…\]\}, \{“$vectorize”: “…”\} or \{“mdkey”: 1\}. Metadata sort conditions must be expressed by their ‘bare’ name.

  * **include\_similarity** – whether to return similarity scores with each match. Requires vector sort.

  * **include\_sort\_vector** – whether to return the very query vector used for the ANN search alongside the iterable of results. Requires vector sort. Note that the shape of the return value depends on this parameter.

  * **include\_embeddings** – whether to retrieve the matches’ own embedding vectors.

Returns:     

  * if include\_sort\_vector = False, the return value is an iterable over     

the AstraDBQueryResult items returned by the query. Entries that fail the decoding step, if any, are discarded after the query, which may lead to fewer items being returned than the required n.

  * if include\_sort\_vector = True, the return value is a 2-item tuple     

\(sort\_v, results\_ite\) tuple, where: \- sort\_v is the sort vector, if requested, or None if not available. \- results\_ite is an iterable over AstraDBQueryResult items as above.

Return type:     

The shape of the return value depends on the value of include\_sort\_vector

_async _arun\_query\_raw\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[False\] = False_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → AsyncIterable\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.arun_query_raw)\# _async _arun\_query\_raw\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[True\]_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → tuple\[list\[float\] | None, AsyncIterable\[Dict\[str, Any\]\]\]     

Execute a generic query on stored documents, returning Astra DB documents.

The return value has a variable format, depending on whether the ‘sort vector’ is requested back from the server.

Only the n parameter is required. Omitting all other parameters results in a query that matches each and every document found on the collection.

The method does not expose a projection directly, which is instead automatically determined based on the invocation options.

The returned documents are exactly as they come back from Astra DB \(taking into account the projection as well\). A further step, namely subsequent invocation of the convert\_astra\_db\_document method, is required to reconstruct codec-independent Document objects. The reason for keeping the retrieval and the decoding steps separate is that a caller may want to first deduplicate/discard items, in order to convert only the items actually needed.

Parameters:     

  * **n** – amount of items to return. Fewer items than n may be returned in the following cases: \(a\) the decoding skips some raw entries from the server; \(b\) the collection has not enough matches.

  * **ids** – a list of document IDs to restrict the query to. If this is supplied, only document with an ID among the provided one will match. If further query filters are provided \(i.e. metadata\), matches must satisfy both requirements.

  * **filter** – a metadata filtering part. If provided, it must refer to metadata keys by their bare name \(such as \{“key”: 123\}\). This filter can combine nested conditions with “$or”/”$and” connectors, for example: \- \{“tag”: “a”\} \- \{“$or”: \[\{“tag”: “a”\}, “label”: “b”\]\} \- \{“$and”: \[\{“tag”: \{“$in”: \[“a”, “z”\]\}\}, “label”: “b”\]\}

  * **sort** – a ‘sort’ clause for the query, such as \{“$vector”: \[…\]\}, \{“$vectorize”: “…”\} or \{“mdkey”: 1\}. Metadata sort conditions must be expressed by their ‘bare’ name.

  * **include\_similarity** – whether to return similarity scores with each match. Requires vector sort.

  * **include\_sort\_vector** – whether to return the very query vector used for the ANN search alongside the iterable of results. Requires vector sort. Note that the shape of the return value depends on this parameter.

  * **include\_embeddings** – whether to retrieve the matches’ own embedding vectors.

Returns:     

  * if include\_sort\_vector = False, the return value is an iterable over     

Astra DB documents \(dictionaries\);

  * if include\_sort\_vector = True, the return value is a 2-item tuple     

\(sort\_v, astra\_db\_ite\) tuple, where: \- sort\_v is the sort vector, if requested, or None if not available. \- astra\_db\_ite is an iterable over Astra DB documents \(dictionaries\).

Return type:     

The shape of the return value depends on the value of include\_sort\_vector

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

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _lexical\_query : str | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **lexical\_query** \(_str_ _|__None_\) – for hybrid search, a specific query for the lexical portion of the retrieval. If omitted or empty, defaults to the same as ‘query’. If passed on a non-hybrid search, an error is raised.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents most similar to the query.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents most similar to the query vector.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_with\_embedding\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → tuple\[list\[float\], list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_with_embedding)\#     

Return docs most similar to the query with embedding.

Also includes the query embedding vector.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

\(The query embedding vector, The list of \(Document, embedding\), the most similar to the query vector.\).

Return type:     

tuple\[list\[float\], list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\]\]

_async _asimilarity\_search\_with\_embedding\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_with_embedding_by_vector)\#     

Return docs most similar to embedding vector with embedding.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

\(The query embedding vector, The list of \(Document, embedding\), the most similar to the query vector.\).

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\]

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

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _lexical\_query : str | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_with_score)\#     

Return docs most similar to query with score.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **lexical\_query** \(_str_ _|__None_\) – for hybrid search, a specific query for the lexical portion of the retrieval. If omitted or empty, defaults to the same as ‘query’. If passed on a non-hybrid search, an error is raised.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector with score.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_id\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _lexical\_query : str | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_with_score_id)\#     

Return docs most similar to the query with score and id.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **lexical\_query** \(_str_ _|__None_\) – for hybrid search, a specific query for the lexical portion of the retrieval. If omitted or empty, defaults to the same as ‘query’. If passed on a non-hybrid search, an error is raised.

Returns:     

The list of \(Document, score, id\), the most similar to the query.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

_async _asimilarity\_search\_with\_score\_id\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.asimilarity_search_with_score_id_by_vector)\#     

Return docs most similar to embedding vector with score and id.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score, id\), the most similar to the query vector.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

_async _aupdate\_metadata\(

    _id\_to\_metadata : dict\[str, dict\]_,     _\*_ ,     _overwrite\_concurrency : int | None = None_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.aupdate_metadata)\#     

Add/overwrite the metadata of existing documents.

For each document to update, the new metadata dictionary is appended to the existing metadata, overwriting individual keys that existed already.

Parameters:     

  * **id\_to\_metadata** \(_dict_ _\[__str_ _,__dict_ _\]_\) – map from the Document IDs to modify to the new metadata for updating. Keys in this dictionary that do not correspond to an existing document will be silently ignored. The values of this map are metadata dictionaries for updating the documents. Any pre-existing metadata will be merged with these entries, which take precedence on a key-by-key basis.

  * **overwrite\_concurrency** \(_int_ _|__None_\) – number of asynchronous tasks to process the updates. Defaults to the vector-store overall setting if not provided.

Returns:     

the number of documents successfully updated \(i.e. found to exist, since even an update with \{\} as the new metadata counts as successful.\)

Return type:     

int

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.clear)\#     

Empty the collection of all its stored entries.

Return type:     

None

copy\(

    _\*_ ,     _token : str | TokenProvider | None = None_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _component\_name : str | None = None_,     _collection\_embedding\_api\_key : str | EmbeddingHeadersProvider | None = None_,     _collection\_reranking\_api\_key : str | RerankingHeadersProvider | None = None_, \) → AstraDBVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.copy)\#     

Create a copy, possibly with changed attributes.

This method creates a shallow copy of this environment. If a parameter is passed and differs from None, it will replace the corresponding value in the copy.

The method allows changing only the parameters that ensure the copy is functional and does not trigger side-effects: for example, one cannot create a copy acting on a new collection. In those cases, one should create a new instance of `AstraDBVectorStore` from scratch.

Parameters:     

  * **token** \(_str_ _|__TokenProvider_ _|__None_\)

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\)

  * **component\_name** \(_str_ _|__None_\)

  * **collection\_embedding\_api\_key** \(_str_ _|__EmbeddingHeadersProvider_ _|__None_\)

  * **collection\_reranking\_api\_key** \(_str_ _|__RerankingHeadersProvider_ _|__None_\)

Return type:     

AstraDBVectorStore

token\#     

API token for Astra DB usage, either in the form of a string or a subclass of `astrapy.authentication.TokenProvider`. In order to suppress token usage in the copy, explicitly pass `astrapy.authentication.StaticTokenProvider(None)`.

ext\_callers\#     

additional custom \(caller\_name, caller\_version\) pairs to attach to the User-Agent header when issuing Data API requests.

component\_name\#     

a value for the LangChain component name to use when identifying the originator of the Data API requests.

collection\_embedding\_api\_key\#     

the API Key to supply in each Data API request if necessary. This is necessary if using the Vectorize feature and no secret is stored with the database. In order to suppress the API Key in the copy, explicitly pass `astrapy.authentication.EmbeddingAPIKeyHeaderProvider(None)`.

collection\_reranking\_api\_key\#     

for usage of server-side reranking services within Astra DB. With this parameter one can supply an API Key that will be passed to Astra DB with each data request. This parameter can be either a string or a subclass of `astrapy.authentication.RerankingHeadersProvider`. This is useful when the service is configured for the collection, but no corresponding secret is stored within Astra’s key management system.

delete\(

    _ids : list\[str\] | None = None_,     _concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.delete)\#     

Delete by vector ids.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **concurrency** \(_int_ _|__None_\) – max number of threads issuing single-doc delete requests. Defaults to vector-store overall setting.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

True if deletion is \(entirely\) successful, False otherwise.

Return type:     

bool | None

delete\_by\_document\_id\(

    _document\_id : str_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.delete_by_document_id)\#     

Remove a single document from the store, given its document ID.

Parameters:     

**document\_id** \(_str_\) – The document ID

Returns:     

True if a document has indeed been deleted, False if ID not found.

Return type:     

bool

delete\_by\_metadata\_filter\(

    _filter : dict\[str, Any\]_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.delete_by_metadata_filter)\#     

Delete all documents matching a certain metadata filtering condition.

This operation does not use the vector embeddings in any way, it simply removes all documents whose metadata match the provided condition.

Parameters:     

**filter** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Filter on the metadata to apply. The filter cannot be empty.

Returns:     

A number expressing the amount of deleted documents.

Return type:     

int

delete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.delete_collection)\#     

Completely delete the collection from the database.

Completely delete the collection from the database \(as opposed to `clear()`, which empties it only\). Stored data is lost and unrecoverable, resources are freed. Use with caution.

Return type:     

None

filter\_to\_query\(

    _filter\_dict : dict\[str, Any\] | None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.filter_to_query)\#     

Prepare a query for use on DB based on metadata filter.

Encode an “abstract” filter clause on metadata into a query filter condition aware of the collection schema choice.

Parameters:     

**filter\_dict** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – a metadata condition in the form \{“field”: “value”\} or related.

Returns:     

the corresponding mapping ready for use in queries, aware of the details of the schema used to encode the document on DB.

Return type:     

dict\[str, _Any_\]

_classmethod _from\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _\*\* kwargs: Any_, \) → AstraDBVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.from_documents)\#     

Create an Astra DB vectorstore from a document list.

Utility method that defers to `from_texts()` \(see that one\).

Parameters:     

  * **texts** – the texts to insert.

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – a list of Document objects for insertion in the store.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – the embedding function to use in the store.

  * **\*\*kwargs** \(_Any_\) – you can pass any argument that you would to `add_texts()` and/or to the `AstraDBVectorStore` constructor \(see these methods for details\). These arguments will be routed to the respective methods as they are.

Returns:     

an `AstraDBVectorStore` vectorstore.

Return type:     

AstraDBVectorStore

_classmethod _from\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → AstraDBVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.from_texts)\#     

Create an Astra DB vectorstore from raw texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – the texts to insert.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – the embedding function to use in the store.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – metadata dicts for the texts.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – ids to associate to the texts.

  * **\*\*kwargs** \(_Any_\) – you can pass any argument that you would to `add_texts()` and/or to the `AstraDBVectorStore` constructor \(see these methods for details\). These arguments will be routed to the respective methods as they are.

Returns:     

an `AstraDBVectorStore` vectorstore.

Return type:     

AstraDBVectorStore

full\_decode\_astra\_db\_found\_document\(

    _astra\_db\_document : Dict\[str, Any\]_, \) → [AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.full_decode_astra_db_found_document)\#     

Decode an Astra DB document in full, i.e. into Document+embedding/similarity.

This operation returns a representation that is independent of the codec being used in the collection \(whereas the input, a ‘raw’ Astra DB document, is codec-dependent\).

The input raw document can carry information on embedding and similarity, depending on details of the query used to retrieve it. These can be set to None in the resulf if not found.

The whole method can return a None, to signal that the codec has refused the conversion \(e.g. because the input document is deemed faulty\).

Parameters:     

**astra\_db\_document** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – a dictionary obtained through run\_query\_raw from the collection.

Returns:     

a AstraDBQueryResult named tuple with Document, id, embedding     

\(where applicable\) and similarity \(where applicable\), or an overall None if the decoding is refused by the codec.

Return type:     

[_AstraDBQueryResult_](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult") | None

full\_decode\_astra\_db\_reranked\_result\(

    _astra\_db\_reranked\_result : RerankedResult\[DocDict\]_, \) → [AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.full_decode_astra_db_reranked_result)\#     

Full-decode an Astra DB find-and-rerank hit \(Document+embedding/similarity\).

This operation returns a representation that is independent of the codec being used in the collection \(whereas the ‘document’ part of the input, a ‘raw’ Astra DB response from a find-and-rerank hybrid search, is codec-dependent\).

The input raw document is what the find\_and\_rerank Astrapy method returns, i.e. an iterable over RerankedResult objects. Missing entries \(such as the embedding\) are set to None in the resulf if not found.

The whole method can return a None, to signal that the codec has refused the conversion \(e.g. because the input document is deemed faulty\).

Parameters:     

**astra\_db\_reranked\_result** \(_RerankedResult_ _\[__DocDict_ _\]_\) – a RerankedResult obtained by a find\_and\_rerank method call on the collection.

Returns:     

a AstraDBQueryResult named tuple with Document, id, embedding     

\(where applicable\) and similarity \(where applicable\), or an overall None if the decoding is refused by the codec.

Return type:     

[AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult") | None

get\_by\_document\_id\(

    _document\_id : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.get_by_document_id)\#     

Retrieve a single document from the store, given its document ID.

Parameters:     

**document\_id** \(_str_\) – The document ID

Returns:     

The the document if it exists. Otherwise None.

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

metadata\_search\(

    _filter : dict\[str, Any\] | None = None_,     _n : int = 5_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.metadata_search)\#     

Get documents via a metadata search.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – the metadata to query for.

  * **n** \(_int_\) – the maximum number of documents to return.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

run\_query\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[False\] = False_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → Iterable\[[AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.run_query)\# run\_query\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[True\]_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → tuple\[list\[float\] | None, Iterable\[[AstraDBQueryResult](https://python.langchain.com/api_reference/astradb/vectorstores/langchain_astradb.vectorstores.AstraDBQueryResult.html#langchain_astradb.vectorstores.AstraDBQueryResult "langchain_astradb.vectorstores.AstraDBQueryResult")\]\]     

Execute a generic query on stored documents, returning Documents+other info.

The return value has a variable format, depending on whether the ‘sort vector’ is requested back from the server.

Only the n parameter is required. Omitting all other parameters results in a query that matches each and every document found on the collection.

The method does not expose a projection directly, which is instead automatically determined based on the invocation options.

The returned Document objects are codec-independent.

Parameters:     

  * **n** – amount of items to return. Fewer items than n may be returned in the following cases: \(a\) the decoding skips some raw entries from the server; \(b\) the collection has not enough matches.

  * **ids** – a list of document IDs to restrict the query to. If this is supplied, only document with an ID among the provided one will match. If further query filters are provided \(i.e. metadata\), matches must satisfy both requirements.

  * **filter** – a metadata filtering part. If provided, it must refer to metadata keys by their bare name \(such as \{“key”: 123\}\). This filter can combine nested conditions with “$or”/”$and” connectors, for example: \- \{“tag”: “a”\} \- \{“$or”: \[\{“tag”: “a”\}, “label”: “b”\]\} \- \{“$and”: \[\{“tag”: \{“$in”: \[“a”, “z”\]\}\}, “label”: “b”\]\}

  * **sort** – a ‘sort’ clause for the query, such as \{“$vector”: \[…\]\}, \{“$vectorize”: “…”\} or \{“mdkey”: 1\}. Metadata sort conditions must be expressed by their ‘bare’ name.

  * **include\_similarity** – whether to return similarity scores with each match. Requires vector sort.

  * **include\_sort\_vector** – whether to return the very query vector used for the ANN search alongside the iterable of results. Requires vector sort. Note that the shape of the return value depends on this parameter.

  * **include\_embeddings** – whether to retrieve the matches’ own embedding vectors.

Returns:     

  * if include\_sort\_vector = False, the return value is an iterable over     

the AstraDBQueryResult items returned by the query. Entries that fail the decoding step, if any, are discarded after the query, which may lead to fewer items being returned than the required n.

  * if include\_sort\_vector = True, the return value is a 2-item tuple     

\(sort\_v, results\_ite\) tuple, where: \- sort\_v is the sort vector, if requested, or None if not available. \- results\_ite is an iterable over AstraDBQueryResult items as above.

Return type:     

The shape of the return value depends on the value of include\_sort\_vector

run\_query\_raw\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[False\] = False_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → Iterable\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.run_query_raw)\# run\_query\_raw\(

    _\*_ ,     _n : int_,     _include\_sort\_vector : Literal\[True\]_,     _ids : list\[str\] | None = None_,     _filter : dict\[str, Any\] | None = None_,     _sort : dict\[str, Any\] | None = None_,     _include\_similarity : bool | None = None_,     _include\_embeddings : bool = False_, \) → tuple\[list\[float\] | None, Iterable\[Dict\[str, Any\]\]\]     

Execute a generic query on stored documents, returning Astra DB documents.

The return value has a variable format, depending on whether the ‘sort vector’ is requested back from the server.

Only the n parameter is required. Omitting all other parameters results in a query that matches each and every document found on the collection.

The method does not expose a projection directly, which is instead automatically determined based on the invocation options.

The returned documents are exactly as they come back from Astra DB \(taking into account the projection as well\). A further step, namely subsequent invocation of the convert\_astra\_db\_document method, is required to reconstruct codec-independent Document objects. The reason for keeping the retrieval and the decoding steps separate is that a caller may want to first deduplicate/discard items, in order to convert only the items actually needed.

Parameters:     

  * **n** – amount of items to return. Fewer items than n may be returned if the collection has not enough matches.

  * **ids** – a list of document IDs to restrict the query to. If this is supplied, only document with an ID among the provided one will match. If further query filters are provided \(i.e. metadata\), matches must satisfy both requirements.

  * **filter** – a metadata filtering part. If provided, it must refer to metadata keys by their bare name \(such as \{“key”: 123\}\). This filter can combine nested conditions with “$or”/”$and” connectors, for example: \- \{“tag”: “a”\} \- \{“$or”: \[\{“tag”: “a”\}, “label”: “b”\]\} \- \{“$and”: \[\{“tag”: \{“$in”: \[“a”, “z”\]\}\}, “label”: “b”\]\}

  * **sort** – a ‘sort’ clause for the query, such as \{“$vector”: \[…\]\}, \{“$vectorize”: “…”\} or \{“mdkey”: 1\}. Metadata sort conditions must be expressed by their ‘bare’ name.

  * **include\_similarity** – whether to return similarity scores with each match. Requires vector sort.

  * **include\_sort\_vector** – whether to return the very query vector used for the ANN search alongside the iterable of results. Requires vector sort. Note that the shape of the return value depends on this parameter.

  * **include\_embeddings** – whether to retrieve the matches’ own embedding vectors.

Returns:     

  * if include\_sort\_vector = False, the return value is an iterable over     

Astra DB documents \(dictionaries\);

  * if include\_sort\_vector = True, the return value is a 2-item tuple     

\(sort\_v, astra\_db\_ite\) tuple, where: \- sort\_v is the sort vector, if requested, or None if not available. \- astra\_db\_ite is an iterable over Astra DB documents \(dictionaries\).

Return type:     

The shape of the return value depends on the value of include\_sort\_vector

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

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _lexical\_query : str | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **lexical\_query** \(_str_ _|__None_\) – for hybrid search, a specific query for the lexical portion of the retrieval. If omitted or empty, defaults to the same as ‘query’. If passed on a non-hybrid search, an error is raised.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents most similar to the query.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **\*\*kwargs** \(_Any_\) – Additional arguments are ignored.

Returns:     

The list of Documents most similar to the query vector.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_with\_embedding\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → tuple\[list\[float\], list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_with_embedding)\#     

Return docs most similar to the query with embedding.

Also includes the query embedding vector.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

\(The query embedding vector, The list of \(Document, embedding\), the most similar to the query vector.\).

Return type:     

tuple\[list\[float\], list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\]\]

similarity\_search\_with\_embedding\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_with_embedding_by_vector)\#     

Return docs most similar to embedding vector with embedding.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

\(The query embedding vector, The list of \(Document, embedding\), the most similar to the query vector.\).

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), list\[float\]\]\]

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

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _lexical\_query : str | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_with_score)\#     

Return docs most similar to query with score.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **lexical\_query** \(_str_ _|__None_\) – for hybrid search, a specific query for the lexical portion of the retrieval. If omitted or empty, defaults to the same as ‘query’. If passed on a non-hybrid search, an error is raised.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector with score.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_id\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _lexical\_query : str | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_with_score_id)\#     

Return docs most similar to the query with score and id.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **lexical\_query** \(_str_ _|__None_\) – for hybrid search, a specific query for the lexical portion of the retrieval. If omitted or empty, defaults to the same as ‘query’. If passed on a non-hybrid search, an error is raised.

Returns:     

The list of \(Document, score, id\), the most similar to the query.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

similarity\_search\_with\_score\_id\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.similarity_search_with_score_id_by_vector)\#     

Return docs most similar to embedding vector with score and id.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score, id\), the most similar to the query vector.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

update\_metadata\(

    _id\_to\_metadata : dict\[str, dict\]_,     _\*_ ,     _overwrite\_concurrency : int | None = None_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/vectorstores.html#AstraDBVectorStore.update_metadata)\#     

Add/overwrite the metadata of existing documents.

For each document to update, the new metadata dictionary is appended to the existing metadata, overwriting individual keys that existed already.

Parameters:     

  * **id\_to\_metadata** \(_dict_ _\[__str_ _,__dict_ _\]_\) – map from the Document IDs to modify to the new metadata for updating. Keys in this dictionary that do not correspond to an existing document will be silently ignored. The values of this map are metadata dictionaries for updating the documents. Any pre-existing metadata will be merged with these entries, which take precedence on a key-by-key basis.

  * **overwrite\_concurrency** \(_int_ _|__None_\) – number of threads to process the updates. Defaults to the vector-store overall setting if not provided.

Returns:     

the number of documents successfully updated \(i.e. found to exist, since even an update with \{\} as the new metadata counts as successful.\)

Return type:     

int

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)