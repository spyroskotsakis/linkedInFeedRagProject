# AzureCosmosDBNoSqlSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/vectorstores/langchain_azure_ai.vectorstores.cache.AzureCosmosDBNoSqlSemanticCache.html
**Word Count:** 420
**Links Count:** 124
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# AzureCosmosDBNoSqlSemanticCache\#

_class _langchain\_azure\_ai.vectorstores.cache.AzureCosmosDBNoSqlSemanticCache\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _cosmos\_client : CosmosClient_,     _database\_name : str = 'CosmosNoSqlCacheDB'_,     _container\_name : str = 'CosmosNoSqlCacheContainer'_,     _\*_ ,     _vector\_embedding\_policy : Dict\[str, Any\]_,     _indexing\_policy : Dict\[str, Any\]_,     _cosmos\_container\_properties : Dict\[str, Any\]_,     _cosmos\_database\_properties : Dict\[str, Any\]_,     _vector\_search\_fields : Dict\[str, Any\]_,     _search\_type : str = 'vector'_,     _create\_container : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBNoSqlSemanticCache)\#     

Cache that uses Cosmos DB NoSQL backend.

AzureCosmosDBNoSqlSemanticCache constructor.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – CosmosDB Embedding.

  * **cosmos\_client** \(_CosmosClient_\) – CosmosDB client

  * **database\_name** \(_str_\) – CosmosDB database name

  * **container\_name** \(_str_\) – CosmosDB container name

  * **vector\_embedding\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB vector embedding policy

  * **indexing\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB indexing policy

  * **cosmos\_container\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB container properties

  * **cosmos\_database\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB database properties

  * **vector\_search\_fields** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – Vector Search Fields for the container.

  * **search\_type** \(_str_\) – CosmosDB search type.

  * **create\_container** \(_bool_\) – Create the container if it doesn’t exist.

Methods

`__init__`\(embedding, cosmos\_client\[, ...\]\) | AzureCosmosDBNoSqlSemanticCache constructor.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear semantic cache for a given llm\_string.   `lookup`\(prompt, llm\_string\) | Look up based on prompt.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _cosmos\_client : CosmosClient_,     _database\_name : str = 'CosmosNoSqlCacheDB'_,     _container\_name : str = 'CosmosNoSqlCacheContainer'_,     _\*_ ,     _vector\_embedding\_policy : Dict\[str, Any\]_,     _indexing\_policy : Dict\[str, Any\]_,     _cosmos\_container\_properties : Dict\[str, Any\]_,     _cosmos\_database\_properties : Dict\[str, Any\]_,     _vector\_search\_fields : Dict\[str, Any\]_,     _search\_type : str = 'vector'_,     _create\_container : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBNoSqlSemanticCache.__init__)\#     

AzureCosmosDBNoSqlSemanticCache constructor.

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – CosmosDB Embedding.

  * **cosmos\_client** \(_CosmosClient_\) – CosmosDB client

  * **database\_name** \(_str_\) – CosmosDB database name

  * **container\_name** \(_str_\) – CosmosDB container name

  * **vector\_embedding\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB vector embedding policy

  * **indexing\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB indexing policy

  * **cosmos\_container\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB container properties

  * **cosmos\_database\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – CosmosDB database properties

  * **vector\_search\_fields** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – Vector Search Fields for the container.

  * **search\_type** \(_str_\) – CosmosDB search type.

  * **create\_container** \(_bool_\) – Create the container if it doesn’t exist.

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

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBNoSqlSemanticCache.clear)\#     

Clear semantic cache for a given llm\_string.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBNoSqlSemanticCache.lookup)\#     

Look up based on prompt.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/vectorstores/cache.html#AzureCosmosDBNoSqlSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)