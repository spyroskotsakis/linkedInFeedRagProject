# UpstashRedisCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.UpstashRedisCache.html
**Word Count:** 523
**Links Count:** 152
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# UpstashRedisCache\#

_class _langchain\_community.cache.UpstashRedisCache\(

    _redis\_ : Any_,     _\*_ ,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#UpstashRedisCache)\#     

Cache that uses Upstash Redis as a backend.

Initialize an instance of UpstashRedisCache.

This method initializes an object with Upstash Redis caching capabilities. It takes a redis\_ parameter, which should be an instance of an Upstash Redis client class, allowing the object to interact with Upstash Redis server for caching purposes.

Parameters:     

  * **redis** – An instance of Upstash Redis client class \(e.g., Redis\) used for caching. This allows the object to communicate with Redis server for caching operations on.

  * **ttl** \(_int_ _,__optional_\) – Time-to-live \(TTL\) for cached items in seconds. If provided, it sets the time duration for how long cached items will remain valid. If not provided, cached items will not have an automatic expiration.

  * **redis\_** \(_Any_\)

Methods

`__init__`\(redis\_, \*\[, ttl\]\) | Initialize an instance of UpstashRedisCache.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _redis\_ : Any_,     _\*_ ,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#UpstashRedisCache.__init__)\#     

Initialize an instance of UpstashRedisCache.

This method initializes an object with Upstash Redis caching capabilities. It takes a redis\_ parameter, which should be an instance of an Upstash Redis client class, allowing the object to interact with Upstash Redis server for caching purposes.

Parameters:     

  * **redis** – An instance of Upstash Redis client class \(e.g., Redis\) used for caching. This allows the object to communicate with Redis server for caching operations on.

  * **ttl** \(_int_ _,__optional_\) – Time-to-live \(TTL\) for cached items in seconds. If provided, it sets the time duration for how long cached items will remain valid. If not provided, cached items will not have an automatic expiration.

  * **redis\_** \(_Any_\)

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#UpstashRedisCache.clear)\#     

Clear cache. If asynchronous is True, flush asynchronously. This flushes the _whole_ db.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#UpstashRedisCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#UpstashRedisCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

Examples using UpstashRedisCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Upstash Vector](https://python.langchain.com/docs/integrations/providers/upstash/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)