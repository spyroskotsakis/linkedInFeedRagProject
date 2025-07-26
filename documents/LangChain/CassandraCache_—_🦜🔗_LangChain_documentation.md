# CassandraCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.CassandraCache.html
**Word Count:** 732
**Links Count:** 165
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# CassandraCache\#

_class _langchain\_community.cache.CassandraCache\(

    _session : CassandraSession | None = None_,     _keyspace : str | None = None_,     _table\_name : str = 'langchain\_llm\_cache'_,     _ttl\_seconds : int | None = None_,     _skip\_provisioning : bool = False_,     _setup\_mode : CassandraSetupMode = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache)\#     

Cache that uses Cassandra / Astra DB as a backend.

Example               import cassio          from langchain_community.cache import CassandraCache     from langchain_core.globals import set_llm_cache          cassio.init(auto=True)  # Requires env. variables, see CassIO docs          set_llm_cache(CassandraCache())     

It uses a single Cassandra table. The lookup keys \(which get to form the primary key\) are:

>   * prompt, a string >  >   * llm\_string, a deterministic str representation of the model parameters. \(needed to prevent same-prompt-different-model collisions\) >  > 

Parameters:     

  * **session** \(_Optional_ _\[__CassandraSession_ _\]_\) – an open Cassandra session. Leave unspecified to use the global cassio init \(see below\)

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – the keyspace to use for storing the cache. Leave unspecified to use the global cassio init \(see below\)

  * **table\_name** \(_str_\) – name of the Cassandra table to use as cache

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – time-to-live for cache entries \(default: None, i.e. forever\)

  * **setup\_mode** \(_CassandraSetupMode_\) – a value in langchain\_community.utilities.cassandra.SetupMode. Choose between SYNC, ASYNC and OFF - the latter if the Cassandra table is guaranteed to exist already, for a faster initialization.

  * **skip\_provisioning** \(_bool_\)

Note

The session and keyspace parameters, when left out \(or passed as None\), fall back to the globally-available cassio settings if any are available. In other words, if a previously-run ‘cassio.init\(…\)’ has been executed previously anywhere in the code, Cassandra-based objects need not specify the connection parameters at all.

Methods

`__init__`\(\[session, keyspace, table\_name, ...\]\) |    ---|---   `aclear`\(\*\*kwargs\) | Clear cache.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache.   `delete`\(prompt, llm\_string\) | Evict from cache if there's an entry.   `delete_through_llm`\(prompt, llm\[, stop\]\) | A wrapper around delete with the LLM being passed.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _session : CassandraSession | None = None_,     _keyspace : str | None = None_,     _table\_name : str = 'langchain\_llm\_cache'_,     _ttl\_seconds : int | None = None_,     _skip\_provisioning : bool = False_,     _setup\_mode : CassandraSetupMode = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.__init__)\#     

Parameters:     

  * **session** \(_Optional_ _\[__CassandraSession_ _\]_\)

  * **keyspace** \(_Optional_ _\[__str_ _\]_\)

  * **table\_name** \(_str_\)

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\)

  * **skip\_provisioning** \(_bool_\)

  * **setup\_mode** \(_CassandraSetupMode_\)

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.aclear)\#     

Clear cache. This is for all LLMs at once.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.alookup)\#     

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

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.clear)\#     

Clear cache. This is for all LLMs at once.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

delete\(_prompt : str_, _llm\_string : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.delete)\#     

Evict from cache if there’s an entry.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

None

delete\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.delete_through_llm)\#     

A wrapper around delete with the LLM being passed. In case the llm.invoke\(prompt\) calls have a stop param, you should pass it here

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.lookup)\#     

Look up based on prompt and llm\_string.

A cache implementation is expected to generate a key from the 2-tuple of prompt and llm\_string \(e.g., by concatenating them with a delimiter\).

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

Returns:     

On a cache miss, return None. On a cache hit, return the cached value. The cached value is a list of Generations \(or subclasses\).

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraCache.update)\#     

Update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the lookup method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

Examples using CassandraCache

  * [Cassandra](https://python.langchain.com/docs/integrations/providers/cassandra/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page