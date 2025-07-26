# InMemoryCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/caches/langchain_core.caches.InMemoryCache.html
**Word Count:** 391
**Links Count:** 139
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# InMemoryCache\#

_class _langchain\_core.caches.InMemoryCache\(_\*_ , _maxsize : int | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache)\#     

Cache that stores things in memory.

Initialize with empty cache.

Parameters:     

**maxsize** \(_Optional_ _\[__int_ _\]_\) – The maximum number of items to store in the cache. If None, the cache has no maximum size. If the cache exceeds the maximum size, the oldest items are removed. Default is None.

Raises:     

**ValueError** – If maxsize is less than or equal to 0.

Methods

`__init__`\(\*\[, maxsize\]\) | Initialize with empty cache.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _\*_ ,     _maxsize : int | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.__init__)\#     

Initialize with empty cache.

Parameters:     

**maxsize** \(_int_ _|__None_\) – The maximum number of items to store in the cache. If None, the cache has no maximum size. If the cache exceeds the maximum size, the oldest items are removed. Default is None.

Raises:     

**ValueError** – If maxsize is less than or equal to 0.

Return type:     

None

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.aclear)\#     

Async clear cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.alookup)\#     

Async look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration.

Returns:     

On a cache miss, return None. On a cache hit, return the cached value.

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

_async _aupdate\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.clear)\#     

Clear cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration.

Returns:     

On a cache miss, return None. On a cache hit, return the cached value.

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/caches.html#InMemoryCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

Examples using InMemoryCache

  * [How to cache LLM responses](https://python.langchain.com/docs/how_to/llm_caching/)

  * [How to cache chat model responses](https://python.langchain.com/docs/how_to/chat_model_caching/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)