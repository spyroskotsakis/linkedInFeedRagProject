# SingleStoreDB — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.singlestoredb.SingleStoreDB.html
**Word Count:** 4942
**Links Count:** 485
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# SingleStoreDB\#

_class _langchain\_community.vectorstores.singlestoredb.SingleStoreDB\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.DOT\_PRODUCT_,     _table\_name : str = 'embeddings'_,     _content\_field : str = 'content'_,     _metadata\_field : str = 'metadata'_,     _vector\_field : str = 'vector'_,     _id\_field : str = 'id'_,     _use\_vector\_index : bool = False_,     _vector\_index\_name : str = ''_,     _vector\_index\_options : dict | None = None_,     _vector\_size : int = 1536_,     _use\_full\_text\_search : bool = False_,     _pool\_size : int = 5_,     _max\_overflow : int = 10_,     _timeout : float = 30_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB)\#     

Deprecated since version 0.3.22: This class is pending deprecation and may be removed in a future version. You can swap to using the SingleStoreVectorStore implementation in langchain\_singlestore. See <[singlestore-labs/langchain-singlestore](https://github.com/singlestore-labs/langchain-singlestore)> for details about the new implementation. Use `from langchain_singlestore import SingleStoreVectorStore` instead.

SingleStore DB vector store.

The prerequisite for using this class is the installation of the `singlestoredb` Python package.

The SingleStoreDB vectorstore can be created by providing an embedding function and the relevant parameters for the database connection, connection pool, and optionally, the names of the table and the fields to use.

Initialize with necessary components.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – A text embedding model.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _,__optional_\) – 

Determines the strategy employed for calculating the distance between vectors in the embedding space. Defaults to DOT\_PRODUCT. Available options are: \- DOT\_PRODUCT: Computes the scalar product of two vectors.

> This is the default behavior

    * EUCLIDEAN\_DISTANCE: Computes the Euclidean distance between     

two vectors. This metric considers the geometric distance in the vector space, and might be more suitable for embeddings that rely on spatial relationships. This metric is not compatible with the WEIGHTED\_SUM search strategy.

  * **table\_name** \(_str_ _,__optional_\) – Specifies the name of the table in use. Defaults to “embeddings”.

  * **content\_field** \(_str_ _,__optional_\) – Specifies the field to store the content. Defaults to “content”.

  * **metadata\_field** \(_str_ _,__optional_\) – Specifies the field to store metadata. Defaults to “metadata”.

  * **vector\_field** \(_str_ _,__optional_\) – Specifies the field to store the vector. Defaults to “vector”.

  * **id\_field** \(_str_ _,__optional_\) – Specifies the field to store the id. Defaults to “id”.

  * **use\_vector\_index** \(_bool_ _,__optional_\) – Toggles the use of a vector index. Works only with SingleStoreDB 8.5 or later. Defaults to False. If set to True, vector\_size parameter is required to be set to a proper value.

  * **vector\_index\_name** \(_str_ _,__optional_\) – Specifies the name of the vector index. Defaults to empty. Will be ignored if use\_vector\_index is set to False.

  * **vector\_index\_options** \(_dict_ _,__optional_\) – 

Specifies the options for the vector index. Defaults to \{\}. Will be ignored if use\_vector\_index is set to False. The options are: index\_type \(str, optional\): Specifies the type of the index.

> Defaults to IVF\_PQFS.

For more options, please refer to the SingleStoreDB documentation: <https://docs.singlestore.com/cloud/reference/sql-reference/vector-functions/vector-indexing/>

  * **vector\_size** \(_int_ _,__optional_\) – Specifies the size of the vector. Defaults to 1536. Required if use\_vector\_index is set to True. Should be set to the same value as the size of the vectors stored in the vector\_field.

  * **use\_full\_text\_search** \(_bool_ _,__optional_\) – Toggles the use a full-text index on the document content. Defaults to False. If set to True, the table will be created with a full-text index on the content field, and the simularity\_search method will all using TEXT\_ONLY, FILTER\_BY\_TEXT, FILTER\_BY\_VECTOR, and WIGHTED\_SUM search strategies. If set to False, the simularity\_search method will only allow VECTOR\_ONLY search strategy.

  * **pool** \(_Following arguments pertain to the connection_\)

  * **pool\_size** \(_int_ _,__optional_\) – Determines the number of active connections in the pool. Defaults to 5.

  * **max\_overflow** \(_int_ _,__optional_\) – Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10.

  * **timeout** \(_float_ _,__optional_\) – Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30.

  * **connection** \(_database_\)

  * **host** \(_str_ _,__optional_\) – Specifies the hostname, IP address, or URL for the database connection. The default scheme is “mysql”.

  * **user** \(_str_ _,__optional_\) – Database username.

  * **password** \(_str_ _,__optional_\) – Database password.

  * **port** \(_int_ _,__optional_\) – Database port. Defaults to 3306 for non-HTTP connections, 80 for HTTP connections, and 443 for HTTPS connections.

  * **database** \(_str_ _,__optional_\) – Database name.

  * **the** \(_Additional optional arguments provide further customization over_\)

  * **connection**

  * **pure\_python** \(_bool_ _,__optional_\) – Toggles the connector mode. If True, operates in pure Python mode.

  * **local\_infile** \(_bool_ _,__optional_\) – Allows local file uploads.

  * **charset** \(_str_ _,__optional_\) – Specifies the character set for string values.

  * **ssl\_key** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL key.

  * **ssl\_cert** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate.

  * **ssl\_ca** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate authority.

  * **ssl\_cipher** \(_str_ _,__optional_\) – Sets the SSL cipher list.

  * **ssl\_disabled** \(_bool_ _,__optional_\) – Disables SSL usage.

  * **ssl\_verify\_cert** \(_bool_ _,__optional_\) – Verifies the server’s certificate. Automatically enabled if `ssl_ca` is specified.

  * **ssl\_verify\_identity** \(_bool_ _,__optional_\) – Verifies the server’s identity.

  * **conv** \(_dict_ _\[__int_ _,__Callable_ _\]__,__optional_\) – A dictionary of data conversion functions.

  * **credential\_type** \(_str_ _,__optional_\) – Specifies the type of authentication to use: auth.PASSWORD, auth.JWT, or auth.BROWSER\_SSO.

  * **autocommit** \(_bool_ _,__optional_\) – Enables autocommits.

  * **results\_type** \(_str_ _,__optional_\) – Determines the structure of the query results: tuples, namedtuples, dicts.

  * **results\_format** \(_str_ _,__optional_\) – Deprecated. This option has been renamed to results\_type.

  * **kwargs** \(_Any_\)

Examples

Basic Usage:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          vectorstore = SingleStoreDB(         OpenAIEmbeddings(),         host="https://user:password@127.0.0.1:3306/database"     )     

Advanced Usage:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          vectorstore = SingleStoreDB(         OpenAIEmbeddings(),         distance_strategy=DistanceStrategy.EUCLIDEAN_DISTANCE,         host="127.0.0.1",         port=3306,         user="user",         password="password",         database="db",         table_name="my_custom_table",         pool_size=10,         timeout=60,     )     

Using environment variables:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          os.environ['SINGLESTOREDB_URL'] = 'me:p455w0rd@s2-host.com/my_db'     vectorstore = SingleStoreDB(OpenAIEmbeddings())     

Using vector index:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          os.environ['SINGLESTOREDB_URL'] = 'me:p455w0rd@s2-host.com/my_db'     vectorstore = SingleStoreDB(         OpenAIEmbeddings(),         use_vector_index=True,     )     

Using full-text index:

Attributes

`embeddings` | Access the query embedding object if available.   ---|---      Methods

`__init__`\(embedding, \*\[, distance\_strategy, ...\]\) | Initialize with necessary components.   ---|---   `aadd_documents`\(documents, \*\*kwargs\) | Async run more documents through the embeddings and add to the vectorstore.   `aadd_texts`\(texts\[, metadatas, ids\]\) | Async run more texts through the embeddings and add to the vectorstore.   `add_documents`\(documents, \*\*kwargs\) | Add or update documents in the vectorstore.   `add_images`\(uris\[, metadatas, embeddings, ...\]\) | Run images through the embeddings and add to the vectorstore.   `add_texts`\(texts\[, metadatas, embeddings, ...\]\) | Add more texts to the vectorstore.   `adelete`\(\[ids\]\) | Async delete by vector ID or other criteria.   `afrom_documents`\(documents, embedding, \*\*kwargs\) | Async return VectorStore initialized from documents and embeddings.   `afrom_texts`\(texts, embedding\[, metadatas, ids\]\) | Async return VectorStore initialized from texts and embeddings.   `aget_by_ids`\(ids, /\) | Async get documents by their IDs.   `amax_marginal_relevance_search`\(query\[, k, ...\]\) | Async return docs selected using the maximal marginal relevance.   `amax_marginal_relevance_search_by_vector`\(...\) | Async return docs selected using the maximal marginal relevance.   `as_retriever`\(\*\*kwargs\) | Return VectorStoreRetriever initialized from this VectorStore.   `asearch`\(query, search\_type, \*\*kwargs\) | Async return docs most similar to query using a specified search type.   `asimilarity_search`\(query\[, k\]\) | Async return docs most similar to query.   `asimilarity_search_by_vector`\(embedding\[, k\]\) | Async return docs most similar to embedding vector.   `asimilarity_search_with_relevance_scores`\(query\) | Async return docs and relevance scores in the range \[0, 1\].   `asimilarity_search_with_score`\(\*args, \*\*kwargs\) | Async run similarity search with distance.   `delete`\(\[ids\]\) | Delete documents from the vectorstore.   `drop`\(\) | Drop the table and delete all data from the vectorstore.   `from_documents`\(documents, embedding, \*\*kwargs\) | Return VectorStore initialized from documents and embeddings.   `from_texts`\(texts, embedding\[, metadatas, ...\]\) | Create a SingleStoreDB vectorstore from raw documents. This is a user-friendly interface that: 1. Embeds documents. 2. Creates a new table for the embeddings in SingleStoreDB. 3. Adds the documents to the newly created table. This is intended to be a quick way to get started. :param texts: List of texts to add to the vectorstore. :type texts: List\[str\] :param embedding: A text embedding model. :type embedding: Embeddings :param metadatas: Optional list of metadatas. Defaults to None. :type metadatas: Optional\[List\[dict\]\], optional :param distance\_strategy: Determines the strategy employed for calculating the distance between vectors in the embedding space. Defaults to DOT\_PRODUCT. Available options are: - DOT\_PRODUCT: Computes the scalar product of two vectors. This is the default behavior - EUCLIDEAN\_DISTANCE: Computes the Euclidean distance between two vectors. This metric considers the geometric distance in the vector space, and might be more suitable for embeddings that rely on spatial relationships. This metric is not compatible with the WEIGHTED\_SUM search strategy. :type distance\_strategy: DistanceStrategy, optional :param table\_name: Specifies the name of the table in use. Defaults to "embeddings". :type table\_name: str, optional :param content\_field: Specifies the field to store the content. Defaults to "content". :type content\_field: str, optional :param metadata\_field: Specifies the field to store metadata. Defaults to "metadata". :type metadata\_field: str, optional :param vector\_field: Specifies the field to store the vector. Defaults to "vector". :type vector\_field: str, optional :param id\_field: Specifies the field to store the id. Defaults to "id". :type id\_field: str, optional :param use\_vector\_index: Toggles the use of a vector index. Works only with SingleStoreDB 8.5 or later. Defaults to False. If set to True, vector\_size parameter is required to be set to a proper value. :type use\_vector\_index: bool, optional :param vector\_index\_name: Specifies the name of the vector index. Defaults to empty. Will be ignored if use\_vector\_index is set to False. :type vector\_index\_name: str, optional :param vector\_index\_options: Specifies the options for the vector index. Defaults to \{\}. Will be ignored if use\_vector\_index is set to False. The options are: index\_type \(str, optional\): Specifies the type of the index. Defaults to IVF\_PQFS. For more options, please refer to the SingleStoreDB documentation: <https://docs.singlestore.com/cloud/reference/sql-reference/vector-functions/vector-indexing/> :type vector\_index\_options: dict, optional :param vector\_size: Specifies the size of the vector. Defaults to 1536. Required if use\_vector\_index is set to True. Should be set to the same value as the size of the vectors stored in the vector\_field. :type vector\_size: int, optional :param use\_full\_text\_search: Toggles the use a full-text index on the document content. Defaults to False. If set to True, the table will be created with a full-text index on the content field, and the simularity\_search method will all using TEXT\_ONLY, FILTER\_BY\_TEXT, FILTER\_BY\_VECTOR, and WIGHTED\_SUM search strategies. If set to False, the simularity\_search method will only allow VECTOR\_ONLY search strategy. :type use\_full\_text\_search: bool, optional :param pool\_size: Determines the number of active connections in the pool. Defaults to 5. :type pool\_size: int, optional :param max\_overflow: Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10. :type max\_overflow: int, optional :param timeout: Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30. :type timeout: float, optional :param Additional optional arguments provide further customization over the: :param database connection: :param pure\_python: Toggles the connector mode. If True, operates in pure Python mode. :type pure\_python: bool, optional :param local\_infile: Allows local file uploads. :type local\_infile: bool, optional :param charset: Specifies the character set for string values. :type charset: str, optional :param ssl\_key: Specifies the path of the file containing the SSL key. :type ssl\_key: str, optional :param ssl\_cert: Specifies the path of the file containing the SSL certificate. :type ssl\_cert: str, optional :param ssl\_ca: Specifies the path of the file containing the SSL certificate authority. :type ssl\_ca: str, optional :param ssl\_cipher: Sets the SSL cipher list. :type ssl\_cipher: str, optional :param ssl\_disabled: Disables SSL usage. :type ssl\_disabled: bool, optional :param ssl\_verify\_cert: Verifies the server's certificate. Automatically enabled if `ssl_ca` is specified. :type ssl\_verify\_cert: bool, optional :param ssl\_verify\_identity: Verifies the server's identity. :type ssl\_verify\_identity: bool, optional :param conv: A dictionary of data conversion functions. :type conv: dict\[int, Callable\], optional :param credential\_type: Specifies the type of authentication to use: auth.PASSWORD, auth.JWT, or auth.BROWSER\_SSO. :type credential\_type: str, optional :param autocommit: Enables autocommits. :type autocommit: bool, optional :param results\_type: Determines the structure of the query results: tuples, namedtuples, dicts. :type results\_type: str, optional :param results\_format: Deprecated. This option has been renamed to results\_type. :type results\_format: str, optional.   `get_by_ids`\(ids, /\) | Get documents by their IDs.   `max_marginal_relevance_search`\(query\[, k, ...\]\) | Return docs selected using the maximal marginal relevance.   `max_marginal_relevance_search_by_vector`\(...\) | Return docs selected using the maximal marginal relevance.   `search`\(query, search\_type, \*\*kwargs\) | Return docs most similar to query using a specified search type.   `similarity_search`\(query\[, k, filter, ...\]\) | Returns the most similar indexed documents to the query text.   `similarity_search_by_vector`\(embedding\[, k\]\) | Return docs most similar to embedding vector.   `similarity_search_with_relevance_scores`\(query\) | Return docs and relevance scores in the range \[0, 1\].   `similarity_search_with_score`\(query\[, k, ...\]\) | Return docs most similar to query.      \_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.DOT\_PRODUCT_,     _table\_name : str = 'embeddings'_,     _content\_field : str = 'content'_,     _metadata\_field : str = 'metadata'_,     _vector\_field : str = 'vector'_,     _id\_field : str = 'id'_,     _use\_vector\_index : bool = False_,     _vector\_index\_name : str = ''_,     _vector\_index\_options : dict | None = None_,     _vector\_size : int = 1536_,     _use\_full\_text\_search : bool = False_,     _pool\_size : int = 5_,     _max\_overflow : int = 10_,     _timeout : float = 30_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.__init__)\#     

Initialize with necessary components.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – A text embedding model.

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _,__optional_\) – 

Determines the strategy employed for calculating the distance between vectors in the embedding space. Defaults to DOT\_PRODUCT. Available options are: \- DOT\_PRODUCT: Computes the scalar product of two vectors.

> This is the default behavior

    * EUCLIDEAN\_DISTANCE: Computes the Euclidean distance between     

two vectors. This metric considers the geometric distance in the vector space, and might be more suitable for embeddings that rely on spatial relationships. This metric is not compatible with the WEIGHTED\_SUM search strategy.

  * **table\_name** \(_str_ _,__optional_\) – Specifies the name of the table in use. Defaults to “embeddings”.

  * **content\_field** \(_str_ _,__optional_\) – Specifies the field to store the content. Defaults to “content”.

  * **metadata\_field** \(_str_ _,__optional_\) – Specifies the field to store metadata. Defaults to “metadata”.

  * **vector\_field** \(_str_ _,__optional_\) – Specifies the field to store the vector. Defaults to “vector”.

  * **id\_field** \(_str_ _,__optional_\) – Specifies the field to store the id. Defaults to “id”.

  * **use\_vector\_index** \(_bool_ _,__optional_\) – Toggles the use of a vector index. Works only with SingleStoreDB 8.5 or later. Defaults to False. If set to True, vector\_size parameter is required to be set to a proper value.

  * **vector\_index\_name** \(_str_ _,__optional_\) – Specifies the name of the vector index. Defaults to empty. Will be ignored if use\_vector\_index is set to False.

  * **vector\_index\_options** \(_dict_ _,__optional_\) – 

Specifies the options for the vector index. Defaults to \{\}. Will be ignored if use\_vector\_index is set to False. The options are: index\_type \(str, optional\): Specifies the type of the index.

> Defaults to IVF\_PQFS.

For more options, please refer to the SingleStoreDB documentation: <https://docs.singlestore.com/cloud/reference/sql-reference/vector-functions/vector-indexing/>

  * **vector\_size** \(_int_ _,__optional_\) – Specifies the size of the vector. Defaults to 1536. Required if use\_vector\_index is set to True. Should be set to the same value as the size of the vectors stored in the vector\_field.

  * **use\_full\_text\_search** \(_bool_ _,__optional_\) – Toggles the use a full-text index on the document content. Defaults to False. If set to True, the table will be created with a full-text index on the content field, and the simularity\_search method will all using TEXT\_ONLY, FILTER\_BY\_TEXT, FILTER\_BY\_VECTOR, and WIGHTED\_SUM search strategies. If set to False, the simularity\_search method will only allow VECTOR\_ONLY search strategy.

  * **pool** \(_Following arguments pertain to the connection_\)

  * **pool\_size** \(_int_ _,__optional_\) – Determines the number of active connections in the pool. Defaults to 5.

  * **max\_overflow** \(_int_ _,__optional_\) – Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10.

  * **timeout** \(_float_ _,__optional_\) – Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30.

  * **connection** \(_database_\)

  * **host** \(_str_ _,__optional_\) – Specifies the hostname, IP address, or URL for the database connection. The default scheme is “mysql”.

  * **user** \(_str_ _,__optional_\) – Database username.

  * **password** \(_str_ _,__optional_\) – Database password.

  * **port** \(_int_ _,__optional_\) – Database port. Defaults to 3306 for non-HTTP connections, 80 for HTTP connections, and 443 for HTTPS connections.

  * **database** \(_str_ _,__optional_\) – Database name.

  * **the** \(_Additional optional arguments provide further customization over_\)

  * **connection**

  * **pure\_python** \(_bool_ _,__optional_\) – Toggles the connector mode. If True, operates in pure Python mode.

  * **local\_infile** \(_bool_ _,__optional_\) – Allows local file uploads.

  * **charset** \(_str_ _,__optional_\) – Specifies the character set for string values.

  * **ssl\_key** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL key.

  * **ssl\_cert** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate.

  * **ssl\_ca** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate authority.

  * **ssl\_cipher** \(_str_ _,__optional_\) – Sets the SSL cipher list.

  * **ssl\_disabled** \(_bool_ _,__optional_\) – Disables SSL usage.

  * **ssl\_verify\_cert** \(_bool_ _,__optional_\) – Verifies the server’s certificate. Automatically enabled if `ssl_ca` is specified.

  * **ssl\_verify\_identity** \(_bool_ _,__optional_\) – Verifies the server’s identity.

  * **conv** \(_dict_ _\[__int_ _,__Callable_ _\]__,__optional_\) – A dictionary of data conversion functions.

  * **credential\_type** \(_str_ _,__optional_\) – Specifies the type of authentication to use: auth.PASSWORD, auth.JWT, or auth.BROWSER\_SSO.

  * **autocommit** \(_bool_ _,__optional_\) – Enables autocommits.

  * **results\_type** \(_str_ _,__optional_\) – Determines the structure of the query results: tuples, namedtuples, dicts.

  * **results\_format** \(_str_ _,__optional_\) – Deprecated. This option has been renamed to results\_type.

  * **kwargs** \(_Any_\)

Examples

Basic Usage:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          vectorstore = SingleStoreDB(         OpenAIEmbeddings(),         host="https://user:password@127.0.0.1:3306/database"     )     

Advanced Usage:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          vectorstore = SingleStoreDB(         OpenAIEmbeddings(),         distance_strategy=DistanceStrategy.EUCLIDEAN_DISTANCE,         host="127.0.0.1",         port=3306,         user="user",         password="password",         database="db",         table_name="my_custom_table",         pool_size=10,         timeout=60,     )     

Using environment variables:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          os.environ['SINGLESTOREDB_URL'] = 'me:p455w0rd@s2-host.com/my_db'     vectorstore = SingleStoreDB(OpenAIEmbeddings())     

Using vector index:               from langchain_openai import OpenAIEmbeddings     from langchain_community.vectorstores import SingleStoreDB          os.environ['SINGLESTOREDB_URL'] = 'me:p455w0rd@s2-host.com/my_db'     vectorstore = SingleStoreDB(         OpenAIEmbeddings(),         use_vector_index=True,     )     

Using full-text index:

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

    _uris : List\[str\]_,     _metadatas : List\[dict\] | None = None_,     _embeddings : List\[List\[float\]\] | None = None_,     _return\_ids : bool = False_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.add_images)\#     

Run images through the embeddings and add to the vectorstore.

Parameters:     

  * **List****\[****str****\]** \(_uris_\) – File path to images. Each URI will be added to the vectorstore as document content.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – Optional list of metadatas. Defaults to None.

  * **embeddings** \(_Optional_ _\[__List_ _\[__List_ _\[__float_ _\]__\]__\]__,__optional_\) – Optional pre-generated embeddings. Defaults to None.

  * **uris** \(_List_ _\[__str_ _\]_\)

  * **return\_ids** \(_bool_\)

  * **kwargs** \(_Any_\)

Returns:     

list of document ids added to the vectorstore     

if return\_ids is True. Otherwise, an empty list.

Return type:     

List\[str\]

add\_texts\(

    _texts : Iterable\[str\]_,     _metadatas : List\[dict\] | None = None_,     _embeddings : List\[List\[float\]\] | None = None_,     _return\_ids : bool = False_,     _\*\* kwargs: Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.add_texts)\#     

Add more texts to the vectorstore.

Parameters:     

  * **texts** \(_Iterable_ _\[__str_ _\]_\) – Iterable of strings/text to add to the vectorstore.

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\) – Optional list of metadatas. Defaults to None.

  * **embeddings** \(_Optional_ _\[__List_ _\[__List_ _\[__float_ _\]__\]__\]__,__optional_\) – Optional pre-generated embeddings. Defaults to None.

  * **return\_ids** \(_bool_\)

  * **kwargs** \(_Any_\)

Returns:     

list of document ids added to the vectorstore     

if return\_ids is True. Otherwise, an empty list.

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

delete\(

    _ids : List\[str\] | None = None_,     _\*\* kwargs: Any_, \) → bool | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.delete)\#     

Delete documents from the vectorstore.

Parameters:     

  * **ids** \(_List_ _\[__str_ _\]__,__optional_\) – List of document ids to delete. If None, all documents will be deleted. Defaults to None.

  * **kwargs** \(_Any_\)

Returns:     

True if deletion was successful, False otherwise.

Return type:     

bool

drop\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.drop)\#     

Drop the table and delete all data from the vectorstore. Vector store will be unusable after this operation.

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

    _texts : List\[str\]_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metadatas : List\[dict\] | None = None_,     _distance\_strategy : [DistanceStrategy](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.utils.DistanceStrategy.html#langchain_community.vectorstores.utils.DistanceStrategy "langchain_community.vectorstores.utils.DistanceStrategy") = DistanceStrategy.DOT\_PRODUCT_,     _table\_name : str = 'embeddings'_,     _content\_field : str = 'content'_,     _metadata\_field : str = 'metadata'_,     _vector\_field : str = 'vector'_,     _id\_field : str = 'id'_,     _use\_vector\_index : bool = False_,     _vector\_index\_name : str = ''_,     _vector\_index\_options : dict | None = None_,     _vector\_size : int = 1536_,     _use\_full\_text\_search : bool = False_,     _pool\_size : int = 5_,     _max\_overflow : int = 10_,     _timeout : float = 30_,     _\*\* kwargs: Any_, \) → SingleStoreDB[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.from_texts)\#     

Create a SingleStoreDB vectorstore from raw documents. This is a user-friendly interface that:

>   1. Embeds documents. >  >   2. Creates a new table for the embeddings in SingleStoreDB. >  >   3. Adds the documents to the newly created table. >  > 

This is intended to be a quick way to get started. :param texts: List of texts to add to the vectorstore. :type texts: List\[str\] :param embedding: A text embedding model. :type embedding: Embeddings :param metadatas: Optional list of metadatas.

> Defaults to None.

Parameters:     

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _,__optional_\) – 

Determines the strategy employed for calculating the distance between vectors in the embedding space. Defaults to DOT\_PRODUCT. Available options are: \- DOT\_PRODUCT: Computes the scalar product of two vectors.

> This is the default behavior

    * EUCLIDEAN\_DISTANCE: Computes the Euclidean distance between     

two vectors. This metric considers the geometric distance in the vector space, and might be more suitable for embeddings that rely on spatial relationships. This metric is not compatible with the WEIGHTED\_SUM search strategy.

  * **table\_name** \(_str_ _,__optional_\) – Specifies the name of the table in use. Defaults to “embeddings”.

  * **content\_field** \(_str_ _,__optional_\) – Specifies the field to store the content. Defaults to “content”.

  * **metadata\_field** \(_str_ _,__optional_\) – Specifies the field to store metadata. Defaults to “metadata”.

  * **vector\_field** \(_str_ _,__optional_\) – Specifies the field to store the vector. Defaults to “vector”.

  * **id\_field** \(_str_ _,__optional_\) – Specifies the field to store the id. Defaults to “id”.

  * **use\_vector\_index** \(_bool_ _,__optional_\) – Toggles the use of a vector index. Works only with SingleStoreDB 8.5 or later. Defaults to False. If set to True, vector\_size parameter is required to be set to a proper value.

  * **vector\_index\_name** \(_str_ _,__optional_\) – Specifies the name of the vector index. Defaults to empty. Will be ignored if use\_vector\_index is set to False.

  * **vector\_index\_options** \(_dict_ _,__optional_\) – 

Specifies the options for the vector index. Defaults to \{\}. Will be ignored if use\_vector\_index is set to False. The options are: index\_type \(str, optional\): Specifies the type of the index.

> Defaults to IVF\_PQFS.

For more options, please refer to the SingleStoreDB documentation: <https://docs.singlestore.com/cloud/reference/sql-reference/vector-functions/vector-indexing/>

  * **vector\_size** \(_int_ _,__optional_\) – Specifies the size of the vector. Defaults to 1536. Required if use\_vector\_index is set to True. Should be set to the same value as the size of the vectors stored in the vector\_field.

  * **use\_full\_text\_search** \(_bool_ _,__optional_\) – Toggles the use a full-text index on the document content. Defaults to False. If set to True, the table will be created with a full-text index on the content field, and the simularity\_search method will all using TEXT\_ONLY, FILTER\_BY\_TEXT, FILTER\_BY\_VECTOR, and WIGHTED\_SUM search strategies. If set to False, the simularity\_search method will only allow VECTOR\_ONLY search strategy.

  * **pool\_size** \(_int_ _,__optional_\) – Determines the number of active connections in the pool. Defaults to 5.

  * **max\_overflow** \(_int_ _,__optional_\) – Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10.

  * **timeout** \(_float_ _,__optional_\) – Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30.

  * **the** \(_Additional optional arguments provide further customization over_\)

  * **connection** \(_database_\)

  * **pure\_python** \(_bool_ _,__optional_\) – Toggles the connector mode. If True, operates in pure Python mode.

  * **local\_infile** \(_bool_ _,__optional_\) – Allows local file uploads.

  * **charset** \(_str_ _,__optional_\) – Specifies the character set for string values.

  * **ssl\_key** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL key.

  * **ssl\_cert** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate.

  * **ssl\_ca** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate authority.

  * **ssl\_cipher** \(_str_ _,__optional_\) – Sets the SSL cipher list.

  * **ssl\_disabled** \(_bool_ _,__optional_\) – Disables SSL usage.

  * **ssl\_verify\_cert** \(_bool_ _,__optional_\) – Verifies the server’s certificate. Automatically enabled if `ssl_ca` is specified.

  * **ssl\_verify\_identity** \(_bool_ _,__optional_\) – Verifies the server’s identity.

  * **conv** \(_dict_ _\[__int_ _,__Callable_ _\]__,__optional_\) – A dictionary of data conversion functions.

  * **credential\_type** \(_str_ _,__optional_\) – Specifies the type of authentication to use: auth.PASSWORD, auth.JWT, or auth.BROWSER\_SSO.

  * **autocommit** \(_bool_ _,__optional_\) – Enables autocommits.

  * **results\_type** \(_str_ _,__optional_\) – Determines the structure of the query results: tuples, namedtuples, dicts.

  * **results\_format** \(_str_ _,__optional_\) – Deprecated. This option has been renamed to results\_type.

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **metadatas** \(_Optional_ _\[__List_ _\[__dict_ _\]__\]__,__optional_\)

  * **kwargs** \(_Any_\)

Return type:     

_SingleStoreDB_

Example               from langchain_community.vectorstores import SingleStoreDB     from langchain_openai import OpenAIEmbeddings          s2 = SingleStoreDB.from_texts(         texts,         OpenAIEmbeddings(),         host="username:password@localhost:3306/database"     )     

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

max\_marginal\_relevance\_search\(

    _query : str_,     _k : int = 4_,     _fetch\_k : int = 20_,     _lambda\_mult : float = 0.5_,     _\*\* kwargs: Any_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Return docs selected using the maximal marginal relevance.

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

similarity\_search\(

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _search\_strategy : SearchStrategy = SearchStrategy.VECTOR\_ONLY_,     _filter\_threshold : float = 0_,     _text\_weight : float = 0.5_,     _vector\_weight : float = 0.5_,     _vector\_select\_count\_multiplier : int = 10_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.similarity_search)\#     

Returns the most similar indexed documents to the query text.

Uses cosine similarity.

Parameters:     

  * **query** \(_str_\) – The query text for which to find similar documents.

  * **k** \(_int_\) – The number of documents to return. Default is 4.

  * **filter** \(_dict_\) – A dictionary of metadata fields and values to filter by. Default is None.

  * **search\_strategy** \(_SearchStrategy_\) – 

The search strategy to use. Default is SearchStrategy.VECTOR\_ONLY. Available options are: \- SearchStrategy.VECTOR\_ONLY: Searches only by vector similarity. \- SearchStrategy.TEXT\_ONLY: Searches only by text similarity. This

> option is only available if use\_full\_text\_search is True.

    * SearchStrategy.FILTER\_BY\_TEXT: Filters by text similarity and     

searches by vector similarity. This option is only available if use\_full\_text\_search is True.

    * SearchStrategy.FILTER\_BY\_VECTOR: Filters by vector similarity and     

searches by text similarity. This option is only available if use\_full\_text\_search is True.

    * SearchStrategy.WEIGHTED\_SUM: Searches by a weighted sum of text and     

vector similarity. This option is only available if use\_full\_text\_search is True and distance\_strategy is DOT\_PRODUCT.

  * **filter\_threshold** \(_float_\) – The threshold for filtering by text or vector similarity. Default is 0. This option has effect only if search\_strategy is SearchStrategy.FILTER\_BY\_TEXT or SearchStrategy.FILTER\_BY\_VECTOR.

  * **text\_weight** \(_float_\) – The weight of text similarity in the weighted sum search strategy. Default is 0.5. This option has effect only if search\_strategy is SearchStrategy.WEIGHTED\_SUM.

  * **vector\_weight** \(_float_\) – The weight of vector similarity in the weighted sum search strategy. Default is 0.5. This option has effect only if search\_strategy is SearchStrategy.WEIGHTED\_SUM.

  * **vector\_select\_count\_multiplier** \(_int_\) – The multiplier for the number of vectors to select when using the vector index. Default is 10. This parameter has effect only if use\_vector\_index is True and search\_strategy is SearchStrategy.WEIGHTED\_SUM or SearchStrategy.FILTER\_BY\_TEXT. The number of vectors selected will be k \* vector\_select\_count\_multiplier. This is needed due to the limitations of the vector index.

  * **kwargs** \(_Any_\)

Returns:     

A list of documents that are most similar to the query text.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples

Basic Usage: .. code-block:: python

> from langchain\_community.vectorstores import SingleStoreDB from langchain\_openai import OpenAIEmbeddings >  > s2 = SingleStoreDB.from\_documents\( >      >  > docs, OpenAIEmbeddings\(\), host=”username:password@localhost:3306/database” >  > \) results = s2.similarity\_search\(“query text”, 1, >
>> \{“metadata\_field”: “metadata\_value”\}\)

Different Search Strategies: .. code-block:: python

> from langchain\_community.vectorstores import SingleStoreDB from langchain\_openai import OpenAIEmbeddings >  > s2 = SingleStoreDB.from\_documents\( >      >  > docs, OpenAIEmbeddings\(\), host=”username:password@localhost:3306/database”, use\_full\_text\_search=True, use\_vector\_index=True, >  > \) results = s2.similarity\_search\(“query text”, 1, >
>> search\_strategy=SingleStoreDB.SearchStrategy.FILTER\_BY\_TEXT, filter\_threshold=0.5\)

Weighted Sum Search Strategy: .. code-block:: python

> from langchain\_community.vectorstores import SingleStoreDB from langchain\_openai import OpenAIEmbeddings >  > s2 = SingleStoreDB.from\_documents\( >      >  > docs, OpenAIEmbeddings\(\), host=”username:password@localhost:3306/database”, use\_full\_text\_search=True, use\_vector\_index=True, >  > \) results = s2.similarity\_search\(“query text”, 1, >
>> search\_strategy=SingleStoreDB.SearchStrategy.WEIGHTED\_SUM, text\_weight=0.3, vector\_weight=0.7\)

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

    _query : str_,     _k : int = 4_,     _filter : dict | None = None_,     _search\_strategy : SearchStrategy = SearchStrategy.VECTOR\_ONLY_,     _filter\_threshold : float = 1_,     _text\_weight : float = 0.5_,     _vector\_weight : float = 0.5_,     _vector\_select\_count\_multiplier : int = 10_,     _\*\* kwargs: Any_, \) → List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/singlestoredb.html#SingleStoreDB.similarity_search_with_score)\#     

Return docs most similar to query. Uses cosine similarity.

Parameters:     

  * **query** \(_str_\) – Text to look up documents similar to.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

  * **filter** \(_Optional_ _\[__dict_ _\]_\) – A dictionary of metadata fields and values to filter by. Defaults to None.

  * **search\_strategy** \(_SearchStrategy_\) – 

The search strategy to use. Default is SearchStrategy.VECTOR\_ONLY. Available options are: \- SearchStrategy.VECTOR\_ONLY: Searches only by vector similarity. \- SearchStrategy.TEXT\_ONLY: Searches only by text similarity. This

> option is only available if use\_full\_text\_search is True.

    * SearchStrategy.FILTER\_BY\_TEXT: Filters by text similarity and     

searches by vector similarity. This option is only available if use\_full\_text\_search is True.

    * SearchStrategy.FILTER\_BY\_VECTOR: Filters by vector similarity and     

searches by text similarity. This option is only available if use\_full\_text\_search is True.

    * SearchStrategy.WEIGHTED\_SUM: Searches by a weighted sum of text and     

vector similarity. This option is only available if use\_full\_text\_search is True and distance\_strategy is DOT\_PRODUCT.

  * **filter\_threshold** \(_float_\) – The threshold for filtering by text or vector similarity. Default is 0. This option has effect only if search\_strategy is SearchStrategy.FILTER\_BY\_TEXT or SearchStrategy.FILTER\_BY\_VECTOR.

  * **text\_weight** \(_float_\) – The weight of text similarity in the weighted sum search strategy. Default is 0.5. This option has effect only if search\_strategy is SearchStrategy.WEIGHTED\_SUM.

  * **vector\_weight** \(_float_\) – The weight of vector similarity in the weighted sum search strategy. Default is 0.5. This option has effect only if search\_strategy is SearchStrategy.WEIGHTED\_SUM.

  * **vector\_select\_count\_multiplier** \(_int_\) – The multiplier for the number of vectors to select when using the vector index. Default is 10. This parameter has effect only if use\_vector\_index is True and search\_strategy is SearchStrategy.WEIGHTED\_SUM or SearchStrategy.FILTER\_BY\_TEXT. The number of vectors selected will be k \* vector\_select\_count\_multiplier. This is needed due to the limitations of the vector index.

  * **kwargs** \(_Any_\)

Returns:     

List of Documents most similar to the query and score for each document.

Raises:     

**ValueError** – If the search strategy is not supported with the distance strategy.

Return type:     

List\[Tuple\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), float\]\]

Examples

Basic Usage: .. code-block:: python

> from langchain\_community.vectorstores import SingleStoreDB from langchain\_openai import OpenAIEmbeddings >  > s2 = SingleStoreDB.from\_documents\( >      >  > docs, OpenAIEmbeddings\(\), host=”username:password@localhost:3306/database” >  > \) results = s2.similarity\_search\_with\_score\(“query text”, 1, >
>> \{“metadata\_field”: “metadata\_value”\}\)

Different Search Strategies:               from langchain_community.vectorstores import SingleStoreDB     from langchain_openai import OpenAIEmbeddings          s2 = SingleStoreDB.from_documents(         docs,         OpenAIEmbeddings(),         host="username:password@localhost:3306/database",         use_full_text_search=True,         use_vector_index=True,     )     results = s2.similarity_search_with_score("query text", 1,             search_strategy=SingleStoreDB.SearchStrategy.FILTER_BY_VECTOR,             filter_threshold=0.5)     

Weighted Sum Search Strategy: .. code-block:: python

> from langchain\_community.vectorstores import SingleStoreDB from langchain\_openai import OpenAIEmbeddings >  > s2 = SingleStoreDB.from\_documents\( >      >  > docs, OpenAIEmbeddings\(\), host=”username:password@localhost:3306/database”, use\_full\_text\_search=True, use\_vector\_index=True, >  > \) results = s2.similarity\_search\_with\_score\(“query text”, 1, >
>> search\_strategy=SingleStoreDB.SearchStrategy.WEIGHTED\_SUM, text\_weight=0.3, vector\_weight=0.7\)

Examples using SingleStoreDB

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/vectorstores/singlestoredb/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)