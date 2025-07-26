# GraphVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html
**Word Count:** 2617
**Links Count:** 306
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# GraphVectorStore\#

_class _langchain\_community.graph\_vectorstores.base.GraphVectorStore\(_\* args: Any_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore)\#     

Deprecated since version 0.3.21: See <https://datastax.github.io/graph-rag/guide/migration/#from-langchain-graphvectorstore> for migration instructions. It will be removed in langchain-community==0.5.

A hybrid vector-and-graph graph store.

Document chunks support vector-similarity search as well as edges linking chunks based on structural and semantic properties.

Added in version 0.3.1.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Run more documents through the embeddings and add to the vector store.   `aadd_nodes`\(nodes, \*\*kwargs\) | Add nodes to the graph store.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vector store.   `add_documents`\(documents, \*\*kwargs\) | Run more documents through the embeddings and add to the vector store.   `add_nodes`\(nodes, \*\*kwargs\) | Add nodes to the graph store.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vector store.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `ammr_traversal_search`\(query, \*\[, ...\]\) | Retrieve documents from this graph store using MMR-traversal.   `as_retriever`\(\*\*kwargs\) | Return GraphVectorStoreRetriever initialized from this GraphVectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `atraversal_search`\(query, \*\[, k, depth, filter\]\) | Retrieve documents from traversing this graph store.   `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ids\]\) | Return VectorStore initialized from texts and embeddings.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `mmr_traversal_search`\(query, \*\[, ...\]\) | Retrieve documents from this graph store using MMR-traversal.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(\*args, \*\*kwargs\) | Run similarity search with distance.   `traversal_search`\(query, \*\[, k, depth, filter\]\) | Retrieve documents from traversing this graph store.      \_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → Any\#     

Parameters:     

  * **self** \(_Any_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

_async _aadd\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.aadd_documents)\#     

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

    _nodes : Iterable\[[Node](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node")\]_,     _\*\* kwargs: Any_, \) → AsyncIterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.aadd_nodes)\#     

Add nodes to the graph store.

Parameters:     

  * **nodes** \(_Iterable_ _\[_[_Node_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") _\]_\) – the nodes to add.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_AsyncIterable_\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : Iterable\[dict\] | None = None_,     _\*_ ,     _ids : Iterable\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.aadd_texts)\#     

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

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.add_documents)\#     

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

_abstractmethod _add\_nodes\(

    _nodes : Iterable\[[Node](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node")\]_,     _\*\* kwargs: Any_, \) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.add_nodes)\#     

Add nodes to the graph store.

Parameters:     

  * **nodes** \(_Iterable_ _\[_[_Node_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.Node.html#langchain_community.graph_vectorstores.base.Node "langchain_community.graph_vectorstores.base.Node") _\]_\) – the nodes to add.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_Iterable_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : Iterable\[dict\] | None = None_,     _\*_ ,     _ids : Iterable\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.add_texts)\#     

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

_async _ammr\_traversal\_search\(

    _query : str_,     _\*_ ,     _initial\_roots : Sequence\[str\] = \(\)_,     _k : int = 4_,     _depth : int = 2_,     _fetch\_k : int = 100_,     _adjacent\_k : int = 10_,     _lambda\_mult : float = 0.5_,     _score\_threshold : float = -inf_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.ammr_traversal_search)\#     

Retrieve documents from this graph store using MMR-traversal.

This strategy first retrieves the top fetch\_k results by similarity to the question. It then selects the top k results based on maximum-marginal relevance using the given lambda\_mult.

At each step, it considers the \(remaining\) documents from fetch\_k as well as any documents connected by edges to a selected document retrieved based on similarity \(a “root”\).

Parameters:     

  * **query** \(_str_\) – The query string to search for.

  * **initial\_roots** \(_Sequence_ _\[__str_ _\]_\) – Optional list of document IDs to use for initializing search. The top adjacent\_k nodes adjacent to each initial root will be included in the set of initial candidates. To fetch only in the neighborhood of these nodes, set fetch\_k = 0.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch via similarity. Defaults to 100.

  * **adjacent\_k** \(_int_\) – Number of adjacent Documents to fetch. Defaults to 10.

  * **depth** \(_int_\) – Maximum depth of a node \(number of edges\) from a node retrieved via similarity. Defaults to 2.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **score\_threshold** \(_float_\) – Only documents with a score greater than or equal this threshold will be chosen. Defaults to negative infinity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_AsyncIterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

as\_retriever\(

    _\*\* kwargs: Any_, \) → [GraphVectorStoreRetriever](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever.html#langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever "langchain_community.graph_vectorstores.base.GraphVectorStoreRetriever")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.as_retriever)\#     

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

    _query : str_,     _search\_type : str_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.asearch)\#     

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

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.asimilarity_search)\#     

Async return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

_async _atraversal\_search\(

    _query : str_,     _\*_ ,     _k : int = 4_,     _depth : int = 1_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → AsyncIterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.atraversal_search)\#     

Retrieve documents from traversing this graph store.

First, k nodes are retrieved using a search for each query string. Then, additional nodes are discovered up to the given depth from those starting nodes.

Parameters:     

  * **query** \(_str_\) – The query string.

  * **k** \(_int_\) – The number of Documents to return from the initial search. Defaults to 4. Applies to each of the query strings.

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

_abstractmethod classmethod _from\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : list\[dict\] | None = None_,     _\*_ ,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → VST\#     

Return VectorStore initialized from texts and embeddings.

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.max_marginal_relevance_search)\#     

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

_abstractmethod _mmr\_traversal\_search\(

    _query : str_,     _\*_ ,     _initial\_roots : Sequence\[str\] = \(\)_,     _k : int = 4_,     _depth : int = 2_,     _fetch\_k : int = 100_,     _adjacent\_k : int = 10_,     _lambda\_mult : float = 0.5_,     _score\_threshold : float = -inf_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.mmr_traversal_search)\#     

Retrieve documents from this graph store using MMR-traversal.

This strategy first retrieves the top fetch\_k results by similarity to the question. It then selects the top k results based on maximum-marginal relevance using the given lambda\_mult.

At each step, it considers the \(remaining\) documents from fetch\_k as well as any documents connected by edges to a selected document retrieved based on similarity \(a “root”\).

Parameters:     

  * **query** \(_str_\) – The query string to search for.

  * **initial\_roots** \(_Sequence_ _\[__str_ _\]_\) – Optional list of document IDs to use for initializing search. The top adjacent\_k nodes adjacent to each initial root will be included in the set of initial candidates. To fetch only in the neighborhood of these nodes, set fetch\_k = 0.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch via similarity. Defaults to 100.

  * **adjacent\_k** \(_int_\) – Number of adjacent Documents to fetch. Defaults to 10.

  * **depth** \(_int_\) – Maximum depth of a node \(number of edges\) from a node retrieved via similarity. Defaults to 2.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **score\_threshold** \(_float_\) – Only documents with a score greater than or equal this threshold will be chosen. Defaults to negative infinity.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

search\(

    _query : str_,     _search\_type : str_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.search)\#     

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

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Documents most similar to the query.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _\* args: Any_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Run similarity search with distance.

Parameters:     

  * **\*args** \(_Any_\) – Arguments to pass to the search method.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_abstractmethod _traversal\_search\(

    _query : str_,     _\*_ ,     _k : int = 4_,     _depth : int = 1_,     _filter : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/base.html#GraphVectorStore.traversal_search)\#     

Retrieve documents from traversing this graph store.

First, k nodes are retrieved using a search for each query string. Then, additional nodes are discovered up to the given depth from those starting nodes.

Parameters:     

  * **query** \(_str_\) – The query string.

  * **k** \(_int_\) – The number of Documents to return from the initial search. Defaults to 4. Applies to each of the query strings.

  * **depth** \(_int_\) – The maximum depth of edges to traverse. Defaults to 1.

  * **filter** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to filter the results.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

Collection of retrieved documents.

Return type:     

_Iterable_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)