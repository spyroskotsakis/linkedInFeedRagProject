# Chroma — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.Chroma.html
**Word Count:** 2980
**Links Count:** 317
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# Chroma\#

_class _langchain\_chroma.vectorstores.Chroma\(

    _collection\_name : str = 'langchain'_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _persist\_directory : str | None = None_,     _client\_settings : Settings | None = None_,     _collection\_metadata : dict | None = None_,     _client : ClientAPI | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _create\_collection\_if\_not\_exists : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma)\#     

Chroma vector store integration.

Setup:     

Install `chromadb`, `langchain-chroma` packages:               pip install -qU chromadb langchain-chroma     

Key init args — indexing params:     

collection\_name: str     

Name of the collection.

embedding\_function: Embeddings     

Embedding function to use.

Key init args — client params:     

client: Optional\[Client\]     

Chroma client to use.

client\_settings: Optional\[chromadb.config.Settings\]     

Chroma client settings.

persist\_directory: Optional\[str\]     

Directory to persist the collection.

Instantiate:                    from langchain_chroma import Chroma     from langchain_openai import OpenAIEmbeddings          vector_store = Chroma(         collection_name="foo",         embedding_function=OpenAIEmbeddings(),         # other params...     )     

Add Documents:                    from langchain_core.documents import Document          document_1 = Document(page_content="foo", metadata={"baz": "bar"})     document_2 = Document(page_content="thud", metadata={"bar": "baz"})     document_3 = Document(page_content="i will be deleted :(")          documents = [document_1, document_2, document_3]     ids = ["1", "2", "3"]     vector_store.add_documents(documents=documents, ids=ids)     

Update Documents:                    updated_document = Document(         page_content="qux",         metadata={"bar": "baz"}     )          vector_store.update_documents(ids=["1"],documents=[updated_document])     

Delete Documents:                    vector_store.delete(ids=["3"])     

Search:                    results = vector_store.similarity_search(query="thud",k=1)     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * thud [{'baz': 'bar'}]     

Search with filter:                    results = vector_store.similarity_search(query="thud",k=1,filter={"baz": "bar"})     for doc in results:         print(f"* {doc.page_content} [{doc.metadata}]")                    * foo [{'baz': 'bar'}]     

Search with score:                    results = vector_store.similarity_search_with_score(query="qux",k=1)     for doc, score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.000000] qux [{'bar': 'baz', 'baz': 'bar'}]     

Async:                    # add documents     # await vector_store.aadd_documents(documents=documents, ids=ids)          # delete documents     # await vector_store.adelete(ids=["3"])          # search     # results = vector_store.asimilarity_search(query="thud",k=1)          # search with score     results = await vector_store.asimilarity_search_with_score(query="qux",k=1)     for doc,score in results:         print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")                    * [SIM=0.335463] foo [{'baz': 'bar'}]     

Use as Retriever:                    retriever = vector_store.as_retriever(         search_type="mmr",         search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},     )     retriever.invoke("thud")                    [Document(metadata={'baz': 'bar'}, page_content='thud')]     

Initialize with a Chroma client.

Parameters:     

  * **collection\_name** \(_str_\) – Name of the collection to create.

  * **embedding\_function** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\) – Embedding class object. Used to embed texts.

  * **persist\_directory** \(_Optional_ _\[__str_ _\]_\) – Directory to persist the collection.

  * **client\_settings** \(_Optional_ _\[__chromadb.config.Settings_ _\]_\) – Chroma client settings

  * **collection\_metadata** \(_Optional_ _\[__dict_ _\]_\) – Collection configurations.

  * **client** \(_Optional_ _\[__chromadb.ClientAPI_ _\]_\) – Chroma client. Documentation: <https://docs.trychroma.com/reference/python/client>

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\) – Function to calculate relevance score from distance. Used only in similarity\_search\_with\_relevance\_scores

  * **create\_collection\_if\_not\_exists** \(_Optional_ _\[__bool_ _\]_\) – Whether to create collection if it doesn’t exist. Defaults to True.

Attributes

`embeddings` | Access the query embedding object.   ---|---      Methods

`__init__`\(\[collection\_name, ...\]\) | Initialize with a Chroma client.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_images`\(uris\[, metadatas, ids\]\) | Run more images through the embeddings and add to the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `delete`\(\[ids\]\) | Delete by vector IDs.   `delete_collection`\(\) | Delete the collection.   `encode_image`\(uri\) | Get base64 string from image URI.   `from_documents`\(documents\[, embedding, ids, ...\]\) | Create a Chroma vectorstore from a list of documents.   `from_texts`\(texts\[, embedding, metadatas, ...\]\) | Create a Chroma vectorstore from a raw documents.   `get`\(\[ids, where, limit, offset, ...\]\) | Gets the collection.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `reset_collection`\(\) | Resets the collection.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Run similarity search with Chroma.   `similarity_search_by_image`\(uri\[, k, filter\]\) | Search for similar images based on the given image URI.   `similarity_search_by_image_with_relevance_score`\(uri\) | Search for similar images based on the given image URI.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_by_vector_with_relevance_scores`\(...\) | Return docs most similar to embedding vector and similarity score.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Run similarity search with Chroma with distance.   `similarity_search_with_vectors`\(query\[, k, ...\]\) | Run similarity search with Chroma with vectors.   `update_document`\(document\_id, document\) | Update a document in the collection.   `update_documents`\(ids, documents\) | Update a document in the collection.      \_\_init\_\_\(

    _collection\_name : str = 'langchain'_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _persist\_directory : str | None = None_,     _client\_settings : Settings | None = None_,     _collection\_metadata : dict | None = None_,     _client : ClientAPI | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_,     _create\_collection\_if\_not\_exists : bool | None = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.__init__)\#     

Initialize with a Chroma client.

Parameters:     

  * **collection\_name** \(_str_\) – Name of the collection to create.

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – Embedding class object. Used to embed texts.

  * **persist\_directory** \(_str_ _|__None_\) – Directory to persist the collection.

  * **client\_settings** \(_Settings_ _|__None_\) – Chroma client settings

  * **collection\_metadata** \(_dict_ _|__None_\) – Collection configurations.

  * **client** \(_ClientAPI_ _|__None_\) – Chroma client. Documentation: <https://docs.trychroma.com/reference/python/client>

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\) – Function to calculate relevance score from distance. Used only in similarity\_search\_with\_relevance\_scores

  * **create\_collection\_if\_not\_exists** \(_bool_ _|__None_\) – Whether to create collection if it doesn’t exist. Defaults to True.

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

add\_images\(

    _uris : list\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.add_images)\#     

Run more images through the embeddings and add to the vectorstore.

Parameters:     

  * **uris** \(_list_ _\[__str_ _\]_\) – File path to the image.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas. When querying, you can filter on this metadata.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of IDs. \(Items without IDs will be assigned UUIDs\)

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass.

Returns:     

List of IDs of the added images.

Raises:     

**ValueError** – When metadata is incorrect.

Return type:     

list\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Texts to add to the vectorstore.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas. When querying, you can filter on this metadata.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of IDs. \(Items without IDs will be assigned UUIDs\)

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

List of IDs of the added texts.

Raises:     

**ValueError** – When metadata is incorrect.

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

delete\(

    _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.delete)\#     

Delete by vector IDs.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

None

delete\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.delete_collection)\#     

Delete the collection.

Return type:     

None

encode\_image\(_uri : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.encode_image)\#     

Get base64 string from image URI.

Parameters:     

**uri** \(_str_\)

Return type:     

str

_classmethod _from\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _ids : list\[str\] | None = None_,     _collection\_name : str = 'langchain'_,     _persist\_directory : str | None = None_,     _client\_settings : Settings | None = None_,     _client : ClientAPI | None = None_,     _collection\_metadata : dict | None = None_,     _\*\* kwargs: Any_, \) → Chroma[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.from_documents)\#     

Create a Chroma vectorstore from a list of documents.

If a persist\_directory is specified, the collection will be persisted there. Otherwise, the data will be ephemeral in-memory.

Parameters:     

  * **collection\_name** \(_str_\) – Name of the collection to create.

  * **persist\_directory** \(_str_ _|__None_\) – Directory to persist the collection.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of document IDs. Defaults to None.

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of documents to add to the vectorstore.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – Embedding function. Defaults to None.

  * **client\_settings** \(_Settings_ _|__None_\) – Chroma client settings.

  * **client** \(_ClientAPI_ _|__None_\) – Chroma client. Documentation: <https://docs.trychroma.com/reference/python/client>

  * **collection\_metadata** \(_dict_ _|__None_\) – Collection configurations. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to initialize a Chroma client.

Returns:     

Chroma vectorstore.

Return type:     

Chroma

_classmethod _from\_texts\(

    _texts : list\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _metadatas : list\[dict\] | None = None_,     _ids : list\[str\] | None = None_,     _collection\_name : str = 'langchain'_,     _persist\_directory : str | None = None_,     _client\_settings : Settings | None = None_,     _client : ClientAPI | None = None_,     _collection\_metadata : dict | None = None_,     _\*\* kwargs: Any_, \) → Chroma[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.from_texts)\#     

Create a Chroma vectorstore from a raw documents.

If a persist\_directory is specified, the collection will be persisted there. Otherwise, the data will be ephemeral in-memory.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\) – List of texts to add to the collection.

  * **collection\_name** \(_str_\) – Name of the collection to create.

  * **persist\_directory** \(_str_ _|__None_\) – Directory to persist the collection.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|__None_\) – Embedding function. Defaults to None.

  * **metadatas** \(_list_ _\[__dict_ _\]__|__None_\) – List of metadatas. Defaults to None.

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of document IDs. Defaults to None.

  * **client\_settings** \(_Settings_ _|__None_\) – Chroma client settings.

  * **client** \(_ClientAPI_ _|__None_\) – Chroma client. Documentation: <https://docs.trychroma.com/reference/python/client>

  * **collection\_metadata** \(_dict_ _|__None_\) – Collection configurations. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to initialize a Chroma client.

Returns:     

Chroma vectorstore.

Return type:     

Chroma

get\(

    _ids : OneOrMany\[ID\] | None = None_,     _where : Where | None = None_,     _limit : int | None = None_,     _offset : int | None = None_,     _where\_document : WhereDocument | None = None_,     _include : list\[str\] | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.get)\#     

Gets the collection.

Parameters:     

  * **ids** \(_Optional_ _\[__OneOrMany_ _\[__ID_ _\]__\]_\) – The ids of the embeddings to get. Optional.

  * **where** \(_Optional_ _\[__Where_ _\]_\) – A Where type dict used to filter results by. E.g. \{“$and”: \[\{“color”: “red”\}, \{“price”: 4.20\}\]\} Optional.

  * **limit** \(_Optional_ _\[__int_ _\]_\) – The number of documents to return. Optional.

  * **offset** \(_Optional_ _\[__int_ _\]_\) – The offset to start returning results from. Useful for paging results with limit. Optional.

  * **where\_document** \(_Optional_ _\[__WhereDocument_ _\]_\) – A WhereDocument type dict used to filter by the documents. E.g. \{“$contains”: “hello”\}. Optional.

  * **include** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – A list of what to include in the results. Can contain “embeddings”, “metadatas”, “documents”. Ids are always included. Defaults to \[“metadatas”, “documents”\]. Optional.

Returns:     

A dict with the keys “ids”, “embeddings”, “metadatas”, “documents”.

Return type:     

dict\[str, Any\]

get\_by\_ids\(

    _ids : Sequence\[str\]_,     _/_ , \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.get_by_ids)\#     

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

Added in version 0.2.1.

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict\[str, str\] | None = None_,     _where\_document : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **where\_document** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – dict used to filter by the document contents. E.g. \{“$contains”: “hello”\}.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of Documents selected by maximal marginal relevance.

Raises:     

**ValueError** – If the embedding function is not provided.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict\[str, str\] | None = None_,     _where\_document : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **where\_document** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – dict used to filter by the document contents. E.g. \{“$contains”: “hello”\}.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

reset\_collection\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.reset_collection)\#     

Resets the collection.

Resets the collection by deleting the collection and recreating an empty one.

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

    _query : str_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search)\#     

Run similarity search with Chroma.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of documents most similar to the query text.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_image\(

    _uri : str_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search_by_image)\#     

Search for similar images based on the given image URI.

Parameters:     

  * **uri** \(_str_\) – URI of the image to search for.

  * **k** \(_int_ _,__optional_\) – Number of results to return. Defaults to DEFAULT\_K.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__,__optional_\) – Filter by metadata.

  * **\*\*kwargs** \(_Any_\) – Additional arguments to pass to function.

Returns:     

List of Images most similar to the provided image. Each element in list is a Langchain Document Object. The page content is b64 encoded image, metadata is default or as defined by user.

Raises:     

**ValueError** – If the embedding function does not support image embeddings.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_image\_with\_relevance\_score\(

    _uri : str_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search_by_image_with_relevance_score)\#     

Search for similar images based on the given image URI.

Parameters:     

  * **uri** \(_str_\) – URI of the image to search for.

  * **k** \(_int_ _,__optional_\) – Number of results to return.

  * **DEFAULT\_K.** \(_Defaults to_\)

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__,__optional_\) – Filter by metadata.

  * **\*\*kwargs** \(_Any_\) – Additional arguments to pass to function.

Returns:     

List of tuples containing documents similar to the query image and their similarity scores. 0th element in each tuple is a Langchain Document Object. The page content is b64 encoded img, metadata is default or defined by user.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Raises:     

**ValueError** – If the embedding function does not support image embeddings.

similarity\_search\_by\_vector\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _where\_document : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **where\_document** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – dict used to filter by the document contents. E.g. \{“$contains”: “hello”\}.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of Documents most similar to the query vector.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\_with\_relevance\_scores\(

    _embedding : list\[float\]_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _where\_document : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search_by_vector_with_relevance_scores)\#     

Return docs most similar to embedding vector and similarity score.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **where\_document** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – dict used to filter by the documents. E.g. \{“$contains”: “hello”\}\}.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of documents most similar to the query text and relevance score in float for each. Lower score represents more similarity.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

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

    _query : str_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _where\_document : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search_with_score)\#     

Run similarity search with Chroma with distance.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **where\_document** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – dict used to filter by document contents. E.g. \{“$contains”: “hello”\}.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of documents most similar to the query text and distance in float for each. Lower score represents more similarity.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_vectors\(

    _query : str_,     _k : int = 4_,     _filter : dict\[str, str\] | None = None_,     _where\_document : dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → list\[tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), ndarray\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.similarity_search_with_vectors)\#     

Run similarity search with Chroma with vectors.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **filter** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Filter by metadata. Defaults to None.

  * **where\_document** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – dict used to filter by the document contents. E.g. \{“$contains”: “hello”\}.

  * **kwargs** \(_Any_\) – Additional keyword arguments to pass to Chroma collection query.

Returns:     

List of documents most similar to the query text and embedding vectors for each.

Return type:     

list\[tuple\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), _ndarray_\]\]

update\_document\(

    _document\_id : str_,     _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.update_document)\#     

Update a document in the collection.

Parameters:     

  * **document\_id** \(_str_\) – ID of the document to update.

  * **document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\) – Document to update.

Return type:     

None

update\_documents\(

    _ids : list\[str\]_,     _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#Chroma.update_documents)\#     

Update a document in the collection.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]_\) – List of ids of the document to update.

  * **documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – List of documents to update.

Raises:     

**ValueError** – If the embedding function is not provided.

Return type:     

None

Examples using Chroma

  * [Build a Local RAG Application](https://python.langchain.com/docs/tutorials/local_rag/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Chroma](https://python.langchain.com/docs/integrations/vectorstores/chroma/)

  * [Confident](https://python.langchain.com/docs/integrations/callbacks/confident/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Docugami](https://python.langchain.com/docs/integrations/document_loaders/docugami/)

  * [Google Cloud Vertex AI Reranker](https://python.langchain.com/docs/integrations/document_transformers/google_cloud_vertexai_rerank/)

  * [How deal with high cardinality categoricals when doing query analysis](https://python.langchain.com/docs/how_to/query_high_cardinality/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to create and query vector stores](https://python.langchain.com/docs/how_to/vectorstores/)

  * [How to do “self-querying” retrieval](https://python.langchain.com/docs/how_to/self_query/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)

  * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)

  * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)

  * [How to reorder retrieved results to mitigate the “lost in the middle” effect](https://python.langchain.com/docs/how_to/long_context_reorder/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [How to select examples by similarity](https://python.langchain.com/docs/how_to/example_selectors_similarity/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to use few shot examples](https://python.langchain.com/docs/how_to/few_shot_examples/)

  * [How to use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)

  * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

  * [How to use the Parent Document Retriever](https://python.langchain.com/docs/how_to/parent_document_retriever/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [LOTR \(Merger Retriever\)](https://python.langchain.com/docs/integrations/retrievers/merger_retriever/)

  * [Psychic](https://python.langchain.com/docs/integrations/document_loaders/psychic/)

  * [RePhraseQuery](https://python.langchain.com/docs/integrations/retrievers/re_phrase/)

  * [Vector stores and retrievers](https://python.langchain.com/docs/tutorials/retrievers/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)