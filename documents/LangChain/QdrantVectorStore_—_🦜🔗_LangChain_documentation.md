# QdrantVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.QdrantVectorStore.html
**Word Count:** 1838
**Links Count:** 276
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# QdrantVectorStore\#

_class _langchain\_qdrant.qdrant.QdrantVectorStore\(

    _client : QdrantClient_,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _retrieval\_mode : [RetrievalMode](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode") = RetrievalMode.DENSE_,     _vector\_name : str = ''_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _distance : Distance = Distance.COSINE_,     _sparse\_embedding : [SparseEmbeddings](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") | None = None_,     _sparse\_vector\_name : str = 'langchain-sparse'_,     _validate\_embeddings : bool = True_,     _validate\_collection\_config : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore)\#     

Qdrant vector store integration.

Setup:     

Install `langchain-qdrant` package.               pip install -qU langchain-qdrant     

Key init args — indexing params:     

collection\_name: str     

Name of the collection.

embedding: Embeddings     

Embedding function to use.

sparse\_embedding: SparseEmbeddings     

Optional sparse embedding function to use.

Key init args — client params:     

client: QdrantClient     

Qdrant client to use.

retrieval\_mode: RetrievalMode     

Retrieval mode to use.

Instantiate:                    from langchain_qdrant import QdrantVectorStore     from qdrant_client import QdrantClient     from qdrant_client.http.models import Distance, VectorParams     from langchain_openai import OpenAIEmbeddings          client = QdrantClient(":memory:")          client.create_collection(         collection_name="demo_collection",         vectors_config=VectorParams(size=1536, distance=Distance.COSINE),     )          vector_store = QdrantVectorStore(         client=client,         collection_name="demo_collection",         embedding=OpenAIEmbeddings(),     )     

Add Documents:                    from langchain_core.documents import Document     from uuid import uuid4          document_1 = Document(page_content="foo", metadata={"baz": "bar"})     document_2 = Document(page_content="thud", metadata={"bar": "baz"})     document_3 = Document(page_content="i will be deleted :(")          documents = [document_1, document_2, document_3]     ids = [str(uuid4()) for _ in range(len(documents))]     vector_store.add_documents(documents=documents, ids=ids)     

Delete Documents:                    vector_store.delete(ids=[ids[-1]])     

Search:                    results = vector_store.similarity_search(query="thud",k=1)     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'bar': 'baz', '_id': '0d706099-6dd9-412a-9df6-a71043e020de', '_collection_name': 'demo_collection'}]     

Search with filter:                    from qdrant_client.http import models          results = vector_store.similarity_search(query="thud",k=1,filter=models.Filter(must=[models.FieldCondition(key="metadata.bar", match=models.MatchValue(value="baz"),)]))     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'bar': 'baz', '_id': '0d706099-6dd9-412a-9df6-a71043e020de', '_collection_name': 'demo_collection'}]     

Search with score:                    results = vector_store.similarity_search_with_score(query="qux",k=1)     for doc, score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.832268] foo [{'baz': 'bar', '_id': '44ec7094-b061-45ac-8fbf-014b0f18e8aa', '_collection_name': 'demo_collection'}]     

Async:                    # add documents     # await vector_store.aadd_documents(documents=documents, ids=ids)          # delete documents     # await vector_store.adelete(ids=["3"])          # search     # results = vector_store.asimilarity_search(query="thud",k=1)          # search with score     results = await vector_store.asimilarity_search_with_score(query="qux",k=1)     for doc,score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.832268] foo [{'baz': 'bar', '_id': '44ec7094-b061-45ac-8fbf-014b0f18e8aa', '_collection_name': 'demo_collection'}]     

Use as Retriever:                    retriever = vector_store.as_retriever(         search_type="mmr",         search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},     )     retriever.invoke("thud")                    [Document(metadata={'bar': 'baz', '_id': '0d706099-6dd9-412a-9df6-a71043e020de', '_collection_name': 'demo_collection'}, page_content='thud')]     

Initialize a new instance of QdrantVectorStore.

Example               

qdrant = Qdrant\(     

client=client, collection\_name=”my-collection”, embedding=OpenAIEmbeddings\(\), retrieval\_mode=RetrievalMode.HYBRID, sparse\_embedding=FastEmbedSparse\(\),

\)

Attributes

`CONTENT_KEY` |    ---|---   `METADATA_KEY` |    `SPARSE_VECTOR_NAME` |    `VECTOR_NAME` |    `client` | Get the Qdrant client instance that is being used.   `embeddings` | Get the dense embeddings instance that is being used.   `sparse_embeddings` | Get the sparse embeddings instance that is being used.      Methods

`__init__`\(client, collection\_name\[, ...\]\) | Initialize a new instance of QdrantVectorStore.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids, batch\_size\]\) | Add texts with embeddings to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `construct_instance`\(\[embedding, ...\]\) |    `delete`\(\[ids\]\) | Delete documents by their ids.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_existing_collection`\(collection\_name\[, ...\]\) | Construct an instance of `QdrantVectorStore` from an existing collection without adding any data.   `from_texts`\(texts\[, embedding, metadatas, ...\]\) | Construct an instance of `QdrantVectorStore` from a list of texts.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance with dense vectors.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance with dense vectors.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, ...\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs most similar to embedding vector.      Parameters:     

  * **client** \(_QdrantClient_\)

  * **collection\_name** \(_str_\)

  * **embedding** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **retrieval\_mode** \([_RetrievalMode_](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode")\)

  * **vector\_name** \(_str_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **distance** \(_models.Distance_\)

  * **sparse\_embedding** \(_Optional_ _\[_[_SparseEmbeddings_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") _\]_\)

  * **sparse\_vector\_name** \(_str_\)

  * **validate\_embeddings** \(_bool_\)

  * **validate\_collection\_config** \(_bool_\)

\_\_init\_\_\(

    _client : QdrantClient_,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _retrieval\_mode : [RetrievalMode](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode") = RetrievalMode.DENSE_,     _vector\_name : str = ''_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _distance : Distance = Distance.COSINE_,     _sparse\_embedding : [SparseEmbeddings](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") | None = None_,     _sparse\_vector\_name : str = 'langchain-sparse'_,     _validate\_embeddings : bool = True_,     _validate\_collection\_config : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.__init__)\#     

Initialize a new instance of QdrantVectorStore.

Example               

qdrant = Qdrant\(     

client=client, collection\_name=”my-collection”, embedding=OpenAIEmbeddings\(\), retrieval\_mode=RetrievalMode.HYBRID, sparse\_embedding=FastEmbedSparse\(\),

\)

Parameters:     

  * **client** \(_QdrantClient_\)

  * **collection\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **retrieval\_mode** \([_RetrievalMode_](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode")\)

  * **vector\_name** \(_str_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **distance** \(_Distance_\)

  * **sparse\_embedding** \([_SparseEmbeddings_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") _|__None_\)

  * **sparse\_vector\_name** \(_str_\)

  * **validate\_embeddings** \(_bool_\)

  * **validate\_collection\_config** \(_bool_\)

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

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : Sequence\[str | int\] | None = None_,     _batch\_size : int = 64_,     _\*\* kwargs: Any_, \) → list\[str | int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.add_texts)\#     

Add texts with embeddings to the vectorstore.

Returns:     

List of ids from adding the texts into the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_Sequence_ _\[__str_ _|__int_ _\]__|__None_\)

  * **batch\_size** \(_int_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[str | int\]

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

_classmethod _construct\_instance\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _retrieval\_mode : [RetrievalMode](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode") = RetrievalMode.DENSE_,     _sparse\_embedding : [SparseEmbeddings](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") | None = None_,     _client\_options : dict\[str, Any\] = \{\}_,     _collection\_name : str | None = None_,     _distance : Distance = Distance.COSINE_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str = ''_,     _sparse\_vector\_name : str = 'langchain-sparse'_,     _force\_recreate : bool = False_,     _collection\_create\_options : dict\[str, Any\] = \{\}_,     _vector\_params : dict\[str, Any\] = \{\}_,     _sparse\_vector\_params : dict\[str, Any\] = \{\}_,     _validate\_embeddings : bool = True_,     _validate\_collection\_config : bool = True_, \) → QdrantVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.construct_instance)\#     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **retrieval\_mode** \([_RetrievalMode_](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode")\)

  * **sparse\_embedding** \([_SparseEmbeddings_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") _|__None_\)

  * **client\_options** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **collection\_name** \(_str_ _|__None_\)

  * **distance** \(_Distance_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **vector\_name** \(_str_\)

  * **sparse\_vector\_name** \(_str_\)

  * **force\_recreate** \(_bool_\)

  * **collection\_create\_options** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **vector\_params** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **sparse\_vector\_params** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **validate\_embeddings** \(_bool_\)

  * **validate\_collection\_config** \(_bool_\)

Return type:     

_QdrantVectorStore_

delete\(

    _ids : list\[str | int\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.delete)\#     

Delete documents by their ids.

Parameters:     

  * **ids** \(_list_ _\[__str_ _|__int_ _\]__|__None_\) – List of ids to delete.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise.

Return type:     

bool | None

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

_classmethod _from\_existing\_collection\(

    _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _retrieval\_mode : [RetrievalMode](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode") = RetrievalMode.DENSE_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : int | None = None_,     _host : str | None = None_,     _path : str | None = None_,     _distance : Distance = Distance.COSINE_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str = ''_,     _sparse\_vector\_name : str = 'langchain-sparse'_,     _sparse\_embedding : [SparseEmbeddings](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") | None = None_,     _validate\_embeddings : bool = True_,     _validate\_collection\_config : bool = True_,     _\*\* kwargs: Any_, \) → QdrantVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.from_existing_collection)\#     

Construct an instance of `QdrantVectorStore` from an existing collection without adding any data.

Returns:     

A new instance of `QdrantVectorStore`.

Return type:     

QdrantVectorStore

Parameters:     

  * **collection\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **retrieval\_mode** \([_RetrievalMode_](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode")\)

  * **location** \(_str_ _|__None_\)

  * **url** \(_str_ _|__None_\)

  * **port** \(_int_ _|__None_\)

  * **grpc\_port** \(_int_\)

  * **prefer\_grpc** \(_bool_\)

  * **https** \(_bool_ _|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **prefix** \(_str_ _|__None_\)

  * **timeout** \(_int_ _|__None_\)

  * **host** \(_str_ _|__None_\)

  * **path** \(_str_ _|__None_\)

  * **distance** \(_Distance_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **vector\_name** \(_str_\)

  * **sparse\_vector\_name** \(_str_\)

  * **sparse\_embedding** \([_SparseEmbeddings_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") _|__None_\)

  * **validate\_embeddings** \(_bool_\)

  * **validate\_collection\_config** \(_bool_\)

  * **kwargs** \(_Any_\)

_classmethod _from\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : list\[dict\] | None = None_,     _ids : Sequence\[str | int\] | None = None_,     _collection\_name : str | None = None_,     _location : str | None = None_,     _url : str | None = None_,     _port : int | None = 6333_,     _grpc\_port : int = 6334_,     _prefer\_grpc : bool = False_,     _https : bool | None = None_,     _api\_key : str | None = None_,     _prefix : str | None = None_,     _timeout : int | None = None_,     _host : str | None = None_,     _path : str | None = None_,     _distance : Distance = Distance.COSINE_,     _content\_payload\_key : str = 'page\_content'_,     _metadata\_payload\_key : str = 'metadata'_,     _vector\_name : str = ''_,     _retrieval\_mode : [RetrievalMode](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode") = RetrievalMode.DENSE_,     _sparse\_embedding : [SparseEmbeddings](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") | None = None_,     _sparse\_vector\_name : str = 'langchain-sparse'_,     _collection\_create\_options : dict\[str, Any\] = \{\}_,     _vector\_params : dict\[str, Any\] = \{\}_,     _sparse\_vector\_params : dict\[str, Any\] = \{\}_,     _batch\_size : int = 64_,     _force\_recreate : bool = False_,     _validate\_embeddings : bool = True_,     _validate\_collection\_config : bool = True_,     _\*\* kwargs: Any_, \) → QdrantVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.from_texts)\#     

Construct an instance of `QdrantVectorStore` from a list of texts.

This is a user-friendly interface that: 1\. Creates embeddings, one for each text 2\. Creates a Qdrant collection if it doesn’t exist. 3\. Adds the text embeddings to the Qdrant database

This is intended to be a quick way to get started.

Example               

from langchain\_qdrant import Qdrant from langchain\_openai import OpenAIEmbeddings embeddings = OpenAIEmbeddings\(\) qdrant = Qdrant.from\_texts\(texts, embeddings, url=”<http://localhost:6333>”\)

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\)

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_Sequence_ _\[__str_ _|__int_ _\]__|__None_\)

  * **collection\_name** \(_str_ _|__None_\)

  * **location** \(_str_ _|__None_\)

  * **url** \(_str_ _|__None_\)

  * **port** \(_int_ _|__None_\)

  * **grpc\_port** \(_int_\)

  * **prefer\_grpc** \(_bool_\)

  * **https** \(_bool_ _|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **prefix** \(_str_ _|__None_\)

  * **timeout** \(_int_ _|__None_\)

  * **host** \(_str_ _|__None_\)

  * **path** \(_str_ _|__None_\)

  * **distance** \(_Distance_\)

  * **content\_payload\_key** \(_str_\)

  * **metadata\_payload\_key** \(_str_\)

  * **vector\_name** \(_str_\)

  * **retrieval\_mode** \([_RetrievalMode_](https://python.langchain.com/api_reference/qdrant/qdrant/langchain_qdrant.qdrant.RetrievalMode.html#langchain_qdrant.qdrant.RetrievalMode "langchain_qdrant.qdrant.RetrievalMode")\)

  * **sparse\_embedding** \([_SparseEmbeddings_](https://python.langchain.com/api_reference/qdrant/sparse_embeddings/langchain_qdrant.sparse_embeddings.SparseEmbeddings.html#langchain_qdrant.sparse_embeddings.SparseEmbeddings "langchain_qdrant.sparse_embeddings.SparseEmbeddings") _|__None_\)

  * **sparse\_vector\_name** \(_str_\)

  * **collection\_create\_options** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **vector\_params** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **sparse\_vector\_params** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **batch\_size** \(_int_\)

  * **force\_recreate** \(_bool_\)

  * **validate\_embeddings** \(_bool_\)

  * **validate\_collection\_config** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_QdrantVectorStore_

get\_by\_ids\(

    _ids : Sequence\[str | int\]_,     _/_ , \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.get_by_ids)\#     

Get documents by their IDs.

The returned documents are expected to have the ID field set to the ID of the document in the vector store.

Fewer documents may be returned than requested if some IDs are not found or if there are duplicated IDs.

Users should not assume that the order of the returned documents matches the order of the input IDs. Instead, users should rely on the ID field of the returned documents.

This method should **NOT** raise exceptions if no documents are found for some IDs.

Parameters:     

**ids** \(_Sequence_ _\[__str_ _|__int_ _\]_\) – List of ids to retrieve.

Returns:     

List of Documents.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Added in version 0.2.11.

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance with dense vectors.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Returns:     

List of Documents selected by maximal marginal relevance.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance with dense vectors.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Returns:     

List of Documents selected by maximal marginal relevance.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.max_marginal_relevance_search_with_score_by_vector)\#     

Return docs selected using the maximal marginal relevance. Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Returns:     

List of Documents selected by maximal marginal relevance and distance for each.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _hybrid\_fusion : FusionQuery | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.similarity_search)\#     

Return docs most similar to query.

Returns:     

List of Documents most similar to the query.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **offset** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **hybrid\_fusion** \(_FusionQuery_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Returns:     

List of Documents most similar to the query.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **offset** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 4_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _hybrid\_fusion : FusionQuery | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.similarity_search_with_score)\#     

Return docs most similar to query.

Returns:     

List of documents most similar to the query text and distance for each.

Parameters:     

  * **query** \(_str_\)

  * **k** \(_int_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **offset** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **hybrid\_fusion** \(_FusionQuery_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : Filter | None = None_,     _search\_params : SearchParams | None = None_,     _offset : int = 0_,     _score\_threshold : float | None = None_,     _consistency : Annotated\[int, Strict\(strict=True\)\] | ReadConsistencyType | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_qdrant/qdrant.html#QdrantVectorStore.similarity_search_with_score_by_vector)\#     

Return docs most similar to embedding vector.

Returns:     

List of Documents most similar to the query and distance for each.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **filter** \(_Filter_ _|__None_\)

  * **search\_params** \(_SearchParams_ _|__None_\)

  * **offset** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **consistency** \(_Annotated_ _\[__int_ _,__Strict_ _\(__strict=True_ _\)__\]__|__ReadConsistencyType_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)