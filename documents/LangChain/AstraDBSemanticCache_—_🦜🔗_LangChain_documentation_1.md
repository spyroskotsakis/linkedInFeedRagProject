# AstraDBSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.AstraDBSemanticCache.html
**Word Count:** 1124
**Links Count:** 197
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# AstraDBSemanticCache\#

_class _langchain\_community.cache.AstraDBSemanticCache\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_semantic\_cache'_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : [AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") | None = None_,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _namespace : str | None = None_,     _setup\_mode : AstraSetupMode = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metric : str | None = None_,     _similarity\_threshold : float = 0.85_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache)\#     

Deprecated since version 0.0.28: Use `:class:`~langchain_astradb.AstraDBSemanticCache`` instead. It will not be removed until langchain-community==1.0.

Cache that uses Astra DB as a vector-store backend for semantic \(i.e. similarity-based\) lookup.

It uses a single \(vector\) collection and can store cached values from several LLMs, so the LLM’s ‘llm\_string’ is stored in the document metadata.

You can choose the preferred similarity \(or use the API default\). The default score threshold is tuned to the default metric. Tune it carefully yourself if switching to another distance metric.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **setup\_mode** \(_AstraSetupMode_\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding provider for semantic encoding and search.

  * **metric** \(_Optional_ _\[__str_ _\]_\) – the function to use for evaluating similarity of text embeddings. Defaults to ‘cosine’ \(alternatives: ‘euclidean’, ‘dot\_product’\)

  * **similarity\_threshold** \(_float_\) – the minimum similarity for accepting a \(semantic-search\) match.

Methods

`__init__`\(\*\[, collection\_name, token, ...\]\) | Cache that uses Astra DB as a vector-store backend for semantic \(i.e. similarity-based\) lookup.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `adelete_by_document_id`\(document\_id\) | Given this is a "similarity search" cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `alookup_with_id`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `alookup_with_id_through_llm`\(prompt, llm\[, stop\]\) |    `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache that can take additional keyword arguments.   `delete_by_document_id`\(document\_id\) | Given this is a "similarity search" cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `lookup_with_id`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `lookup_with_id_through_llm`\(prompt, llm\[, stop\]\) |    `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_semantic\_cache'_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : [AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") | None = None_,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _namespace : str | None = None_,     _setup\_mode : AstraSetupMode = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metric : str | None = None_,     _similarity\_threshold : float = 0.85_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.__init__)\#     

Cache that uses Astra DB as a vector-store backend for semantic \(i.e. similarity-based\) lookup.

It uses a single \(vector\) collection and can store cached values from several LLMs, so the LLM’s ‘llm\_string’ is stored in the document metadata.

You can choose the preferred similarity \(or use the API default\). The default score threshold is tuned to the default metric. Tune it carefully yourself if switching to another distance metric.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **setup\_mode** \(_AstraSetupMode_\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding provider for semantic encoding and search.

  * **metric** \(_Optional_ _\[__str_ _\]_\) – the function to use for evaluating similarity of text embeddings. Defaults to ‘cosine’ \(alternatives: ‘euclidean’, ‘dot\_product’\)

  * **similarity\_threshold** \(_float_\) – the minimum similarity for accepting a \(semantic-search\) match.

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.aclear)\#     

Async clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _adelete\_by\_document\_id\(

    _document\_id : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.adelete_by_document_id)\#     

Given this is a “similarity search” cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID. This is for the second step.

Parameters:     

**document\_id** \(_str_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.alookup)\#     

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

    _prompt : str_,     _llm\_string : str_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.alookup_with_id)\#     

Look up based on prompt and llm\_string. If there are hits, return \(document\_id, cached\_entry\) for the top hit

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

_async _alookup\_with\_id\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.alookup_with_id_through_llm)\#     

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

_async _aupdate\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.clear)\#     

Clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

delete\_by\_document\_id\(

    _document\_id : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.delete_by_document_id)\#     

Given this is a “similarity search” cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID. This is for the second step.

Parameters:     

**document\_id** \(_str_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.lookup)\#     

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

    _prompt : str_,     _llm\_string : str_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.lookup_with_id)\#     

Look up based on prompt and llm\_string. If there are hits, return \(document\_id, cached\_entry\) for the top hit

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

lookup\_with\_id\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → Tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.lookup_with_id_through_llm)\#     

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_Tuple_\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the lookup method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)