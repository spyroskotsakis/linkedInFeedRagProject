# Neo4jVector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.Neo4jVector.html
**Word Count:** 2659
**Links Count:** 565
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# Neo4jVector\#

_class _langchain\_community.vectorstores.neo4j\_vector.Neo4jVector\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _search\_type : [SearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType") = SearchType.VECTOR_,     _username : str | None = None_,     _password : str | None = None_,     _url : str | None = None_,     _keyword\_index\_name : str | None = 'keyword'_,     _database : str | None = None_,     _index\_name : str = 'vector'_,     _node\_label : str = 'Chunk'_,     _embedding\_node\_property : str = 'embedding'_,     _text\_node\_property : str = 'text'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.COSINE_,     _logger : Logger | None = None_,     _pre\_delete\_collection : bool = False_,     _retrieval\_query : str = ''_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _index\_type : [IndexType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.IndexType.html#langchain_community.vectorstores.neo4j_vector.IndexType "langchain_community.vectorstores.neo4j_vector.IndexType") = IndexType.NODE_,     _graph : [Neo4jGraph](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.neo4j_graph.Neo4jGraph.html#langchain_community.graphs.neo4j_graph.Neo4jGraph "langchain_community.graphs.neo4j_graph.Neo4jGraph") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector)\#     

Deprecated since version 0.3.8: Use `:class:`~langchain_neo4j.Neo4jVector`` instead. It will not be removed until langchain-community==1.0.

Neo4j vector index.

To use, you should have the `neo4j` python package installed.

Parameters:     

  * **url** \(_Optional_ _\[__str_ _\]_\) – Neo4j connection url

  * **username** \(_Optional_ _\[__str_ _\]_\) – Neo4j username.

  * **password** \(_Optional_ _\[__str_ _\]_\) – Neo4j password

  * **database** \(_Optional_ _\[__str_ _\]_\) – Optionally provide Neo4j database Defaults to “neo4j”

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\) – The distance strategy to use. \(default: COSINE\)

  * **search\_type** \([_SearchType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType")\) – The type of search to be performed, either ‘vector’ or ‘hybrid’

  * **node\_label** \(_str_\) – The label used for nodes in the Neo4j database. \(default: “Chunk”\)

  * **embedding\_node\_property** \(_str_\) – The property name in Neo4j to store embeddings. \(default: “embedding”\)

  * **text\_node\_property** \(_str_\) – The property name in Neo4j to store the text. \(default: “text”\)

  * **retrieval\_query** \(_str_\) – The Cypher query to be used for customizing retrieval. If empty, a default query will be used.

  * **index\_type** \([_IndexType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.IndexType.html#langchain_community.vectorstores.neo4j_vector.IndexType "langchain_community.vectorstores.neo4j_vector.IndexType")\) – The type of index to be used, either ‘NODE’ or ‘RELATIONSHIP’

  * **pre\_delete\_collection** \(_bool_\) – If True, will delete existing data if it exists. \(default: False\). Useful for testing.

  * **keyword\_index\_name** \(_Optional_ _\[__str_ _\]_\)

  * **index\_name** \(_str_\)

  * **logger** \(_Optional_ _\[__logging.Logger_ _\]_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

  * **graph** \(_Optional_ _\[_[_Neo4jGraph_](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html#langchain_neo4j.graphs.neo4j_graph.Neo4jGraph "langchain_neo4j.graphs.neo4j_graph.Neo4jGraph") _\]_\)

Example               from langchain_community.vectorstores.neo4j_vector import Neo4jVector     from langchain_community.embeddings.openai import OpenAIEmbeddings          url="bolt://localhost:7687"     username="neo4j"     password="pleaseletmein"     embeddings = OpenAIEmbeddings()     vectorestore = Neo4jVector.from_documents(         embedding=embeddings,         documents=docs,         url=url         username=username,         password=password,     )     

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(embedding, \*\[, search\_type, ...\]\) |    ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(texts, embeddings\[, ...\]\) | Add embeddings to the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `create_new_index`\(\) | This method constructs a Cypher query and executes it to create a new vector index in Neo4j.   `create_new_keyword_index`\(\[text\_node\_properties\]\) | This method constructs a Cypher query and executes it to create a new full text index in Neo4j.   `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `from_documents`\(documents, embedding\[, ...\]\) | Return Neo4jVector initialized from documents and embeddings.   `from_embeddings`\(text\_embeddings, embedding\) | Construct Neo4jVector wrapper from raw documents and pre- generated embeddings.   `from_existing_graph`\(embedding, node\_label, ...\) | Initialize and return a Neo4jVector instance from an existing graph.   `from_existing_index`\(embedding, index\_name\[, ...\]\) | Get instance of an existing Neo4j vector index.   `from_existing_relationship_index`\(embedding, ...\) | Get instance of an existing Neo4j relationship vector index.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Return Neo4jVector initialized from texts and embeddings.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `query`\(query, \*\[, params\]\) | Query Neo4j database with retries and exponential backoff.   `retrieve_existing_fts_index`\(\[...\]\) | Check if the fulltext index exists in the Neo4j database   `retrieve_existing_index`\(\) | Check if the vector index exists in the Neo4j database and returns its embedding dimension.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, params, filter\]\) | Run similarity search with Neo4jVector.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) | Perform a similarity search in the Neo4j database using a given vector and return the top k similar documents with their scores.   `verify_version`\(\) | Check if the connected Neo4j database version supports vector indexing.      \_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _search\_type : [SearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType") = SearchType.VECTOR_,     _username : str | None = None_,     _password : str | None = None_,     _url : str | None = None_,     _keyword\_index\_name : str | None = 'keyword'_,     _database : str | None = None_,     _index\_name : str = 'vector'_,     _node\_label : str = 'Chunk'_,     _embedding\_node\_property : str = 'embedding'_,     _text\_node\_property : str = 'text'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.COSINE_,     _logger : Logger | None = None_,     _pre\_delete\_collection : bool = False_,     _retrieval\_query : str = ''_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _index\_type : [IndexType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.IndexType.html#langchain_community.vectorstores.neo4j_vector.IndexType "langchain_community.vectorstores.neo4j_vector.IndexType") = IndexType.NODE_,     _graph : [Neo4jGraph](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.neo4j_graph.Neo4jGraph.html#langchain_community.graphs.neo4j_graph.Neo4jGraph "langchain_community.graphs.neo4j_graph.Neo4jGraph") | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.__init__)\#     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **search\_type** \([_SearchType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType")\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **url** \(_str_ _|__None_\)

  * **keyword\_index\_name** \(_str_ _|__None_\)

  * **database** \(_str_ _|__None_\)

  * **index\_name** \(_str_\)

  * **node\_label** \(_str_\)

  * **embedding\_node\_property** \(_str_\)

  * **text\_node\_property** \(_str_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy")\)

  * **logger** \(_Logger_ _|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **retrieval\_query** \(_str_\)

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\)

  * **index\_type** \([_IndexType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.IndexType.html#langchain_community.vectorstores.neo4j_vector.IndexType "langchain_community.vectorstores.neo4j_vector.IndexType")\)

  * **graph** \([_Neo4jGraph_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.neo4j_graph.Neo4jGraph.html#langchain_community.graphs.neo4j_graph.Neo4jGraph "langchain_community.graphs.neo4j_graph.Neo4jGraph") _|__None_\)

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

add\_embeddings\(

    _texts : Iterable\[str\]_,     _embeddings : List\[List\[float\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.add_embeddings)\#     

Add embeddings to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\) – List of list of embedding vectors.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – List of metadatas associated with the texts.

  * **kwargs** \(_Any_\) – vectorstore specific parameters

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **kwargs** \(_Any_\) – vectorstore specific parameters

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

Returns:     

List of ids from adding the texts into the vectorstore.

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

create\_new\_index\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.create_new_index)\#     

This method constructs a Cypher query and executes it to create a new vector index in Neo4j.

Return type:     

None

create\_new\_keyword\_index\(

    _text\_node\_properties : List\[str\] = \[\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.create_new_keyword_index)\#     

This method constructs a Cypher query and executes it to create a new full text index in Neo4j.

Parameters:     

**text\_node\_properties** \(_List_ _\[__str_ _\]_\)

Return type:     

None

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

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → Neo4jVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.from_documents)\#     

Return Neo4jVector initialized from documents and embeddings. Neo4j credentials are required in the form of url, username, and password and optional database parameters.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Neo4jVector_

_classmethod _from\_embeddings\(

    _text\_embeddings : List\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*\* kwargs: Any_, \) → Neo4jVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.from_embeddings)\#     

Construct Neo4jVector wrapper from raw documents and pre- generated embeddings.

Return Neo4jVector initialized from documents and embeddings. Neo4j credentials are required in the form of url, username, and password and optional database parameters.

Example               from langchain_community.vectorstores.neo4j_vector import Neo4jVector     from langchain_community.embeddings import OpenAIEmbeddings     embeddings = OpenAIEmbeddings()     text_embeddings = embeddings.embed_documents(texts)     text_embedding_pairs = list(zip(texts, text_embeddings))     vectorstore = Neo4jVector.from_embeddings(         text_embedding_pairs, embeddings)     

Parameters:     

  * **text\_embeddings** \(_List_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **pre\_delete\_collection** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_Neo4jVector_

_classmethod _from\_existing\_graph\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _node\_label : str_,     _embedding\_node\_property : str_,     _text\_node\_properties : List\[str\]_,     _\*_ ,     _keyword\_index\_name : str | None = 'keyword'_,     _index\_name : str = 'vector'_,     _search\_type : [SearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType") = SearchType.VECTOR_,     _retrieval\_query : str = ''_,     _\*\* kwargs: Any_, \) → Neo4jVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.from_existing_graph)\#     

Initialize and return a Neo4jVector instance from an existing graph.

This method initializes a Neo4jVector instance using the provided parameters and the existing graph. It validates the existence of the indices and creates new ones if they don’t exist.

Returns: Neo4jVector: An instance of Neo4jVector initialized with the provided parameters

> and existing graph.

Example: >>> neo4j\_vector = Neo4jVector.from\_existing\_graph\( … embedding=my\_embedding, … node\_label=”Document”, … embedding\_node\_property=”embedding”, … text\_node\_properties=\[“title”, “content”\] … \)

Note: Neo4j credentials are required in the form of url, username, and password, and optional database parameters passed as additional keyword arguments.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **node\_label** \(_str_\)

  * **embedding\_node\_property** \(_str_\)

  * **text\_node\_properties** \(_List_ _\[__str_ _\]_\)

  * **keyword\_index\_name** \(_str_ _|__None_\)

  * **index\_name** \(_str_\)

  * **search\_type** \([_SearchType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType")\)

  * **retrieval\_query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Neo4jVector_

_classmethod _from\_existing\_index\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index\_name : str_,     _search\_type : [SearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType") = SearchType.VECTOR_,     _keyword\_index\_name : str | None = None_,     _\*\* kwargs: Any_, \) → Neo4jVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.from_existing_index)\#     

Get instance of an existing Neo4j vector index. This method will return the instance of the store without inserting any new embeddings. Neo4j credentials are required in the form of url, username, and password and optional database parameters along with the index\_name definition.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **index\_name** \(_str_\)

  * **search\_type** \([_SearchType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType")\)

  * **keyword\_index\_name** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Neo4jVector_

_classmethod _from\_existing\_relationship\_index\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index\_name : str_,     _search\_type : [SearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType") = SearchType.VECTOR_,     _\*\* kwargs: Any_, \) → Neo4jVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.from_existing_relationship_index)\#     

Get instance of an existing Neo4j relationship vector index. This method will return the instance of the store without inserting any new embeddings. Neo4j credentials are required in the form of url, username, and password and optional database parameters along with the index\_name definition.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **index\_name** \(_str_\)

  * **search\_type** \([_SearchType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.neo4j_vector.SearchType.html#langchain_community.vectorstores.neo4j_vector.SearchType "langchain_community.vectorstores.neo4j_vector.SearchType")\)

  * **kwargs** \(_Any_\)

Return type:     

_Neo4jVector_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.COSINE_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → Neo4jVector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.from_texts)\#     

Return Neo4jVector initialized from texts and embeddings. Neo4j credentials are required in the form of url, username, and password and optional database parameters.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy")\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Neo4jVector_

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – search query text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_dict_ _|__None_\) – 

Filter on metadata properties, e.g. \{

> ”str\_property”: “foo”, “int\_property”: 123

\}

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

query\(

    _query : str_,     _\*_ ,     _params : dict | None = None_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.query)\#     

Query Neo4j database with retries and exponential backoff.

Parameters:     

  * **query** \(_str_\) – The Cypher query to execute.

  * **params** \(_dict_ _,__optional_\) – Dictionary of query parameters. Defaults to \{\}.

Returns:     

List of dictionaries containing the query results.

Return type:     

List\[Dict\[str, Any\]\]

retrieve\_existing\_fts\_index\(

    _text\_node\_properties : List\[str\] = \[\]_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.retrieve_existing_fts_index)\#     

Check if the fulltext index exists in the Neo4j database

This method queries the Neo4j database for existing fts indexes with the specified name.

Returns:     

keyword index information

Return type:     

\(Tuple\)

Parameters:     

**text\_node\_properties** \(_List_ _\[__str_ _\]_\)

retrieve\_existing\_index\(\) → Tuple\[int | None, str | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.retrieve_existing_index)\#     

Check if the vector index exists in the Neo4j database and returns its embedding dimension.

This method queries the Neo4j database for existing indexes and attempts to retrieve the dimension of the vector index with the specified name. If the index exists, its dimension is returned. If the index doesn’t exist, None is returned.

Returns:     

The embedding dimension of the existing index if found.

Return type:     

int or None

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

    _query : str_,     _k : int = 4_,     _params : Dict\[str, Any\] = \{\}_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.similarity_search)\#     

Run similarity search with Neo4jVector.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **params** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The search params for the index type. Defaults to empty dict.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – 

Dictionary of argument\(s\) to     

filter on metadata.

Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _params : Dict\[str, Any\] = \{\}_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – 

Dictionary of argument\(s\) to     

filter on metadata.

Defaults to None.

  * **params** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The search params for the index type. Defaults to empty dict.

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

    _query : str_,     _k : int = 4_,     _params : Dict\[str, Any\] = \{\}_,     _filter : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.similarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **params** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The search params for the index type. Defaults to empty dict.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – 

Dictionary of argument\(s\) to     

filter on metadata.

Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _params : Dict\[str, Any\] = \{\}_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.similarity_search_with_score_by_vector)\#     

Perform a similarity search in the Neo4j database using a given vector and return the top k similar documents with their scores.

This method uses a Cypher query to find the top k documents that are most similar to a given embedding. The similarity is measured using a vector index in the Neo4j database. The results are returned as a list of tuples, each containing a Document object and its similarity score.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – The embedding vector to compare against.

  * **k** \(_int_ _,__optional_\) – The number of top similar documents to retrieve.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – 

Dictionary of argument\(s\) to     

filter on metadata.

Defaults to None.

  * **params** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The search params for the index type. Defaults to empty dict.

  * **kwargs** \(_Any_\)

Returns:     

A list of tuples, each containing     

a Document object and its similarity score.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

verify\_version\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/neo4j_vector.html#Neo4jVector.verify_version)\#     

Check if the connected Neo4j database version supports vector indexing.

Queries the Neo4j database to retrieve its version and compares it against a target version \(5.11.0\) that is known to support vector indexing. Raises a ValueError if the connected Neo4j version is not supported.

Return type:     

None

Examples using Neo4jVector

  * [How to best prompt for Graph-RAG](https://python.langchain.com/docs/how_to/graph_prompting/)

  * [Neo4j](https://python.langchain.com/docs/integrations/providers/neo4j/)

  * [Neo4j Vector Index](https://python.langchain.com/docs/integrations/vectorstores/neo4jvector/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)