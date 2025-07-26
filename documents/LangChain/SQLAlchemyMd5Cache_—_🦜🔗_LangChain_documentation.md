# SQLAlchemyMd5Cache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.SQLAlchemyMd5Cache.html
**Word Count:** 321
**Links Count:** 156
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# SQLAlchemyMd5Cache\#

_class _langchain\_community.cache.SQLAlchemyMd5Cache\(

    _engine: ~sqlalchemy.engine.base.Engine_,     _cache\_schema: ~typing.Type\[~langchain\_community.cache.FullMd5LLMCache\] = <class 'langchain\_community.cache.FullMd5LLMCache'>_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SQLAlchemyMd5Cache)\#     

Cache that uses SQAlchemy as a backend.

Initialize by creating all tables.

Methods

`__init__`\(engine\[, cache\_schema\]\) | Initialize by creating all tables.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache.   `get_md5`\(input\_string\) |    `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update based on prompt and llm\_string.      Parameters:     

  * **engine** \(_Engine_\)

  * **cache\_schema** \(_Type_ _\[_[_FullMd5LLMCache_](https://python.langchain.com/api_reference/community/cache/langchain_community.cache.FullMd5LLMCache.html#langchain_community.cache.FullMd5LLMCache "langchain_community.cache.FullMd5LLMCache") _\]_\)

\_\_init\_\_\(

    _engine: ~sqlalchemy.engine.base.Engine_,     _cache\_schema: ~typing.Type\[~langchain\_community.cache.FullMd5LLMCache\] = <class 'langchain\_community.cache.FullMd5LLMCache'>_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SQLAlchemyMd5Cache.__init__)\#     

Initialize by creating all tables.

Parameters:     

  * **engine** \(_Engine_\)

  * **cache\_schema** \(_Type_ _\[_[_FullMd5LLMCache_](https://python.langchain.com/api_reference/community/cache/langchain_community.cache.FullMd5LLMCache.html#langchain_community.cache.FullMd5LLMCache "langchain_community.cache.FullMd5LLMCache") _\]_\)

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SQLAlchemyMd5Cache.clear)\#     

Clear cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_static _get\_md5\(_input\_string : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SQLAlchemyMd5Cache.get_md5)\#     

Parameters:     

**input\_string** \(_str_\)

Return type:     

str

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SQLAlchemyMd5Cache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#SQLAlchemyMd5Cache.update)\#     

Update based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page