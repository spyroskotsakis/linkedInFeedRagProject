# AzureCosmosDBMongoVCoreSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.cache.AzureCosmosDBMongoVCoreSemanticCache.html
**Word Count:** 1148
**Links Count:** 134
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# AzureCosmosDBMongoVCoreSemanticCache\#

_class _langchain\_azure\_ai.vectorstores.cache.AzureCosmosDBMongoVCoreSemanticCache\(

    _cosmosdb\_connection\_string : str_,     _database\_name : str_,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _cosmosdb\_client : Any | None = None_,     _num\_lists : int = 100_,     _similarity : [CosmosDBSimilarityType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType") = CosmosDBSimilarityType.COS_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _dimensions : int = 1536_,     _m : int = 16_,     _ef\_construction : int = 64_,     _max\_degree : int = 32_,     _l\_build : int = 50_,     _l\_search : int = 40_,     _ef\_search : int = 40_,     _application\_name : str = 'langchainpy'_,     _score\_threshold : float | None = None_,     _compression : [CosmosDBVectorSearchCompression](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression") | None = None_,     _pq\_compressed\_dims : int | None = None_,     _pq\_sample\_size : int | None = None_,     _oversampling : float | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBMongoVCoreSemanticCache)\#     

Cache that uses Cosmos DB Mongo vCore vector-store backend.

AzureCosmosDBMongoVCoreSemanticCache constructor.

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

>     * vector-ivf >  >     * vector-hnsw >  >     * vector-diskann

  * **m** \(_int_\) – The max number of connections per layer \(16 by default, minimum value is 2, maximum value is 100\). Higher m is suitable for datasets with high dimensionality and/or high accuracy requirements.

  * **ef\_construction** \(_int_\) – the size of the dynamic candidate list for constructing the graph \(64 by default, minimum value is 4, maximum value is 1000\). Higher ef\_construction will result in better index quality and higher accuracy, but it will also increase the time required to build the index. ef\_construction has to be at least 2 \* m

  * **ef\_search** \(_int_\) – The size of the dynamic candidate list for search \(40 by default\). A higher value provides better recall at the cost of speed.

  * **max\_degree** \(_int_\) – Max number of neighbors. Default value is 32, range from 20 to 2048. Only vector-diskann search supports this for now.

  * **l\_build** \(_int_\) – l value for index building. Default value is 50, range from 10 to 500. Only vector-diskann search supports this for now.

  * **l\_search** \(_int_\) – l value for index searching. Default value is 40, range from 10 to 10000. Only vector-diskann search supports this.

  * **score\_threshold** \(_Optional_ _\[__float_ _\]_\) – Maximum score used to filter the vector search documents.

  * **application\_name** \(_str_\) – Application name for the client for tracking and logging

  * **compression** \(_Optional_ _\[_[_CosmosDBVectorSearchCompression_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression") _\]_\) – compression type for vector indexes.

  * **pq\_compressed\_dims** \(_Optional_ _\[__int_ _\]_\) – Number of dimensions after compression for product quantization. Must be less than original dimensions. Automatically calculated if omitted. Range: 1-8000.

  * **pq\_sample\_size** \(_Optional_ _\[__int_ _\]_\) – Number of samples for PQ centroid training. Higher value means better quality but longer build time. Default: 1000. Range: 1000-100000.

  * **oversampling** \(_Optional_ _\[__float_ _\]_\) – The oversampling factor for compressed index. The oversampling factor \(a float with a minimum of 1\) specifies how many more candidate vectors to retrieve from the compressed index than k \(the number of desired results\).

Attributes

`DEFAULT_COLLECTION_NAME` |    ---|---   `DEFAULT_DATABASE_NAME` |       Methods

`__init__`\(cosmosdb\_connection\_string, ...\[, ...\]\) | AzureCosmosDBMongoVCoreSemanticCache constructor.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear semantic cache for a given llm\_string.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _cosmosdb\_connection\_string : str_,     _database\_name : str_,     _collection\_name : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _\*_ ,     _cosmosdb\_client : Any | None = None_,     _num\_lists : int = 100_,     _similarity : [CosmosDBSimilarityType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBSimilarityType") = CosmosDBSimilarityType.COS_,     _kind : [CosmosDBVectorSearchType](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchType") = CosmosDBVectorSearchType.VECTOR\_IVF_,     _dimensions : int = 1536_,     _m : int = 16_,     _ef\_construction : int = 64_,     _max\_degree : int = 32_,     _l\_build : int = 50_,     _l\_search : int = 40_,     _ef\_search : int = 40_,     _application\_name : str = 'langchainpy'_,     _score\_threshold : float | None = None_,     _compression : [CosmosDBVectorSearchCompression](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression") | None = None_,     _pq\_compressed\_dims : int | None = None_,     _pq\_sample\_size : int | None = None_,     _oversampling : float | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBMongoVCoreSemanticCache.__init__)\#     

AzureCosmosDBMongoVCoreSemanticCache constructor.

Parameters:     

  * **cosmosdb\_connection\_string** \(_str_\) – Cosmos DB Mongo vCore connection string

  * **cosmosdb\_client** \(_Any_ _|__None_\) – Cosmos DB Mongo vCore client

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

>     * vector-ivf >  >     * vector-hnsw >  >     * vector-diskann

  * **m** \(_int_\) – The max number of connections per layer \(16 by default, minimum value is 2, maximum value is 100\). Higher m is suitable for datasets with high dimensionality and/or high accuracy requirements.

  * **ef\_construction** \(_int_\) – the size of the dynamic candidate list for constructing the graph \(64 by default, minimum value is 4, maximum value is 1000\). Higher ef\_construction will result in better index quality and higher accuracy, but it will also increase the time required to build the index. ef\_construction has to be at least 2 \* m

  * **ef\_search** \(_int_\) – The size of the dynamic candidate list for search \(40 by default\). A higher value provides better recall at the cost of speed.

  * **max\_degree** \(_int_\) – Max number of neighbors. Default value is 32, range from 20 to 2048. Only vector-diskann search supports this for now.

  * **l\_build** \(_int_\) – l value for index building. Default value is 50, range from 10 to 500. Only vector-diskann search supports this for now.

  * **l\_search** \(_int_\) – l value for index searching. Default value is 40, range from 10 to 10000. Only vector-diskann search supports this.

  * **score\_threshold** \(_float_ _|__None_\) – Maximum score used to filter the vector search documents.

  * **application\_name** \(_str_\) – Application name for the client for tracking and logging

  * **compression** \([_CosmosDBVectorSearchCompression_](https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression.html#langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression "langchain_azure_ai.vectorstores.azure_cosmos_db_mongo_vcore.CosmosDBVectorSearchCompression") _|__None_\) – compression type for vector indexes.

  * **pq\_compressed\_dims** \(_int_ _|__None_\) – Number of dimensions after compression for product quantization. Must be less than original dimensions. Automatically calculated if omitted. Range: 1-8000.

  * **pq\_sample\_size** \(_int_ _|__None_\) – Number of samples for PQ centroid training. Higher value means better quality but longer build time. Default: 1000. Range: 1000-100000.

  * **oversampling** \(_float_ _|__None_\) – The oversampling factor for compressed index. The oversampling factor \(a float with a minimum of 1\) specifies how many more candidate vectors to retrieve from the compressed index than k \(the number of desired results\).

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

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBMongoVCoreSemanticCache.clear)\#     

Clear semantic cache for a given llm\_string.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBMongoVCoreSemanticCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBMongoVCoreSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)