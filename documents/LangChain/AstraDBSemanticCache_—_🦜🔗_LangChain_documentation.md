# AstraDBSemanticCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/cache/langchain_astradb.cache.AstraDBSemanticCache.html
**Word Count:** 1416
**Links Count:** 151
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBSemanticCache\#

_class _langchain\_astradb.cache.AstraDBSemanticCache\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_semantic\_cache'_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metric : str | None = None_,     _similarity\_threshold : float = 0.85_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache)\#     

Astra DB semantic cache.

Cache that uses Astra DB as a vector-store backend for semantic \(i.e. similarity-based\) lookup.

It uses a single \(vector\) collection and can store cached values from several LLMs, so the LLM’s ‘llm\_string’ is stored in the document metadata.

You can choose the preferred similarity \(or use the API default\). The default score threshold is tuned to the default metric. Tune it carefully yourself if switching to another distance metric.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding provider for semantic encoding and search.

  * **metric** \(_str_ _|__None_\) – the function to use for evaluating similarity of text embeddings. Defaults to ‘cosine’ \(alternatives: ‘euclidean’, ‘dot\_product’\)

  * **similarity\_threshold** \(_float_\) – the minimum similarity for accepting a \(semantic-search\) match.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Methods

`__init__`\(\*\[, collection\_name, token, ...\]\) | Astra DB semantic cache.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `adelete_by_document_id`\(document\_id\) | Delete by document ID.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `alookup_with_id`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `alookup_with_id_through_llm`\(prompt, llm\[, stop\]\) | Look up based on prompt and LLM.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache that can take additional keyword arguments.   `delete_by_document_id`\(document\_id\) | Delete by document ID.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `lookup_with_id`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `lookup_with_id_through_llm`\(prompt, llm\[, stop\]\) | Look up based on prompt and LLM.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_semantic\_cache'_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_,     _embedding : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _metric : str | None = None_,     _similarity\_threshold : float = 0.85_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.__init__)\#     

Astra DB semantic cache.

Cache that uses Astra DB as a vector-store backend for semantic \(i.e. similarity-based\) lookup.

It uses a single \(vector\) collection and can store cached values from several LLMs, so the LLM’s ‘llm\_string’ is stored in the document metadata.

You can choose the preferred similarity \(or use the API default\). The default score threshold is tuned to the default metric. Tune it carefully yourself if switching to another distance metric.

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **embedding** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embedding provider for semantic encoding and search.

  * **metric** \(_str_ _|__None_\) – the function to use for evaluating similarity of text embeddings. Defaults to ‘cosine’ \(alternatives: ‘euclidean’, ‘dot\_product’\)

  * **similarity\_threshold** \(_float_\) – the minimum similarity for accepting a \(semantic-search\) match.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.aclear)\#     

Async clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _adelete\_by\_document\_id\(

    _document\_id : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.adelete_by_document_id)\#     

Delete by document ID.

Given this is a “similarity search” cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID. This is for the second step.

Parameters:     

**document\_id** \(_str_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.alookup)\#     

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

    _prompt : str_,     _llm\_string : str_, \) → tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.alookup_with_id)\#     

Look up based on prompt and llm\_string.

If there are hits, return \(document\_id, cached\_entry\) for the top hit

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

tuple\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

_async _alookup\_with\_id\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : list\[str\] | None = None_, \) → tuple\[str, RETURN\_VAL\_TYPE\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.alookup_with_id_through_llm)\#     

Look up based on prompt and LLM.

If there are hits, return \(document\_id, cached\_entry\) for the top hit

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_list_ _\[__str_ _\]__|__None_\)

Return type:     

tuple\[str, RETURN\_VAL\_TYPE\] | None

_async _aupdate\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.clear)\#     

Clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

delete\_by\_document\_id\(

    _document\_id : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.delete_by_document_id)\#     

Delete by document ID.

Given this is a “similarity search” cache, an invalidation pattern that makes sense is first a lookup to get an ID, and then deleting with that ID. This is for the second step.

Parameters:     

**document\_id** \(_str_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.lookup)\#     

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

    _prompt : str_,     _llm\_string : str_, \) → tuple\[str, Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.lookup_with_id)\#     

Look up based on prompt and llm\_string.

If there are hits, return \(document\_id, cached\_entry\) for the top hit

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

tuple\[str, _Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]\] | None

lookup\_with\_id\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : list\[str\] | None = None_, \) → tuple\[str, RETURN\_VAL\_TYPE\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.lookup_with_id_through_llm)\#     

Look up based on prompt and LLM.

If there are hits, return \(document\_id, cached\_entry\) for the top hit

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_list_ _\[__str_ _\]__|__None_\)

Return type:     

tuple\[str, RETURN\_VAL\_TYPE\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBSemanticCache.update)\#     

Update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the lookup method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)