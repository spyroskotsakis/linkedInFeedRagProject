# SingleStoreDBSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.SingleStoreDBSemanticCache.html
**Word Count:** 1374
**Links Count:** 162
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# SingleStoreDBSemanticCache\#

_class _langchain\_community.cache.SingleStoreDBSemanticCache\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _cache\_table\_prefix : str = 'cache\_'_,     _search\_threshold : float = 0.2_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SingleStoreDBSemanticCache)\#     

Deprecated since version 0.3.22: This class is pending deprecation and may be removed in a future version. You can swap to using the SingleStoreSemanticCache implementation in langchain\_singlestore. See <[singlestore-labs/langchain-singlestore](https://github.com/singlestore-labs/langchain-singlestore)> for details about the new implementation. Use `from langchain_singlestore import SingleStoreSemanticCache` instead.

Cache that uses SingleStore DB as a backend

Initialize with necessary components.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – A text embedding model.

  * **cache\_table\_prefix** \(_str_ _,__optional_\) – Prefix for the cache table name. Defaults to “cache\_”.

  * **search\_threshold** \(_float_ _,__optional_\) – The minimum similarity score for a search result to be considered a match. Defaults to 0.2.

  * **store** \(_Following arguments pertrain to the SingleStoreDB vector_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _,__optional_\) – 

Determines the strategy employed for calculating the distance between vectors in the embedding space. Defaults to DOT\_PRODUCT. Available options are: \- DOT\_PRODUCT: Computes the scalar product of two vectors.

> This is the default behavior

    * EUCLIDEAN\_DISTANCE: Computes the Euclidean distance between     

two vectors. This metric considers the geometric distance in the vector space, and might be more suitable for embeddings that rely on spatial relationships. This metric is not compatible with the WEIGHTED\_SUM search strategy.

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

Basic Usage:               import langchain     from langchain.cache import SingleStoreDBSemanticCache     from langchain.embeddings import OpenAIEmbeddings          langchain.llm_cache = SingleStoreDBSemanticCache(         embedding=OpenAIEmbeddings(),         host="https://user:password@127.0.0.1:3306/database"     )     

Advanced Usage:               import langchain     from langchain.cache import SingleStoreDBSemanticCache     from langchain.embeddings import OpenAIEmbeddings          langchain.llm_cache = = SingleStoreDBSemanticCache(         embeddings=OpenAIEmbeddings(),         use_vector_index=True,         host="127.0.0.1",         port=3306,         user="user",         password="password",         database="db",         table_name="my_custom_table",         pool_size=10,         timeout=60,     )     

Methods

`__init__`\(embedding, \*\[, cache\_table\_prefix, ...\]\) | Initialize with necessary components.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear semantic cache for a given llm\_string.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _cache\_table\_prefix : str = 'cache\_'_,     _search\_threshold : float = 0.2_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SingleStoreDBSemanticCache.__init__)\#     

Initialize with necessary components.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – A text embedding model.

  * **cache\_table\_prefix** \(_str_ _,__optional_\) – Prefix for the cache table name. Defaults to “cache\_”.

  * **search\_threshold** \(_float_ _,__optional_\) – The minimum similarity score for a search result to be considered a match. Defaults to 0.2.

  * **store** \(_Following arguments pertrain to the SingleStoreDB vector_\)

  * **distance\_strategy** \([_DistanceStrategy_](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy") _,__optional_\) – 

Determines the strategy employed for calculating the distance between vectors in the embedding space. Defaults to DOT\_PRODUCT. Available options are: \- DOT\_PRODUCT: Computes the scalar product of two vectors.

> This is the default behavior

    * EUCLIDEAN\_DISTANCE: Computes the Euclidean distance between     

two vectors. This metric considers the geometric distance in the vector space, and might be more suitable for embeddings that rely on spatial relationships. This metric is not compatible with the WEIGHTED\_SUM search strategy.

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

Basic Usage:               import langchain     from langchain.cache import SingleStoreDBSemanticCache     from langchain.embeddings import OpenAIEmbeddings          langchain.llm_cache = SingleStoreDBSemanticCache(         embedding=OpenAIEmbeddings(),         host="https://user:password@127.0.0.1:3306/database"     )     

Advanced Usage:               import langchain     from langchain.cache import SingleStoreDBSemanticCache     from langchain.embeddings import OpenAIEmbeddings          langchain.llm_cache = = SingleStoreDBSemanticCache(         embeddings=OpenAIEmbeddings(),         use_vector_index=True,         host="127.0.0.1",         port=3306,         user="user",         password="password",         database="db",         table_name="my_custom_table",         pool_size=10,         timeout=60,     )     

_async _aclear\(

    _\*\* kwargs: Any_, \) → None\#     

Async clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None\#     

Async look up based on prompt and llm\_string.

A cache implementation is expected to generate a key from the 2-tuple of prompt and llm\_string \(e.g., by concatenating them with a delimiter\).

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

Returns:     

On a cache miss, return None. On a cache hit, return the cached value. The cached value is a list of Generations \(or subclasses\).

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

_async _aupdate\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SingleStoreDBSemanticCache.clear)\#     

Clear semantic cache for a given llm\_string.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SingleStoreDBSemanticCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SingleStoreDBSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

Examples using SingleStoreDBSemanticCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)