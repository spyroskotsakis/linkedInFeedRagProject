# OpenSearchVectorSearch — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.opensearch_vector_search.OpenSearchVectorSearch.html
**Word Count:** 2849
**Links Count:** 523
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# OpenSearchVectorSearch\#

_class _langchain\_community.vectorstores.opensearch\_vector\_search.OpenSearchVectorSearch\(

    _opensearch\_url : str_,     _index\_name : str_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch)\#     

Amazon OpenSearch Vector Engine vector store.

Example               from langchain_community.vectorstores import OpenSearchVectorSearch     opensearch_vector_search = OpenSearchVectorSearch(         "http://localhost:9200",         "embeddings",         embedding_function     )     

Initialize with necessary components.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(opensearch\_url, index\_name, ...\) | Initialize with necessary components.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, bulk\_size\]\) | Asynchronously run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(text\_embeddings\[, metadatas, ...\]\) | Add the given texts and embeddings to the vectorstore.   `add_texts`\(texts\[, metadatas, ids, bulk\_size\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Asynchronously delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_embeddings`\(embeddings, texts, embedding\) | Asynchronously construct OpenSearchVectorSearch wrapper from pre-vectorized embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Asynchronously construct OpenSearchVectorSearch wrapper from raw texts.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `configure_search_pipelines`\(pipeline\_name\[, ...\]\) | Configures a search pipeline for hybrid search.   `create_index`\(dimension\[, index\_name\]\) | Create a new Index with given arguments   `delete`\(\[ids, refresh\_indices\]\) | Delete documents from the Opensearch index.   `delete_index`\(\[index\_name\]\) | Deletes a given index from vectorstore.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_embeddings`\(embeddings, texts, embedding\) | Construct OpenSearchVectorSearch wrapper from pre-vectorized embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Construct OpenSearchVectorSearch wrapper from raw texts.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_search_pipeline_info`\(pipeline\_name\) | Get information about a search pipeline.   `index_exists`\(\[index\_name\]\) | If given index present in vectorstore, returns True else False.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `search_pipeline_exists`\(pipeline\_name\) | Checks if a search pipeline exists.   `similarity_search`\(query\[, k, score\_threshold\]\) | Return docs most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to the embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs and it's scores most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) | Return docs and it's scores most similar to the embedding vector.      Parameters:     

  * **opensearch\_url** \(_str_\)

  * **index\_name** \(_str_\)

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _opensearch\_url : str_,     _index\_name : str_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.__init__)\#     

Initialize with necessary components.

Parameters:     

  * **opensearch\_url** \(_str_\)

  * **index\_name** \(_str_\)

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

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

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _bulk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.aadd_texts)\#     

Asynchronously run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **bulk\_size** \(_int_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _text\_embeddings : Iterable\[Tuple\[str, List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _bulk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.add_embeddings)\#     

Add the given texts and embeddings to the vectorstore.

Parameters:     

  * **text\_embeddings** \(_Iterable_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\) – Iterable pairs of string and embedding to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts.

  * **bulk\_size** \(_int_ _|__None_\) – Bulk API request count; Default: 500

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _bulk\_size : int | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts.

  * **bulk\_size** \(_int_ _|__None_\) – Bulk API request count; Default: 500

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

_async _adelete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.adelete)\#     

Asynchronously delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

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

    _embeddings : List\[List\[float\]\]_,     _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _bulk\_size : int | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → OpenSearchVectorSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.afrom_embeddings)\#     

Asynchronously construct OpenSearchVectorSearch wrapper from pre-vectorized embeddings.

Example               from langchain_community.vectorstores import OpenSearchVectorSearch     from langchain_community.embeddings import OpenAIEmbeddings     embedder = OpenAIEmbeddings()     embeddings = await embedder.aembed_documents(["foo", "bar"])     opensearch_vector_search =         await OpenSearchVectorSearch.afrom_embeddings(             embeddings,             texts,             embedder,             opensearch_url="http://localhost:9200"     )     

OpenSearch by default supports Approximate Search powered by nmslib, faiss and lucene engines recommended for large datasets. Also supports brute force search through Script Scoring and Painless Scripting.

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

Optional Keyword Args for Approximate Search:     

engine: “nmslib”, “faiss”, “lucene”; default: “nmslib”

space\_type: “l2”, “l1”, “cosinesimil”, “linf”, “innerproduct”; default: “l2”

ef\_search: Size of the dynamic list used during k-NN searches. Higher values lead to more accurate but slower searches; default: 512

ef\_construction: Size of the dynamic list used during k-NN graph creation. Higher values lead to more accurate graph but slower indexing speed; default: 512

m: Number of bidirectional links created for each new element. Large impact on memory consumption. Between 2 and 100; default: 16

Keyword Args for Script Scoring or Painless Scripting:     

is\_appx\_search: False

Parameters:     

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\)

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **bulk\_size** \(_int_ _|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_OpenSearchVectorSearch_

_async classmethod _afrom\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _bulk\_size : int | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → OpenSearchVectorSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.afrom_texts)\#     

Asynchronously construct OpenSearchVectorSearch wrapper from raw texts.

Example               from langchain_community.vectorstores import OpenSearchVectorSearch     from langchain_community.embeddings import OpenAIEmbeddings     embeddings = OpenAIEmbeddings()     opensearch_vector_search = await OpenSearchVectorSearch.afrom_texts(         texts,         embeddings,         opensearch_url="http://localhost:9200"     )     

OpenSearch by default supports Approximate Search powered by nmslib, faiss and lucene engines recommended for large datasets. Also supports brute force search through Script Scoring and Painless Scripting.

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

Optional Keyword Args for Approximate Search:     

engine: “nmslib”, “faiss”, “lucene”; default: “nmslib”

space\_type: “l2”, “l1”, “cosinesimil”, “linf”, “innerproduct”; default: “l2”

ef\_search: Size of the dynamic list used during k-NN searches. Higher values lead to more accurate but slower searches; default: 512

ef\_construction: Size of the dynamic list used during k-NN graph creation. Higher values lead to more accurate graph but slower indexing speed; default: 512

m: Number of bidirectional links created for each new element. Large impact on memory consumption. Between 2 and 100; default: 16

Keyword Args for Script Scoring or Painless Scripting:     

is\_appx\_search: False

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **bulk\_size** \(_int_ _|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_OpenSearchVectorSearch_

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

configure\_search\_pipelines\(

    _pipeline\_name : str_,     _keyword\_weight : float = 0.7_,     _vector\_weight : float = 0.3_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.configure_search_pipelines)\#     

Configures a search pipeline for hybrid search. :param pipeline\_name: Name of the pipeline :param keyword\_weight: Weight for keyword search :param vector\_weight: Weight for vector search

Returns:     

Acknowledgement of the pipeline creation. \(if there is any error while configuring the pipeline, it will return None\)

Return type:     

response

Raises:     

**Exception** – If an error occurs

Parameters:     

  * **pipeline\_name** \(_str_\)

  * **keyword\_weight** \(_float_\)

  * **vector\_weight** \(_float_\)

create\_index\(

    _dimension : int_,     _index\_name : str | None = '7ee171ef854e42f89b4d86cda667530c'_,     _\*\* kwargs: Any_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.create_index)\#     

Create a new Index with given arguments

Parameters:     

  * **dimension** \(_int_\)

  * **index\_name** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

str | None

delete\(

    _ids : List\[str\] | None = None_,     _refresh\_indices : bool | None = True_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.delete)\#     

Delete documents from the Opensearch index.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids of documents to delete.

  * **refresh\_indices** \(_bool_ _|__None_\) – Whether to refresh the index after deleting documents. Defaults to True.

  * **kwargs** \(_Any_\)

Return type:     

bool | None

delete\_index\(

    _index\_name : str | None = None_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.delete_index)\#     

Deletes a given index from vectorstore.

Parameters:     

**index\_name** \(_str_ _|__None_\)

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

_classmethod _from\_embeddings\(

    _embeddings : List\[List\[float\]\]_,     _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _bulk\_size : int | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → OpenSearchVectorSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.from_embeddings)\#     

Construct OpenSearchVectorSearch wrapper from pre-vectorized embeddings.

Example               from langchain_community.vectorstores import OpenSearchVectorSearch     from langchain_community.embeddings import OpenAIEmbeddings     embedder = OpenAIEmbeddings()     embeddings = embedder.embed_documents(["foo", "bar"])     opensearch_vector_search = OpenSearchVectorSearch.from_embeddings(         embeddings,         texts,         embedder,         opensearch_url="http://localhost:9200"     )     

OpenSearch by default supports Approximate Search powered by nmslib, faiss and lucene engines recommended for large datasets. Also supports brute force search through Script Scoring and Painless Scripting.

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

Optional Keyword Args for Approximate Search:     

engine: “nmslib”, “faiss”, “lucene”; default: “nmslib”

space\_type: “l2”, “l1”, “cosinesimil”, “linf”, “innerproduct”; default: “l2”

ef\_search: Size of the dynamic list used during k-NN searches. Higher values lead to more accurate but slower searches; default: 512

ef\_construction: Size of the dynamic list used during k-NN graph creation. Higher values lead to more accurate graph but slower indexing speed; default: 512

m: Number of bidirectional links created for each new element. Large impact on memory consumption. Between 2 and 100; default: 16

Keyword Args for Script Scoring or Painless Scripting:     

is\_appx\_search: False

Parameters:     

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\)

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **bulk\_size** \(_int_ _|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_OpenSearchVectorSearch_

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _bulk\_size : int | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → OpenSearchVectorSearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.from_texts)\#     

Construct OpenSearchVectorSearch wrapper from raw texts.

Example               from langchain_community.vectorstores import OpenSearchVectorSearch     from langchain_community.embeddings import OpenAIEmbeddings     embeddings = OpenAIEmbeddings()     opensearch_vector_search = OpenSearchVectorSearch.from_texts(         texts,         embeddings,         opensearch_url="http://localhost:9200"     )     

OpenSearch by default supports Approximate Search powered by nmslib, faiss and lucene engines recommended for large datasets. Also supports brute force search through Script Scoring and Painless Scripting.

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

Optional Keyword Args for Approximate Search:     

engine: “nmslib”, “faiss”, “lucene”; default: “nmslib”

space\_type: “l2”, “l1”, “cosinesimil”, “linf”, “innerproduct”; default: “l2”

ef\_search: Size of the dynamic list used during k-NN searches. Higher values lead to more accurate but slower searches; default: 512

ef\_construction: Size of the dynamic list used during k-NN graph creation. Higher values lead to more accurate graph but slower indexing speed; default: 512

m: Number of bidirectional links created for each new element. Large impact on memory consumption. Between 2 and 100; default: 16

Keyword Args for Script Scoring or Painless Scripting:     

is\_appx\_search: False

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **bulk\_size** \(_int_ _|__None_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_OpenSearchVectorSearch_

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

get\_search\_pipeline\_info\(

    _pipeline\_name : str_, \) → Dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.get_search_pipeline_info)\#     

Get information about a search pipeline.

Parameters:     

**pipeline\_name** \(_str_\) – Name of the pipeline

Returns:     

Information about the pipeline None: If pipeline does not exist

Return type:     

dict

Raises:     

**Exception** – If an error occurs

Example               >>> get_search_pipeline_info("my_pipeline_1")     {'search_pipeline_1': {         "description": "Post processor for hybrid search",         "phase_results_processors": [             {                 "normalization-processor": {                     "normalization": {"technique": "min_max"},                     "combination": {                         "technique": "arithmetic_mean",                         "parameters": {"weights": [0.7, 0.3]}                     }                 }             }         ]     }     }     >>> get_search_pipeline_info("my_pipeline_2")     None     

index\_exists\(

    _index\_name : str | None = None_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.index_exists)\#     

If given index present in vectorstore, returns True else False.

Parameters:     

**index\_name** \(_str_ _|__None_\)

Return type:     

bool | None

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **kwargs** \(_Any_\)

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

search\_pipeline\_exists\(

    _pipeline\_name : str_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.search_pipeline_exists)\#     

Checks if a search pipeline exists.

Parameters:     

**pipeline\_name** \(_str_\) – Name of the pipeline

Returns:     

True if the pipeline exists, False otherwise

Return type:     

bool

Raises:     

**Exception** – If an error occurs

Example               >>> search_pipeline_exists("my_pipeline_1")     True     >>> search_pipeline_exists("my_pipeline_2")     False     

similarity\_search\(

    _query : str_,     _k : int = 4_,     _score\_threshold : float | None = 0.0_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.similarity_search)\#     

Return docs most similar to query.

By default, supports Approximate Search. Also supports Script Scoring and Painless Scripting.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **score\_threshold** \(_float_ _|__None_\) – Specify a score threshold to return only documents

  * **0.0.** \(_above the threshold. Defaults to_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Optional Args:     

vector\_field: Document field embeddings are stored in. Defaults to “vector\_field”.

text\_field: Document field the text of the document is stored in. Defaults to “text”.

metadata\_field: Document field that metadata is stored in. Defaults to “metadata”. Can be set to a special value “\*” to include the entire document.

Optional Args for Approximate Search:     

search\_type: “approximate\_search”; default: “approximate\_search”

boolean\_filter: A Boolean filter is a post filter consists of a Boolean query that contains a k-NN query and a filter.

subquery\_clause: Query clause on the knn vector field; default: “must”

lucene\_filter: the Lucene algorithm decides whether to perform an exact k-NN search with pre-filtering or an approximate search with modified post-filtering. \(deprecated, use efficient\_filter\)

efficient\_filter: the Lucene Engine or Faiss Engine decides whether to perform an exact k-NN search with pre-filtering or an approximate search with modified post-filtering.

Optional Args for Script Scoring Search:     

search\_type: “script\_scoring”; default: “approximate\_search”

space\_type: “l2”, “l1”, “linf”, “cosinesimil”, “innerproduct”, “hammingbit”; default: “l2”

pre\_filter: script\_score query to pre-filter documents before identifying nearest neighbors; default: \{“match\_all”: \{\}\}

Optional Args for Painless Scripting Search:     

search\_type: “painless\_scripting”; default: “approximate\_search”

space\_type: “l2Squared”, “l1Norm”, “cosineSimilarity”; default: “l2Squared”

pre\_filter: script\_score query to pre-filter documents before identifying nearest neighbors; default: \{“match\_all”: \{\}\}

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _score\_threshold : float | None = 0.0_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.similarity_search_by_vector)\#     

Return docs most similar to the embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **score\_threshold** \(_float_ _|__None_\)

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

    _query : str_,     _k : int = 4_,     _score\_threshold : float | None = 0.0_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.similarity_search_with_score)\#     

Return docs and it’s scores most similar to query.

By default, supports Approximate Search. Also supports Script Scoring and Painless Scripting.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **score\_threshold** \(_float_ _|__None_\) – Specify a score threshold to return only documents

  * **0.0.** \(_above the threshold. Defaults to_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents along with its scores most similar to the query.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Optional Args:     

same as similarity\_search

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _score\_threshold : float | None = 0.0_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/opensearch_vector_search.html#OpenSearchVectorSearch.similarity_search_with_score_by_vector)\#     

Return docs and it’s scores most similar to the embedding vector.

By default, supports Approximate Search. Also supports Script Scoring and Painless Scripting.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding vector to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **score\_threshold** \(_float_ _|__None_\) – Specify a score threshold to return only documents

  * **0.0.** \(_above the threshold. Defaults to_\)

  * **kwargs** \(_Any_\)

Returns:     

List of Documents along with its scores most similar to the query.

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Optional Args:     

same as similarity\_search

Examples using OpenSearchVectorSearch

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/opensearch/)

__On this page   *[/]: Positional-only parameter separator (PEP 570)