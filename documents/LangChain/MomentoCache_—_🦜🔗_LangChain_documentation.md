# MomentoCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.MomentoCache.html
**Word Count:** 572
**Links Count:** 159
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# MomentoCache\#

_class _langchain\_community.cache.MomentoCache\(

    _cache\_client : momento.CacheClient_,     _cache\_name : str_,     _\*_ ,     _ttl : timedelta | None = None_,     _ensure\_cache\_exists : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MomentoCache)\#     

Cache that uses Momento as a backend. See <https://gomomento.com/>

Instantiate a prompt cache using Momento as a backend.

Note: to instantiate the cache client passed to MomentoCache, you must have a Momento account. See <https://gomomento.com/>.

Parameters:     

  * **cache\_client** \(_CacheClient_\) – The Momento cache client.

  * **cache\_name** \(_str_\) – The name of the cache to use to store the data.

  * **ttl** \(_Optional_ _\[__timedelta_ _\]__,__optional_\) – The time to live for the cache items. Defaults to None, ie use the client default TTL.

  * **ensure\_cache\_exists** \(_bool_ _,__optional_\) – Create the cache if it doesn’t exist. Defaults to True.

Raises:     

  * **ImportError** – Momento python package is not installed.

  * **TypeError** – cache\_client is not of type momento.CacheClientObject

  * **ValueError** – ttl is non-null and non-negative

Methods

`__init__`\(cache\_client, cache\_name, \*\[, ttl, ...\]\) | Instantiate a prompt cache using Momento as a backend.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear the cache.   `from_client_params`\(cache\_name, ttl, \*\[, ...\]\) | Construct cache from CacheClient parameters.   `lookup`\(prompt, llm\_string\) | Lookup llm generations in cache by prompt and associated model and settings.   `update`\(prompt, llm\_string, return\_val\) | Store llm generations in cache.      \_\_init\_\_\(

    _cache\_client : momento.CacheClient_,     _cache\_name : str_,     _\*_ ,     _ttl : timedelta | None = None_,     _ensure\_cache\_exists : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MomentoCache.__init__)\#     

Instantiate a prompt cache using Momento as a backend.

Note: to instantiate the cache client passed to MomentoCache, you must have a Momento account. See <https://gomomento.com/>.

Parameters:     

  * **cache\_client** \(_CacheClient_\) – The Momento cache client.

  * **cache\_name** \(_str_\) – The name of the cache to use to store the data.

  * **ttl** \(_Optional_ _\[__timedelta_ _\]__,__optional_\) – The time to live for the cache items. Defaults to None, ie use the client default TTL.

  * **ensure\_cache\_exists** \(_bool_ _,__optional_\) – Create the cache if it doesn’t exist. Defaults to True.

Raises:     

  * **ImportError** – Momento python package is not installed.

  * **TypeError** – cache\_client is not of type momento.CacheClientObject

  * **ValueError** – ttl is non-null and non-negative

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MomentoCache.clear)\#     

Clear the cache.

Raises:     

**SdkException** – Momento service or network error

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_classmethod _from\_client\_params\(

    _cache\_name : str_,     _ttl : timedelta_,     _\*_ ,     _configuration : momento.config.Configuration | None = None_,     _api\_key : str | None = None_,     _auth\_token : str | None = None_,     _\*\* kwargs: Any_, \) → MomentoCache[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MomentoCache.from_client_params)\#     

Construct cache from CacheClient parameters.

Parameters:     

  * **cache\_name** \(_str_\)

  * **ttl** \(_timedelta_\)

  * **configuration** \(_Optional_ _\[__momento.config.Configuration_ _\]_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **auth\_token** \(_Optional_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

MomentoCache

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MomentoCache.lookup)\#     

Lookup llm generations in cache by prompt and associated model and settings.

Parameters:     

  * **prompt** \(_str_\) – The prompt run through the language model.

  * **llm\_string** \(_str_\) – The language model version and settings.

Raises:     

**SdkException** – Momento service or network error

Returns:     

A list of language model generations.

Return type:     

Optional\[RETURN\_VAL\_TYPE\]

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#MomentoCache.update)\#     

Store llm generations in cache.

Parameters:     

  * **prompt** \(_str_\) – The prompt run through the language model.

  * **llm\_string** \(_str_\) – The language model string.

  * **return\_val** \(_RETURN\_VAL\_TYPE_\) – A list of language model generations.

Raises:     

  * **SdkException** – Momento service or network error

  * **Exception** – Unexpected response

Return type:     

None

Examples using MomentoCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Momento](https://python.langchain.com/docs/integrations/providers/momento/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)