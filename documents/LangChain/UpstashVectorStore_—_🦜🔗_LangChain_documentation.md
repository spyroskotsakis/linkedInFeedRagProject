# UpstashVectorStore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.upstash.UpstashVectorStore.html
**Word Count:** 2409
**Links Count:** 500
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# UpstashVectorStore\#

_class _langchain\_community.vectorstores.upstash.UpstashVectorStore\(

    _text\_key : str = 'text'_,     _index : Index | None = None_,     _async\_index : AsyncIndex | None = None_,     _index\_url : str | None = None_,     _index\_token : str | None = None_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | bool | None = None_,     _\*_ ,     _namespace : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore)\#     

Upstash Vector vector store

To use, the `upstash-vector` python package must be installed.

Also an Upstash Vector index is required. First create a new Upstash Vector index and copy the index\_url and index\_token variables. Then either pass them through the constructor or set the environment variables UPSTASH\_VECTOR\_REST\_URL and UPSTASH\_VECTOR\_REST\_TOKEN.

Example               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import UpstashVectorStore          embeddings = OpenAIEmbeddings(model="text-embedding-3-large")     vectorstore = UpstashVectorStore(         embedding=embeddings,         index_url="...",         index_token="..."     )          # or          import os          os.environ["UPSTASH_VECTOR_REST_URL"] = "..."     os.environ["UPSTASH_VECTOR_REST_TOKEN"] = "..."          vectorstore = UpstashVectorStore(         embedding=embeddings     )     

Constructor for UpstashVectorStore.

If index or index\_url and index\_token are not provided, the constructor will attempt to create an index using the environment variables UPSTASH\_VECTOR\_REST\_URL\`and \`UPSTASH\_VECTOR\_REST\_TOKEN.

Parameters:     

  * **text\_key** \(_str_\) – Key to store the text in metadata.

  * **index** \(_Optional_ _\[__Index_ _\]_\) – UpstashVector Index object.

  * **async\_index** \(_Optional_ _\[__AsyncIndex_ _\]_\) – UpstashVector AsyncIndex object, provide only if async

  * **needed** \(_functions are_\)

  * **index\_url** \(_Optional_ _\[__str_ _\]_\) – URL of the UpstashVector index.

  * **index\_token** \(_Optional_ _\[__str_ _\]_\) – Token of the UpstashVector index.

  * **embedding** \(_Optional_ _\[__Union_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _,__bool_ _\]__\]_\) – Embeddings object or a boolean. When false, no embedding is applied. If true, Upstash embeddings are used. When Upstash embeddings are used, text is sent directly to Upstash and embedding is applied there instead of embedding in Langchain.

  * **namespace** \(_str_\) – Namespace to use from the index.

Example               from langchain_community.vectorstores.upstash import UpstashVectorStore     from langchain_community.embeddings.openai import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     vectorstore = UpstashVectorStore(         embedding=embeddings,         index_url="...",         index_token="...",         namespace="..."     )          # With an existing index     from upstash_vector import Index          index = Index(url="...", token="...")     vectorstore = UpstashVectorStore(         embedding=embeddings,         index=index,         namespace="..."     )     

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(\[text\_key, index, async\_index, ...\]\) | Constructor for UpstashVectorStore.   ---|---   `aadd_documents`\(documents\[, ids, batch\_size, ...\]\) | Get the embeddings for the documents and add them to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids, ...\]\) | Get the embeddings for the texts and add them to the vectorstore.   `add_documents`\(documents\[, ids, batch\_size, ...\]\) | Get the embeddings for the documents and add them to the vectorstore.   `add_texts`\(texts\[, metadatas, ids, ...\]\) | Get the embeddings for the texts and add them to the vectorstore.   `adelete`\(\[ids, delete\_all, batch\_size, namespace\]\) | Delete by vector IDs   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a new UpstashVectorStore from a list of texts.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `ainfo`\(\) | Get statistics about the index.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k, filter, namespace\]\) | Return documents most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Return documents closest to the given embedding.   `asimilarity_search_by_vector_with_score`\(...\) | Return texts whose embedding is closest to the given embedding   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Retrieve texts most similar to query and convert the result to Document objects.   `delete`\(\[ids, delete\_all, batch\_size, namespace\]\) | Delete by vector IDs   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a new UpstashVectorStore from a list of texts.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `info`\(\) | Get statistics about the index.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, namespace\]\) | Return documents most similar to query.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return documents closest to the given embedding.   `similarity_search_by_vector_with_score`\(embedding\) | Return texts whose embedding is closest to the given embedding   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Retrieve texts most similar to query and convert the result to Document objects.      \_\_init\_\_\(

    _text\_key : str = 'text'_,     _index : Index | None = None_,     _async\_index : AsyncIndex | None = None_,     _index\_url : str | None = None_,     _index\_token : str | None = None_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | bool | None = None_,     _\*_ ,     _namespace : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.__init__)\#     

Constructor for UpstashVectorStore.

If index or index\_url and index\_token are not provided, the constructor will attempt to create an index using the environment variables UPSTASH\_VECTOR\_REST\_URL\`and \`UPSTASH\_VECTOR\_REST\_TOKEN.

Parameters:     

  * **text\_key** \(_str_\) – Key to store the text in metadata.

  * **index** \(_Optional_ _\[__Index_ _\]_\) – UpstashVector Index object.

  * **async\_index** \(_Optional_ _\[__AsyncIndex_ _\]_\) – UpstashVector AsyncIndex object, provide only if async

  * **needed** \(_functions are_\)

  * **index\_url** \(_Optional_ _\[__str_ _\]_\) – URL of the UpstashVector index.

  * **index\_token** \(_Optional_ _\[__str_ _\]_\) – Token of the UpstashVector index.

  * **embedding** \(_Optional_ _\[__Union_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _,__bool_ _\]__\]_\) – Embeddings object or a boolean. When false, no embedding is applied. If true, Upstash embeddings are used. When Upstash embeddings are used, text is sent directly to Upstash and embedding is applied there instead of embedding in Langchain.

  * **namespace** \(_str_\) – Namespace to use from the index.

Example               from langchain_community.vectorstores.upstash import UpstashVectorStore     from langchain_community.embeddings.openai import OpenAIEmbeddings          embeddings = OpenAIEmbeddings()     vectorstore = UpstashVectorStore(         embedding=embeddings,         index_url="...",         index_token="...",         namespace="..."     )          # With an existing index     from upstash_vector import Index          index = Index(url="...", token="...")     vectorstore = UpstashVectorStore(         embedding=embeddings,         index=index,         namespace="..."     )     

_async _aadd\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _embedding\_chunk\_size : int = 1000_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.aadd_documents)\#     

Get the embeddings for the documents and add them to the vectorstore.

Documents are sent to the embeddings object in batches of size embedding\_chunk\_size. The embeddings are then upserted into the vectorstore in batches of size batch\_size.

Parameters:     

  * **documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Iterable of Documents to add to the vectorstore.

  * **batch\_size** \(_int_\) – Batch size to use when upserting the embeddings.

  * **request.** \(_Upstash supports at max 1000 vectors per_\)

  * **embedding\_batch\_size** – Chunk size to use when embedding the texts.

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **embedding\_chunk\_size** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _embedding\_chunk\_size : int = 1000_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.aadd_texts)\#     

Get the embeddings for the texts and add them to the vectorstore.

Texts are sent to the embeddings object in batches of size embedding\_chunk\_size. The embeddings are then upserted into the vectorstore in batches of size batch\_size.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts.

  * **batch\_size** \(_int_\) – Batch size to use when upserting the embeddings.

  * **request.** \(_Upstash supports at max 1000 vectors per_\)

  * **embedding\_batch\_size** – Chunk size to use when embedding the texts.

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **embedding\_chunk\_size** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

add\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _embedding\_chunk\_size : int = 1000_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.add_documents)\#     

Get the embeddings for the documents and add them to the vectorstore.

Documents are sent to the embeddings object in batches of size embedding\_chunk\_size. The embeddings are then upserted into the vectorstore in batches of size batch\_size.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Iterable of Documents to add to the vectorstore.

  * **batch\_size** \(_int_\) – Batch size to use when upserting the embeddings.

  * **request.** \(_Upstash supports at max 1000 vectors per_\)

  * **embedding\_batch\_size** – Chunk size to use when embedding the texts.

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **embedding\_chunk\_size** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _batch\_size : int = 32_,     _embedding\_chunk\_size : int = 1000_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.add_texts)\#     

Get the embeddings for the texts and add them to the vectorstore.

Texts are sent to the embeddings object in batches of size embedding\_chunk\_size. The embeddings are then upserted into the vectorstore in batches of size batch\_size.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – Optional list of ids to associate with the texts.

  * **batch\_size** \(_int_\) – Batch size to use when upserting the embeddings.

  * **request.** \(_Upstash supports at max 1000 vectors per_\)

  * **embedding\_batch\_size** – Chunk size to use when embedding the texts.

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **embedding\_chunk\_size** \(_int_\)

  * **kwargs** \(_Any_\)

Returns:     

List of ids from adding the texts into the vectorstore.

Return type:     

_List_\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _delete\_all : bool | None = None_,     _batch\_size : int | None = 1000_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.adelete)\#     

Delete by vector IDs

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **delete\_all** \(_bool_ _|__None_\) – Delete all vectors in the index.

  * **batch\_size** \(_int_ _|__None_\) – Batch size to use when deleting the embeddings.

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **request.** \(_Upstash supports at max 1000 deletions per_\)

  * **kwargs** \(_Any_\)

Return type:     

None

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _embedding\_chunk\_size : int = 1000_,     _batch\_size : int = 32_,     _text\_key : str = 'text'_,     _index : Index | None = None_,     _async\_index : AsyncIndex | None = None_,     _index\_url : str | None = None_,     _index\_token : str | None = None_,     _\*_ ,     _namespace : str = ''_,     _\*\* kwargs: Any_, \) → UpstashVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.afrom_texts)\#     

Create a new UpstashVectorStore from a list of texts.

Example

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\)

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **embedding\_chunk\_size** \(_int_\)

  * **batch\_size** \(_int_\)

  * **text\_key** \(_str_\)

  * **index** \(_Optional_ _\[__Index_ _\]_\)

  * **async\_index** \(_Optional_ _\[__AsyncIndex_ _\]_\)

  * **index\_url** \(_Optional_ _\[__str_ _\]_\)

  * **index\_token** \(_Optional_ _\[__str_ _\]_\)

  * **namespace** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

UpstashVectorStore

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

_async _ainfo\(\) → InfoResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.ainfo)\#     

Get statistics about the index.

Returns:     

  * total number of vectors

  * total number of vectors waiting to be indexed

  * total size of the index on disk in bytes

  * dimension count for the index

  * similarity function selected for the index

Return type:     

InfoResult

_async _amax\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.amax_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\] | str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__str_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

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

    _query : str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.asimilarity_search)\#     

Return documents most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\] | str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.asimilarity_search_by_vector)\#     

Return documents closest to the given embedding.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__str_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\_with\_score\(

    _embedding : List\[float\] | str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.asimilarity_search_by_vector_with_score)\#     

Return texts whose embedding is closest to the given embedding

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__str_\)

  * **k** \(_int_\)

  * **filter** \(_str_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.asimilarity_search_with_score)\#     

Retrieve texts most similar to query and convert the result to Document objects.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

delete\(

    _ids : List\[str\] | None = None_,     _delete\_all : bool | None = None_,     _batch\_size : int | None = 1000_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.delete)\#     

Delete by vector IDs

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **delete\_all** \(_bool_ _|__None_\) – Delete all vectors in the index.

  * **batch\_size** \(_int_ _|__None_\) – Batch size to use when deleting the embeddings.

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **request.** \(_Upstash supports at max 1000 deletions per_\)

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

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _embedding\_chunk\_size : int = 1000_,     _batch\_size : int = 32_,     _text\_key : str = 'text'_,     _index : Index | None = None_,     _async\_index : AsyncIndex | None = None_,     _index\_url : str | None = None_,     _index\_token : str | None = None_,     _\*_ ,     _namespace : str = ''_,     _\*\* kwargs: Any_, \) → UpstashVectorStore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.from_texts)\#     

Create a new UpstashVectorStore from a list of texts.

Example

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\)

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **embedding\_chunk\_size** \(_int_\)

  * **batch\_size** \(_int_\)

  * **text\_key** \(_str_\)

  * **index** \(_Optional_ _\[__Index_ _\]_\)

  * **async\_index** \(_Optional_ _\[__AsyncIndex_ _\]_\)

  * **index\_url** \(_Optional_ _\[__str_ _\]_\)

  * **index\_token** \(_Optional_ _\[__str_ _\]_\)

  * **namespace** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

UpstashVectorStore

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

info\(\) → InfoResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.info)\#     

Get statistics about the index.

Returns:     

  * total number of vectors

  * total number of vectors waiting to be indexed

  * total size of the index on disk in bytes

  * dimension count for the index

  * similarity function selected for the index

Return type:     

InfoResult

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\] | str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__str_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

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

    _query : str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.similarity_search)\#     

Return documents most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\] | str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.similarity_search_by_vector)\#     

Return documents closest to the given embedding.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__str_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\_with\_score\(

    _embedding : List\[float\] | str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.similarity_search_by_vector_with_score)\#     

Return texts whose embedding is closest to the given embedding

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__str_\)

  * **k** \(_int_\)

  * **filter** \(_str_ _|__None_\)

  * **namespace** \(_str_ _|__None_\)

  * **kwargs** \(_Any_\)

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

    _query : str_,     _k : int = 4_,     _filter : str | None = None_,     _\*_ ,     _namespace : str | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/upstash.html#UpstashVectorStore.similarity_search_with_score)\#     

Retrieve texts most similar to query and convert the result to Document objects.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_str_ _|__None_\) – Optional metadata filter in str format

  * **namespace** \(_str_ _|__None_\) – Namespace to use from the index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using UpstashVectorStore

  * [Upstash Vector](https://python.langchain.com/docs/integrations/vectorstores/upstash/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)