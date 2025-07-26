# Milvus — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.milvus.Milvus.html
**Word Count:** 2739
**Links Count:** 495
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# Milvus\#

_class _langchain\_community.vectorstores.milvus.Milvus\(

    _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'LangChainCollection'_,     _collection\_description : str = ''_,     _collection\_properties : dict\[str, Any\] | None = None_,     _connection\_args : dict\[str, Any\] | None = None_,     _consistency\_level : str = 'Session'_,     _index\_params : dict | None = None_,     _search\_params : dict | None = None_,     _drop\_old : bool | None = False_,     _auto\_id : bool = False_,     _\*_ ,     _primary\_field : str = 'pk'_,     _text\_field : str = 'text'_,     _vector\_field : str = 'vector'_,     _metadata\_field : str | None = None_,     _partition\_key\_field : str | None = None_,     _partition\_names : list | None = None_,     _replica\_number : int = 1_,     _timeout : float | None = None_,     _num\_shards : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus)\#     

Deprecated since version 0.2.0: Use `:class:`~langchain_milvus.MilvusVectorStore`` instead. It will not be removed until langchain-community==1.0.

Milvus vector store.

You need to install pymilvus and run Milvus.

See the following documentation for how to run a Milvus instance: <https://milvus.io/docs/install_standalone-docker.md>

If looking for a hosted Milvus, take a look at this documentation: <https://zilliz.com/cloud> and make use of the Zilliz vectorstore found in this project.

IF USING L2/IP metric, IT IS HIGHLY SUGGESTED TO NORMALIZE YOUR DATA.

Parameters:     

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Function used to embed the text.

  * **collection\_name** \(_str_\) – Which Milvus collection to use. Defaults to “LangChainCollection”.

  * **collection\_description** \(_str_\) – The description of the collection. Defaults to “”.

  * **collection\_properties** \(_Optional_ _\[__dict_ _\[__str_ _,__any_ _\]__\]_\) – The collection properties. Defaults to None. If set, will override collection existing properties. For example: \{“collection.ttl.seconds”: 60\}.

  * **connection\_args** \(_Optional_ _\[__dict_ _\[__str_ _,__any_ _\]__\]_\) – The connection args used for this class comes in the form of a dict.

  * **consistency\_level** \(_str_\) – The consistency level to use for a collection. Defaults to “Session”.

  * **index\_params** \(_Optional_ _\[__dict_ _\]_\) – Which index params to use. Defaults to HNSW/AUTOINDEX depending on service.

  * **search\_params** \(_Optional_ _\[__dict_ _\]_\) – Which search params to use. Defaults to default of index.

  * **drop\_old** \(_Optional_ _\[__bool_ _\]_\) – Whether to drop the current collection. Defaults to False.

  * **auto\_id** \(_bool_\) – Whether to enable auto id for primary key. Defaults to False. If False, you needs to provide text ids \(string less than 65535 bytes\). If True, Milvus will generate unique integers as primary keys.

  * **primary\_field** \(_str_\) – Name of the primary key field. Defaults to “pk”.

  * **text\_field** \(_str_\) – Name of the text field. Defaults to “text”.

  * **vector\_field** \(_str_\) – Name of the vector field. Defaults to “vector”.

  * **metadata\_field** \(_str_\) – Name of the metadata field. Defaults to None. When metadata\_field is specified, the document’s metadata will store as json.

  * **partition\_key\_field** \(_Optional_ _\[__str_ _\]_\)

  * **partition\_names** \(_Optional_ _\[__list_ _\]_\)

  * **replica\_number** \(_int_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\)

  * **num\_shards** \(_Optional_ _\[__int_ _\]_\)

The connection args used for this class comes in the form of a dict, here are a few of the options:

> address \(str\): The actual address of Milvus >      >  > instance. Example address: “localhost:19530” >  > uri \(str\): The uri of Milvus instance. Example uri: >      >  > “<http://randomwebsite:19530>”, “[tcp:foobarsite:19530](tcp:foobarsite:19530)”, “<https://ok.s3.south.com:19530>”. >  > host \(str\): The host of Milvus instance. Default at “localhost”, >      >  > PyMilvus will fill in the default host if only port is provided. >  > port \(str/int\): The port of Milvus instance. Default at 19530, PyMilvus >      >  > will fill in the default port if only host is provided. >  > user \(str\): Use which user to connect to Milvus instance. If user and >      >  > password are provided, we will add related header in every RPC call. >  > password \(str\): Required when user is provided. The password >      >  > corresponding to the user. >  > secure \(bool\): Default is false. If set to true, tls will be enabled. client\_key\_path \(str\): If use tls two-way authentication, need to >
>> write the client.key path. >  > client\_pem\_path \(str\): If use tls two-way authentication, need to >      >  > write the client.pem path. >  > ca\_pem\_path \(str\): If use tls two-way authentication, need to write >      >  > the ca.pem path. >  > server\_pem\_path \(str\): If use tls one-way authentication, need to >      >  > write the server.pem path. >  > server\_name \(str\): If use tls, need to write the common name.

Example               

from langchain\_community.vectorstores import Milvus from langchain\_community.embeddings import OpenAIEmbeddings

embedding = OpenAIEmbeddings\(\) \# Connect to a milvus instance on localhost milvus\_store = Milvus\(

> embedding\_function = Embeddings, collection\_name = “LangChainCollection”, drop\_old = True, auto\_id = True

\)

Raises:     

**ValueError** – If the pymilvus python package is not installed.

Parameters:     

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **collection\_description** \(_str_\)

  * **collection\_properties** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **connection\_args** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **consistency\_level** \(_str_\)

  * **index\_params** \(_Optional_ _\[__dict_ _\]_\)

  * **search\_params** \(_Optional_ _\[__dict_ _\]_\)

  * **drop\_old** \(_Optional_ _\[__bool_ _\]_\)

  * **auto\_id** \(_bool_\)

  * **primary\_field** \(_str_\)

  * **text\_field** \(_str_\)

  * **vector\_field** \(_str_\)

  * **metadata\_field** \(_Optional_ _\[__str_ _\]_\)

  * **partition\_key\_field** \(_Optional_ _\[__str_ _\]_\)

  * **partition\_names** \(_Optional_ _\[__list_ _\]_\)

  * **replica\_number** \(_int_\)

  * **timeout** \(_Optional_ _\[__float_ _\]_\)

  * **num\_shards** \(_Optional_ _\[__int_ _\]_\)

Initialize the Milvus vector store.

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(embedding\_function\[, ...\]\) | Initialize the Milvus vector store.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_texts`\(texts\[, metadatas, timeout, ...\]\) | Insert text data into Milvus.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `delete`\(\[ids, expr\]\) | Delete by vector ID or boolean expression.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a Milvus collection, indexes it with HNSW, and insert data.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `get_pks`\(expr, \*\*kwargs\) | Get primary keys with expression   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Perform a search and return results that are reordered by MMR.   `max_marginal_relevance_search_by_vector`\(...\) | Perform a search and return results that are reordered by MMR.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, param, expr, ...\]\) | Perform a similarity search against the query string.   `similarity_search_by_vector`\(embedding\[, k, ...\]\) | Perform a similarity search against the query string.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Perform a search on a query string and return results with score.   `similarity_search_with_score_by_vector`\(embedding\) | Perform a search on a query string and return results with score.   `upsert`\(\[ids, documents\]\) | Update/Insert documents to the vectorstore.      \_\_init\_\_\(

    _embedding\_function : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _collection\_name : str = 'LangChainCollection'_,     _collection\_description : str = ''_,     _collection\_properties : dict\[str, Any\] | None = None_,     _connection\_args : dict\[str, Any\] | None = None_,     _consistency\_level : str = 'Session'_,     _index\_params : dict | None = None_,     _search\_params : dict | None = None_,     _drop\_old : bool | None = False_,     _auto\_id : bool = False_,     _\*_ ,     _primary\_field : str = 'pk'_,     _text\_field : str = 'text'_,     _vector\_field : str = 'vector'_,     _metadata\_field : str | None = None_,     _partition\_key\_field : str | None = None_,     _partition\_names : list | None = None_,     _replica\_number : int = 1_,     _timeout : float | None = None_,     _num\_shards : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.__init__)\#     

Initialize the Milvus vector store.

Parameters:     

  * **embedding\_function** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **collection\_name** \(_str_\)

  * **collection\_description** \(_str_\)

  * **collection\_properties** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **connection\_args** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **consistency\_level** \(_str_\)

  * **index\_params** \(_dict_ _|__None_\)

  * **search\_params** \(_dict_ _|__None_\)

  * **drop\_old** \(_bool_ _|__None_\)

  * **auto\_id** \(_bool_\)

  * **primary\_field** \(_str_\)

  * **text\_field** \(_str_\)

  * **vector\_field** \(_str_\)

  * **metadata\_field** \(_str_ _|__None_\)

  * **partition\_key\_field** \(_str_ _|__None_\)

  * **partition\_names** \(_list_ _|__None_\)

  * **replica\_number** \(_int_\)

  * **timeout** \(_float_ _|__None_\)

  * **num\_shards** \(_int_ _|__None_\)

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

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _timeout : float | None = None_,     _batch\_size : int = 1000_,     _\*_ ,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.add_texts)\#     

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

    _ids : List\[str\] | None = None_,     _expr : str | None = None_,     _\*\* kwargs: Any_, \) → MutationResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.delete)\#     

Delete by vector ID or boolean expression. Refer to \[Milvus documentation\]\(<https://milvus.io/docs/delete_data.md>\) for notes and examples of expressions.

Parameters:     

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of ids to delete.

  * **expr** \(_Optional_ _\[__str_ _\]_\) – Boolean expression that specifies the entities to delete.

  * **kwargs** \(_Any_\) – Other parameters in Milvus delete api.

Return type:     

MutationResult

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _collection\_name : str = 'LangChainCollection'_,     _connection\_args : dict\[str, Any\] = \{'host': 'localhost', 'password': '', 'port': '19530', 'secure': False, 'user': ''\}_,     _consistency\_level : str = 'Session'_,     _index\_params : dict | None = None_,     _search\_params : dict | None = None_,     _drop\_old : bool = False_,     _\*_ ,     _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → Milvus[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.from_texts)\#     

Create a Milvus collection, indexes it with HNSW, and insert data.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – Text data.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding function.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]_\) – Metadata for each text if it exists. Defaults to None.

  * **collection\_name** \(_str_ _,__optional_\) – Collection name to use. Defaults to “LangChainCollection”.

  * **connection\_args** \(_dict_ _\[__str_ _,__Any_ _\]__,__optional_\) – Connection args to use. Defaults to DEFAULT\_MILVUS\_CONNECTION.

  * **consistency\_level** \(_str_ _,__optional_\) – Which consistency level to use. Defaults to “Session”.

  * **index\_params** \(_Optional_ _\[__dict_ _\]__,__optional_\) – Which index\_params to use. Defaults to None.

  * **search\_params** \(_Optional_ _\[__dict_ _\]__,__optional_\) – Which search params to use. Defaults to None.

  * **drop\_old** \(_Optional_ _\[__bool_ _\]__,__optional_\) – Whether to drop the collection with that name if it exists. Defaults to False.

  * **ids** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of text ids. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

Milvus Vector Store

Return type:     

Milvus

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

    _expr : str_,     _\*\* kwargs: Any_, \) → List\[int\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.get_pks)\#     

Get primary keys with expression

Parameters:     

  * **expr** \(_str_\) – Expression - E.g: “id in \[1, 2\]”, or “title LIKE ‘Abc%’”

  * **kwargs** \(_Any_\)

Returns:     

List of IDs \(Primary Keys\)

Return type:     

List\[int\]

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.max_marginal_relevance_search)\#     

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

    _embedding : list\[float\]_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.max_marginal_relevance_search_by_vector)\#     

Perform a search and return results that are reordered by MMR.

Parameters:     

  * **embedding** \(_str_\) – The embedding vector being searched.

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

similarity\_search\(

    _query : str_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.similarity_search)\#     

Perform a similarity search against the query string.

Parameters:     

  * **query** \(_str_\) – The text to search.

  * **k** \(_int_ _,__optional_\) – How many results to return. Defaults to 4.

  * **param** \(_dict_ _,__optional_\) – The search params for the index type. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_int_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Returns:     

Document results for search.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

similarity\_search\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.similarity_search_by_vector)\#     

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

    _query : str_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.similarity_search_with_score)\#     

Perform a search on a query string and return results with score.

For more information about the search parameters, take a look at the pymilvus documentation found here: <https://milvus.io/api-reference/pymilvus/v2.2.6/Collection/search().md>

Parameters:     

  * **query** \(_str_\) – The text being searched.

  * **k** \(_int_ _,__optional_\) – The amount of results to return. Defaults to 4.

  * **param** \(_dict_\) – The search params for the specified index. Defaults to None.

  * **expr** \(_str_ _,__optional_\) – Filtering expression. Defaults to None.

  * **timeout** \(_float_ _,__optional_\) – How long to wait before timeout error. Defaults to None.

  * **kwargs** \(_Any_\) – Collection.search\(\) keyword arguments.

Return type:     

List\[float\], List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), any, any\]\]

similarity\_search\_with\_score\_by\_vector\(

    _embedding : List\[float\]_,     _k : int = 4_,     _param : dict | None = None_,     _expr : str | None = None_,     _timeout : float | None = None_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.similarity_search_with_score_by_vector)\#     

Perform a search on a query string and return results with score.

For more information about the search parameters, take a look at the pymilvus documentation found here: <https://milvus.io/api-reference/pymilvus/v2.2.6/Collection/search().md>

Parameters:     

  * **embedding** \(_List_ _\[__float_ _\]_\) – The embedding vector being searched.

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

    _ids : List\[str\] | None = None_,     _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_,     _\*\* kwargs: Any_, \) → List\[str\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/milvus.html#Milvus.upsert)\#     

Update/Insert documents to the vectorstore.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__|__None_\) – IDs to update - Let’s call get\_pks to get ids with expression

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Documents to add to the vectorstore.

  * **kwargs** \(_Any_\)

Returns:     

IDs of the added texts.

Return type:     

List\[str\]

Examples using Milvus

  * [Milvus](https://python.langchain.com/docs/integrations/providers/milvus/)

  * [Zilliz](https://python.langchain.com/docs/integrations/vectorstores/zilliz/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)