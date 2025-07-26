# AzureCosmosDBNoSqlSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.AzureCosmosDBNoSqlSemanticCache.html
**Word Count:** 317
**Links Count:** 154
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# AzureCosmosDBNoSqlSemanticCache\#

_class _langchain\_community.cache.AzureCosmosDBNoSqlSemanticCache\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _cosmos\_client : CosmosClient_,     _database\_name : str = 'CosmosNoSqlCacheDB'_,     _container\_name : str = 'CosmosNoSqlCacheContainer'_,     _\*_ ,     _vector\_embedding\_policy : Dict\[str, Any\]_,     _indexing\_policy : Dict\[str, Any\]_,     _cosmos\_container\_properties : Dict\[str, Any\]_,     _cosmos\_database\_properties : Dict\[str, Any\]_,     _create\_container : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBNoSqlSemanticCache)\#     

Cache that uses Cosmos DB NoSQL backend

Methods

`__init__`\(embedding, cosmos\_client\[, ...\]\) |    ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear semantic cache for a given llm\_string.   `lookup`\(prompt, llm\_string\) | Look up based on prompt.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **cosmos\_client** \(_CosmosClient_\)

  * **database\_name** \(_str_\)

  * **container\_name** \(_str_\)

  * **vector\_embedding\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **indexing\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **cosmos\_container\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **cosmos\_database\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **create\_container** \(_bool_\)

\_\_init\_\_\(

    _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _cosmos\_client : CosmosClient_,     _database\_name : str = 'CosmosNoSqlCacheDB'_,     _container\_name : str = 'CosmosNoSqlCacheContainer'_,     _\*_ ,     _vector\_embedding\_policy : Dict\[str, Any\]_,     _indexing\_policy : Dict\[str, Any\]_,     _cosmos\_container\_properties : Dict\[str, Any\]_,     _cosmos\_database\_properties : Dict\[str, Any\]_,     _create\_container : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBNoSqlSemanticCache.__init__)\#     

Parameters:     

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **cosmos\_client** \(_CosmosClient_\)

  * **database\_name** \(_str_\)

  * **container\_name** \(_str_\)

  * **vector\_embedding\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **indexing\_policy** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **cosmos\_container\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **cosmos\_database\_properties** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **create\_container** \(_bool_\)

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

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBNoSqlSemanticCache.clear)\#     

Clear semantic cache for a given llm\_string.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBNoSqlSemanticCache.lookup)\#     

Look up based on prompt.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AzureCosmosDBNoSqlSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)