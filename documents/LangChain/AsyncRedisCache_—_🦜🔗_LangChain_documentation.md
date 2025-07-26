# AsyncRedisCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.AsyncRedisCache.html
**Word Count:** 304
**Links Count:** 153
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# AsyncRedisCache\#

_class _langchain\_community.cache.AsyncRedisCache\(

    _redis\_ : Any_,     _\*_ ,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache)\#     

Cache that uses Redis as a backend. Allows to use an async redis.asyncio.Redis client.

Initialize an instance of AsyncRedisCache.

This method initializes an object with Redis caching capabilities. It takes a redis\_ parameter, which should be an instance of a Redis client class \(redis.asyncio.Redis\), allowing the object to interact with a Redis server for caching purposes.

Parameters:     

  * **redis** \(_Any_\) – An instance of a Redis client class \(redis.asyncio.Redis\) to be used for caching. This allows the object to communicate with a Redis server for caching operations.

  * **ttl** \(_int_ _,__optional_\) – Time-to-live \(TTL\) for cached items in seconds. If provided, it sets the time duration for how long cached items will remain valid. If not provided, cached items will not have an automatic expiration.

  * **redis\_** \(_Any_\)

Methods

`__init__`\(redis\_, \*\[, ttl\]\) | Initialize an instance of AsyncRedisCache.   ---|---   `aclear`\(\*\*kwargs\) | Clear cache.   `alookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _redis\_ : Any_,     _\*_ ,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.__init__)\#     

Initialize an instance of AsyncRedisCache.

This method initializes an object with Redis caching capabilities. It takes a redis\_ parameter, which should be an instance of a Redis client class \(redis.asyncio.Redis\), allowing the object to interact with a Redis server for caching purposes.

Parameters:     

  * **redis** \(_Any_\) – An instance of a Redis client class \(redis.asyncio.Redis\) to be used for caching. This allows the object to communicate with a Redis server for caching operations.

  * **ttl** \(_int_ _,__optional_\) – Time-to-live \(TTL\) for cached items in seconds. If provided, it sets the time duration for how long cached items will remain valid. If not provided, cached items will not have an automatic expiration.

  * **redis\_** \(_Any_\)

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.aclear)\#     

Clear cache. If asynchronous is True, flush asynchronously. Async version.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.alookup)\#     

Look up based on prompt and llm\_string. Async version.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

_async _aupdate\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.aupdate)\#     

Update cache based on prompt and llm\_string. Async version.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.clear)\#     

Clear cache. If asynchronous is True, flush asynchronously.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AsyncRedisCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)