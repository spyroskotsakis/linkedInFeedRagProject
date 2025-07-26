# RedisSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.RedisSemanticCache.html
**Word Count:** 368
**Links Count:** 154
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# RedisSemanticCache\#

_class _langchain\_community.cache.RedisSemanticCache\(

    _redis\_url : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _score\_threshold : float = 0.2_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#RedisSemanticCache)\#     

Cache that uses Redis as a vector-store backend.

Initialize by passing in the init GPTCache func

Parameters:     

  * **redis\_url** \(_str_\) – URL to connect to Redis.

  * **embedding** \(_Embedding_\) – Embedding provider for semantic encoding and search.

  * **score\_threshold** \(_float_ _,__0.2_\)

Example:               from langchain_community.globals import set_llm_cache          from langchain_community.cache import RedisSemanticCache     from langchain_community.embeddings import OpenAIEmbeddings          set_llm_cache(RedisSemanticCache(         redis_url="redis://localhost:6379",         embedding=OpenAIEmbeddings()     ))     

Attributes

`DEFAULT_SCHEMA` |    ---|---      Methods

`__init__`\(redis\_url, embedding\[, score\_threshold\]\) | Initialize by passing in the init GPTCache func   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear semantic cache for a given llm\_string.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _redis\_url : str_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _score\_threshold : float = 0.2_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#RedisSemanticCache.__init__)\#     

Initialize by passing in the init GPTCache func

Parameters:     

  * **redis\_url** \(_str_\) – URL to connect to Redis.

  * **embedding** \(_Embedding_\) – Embedding provider for semantic encoding and search.

  * **score\_threshold** \(_float_ _,__0.2_\)

Example:               from langchain_community.globals import set_llm_cache          from langchain_community.cache import RedisSemanticCache     from langchain_community.embeddings import OpenAIEmbeddings          set_llm_cache(RedisSemanticCache(         redis_url="redis://localhost:6379",         embedding=OpenAIEmbeddings()     ))     

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

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#RedisSemanticCache.clear)\#     

Clear semantic cache for a given llm\_string.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#RedisSemanticCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#RedisSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

Examples using RedisSemanticCache

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Redis](https://python.langchain.com/docs/integrations/providers/redis/)

__On this page