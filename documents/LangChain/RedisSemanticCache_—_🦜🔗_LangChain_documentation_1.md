# RedisSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/cache/langchain_redis.cache.RedisSemanticCache.html
**Word Count:** 1125
**Links Count:** 128
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# RedisSemanticCache\#

_class _langchain\_redis.cache.RedisSemanticCache\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _redis\_url : str = 'redis://localhost:6379'_,     _distance\_threshold : float = 0.2_,     _ttl : int | None = None_,     _name : str | None = 'llmcache'_,     _prefix : str | None = 'llmcache'_,     _redis\_client : Redis | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache)\#     

Redis-based semantic cache implementation for LangChain.

This class provides a semantic caching mechanism using Redis and vector similarity search. It allows for storing and retrieving language model responses based on the semantic similarity of prompts, rather than exact string matching.

redis\#     

The Redis client instance.

Type:     

[Redis](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")

embeddings\#     

The embedding function to use for encoding prompts.

Type:     

[Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

cache\#     

The underlying RedisVL semantic cache instance.

Type:     

RedisVLSemanticCache

Parameters:     

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – The embedding function to use for encoding prompts.

  * **redis\_url** \(_str_\) – The URL of the Redis instance to connect to. Defaults to “redis://localhost:6379”.

  * **distance\_threshold** \(_float_\) – The maximum distance for considering a cache hit. Defaults to 0.2.

  * **ttl** \(_Optional_ _\[__int_ _\]_\) – Time-to-live for cache entries in seconds. Defaults to None \(no expiration\).

  * **name** \(_Optional_ _\[__str_ _\]_\) – Name for the cache index. Defaults to “llmcache”.

  * **prefix** \(_Optional_ _\[__str_ _\]_\) – Prefix for all keys stored in Redis. Defaults to “llmcache”.

  * **redis** \(_Optional_ _\[_[_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis") _\]_\) – An existing Redis client instance. If provided, redis\_url is ignored.

  * **redis\_client** \(_Optional_ _\[_[_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis") _\]_\)

Example               from langchain_redis import RedisSemanticCache     from langchain_openai import OpenAIEmbeddings     from langchain_core.globals import set_llm_cache          embeddings = OpenAIEmbeddings()     semantic_cache = RedisSemanticCache(         embeddings=embeddings,         redis_url="redis://localhost:6379",         distance_threshold=0.1     )          set_llm_cache(semantic_cache)          # Now, when you use an LLM, it will automatically use this semantic cache     

Note

  * This cache uses vector similarity search to find semantically similar prompts.

  * The distance\_threshold determines how similar a prompt must be to trigger a cache hit.

  * Lowering the distance\_threshold increases precision but may reduce cache hits.

  * The cache uses the RedisVL library for efficient vector storage and retrieval.

  * Semantic caching can be more flexible than exact matching, allowing cache hits for prompts that are semantically similar but not identical.

Methods

`__init__`\(embeddings\[, redis\_url, ...\]\) |    ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear all entries in the Redis semantic cache.   `lookup`\(prompt, llm\_string\) | Look up the result of a previous language model call in the   `name`\(\) | Get the name of the semantic cache index.   `update`\(prompt, llm\_string, return\_val\) | Update the semantic cache with a new result for a given prompt      \_\_init\_\_\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _redis\_url : str = 'redis://localhost:6379'_,     _distance\_threshold : float = 0.2_,     _ttl : int | None = None_,     _name : str | None = 'llmcache'_,     _prefix : str | None = 'llmcache'_,     _redis\_client : Redis | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.__init__)\#     

Parameters:     

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **redis\_url** \(_str_\)

  * **distance\_threshold** \(_float_\)

  * **ttl** \(_int_ _|__None_\)

  * **name** \(_str_ _|__None_\)

  * **prefix** \(_str_ _|__None_\)

  * **redis\_client** \(_Redis_ _|__None_\)

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.aclear)\#     

Async clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.alookup)\#     

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

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.clear)\#     

Clear all entries in the Redis semantic cache.

This method removes all cache entries from the semantic cache.

Parameters:     

**\*\*kwargs** \(_Any_\) – Additional keyword arguments. Currently not used, but included for potential future extensions.

Returns:     

None

Return type:     

None

Example               from langchain_openai import OpenAIEmbeddings          cache = RedisSemanticCache(         embeddings=OpenAIEmbeddings(),         redis_url="redis://localhost:6379",         name="my_semantic_cache"     )          # Add some entries to the cache     cache.update(       "What is the capital of France?",       "llm1",       [Generation(text="Paris")]     )     cache.update(       "Who wrote Romeo and Juliet?",       "llm2",       [Generation(text="Shakespeare")]     )          # Clear all entries     cache.clear()          # After this, all entries in the semantic cache will be removed     

Note

  * This method clears all entries in the semantic cache, regardless of their content or similarity.

  * It uses the underlying cache implementation’s clear method, which efficiently removes all entries.

  * This operation is irreversible. Make sure you want to clear all cached data before calling this method.

  * After clearing, the cache will be empty, but the index structure is maintained and ready for new entries.

  * This method is useful for resetting the cache or clearing out old data, especially if the nature of the queries or the embedding model has changed significantly.

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.lookup)\#     

Look up the result of a previous language model call in the     

Redis semantic cache.

This method checks if there’s a cached result for a semantically similar prompt and the same language model combination.

Parameters:     

  * **prompt** \(_str_\) – The input prompt for which to look up the cached result.

  * **llm\_string** \(_str_\) – A string representation of the language model and its parameters.

Returns:     

The cached result if a semantically similar     

prompt is found,

or None if no suitable match is present in the cache. The result is typically a list containing a single Generation object.

Return type:     

Optional\[RETURN\_VAL\_TYPE\]

Example               from langchain_openai import OpenAIEmbeddings     cache = RedisSemanticCache(         embeddings=OpenAIEmbeddings(),         redis_url="redis://localhost:6379"     )     prompt = "What's the capital city of France?"     llm_string = "openai/gpt-3.5-turbo"          result = cache.lookup(prompt, llm_string)     if result:         print("Semantic cache hit:", result[0].text)     else:         print("Semantic cache miss")     

Note

  * This method uses vector similarity search to find semantically similar prompts.

  * The prompt is embedded using the provided embedding function.

  * The method checks for cached results within the distance threshold specified during cache initialization.

  * If multiple results are within the threshold, the most similar one is returned.

  * The llm\_string is used to ensure the cached result is from the same language model.

  * This method is typically called internally by LangChain, but can be used directly for manual cache interactions.

  * Unlike exact matching, this may return results for prompts that are semantically similar but not identical to the input.

name\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.name)\#     

Get the name of the semantic cache index.

This method returns the name of the index used for the semantic cache in Redis.

Returns:     

The name of the semantic cache index.

Return type:     

str

Example               from langchain_openai import OpenAIEmbeddings          cache = RedisSemanticCache(         embeddings=OpenAIEmbeddings(),         redis_url="redis://localhost:6379",         name="my_custom_cache"     )          index_name = cache.name()     print(f"The semantic cache is using index: {index_name}")     

Note

  * The index name is set during the initialization of the RedisSemanticCache.

  * If no custom name was provided during initialization, a default name is used.

  * This name is used internally to identify and manage the semantic cache in Redis.

  * Knowing the index name can be useful for debugging or for direct interactions with the Redis database outside of this cache interface.

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisSemanticCache.update)\#     

Update the semantic cache with a new result for a given prompt     

and language model.

This method stores a new result in the Redis semantic cache for the specified prompt and language model combination, using vector embedding for semantic similarity.

Parameters:     

  * **prompt** \(_str_\) – The input prompt associated with the result.

  * **llm\_string** \(_str_\) – A string representation of the language model and its parameters.

  * **return\_val** \(_RETURN\_VAL\_TYPE_\) – The result to be cached, typically a list containing a single Generation object.

Returns:     

None

Return type:     

None

Example               from langchain_core.outputs import Generation     from langchain_openai import OpenAIEmbeddings          cache = RedisSemanticCache(         embeddings=OpenAIEmbeddings(),         redis_url="redis://localhost:6379"     )     prompt = "What is the capital of France?"     llm_string = "openai/gpt-3.5-turbo"     result = [Generation(text="The capital of France is Paris.")]          cache.update(prompt, llm_string, result)     

Note

  * The method uses the provided embedding function to convert the prompt into a vector.

  * The vector, along with the prompt, llm\_string, and result, is stored in the Redis cache.

  * If a TTL \(Time To Live\) was specified when initializing the cache, it will be applied to this entry.

  * This method is typically called internally by LangChain after a language model generates a response, but it can be used directly for manual cache updates.

  * Unlike exact matching caches, this allows for semantic similarity lookups later.

  * If the cache already contains very similar entries, this will add a new entry rather than overwriting.

  * The effectiveness of the cache depends on the quality of the embedding function used.

Examples using RedisSemanticCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Redis](https://python.langchain.com/docs/integrations/providers/redis/)

__On this page