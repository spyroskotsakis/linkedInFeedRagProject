# Vectara — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.Vectara.html
**Word Count:** 1964
**Links Count:** 503
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# Vectara\#

_class _langchain\_community.vectorstores.vectara.Vectara\(

    _vectara\_customer\_id : str | None = None_,     _vectara\_corpus\_id : str | None = None_,     _vectara\_api\_key : str | None = None_,     _vectara\_api\_timeout : int = 120_,     _source : str = 'langchain'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara)\#     

Vectara API vector store.

> See \(<https://vectara.com>\).

Example               from langchain_community.vectorstores import Vectara          vectorstore = Vectara(         vectara_customer_id=vectara_customer_id,         vectara_corpus_id=vectara_corpus_id,         vectara_api_key=vectara_api_key     )     

Initialize with Vectara API.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(\[vectara\_customer\_id, ...\]\) | Initialize with Vectara API.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_files`\(files\_list\[, metadatas\]\) | Vectara provides a way to add documents directly via our API where pre-processing and chunking occurs internally in an optimal way This method provides a way to use that API in LangChain   `add_texts`\(texts\[, metadatas, doc\_metadata\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_chat`\(config\) | Return a Vectara RAG runnable for chat.   `as_rag`\(config\) | Return a Vectara RAG runnable.   `as_retriever`\(\*\*kwargs\) | return a retriever object.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_files`\(files\[, embedding, metadatas\]\) | Construct Vectara wrapper from raw documents.   `from_texts`\(texts\[, embedding, metadatas\]\) | Construct Vectara wrapper from raw documents.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query, \*\*kwargs\) | Return Vectara documents most similar to query, along with scores.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query, \*\*kwargs\) | Return Vectara documents most similar to query, along with scores.   `vectara_query`\(query, config, \*\*kwargs\) | Run a Vectara query      Parameters:     

  * **vectara\_customer\_id** \(_Optional_ _\[__str_ _\]_\)

  * **vectara\_corpus\_id** \(_Optional_ _\[__str_ _\]_\)

  * **vectara\_api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **vectara\_api\_timeout** \(_int_\)

  * **source** \(_str_\)

\_\_init\_\_\(

    _vectara\_customer\_id : str | None = None_,     _vectara\_corpus\_id : str | None = None_,     _vectara\_api\_key : str | None = None_,     _vectara\_api\_timeout : int = 120_,     _source : str = 'langchain'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.__init__)\#     

Initialize with Vectara API.

Parameters:     

  * **vectara\_customer\_id** \(_str_ _|__None_\)

  * **vectara\_corpus\_id** \(_str_ _|__None_\)

  * **vectara\_api\_key** \(_str_ _|__None_\)

  * **vectara\_api\_timeout** \(_int_\)

  * **source** \(_str_\)

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

add\_files\(

    _files\_list : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.add_files)\#     

Vectara provides a way to add documents directly via our API where pre-processing and chunking occurs internally in an optimal way This method provides a way to use that API in LangChain

Parameters:     

  * **files\_list** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings, each representing a local file path. Files could be text, HTML, PDF, markdown, doc/docx, ppt/pptx, etc. see API docs for full list

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with each file

  * **kwargs** \(_Any_\)

Returns:     

List of ids associated with each of the files indexed

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _doc\_metadata : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **doc\_metadata** \(_dict_ _|__None_\) – optional metadata for the document

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

This function indexes all the input text strings in the Vectara corpus as a single Vectara document, where each input text is considered a “section” and the metadata are associated with each section. if ‘doc\_metadata’ is provided, it is associated with the Vectara document.

Returns:     

document ID of the document added

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **doc\_metadata** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

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

as\_chat\(

    _config : [VectaraQueryConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")_, \) → [VectaraRAG](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRAG.html#langchain_community.vectorstores.vectara.VectaraRAG "langchain_community.vectorstores.vectara.VectaraRAG")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.as_chat)\#     

Return a Vectara RAG runnable for chat.

Parameters:     

**config** \([_VectaraQueryConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")\)

Return type:     

[_VectaraRAG_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRAG.html#langchain_community.vectorstores.vectara.VectaraRAG "langchain_community.vectorstores.vectara.VectaraRAG")

as\_rag\(

    _config : [VectaraQueryConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")_, \) → [VectaraRAG](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRAG.html#langchain_community.vectorstores.vectara.VectaraRAG "langchain_community.vectorstores.vectara.VectaraRAG")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.as_rag)\#     

Return a Vectara RAG runnable.

Parameters:     

**config** \([_VectaraQueryConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")\)

Return type:     

[_VectaraRAG_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRAG.html#langchain_community.vectorstores.vectara.VectaraRAG "langchain_community.vectorstores.vectara.VectaraRAG")

as\_retriever\(

    _\*\* kwargs: Any_, \) → [VectaraRetriever](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRetriever.html#langchain_community.vectorstores.vectara.VectaraRetriever "langchain_community.vectorstores.vectara.VectaraRetriever")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.as_retriever)\#     

return a retriever object.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

[_VectaraRetriever_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraRetriever.html#langchain_community.vectorstores.vectara.VectaraRetriever "langchain_community.vectorstores.vectara.VectaraRetriever")

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

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.delete)\#     

Delete by vector ID or other criteria. :param ids: List of ids to delete.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

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

_classmethod _from\_files\(

    _files : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : List\[dict\] | None = None_,     _\*\* kwargs: Any_, \) → Vectara[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.from_files)\#     

Construct Vectara wrapper from raw documents. This is intended to be a quick way to get started. .. rubric:: Example               from langchain_community.vectorstores import Vectara     vectara = Vectara.from_files(         files_list,         vectara_customer_id=customer_id,         vectara_corpus_id=corpus_id,         vectara_api_key=api_key,     )     

Parameters:     

  * **files** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Vectara_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : List\[dict\] | None = None_,     _\*\* kwargs: Any_, \) → Vectara[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.from_texts)\#     

Construct Vectara wrapper from raw documents. This is intended to be a quick way to get started. .. rubric:: Example               from langchain_community.vectorstores import Vectara     vectara = Vectara.from_texts(         texts,         vectara_customer_id=customer_id,         vectara_corpus_id=corpus_id,         vectara_api_key=api_key,     )     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Vectara_

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

    _query : str_,     _fetch\_k : int = 50_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** – Number of Documents to return. Defaults to 5.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 50

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **kwargs** \(_Any_\) – any other querying variable in VectaraQueryConfig

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

    _query : str_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.similarity_search)\#     

Return Vectara documents most similar to query, along with scores.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **VectaraQueryConfig** \(_any other querying variable in_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query

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

    _query : str_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.similarity_search_with_score)\#     

Return Vectara documents most similar to query, along with scores.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** – Number of Documents to return. Defaults to 10.

  * **like** \(_any other querying variable in VectaraQueryConfig_\)

  * **lambda\_val** \(_-_\) – lexical match parameter for hybrid search.

  * **filter** \(_-_\) – filter string

  * **score\_threshold** \(_-_\) – minimal score threshold for the result.

  * **n\_sentence\_before** \(_-_\) – number of sentences before the matching segment

  * **n\_sentence\_after** \(_-_\) – number of sentences after the matching segment

  * **rerank\_config** \(_-_\) – optional configuration for Reranking \(see RerankConfig dataclass\)

  * **summary\_config** \(_-_\) – optional configuration for summary \(see SummaryConfig dataclass\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

vectara\_query\(

    _query : str_,     _config : [VectaraQueryConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#Vectara.vectara_query)\#     

Run a Vectara query

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **config** \([_VectaraQueryConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html#langchain_community.vectorstores.vectara.VectaraQueryConfig "langchain_community.vectorstores.vectara.VectaraQueryConfig")\) – VectaraQueryConfig object

  * **kwargs** \(_Any_\)

Returns:     

A list of k Documents matching the given query If summary is enabled, last document is the summary text with ‘summary’=True

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using Vectara

  * [Vectara](https://python.langchain.com/docs/integrations/vectorstores/vectara/)

  * [Vectara Chat](https://python.langchain.com/docs/integrations/providers/vectara/vectara_chat/)

  * [Vectara self-querying ](https://python.langchain.com/docs/integrations/retrievers/self_query/vectara_self_query/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)