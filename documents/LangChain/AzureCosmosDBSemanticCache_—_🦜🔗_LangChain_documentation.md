# AzureCosmosDBSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.AzureCosmosDBSemanticCache.html
**Word Count:** 870
**Links Count:** 163
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# AzureCosmosDBSemanticCache\#

_class _langchain\_community.cache.AzureCosmosDBSemanticCache\(

    _cosmosdb\_connection\_string : str_,     _database\_name : str_,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _cosmosdb\_client : Any | None = None_,     _num\_lists : int = 100_,     _similarity : [CosmosDBSimilarityType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType.html#langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType "langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType") = CosmosDBSimilarityType.COS_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType.html#langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType "langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _dimensions : int = 1536_,     _m : int = 16_,     _ef\_construction : int = 64_,     _ef\_search : int = 40_,     _score\_threshold : float | None = None_,     _application\_name : str = 'LangChain-CDBMongoVCore-SemanticCache-Python'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBSemanticCache)\#     

Cache that uses Cosmos DB Mongo vCore vector-store backend

Parameters:     

  * **cosmosdb\_connection\_string** \(_str_\) – Cosmos DB Mongo vCore connection string

  * **cosmosdb\_client** \(_Optional_ _\[__Any_ _\]_\) – Cosmos DB Mongo vCore client

  * **embedding** \(_Embedding_\) – Embedding provider for semantic encoding and search.

  * **database\_name** \(_str_\) – Database name for the CosmosDBMongoVCoreSemanticCache

  * **collection\_name** \(_str_\) – Collection name for the CosmosDBMongoVCoreSemanticCache

  * **num\_lists** \(_int_\) – This integer is the number of clusters that the inverted file \(IVF\) index uses to group the vector data. We recommend that numLists is set to documentCount/1000 for up to 1 million documents and to sqrt\(documentCount\) for more than 1 million documents. Using a numLists value of 1 is akin to performing brute-force search, which has limited performance

  * **dimensions** \(_int_\) – Number of dimensions for vector similarity. The maximum number of supported dimensions is 2000

  * **similarity** \([_CosmosDBSimilarityType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType")\) – 

Similarity metric to use with the IVF index.

Possible options are:          * CosmosDBSimilarityType.COS \(cosine distance\),

    * CosmosDBSimilarityType.L2 \(Euclidean distance\), and

    * CosmosDBSimilarityType.IP \(inner product\).

  * **kind** \([_CosmosDBVectorSearchType_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType")\) – 

Type of vector index to create. Possible options are:

>     * vector-ivf >  >     * vector-hnsw: available as a preview feature only, >      >  > to enable visit <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/preview-features>

  * **m** \(_int_\) – The max number of connections per layer \(16 by default, minimum value is 2, maximum value is 100\). Higher m is suitable for datasets with high dimensionality and/or high accuracy requirements.

  * **ef\_construction** \(_int_\) – the size of the dynamic candidate list for constructing the graph \(64 by default, minimum value is 4, maximum value is 1000\). Higher ef\_construction will result in better index quality and higher accuracy, but it will also increase the time required to build the index. ef\_construction has to be at least 2 \* m

  * **ef\_search** \(_int_\) – The size of the dynamic candidate list for search \(40 by default\). A higher value provides better recall at the cost of speed.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Maximum score used to filter the vector search documents.

  * **application\_name** \(_str_\) – Application name for the client for tracking and logging

Attributes

`DEFAULT_COLLECTION_NAME` |    ---|---   `DEFAULT_DATABASE_NAME` |       Methods

`__init__`\(cosmosdb\_connection\_string, ...\[, ...\]\) |    ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear semantic cache for a given llm\_string.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _cosmosdb\_connection\_string : str_,     _database\_name : str_,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _cosmosdb\_client : Any | None = None_,     _num\_lists : int = 100_,     _similarity : [CosmosDBSimilarityType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType.html#langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType "langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType") = CosmosDBSimilarityType.COS_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType.html#langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType "langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _dimensions : int = 1536_,     _m : int = 16_,     _ef\_construction : int = 64_,     _ef\_search : int = 40_,     _score\_threshold : float | None = None_,     _application\_name : str = 'LangChain-CDBMongoVCore-SemanticCache-Python'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBSemanticCache.__init__)\#     

Parameters:     

  * **cosmosdb\_connection\_string** \(_str_\) – Cosmos DB Mongo vCore connection string

  * **cosmosdb\_client** \(_Any_ _|__None_\) – Cosmos DB Mongo vCore client

  * **embedding** \(_Embedding_\) – Embedding provider for semantic encoding and search.

  * **database\_name** \(_str_\) – Database name for the CosmosDBMongoVCoreSemanticCache

  * **collection\_name** \(_str_\) – Collection name for the CosmosDBMongoVCoreSemanticCache

  * **num\_lists** \(_int_\) – This integer is the number of clusters that the inverted file \(IVF\) index uses to group the vector data. We recommend that numLists is set to documentCount/1000 for up to 1 million documents and to sqrt\(documentCount\) for more than 1 million documents. Using a numLists value of 1 is akin to performing brute-force search, which has limited performance

  * **dimensions** \(_int_\) – Number of dimensions for vector similarity. The maximum number of supported dimensions is 2000

  * **similarity** \([_CosmosDBSimilarityType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType.html#langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType "langchain_community.vectorstores.azure_cosmos_db.CosmosDBSimilarityType")\) – 

Similarity metric to use with the IVF index.

Possible options are:          * CosmosDBSimilarityType.COS \(cosine distance\),

    * CosmosDBSimilarityType.L2 \(Euclidean distance\), and

    * CosmosDBSimilarityType.IP \(inner product\).

  * **kind** \([_CosmosDBVectorSearchType_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType.html#langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType "langchain_community.vectorstores.azure_cosmos_db.CosmosDBVectorSearchType")\) – 

Type of vector index to create. Possible options are:

>     * vector-ivf >  >     * vector-hnsw: available as a preview feature only, >      >  > to enable visit <https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/preview-features>

  * **m** \(_int_\) – The max number of connections per layer \(16 by default, minimum value is 2, maximum value is 100\). Higher m is suitable for datasets with high dimensionality and/or high accuracy requirements.

  * **ef\_construction** \(_int_\) – the size of the dynamic candidate list for constructing the graph \(64 by default, minimum value is 4, maximum value is 1000\). Higher ef\_construction will result in better index quality and higher accuracy, but it will also increase the time required to build the index. ef\_construction has to be at least 2 \* m

  * **ef\_search** \(_int_\) – The size of the dynamic candidate list for search \(40 by default\). A higher value provides better recall at the cost of speed.

  * **score\_threshold** \(_float_ _|__None_\) – Maximum score used to filter the vector search documents.

  * **application\_name** \(_str_\) – Application name for the client for tracking and logging

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

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBSemanticCache.clear)\#     

Clear semantic cache for a given llm\_string.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBSemanticCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

Examples using AzureCosmosDBSemanticCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)