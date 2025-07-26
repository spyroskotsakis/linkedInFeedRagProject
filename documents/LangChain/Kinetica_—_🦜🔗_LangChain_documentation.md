# Kinetica — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.Kinetica.html
**Word Count:** 2550
**Links Count:** 545
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# Kinetica\#

_class _langchain\_community.vectorstores.kinetica.Kinetica\(

    _config : [KineticaSettings](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'langchain\_kinetica\_embeddings'_,     _schema\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") = DistanceStrategy.EUCLIDEAN_,     _pre\_delete\_collection : bool = False_,     _logger : Logger | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica)\#     

Kinetica vector store.

To use, you should have the `gpudb` python package installed.

Parameters:     

  * **config** \([_KineticaSettings_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")\) – Kinetica connection settings class.

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Any embedding function implementing langchain.embeddings.base.Embeddings interface.

  * **collection\_name** \(_str_\) – The name of the collection to use. \(default: langchain\) NOTE: This is not the name of the table, but the name of the collection. The tables will be created when initializing the store \(if not exists\) So, make sure the user has the right permissions to create tables.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy")\) – The distance strategy to use. \(default: COSINE\)

  * **pre\_delete\_collection** \(_bool_\) – If True, will delete the collection if it exists. \(default: False\). Useful for testing.

  * **engine\_args** – SQLAlchemy’s create engine arguments.

  * **schema\_name** \(_str_\)

  * **logger** \(_Optional_ _\[__logging.Logger_ _\]_\)

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

Example               from langchain_community.vectorstores import Kinetica, KineticaSettings     from langchain_community.embeddings.openai import OpenAIEmbeddings          kinetica_settings = KineticaSettings(         host="http://127.0.0.1", username="", password=""         )     COLLECTION_NAME = "kinetica_store"     embeddings = OpenAIEmbeddings()     vectorstore = Kinetica.from_documents(         documents=docs,         embedding=embeddings,         collection_name=COLLECTION_NAME,         config=kinetica_settings,     )     

Constructor for the Kinetica class

Parameters:     

  * **config** \([_KineticaSettings_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")\) – a KineticaSettings instance

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – embedding function to use

  * **collection\_name** \(_str_ _,__optional_\) – the Kinetica table name. Defaults to \_LANGCHAIN\_DEFAULT\_COLLECTION\_NAME.

  * **schema\_name** \(_str_ _,__optional_\) – the Kinetica table name. Defaults to \_LANGCHAIN\_DEFAULT\_SCHEMA\_NAME.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") _,__optional_\) – \_description\_. Defaults to DEFAULT\_DISTANCE\_STRATEGY.

  * **pre\_delete\_collection** \(_bool_ _,__optional_\) – \_description\_. Defaults to False.

  * **logger** \(_Optional_ _\[__logging.Logger_ _\]__,__optional_\) – \_description\_. Defaults to None.

  * **relevance\_score\_fn** \(_Optional_ _\[__Callable_ _\[__\[__float_ _\]__,__float_ _\]__\]_\)

Attributes

`distance_strategy` |    ---|---   `embeddings` | Access the query embedding object if available.      Methods

`__init__`\(config, embedding\_function\[, ...\]\) | Constructor for the Kinetica class   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_embeddings`\(texts, embeddings\[, ...\]\) | Add embeddings to the vectorstore.   `add_texts`\(texts\[, metadatas, ids\]\) | Run more texts through the embeddings and add to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `create_schema`\(\) | Create a new Kinetica schema   `create_tables_if_not_exists`\(\) | Create the table to store the texts and embeddings   `delete`\(\[ids\]\) | Delete by vector ID or other criteria.   `delete_schema`\(\) | Delete a Kinetica schema with cascade set to true This method will delete a schema with all tables in it.   `drop_tables`\(\) | Delete the table   `from_documents`\(documents, embedding\[, ...\]\) | Adds the list of Document passed in to the vector store and returns it   `from_embeddings`\(text\_embeddings, embedding\) | Adds the embeddings passed in to the vector store and returns it   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Adds the texts passed in to the vector store and returns it   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance   `max_marginal_relevance_search_with_score`\(query\) | Return docs selected using the maximal marginal relevance with score.   `max_marginal_relevance_search_with_score_by_vector`\(...\) | Return docs selected using the maximal marginal relevance with score   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter\]\) | Run similarity search with Kinetica with distance.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, filter\]\) | Return docs most similar to query.   `similarity_search_with_score_by_vector`\(embedding\) |       \_\_init\_\_\(

    _config : [KineticaSettings](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")_,     _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'langchain\_kinetica\_embeddings'_,     _schema\_name : str = 'langchain'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") = DistanceStrategy.EUCLIDEAN_,     _pre\_delete\_collection : bool = False_,     _logger : Logger | None = None_,     _relevance\_score\_fn : Callable\[\[float\], float\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.__init__)\#     

Constructor for the Kinetica class

Parameters:     

  * **config** \([_KineticaSettings_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")\) – a KineticaSettings instance

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – embedding function to use

  * **collection\_name** \(_str_ _,__optional_\) – the Kinetica table name. Defaults to \_LANGCHAIN\_DEFAULT\_COLLECTION\_NAME.

  * **schema\_name** \(_str_ _,__optional_\) – the Kinetica table name. Defaults to \_LANGCHAIN\_DEFAULT\_SCHEMA\_NAME.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") _,__optional_\) – \_description\_. Defaults to DEFAULT\_DISTANCE\_STRATEGY.

  * **pre\_delete\_collection** \(_bool_ _,__optional_\) – \_description\_. Defaults to False.

  * **logger** \(_Optional_ _\[__logging.Logger_ _\]__,__optional_\) – \_description\_. Defaults to None.

  * **relevance\_score\_fn** \(_Callable_ _\[__\[__float_ _\]__,__float_ _\]__|__None_\)

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

add\_embeddings\(

    _texts : Iterable\[str\]_,     _embeddings : List\[List\[float\]\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.add_embeddings)\#     

Add embeddings to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **embeddings** \(_List_ _\[__List_ _\[__float_ _\]__\]_\) – List of list of embedding vectors.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – List of metadatas associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of ids for the text embedding pairs

  * **kwargs** \(_Any_\) – vectorstore specific parameters

Return type:     

_List_\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.add_texts)\#     

Run more texts through the embeddings and add to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings to add to the vectorstore.

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\) – Optional list of metadatas \(JSON data\) associated with the texts.

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – List of IDs \(UUID\) for the texts supplied; will be generated if None

  * **kwargs** \(_Any_\) – vectorstore specific parameters

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

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.amax_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **fetch\_k** \(_int_\)

  * **lambda\_mult** \(_float_\)

  * **filter** \(_Dict_ _\[__str_ _,__str_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

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

create\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.create_schema)\#     

Create a new Kinetica schema

Return type:     

None

create\_tables\_if\_not\_exists\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.create_tables_if_not_exists)\#     

Create the table to store the texts and embeddings

Return type:     

_Any_

delete\(

    _ids : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None\#     

Delete by vector ID or other criteria.

Parameters:     

  * **ids** \(_list_ _\[__str_ _\]__|__None_\) – List of ids to delete. If None, delete all. Default is None.

  * **\*\*kwargs** \(_Any_\) – Other keyword arguments that subclasses might use.

Returns:     

True if deletion is successful, False otherwise, None if not implemented.

Return type:     

Optional\[bool\]

delete\_schema\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.delete_schema)\#     

Delete a Kinetica schema with cascade set to true This method will delete a schema with all tables in it.

Return type:     

None

drop\_tables\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.drop_tables)\#     

Delete the table

Return type:     

None

_classmethod _from\_documents\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _config : [KineticaSettings](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings") = KineticaSettings\(host='http://127.0.0.1', port=9191, username=None, password=None, database='langchain', table='langchain\_kinetica\_embeddings', metric='l2'\)_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'langchain\_kinetica\_embeddings'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") = DistanceStrategy.EUCLIDEAN_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*_ ,     _schema\_name : str = 'langchain'_,     _\*\* kwargs: Any_, \) → Kinetica[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.from_documents)\#     

Adds the list of Document passed in to the vector store and returns it

Parameters:     

  * **cls** \(_Type_ _\[__Kinetica_ _\]_\) – Kinetica class

  * **texts** \(_List_ _\[__str_ _\]_\) – A list of texts for which the embeddings are generated

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – List of embeddings

  * **config** \([_KineticaSettings_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")\) – a KineticaSettings instance

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – List of dicts, JSON describing the texts/documents. Defaults to None.

  * **collection\_name** \(_str_ _,__optional_\) – Kinetica schema name. Defaults to \_LANGCHAIN\_DEFAULT\_COLLECTION\_NAME.

  * **schema\_name** \(_str_ _,__optional_\) – Kinetica schema name. Defaults to \_LANGCHAIN\_DEFAULT\_SCHEMA\_NAME.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") _,__optional_\) – Distance strategy e.g., l2, cosine etc.. Defaults to DEFAULT\_DISTANCE\_STRATEGY.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]__,__optional_\) – A list of UUIDs for each text/document. Defaults to None.

  * **pre\_delete\_collection** \(_bool_ _,__optional_\) – Indicates whether the Kinetica schema is to be deleted or not. Defaults to False.

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Returns:     

a Kinetica instance

Return type:     

Kinetica

_classmethod _from\_embeddings\(

    _text\_embeddings : List\[Tuple\[str, List\[float\]\]\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _config : [KineticaSettings](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings") = KineticaSettings\(host='http://127.0.0.1', port=9191, username=None, password=None, database='langchain', table='langchain\_kinetica\_embeddings', metric='l2'\)_,     _dimensions : int = Dimension.OPENAI_,     _collection\_name : str = 'langchain\_kinetica\_embeddings'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") = DistanceStrategy.EUCLIDEAN_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*_ ,     _schema\_name : str = 'langchain'_,     _\*\* kwargs: Any_, \) → Kinetica[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.from_embeddings)\#     

Adds the embeddings passed in to the vector store and returns it

Parameters:     

  * **cls** \(_Type_ _\[__Kinetica_ _\]_\) – Kinetica class

  * **text\_embeddings** \(_List_ _\[__Tuple_ _\[__str_ _,__List_ _\[__float_ _\]__\]__\]_\) – A list of texts and the embeddings

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – List of embeddings

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – List of dicts, JSON describing the texts/documents. Defaults to None.

  * **config** \([_KineticaSettings_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")\) – a KineticaSettings instance

  * **dimensions** \(_int_ _,__optional_\) – Dimension for the vector data, if not passed a default will be used. Defaults to Dimension.OPENAI.

  * **collection\_name** \(_str_ _,__optional_\) – Kinetica schema name. Defaults to \_LANGCHAIN\_DEFAULT\_COLLECTION\_NAME.

  * **schema\_name** \(_str_ _,__optional_\) – Kinetica schema name. Defaults to \_LANGCHAIN\_DEFAULT\_SCHEMA\_NAME.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") _,__optional_\) – Distance strategy e.g., l2, cosine etc.. Defaults to DEFAULT\_DISTANCE\_STRATEGY.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]__,__optional_\) – A list of UUIDs for each text/document. Defaults to None.

  * **pre\_delete\_collection** \(_bool_ _,__optional_\) – Indicates whether the Kinetica schema is to be deleted or not. Defaults to False.

  * **kwargs** \(_Any_\)

Returns:     

a Kinetica instance

Return type:     

Kinetica

_classmethod _from\_texts\(

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _config : [KineticaSettings](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings") = KineticaSettings\(host='http://127.0.0.1', port=9191, username=None, password=None, database='langchain', table='langchain\_kinetica\_embeddings', metric='l2'\)_,     _collection\_name : str = 'langchain\_kinetica\_embeddings'_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") = DistanceStrategy.EUCLIDEAN_,     _ids : List\[str\] | None = None_,     _pre\_delete\_collection : bool = False_,     _\*_ ,     _schema\_name : str = 'langchain'_,     _\*\* kwargs: Any_, \) → Kinetica[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.from_texts)\#     

Adds the texts passed in to the vector store and returns it

Parameters:     

  * **cls** \(_Type_ _\[__Kinetica_ _\]_\) – Kinetica class

  * **texts** \(_List_ _\[__str_ _\]_\) – A list of texts for which the embeddings are generated

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – List of embeddings

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – List of dicts, JSON describing the texts/documents. Defaults to None.

  * **config** \([_KineticaSettings_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html#langchain_community.vectorstores.kinetica.KineticaSettings "langchain_community.vectorstores.kinetica.KineticaSettings")\) – a KineticaSettings instance

  * **collection\_name** \(_str_ _,__optional_\) – Kinetica schema name. Defaults to \_LANGCHAIN\_DEFAULT\_COLLECTION\_NAME.

  * **schema\_name** \(_str_ _,__optional_\) – Kinetica schema name. Defaults to \_LANGCHAIN\_DEFAULT\_SCHEMA\_NAME.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.DistanceStrategy.html#langchain_community.vectorstores.kinetica.DistanceStrategy "langchain_community.vectorstores.kinetica.DistanceStrategy") _,__optional_\) – Distance strategy e.g., l2, cosine etc.. Defaults to DEFAULT\_DISTANCE\_STRATEGY.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]__,__optional_\) – A list of UUIDs for each text/document. Defaults to None.

  * **pre\_delete\_collection** \(_bool_ _,__optional_\) – Indicates whether the Kinetica schema is to be deleted or not. Defaults to False.

  * **kwargs** \(_Any_\)

Returns:     

a Kinetica instance

Return type:     

Kinetica

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

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.max_marginal_relevance_search)\#     

Return docs selected using the maximal marginal relevance.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.max_marginal_relevance_search_by_vector)\#     

Return docs selected using the maximal marginal relevance     

to embedding vector.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **embedding** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal relevance.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

max\_marginal\_relevance\_search\_with\_score\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.max_marginal_relevance_search_with_score)\#     

Return docs selected using the maximal marginal relevance with score.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal     

relevance to the query and score for each.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

max\_marginal\_relevance\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _filter : Dict\[str, str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.max_marginal_relevance_search_with_score_by_vector)\#     

Return docs selected using the maximal marginal relevance with score     

to embedding vector.

Maximal marginal relevance optimizes for similarity to query AND diversity     

among selected documents.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **fetch\_k** \(_int_\) – Number of Documents to fetch to pass to MMR algorithm. Defaults to 20.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents selected by maximal marginal     

relevance to the query and score for each.

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

similarity\_search\(

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.similarity_search)\#     

Run similarity search with Kinetica with distance.

Parameters:     

  * **query** \(_str_\) – Query text to search for.

  * **k** \(_int_\) – Number of results to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.similarity_search_by_vector)\#     

Return docs most similar to embedding vector.

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – Embedding to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query vector.

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.similarity_search_with_score)\#     

Return docs most similar to query.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – Filter by metadata. Defaults to None.

Returns:     

List of Documents most similar to the query and score for each

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _filter : dict | None = None_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#Kinetica.similarity_search_with_score_by_vector)\#     

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\)

  * **k** \(_int_\)

  * **filter** \(_dict_ _|__None_\)

Return type:     

_List_\[_Tuple_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples using Kinetica

  * [Kinetica](https://python.langchain.com/docs/integrations/providers/kinetica/)

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Kinetica Vectorstore based Retriever](https://python.langchain.com/docs/integrations/retrievers/kinetica/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)