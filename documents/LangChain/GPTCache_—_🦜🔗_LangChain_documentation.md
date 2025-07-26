# GPTCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.GPTCache.html
**Word Count:** 446
**Links Count:** 151
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# GPTCache\#

_class _langchain\_community.cache.GPTCache\(

    _init\_func : Callable\[\[Any, str\], None\] | Callable\[\[Any\], None\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#GPTCache)\#     

Cache that uses GPTCache as a backend.

Initialize by passing in init function \(default: None\).

Parameters:     

  * **init\_func** \(_Optional_ _\[__Callable_ _\[__\[__Any_ _\]__,__None_ _\]__\]_\) – init GPTCache function

  * **\(****default** – None\)

Example: .. code-block:: python

> \# Initialize GPTCache with a custom init function import gptcache from gptcache.processor.pre import get\_prompt from gptcache.manager.factory import get\_data\_manager from langchain\_community.globals import set\_llm\_cache >  > \# Avoid multiple caches using the same file, causing different llm model caches to affect each other >  > def init\_gptcache\(cache\_obj: gptcache.Cache, llm str\): >      >  > cache\_obj.init\( >      >  > pre\_embedding\_func=get\_prompt, data\_manager=manager\_factory\( >
>> manager=”map”, data\_dir=f”map\_cache\_\{llm\}” >  > \), >  > \) >  > set\_llm\_cache\(GPTCache\(init\_gptcache\)\)

Methods

`__init__`\(\[init\_func\]\) | Initialize by passing in init function \(default: None\).   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache.   `lookup`\(prompt, llm\_string\) | Look up the cache data.   `update`\(prompt, llm\_string, return\_val\) | Update cache.      \_\_init\_\_\(

    _init\_func : Callable\[\[Any, str\], None\] | Callable\[\[Any\], None\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#GPTCache.__init__)\#     

Initialize by passing in init function \(default: None\).

Parameters:     

  * **init\_func** \(_Optional_ _\[__Callable_ _\[__\[__Any_ _\]__,__None_ _\]__\]_\) – init GPTCache function

  * **\(****default** – None\)

Example: .. code-block:: python

> \# Initialize GPTCache with a custom init function import gptcache from gptcache.processor.pre import get\_prompt from gptcache.manager.factory import get\_data\_manager from langchain\_community.globals import set\_llm\_cache >  > \# Avoid multiple caches using the same file, causing different llm model caches to affect each other >  > def init\_gptcache\(cache\_obj: gptcache.Cache, llm str\): >      >  > cache\_obj.init\( >      >  > pre\_embedding\_func=get\_prompt, data\_manager=manager\_factory\( >
>> manager=”map”, data\_dir=f”map\_cache\_\{llm\}” >  > \), >  > \) >  > set\_llm\_cache\(GPTCache\(init\_gptcache\)\)

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#GPTCache.clear)\#     

Clear cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#GPTCache.lookup)\#     

Look up the cache data. First, retrieve the corresponding cache object using the llm\_string parameter, and then retrieve the data from the cache based on the prompt.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#GPTCache.update)\#     

Update cache. First, retrieve the corresponding cache object using the llm\_string parameter, and then store the prompt and return\_val in the cache object.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

Examples using GPTCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page