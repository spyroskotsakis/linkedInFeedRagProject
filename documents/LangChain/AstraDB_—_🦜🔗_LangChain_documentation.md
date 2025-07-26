# AstraDB — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html
**Word Count:** 3181
**Links Count:** 554
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# AstraDB\#

_class _langchain\_community.vectorstores.astradb.AstraDB\(

    _\*_ ,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : LibAstraDB | None = None_,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _namespace : str | None = None_,     _metric : str | None = None_,     _batch\_size : int | None = None_,     _bulk\_insert\_batch\_concurrency : int | None = None_,     _bulk\_insert\_overwrite\_concurrency : int | None = None_,     _bulk\_delete\_concurrency : int | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB)\#     

Deprecated since version 0.0.21: Use `:class:`~langchain_astradb.AstraDBVectorStore`` instead. It will not be removed until langchain-community==1.0.

Wrapper around DataStax Astra DB for vector-store workloads.

For quickstart and details, visit <https://docs.datastax.com/en/astra/astra-db-vector/>

Example               from langchain_community.vectorstores import AstraDB     from langchain_openai.embeddings import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     vectorstore = AstraDB(         embedding=embeddings,         collection_name="my_store",         token="AstraCS:...",         api_endpoint="https://<DB-ID>-<REGION>.apps.astra.datastax.com"     )          vectorstore.add_texts(["Giraffes", "All good here"])     results = vectorstore.similarity_search("Everything's ok", k=1)     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – embedding function to use.

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[__LibAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **metric** \(_Optional_ _\[__str_ _\]_\) – similarity function to use out of those available in Astra DB. If left out, it will use Astra DB API’s defaults \(i.e. “cosine” - but, for performance reasons, “dot\_product” is suggested if embeddings are normalized to one\).

  * **batch\_size** \(_Optional_ _\[__int_ _\]_\) – Size of batches for bulk insertions.

  * **bulk\_insert\_batch\_concurrency** \(_Optional_ _\[__int_ _\]_\) – Number of threads or coroutines to insert batches concurrently.

  * **bulk\_insert\_overwrite\_concurrency** \(_Optional_ _\[__int_ _\]_\) – Number of threads or coroutines in a batch to insert pre-existing entries.

  * **bulk\_delete\_concurrency** \(_Optional_ _\[__int_ _\]_\) – Number of threads \(for deleting multiple rows concurrently\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\)

Note

For concurrency in synchronous `add_texts()`:, as a rule of thumb, on a typical client machine it is suggested to keep the quantity bulk\_insert\_batch\_concurrency \* bulk\_insert\_overwrite\_concurrency much below 1000 to avoid exhausting the client multithreading/networking resources. The hardcoded defaults are somewhat conservative to meet most machines’ specs, but a sensible choice to test may be:

  * bulk\_insert\_batch\_concurrency = 80

  * bulk\_insert\_overwrite\_concurrency = 10

A bit of experimentation is required to nail the best results here, depending on both the machine/network specs and the expected workload \(specifically, how often a write is an update of an existing id\). Remember you can pass concurrency settings to individual calls to `add_texts()` and `add_documents()` as well.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(\*, embedding, collection\_name\[, ...\]\) | Wrapper around DataStax Astra DB for vector-store workloads.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, ...\]\) | Run texts through the embeddings and add them to the vectorstore.   `aclear`\(\) | Empty the collection of all its stored entries.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids, ...\]\) | Run texts through the embeddings and add them to the vectorstore.   `adelete`\(\[ids, concurrency\]\) | Delete by vector ids.   `adelete_by_document_id`\(document\_id\) | Remove a single document from the store, given its document ID.   `adelete_collection`\(\) | Completely delete the collection from the database \(as opposed to `aclear()`, which empties it only\).   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Create an Astra DB vectorstore from raw texts.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter\]\) | Return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, filter\]\) | Return docs most similar to query with score.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs most similar to embedding vector with score.   `asimilarity_search_with_score_id`\(query\[, k, ...\]\) | Return docs most similar to the query with score and id.   `asimilarity_search_with_score_id_by_vector`\(...\) | Return docs most similar to embedding vector with score and id.   `clear`\(\) | Empty the collection of all its stored entries.   `delete`\(\[ids, concurrency\]\) | Delete by vector ids.   `delete_by_document_id`\(document\_id\) | Remove a single document from the store, given its document ID.   `delete_collection`\(\) | Completely delete the collection from the database \(as opposed to `clear()`, which empties it only\).   `from_documents`\(documents, embedding, \*\*kwargs\) | Create an Astra DB vectorstore from a document list.   `from_texts`\(texts, embedding\[, metadatas, ids\]\) | Create an Astra DB vectorstore from raw texts.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, filter\]\) | Return docs most similar to query with score.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector with score.   `similarity_search_with_score_id`\(query\[, k, ...\]\) | Return docs most similar to the query with score and id.   `similarity_search_with_score_id_by_vector`\(...\) | Return docs most similar to embedding vector with score and id.      \_\_init\_\_\(

    _\*_ ,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : LibAstraDB | None = None_,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _namespace : str | None = None_,     _metric : str | None = None_,     _batch\_size : int | None = None_,     _bulk\_insert\_batch\_concurrency : int | None = None_,     _bulk\_insert\_overwrite\_concurrency : int | None = None_,     _bulk\_delete\_concurrency : int | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.__init__)\#     

Wrapper around DataStax Astra DB for vector-store workloads.

For quickstart and details, visit <https://docs.datastax.com/en/astra/astra-db-vector/>

Example               from langchain_community.vectorstores import AstraDB     from langchain_openai.embeddings import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     vectorstore = AstraDB(         embedding=embeddings,         collection_name="my_store",         token="AstraCS:...",         api_endpoint="https://<DB-ID>-<REGION>.apps.astra.datastax.com"     )          vectorstore.add_texts(["Giraffes", "All good here"])     results = vectorstore.similarity_search("Everything's ok", k=1)     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – embedding function to use.

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[__LibAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **metric** \(_Optional_ _\[__str_ _\]_\) – similarity function to use out of those available in Astra DB. If left out, it will use Astra DB API’s defaults \(i.e. “cosine” - but, for performance reasons, “dot\_product” is suggested if embeddings are normalized to one\).

  * **batch\_size** \(_Optional_ _\[__int_ _\]_\) – Size of batches for bulk insertions.

  * **bulk\_insert\_batch\_concurrency** \(_Optional_ _\[__int_ _\]_\) – Number of threads or coroutines to insert batches concurrently.

  * **bulk\_insert\_overwrite\_concurrency** \(_Optional_ _\[__int_ _\]_\) – Number of threads or coroutines in a batch to insert pre-existing entries.

  * **bulk\_delete\_concurrency** \(_Optional_ _\[__int_ _\]_\) – Number of threads \(for deleting multiple rows concurrently\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*_ ,     _batch\_size : int | None = None_,     _batch\_concurrency : int | None = None_,     _overwrite\_concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.aadd_texts)\#     

Run texts through the embeddings and add them to the vectorstore.

If passing explicit ids, those entries whose id is in the store already will be replaced.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids.

  * **batch\_size** \(_int_ _|__None_\) – Number of documents in each API call. Check the underlying Astra DB HTTP API specs for the max value \(20 at the time of writing this\). If not provided, defaults to the instance-level setting.

  * **batch\_concurrency** \(_int_ _|__None_\) – number of threads to process insertion batches concurrently. Defaults to instance-level setting if not provided.

  * **overwrite\_concurrency** \(_int_ _|__None_\) – number of threads to process pre-existing documents in each batch \(which require individual API calls\). Defaults to instance-level setting if not provided.

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

Note

There are constraints on the allowed field names in the metadata dictionaries, coming from the underlying Astra DB API. For instance, the $ \(dollar sign\) cannot be used in the dict keys. See this document for details: <https://docs.datastax.com/en/astra/astra-db-vector/api-reference/data-api.html>

Returns:     

The list of ids of the added texts.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **batch\_size** \(_int_ _|__None_\)

  * **batch\_concurrency** \(_int_ _|__None_\)

  * **overwrite\_concurrency** \(_int_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.aclear)\#     

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*_ ,     _batch\_size : int | None = None_,     _batch\_concurrency : int | None = None_,     _overwrite\_concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.add_texts)\#     

Run texts through the embeddings and add them to the vectorstore.

If passing explicit ids, those entries whose id is in the store already will be replaced.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids.

  * **batch\_size** \(_int_ _|__None_\) – Number of documents in each API call. Check the underlying Astra DB HTTP API specs for the max value \(20 at the time of writing this\). If not provided, defaults to the instance-level setting.

  * **batch\_concurrency** \(_int_ _|__None_\) – number of threads to process insertion batches concurrently. Defaults to instance-level setting if not provided.

  * **overwrite\_concurrency** \(_int_ _|__None_\) – number of threads to process pre-existing documents in each batch \(which require individual API calls\). Defaults to instance-level setting if not provided.

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

Note

There are constraints on the allowed field names in the metadata dictionaries, coming from the underlying Astra DB API. For instance, the $ \(dollar sign\) cannot be used in the dict keys. See this document for details: <https://docs.datastax.com/en/astra/astra-db-vector/api-reference/data-api.html>

Returns:     

The list of ids of the added texts.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **batch\_size** \(_int_ _|__None_\)

  * **batch\_concurrency** \(_int_ _|__None_\)

  * **overwrite\_concurrency** \(_int_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.adelete)\#     

Delete by vector ids.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **concurrency** \(_int_ _|__None_\) – max concurrency of single-doc delete requests. Defaults to instance-level setting.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool | None

_async _adelete\_by\_document\_id\(_document\_id : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.adelete_by_document_id)\#     

Remove a single document from the store, given its document ID.

Parameters:     

**document\_id** \(_str_\) – The document ID

Return type:     

bool

Returns     

True if a document has indeed been deleted, False if ID not found.

_async _adelete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.adelete_collection)\#     

Completely delete the collection from the database \(as opposed to `aclear()`, which empties it only\). Stored data is lost and unrecoverable, resources are freed. Use with caution.

Return type:     

None

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → ADBVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.afrom_texts)\#     

Create an Astra DB vectorstore from raw texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – the texts to insert.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – the embedding function to use in the store.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – metadata dicts for the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – ids to associate to the texts.

  * **\*\*kwargs** \(_Any_\) – you can pass any argument that you would to `add_texts()` and/or to the ‘AstraDB’ constructor \(see these methods for details\). These arguments will be routed to the respective methods as they are.

Returns:     

an AstraDb vectorstore.

Return type:     

_ADBVST_

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.asimilarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.asimilarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents most similar to the query vector.

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.asimilarity_search_with_score)\#     

Return docs most similar to query with score.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.asimilarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector with score.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_id\(

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.asimilarity_search_with_score_id)\#     

Return docs most similar to the query with score and id.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score, id\), the most similar to the query.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

_async _asimilarity\_search\_with\_score\_id\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.asimilarity_search_with_score_id_by_vector)\#     

Return docs most similar to embedding vector with score and id.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.clear)\#     

Empty the collection of all its stored entries.

Return type:     

None

delete\(

    _ids : List\[str\] | None = None_,     _concurrency : int | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.delete)\#     

Delete by vector ids.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **concurrency** \(_int_ _|__None_\) – max number of threads issuing single-doc delete requests. Defaults to instance-level setting.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool | None

delete\_by\_document\_id\(_document\_id : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.delete_by_document_id)\#     

Remove a single document from the store, given its document ID.

Parameters:     

**document\_id** \(_str_\) – The document ID

Return type:     

bool

Returns     

True if a document has indeed been deleted, False if ID not found.

delete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.delete_collection)\#     

Completely delete the collection from the database \(as opposed to `clear()`, which empties it only\). Stored data is lost and unrecoverable, resources are freed. Use with caution.

Return type:     

None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*\* kwargs: Any_, \) → ADBVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.from_documents)\#     

Create an Astra DB vectorstore from a document list.

Utility method that defers to ‘from\_texts’ \(see that one\).

Args: see ‘from\_texts’, except here you have to supply ‘documents’     

in place of ‘texts’ and ‘metadatas’.

Returns:     

an AstraDB vectorstore.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **kwargs** \(_Any_\)

Return type:     

_ADBVST_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → ADBVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.from_texts)\#     

Create an Astra DB vectorstore from raw texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – the texts to insert.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – the embedding function to use in the store.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – metadata dicts for the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – ids to associate to the texts.

  * **\*\*kwargs** \(_Any_\) – you can pass any argument that you would to `add_texts()` and/or to the ‘AstraDB’ constructor \(see these methods for details\). These arguments will be routed to the respective methods as they are.

Returns:     

an AstraDb vectorstore.

Return type:     

_ADBVST_

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents selected by maximal marginal relevance.

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

  * **kwargs** \(_Any_\)

Returns:     

The list of Documents most similar to the query vector.

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.similarity_search_with_score)\#     

Return docs most similar to query with score.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector with score.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_id\(

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.similarity_search_with_score_id)\#     

Return docs most similar to the query with score and id.

Parameters:     

  * **query** \(_str_\) – Query to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score, id\), the most similar to the query.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

similarity\_search\_with\_score\_id\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/astradb.html#AstraDB.similarity_search_with_score_id_by_vector)\#     

Return docs most similar to embedding vector with score and id.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Filter on the metadata to apply.

Returns:     

The list of \(Document, score, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

Examples using AstraDB

  * [Astra DB \(Cassandra\)](https://python.langchain.com/docs/integrations/retrievers/self_query/astradb/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)