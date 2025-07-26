# RedisCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/cache/langchain_redis.cache.RedisCache.html
**Word Count:** 883
**Links Count:** 116
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# RedisCache\#

_class _langchain\_redis.cache.RedisCache\(

    _redis\_url : str = 'redis://localhost:6379'_,     _ttl : int | None = None_,     _prefix : str | None = 'redis'_,     _redis\_client : Redis | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisCache)\#     

Redis cache implementation for LangChain.

This class provides a Redis-based caching mechanism for LangChain, allowing storage and retrieval of language model responses.

redis\#     

The Redis client instance.

Type:     

[Redis](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")

ttl\#     

Time-to-live for cache entries in seconds. If None, entries don’t expire.

Type:     

Optional\[int\]

prefix\#     

Prefix for all keys stored in Redis.

Type:     

Optional\[str\]

Parameters:     

  * **redis\_url** \(_str_\) – The URL of the Redis instance to connect to. Defaults to “redis://localhost:6379”.

  * **ttl** \(_Optional_ _\[__int_ _\]_\) – Time-to-live for cache entries in seconds. Defaults to None \(no expiration\).

  * **prefix** \(_Optional_ _\[__str_ _\]_\) – Prefix for all keys stored in Redis. Defaults to “redis”.

  * **redis** \(_Optional_ _\[_[_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis") _\]_\) – An existing Redis client instance. If provided, redis\_url is ignored.

  * **redis\_client** \(_Optional_ _\[_[_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis") _\]_\)

Example               from langchain_redis import RedisCache     from langchain_core.globals import set_llm_cache          # Create a Redis cache instance     redis_cache = RedisCache(redis_url="redis://localhost:6379", ttl=3600)          # Set it as the global LLM cache     set_llm_cache(redis_cache)          # Now, when you use an LLM, it will automatically use this cache     

Note

  * This cache implementation uses Redis JSON capabilities to store structured data.

  * The cache key is created using MD5 hashes of the prompt and LLM string.

  * If TTL is set, cache entries will automatically expire after the specified duration.

  * The prefix can be used to namespace cache entries.

Methods

`__init__`\(\[redis\_url, ttl, prefix, redis\_client\]\) |    ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear all entries in the Redis cache that match the cache prefix.   `lookup`\(prompt, llm\_string\) | Look up the result of a previous language model call in the Redis cache.   `update`\(prompt, llm\_string, return\_val\) | Update the cache with a new result for a given prompt and language model.      \_\_init\_\_\(

    _redis\_url : str = 'redis://localhost:6379'_,     _ttl : int | None = None_,     _prefix : str | None = 'redis'_,     _redis\_client : Redis | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisCache.__init__)\#     

Parameters:     

  * **redis\_url** \(_str_\)

  * **ttl** \(_int_ _|__None_\)

  * **prefix** \(_str_ _|__None_\)

  * **redis\_client** \(_Redis_ _|__None_\)

_async _aclear\(_\*\* kwargs: Any_\) → None\#     

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisCache.clear)\#     

Clear all entries in the Redis cache that match the cache prefix.

This method removes all cache entries that start with the specified prefix.

Parameters:     

**\*\*kwargs** \(_Any_\) – Additional keyword arguments. Currently not used, but included for potential future extensions.

Returns:     

None

Return type:     

None

Example               cache = RedisCache(       redis_url="redis://localhost:6379",       prefix="my_cache"     )          # Add some entries to the cache     cache.update("prompt1", "llm1", [Generation(text="Result 1")])     cache.update("prompt2", "llm2", [Generation(text="Result 2")])          # Clear all entries     cache.clear()          # After this, all entries with keys starting with "my_cache:"     # will be removed     

Note

  * This method uses Redis SCAN to iterate over keys, which is safe for large datasets.

  * It deletes keys in batches of 100 to optimize performance.

  * Only keys that start with the specified prefix \(default is “redis:”\) will be deleted.

  * This operation is irreversible. Make sure you want to clear all cached data before calling this method.

  * If no keys match the prefix, the method will complete without any errors.

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisCache.lookup)\#     

Look up the result of a previous language model call in the Redis cache.

This method checks if there’s a cached result for the given prompt and language model combination.

Parameters:     

  * **prompt** \(_str_\) – The input prompt for which to look up the cached result.

  * **llm\_string** \(_str_\) – A string representation of the language model and its parameters.

Returns:     

The cached result if found, or None if not     

present in the cache.

The result is typically a list containing a single Generation object.

Return type:     

Optional\[RETURN\_VAL\_TYPE\]

Example               cache = RedisCache(redis_url="redis://localhost:6379")     prompt = "What is the capital of France?"     llm_string = "openai/gpt-3.5-turbo"          result = cache.lookup(prompt, llm_string)     if result:         print("Cache hit:", result[0].text)     else:         print("Cache miss")     

Note

  * The method uses an MD5 hash of the prompt and llm\_string to create the cache key.

  * The cached value is stored as JSON and parsed back into a Generation object.

  * If the key exists but the value is None or cannot be parsed, None is returned.

  * This method is typically called internally by LangChain, but can be used directly for manual cache interactions.

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/cache.html#RedisCache.update)\#     

Update the cache with a new result for a given prompt and language model.

This method stores a new result in the Redis cache for the specified prompt and language model combination.

Parameters:     

  * **prompt** \(_str_\) – The input prompt associated with the result.

  * **llm\_string** \(_str_\) – A string representation of the language model and its parameters.

  * **return\_val** \(_RETURN\_VAL\_TYPE_\) – The result to be cached, typically a list containing a single Generation object.

Returns:     

None

Return type:     

None

Example               from langchain_core.outputs import Generation          cache = RedisCache(redis_url="redis://localhost:6379", ttl=3600)     prompt = "What is the capital of France?"     llm_string = "openai/gpt-3.5-turbo"     result = [Generation(text="The capital of France is Paris.")]          cache.update(prompt, llm_string, result)     

Note

  * The method uses an MD5 hash of the prompt and llm\_string to create the cache key.

  * The result is stored as JSON in Redis.

  * If a TTL \(Time To Live\) was specified when initializing the cache, it will be applied to this entry.

  * This method is typically called internally by LangChain after a language model generates a response, but it can be used directly for manual cache updates.

  * If the cache already contains an entry for this prompt and llm\_string, it will be overwritten.

Examples using RedisCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Redis](https://python.langchain.com/docs/integrations/providers/redis/)

__On this page