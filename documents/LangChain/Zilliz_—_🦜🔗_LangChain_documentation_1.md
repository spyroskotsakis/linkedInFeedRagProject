# Zilliz — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.zilliz.Zilliz.html
**Word Count:** 3487
**Links Count:** 300
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# Zilliz\#

_class _langchain\_milvus.vectorstores.zilliz.Zilliz\(_\* args: Any_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/vectorstores/zilliz.html#Zilliz)\#     

Zilliz vector store.

You need to have pymilvus installed and a running Zilliz database.

See the following documentation for how to run a Zilliz instance: <https://docs.zilliz.com/docs/create-cluster>

IF USING L2/IP metric IT IS HIGHLY SUGGESTED TO NORMALIZE YOUR DATA.

Parameters:     

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Function used to embed the text.

  * **collection\_name** \(_str_\) – Which Zilliz collection to use. Defaults to “LangChainCollection”.

  * **connection\_args** \(_Optional_ _\[__dict_ _\[__str_ _,__any_ _\]__\]_\) – The connection args used for this class comes in the form of a dict.

  * **consistency\_level** \(_str_\) – The consistency level to use for a collection. Defaults to “Session”.

  * **index\_params** \(_Optional_ _\[__dict_ _\]_\) – Which index params to use. Defaults to HNSW/AUTOINDEX depending on service.

  * **search\_params** \(_Optional_ _\[__dict_ _\]_\) – Which search params to use. Defaults to default of index.

  * **drop\_old** \(_Optional_ _\[__bool_ _\]_\) – Whether to drop the current collection. Defaults to False.

  * **auto\_id** \(_bool_\) – Whether to enable auto id for primary key. Defaults to False. If False, you need to provide text ids \(string less than 65535 bytes\). If True, Milvus will generate unique integers as primary keys.

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

The connection args used for this class comes in the form of a dict, the two major arguments are:

> uri \(str\): The Public Endpoint of Zilliz instance. Example uri: >      >  > “<https://in03-ba4234asae.api.gcp-us-west1.zillizcloud.com>”, >  > token \(str\): API key, for serverless clusters which can be used as >      >  > replacements for user and password.

For more information, please refer to: <https://docs.zilliz.com/docs/on-zilliz-cloud-console#cluster-details> and <https://docs.zilliz.com/reference/python/python/Connections-connect>

Example               

from langchain\_milvus import Zilliz from langchain\_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings\(\) \# Connect to a Zilliz instance milvus\_store = Zilliz\(

> embedding\_function = embedding, collection\_name = “LangChainCollection”, connection\_args = \{ >
>> “uri”: “<https://in03-ba4234asae.api.gcp-us-west1.zillizcloud.com>”, “token”: “temp”, \# API key >  > \} drop\_old: True,

\)

Raises:     

**ValueError** – If the pymilvus python package is not installed.

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Initialize the Milvus vector store.

Attributes

`aclient` | Get async client.   ---|---   `client` | Get client.   `embeddings` | Get embedding function\(s\).   `vector_fields` | Get vector field\(s\).      Methods

`__init__`\(\*args, \*\*kwargs\) | Initialize the Milvus vector store.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Run more documents through the embeddings and add to the vectorstore asynchronously.   `aadd_embeddings`\(texts, embeddings\[, ...\]\) | Insert text data with embeddings vectors into Milvus asynchronously.   `aadd_texts`\(texts\[, metadatas, timeout, ...\]\) | Insert text data into Milvus asynchronously.   `add_documents`\(documents, \*\*kwargs\) | Run more documents through the embeddings and add to the vectorstore.   `add_embeddings`\(texts, embeddings\[, ...\]\) | Insert text data with embeddings vectors into Milvus.   `add_texts`\(texts\[, metadatas, timeout, ...\]\) | Insert text data into Milvus.   `adelete`\(\[ids, expr\]\) | Async delete by vector ID or boolean expression.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a Milvus collection, indexes it with HNSW, and insert data asynchronously.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `aget_pks`\(expr, \*\*kwargs\) | Async get primary keys with expression   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Perform an async search and return results that are reordered by MMR.   `amax_marginal_relevance_search_by_vector`\(...\) | Perform an async search and return results that are reordered by MMR.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asearch_by_metadata`\(expr\[, fields, limit\]\) | Async searches the Milvus vector store based on metadata conditions.   `asimilarity_search`\(query\[, k, param, expr, ...\]\) | Perform an async similarity search against the query string.   `asimilarity_search_by_vector`\(embedding\[, k, ...\]\) | Perform an async similarity search against the query vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(query\[, k, ...\]\) | Perform an async search on a query string and return results with score.   `asimilarity_search_with_score_by_vector`\(...\) | Perform an async search on an embedding and return results with score.   `aupsert`\(\[ids, documents, batch\_size, timeout\]\) | Update/Insert documents to the vectorstore asynchronously.   `delete`\(\[ids, expr\]\) | Delete by vector ID or boolean expression.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a Milvus collection, indexes it with HNSW, and insert data.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_pks`\(expr, \*\*kwargs\) | Get primary keys with expression   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Perform a search and return results that are reordered by MMR.   `max_marginal_relevance_search_by_vector`\(...\) | Perform a search and return results that are reordered by MMR.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `search_by_metadata`\(expr\[, fields, limit\]\) | Searches the Milvus vector store based on metadata conditions.   `similarity_search`\(query\[, k, param, expr, ...\]\) | Perform a similarity search against the query string.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Perform a similarity search against the query string.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Perform a search on a query string and return results with score.   `similarity_search_with_score_by_vector`\(embedding\) | Perform a search on an embedding and return results with score.   `upsert`\(\[ids, documents, batch\_size, timeout\]\) | Update/Insert documents to the vectorstore.      \_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/vectorstores/zilliz.html#Zilliz.__init__)\#     

Initialize the Milvus vector store.

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_async _aadd\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Run more documents through the embeddings and add to the vectorstore asynchronously.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **kwargs** \(_Any_\)

Returns:     

List of IDs of the added texts.

Return type:     

_List_\[str\]

_async _aadd\_embeddings\(

    _texts : List\[str\]_,     _embeddings : List\[List\[float\]\] | List\[List\[List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _timeout : float | None = None_,     _batch\_size : int = 1000_,     _\*_ ,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Insert text data with embeddings vectors into Milvus asynchronously.

This method inserts a batch of text embeddings into a Milvus collection. If the collection is not initialized, it will automatically initialize the collection based on the embeddings,metadatas, and other parameters. The embeddings are expected to be pre-generated using compatible embedding functions, and the metadata associated with each text is optional but must match the number of texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – the texts to insert

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]__|__List_ _\[__List_ _\[__List_ _\[__float_ _\]__\]__\]_\) – A vector embeddings for each text \(in case of a single vector\) or list of vectors for each text \(in case of multi-vector\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata dicts attached to each of the texts. Defaults to None.

  * **False.** \(_should be less than 65535 bytes. Required and work when auto\_id is_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for each batch insert. Defaults to None.

  * **batch\_size** \(_int_ _,__optional_\) – Batch size to use for insertion. Defaults to 1000.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. The length of each item

  * **kwargs** \(_Any_\)

Raises:     

**MilvusException** – Failure to add texts and embeddings

Returns:     

The resulting keys for each inserted element.

Return type:     

List\[str\]

_async _aadd\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _timeout : float | None = None_,     _batch\_size : int = 1000_,     _\*_ ,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Insert text data into Milvus asynchronously.

Inserting data when the collection has not be made yet will result in creating a new Collection. The data of the first entity decides the schema of the new collection, the dim is extracted from the first embedding and the columns are decided by the first metadata dict. Metadata keys will need to be present for all inserted values. At the moment there is no None equivalent in Milvus.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – The texts to embed, it is assumed that they all fit in memory.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata dicts attached to each of the texts. Defaults to None.

  * **False.** \(_should be less than 65535 bytes. Required and work when auto\_id is_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for each batch insert. Defaults to None.

  * **batch\_size** \(_int_ _,__optional_\) – Batch size to use for insertion. Defaults to 1000.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. The length of each item

  * **kwargs** \(_Any_\)

Raises:     

**MilvusException** – Failure to add texts

Returns:     

The resulting keys for each inserted element.

Return type:     

List\[str\]

add\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Run more documents through the embeddings and add to the vectorstore.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **kwargs** \(_Any_\)

Returns:     

List of IDs of the added texts.

Return type:     

_List_\[str\]

add\_embeddings\(

    _texts : List\[str\]_,     _embeddings : List\[List\[float\]\] | List\[List\[List\[float\]\]\]_,     _metadatas : List\[dict\] | None = None_,     _timeout : float | None = None_,     _batch\_size : int = 1000_,     _\*_ ,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Insert text data with embeddings vectors into Milvus.

This method inserts a batch of text embeddings into a Milvus collection. If the collection is not initialized, it will automatically initialize the collection based on the embeddings,metadatas, and other parameters. The embeddings are expected to be pre-generated using compatible embedding functions, and the metadata associated with each text is optional but must match the number of texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – the texts to insert

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]__|__List_ _\[__List_ _\[__List_ _\[__float_ _\]__\]__\]_\) – A vector embeddings for each text \(in case of a single vector\) or list of vectors for each text \(in case of multi-vector\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata dicts attached to each of the texts. Defaults to None.

  * **False.** \(_should be less than 65535 bytes. Required and work when auto\_id is_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for each batch insert. Defaults to None.

  * **batch\_size** \(_int_ _,__optional_\) – Batch size to use for insertion. Defaults to 1000.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. The length of each item

  * **kwargs** \(_Any_\)

Raises:     

**MilvusException** – Failure to add texts and embeddings

Returns:     

The resulting keys for each inserted element.

Return type:     

List\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _timeout : float | None = None_,     _batch\_size : int = 1000_,     _\*_ ,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\]\#     

Insert text data into Milvus.

Inserting data when the collection has not be made yet will result in creating a new Collection. The data of the first entity decides the schema of the new collection, the dim is extracted from the first embedding and the columns are decided by the first metadata dict. Metadata keys will need to be present for all inserted values. At the moment there is no None equivalent in Milvus.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – The texts to embed, it is assumed that they all fit in memory.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata dicts attached to each of the texts. Defaults to None.

  * **False.** \(_should be less than 65535 bytes. Required and work when auto\_id is_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for each batch insert. Defaults to None.

  * **batch\_size** \(_int_ _,__optional_\) – Batch size to use for insertion. Defaults to 1000.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. The length of each item

  * **kwargs** \(_Any_\)

Raises:     

**MilvusException** – Failure to add texts

Returns:     

The resulting keys for each inserted element.

Return type:     

List\[str\]

_async _adelete\(

    _ids : List\[str\] | None = None_,     _expr : str | None = None_,     _\*\* kwargs: Any_, \) → bool | None\#     

Async delete by vector ID or boolean expression. Refer to \[Milvus documentation\]\(<https://milvus.io/docs/delete_data.md>\) for notes and examples of expressions.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **expr** \(_str_ _|__None_\) – Boolean expression that specifies the entities to delete.

  * **kwargs** \(_Any_\) – Other parameters in Milvus delete api.

Returns:     

True if deletion is successful, False otherwise.

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | [BaseSparseEmbedding](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") | List\[[Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | [BaseSparseEmbedding](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding")\] | None_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'LangChainCollection'_,     _connection\_args : Dict\[str, Any\] | None = None_,     _consistency\_level : str = 'Session'_,     _index\_params : dict | List\[dict\] | None = None_,     _search\_params : dict | List\[dict\] | None = None_,     _drop\_old : bool = False_,     _\*_ ,     _ids : List\[str\] | None = None_,     _auto\_id : bool = False_,     _builtin\_function : [BaseMilvusBuiltInFunction](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") | List\[[BaseMilvusBuiltInFunction](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction")\] | None = None_,     _\*\* kwargs: Any_, \) → [Milvus](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")\#     

Create a Milvus collection, indexes it with HNSW, and insert data asynchronously.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Text data.

  * **embedding** \(_Optional_ _\[__Union_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _,_[_BaseSparseEmbedding_](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") _\]__\]_\) – Embedding function.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata for each text if it exists. Defaults to None.

  * **collection\_name** \(_str_ _,__optional_\) – Collection name to use. Defaults to “LangChainCollection”.

  * **connection\_args** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – Connection args to use. Defaults to DEFAULT\_MILVUS\_CONNECTION.

  * **consistency\_level** \(_str_ _,__optional_\) – Which consistency level to use. Defaults to “Session”.

  * **index\_params** \(_Optional_ _\[__dict_ _\]__,__optional_\) – Which index\_params to use. Defaults to None.

  * **search\_params** \(_Optional_ _\[__dict_ _\]__,__optional_\) – Which search params to use. Defaults to None.

  * **drop\_old** \(_Optional_ _\[__bool_ _\]__,__optional_\) – Whether to drop the collection with that name if it exists. Defaults to False.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. Defaults to None.

  * **auto\_id** \(_bool_\) – Whether to enable auto id for primary key. Defaults to False. If False, you need to provide text ids \(string less than 65535 bytes\). If True, Milvus will generate unique integers as primary keys.

  * **\(****Optional****\[****Union****\[****BaseMilvusBuiltInFunction** \(_builtin\_function_\) – List\[BaseMilvusBuiltInFunction\]\]\]\): Built-in function to use. Defaults to None.

  * **builtin\_function** \([_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _|__List_ _\[_[_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Milvus_](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")

:paramList\[BaseMilvusBuiltInFunction\]\]\]\):     

Built-in function to use. Defaults to None.

Parameters:     

  * **\*\*kwargs** \(_Any_\) – Other parameters in Milvus Collection.

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|_[_BaseSparseEmbedding_](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") _|__List_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|_[_BaseSparseEmbedding_](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") _\]__|__None_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **connection\_args** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **consistency\_level** \(_str_\)

  * **index\_params** \(_dict_ _|__List_ _\[__dict_ _\]__|__None_\)

  * **search\_params** \(_dict_ _|__List_ _\[__dict_ _\]__|__None_\)

  * **drop\_old** \(_bool_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **auto\_id** \(_bool_\)

  * **builtin\_function** \([_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _|__List_ _\[_[_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _\]__|__None_\)

  * **\*\*kwargs**

Returns:     

Milvus Vector Store

Return type:     

[Milvus](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")

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

_async _aget\_pks\(

    _expr : str_,     _\*\* kwargs: Any_, \) → List\[int\] | None\#     

Async get primary keys with expression

Parameters:     

  * **expr** \(_str_\) – Expression - E.g: “id in \[1, 2\]”, or “title LIKE ‘Abc%’”

  * **kwargs** \(_Any_\)

Returns:     

List of IDs \(Primary Keys\)

Return type:     

List\[int\]

_async _amax\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform an async search and return results that are reordered by MMR.

Parameters:     

  * **query** \(_str_\) – The text being searched.

  * **k** \(_int_ _,__optional_\) – How many results to give. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **param** \(_dict_ _,__optional_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _amax\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\] | dict\[int, float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform an async search and return results that are reordered by MMR.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]__|__dict_ _\[__int_ _,__float_ _\]_\) – The embedding vector being searched.

  * **k** \(_int_ _,__optional_\) – How many results to give. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **param** \(_dict_ _,__optional_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

_async _asearch\_by\_metadata\(

    _expr : str_,     _fields : List\[str\] | None = None_,     _limit : int = 10_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async searches the Milvus vector store based on metadata conditions.

This function performs a metadata-based query using an expression that filters stored documents without vector similarity.

Parameters:     

  * **expr** \(_str_\) – A filtering expression \(e.g., “city == ‘Seoul’”\).

  * **fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of fields to retrieve. If None, retrieves all available fields.

  * **limit** \(_int_\) – Maximum number of results to return.

Returns:     

List of documents matching the metadata filter.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\(

    _query : str_,     _k : int = 4_,     _param : dict | list\[dict\] | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform an async similarity search against the query string.

Parameters:     

  * **query** \(_str_\) – The text to search.

  * **k** \(_int_ _,__optional_\) – How many results to return. Defaults to 4.

  * **param** \(_dict_ _|__list_ _\[__dict_ _\]__,__optional_\) – The search params for the index type. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_int_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _asimilarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform an async similarity search against the query vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – The embedding vector to search.

  * **k** \(_int_ _,__optional_\) – How many results to return. Defaults to 4.

  * **param** \(_dict_ _,__optional_\) – The search params for the index type. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_int_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _param : dict | list\[dict\] | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Perform an async search on a query string and return results with score.

For more information about the search parameters, take a look at the pymilvus documentation found here: <https://milvus.io/api-reference/pymilvus/v2.5.x/ORM/Collection/search.md>

Parameters:     

  * **query** \(_str_\) – The text being searched.

  * **k** \(_int_ _,__optional_\) – The amount of results to return. Defaults to 4.

  * **param** \(_dict_ _|__list_ _\[__dict_ _\]__,__optional_\) – The search params for the specified

  * **None.** \(_index. Defaults to_\)

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) or hybrid\_search\(\) keyword arguments.

Returns:     

List of result doc and score.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _asimilarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\] | Dict\[int, float\]_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Perform an async search on an embedding and return results with score.

For more information about the search parameters, take a look at the pymilvus documentation found here: <https://milvus.io/api-reference/pymilvus/v2.5.x/ORM/Collection/search.md>

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__Dict_ _\[__int_ _,__float_ _\]_\) – The embedding vector being searched.

  * **k** \(_int_ _,__optional_\) – The amount of results to return. Defaults to 4.

  * **param** \(_dict_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Result doc and score.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

_async _aupsert\(

    _ids : List\[str\] | None = None_,     _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _batch\_size : int = 1000_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → None\#     

Update/Insert documents to the vectorstore asynchronously.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – IDs to update - Let’s call aget\_pks to get ids with expression

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **batch\_size** \(_int_ _,__optional_\) – Batch size to use for upsert. Defaults to 1000.

  * **timeout** \(_Optional_ _\[__float_ _\]_\) – Timeout for each batch upsert. Defaults to None.

  * **\*\*kwargs** – Other parameters in Milvus upsert api.

Return type:     

None

delete\(

    _ids : List\[str\] | None = None_,     _expr : str | None = None_,     _\*\* kwargs: str_, \) → bool | None\#     

Delete by vector ID or boolean expression. Refer to \[Milvus documentation\]\(<https://milvus.io/docs/delete_data.md>\) for notes and examples of expressions.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids to delete.

  * **expr** \(_str_ _|__None_\) – Boolean expression that specifies the entities to delete.

  * **kwargs** \(_str_\) – Other parameters in Milvus delete api.

Returns:     

True if deletion is successful, False otherwise.

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

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | [BaseSparseEmbedding](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") | List\[[Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | [BaseSparseEmbedding](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding")\] | None_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'LangChainCollection'_,     _connection\_args : Dict\[str, Any\] | None = None_,     _consistency\_level : str = 'Session'_,     _index\_params : dict | List\[dict\] | None = None_,     _search\_params : dict | List\[dict\] | None = None_,     _drop\_old : bool = False_,     _\*_ ,     _ids : List\[str\] | None = None_,     _auto\_id : bool = False_,     _builtin\_function : [BaseMilvusBuiltInFunction](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") | List\[[BaseMilvusBuiltInFunction](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction")\] | None = None_,     _\*\* kwargs: Any_, \) → [Milvus](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")\#     

Create a Milvus collection, indexes it with HNSW, and insert data.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Text data.

  * **embedding** \(_Optional_ _\[__Union_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _,_[_BaseSparseEmbedding_](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") _\]__\]_\) – Embedding function.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata for each text if it exists. Defaults to None.

  * **collection\_name** \(_str_ _,__optional_\) – Collection name to use. Defaults to “LangChainCollection”.

  * **connection\_args** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – Connection args to use. Defaults to DEFAULT\_MILVUS\_CONNECTION.

  * **consistency\_level** \(_str_ _,__optional_\) – Which consistency level to use. Defaults to “Session”.

  * **index\_params** \(_Optional_ _\[__dict_ _\]__,__optional_\) – Which index\_params to use. Defaults to None.

  * **search\_params** \(_Optional_ _\[__dict_ _\]__,__optional_\) – Which search params to use. Defaults to None.

  * **drop\_old** \(_Optional_ _\[__bool_ _\]__,__optional_\) – Whether to drop the collection with that name if it exists. Defaults to False.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. Defaults to None.

  * **auto\_id** \(_bool_\) – Whether to enable auto id for primary key. Defaults to False. If False, you need to provide text ids \(string less than 65535 bytes\). If True, Milvus will generate unique integers as primary keys.

  * **\(****Optional****\[****Union****\[****BaseMilvusBuiltInFunction** \(_builtin\_function_\) – List\[BaseMilvusBuiltInFunction\]\]\]\): Built-in function to use. Defaults to None.

  * **builtin\_function** \([_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _|__List_ _\[_[_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _\]__|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

[_Milvus_](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")

:paramList\[BaseMilvusBuiltInFunction\]\]\]\):     

Built-in function to use. Defaults to None.

Parameters:     

  * **\*\*kwargs** \(_Any_\) – Other parameters in Milvus Collection.

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|_[_BaseSparseEmbedding_](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") _|__List_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _|_[_BaseSparseEmbedding_](https://python.langchain.com/api_reference/milvus/utils/langchain_milvus.utils.sparse.BaseSparseEmbedding.html#langchain_milvus.utils.sparse.BaseSparseEmbedding "langchain_milvus.utils.sparse.BaseSparseEmbedding") _\]__|__None_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

  * **collection\_name** \(_str_\)

  * **connection\_args** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **consistency\_level** \(_str_\)

  * **index\_params** \(_dict_ _|__List_ _\[__dict_ _\]__|__None_\)

  * **search\_params** \(_dict_ _|__List_ _\[__dict_ _\]__|__None_\)

  * **drop\_old** \(_bool_\)

  * **ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **auto\_id** \(_bool_\)

  * **builtin\_function** \([_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _|__List_ _\[_[_BaseMilvusBuiltInFunction_](https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BaseMilvusBuiltInFunction.html#langchain_milvus.function.BaseMilvusBuiltInFunction "langchain_milvus.function.BaseMilvusBuiltInFunction") _\]__|__None_\)

  * **\*\*kwargs**

Returns:     

Milvus Vector Store

Return type:     

[Milvus](https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.Milvus.html#langchain_milvus.vectorstores.milvus.Milvus "langchain_milvus.vectorstores.milvus.Milvus")

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

get\_pks\(

    _expr : str_,     _\*\* kwargs: Any_, \) → List\[int\] | None\#     

Get primary keys with expression

Parameters:     

  * **expr** \(_str_\) – Expression - E.g: “id in \[1, 2\]”, or “title LIKE ‘Abc%’”

  * **kwargs** \(_Any_\)

Returns:     

List of IDs \(Primary Keys\)

Return type:     

List\[int\]

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform a search and return results that are reordered by MMR.

Parameters:     

  * **query** \(_str_\) – The text being searched.

  * **k** \(_int_ _,__optional_\) – How many results to give. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **param** \(_dict_ _,__optional_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : list\[float\] | dict\[int, float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform a search and return results that are reordered by MMR.

Parameters:     

  * **embedding** \(_list_ _\[__float_ _\]__|__dict_ _\[__int_ _,__float_ _\]_\) – The embedding vector being searched.

  * **k** \(_int_ _,__optional_\) – How many results to give. Defaults to 4.

  * **fetch\_k** \(_int_ _,__optional_\) – Total results to select k from. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5

  * **param** \(_dict_ _,__optional_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

search\_by\_metadata\(

    _expr : str_,     _fields : List\[str\] | None = None_,     _limit : int = 10_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Searches the Milvus vector store based on metadata conditions.

This function performs a metadata-based query using an expression that filters stored documents without vector similarity.

Parameters:     

  * **expr** \(_str_\) – A filtering expression \(e.g., “city == ‘Seoul’”\).

  * **fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of fields to retrieve. If None, retrieves all available fields.

  * **limit** \(_int_\) – Maximum number of results to return.

Returns:     

List of documents matching the metadata filter.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\(

    _query : str_,     _k : int = 4_,     _param : dict | list\[dict\] | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform a similarity search against the query string.

Parameters:     

  * **query** \(_str_\) – The text to search.

  * **k** \(_int_ _,__optional_\) – How many results to return. Defaults to 4.

  * **param** \(_dict_ _|__list_ _\[__dict_ _\]__,__optional_\) – The search params for the index type. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_int_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Perform a similarity search against the query string.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – The embedding vector to search.

  * **k** \(_int_ _,__optional_\) – How many results to return. Defaults to 4.

  * **param** \(_dict_ _,__optional_\) – The search params for the index type. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_int_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

    _query : str_,     _k : int = 4_,     _param : dict | list\[dict\] | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Perform a search on a query string and return results with score.

For more information about the search parameters, take a look at the pymilvus documentation found here: <https://milvus.io/api-reference/pymilvus/v2.5.x/ORM/Collection/search.md>

Parameters:     

  * **query** \(_str_\) – The text being searched.

  * **k** \(_int_ _,__optional_\) – The amount of results to return. Defaults to 4.

  * **param** \(_dict_ _|__list_ _\[__dict_ _\]__,__optional_\) – The search params for the specified

  * **None.** \(_index. Defaults to_\)

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) or hybrid\_search\(\) keyword arguments.

Returns:     

List of result doc and score.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\] | Dict\[int, float\]_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]\#     

Perform a search on an embedding and return results with score.

For more information about the search parameters, take a look at the pymilvus documentation found here: <https://milvus.io/api-reference/pymilvus/v2.5.x/ORM/Collection/search.md>

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]__|__Dict_ _\[__int_ _,__float_ _\]_\) – The embedding vector being searched.

  * **k** \(_int_ _,__optional_\) – The amount of results to return. Defaults to 4.

  * **param** \(_dict_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Result doc and score.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

upsert\(

    _ids : List\[str\] | None = None_,     _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _batch\_size : int = 1000_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → None\#     

Update/Insert documents to the vectorstore.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – IDs to update - Let’s call get\_pks to get ids with expression

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **batch\_size** \(_int_\)

  * **timeout** \(_float_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)