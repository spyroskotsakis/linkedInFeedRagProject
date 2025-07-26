# MemcachedCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.MemcachedCache.html
**Word Count:** 512
**Links Count:** 150
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# MemcachedCache\#

_class _langchain\_community.cache.MemcachedCache\(_client\_ : Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MemcachedCache)\#     

Cache that uses Memcached backend through pymemcache client lib

Initialize an instance of MemcachedCache.

Parameters:     

  * **client** \(_str_\) – An instance of any of pymemcache’s Clients \(Client, PooledClient, HashClient\)

  * **client\_** \(_Any_\)

Example: .. code-block:: python

> ifrom langchain.globals import set\_llm\_cache from langchain\_openai import OpenAI >  > from langchain\_community.cache import MemcachedCache from pymemcache.client.base import Client >  > llm = OpenAI\(model=”gpt-3.5-turbo-instruct”, n=2, best\_of=2\) set\_llm\_cache\(MemcachedCache\(Client\(‘localhost’\)\)\) >  > \# The first time, it is not yet in cache, so it should take longer llm.invoke\(“Which city is the most crowded city in the USA?”\) >  > \# The second time it is, so it goes faster llm.invoke\(“Which city is the most crowded city in the USA?”\)

Methods

`__init__`\(client\_\) | Initialize an instance of MemcachedCache.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear the entire cache.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(_client\_ : Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MemcachedCache.__init__)\#     

Initialize an instance of MemcachedCache.

Parameters:     

  * **client** \(_str_\) – An instance of any of pymemcache’s Clients \(Client, PooledClient, HashClient\)

  * **client\_** \(_Any_\)

Example: .. code-block:: python

> ifrom langchain.globals import set\_llm\_cache from langchain\_openai import OpenAI >  > from langchain\_community.cache import MemcachedCache from pymemcache.client.base import Client >  > llm = OpenAI\(model=”gpt-3.5-turbo-instruct”, n=2, best\_of=2\) set\_llm\_cache\(MemcachedCache\(Client\(‘localhost’\)\)\) >  > \# The first time, it is not yet in cache, so it should take longer llm.invoke\(“Which city is the most crowded city in the USA?”\) >  > \# The second time it is, so it goes faster llm.invoke\(“Which city is the most crowded city in the USA?”\)

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MemcachedCache.clear)\#     

Clear the entire cache. Takes optional kwargs:

delay: optional int, the number of seconds to wait before flushing,     

or zero to flush immediately \(the default\). NON-BLOCKING, returns immediately.

noreply: optional bool, True to not wait for the reply \(defaults to     

client.default\_noreply\).

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MemcachedCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MemcachedCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page