# CassandraGraphVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.cassandra.CassandraGraphVectorStore.html
**Word Count:** 3455
**Links Count:** 338
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# CassandraGraphVectorStore\#

_class _langchain\_community.graph\_vectorstores.cassandra.CassandraGraphVectorStore\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ttl\_seconds : int | None = None_,     _\*_ ,     _body\_index\_options : list\[tuple\[str, Any\]\] | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _metadata\_deny\_list : list\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Apache Cassandra\(R\) for graph-vector-store workloads.

To use it, you need a recent installation of the cassio library and a Cassandra cluster / Astra DB instance supporting vector capabilities.

Example               from langchain_community.graph_vectorstores import         CassandraGraphVectorStore     from langchain_openai import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     session = ...             # create your Cassandra session object     keyspace = 'my_keyspace'  # the keyspace should exist already     table_name = 'my_graph_vector_store'     vectorstore = CassandraGraphVectorStore(         embeddings,         session,         keyspace,         table_name,     )     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Session_ _|__None_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_str_ _|__None_\) – Cassandra keyspace. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ttl\_seconds** \(_int_ _|__None_\) – Optional time-to-live for the added texts.

  * **body\_index\_options** \(_list_ _\[__tuple_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Cassandra table \(SYNC, ASYNC or OFF\).

  * **metadata\_deny\_list** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list of metadata keys to not index. i.e. to fine-tune which of the metadata fields are indexed. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\). Note: the metadata\_indexing parameter from langchain\_community.utilities.cassandra.Cassandra is not exposed since CassandraGraphVectorStore only supports the deny\_list option.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(embedding\[, session, keyspace, ...\]\) | Apache Cassandra\(R\) for graph-vector-store workloads.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Run more documents through the embeddings and add to the vector store.   `aadd_nodes`\(nodes, \*\*kwargs\) | Add nodes to the graph store.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vector store.   `add_documents`\(documents, \*\*kwargs\) | Run more documents through the embeddings and add to the vector store.   `add_nodes`\(nodes, \*\*kwargs\) | Add nodes to the graph store.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vector store.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\[, ...\]\) | Create a CassandraGraphVectorStore from a document list.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a CassandraGraphVectorStore from raw texts.   `aget_by_document_id`\(document\_id\) | Retrieve a single document from the store, given its document ID.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `ametadata_search`\(\[filter, n\]\) | Get documents via a metadata search.   `ammr_traversal_search`\(query, \*\[, ...\]\) | Retrieve documents from this graph store using MMR-traversal.   `as_retriever`\(\*\*kwargs\) | Return GraphVectorStoreRetriever initialized from this GraphVectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter\]\) | Retrieve documents from this graph store.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `atraversal_search`\(query, \*\[, k, depth, filter\]\) | Retrieve documents from this knowledge store.   `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `from_documents`\(documents, embedding, \*\[, ...\]\) | Create a CassandraGraphVectorStore from a document list.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a CassandraGraphVectorStore from raw texts.   `get_by_document_id`\(document\_id\) | Retrieve a single document from the store, given its document ID.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_node`\(node\_id\) | Retrieve a single node from the store, given its ID.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `metadata_search`\(\[filter, n\]\) | Get documents via a metadata search.   `mmr_traversal_search`\(query, \*\[, ...\]\) | Retrieve documents from this graph store using MMR-traversal.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Retrieve documents from this graph store.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(\*args, \*\*kwargs\) | Run similarity search with distance.   `traversal_search`\(query, \*\[, k, depth, filter\]\) | Retrieve documents from this knowledge store.      \_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ttl\_seconds : int | None = None_,     _\*_ ,     _body\_index\_options : list\[tuple\[str, Any\]\] | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _metadata\_deny\_list : list\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.__init__)\#     

Apache Cassandra\(R\) for graph-vector-store workloads.

To use it, you need a recent installation of the cassio library and a Cassandra cluster / Astra DB instance supporting vector capabilities.

Example               from langchain_community.graph_vectorstores import         CassandraGraphVectorStore     from langchain_openai import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     session = ...             # create your Cassandra session object     keyspace = 'my_keyspace'  # the keyspace should exist already     table_name = 'my_graph_vector_store'     vectorstore = CassandraGraphVectorStore(         embeddings,         session,         keyspace,         table_name,     )     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Session_ _|__None_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_str_ _|__None_\) – Cassandra keyspace. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ttl\_seconds** \(_int_ _|__None_\) – Optional time-to-live for the added texts.

  * **body\_index\_options** \(_list_ _\[__tuple_ _\[__str_ _,__Any_ _\]__\]__|__None_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Cassandra table \(SYNC, ASYNC or OFF\).

  * **metadata\_deny\_list** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list of metadata keys to not index. i.e. to fine-tune which of the metadata fields are indexed. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\). Note: the metadata\_indexing parameter from langchain\_community.utilities.cassandra.Cassandra is not exposed since CassandraGraphVectorStore only supports the deny\_list option.

Return type:     

None

_async _aadd\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Run more documents through the embeddings and add to the vector store.

The Links present in the document metadata field links will be extracted to create the Node links.

Eg if nodes a and b are connected over a hyperlink https://some-url, the function call would look like:               store.add_documents(         [             Document(                 id="a",                 page_content="some text a",                 metadata={                     "links": [                         Link.incoming(kind="hyperlink", tag="http://some-url")                     ]                 }             ),             Document(                 id="b",                 page_content="some text b",                 metadata={                     "links": [                         Link.outgoing(kind="hyperlink", tag="http://some-url")                     ]                 }             ),         ]          )     

Parameters:     

  * **documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vector store. The document’s metadata key links shall be an iterable of [`Link`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link").

  * **kwargs** \(_Any_\)

Returns:     

List of IDs of the added texts.

Return type:     

list\[str\]

_async _aadd\_nodes\(

    _nodes : Iterable\[[Node](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node")\]_,     _\*\* kwargs: Any_, \) → AsyncIterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.aadd_nodes)\#     

Add nodes to the graph store.

Parameters:     

  * **nodes** \(_Iterable_ _\[_[_Node_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") _\]_\) – the nodes to add.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_AsyncIterable_\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : Iterable\[dict\] | None = None_,     _\*_ ,     _ids : Iterable\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Run more texts through the embeddings and add to the vector store.

The Links present in the metadata field links will be extracted to create the Node links.

Eg if nodes a and b are connected over a hyperlink https://some-url, the function call would look like:               await store.aadd_texts(         ids=["a", "b"],         texts=["some text a", "some text b"],         metadatas=[             {                 "links": [                     Link.incoming(kind="hyperlink", tag="https://some-url")                 ]             },             {                 "links": [                     Link.outgoing(kind="hyperlink", tag="https://some-url")                 ]             },         ],     )     

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vector store.

  * **metadatas** \(_Iterable_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts. The metadata key links shall be an iterable of [`Link`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link").

  * **ids** \(_Iterable_ _\[__str_ _\]__|__None_\) – Optional list of IDs associated with the texts.

  * **\*\*kwargs** \(_Any_\) – vector store specific parameters.

Returns:     

List of ids from adding the texts into the vector store.

Return type:     

list\[str\]

add\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Run more documents through the embeddings and add to the vector store.

The Links present in the document metadata field links will be extracted to create the Node links.

Eg if nodes a and b are connected over a hyperlink https://some-url, the function call would look like:               store.add_documents(         [             Document(                 id="a",                 page_content="some text a",                 metadata={                     "links": [                         Link.incoming(kind="hyperlink", tag="http://some-url")                     ]                 }             ),             Document(                 id="b",                 page_content="some text b",                 metadata={                     "links": [                         Link.outgoing(kind="hyperlink", tag="http://some-url")                     ]                 }             ),         ]          )     

Parameters:     

  * **documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vector store. The document’s metadata key links shall be an iterable of [`Link`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link").

  * **kwargs** \(_Any_\)

Returns:     

List of IDs of the added texts.

Return type:     

list\[str\]

add\_nodes\(

    _nodes : Iterable\[[Node](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node")\]_,     _\*\* kwargs: Any_, \) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.add_nodes)\#     

Add nodes to the graph store.

Parameters:     

  * **nodes** \(_Iterable_ _\[_[_Node_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") _\]_\) – the nodes to add.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_Iterable_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : Iterable\[dict\] | None = None_,     _\*_ ,     _ids : Iterable\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\]\#     

Run more texts through the embeddings and add to the vector store.

The Links present in the metadata field links will be extracted to create the Node links.

Eg if nodes a and b are connected over a hyperlink https://some-url, the function call would look like:               store.add_texts(         ids=["a", "b"],         texts=["some text a", "some text b"],         metadatas=[             {                 "links": [                     Link.incoming(kind="hyperlink", tag="https://some-url")                 ]             },             {                 "links": [                     Link.outgoing(kind="hyperlink", tag="https://some-url")                 ]             },         ],     )     

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vector store.

  * **metadatas** \(_Iterable_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts. The metadata key links shall be an iterable of [`Link`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link").

  * **ids** \(_Iterable_ _\[__str_ _\]__|__None_\) – Optional list of IDs associated with the texts.

  * **\*\*kwargs** \(_Any_\) – vector store specific parameters.

Returns:     

List of ids from adding the texts into the vector store.

Return type:     

list\[str\]

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

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_deny\_list : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → CGVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.afrom_documents)\#     

Create a CassandraGraphVectorStore from a document list.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional list of IDs associated with the documents.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added documents.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **metadata\_deny\_list** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list of metadata keys to not index. i.e. to fine-tune which of the metadata fields are indexed. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\). Note: the metadata\_indexing parameter from langchain\_community.utilities.cassandra.Cassandra is not exposed since CassandraGraphVectorStore only supports the deny\_list option.

  * **kwargs** \(_Any_\)

Returns:     

a CassandraGraphVectorStore.

Return type:     

CGVST

_async classmethod _afrom\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_deny\_list : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → CGVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.afrom_texts)\#     

Create a CassandraGraphVectorStore from raw texts.

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

  * **metadata\_deny\_list** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list of metadata keys to not index. i.e. to fine-tune which of the metadata fields are indexed. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\). Note: the metadata\_indexing parameter from langchain\_community.utilities.cassandra.Cassandra is not exposed since CassandraGraphVectorStore only supports the deny\_list option.

  * **kwargs** \(_Any_\)

Returns:     

a CassandraGraphVectorStore.

Return type:     

CGVST

_async _aget\_by\_document\_id\(

    _document\_id : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.aget_by_document_id)\#     

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

_async _ametadata\_search\(

    _filter : dict\[str, Any\] | None = None_,     _n : int = 5_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.ametadata_search)\#     

Get documents via a metadata search.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – the metadata to query for.

  * **n** \(_int_\) – the maximum number of documents to return.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ammr\_traversal\_search\(

    _query : str_,     _\*_ ,     _initial\_roots : Sequence\[str\] = \(\)_,     _k : int = 4_,     _depth : int = 2_,     _fetch\_k : int = 100_,     _adjacent\_k : int = 10_,     _lambda\_mult : float = 0.5_,     _score\_threshold : float = -inf_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.ammr_traversal_search)\#     

Retrieve documents from this graph store using MMR-traversal.

This strategy first retrieves the top fetch\_k results by similarity to the question. It then selects the top k results based on maximum-marginal relevance using the given lambda\_mult.

At each step, it considers the \(remaining\) documents from fetch\_k as well as any documents connected by edges to a selected document retrieved based on similarity \(a “root”\).

Parameters:     

  * **query** \(_str_\) – The query string to search for.

  * **initial\_roots** \(_Sequence_ _\[__str_ _\]_\) – Optional list of document IDs to use for initializing search. The top adjacent\_k nodes adjacent to each initial root will be included in the set of initial candidates. To fetch only in the neighborhood of these nodes, set fetch\_k = 0.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of initial Documents to fetch via similarity. Will be added to the nodes adjacent to initial\_roots. Defaults to 100.

  * **adjacent\_k** \(_int_\) – Number of adjacent Documents to fetch. Defaults to 10.

  * **depth** \(_int_\) – Maximum depth of a node \(number of edges\) from a node retrieved via similarity. Defaults to 2.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **score\_threshold** \(_float_\) – Only documents with a score greater than or equal this threshold will be chosen. Defaults to -infinity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_AsyncIterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

as\_retriever\(

    _\*\* kwargs: Any_, \) → [GraphVectorStoreRetriever](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever.html#langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever "langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever")\#     

Return GraphVectorStoreRetriever initialized from this GraphVectorStore.

Parameters:     

**\*\*kwargs** \(_Any_\) – 

Keyword arguments to pass to the search function. Can include:

  * search\_type \(Optional\[str\]\): Defines the type of search that the Retriever should perform. Can be `traversal` \(default\), `similarity`, `mmr`,

> `mmr_traversal`, or `similarity_score_threshold`.

  * search\_kwargs \(Optional\[Dict\]\): Keyword arguments to pass to the search function. Can include things like:

    * k\(int\): Amount of documents to return \(Default: 4\).

    * depth\(int\): The maximum depth of edges to traverse \(Default: 1\). Only applies to search\_type: `traversal` and `mmr_traversal`.

    * score\_threshold\(float\): Minimum relevance threshold for similarity\_score\_threshold.

    * fetch\_k\(int\): Amount of documents to pass to MMR algorithm \(Default: 20\).

    * lambda\_mult\(float\): Diversity of results returned by MMR; 1 for minimum diversity and 0 for maximum. \(Default: 0.5\).

Returns:     

Retriever for this GraphVectorStore.

Return type:     

[_GraphVectorStoreRetriever_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever.html#langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever "langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever")

Examples:               # Retrieve documents traversing edges     docsearch.as_retriever(         search_type="traversal",         search_kwargs={'k': 6, 'depth': 2}     )          # Retrieve documents with higher diversity     # Useful if your dataset has many similar documents     docsearch.as_retriever(         search_type="mmr_traversal",         search_kwargs={'k': 6, 'lambda_mult': 0.25, 'depth': 2}     )          # Fetch more documents for the MMR algorithm to consider     # But only return the top 5     docsearch.as_retriever(         search_type="mmr_traversal",         search_kwargs={'k': 5, 'fetch_k': 50, 'depth': 2}     )          # Only retrieve documents that have a relevance score     # Above a certain threshold     docsearch.as_retriever(         search_type="similarity_score_threshold",         search_kwargs={'score_threshold': 0.8}     )          # Only get the single most similar document from the dataset     docsearch.as_retriever(search_kwargs={'k': 1})     

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

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.asimilarity_search)\#     

Retrieve documents from this graph store.

Parameters:     

  * **query** \(_str_\) – The query string.

  * **k** \(_int_\) – The number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

Collection of retrieved documents.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.asimilarity_search_by_vector)\#     

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

_async _atraversal\_search\(

    _query : str_,     _\*_ ,     _k : int = 4_,     _depth : int = 1_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.atraversal_search)\#     

Retrieve documents from this knowledge store.

First, k nodes are retrieved using a vector search for the query string. Then, additional nodes are discovered up to the given depth from those starting nodes.

Parameters:     

  * **query** \(_str_\) – The query string.

  * **k** \(_int_\) – The number of Documents to return from the initial vector search. Defaults to 4.

  * **depth** \(_int_\) – The maximum depth of edges to traverse. Defaults to 1.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

Collection of retrieved documents.

Return type:     

_AsyncIterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

delete\(

    _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None\#     

Delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of ids to delete. If None, delete all. Default is None.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_deny\_list : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → CGVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.from_documents)\#     

Create a CassandraGraphVectorStore from a document list.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – Cassandra table \(required\).

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional list of IDs associated with the documents.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – Optional time-to-live for the added documents.

  * **body\_index\_options** \(_Optional_ _\[__List_ _\[__Tuple_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Optional options used to create the body index. Eg. body\_index\_options = \[cassio.table.cql.STANDARD\_ANALYZER\]

  * **metadata\_deny\_list** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list of metadata keys to not index. i.e. to fine-tune which of the metadata fields are indexed. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\). Note: the metadata\_indexing parameter from langchain\_community.utilities.cassandra.Cassandra is not exposed since CassandraGraphVectorStore only supports the deny\_list option.

  * **kwargs** \(_Any_\)

Returns:     

a CassandraGraphVectorStore.

Return type:     

CGVST

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = ''_,     _ids : List\[str\] | None = None_,     _ttl\_seconds : int | None = None_,     _body\_index\_options : List\[Tuple\[str, Any\]\] | None = None_,     _metadata\_deny\_list : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → CGVST[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.from_texts)\#     

Create a CassandraGraphVectorStore from raw texts.

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

  * **metadata\_deny\_list** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – Optional list of metadata keys to not index. i.e. to fine-tune which of the metadata fields are indexed. Note: if you plan to have massive unique text metadata entries, consider not indexing them for performance \(and to overcome max-length limitations\). Note: the metadata\_indexing parameter from langchain\_community.utilities.cassandra.Cassandra is not exposed since CassandraGraphVectorStore only supports the deny\_list option.

  * **kwargs** \(_Any_\)

Returns:     

a CassandraGraphVectorStore.

Return type:     

CGVST

get\_by\_document\_id\(

    _document\_id : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.get_by_document_id)\#     

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

get\_node\(

    _node\_id : str_, \) → [Node](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.get_node)\#     

Retrieve a single node from the store, given its ID.

Parameters:     

**node\_id** \(_str_\) – The node ID

Returns:     

The the node if it exists. Otherwise None.

Return type:     

[_Node_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") | None

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

metadata\_search\(

    _filter : dict\[str, Any\] | None = None_,     _n : int = 5_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.metadata_search)\#     

Get documents via a metadata search.

Parameters:     

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – the metadata to query for.

  * **n** \(_int_\) – the maximum number of documents to return.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

mmr\_traversal\_search\(

    _query : str_,     _\*_ ,     _initial\_roots : Sequence\[str\] = \(\)_,     _k : int = 4_,     _depth : int = 2_,     _fetch\_k : int = 100_,     _adjacent\_k : int = 10_,     _lambda\_mult : float = 0.5_,     _score\_threshold : float = -inf_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.mmr_traversal_search)\#     

Retrieve documents from this graph store using MMR-traversal.

This strategy first retrieves the top fetch\_k results by similarity to the question. It then selects the top k results based on maximum-marginal relevance using the given lambda\_mult.

At each step, it considers the \(remaining\) documents from fetch\_k as well as any documents connected by edges to a selected document retrieved based on similarity \(a “root”\).

Parameters:     

  * **query** \(_str_\) – The query string to search for.

  * **initial\_roots** \(_Sequence_ _\[__str_ _\]_\) – Optional list of document IDs to use for initializing search. The top adjacent\_k nodes adjacent to each initial root will be included in the set of initial candidates. To fetch only in the neighborhood of these nodes, set fetch\_k = 0.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of initial Documents to fetch via similarity. Will be added to the nodes adjacent to initial\_roots. Defaults to 100.

  * **adjacent\_k** \(_int_\) – Number of adjacent Documents to fetch. Defaults to 10.

  * **depth** \(_int_\) – Maximum depth of a node \(number of edges\) from a node retrieved via similarity. Defaults to 2.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **score\_threshold** \(_float_\) – Only documents with a score greater than or equal this threshold will be chosen. Defaults to -infinity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.similarity_search)\#     

Retrieve documents from this graph store.

Parameters:     

  * **query** \(_str_\) – The query string.

  * **k** \(_int_\) – The number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

Collection of retrieved documents.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.similarity_search_by_vector)\#     

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

    _\* args: Any_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Run similarity search with distance.

Parameters:     

  * **\*args** \(_Any_\) – Arguments to pass to the search method.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

traversal\_search\(

    _query : str_,     _\*_ ,     _k : int = 4_,     _depth : int = 1_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/cassandra.html#CassandraGraphVectorStore.traversal_search)\#     

Retrieve documents from this knowledge store.

First, k nodes are retrieved using a vector search for the query string. Then, additional nodes are discovered up to the given depth from those starting nodes.

Parameters:     

  * **query** \(_str_\) – The query string.

  * **k** \(_int_\) – The number of Documents to return from the initial vector search. Defaults to 4.

  * **depth** \(_int_\) – The maximum depth of edges to traverse. Defaults to 1.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

Collection of retrieved documents.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)