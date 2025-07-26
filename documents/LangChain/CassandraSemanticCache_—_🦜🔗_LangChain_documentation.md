# CassandraSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.CassandraSemanticCache.html
**Word Count:** 1003
**Links Count:** 195
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# CassandraSemanticCache\#

_class _langchain\_community.cache.CassandraSemanticCache\(

    _session : CassandraSession | None = None_,     _keyspace : str | None = None_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _table\_name : str = 'langchain\_llm\_semantic\_cache'_,     _distance\_metric : str | None = None_,     _score\_threshold : float = 0.85_,     _ttl\_seconds : int | None = None_,     _skip\_provisioning : bool = False_,     _similarity\_measure : str = 'dot'_,     _setup\_mode : CassandraSetupMode = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache)\#     

Cache that uses Cassandra as a vector-store backend for semantic \(i.e. similarity-based\) lookup.

Example               import cassio          from langchain_community.cache import CassandraSemanticCache     from langchain_core.globals import set_llm_cache          cassio.init(auto=True)  # Requires env. variables, see CassIO docs          my_embedding = ...          set_llm_cache(CassandraSemanticCache(         embedding=my_embedding,         table_name="my_semantic_cache",     ))     

It uses a single \(vector\) Cassandra table and stores, in principle, cached values from several LLMs, so the LLM’s llm\_string is part of the rows’ primary keys.

One can choose a similarity measure \(default: “dot” for dot-product\). Choosing another one \(“cos”, “l2”\) almost certainly requires threshold tuning. \(which may be in order nevertheless, even if sticking to “dot”\).

Parameters:     

  * **session** \(_Optional_ _\[__CassandraSession_ _\]_\) – an open Cassandra session. Leave unspecified to use the global cassio init \(see below\)

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – the keyspace to use for storing the cache. Leave unspecified to use the global cassio init \(see below\)

  * **embedding** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\) – Embedding provider for semantic encoding and search.

  * **table\_name** \(_str_\) – name of the Cassandra \(vector\) table to use as cache. There is a default for “simple” usage, but remember to explicitly specify different tables if several embedding models coexist in your app \(they cannot share one cache table\).

  * **distance\_metric** \(_Optional_ _\[__str_ _\]_\) – an alias for the ‘similarity\_measure’ parameter \(see below\). As the “distance” terminology is misleading, please prefer ‘similarity\_measure’ for clarity.

  * **score\_threshold** \(_float_\) – numeric value to use as cutoff for the similarity searches

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – time-to-live for cache entries \(default: None, i.e. forever\)

  * **similarity\_measure** \(_str_\) – which measure to adopt for similarity searches. Note: this parameter is aliased by ‘distance\_metric’ - however, it is suggested to use the “similarity” terminology since this value is in fact a similarity \(i.e. higher means closer\). Note that at most one of the two parameters ‘distance\_metric’ and ‘similarity\_measure’ can be provided.

  * **setup\_mode** \(_CassandraSetupMode_\) – a value in langchain\_community.utilities.cassandra.SetupMode. Choose between SYNC, ASYNC and OFF - the latter if the Cassandra table is guaranteed to exist already, for a faster initialization.

  * **skip\_provisioning** \(_bool_\)

Note

The session and keyspace parameters, when left out \(or passed as None\), fall back to the globally-available cassio settings if any are available. In other words, if a previously-run ‘cassio.init\(…\)’ has been executed previously anywhere in the code, Cassandra-based objects need not specify the connection parameters at all.

Methods

`__init__`\(\[session, keyspace, embedding, ...\]\) |    ---|---   `aclear`\(\*\*kwargs\) | Clear the _whole_ semantic cache.   `adelete_by_document_id`\(document\_id\) | Given this is a "similarity search" cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `alookup_with_id`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `alookup_with_id_through_llm`\(prompt, llm\[, stop\]\) |    `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear the _whole_ semantic cache.   `delete_by_document_id`\(document\_id\) | Given this is a "similarity search" cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `lookup_with_id`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `lookup_with_id_through_llm`\(prompt, llm\[, stop\]\) |    `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _session : CassandraSession | None = None_,     _keyspace : str | None = None_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None = None_,     _table\_name : str = 'langchain\_llm\_semantic\_cache'_,     _distance\_metric : str | None = None_,     _score\_threshold : float = 0.85_,     _ttl\_seconds : int | None = None_,     _skip\_provisioning : bool = False_,     _similarity\_measure : str = 'dot'_,     _setup\_mode : CassandraSetupMode = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.__init__)\#     

Parameters:     

  * **session** \(_Optional_ _\[__CassandraSession_ _\]_\)

  * **keyspace** \(_Optional_ _\[__str_ _\]_\)

  * **embedding** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\)

  * **table\_name** \(_str_\)

  * **distance\_metric** \(_Optional_ _\[__str_ _\]_\)

  * **score\_threshold** \(_float_\)

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\)

  * **skip\_provisioning** \(_bool_\)

  * **similarity\_measure** \(_str_\)

  * **setup\_mode** \(_CassandraSetupMode_\)

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.aclear)\#     

Clear the _whole_ semantic cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _adelete\_by\_document\_id\(

    _document\_id : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.adelete_by_document_id)\#     

Given this is a “similarity search” cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID. This is for the second step.

Parameters:     

**document\_id** \(_str_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.alookup)\#     

Async look up based on prompt and llm\_string.

A cache implementation is expected to generate a key from the 2-tuple of prompt and llm\_string \(e.g., by concatenating them with a delimiter\).

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

Returns:     

On a cache miss, return None. On a cache hit, return the cached value. The cached value is a list of Generations \(or subclasses\).

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

_async _alookup\_with\_id\(

    _prompt : str_,     _llm\_string : str_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.alookup_with_id)\#     

Look up based on prompt and llm\_string. If there are hits, return \(document\_id, cached\_entry\)

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

_async _alookup\_with\_id\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.alookup_with_id_through_llm)\#     

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

_async _aupdate\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.clear)\#     

Clear the _whole_ semantic cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

delete\_by\_document\_id\(

    _document\_id : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.delete_by_document_id)\#     

Given this is a “similarity search” cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID. This is for the second step.

Parameters:     

**document\_id** \(_str_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.lookup)\#     

Look up based on prompt and llm\_string.

A cache implementation is expected to generate a key from the 2-tuple of prompt and llm\_string \(e.g., by concatenating them with a delimiter\).

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

Returns:     

On a cache miss, return None. On a cache hit, return the cached value. The cached value is a list of Generations \(or subclasses\).

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

lookup\_with\_id\(

    _prompt : str_,     _llm\_string : str_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.lookup_with_id)\#     

Look up based on prompt and llm\_string. If there are hits, return \(document\_id, cached\_entry\)

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

lookup\_with\_id\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.lookup_with_id_through_llm)\#     

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#CassandraSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the lookup method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

Examples using CassandraSemanticCache

  * [Cassandra](https://python.langchain.com/docs/integrations/providers/cassandra/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

__On this page