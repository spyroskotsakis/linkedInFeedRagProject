# AstraDBCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/cache/langchain_astradb.cache.AstraDBCache.html
**Word Count:** 1190
**Links Count:** 135
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBCache\#

_class _langchain\_astradb.cache.AstraDBCache\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_cache'_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache)\#     

Cache that uses Astra DB as a backend.

It uses a single collection as a kv store The lookup keys, combined in the \_id of the documents, are:

>   * prompt, a string >  >   * llm\_string, a deterministic str representation of the model parameters. \(needed to prevent same-prompt-different-model collisions\) >  > 

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Methods

`__init__`\(\*\[, collection\_name, token, ...\]\) | Cache that uses Astra DB as a backend.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `adelete`\(prompt, llm\_string\) | Evict from cache if there's an entry.   `adelete_through_llm`\(prompt, llm\[, stop\]\) | A wrapper around adelete with the LLM being passed.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache that can take additional keyword arguments.   `delete`\(prompt, llm\_string\) | Evict from cache if there's an entry.   `delete_through_llm`\(prompt, llm\[, stop\]\) | A wrapper around delete with the LLM being passed.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_cache'_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.__init__)\#     

Cache that uses Astra DB as a backend.

It uses a single collection as a kv store The lookup keys, combined in the \_id of the documents, are:

>   * prompt, a string >  >   * llm\_string, a deterministic str representation of the model parameters. \(needed to prevent same-prompt-different-model collisions\) >  > 

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.aclear)\#     

Async clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _adelete\(_prompt : str_, _llm\_string : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.adelete)\#     

Evict from cache if there’s an entry.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

None

_async _adelete\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : list\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.adelete_through_llm)\#     

A wrapper around adelete with the LLM being passed.

In case the llm\(prompt\) calls have a stop param, you should pass it here.

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_list_ _\[__str_ _\]__|__None_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.alookup)\#     

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

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.clear)\#     

Clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

delete\(_prompt : str_, _llm\_string : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.delete)\#     

Evict from cache if there’s an entry.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

None

delete\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : list\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.delete_through_llm)\#     

A wrapper around delete with the LLM being passed.

In case the llm\(prompt\) calls have a stop param, you should pass it here.

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_list_ _\[__str_ _\]__|__None_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.lookup)\#     

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

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/cache.html#AstraDBCache.update)\#     

Update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the lookup method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)