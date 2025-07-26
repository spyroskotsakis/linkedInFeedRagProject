# VDMS — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vdms.VDMS.html
**Word Count:** 2678
**Links Count:** 551
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# VDMS\#

_class _langchain\_community.vectorstores.vdms.VDMS\(

    _client : vdms.vdms_,     _\*_ ,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : DISTANCE\_METRICS = 'L2'_,     _engine : ENGINES = 'FaissFlat'_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _embedding\_dimensions : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS)\#     

Deprecated since version 0.3.18: Use `:class:`~langchain_vdms.VDMS`` instead. It will not be removed until langchain-community==1.0.0.

Intel Lab’s VDMS for vector-store workloads.

To use, you should have both: \- the `vdms` python package installed \- a host \(str\) and port \(int\) associated with a deployed VDMS Server

Visit [IntelLabs/vdms](https://github.com/IntelLabs/vdms/wiki) more information.

IT IS HIGHLY SUGGESTED TO NORMALIZE YOUR DATA.

Parameters:     

  * **client** \(_vdms.vdms_\) – VDMS Client used to connect to VDMS server

  * **collection\_name** \(_str_\) – Name of data collection \[Default: langchain\]

  * **distance\_strategy** \(_DISTANCE\_METRICS_\) – Method used to calculate distances. VDMS supports “L2” \(euclidean distance\) or “IP” \(inner product\) \[Default: L2\]

  * **engine** \(_ENGINES_\) – Underlying implementation for indexing and computing distances. VDMS supports TileDBDense, TileDBSparse, FaissFlat, FaissIVFFlat, and Flinng \[Default: FaissFlat\]

  * **embedding** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\) – Any embedding function implementing langchain\_core.embeddings.Embeddings interface.

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\) – Function for obtaining relevance score

  * **embedding\_dimensions** \(_Optional_ _\[__int_ _\]_\)

Example               from langchain_huggingface import HuggingFaceEmbeddings     from langchain_community.vectorstores.vdms import VDMS, VDMS_Client          model_name = "sentence-transformers/all-mpnet-base-v2"     vectorstore = VDMS(         client=VDMS_Client("localhost", 55555),         embedding=HuggingFaceEmbeddings(model_name=model_name),         collection_name="langchain-demo",         distance_strategy="L2",         engine="FaissFlat",     )     

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(client, \*\[, embedding, ...\]\) |    ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add`\(collection\_name, texts, embeddings\[, ...\]\) |    `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_from`\(texts, embeddings, ids\[, ...\]\) |    `add_images`\(uris\[, metadatas, ids, ...\]\) | Run more images through the embeddings and add to the vectorstore.   `add_set`\(collection\_name\[, engine, metric\]\) |    `add_texts`\(texts\[, metadatas, ids, batch\_size\]\) | Run more texts through the embeddings and add to the vectorstore.   `add_videos`\(paths\[, texts, metadatas, ids, ...\]\) | Run videos through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `count`\(collection\_name\) |    `decode_image`\(base64\_image\) |    `delete`\(\[ids, collection\_name, constraints\]\) | Delete by ID.   `encode_image`\(image\_path\) |    `from_documents`\(documents\[, embedding, ids, ...\]\) | Create a VDMS vectorstore from a list of documents.   `from_texts`\(texts\[, embedding, metadatas, ...\]\) | Create a VDMS vectorstore from a raw documents.   `get`\(collection\_name\[, constraints, limit, ...\]\) | Gets the collection.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_descriptor_response`\(command\_str, setname\) |    `get_k_candidates`\(setname, fetch\_k\[, ...\]\) |    `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score`\(query\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `query_collection_embeddings`\(\[...\]\) |    `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, fetch\_k, filter\]\) | Run similarity search with VDMS.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Run similarity search with VDMS with distance.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector and similarity score.   `update_document`\(collection\_name, ...\) | Update a document in the collection.   `update_documents`\(collection\_name, ids, documents\) | Update a document in the collection.      \_\_init\_\_\(

    _client : vdms.vdms_,     _\*_ ,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _collection\_name : str = 'langchain'_,     _distance\_strategy : DISTANCE\_METRICS = 'L2'_,     _engine : ENGINES = 'FaissFlat'_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _embedding\_dimensions : int | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.__init__)\#     

Parameters:     

  * **client** \(_vdms.vdms_\)

  * **embedding** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **collection\_name** \(_str_\)

  * **distance\_strategy** \(_DISTANCE\_METRICS_\)

  * **engine** \(_ENGINES_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

  * **embedding\_dimensions** \(_Optional_ _\[__int_ _\]_\)

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

add\(

    _collection\_name : str_,     _texts : List\[str\]_,     _embeddings : List\[List\[float\]\]_,     _metadatas : List\[None\] | List\[Dict\[str, Any\]\] | None = None_,     _ids : List\[str\] | None = None_, \) → List[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.add)\#     

Parameters:     

  * **collection\_name** \(_str_\)

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\)

  * **metadatas** \(_List_ _\[__None_ _\]__|__List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_List_

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

add\_from\(

    _texts : List\[str\]_,     _embeddings : List\[List\[float\]\]_,     _ids : List\[str\]_,     _metadatas : List\[dict\] | None = None_,     _batch\_size : int = 32_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.add_from)\#     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\)

  * **ids** \(_List_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **batch\_size** \(_int_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

add\_images\(

    _uris : List\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _add\_path : bool | None = True_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.add_images)\#     

Run more images through the embeddings and add to the vectorstore.

Images are added as embeddings \(AddDescriptor\) instead of separate entity \(AddImage\) within VDMS to leverage similarity search capability

Parameters:     

  * **uris** \(_List_ _\[__str_ _\]_\) – List of paths to the images to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the images.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

  * **add\_path** \(_bool_ _|__None_\) – Bool to add image path as metadata

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding images into the vectorstore.

Return type:     

_List_\[str\]

add\_set\(

    _collection\_name : str_,     _engine : Literal\['TileDBDense', 'TileDBSparse', 'FaissFlat', 'FaissIVFFlat', 'Flinng'\] = 'FaissFlat'_,     _metric : Literal\['L2', 'IP'\] = 'L2'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.add_set)\#     

Parameters:     

  * **collection\_name** \(_str_\)

  * **engine** \(_Literal_ _\[__'TileDBDense'__,__'TileDBSparse'__,__'FaissFlat'__,__'FaissIVFFlat'__,__'Flinng'__\]_\)

  * **metric** \(_Literal_ _\[__'L2'__,__'IP'__\]_\)

Return type:     

str

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – List of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

add\_videos\(

    _paths : List\[str\]_,     _texts : List\[str\] | None = None_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 1_,     _add\_path : bool | None = True_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.add_videos)\#     

Run videos through the embeddings and add to the vectorstore.

Videos are added as embeddings \(AddDescriptor\) instead of separate entity \(AddVideo\) within VDMS to leverage similarity search capability

Parameters:     

  * **paths** \(_List_ _\[__str_ _\]_\) – List of paths to the videos to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of text associated with the videos.

  * **metadatas** – Optional list of metadatas associated with the videos.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

  * **add\_path** \(_bool_ _|__None_\) – Bool to add video path as metadata

  * **texts** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding videos into the vectorstore.

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

count\(_collection\_name : str_\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.count)\#     

Parameters:     

**collection\_name** \(_str_\)

Return type:     

int

decode\_image\(_base64\_image : str_\) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.decode_image)\#     

Parameters:     

**base64\_image** \(_str_\)

Return type:     

bytes

delete\(

    _ids : List\[str\] | None = None_,     _collection\_name : str | None = None_,     _constraints : Dict | None = None_,     _\*\* kwargs: Any_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.delete)\#     

Delete by ID. These are the IDs in the vectorstore.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **collection\_name** \(_str_ _|__None_\)

  * **constraints** \(_Dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

encode\_image\(_image\_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.encode_image)\#     

Parameters:     

**image\_path** \(_str_\)

Return type:     

str

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _collection\_name : str = 'langchain'_,     _\*\* kwargs: Any_, \) → VDMS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.from_documents)\#     

Create a VDMS vectorstore from a list of documents.

Parameters:     

  * **collection\_name** \(_str_\) – Name of the collection to create.

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of documents to add to vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function. Defaults to None.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of document IDs. Defaults to None.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

  * **kwargs** \(_Any_\)

Returns:     

VDMS vectorstore.

Return type:     

VDMS

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _collection\_name : str = 'langchain'_,     _\*\* kwargs: Any_, \) → VDMS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.from_texts)\#     

Create a VDMS vectorstore from a raw documents.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of texts to add to the collection.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function. Defaults to None.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – List of metadatas. Defaults to None.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of document IDs. Defaults to None.

  * **batch\_size** \(_int_\) – Number of concurrent requests to send to the server.

  * **collection\_name** \(_str_\) – Name of the collection to create.

  * **kwargs** \(_Any_\)

Returns:     

VDMS vectorstore.

Return type:     

VDMS

get\(

    _collection\_name : str_,     _constraints : Dict | None = None_,     _limit : int | None = None_,     _include : List\[str\] = \['metadata'\]_, \) → Tuple\[Any, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.get)\#     

Gets the collection. Get embeddings and their associated data from the data store. If no constraints provided returns all embeddings up to limit.

Parameters:     

  * **constraints** \(_Dict_ _|__None_\) – A dict used to filter results by. E.g. \{“color” : \[“==”, “red”\], “price”: \[“>”, 4.00\]\}. Optional.

  * **limit** \(_int_ _|__None_\) – The number of documents to return. Optional.

  * **include** \(_List_ _\[__str_ _\]_\) – A list of what to include in the results. Can contain “embeddings”, “metadatas”, “documents”. Ids are always included. Defaults to \[“metadatas”, “documents”\]. Optional.

  * **collection\_name** \(_str_\)

Return type:     

_Tuple_\[_Any_ , _Any_\]

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

get\_descriptor\_response\(

    _command\_str : str_,     _setname : str_,     _k\_neighbors : int = 3_,     _fetch\_k : int = 15_,     _constraints : dict | None = None_,     _results : Dict\[str, Any\] | None = None_,     _query\_embedding : List\[float\] | None = None_,     _normalize\_distance : bool = False_, \) → Tuple\[List\[Dict\[str, Any\]\], List\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.get_descriptor_response)\#     

Parameters:     

  * **command\_str** \(_str_\)

  * **setname** \(_str_\)

  * **k\_neighbors** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **constraints** \(_dict_ _|__None_\)

  * **results** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **query\_embedding** \(_List_ _\[__float_ _\]__|__None_\)

  * **normalize\_distance** \(_bool_\)

Return type:     

_Tuple_\[_List_\[_Dict_\[str, _Any_\]\], _List_\]

get\_k\_candidates\(

    _setname : str_,     _fetch\_k : int | None_,     _results : Dict\[str, Any\] | None = None_,     _all\_blobs : List | None = None_,     _normalize : bool | None = False_, \) → Tuple\[List\[Dict\[str, Any\]\], List, float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.get_k_candidates)\#     

Parameters:     

  * **setname** \(_str_\)

  * **fetch\_k** \(_int_ _|__None_\)

  * **results** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **all\_blobs** \(_List_ _|__None_\)

  * **normalize** \(_bool_ _|__None_\)

Return type:     

_Tuple_\[_List_\[_Dict_\[str, _Any_\]\], _List_ , float\]

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 3_,     _fetch\_k : int = 15_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Query to look up. Text or path for image or video.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 3_,     _fetch\_k : int = 15_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 3_,     _fetch\_k : int = 15_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.max_marginal_relevance_search_with_score)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Query to look up. Text or path for image or video.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 3_,     _fetch\_k : int = 15_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.max_marginal_relevance_search_with_score_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

query\_collection\_embeddings\(

    _query\_embeddings : List\[List\[float\]\] | None = None_,     _collection\_name : str | None = None_,     _n\_results : int = 3_,     _fetch\_k : int = 15_,     _filter : None | Dict\[str, Any\] = None_,     _results : None | Dict\[str, Any\] = None_,     _normalize\_distance : bool = False_,     _\*\* kwargs: Any_, \) → List\[Tuple\[Dict\[str, Any\], List\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.query_collection_embeddings)\#     

Parameters:     

  * **query\_embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]__|__None_\)

  * **collection\_name** \(_str_ _|__None_\)

  * **n\_results** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **filter** \(_None_ _|__Dict_ _\[__str_ _,__Any_ _\]_\)

  * **results** \(_None_ _|__Dict_ _\[__str_ _,__Any_ _\]_\)

  * **normalize\_distance** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[_Tuple_\[_Dict_\[str, _Any_\], _List_\]\]

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

    _query : str_,     _k : int = 3_,     _fetch\_k : int = 15_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.similarity_search)\#     

Run similarity search with VDMS.

Parameters:     

  * **query** \(_str_\) – Query to look up. Text or path for image or video.

  * **k** \(_int_\) – Number of results to return. Defaults to 3.

  * **fetch\_k** \(_int_\) – Number of candidates to fetch for knn \(>= k\).

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of documents most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 3_,     _fetch\_k : int = 15_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.similarity_search_by_vector)\#     

Return docs most similar to embedding vector. :param embedding: Embedding to look up documents similar to. :type embedding: List\[float\] :param k: Number of Documents to return. Defaults to 3. :type k: int :param fetch\_k: Number of candidates to fetch for knn \(>= k\). :type fetch\_k: int :param filter: Filter by metadata. Defaults to None. :type filter: Optional\[Dict\[str, str\]\]

Returns:     

List of Documents most similar to the query vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **filter** \(_Dict_ _\[__str_ _,__List_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 3_,     _fetch\_k : int = 15_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.similarity_search_with_score)\#     

Run similarity search with VDMS with distance.

Parameters:     

  * **query** \(_str_\) – Query to look up. Text or path for image or video.

  * **k** \(_int_\) – Number of results to return. Defaults to 3.

  * **fetch\_k** \(_int_\) – Number of candidates to fetch for knn \(>= k\).

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of documents most similar to the query text and cosine distance in float for each. Lower score represents more similarity.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 3_,     _fetch\_k : int = 15_,     _filter : Dict\[str, List\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector and similarity score.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 3.

  * **fetch\_k** \(_int_\) – Number of candidates to fetch for knn \(>= k\).

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of documents most similar to the query text. Lower score represents more similarity.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

update\_document\(

    _collection\_name : str_,     _document\_id : str_,     _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.update_document)\#     

Update a document in the collection.

Parameters:     

  * **document\_id** \(_str_\) – ID of the document to update.

  * **document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\) – Document to update.

  * **collection\_name** \(_str_\)

Return type:     

None

update\_documents\(

    _collection\_name : str_,     _ids : List\[str\]_,     _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vdms.html#VDMS.update_documents)\#     

Update a document in the collection.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]_\) – List of ids of the document to update.

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of documents to update.

  * **collection\_name** \(_str_\)

Return type:     

None

Examples using VDMS

  * [Intel’s Visual Data Management System \(VDMS\)](https://python.langchain.com/docs/integrations/vectorstores/vdms/)

  * [VDMS](https://python.langchain.com/docs/integrations/providers/vdms/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)