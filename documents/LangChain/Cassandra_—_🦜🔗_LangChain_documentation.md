# Cassandra — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.cassandra.Cassandra.html
**Word Count:** 4323
**Links Count:** 587
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# Cassandra\#

_class _langchain\_community.vectorstores.cassandra.Cassandra\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ttl\_seconds : int | None = None_,     _\*_ ,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _metadata\_indexing : Tuple\[str, Iterable\[str\]\] | str = 'all'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra)\#     

Apache Cassandra\(R\) for vector-store workloads.

To use it, you need a recent installation of the cassio library and a Cassandra cluster / Astra DB instance supporting vector capabilities.

Visit the cassio.org website for extensive quickstarts and code examples.

Example               from langchain_community.vectorstores import Cassandra     from langchain_openai import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     session = ...             # create your Cassandra session object     keyspace = 'my_keyspace'  # the keyspace should exist already     table_name = 'my_vector_store'     vectorstore = Cassandra(embeddings, session, keyspace, table_name)     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra keyspace. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added texts.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Cassandra table \(SYNC, ASYNC or OFF\).

  * **metadata\_indexing** \(_Union_ _\[__Tuple_ _\[__str_ _,__Iterable_ _\[__str_ _\]__\]__,__str_ _\]_\) – 

Optional specification of a metadata indexing policy, i.e. to fine-tune which of the metadata fields are indexed. It can be a string \(“all” or “none”\), or a 2-tuple. The following means that all fields except ‘f1’, ‘f2’ … are NOT indexed:

> metadata\_indexing=\(“allowlist”, \[“f1”, “f2”, …\]\)

The following means all fields EXCEPT ‘g1’, ‘g2’, … are indexed:     

metadata\_indexing\(“denylist”, \[“g1”, “g2”, …\]\)

The default is to index every metadata field. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\).

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(embedding\[, session, keyspace, ...\]\) | Apache Cassandra\(R\) for vector-store workloads.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, ...\]\) | Run more texts through the embeddings and add to the vectorstore.   `aclear`\(\) | Empty the table.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids, ...\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Delete by vector IDs.   `adelete_by_document_id`\(document\_id\) | Delete by document ID.   `adelete_by_metadata_filter`\(filter, \*\[, ...\]\) | Delete all documents matching a certain metadata filtering condition.   `adelete_collection`\(\) | Just an alias for aclear \(to better align with other VectorStore implementations\).   `afrom_documents`\(documents, embedding, \*\[, ...\]\) | Create a Cassandra vector store from a document list.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a Cassandra vector store from raw texts.   `aget_by_document_id`\(document\_id\) | Retrieve a single document from the store, given its document ID.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :param filter: Filter on the metadata to apply. :param body\_search: Document textual search terms to apply. Only supported by Astra DB at the moment.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param embedding: Embedding to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. Defaults to 20. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :param filter: Filter on the metadata to apply. :param body\_search: Document textual search terms to apply. Only supported by Astra DB at the moment.   `ametadata_search`\(\[filter, n\]\) | Get documents via a metadata search.   `areplace_metadata`\(id\_to\_metadata, \*\[, ...\]\) | Replace the metadata of documents.   `as_retriever`\(\[search\_type, search\_kwargs, ...\]\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter, ...\]\) | Return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `asimilarity_search_with_embedding_id_by_vector`\(...\) | Return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs most similar to embedding vector.   `asimilarity_search_with_score_id`\(query\[, k, ...\]\) | Return docs most similar to query.   `asimilarity_search_with_score_id_by_vector`\(...\) | Return docs most similar to embedding vector.   `clear`\(\) | Empty the table.   `delete`\(\[ids\]\) | Delete by vector IDs.   `delete_by_document_id`\(document\_id\) | Delete by document ID.   `delete_by_metadata_filter`\(filter, \*\[, ...\]\) | Delete all documents matching a certain metadata filtering condition.   `delete_collection`\(\) | Just an alias for clear \(to better align with other VectorStore implementations\).   `from_documents`\(documents, embedding, \*\[, ...\]\) | Create a Cassandra vector store from a document list.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a Cassandra vector store from raw texts.   `get_by_document_id`\(document\_id\) | Retrieve a single document from the store, given its document ID.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. Defaults to 20. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :param filter: Filter on the metadata to apply. :param body\_search: Document textual search terms to apply. Only supported by Astra DB at the moment.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param embedding: Embedding to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. Defaults to 20. :param lambda\_mult: Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5. :param filter: Filter on the metadata to apply. :param body\_search: Document textual search terms to apply. Only supported by Astra DB at the moment.   `metadata_search`\(\[filter, n\]\) | Get documents via a metadata search.   `replace_metadata`\(id\_to\_metadata, \*\[, batch\_size\]\) | Replace the metadata of documents.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, ...\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector.   `similarity_search_with_score_id`\(query\[, k, ...\]\) | Return docs most similar to query.   `similarity_search_with_score_id_by_vector`\(...\) | Return docs most similar to embedding vector.      \_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ttl\_seconds : int | None = None_,     _\*_ ,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _metadata\_indexing : Tuple\[str, Iterable\[str\]\] | str = 'all'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.__init__)\#     

Apache Cassandra\(R\) for vector-store workloads.

To use it, you need a recent installation of the cassio library and a Cassandra cluster / Astra DB instance supporting vector capabilities.

Visit the cassio.org website for extensive quickstarts and code examples.

Example               from langchain_community.vectorstores import Cassandra     from langchain_openai import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     session = ...             # create your Cassandra session object     keyspace = 'my_keyspace'  # the keyspace should exist already     table_name = 'my_vector_store'     vectorstore = Cassandra(embeddings, session, keyspace, table_name)     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra keyspace. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added texts.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Cassandra table \(SYNC, ASYNC or OFF\).

  * **metadata\_indexing** \(_Union_ _\[__Tuple_ _\[__str_ _,__Iterable_ _\[__str_ _\]__\]__,__str_ _\]_\) – 

Optional specification of a metadata indexing policy, i.e. to fine-tune which of the metadata fields are indexed. It can be a string \(“all” or “none”\), or a 2-tuple. The following means that all fields except ‘f1’, ‘f2’ … are NOT indexed:

> metadata\_indexing=\(“allowlist”, \[“f1”, “f2”, …\]\)

The following means all fields EXCEPT ‘g1’, ‘g2’, … are indexed:     

metadata\_indexing\(“denylist”, \[“g1”, “g2”, …\]\)

The default is to index every metadata field. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\).

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _concurrency : int = 16_,     _ttl\_seconds : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.aadd_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of IDs.

  * **concurrency** \(_int_\) – Number of concurrent queries to the database. Defaults to 16.

  * **ttl\_seconds** \(_int_ _|__None_\) – Optional time-to-live for the added texts.

  * **kwargs** \(_Any_\)

Returns:     

List of IDs of the added texts.

Return type:     

List\[str\]

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.aclear)\#     

Empty the table.

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 16_,     _ttl\_seconds : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of IDs.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

  * **ttl\_seconds** \(_int_ _|__None_\) – Optional time-to-live for the added texts.

  * **kwargs** \(_Any_\)

Returns:     

List of IDs of the added texts.

Return type:     

List\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.adelete)\#     

Delete by vector IDs.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

_async _adelete\_by\_document\_id\(_document\_id : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.adelete_by_document_id)\#     

Delete by document ID.

Parameters:     

**document\_id** \(_str_\) – the document ID to delete.

Return type:     

None

_async _adelete\_by\_metadata\_filter\(

    _filter : dict\[str, Any\]_,     _\*_ ,     _batch\_size : int = 50_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.adelete_by_metadata_filter)\#     

Delete all documents matching a certain metadata filtering condition.

This operation does not use the vector embeddings in any way, it simply removes all documents whose metadata match the provided condition.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Filter on the metadata to apply. The filter cannot be empty.

  * **batch\_size** \(_int_\) – amount of deletions per each batch \(until exhaustion of the matching documents\).

Returns:     

A number expressing the amount of deleted documents.

Return type:     

int

_async _adelete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.adelete_collection)\#     

Just an alias for aclear \(to better align with other VectorStore implementations\).

Return type:     

None

_async classmethod _afrom\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_indexing : Tuple\[str, Iterable\[str\]\] | str = 'all'_,     _\*\* kwargs: Any_, \) → CVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.afrom_documents)\#     

Create a Cassandra vector store from a document list.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional list of IDs associated with the documents.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added documents.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **metadata\_indexing** \(_Union_ _\[__Tuple_ _\[__str_ _,__Iterable_ _\[__str_ _\]__\]__,__str_ _\]_\) – 

Optional specification of a metadata indexing policy, i.e. to fine-tune which of the metadata fields are indexed. It can be a string \(“all” or “none”\), or a 2-tuple. The following means that all fields except ‘f1’, ‘f2’ … are NOT indexed:

> metadata\_indexing=\(“allowlist”, \[“f1”, “f2”, …\]\)

The following means all fields EXCEPT ‘g1’, ‘g2’, … are indexed:     

metadata\_indexing\(“denylist”, \[“g1”, “g2”, …\]\)

The default is to index every metadata field. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\).

  * **kwargs** \(_Any_\)

Returns:     

a Cassandra vector store.

Return type:     

CVST

_async classmethod _afrom\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_indexing : Tuple\[str, Iterable\[str\]\] | str = 'all'_,     _\*\* kwargs: Any_, \) → CVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.afrom_texts)\#     

Create a Cassandra vector store from raw texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Optional list of metadatas associated with the texts.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional list of IDs associated with the texts.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added texts.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **metadata\_indexing** \(_Union_ _\[__Tuple_ _\[__str_ _,__Iterable_ _\[__str_ _\]__\]__,__str_ _\]_\) – 

Optional specification of a metadata indexing policy, i.e. to fine-tune which of the metadata fields are indexed. It can be a string \(“all” or “none”\), or a 2-tuple. The following means that all fields except ‘f1’, ‘f2’ … are NOT indexed:

> metadata\_indexing=\(“allowlist”, \[“f1”, “f2”, …\]\)

The following means all fields EXCEPT ‘g1’, ‘g2’, … are indexed:     

metadata\_indexing\(“denylist”, \[“g1”, “g2”, …\]\)

The default is to index every metadata field. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\).

  * **kwargs** \(_Any_\)

Returns:     

a Cassandra vector store.

Return type:     

CVST

_async _aget\_by\_document\_id\(

    _document\_id : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.aget_by_document_id)\#     

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm. :param lambda\_mult: Number between 0 and 1 that determines the degree

> of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

Parameters:     

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param embedding: Embedding to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm.

> Defaults to 20.

Parameters:     

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ametadata\_search\(

    _filter : dict\[str, Any\] = \{\}_,     _n : int = 5_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.ametadata_search)\#     

Get documents via a metadata search.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]_\) – the metadata to query for.

  * **n** \(_int_\) – the maximum number of documents to return.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _areplace\_metadata\(

    _id\_to\_metadata : dict\[str, dict\]_,     _\*_ ,     _concurrency : int = 50_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.areplace_metadata)\#     

Replace the metadata of documents.

For each document to update, identified by its ID, the new metadata dictionary completely replaces what is on the store. This includes passing empty metadata \{\} to erase the currently-stored information.

Parameters:     

  * **id\_to\_metadata** \(_dict_ _\[__str_ _,__dict_ _\]_\) – map from the Document IDs to modify to the new metadata for updating. Keys in this dictionary that do not correspond to an existing document will not cause an error, rather will result in new rows being written into the Cassandra table but without an associated vector: hence unreachable through vector search.

  * **concurrency** \(_int_\) – Number of concurrent queries to the database. Defaults to 50.

Returns:     

None if the writes succeed \(otherwise an error is raised\).

Return type:     

None

as\_retriever\(

    _search\_type : str = 'similarity'_,     _search\_kwargs : Dict\[str, Any\] | None = None_,     _tags : List\[str\] | None = None_,     _metadata : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.as_retriever)\#     

Return VectorStoreRetriever initialized from this VectorStore.

Parameters:     

  * **search\_type** \(_str_\) – Defines the type of search that the Retriever should perform. Can be “similarity” \(default\), “mmr”, or “similarity\_score\_threshold”.

  * **search\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – 

Keyword arguments to pass to the search function. Can include things like:

> k: Amount of documents to return \(Default: 4\) score\_threshold: Minimum relevance threshold >
>> for similarity\_score\_threshold >  > fetch\_k: Amount of documents to pass to MMR algorithm \(Default: 20\) lambda\_mult: Diversity of results returned by MMR; >
>> 1 for minimum diversity and 0 for maximum. \(Default: 0.5\) >  > filter: Filter by document metadata

  * **tags** \(_List_ _\[__str_ _\]__|__None_\) – List of tags associated with the retriever.

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Metadata associated with the retriever.

  * **kwargs** \(_Any_\) – Other arguments passed to the VectorStoreRetriever init.

Returns:     

Retriever for VectorStore.

Return type:     

[_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **kwargs** \(_Any_\)

Returns:     

List of Document, the most similar to the query vector.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **kwargs** \(_Any_\)

Returns:     

List of Document, the most similar to the query vector.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_with\_embedding\_id\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), List\[float\], str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search_with_embedding_id_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, embedding, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), _List_\[float\], str\]\]

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_id\(

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search_with_score_id)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

_async _asimilarity\_search\_with\_score\_id\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.asimilarity_search_with_score_id_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.clear)\#     

Empty the table.

Return type:     

None

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.delete)\#     

Delete by vector IDs.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

delete\_by\_document\_id\(_document\_id : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.delete_by_document_id)\#     

Delete by document ID.

Parameters:     

**document\_id** \(_str_\) – the document ID to delete.

Return type:     

None

delete\_by\_metadata\_filter\(

    _filter : dict\[str, Any\]_,     _\*_ ,     _batch\_size : int = 50_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.delete_by_metadata_filter)\#     

Delete all documents matching a certain metadata filtering condition.

This operation does not use the vector embeddings in any way, it simply removes all documents whose metadata match the provided condition.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Filter on the metadata to apply. The filter cannot be empty.

  * **batch\_size** \(_int_\) – amount of deletions per each batch \(until exhaustion of the matching documents\).

Returns:     

A number expressing the amount of deleted documents.

Return type:     

int

delete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.delete_collection)\#     

Just an alias for clear \(to better align with other VectorStore implementations\).

Return type:     

None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_indexing : Tuple\[str, Iterable\[str\]\] | str = 'all'_,     _\*\* kwargs: Any_, \) → CVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.from_documents)\#     

Create a Cassandra vector store from a document list.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional list of IDs associated with the documents.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added documents.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **metadata\_indexing** \(_Union_ _\[__Tuple_ _\[__str_ _,__Iterable_ _\[__str_ _\]__\]__,__str_ _\]_\) – 

Optional specification of a metadata indexing policy, i.e. to fine-tune which of the metadata fields are indexed. It can be a string \(“all” or “none”\), or a 2-tuple. The following means that all fields except ‘f1’, ‘f2’ … are NOT indexed:

> metadata\_indexing=\(“allowlist”, \[“f1”, “f2”, …\]\)

The following means all fields EXCEPT ‘g1’, ‘g2’, … are indexed:     

metadata\_indexing\(“denylist”, \[“g1”, “g2”, …\]\)

The default is to index every metadata field. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\).

  * **kwargs** \(_Any_\)

Returns:     

a Cassandra vector store.

Return type:     

CVST

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_indexing : Tuple\[str, Iterable\[str\]\] | str = 'all'_,     _\*\* kwargs: Any_, \) → CVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.from_texts)\#     

Create a Cassandra vector store from raw texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Optional list of metadatas associated with the texts.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional list of IDs associated with the texts.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added texts.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **metadata\_indexing** \(_Union_ _\[__Tuple_ _\[__str_ _,__Iterable_ _\[__str_ _\]__\]__,__str_ _\]_\) – 

Optional specification of a metadata indexing policy, i.e. to fine-tune which of the metadata fields are indexed. It can be a string \(“all” or “none”\), or a 2-tuple. The following means that all fields except ‘f1’, ‘f2’ … are NOT indexed:

> metadata\_indexing=\(“allowlist”, \[“f1”, “f2”, …\]\)

The following means all fields EXCEPT ‘g1’, ‘g2’, … are indexed:     

metadata\_indexing\(“denylist”, \[“g1”, “g2”, …\]\)

The default is to index every metadata field. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\).

  * **kwargs** \(_Any_\)

Returns:     

a Cassandra vector store.

Return type:     

CVST

get\_by\_document\_id\(

    _document\_id : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.get_by_document_id)\#     

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param query: Text to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm.

> Defaults to 20.

Parameters:     

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents. :param embedding: Embedding to look up documents similar to. :param k: Number of Documents to return. Defaults to 4. :param fetch\_k: Number of Documents to fetch to pass to MMR algorithm.

> Defaults to 20.

Parameters:     

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

metadata\_search\(

    _filter : dict\[str, Any\] = \{\}_,     _n : int = 5_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.metadata_search)\#     

Get documents via a metadata search.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]_\) – the metadata to query for.

  * **n** \(_int_\) – the maximum number of documents to return.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

replace\_metadata\(

    _id\_to\_metadata : dict\[str, dict\]_,     _\*_ ,     _batch\_size : int = 50_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.replace_metadata)\#     

Replace the metadata of documents.

For each document to update, identified by its ID, the new metadata dictionary completely replaces what is on the store. This includes passing empty metadata \{\} to erase the currently-stored information.

Parameters:     

  * **id\_to\_metadata** \(_dict_ _\[__str_ _,__dict_ _\]_\) – map from the Document IDs to modify to the new metadata for updating. Keys in this dictionary that do not correspond to an existing document will not cause an error, rather will result in new rows being written into the Cassandra table but without an associated vector: hence unreachable through vector search.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

Returns:     

None if the writes succeed \(otherwise an error is raised\).

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **kwargs** \(_Any_\)

Returns:     

List of Document, the most similar to the query vector.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

  * **kwargs** \(_Any_\)

Returns:     

List of Document, the most similar to the query vector.

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

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.similarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_id\(

    _query : str_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.similarity_search_with_score_id)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

similarity\_search\_with\_score\_id\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, str\] | None = None_,     _body\_search : str | List\[str\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/cassandra.html#Cassandra.similarity_search_with_score_id_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter on the metadata to apply.

  * **body\_search** \(_str_ _|__List_ _\[__str_ _\]__|__None_\) – Document textual search terms to apply. Only supported by Astra DB at the moment.

Returns:     

List of \(Document, score, id\), the most similar to the query vector.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, str\]\]

Examples using Cassandra

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [Cassandra](https://python.langchain.com/docs/integrations/providers/cassandra/)

  * [Hybrid Search](https://python.langchain.com/docs/how_to/hybrid/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)