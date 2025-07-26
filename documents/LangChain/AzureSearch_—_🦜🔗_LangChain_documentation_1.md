# AzureSearch — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azuresearch.AzureSearch.html
**Word Count:** 2775
**Links Count:** 620
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# AzureSearch\#

_class _langchain\_community.vectorstores.azuresearch.AzureSearch\(

    _azure\_search\_endpoint : str_,     _azure\_search\_key : str | None_,     _index\_name : str_,     _embedding\_function : Callable | [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _search\_type : str = 'hybrid'_,     _semantic\_configuration\_name : str | None = None_,     _fields : List\[SearchField\] | None = None_,     _vector\_search : VectorSearch | None = None_,     _semantic\_configurations : SemanticConfiguration | List\[SemanticConfiguration\] | None = None_,     _scoring\_profiles : List\[ScoringProfile\] | None = None_,     _default\_scoring\_profile : str | None = None_,     _cors\_options : CorsOptions | None = None_,     _\*_ ,     _vector\_search\_dimensions : int | None = None_,     _additional\_search\_client\_options : Dict\[str, Any\] | None = None_,     _azure\_ad\_access\_token : str | None = None_,     _azure\_credential : TokenCredential | None = None_,     _azure\_async\_credential : AsyncTokenCredential | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch)\#     

Azure Cognitive Search vector store.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(azure\_search\_endpoint, ...\[, ...\]\) |    ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_embeddings`\(text\_embeddings\[, ...\]\) | Add embeddings to an existing index.   `aadd_texts`\(texts\[, metadatas, keys\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(text\_embeddings\[, metadatas, ...\]\) | Add embeddings to an existing index.   `add_texts`\(texts\[, metadatas, keys\]\) | Add texts data to an existing index.   `adelete`\(\[ids\]\) | Delete by vector ID.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_embeddings`\(text\_embeddings, embedding\) |    `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `ahybrid_max_marginal_relevance_search_with_score`\(query\) | Return docs most similar to query with a hybrid query   `ahybrid_search`\(query\[, k\]\) | Returns the most similar indexed documents to the query text.   `ahybrid_search_with_relevance_scores`\(query\) |    `ahybrid_search_with_score`\(query\[, k, filters\]\) | Return docs most similar to query with a hybrid query.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_with_score`\(query\) | Perform a search and return results that are reordered by MMR.   `as_retriever`\(\*\*kwargs\) | Return AzureSearchVectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asemantic_hybrid_search`\(query\[, k\]\) | Returns the most similar indexed documents to the query text.   `asemantic_hybrid_search_with_score`\(query\[, ...\]\) | Returns the most similar indexed documents to the query text.   `asemantic_hybrid_search_with_score_and_rerank`\(query\) | Return docs most similar to query with a hybrid query.   `asimilarity_search`\(query\[, k, search\_type\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query, \*\[, k\]\) | Run similarity search with distance.   `avector_search`\(query\[, k, filters\]\) | Returns the most similar indexed documents to the query text.   `avector_search_with_score`\(query\[, k, filters\]\) | Return docs most similar to query.   `delete`\(\[ids\]\) | Delete by vector ID.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_embeddings`\(text\_embeddings, embedding\) |    `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Return VectorStore initialized from texts and embeddings.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `hybrid_max_marginal_relevance_search_with_score`\(query\) | Return docs most similar to query with a hybrid query   `hybrid_search`\(query\[, k\]\) | Returns the most similar indexed documents to the query text.   `hybrid_search_with_relevance_scores`\(query\[, ...\]\) |    `hybrid_search_with_score`\(query\[, k, filters\]\) | Return docs most similar to query with a hybrid query.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score`\(query\) | Perform a search and return results that are reordered by MMR.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `semantic_hybrid_search`\(query\[, k\]\) | Returns the most similar indexed documents to the query text.   `semantic_hybrid_search_with_score`\(query\[, ...\]\) | Returns the most similar indexed documents to the query text.   `semantic_hybrid_search_with_score_and_rerank`\(query\) | Return docs most similar to query with a hybrid query.   `similarity_search`\(query\[, k, search\_type\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query, \*\[, k\]\) | Run similarity search with distance.   `vector_search`\(query\[, k, filters\]\) | Returns the most similar indexed documents to the query text.   `vector_search_with_score`\(query\[, k, filters\]\) | Return docs most similar to query.      Parameters:     

  * **azure\_search\_endpoint** \(_str_\)

  * **azure\_search\_key** \(_Optional_ _\[__str_ _\]_\)

  * **index\_name** \(_str_\)

  * **embedding\_function** \(_Union_ _\[__Callable_ _,_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **search\_type** \(_str_\)

  * **semantic\_configuration\_name** \(_Optional_ _\[__str_ _\]_\)

  * **fields** \(_Optional_ _\[__List_ _\[__SearchField_ _\]__\]_\)

  * **vector\_search** \(_Optional_ _\[__VectorSearch_ _\]_\)

  * **semantic\_configurations** \(_Optional_ _\[__Union_ _\[__SemanticConfiguration_ _,__List_ _\[__SemanticConfiguration_ _\]__\]__\]_\)

  * **scoring\_profiles** \(_Optional_ _\[__List_ _\[__ScoringProfile_ _\]__\]_\)

  * **default\_scoring\_profile** \(_Optional_ _\[__str_ _\]_\)

  * **cors\_options** \(_Optional_ _\[__CorsOptions_ _\]_\)

  * **vector\_search\_dimensions** \(_Optional_ _\[__int_ _\]_\)

  * **additional\_search\_client\_options** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **azure\_ad\_access\_token** \(_Optional_ _\[__str_ _\]_\)

  * **azure\_credential** \(_Optional_ _\[__TokenCredential_ _\]_\)

  * **azure\_async\_credential** \(_Optional_ _\[__AsyncTokenCredential_ _\]_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _azure\_search\_endpoint : str_,     _azure\_search\_key : str | None_,     _index\_name : str_,     _embedding\_function : Callable | [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _search\_type : str = 'hybrid'_,     _semantic\_configuration\_name : str | None = None_,     _fields : List\[SearchField\] | None = None_,     _vector\_search : VectorSearch | None = None_,     _semantic\_configurations : SemanticConfiguration | List\[SemanticConfiguration\] | None = None_,     _scoring\_profiles : List\[ScoringProfile\] | None = None_,     _default\_scoring\_profile : str | None = None_,     _cors\_options : CorsOptions | None = None_,     _\*_ ,     _vector\_search\_dimensions : int | None = None_,     _additional\_search\_client\_options : Dict\[str, Any\] | None = None_,     _azure\_ad\_access\_token : str | None = None_,     _azure\_credential : TokenCredential | None = None_,     _azure\_async\_credential : AsyncTokenCredential | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.__init__)\#     

Parameters:     

  * **azure\_search\_endpoint** \(_str_\)

  * **azure\_search\_key** \(_Optional_ _\[__str_ _\]_\)

  * **index\_name** \(_str_\)

  * **embedding\_function** \(_Union_ _\[__Callable_ _,_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **search\_type** \(_str_\)

  * **semantic\_configuration\_name** \(_Optional_ _\[__str_ _\]_\)

  * **fields** \(_Optional_ _\[__List_ _\[__SearchField_ _\]__\]_\)

  * **vector\_search** \(_Optional_ _\[__VectorSearch_ _\]_\)

  * **semantic\_configurations** \(_Optional_ _\[__Union_ _\[__SemanticConfiguration_ _,__List_ _\[__SemanticConfiguration_ _\]__\]__\]_\)

  * **scoring\_profiles** \(_Optional_ _\[__List_ _\[__ScoringProfile_ _\]__\]_\)

  * **default\_scoring\_profile** \(_Optional_ _\[__str_ _\]_\)

  * **cors\_options** \(_Optional_ _\[__CorsOptions_ _\]_\)

  * **vector\_search\_dimensions** \(_Optional_ _\[__int_ _\]_\)

  * **additional\_search\_client\_options** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **azure\_ad\_access\_token** \(_Optional_ _\[__str_ _\]_\)

  * **azure\_credential** \(_Optional_ _\[__TokenCredential_ _\]_\)

  * **azure\_async\_credential** \(_Optional_ _\[__AsyncTokenCredential_ _\]_\)

  * **kwargs** \(_Any_\)

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

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _keys : List\[str\] | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.aadd_embeddings)\#     

Add embeddings to an existing index.

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **keys** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_List_\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _keys : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.aadd_texts)\#     

Async run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** – Optional list

  * **\*\*kwargs** \(_Any_\) – vectorstore specific parameters.

  * **keys** \(_List_ _\[__str_ _\]__|__None_\)

  * **\*\*kwargs**

Returns:     

List of ids from adding the texts into the vectorstore.

Raises:     

  * **ValueError** – If the number of metadatas does not match the number of texts.

  * **ValueError** – If the number of ids does not match the number of texts.

Return type:     

_List_\[str\]

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

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _keys : List\[str\] | None = None_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.add_embeddings)\#     

Add embeddings to an existing index.

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **keys** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _keys : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.add_texts)\#     

Add texts data to an existing index.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **keys** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.adelete)\#     

Delete by vector ID.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool

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

_async classmethod _afrom\_embeddings\(

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _azure\_search\_endpoint : str = ''_,     _azure\_search\_key : str = ''_,     _index\_name : str = 'langchain-index'_,     _fields : List\[SearchField\] | None = None_,     _\*\* kwargs: Any_, \) → AzureSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.afrom_embeddings)\#     

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\)

  * **azure\_search\_endpoint** \(_str_\)

  * **azure\_search\_key** \(_str_\)

  * **index\_name** \(_str_\)

  * **fields** \(_Optional_ _\[__List_ _\[__SearchField_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Return type:     

AzureSearch

_async classmethod _afrom\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _azure\_search\_endpoint : str = ''_,     _azure\_search\_key : str = ''_,     _azure\_ad\_access\_token : str | None = None_,     _index\_name : str = 'langchain-index'_,     _fields : List\[SearchField\] | None = None_,     _\*\* kwargs: Any_, \) → AzureSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.afrom_texts)\#     

Async return VectorStore initialized from texts and embeddings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** – Optional list of IDs associated with the texts.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

  * **azure\_search\_endpoint** \(_str_\)

  * **azure\_search\_key** \(_str_\)

  * **azure\_ad\_access\_token** \(_Optional_ _\[__str_ _\]_\)

  * **index\_name** \(_str_\)

  * **fields** \(_Optional_ _\[__List_ _\[__SearchField_ _\]__\]_\)

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

_async _ahybrid\_max\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.ahybrid_max_marginal_relevance_search_with_score)\#     

Return docs most similar to query with a hybrid query     

and reorder results by MMR.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _,__optional_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **filters** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _ahybrid\_search\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.ahybrid_search)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _ahybrid\_search\_with\_relevance\_scores\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _score\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.ahybrid_search_with_relevance_scores)\#     

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _ahybrid\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.ahybrid_search_with_score)\#     

Return docs most similar to query with a hybrid query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filters** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

_async _amax\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.amax_marginal_relevance_search_with_score)\#     

Perform a search and return results that are reordered by MMR.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _,__optional_\) – How many results to give. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **filters** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar     

to the query and score for each

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

as\_retriever\(

    _\*\* kwargs: Any_, \) → [AzureSearchVectorStoreRetriever](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azuresearch.AzureSearchVectorStoreRetriever.html#langchain_community.vectorstores.azuresearch.AzureSearchVectorStoreRetriever "langchain_community.vectorstores.azuresearch.AzureSearchVectorStoreRetriever")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.as_retriever)\#     

Return AzureSearchVectorStoreRetriever initialized from this VectorStore.

Parameters:     

  * **search\_type** \(_Optional_ _\[__str_ _\]_\) – Overrides the type of search that the Retriever should perform. Defaults to self.search\_type. Can be “similarity”, “hybrid”, or “semantic\_hybrid”.

  * **search\_kwargs** \(_Optional_ _\[__Dict_ _\]_\) – 

Keyword arguments to pass to the search function. Can include things like:

> score\_threshold: Minimum relevance threshold >      >  > for similarity\_score\_threshold >  > fetch\_k: Amount of documents to pass to MMR algorithm \(Default: 20\) lambda\_mult: Diversity of results returned by MMR; >
>> 1 for minimum diversity and 0 for maximum. \(Default: 0.5\) >  > filter: Filter by document metadata

  * **kwargs** \(_Any_\)

Returns:     

Retriever class for VectorStore.

Return type:     

[AzureSearchVectorStoreRetriever](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azuresearch.AzureSearchVectorStoreRetriever.html#langchain_community.vectorstores.azuresearch.AzureSearchVectorStoreRetriever "langchain_community.vectorstores.azuresearch.AzureSearchVectorStoreRetriever")

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

_async _asemantic\_hybrid\_search\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.asemantic_hybrid_search)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filters** – Filtering expression.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asemantic\_hybrid\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _score\_type : Literal\['score', 'reranker\_score'\] = 'score'_,     _\*_ ,     _score\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.asemantic_hybrid_search_with_score)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **score\_type** \(_Literal_ _\[__'score'__,__'reranker\_score'__\]_\) – Must either be “score” or “reranker\_score”. Defaulted to “score”.

  * **filters** – Filtering expression.

  * **score\_threshold** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

A list of documents and their     

corresponding scores.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asemantic\_hybrid\_search\_with\_score\_and\_rerank\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.asemantic_hybrid_search_with_score_and_rerank)\#     

Return docs most similar to query with a hybrid query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filters** \(_str_ _|__None_\) – Filtering expression.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, float\]\]

_async _asimilarity\_search\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _search\_type : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.asimilarity_search)\#     

Async return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **search\_type** \(_str_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _\*_ ,     _score\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.asimilarity_search_with_relevance_scores)\#     

Async return docs and relevance scores in the range \[0, 1\].

0 is dissimilar, 1 is most similar.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – 

kwargs to be passed to similarity search. Should include: score\_threshold: Optional, a floating point value between 0 to 1 to

> filter the resulting set of retrieved docs

  * **score\_threshold** \(_float_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Tuples of \(doc, similarity\_score\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\(

    _query : str_,     _\*_ ,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.asimilarity_search_with_score)\#     

Run similarity search with distance.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _avector\_search\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.avector_search)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filters** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _avector\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.avector_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _,__optional_\) – Number of Documents to return. Defaults to 4.

  * **filters** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar     

to the query and score for each

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.delete)\#     

Delete by vector ID.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool

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

_classmethod _from\_embeddings\(

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _\*_ ,     _azure\_search\_endpoint : str = ''_,     _azure\_search\_key : str = ''_,     _index\_name : str = 'langchain-index'_,     _fields : List\[SearchField\] | None = None_,     _\*\* kwargs: Any_, \) → AzureSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.from_embeddings)\#     

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\)

  * **azure\_search\_endpoint** \(_str_\)

  * **azure\_search\_key** \(_str_\)

  * **index\_name** \(_str_\)

  * **fields** \(_Optional_ _\[__List_ _\[__SearchField_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Return type:     

AzureSearch

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _azure\_search\_endpoint : str = ''_,     _azure\_search\_key : str = ''_,     _azure\_ad\_access\_token : str | None = None_,     _index\_name : str = 'langchain-index'_,     _fields : List\[SearchField\] | None = None_,     _\*\* kwargs: Any_, \) → AzureSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.from_texts)\#     

Return VectorStore initialized from texts and embeddings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** – Optional list of IDs associated with the texts.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

  * **azure\_search\_endpoint** \(_str_\)

  * **azure\_search\_key** \(_str_\)

  * **azure\_ad\_access\_token** \(_Optional_ _\[__str_ _\]_\)

  * **index\_name** \(_str_\)

  * **fields** \(_Optional_ _\[__List_ _\[__SearchField_ _\]__\]_\)

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

hybrid\_max\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.hybrid_max_marginal_relevance_search_with_score)\#     

Return docs most similar to query with a hybrid query     

and reorder results by MMR.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _,__optional_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **filters** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

hybrid\_search\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.hybrid_search)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

hybrid\_search\_with\_relevance\_scores\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _score\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.hybrid_search_with_relevance_scores)\#     

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

hybrid\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.hybrid_search_with_score)\#     

Return docs most similar to query with a hybrid query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filters** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

max\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.max_marginal_relevance_search_with_score)\#     

Perform a search and return results that are reordered by MMR.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _,__optional_\) – How many results to give. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **filters** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar     

to the query and score for each

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

semantic\_hybrid\_search\(

    _query : str_,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.semantic_hybrid_search)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filters** – Filtering expression.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

semantic\_hybrid\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _score\_type : Literal\['score', 'reranker\_score'\] = 'score'_,     _\*_ ,     _score\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.semantic_hybrid_search_with_score)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **score\_type** \(_Literal_ _\[__'score'__,__'reranker\_score'__\]_\) – Must either be “score” or “reranker\_score”. Defaulted to “score”.

  * **filters** – Filtering expression.

  * **score\_threshold** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

A list of documents and their     

corresponding scores.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

semantic\_hybrid\_search\_with\_score\_and\_rerank\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.semantic_hybrid_search_with_score_and_rerank)\#     

Return docs most similar to query with a hybrid query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filters** \(_str_ _|__None_\) – Filtering expression.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float, float\]\]

similarity\_search\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _search\_type : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **search\_type** \(_str_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _\*_ ,     _score\_threshold : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.similarity_search_with_relevance_scores)\#     

Return docs and relevance scores in the range \[0, 1\].

0 is dissimilar, 1 is most similar.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – 

kwargs to be passed to similarity search. Should include: score\_threshold: Optional, a floating point value between 0 to 1 to

> filter the resulting set of retrieved docs.

  * **score\_threshold** \(_float_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Tuples of \(doc, similarity\_score\).

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\(

    _query : str_,     _\*_ ,     _k : int = 4_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.similarity_search_with_score)\#     

Run similarity search with distance.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

vector\_search\(

    _query : str_,     _k : int = 4_,     _\*_ ,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.vector_search)\#     

Returns the most similar indexed documents to the query text.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filters** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

vector\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _filters : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/azuresearch.html#AzureSearch.vector_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_ _,__optional_\) – Number of Documents to return. Defaults to 4.

  * **filters** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar     

to the query and score for each

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using AzureSearch

  * [Azure AI Search](https://python.langchain.com/docs/integrations/vectorstores/azuresearch/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)