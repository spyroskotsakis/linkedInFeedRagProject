# PineconeSparseVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/pinecone/vectorstores_sparse/langchain_pinecone.vectorstores_sparse.PineconeSparseVectorStore.html
**Word Count:** 2529
**Links Count:** 276
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# PineconeSparseVectorStore\#

_class _langchain\_pinecone.vectorstores\_sparse.PineconeSparseVectorStore\(

    _index : Any | None = None_,     _embedding : [PineconeSparseEmbeddings](https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeSparseEmbeddings.html#langchain_pinecone.embeddings.PineconeSparseEmbeddings "langchain_pinecone.embeddings.PineconeSparseEmbeddings") | None = None_,     _text\_key : str | None = 'text'_,     _namespace : str | None = None_,     _distance\_strategy : DistanceStrategy | None = DistanceStrategy.COSINE_,     _\*_ ,     _pinecone\_api\_key : str | None = None_,     _index\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore)\#     

Pinecone sparse vector store integration.

This class extends PineconeVectorStore to support sparse vector representations. It requires a Pinecone sparse index and PineconeSparseEmbeddings.

Setup:     

``python # Install required packages pip install langchain-pinecone pinecone-client ``

Key init args - indexing params:     

text\_key \(str\): The metadata key where the document text will be stored. namespace \(str\): Pinecone namespace to use. distance\_strategy \(DistanceStrategy\): Strategy for computing distances.

Key init args - client params:     

index \(pinecone.Index\): A Pinecone sparse index. embedding \(PineconeSparseEmbeddings\): A sparse embeddings model. pinecone\_api\_key \(str\): The Pinecone API key. index\_name \(str\): The name of the Pinecone index.

See full list of supported init args and their descriptions in the params section.

Instantiate:     

\`\`\`python from pinecone import Pinecone from langchain\_pinecone import PineconeSparseVectorStore from langchain\_pinecone.embeddings import PineconeSparseEmbeddings

\# Initialize Pinecone client pc = Pinecone\(api\_key=”your-api-key”\)

\# Get your sparse index index = pc.Index\(“your-sparse-index-name”\)

\# Initialize embedding function embeddings = PineconeSparseEmbeddings\(\)

\# Create vector store vectorstore = PineconeSparseVectorStore\(

> index=index, embedding=embeddings, text\_key=”content”, namespace=”my-namespace”

Add Documents:     

\`\`\`python from langchain\_core.documents import Document

docs = \[     

Document\(page\_content=”This is a sparse vector example”\), Document\(page\_content=”Another document for testing”\)

\]

\# Option 1: Add from Document objects vectorstore.add\_documents\(docs\)

\# Option 2: Add from texts texts = \[“Text 1”, “Text 2”\] metadatas = \[\{“source”: “source1”\}, \{“source”: “source2”\}\] vectorstore.add\_texts\(texts, metadatas=metadatas\) \`\`\`

Update Documents:     

Update documents by re-adding them with the same IDs. \`\`\`python ids = \[“id1”, “id2”\] texts = \[“Updated text 1”, “Updated text 2”\] metadatas = \[\{“source”: “updated\_source1”\}, \{“source”: “updated\_source2”\}\]

vectorstore.add\_texts\(texts, metadatas=metadatas, ids=ids\) \`\`\`

Delete Documents:     

\`\`\`python \# Delete by IDs vectorstore.delete\(ids=\[“id1”, “id2”\]\)

\# Delete by filter vectorstore.delete\(filter=\{“source”: “source1”\}\)

\# Delete all documents in a namespace vectorstore.delete\(delete\_all=True, namespace=”my-namespace”\) \`\`\`

Search:     

\`\`\`python \# Search for similar documents docs = vectorstore.similarity\_search\(“query text”, k=5\)

\# Search with filters docs = vectorstore.similarity\_search\(

> “query text”, k=5, filter=\{“source”: “source1”\}

\)

\# Maximal marginal relevance search for diversity docs = vectorstore.max\_marginal\_relevance\_search\(

> “query text”, k=5, fetch\_k=20, lambda\_mult=0.5

Search with score:     

\`\`\`python \# Search with relevance scores docs\_and\_scores = vectorstore.similarity\_search\_with\_score\(

> “query text”, k=5

\)

for doc, score in docs\_and\_scores:     

print\(f”Score: \{score\}, Document: \{doc.page\_content\}”\)

\`\`\`

Use as Retriever:     

\`\`\`python \# Create a retriever retriever = vectorstore.as\_retriever\(\)

\# Customize retriever retriever = vectorstore.as\_retriever\(

> search\_type=”mmr”, search\_kwargs=\{“k”: 5, “fetch\_k”: 20, “lambda\_mult”: 0.5\}, filter=\{“source”: “source1”\}

\)

\# Use the retriever docs = retriever.get\_relevant\_documents\(“query text”\) \`\`\`

Attributes

`async_index` | Get asynchronous index instance.   ---|---   `embeddings` | Access the query embedding object if available.   `index` | Get synchronous index instance.      Methods

`__init__`\(\[index, embedding, text\_key, ...\]\) |    ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, ...\]\) | Asynchronously run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, ids, ...\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids, delete\_all, namespace, filter\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance asynchronously.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter, namespace\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_by_vector_with_score`\(...\) | Return pinecone documents most similar to embedding, along with scores asynchronously.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Asynchronously return pinecone documents most similar to query, along with scores.   `delete`\(\[ids, delete\_all, namespace, filter\]\) | Delete by vector IDs or filter.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_existing_index`\(index\_name, embedding\[, ...\]\) | Load pinecone vectorstore from index name.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Construct Pinecone wrapper from raw documents.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_pinecone_index`\(index\_name\[, ...\]\) | Return a Pinecone Index instance.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, namespace\]\) | Return pinecone documents most similar to query.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_by_vector_with_score`\(...\) | Return pinecone documents most similar to embedding, along with scores.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return pinecone documents most similar to query, along with scores.      Parameters:     

  * **index** \(_Optional_ _\[__Any_ _\]_\)

  * **embedding** \(_Optional_ _\[_[_PineconeSparseEmbeddings_](https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeSparseEmbeddings.html#langchain_pinecone.embeddings.PineconeSparseEmbeddings "langchain_pinecone.embeddings.PineconeSparseEmbeddings") _\]_\)

  * **text\_key** \(_Optional_ _\[__str_ _\]_\)

  * **namespace** \(_Optional_ _\[__str_ _\]_\)

  * **distance\_strategy** \(_Optional_ _\[_[_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _\]_\)

  * **pinecone\_api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **index\_name** \(_Optional_ _\[__str_ _\]_\)

\_\_init\_\_\(

    _index : Any | None = None_,     _embedding : [PineconeSparseEmbeddings](https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeSparseEmbeddings.html#langchain_pinecone.embeddings.PineconeSparseEmbeddings "langchain_pinecone.embeddings.PineconeSparseEmbeddings") | None = None_,     _text\_key : str | None = 'text'_,     _namespace : str | None = None_,     _distance\_strategy : DistanceStrategy | None = DistanceStrategy.COSINE_,     _\*_ ,     _pinecone\_api\_key : str | None = None_,     _index\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.__init__)\#     

Parameters:     

  * **index** \(_Any_ _|__None_\)

  * **embedding** \([_PineconeSparseEmbeddings_](https://python.langchain.com/api_reference/pinecone/embeddings/langchain_pinecone.embeddings.PineconeSparseEmbeddings.html#langchain_pinecone.embeddings.PineconeSparseEmbeddings "langchain_pinecone.embeddings.PineconeSparseEmbeddings") _|__None_\)

  * **text\_key** \(_str_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **distance\_strategy** \(_DistanceStrategy_ _|__None_\)

  * **pinecone\_api\_key** \(_str_ _|__None_\)

  * **index\_name** \(_str_ _|__None_\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _namespace : str | None = None_,     _batch\_size : int = 32_,     _embedding\_chunk\_size : int = 1000_,     _\*_ ,     _id\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.aadd_texts)\#     

Asynchronously run more texts through the embeddings and add to the vectorstore.

Upsert optimization is done by chunking the embeddings and upserting them. This is done to avoid memory issues and optimize using HTTP based embeddings. For OpenAI embeddings, use pool\_threads>4 when constructing the pinecone.Index, embedding\_chunk\_size>1000 and batch\_size~64 for best performance. :param texts: Iterable of strings to add to the vectorstore. :param metadatas: Optional list of metadatas associated with the texts. :param ids: Optional list of ids to associate with the texts. :param namespace: Optional pinecone namespace to add the texts to. :param batch\_size: Batch size to use when adding the texts to the vectorstore. :param embedding\_chunk\_size: Chunk size to use when embedding the texts. :param id\_prefix: Optional string to use as an ID prefix when upserting vectors.

Returns:     

List of ids from adding the texts into the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **batch\_size** \(_int_\)

  * **embedding\_chunk\_size** \(_int_\)

  * **id\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _namespace : str | None = None_,     _batch\_size : int = 32_,     _embedding\_chunk\_size : int = 1000_,     _\*_ ,     _async\_req : bool = True_,     _id\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Upsert optimization is done by chunking the embeddings and upserting them. This is done to avoid memory issues and optimize using HTTP based embeddings. For OpenAI embeddings, use pool\_threads>4 when constructing the pinecone.Index, embedding\_chunk\_size>1000 and batch\_size~64 for best performance. :param texts: Iterable of strings to add to the vectorstore. :param metadatas: Optional list of metadatas associated with the texts. :param ids: Optional list of ids to associate with the texts. :param namespace: Optional pinecone namespace to add the texts to. :param batch\_size: Batch size to use when adding the texts to the vectorstore. :param embedding\_chunk\_size: Chunk size to use when embedding the texts. :param async\_req: Whether runs asynchronously. Defaults to True. :param id\_prefix: Optional string to use as an ID prefix when upserting vectors.

Returns:     

List of ids from adding the texts into the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **batch\_size** \(_int_\)

  * **embedding\_chunk\_size** \(_int_\)

  * **async\_req** \(_bool_\)

  * **id\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _delete\_all : bool | None = None_,     _namespace : str | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.adelete)\#     

Async delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete. If None, delete all. Default is None.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

  * **delete\_all** \(_bool_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **\*\*kwargs**

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _text\_key : str = 'text'_,     _namespace : str | None = None_,     _index\_name : str | None = None_,     _upsert\_kwargs : dict | None = None_,     _embeddings\_chunk\_size : int = 1000_,     _\*_ ,     _id\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → [PineconeVectorStore](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html#langchain_pinecone.vectorstores.PineconeVectorStore "langchain_pinecone.vectorstores.PineconeVectorStore")\#     

Async return VectorStore initialized from texts and embeddings.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function to use.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts. Default is None.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of IDs associated with the texts.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

  * **batch\_size** \(_int_\)

  * **text\_key** \(_str_\)

  * **namespace** \(_str_ _|__None_\)

  * **index\_name** \(_str_ _|__None_\)

  * **upsert\_kwargs** \(_dict_ _|__None_\)

  * **embeddings\_chunk\_size** \(_int_\)

  * **id\_prefix** \(_str_ _|__None_\)

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.amax_marginal_relevance_search)\#     

Async return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Default is 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **\*\*kwargs**

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : SparseValues_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance asynchronously.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_SparseValues_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_dict_ _|__None_\) – Dictionary of argument\(s\) to filter on metadata

  * **namespace** \(_str_ _|__None_\) – Namespace to search in. Default will search in ‘’ namespace.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.asimilarity_search)\#     

Async return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Input text.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **\*\*kwargs** \(_Any_\) – Arguments to pass to the search method.

  * **filter** \(_dict_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **\*\*kwargs**

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

_async _asimilarity\_search\_by\_vector\_with\_score\(

    _embedding : SparseValues_,     _\*_ ,     _k : int = 4_,     _filter : dict | None = None_,     _namespace : str | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.asimilarity_search_by_vector_with_score)\#     

Return pinecone documents most similar to embedding, along with scores asynchronously.

Parameters:     

  * **embedding** \(_SparseValues_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _namespace : str | None = None_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.asimilarity_search_with_score)\#     

Asynchronously return pinecone documents most similar to query, along with scores.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _|__None_\) – Dictionary of argument\(s\) to filter on metadata

  * **namespace** \(_str_ _|__None_\) – Namespace to search in. Default will search in ‘’ namespace.

Returns:     

List of Documents most similar to the query and score for each

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

delete\(

    _ids : List\[str\] | None = None_,     _delete\_all : bool | None = None_,     _namespace : str | None = None_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.delete)\#     

Delete by vector IDs or filter. :param ids: List of ids to delete. :param delete\_all: Whether delete all vectors in the index. :param filter: Dictionary of conditions to filter vectors to delete. :param namespace: Namespace to search in. Default will search in ‘’ namespace.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **delete\_all** \(_bool_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **filter** \(_dict_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

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

_classmethod _from\_existing\_index\(

    _index\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _text\_key : str = 'text'_,     _namespace : str | None = None_,     _pool\_threads : int = 4_, \) → [PineconeVectorStore](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html#langchain_pinecone.vectorstores.PineconeVectorStore "langchain_pinecone.vectorstores.PineconeVectorStore")\#     

Load pinecone vectorstore from index name.

Parameters:     

  * **index\_name** \(_str_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **text\_key** \(_str_\)

  * **namespace** \(_str_ _|__None_\)

  * **pool\_threads** \(_int_\)

Return type:     

[_PineconeVectorStore_](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html#langchain_pinecone.vectorstores.PineconeVectorStore "langchain_pinecone.vectorstores.PineconeVectorStore")

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _text\_key : str = 'text'_,     _namespace : str | None = None_,     _index\_name : str | None = None_,     _upsert\_kwargs : dict | None = None_,     _pool\_threads : int = 4_,     _embeddings\_chunk\_size : int = 1000_,     _async\_req : bool = True_,     _\*_ ,     _id\_prefix : str | None = None_,     _\*\* kwargs: Any_, \) → [PineconeVectorStore](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html#langchain_pinecone.vectorstores.PineconeVectorStore "langchain_pinecone.vectorstores.PineconeVectorStore")\#     

Construct Pinecone wrapper from raw documents.

This is a user-friendly interface that:     

  1. Embeds documents.

  2. Adds the documents to a provided Pinecone index

This is intended to be a quick way to get started.

The pool\_threads affects the speed of the upsert operations.

Setup: set the PINECONE\_API\_KEY environment variable to your Pinecone API key.

Example               from langchain_pinecone import PineconeVectorStore, PineconeEmbeddings          embeddings = PineconeEmbeddings(model="multilingual-e5-large")          index_name = "my-index"     vectorstore = PineconeVectorStore.from_texts(         texts,         index_name=index_name,         embedding=embedding,         namespace=namespace,     )     

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **batch\_size** \(_int_\)

  * **text\_key** \(_str_\)

  * **namespace** \(_str_ _|__None_\)

  * **index\_name** \(_str_ _|__None_\)

  * **upsert\_kwargs** \(_dict_ _|__None_\)

  * **pool\_threads** \(_int_\)

  * **embeddings\_chunk\_size** \(_int_\)

  * **async\_req** \(_bool_\)

  * **id\_prefix** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_PineconeVectorStore_](https://python.langchain.com/api_reference/pinecone/vectorstores/langchain_pinecone.vectorstores.PineconeVectorStore.html#langchain_pinecone.vectorstores.PineconeVectorStore "langchain_pinecone.vectorstores.PineconeVectorStore")

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

_classmethod _get\_pinecone\_index\(

    _index\_name : str | None_,     _pool\_threads : int = 4_,     _\*_ ,     _pinecone\_api\_key : str | None = None_, \) → Index\#     

Return a Pinecone Index instance.

Parameters:     

  * **index\_name** \(_str_ _|__None_\) – Name of the index to use.

  * **pool\_threads** \(_int_\) – Number of threads to use for index upsert.

  * **pinecone\_api\_key** \(_str_ _|__None_\) – The api\_key of Pinecone.

Returns:     

Pinecone Index instance.

Return type:     

_Index_

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_dict_ _|__None_\) – Dictionary of argument\(s\) to filter on metadata

  * **namespace** \(_str_ _|__None_\) – Namespace to search in. Default will search in ‘’ namespace.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : SparseValues_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_SparseValues_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_dict_ _|__None_\) – Dictionary of argument\(s\) to filter on metadata

  * **namespace** \(_str_ _|__None_\) – Namespace to search in. Default will search in ‘’ namespace.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.similarity_search)\#     

Return pinecone documents most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _|__None_\) – Dictionary of argument\(s\) to filter on metadata

  * **namespace** \(_str_ _|__None_\) – Namespace to search in. Default will search in ‘’ namespace.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

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

similarity\_search\_by\_vector\_with\_score\(

    _embedding : SparseValues_,     _\*_ ,     _k : int = 4_,     _filter : dict | None = None_,     _namespace : str | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.similarity_search_by_vector_with_score)\#     

Return pinecone documents most similar to embedding, along with scores.

Parameters:     

  * **embedding** \(_SparseValues_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _namespace : str | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_pinecone/vectorstores_sparse.html#PineconeSparseVectorStore.similarity_search_with_score)\#     

Return pinecone documents most similar to query, along with scores.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _|__None_\) – Dictionary of argument\(s\) to filter on metadata

  * **namespace** \(_str_ _|__None_\) – Namespace to search in. Default will search in ‘’ namespace.

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)