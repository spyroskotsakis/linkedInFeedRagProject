# FAISS — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.faiss.FAISS.html
**Word Count:** 2851
**Links Count:** 597
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# FAISS\#

_class _langchain\_community.vectorstores.faiss.FAISS\(

    _embedding\_function : Callable\[\[str\], List\[float\]\] | [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index : Any_,     _docstore : [Docstore](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")_,     _index\_to\_docstore\_id : Dict\[int, str\]_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _normalize\_L2 : bool = False_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.EUCLIDEAN\_DISTANCE_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS)\#     

FAISS vector store integration.

See \[The FAISS Library\]\(<https://arxiv.org/pdf/2401.08281>\) paper.

Setup:     

Install `langchain_community` and `faiss-cpu` python packages.               pip install -qU langchain_community faiss-cpu     

Key init args — indexing params:     

embedding\_function: Embeddings     

Embedding function to use.

Key init args — client params:     

index: Any     

FAISS index to use.

docstore: Docstore     

Docstore to use.

index\_to\_docstore\_id: Dict\[int, str\]     

Mapping of index to docstore id.

Instantiate:                    import faiss     from langchain_community.vectorstores import FAISS     from langchain_community.docstore.in_memory import InMemoryDocstore     from langchain_openai import OpenAIEmbeddings          index = faiss.IndexFlatL2(len(OpenAIEmbeddings().embed_query("hello world")))          vector_store = FAISS(         embedding_function=OpenAIEmbeddings(),         index=index,         docstore= InMemoryDocstore(),         index_to_docstore_id={}     )     

Add Documents:                    from langchain_core.documents import Document          document_1 = Document(page_content="foo", metadata={"baz": "bar"})     document_2 = Document(page_content="thud", metadata={"bar": "baz"})     document_3 = Document(page_content="i will be deleted :(")          documents = [document_1, document_2, document_3]     ids = ["1", "2", "3"]     vector_store.add_documents(documents=documents, ids=ids)     

Delete Documents:                    vector_store.delete(ids=["3"])     

Search:                    results = vector_store.similarity_search(query="thud",k=1)     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'bar': 'baz'}]     

Search with filter:                    results = vector_store.similarity_search(query="thud",k=1,filter={"bar": "baz"})     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'bar': 'baz'}]     

Search with score:                    results = vector_store.similarity_search_with_score(query="qux",k=1)     for doc, score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.335304] foo [{'baz': 'bar'}]     

Async:                    # add documents     # await vector_store.aadd_documents(documents=documents, ids=ids)          # delete documents     # await vector_store.adelete(ids=["3"])          # search     # results = vector_store.asimilarity_search(query="thud",k=1)          # search with score     results = await vector_store.asimilarity_search_with_score(query="qux",k=1)     for doc,score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.335304] foo [{'baz': 'bar'}]     

Use as Retriever:                    retriever = vector_store.as_retriever(         search_type="mmr",         search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},     )     retriever.invoke("thud")                    [Document(metadata={'bar': 'baz'}, page_content='thud')]     

Initialize with necessary components.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(embedding\_function, index, ...\[, ...\]\) | Initialize with necessary components.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(text\_embeddings\[, metadatas, ids\]\) | Add the given texts and embeddings to the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_embeddings`\(text\_embeddings, embedding\) | Construct FAISS wrapper from raw documents asynchronously.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Construct FAISS wrapper from raw documents asynchronously.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance asynchronously.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance asynchronously.   `amax_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs and their similarity scores selected using the maximal marginal   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter, fetch\_k\]\) | Return docs most similar to query asynchronously.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector asynchronously.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query asynchronously.   `asimilarity_search_with_score_by_vector`\(...\) | Return docs most similar to query asynchronously.   `delete`\(\[ids\]\) | Delete by ID.   `deserialize_from_bytes`\(serialized, embeddings, \*\) | Deserialize FAISS index, docstore, and index\_to\_docstore\_id from bytes.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_embeddings`\(text\_embeddings, embedding\) | Construct FAISS wrapper from raw documents.   `from_texts`\(texts, embedding\[, metadatas, ids\]\) | Construct FAISS wrapper from raw documents.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `load_local`\(folder\_path, embeddings\[, ...\]\) | Load FAISS index, docstore, and index\_to\_docstore\_id from disk.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs and their similarity scores selected using the maximal marginal   `merge_from`\(target\) | Merge another FAISS object with the current one.   `save_local`\(folder\_path\[, index\_name\]\) | Save FAISS index, docstore, and index\_to\_docstore\_id to disk.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `serialize_to_bytes`\(\) | Serialize FAISS index, docstore, and index\_to\_docstore\_id to bytes.   `similarity_search`\(query\[, k, filter, fetch\_k\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to query.      Parameters:     

  * **embedding\_function** \(_Union_ _\[__Callable_ _\[__\[__str_ _\]__,__List_ _\[__float_ _\]__\]__,_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **index** \(_Any_\)

  * **docstore** \([_Docstore_](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")\)

  * **index\_to\_docstore\_id** \(_Dict_ _\[__int_ _,__str_ _\]_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

  * **normalize\_L2** \(_bool_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\)

\_\_init\_\_\(

    _embedding\_function : Callable\[\[str\], List\[float\]\] | [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index : Any_,     _docstore : [Docstore](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")_,     _index\_to\_docstore\_id : Dict\[int, str\]_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _normalize\_L2 : bool = False_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.EUCLIDEAN\_DISTANCE_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.__init__)\#     

Initialize with necessary components.

Parameters:     

  * **embedding\_function** \(_Callable_ _\[__\[__str_ _\]__,__List_ _\[__float_ _\]__\]__|_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **index** \(_Any_\)

  * **docstore** \([_Docstore_](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")\)

  * **index\_to\_docstore\_id** \(_Dict_ _\[__int_ _,__str_ _\]_\)

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\)

  * **normalize\_L2** \(_bool_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy")\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.aadd_texts)\#     

Run more texts through the embeddings and add to the vectorstore     

asynchronously.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

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

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.add_embeddings)\#     

Add the given texts and embeddings to the vectorstore.

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\) – Iterable pairs of string and embedding to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of unique IDs.

  * **kwargs** \(_Any_\)

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

_async classmethod _afrom\_embeddings\(

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : Iterable\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → FAISS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.afrom_embeddings)\#     

Construct FAISS wrapper from raw documents asynchronously.

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Iterable_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_FAISS_

_async classmethod _afrom\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → FAISS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.afrom_texts)\#     

Construct FAISS wrapper from raw documents asynchronously.

This is a user friendly interface that:     

  1. Embeds documents.

  2. Creates an in memory docstore

  3. Initializes the FAISS database

This is intended to be a quick way to get started.

Example               from langchain_community.vectorstores import FAISS     from langchain_community.embeddings import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     faiss = await FAISS.afrom_texts(texts, embeddings)     

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_FAISS_

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance asynchronously.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch before filtering \(if needed\) to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance asynchronously.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch before filtering to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _\*_ ,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Callable | Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.amax_marginal_relevance_search_with_score_by_vector)\#     

Return docs and their similarity scores selected using the maximal marginal     

relevance asynchronously.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch before filtering to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Returns:     

List of Documents and similarity scores selected by maximal marginal     

relevance and score for each.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.asimilarity_search)\#     

Return docs most similar to query asynchronously.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – \(Optional\[Dict\[str, str\]\]\): Filter by metadata. Defaults to None.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.asimilarity_search_by_vector)\#     

Return docs most similar to embedding vector asynchronously.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None. If a callable, it must take as input the metadata dict of Document and return a bool.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the embedding.

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

    _query : str_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.asimilarity_search_with_score)\#     

Return docs most similar to query asynchronously.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None. If a callable, it must take as input the metadata dict of Document and return a bool.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **kwargs** \(_Any_\)

Returns:     

List of documents most similar to the query text with L2 distance in float. Lower score represents more similarity.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.asimilarity_search_with_score_by_vector)\#     

Return docs most similar to query asynchronously.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Filter by metadata. Defaults to None. If a callable, it must take as input the metadata dict of Document and return a bool.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **\*\*kwargs** \(_Any_\) – 

kwargs to be passed to similarity search. Can include: score\_threshold: Optional, a floating point value between 0 to 1 to

> filter the resulting set of retrieved docs

Returns:     

List of documents most similar to the query text and L2 distance in float for each. Lower score represents more similarity.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.delete)\#     

Delete by ID. These are the IDs in the vectorstore.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

_classmethod _deserialize\_from\_bytes\(

    _serialized : bytes_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _allow\_dangerous\_deserialization : bool = False_,     _\*\* kwargs: Any_, \) → FAISS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.deserialize_from_bytes)\#     

Deserialize FAISS index, docstore, and index\_to\_docstore\_id from bytes.

Parameters:     

  * **serialized** \(_bytes_\)

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **allow\_dangerous\_deserialization** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_FAISS_

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

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : Iterable\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → FAISS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.from_embeddings)\#     

Construct FAISS wrapper from raw documents.

This is a user friendly interface that:     

  1. Embeds documents.

  2. Creates an in memory docstore

  3. Initializes the FAISS database

This is intended to be a quick way to get started.

Example               from langchain_community.vectorstores import FAISS     from langchain_community.embeddings import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     text_embeddings = embeddings.embed_documents(texts)     text_embedding_pairs = zip(texts, text_embeddings)     faiss = FAISS.from_embeddings(text_embedding_pairs, embeddings)     

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Iterable_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_FAISS_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → FAISS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.from_texts)\#     

Construct FAISS wrapper from raw documents.

This is a user friendly interface that:     

  1. Embeds documents.

  2. Creates an in memory docstore

  3. Initializes the FAISS database

This is intended to be a quick way to get started.

Example               from langchain_community.vectorstores import FAISS     from langchain_community.embeddings import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     faiss = FAISS.from_texts(texts, embeddings)     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_FAISS_

get\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.get_by_ids)\#     

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

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Added in version 0.2.11.

_classmethod _load\_local\(

    _folder\_path : str_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _index\_name : str = 'index'_,     _\*_ ,     _allow\_dangerous\_deserialization : bool = False_,     _\*\* kwargs: Any_, \) → FAISS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.load_local)\#     

Load FAISS index, docstore, and index\_to\_docstore\_id from disk.

Parameters:     

  * **folder\_path** \(_str_\) – folder path to load index, docstore, and index\_to\_docstore\_id from.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embeddings to use when generating queries

  * **index\_name** \(_str_\) – for saving with a specific index file name

  * **allow\_dangerous\_deserialization** \(_bool_\) – whether to allow deserialization of the data which involves loading a pickle file. Pickle files can be modified by malicious actors to deliver a malicious payload that results in execution of arbitrary code on your machine.

  * **kwargs** \(_Any_\)

Return type:     

_FAISS_

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch before filtering \(if needed\) to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch before filtering to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _\*_ ,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Callable | Dict\[str, Any\] | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.max_marginal_relevance_search_with_score_by_vector)\#     

Return docs and their similarity scores selected using the maximal marginal     

relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch before filtering to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Returns:     

List of Documents and similarity scores selected by maximal marginal     

relevance and score for each.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

merge\_from\(

    _target : FAISS_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.merge_from)\#     

Merge another FAISS object with the current one.

Add the target FAISS to the current one.

Parameters:     

**target** \(_FAISS_\) – FAISS object you wish to merge into the current one

Returns:     

None.

Return type:     

None

save\_local\(

    _folder\_path : str_,     _index\_name : str = 'index'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.save_local)\#     

Save FAISS index, docstore, and index\_to\_docstore\_id to disk.

Parameters:     

  * **folder\_path** \(_str_\) – folder path to save index, docstore, and index\_to\_docstore\_id to.

  * **index\_name** \(_str_\) – for saving with a specific index file name

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

serialize\_to\_bytes\(\) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.serialize_to_bytes)\#     

Serialize FAISS index, docstore, and index\_to\_docstore\_id to bytes.

Return type:     

bytes

similarity\_search\(

    _query : str_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.similarity_search)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Callable_ _|__Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – \(Optional\[Dict\[str, str\]\]\): Filter by metadata. Defaults to None.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None. If a callable, it must take as input the metadata dict of Document and return a bool.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the embedding.

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

    _query : str_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.similarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None. If a callable, it must take as input the metadata dict of Document and return a bool.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **kwargs** \(_Any_\)

Returns:     

List of documents most similar to the query text with L2 distance in float. Lower score represents more similarity.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : Callable | Dict\[str, Any\] | None = None_,     _fetch\_k : int = 20_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#FAISS.similarity_search_with_score_by_vector)\#     

Return docs most similar to query.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Union_ _\[__Callable_ _,__Dict_ _\[__str_ _,__Any_ _\]__\]__\]_\) – Filter by metadata. Defaults to None. If a callable, it must take as input the metadata dict of Document and return a bool.

  * **fetch\_k** \(_int_\) – \(Optional\[int\]\) Number of Documents to fetch before filtering. Defaults to 20.

  * **\*\*kwargs** \(_Any_\) – 

kwargs to be passed to similarity search. Can include: score\_threshold: Optional, a floating point value between 0 to 1 to

> filter the resulting set of retrieved docs

Returns:     

List of documents most similar to the query text and L2 distance in float for each. Lower score represents more similarity.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using FAISS

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Caching](https://python.langchain.com/docs/how_to/caching_embeddings/)

  * [Cohere reranker](https://python.langchain.com/docs/integrations/retrievers/cohere-reranker/)

  * [Cross Encoder Reranker](https://python.langchain.com/docs/integrations/document_transformers/cross_encoder_reranker/)

  * [DashScope Reranker](https://python.langchain.com/docs/integrations/document_transformers/dashscope_rerank/)

  * [Facebook - Meta](https://python.langchain.com/docs/integrations/providers/facebook/)

  * [Faiss](https://python.langchain.com/docs/integrations/vectorstores/faiss/)

  * [Faiss \(Async\)](https://python.langchain.com/docs/integrations/vectorstores/faiss_async/)

  * [FlashRank reranker](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/)

  * [Fleet AI Context](https://python.langchain.com/docs/integrations/retrievers/fleet_context/)

  * [How to add values to a chain’s state](https://python.langchain.com/docs/how_to/assign/)

  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)

  * [How to combine results from multiple retrievers](https://python.langchain.com/docs/how_to/ensemble_retriever/)

  * [How to create and query vector stores](https://python.langchain.com/docs/how_to/vectorstores/)

  * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)

  * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to inspect runnables](https://python.langchain.com/docs/how_to/inspect/)

  * [How to invoke runnables in parallel](https://python.langchain.com/docs/how_to/parallel/)

  * [How to load PDFs](https://python.langchain.com/docs/how_to/document_loader_pdf/)

  * [How to pass through arguments from one step to the next](https://python.langchain.com/docs/how_to/passthrough/)

  * [How to select examples by maximal marginal relevance \(MMR\)](https://python.langchain.com/docs/how_to/example_selectors_mmr/)

  * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)

  * [How to use a time-weighted vector store retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)

  * [How to use a vectorstore as a retriever](https://python.langchain.com/docs/how_to/vectorstore_retriever/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

  * [LLMLingua Document Compressor](https://python.langchain.com/docs/integrations/retrievers/llmlingua/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [NVIDIA NIMs ](https://python.langchain.com/docs/integrations/text_embedding/nvidia_ai_endpoints/)

  * [OpenVINO Reranker](https://python.langchain.com/docs/integrations/document_transformers/openvino_rerank/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/providers/ragatouille/)

  * [RankLLM Reranker](https://python.langchain.com/docs/integrations/document_transformers/rankllm-reranker/)

  * [UpTrain](https://python.langchain.com/docs/integrations/callbacks/uptrain/)

  * [Volcengine Reranker](https://python.langchain.com/docs/integrations/document_transformers/volcengine_rerank/)

  * [VoyageAI Reranker](https://python.langchain.com/docs/integrations/document_transformers/voyageai-reranker/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

__On this page   *[/]: Positional-only parameter separator (PEP 570)   *[\*]: Keyword-only parameters separator (PEP 3102)