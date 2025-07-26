# AstraDBCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cache/langchain_community.cache.AstraDBCache.html
**Word Count:** 900
**Links Count:** 177
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# AstraDBCache\#

_class _langchain\_community.cache.AstraDBCache\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_cache'_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : [AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") | None = None_,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _namespace : str | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : AstraSetupMode = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache)\#     

Deprecated since version 0.0.28: Use `:class:`~langchain_astradb.AstraDBCache`` instead. It will not be removed until langchain-community==1.0.

Cache that uses Astra DB as a backend.

It uses a single collection as a kv store The lookup keys, combined in the \_id of the documents, are:

>   * prompt, a string >  >   * llm\_string, a deterministic str representation of the model parameters. \(needed to prevent same-prompt-different-model collisions\) >  > 

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **setup\_mode** \(_AstraSetupMode_\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

Methods

`__init__`\(\*\[, collection\_name, token, ...\]\) | Cache that uses Astra DB as a backend.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `adelete`\(prompt, llm\_string\) | Evict from cache if there's an entry.   `adelete_through_llm`\(prompt, llm\[, stop\]\) | A wrapper around adelete with the LLM being passed.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `clear`\(\*\*kwargs\) | Clear cache that can take additional keyword arguments.   `delete`\(prompt, llm\_string\) | Evict from cache if there's an entry.   `delete_through_llm`\(prompt, llm\[, stop\]\) | A wrapper around delete with the LLM being passed.   `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update cache based on prompt and llm\_string.      \_\_init\_\_\(

    _\*_ ,     _collection\_name : str = 'langchain\_astradb\_cache'_,     _token : str | None = None_,     _api\_endpoint : str | None = None_,     _astra\_db\_client : [AstraDB](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") | None = None_,     _async\_astra\_db\_client : AsyncAstraDB | None = None_,     _namespace : str | None = None_,     _pre\_delete\_collection : bool = False_,     _setup\_mode : AstraSetupMode = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.__init__)\#     

Cache that uses Astra DB as a backend.

It uses a single collection as a kv store The lookup keys, combined in the \_id of the documents, are:

>   * prompt, a string >  >   * llm\_string, a deterministic str representation of the model parameters. \(needed to prevent same-prompt-different-model collisions\) >  > 

Parameters:     

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_Optional_ _\[__str_ _\]_\) – API token for Astra DB usage.

  * **api\_endpoint** \(_Optional_ _\[__str_ _\]_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com.

  * **astra\_db\_client** \(_Optional_ _\[_[_AstraDB_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.astradb.AstraDB.html#langchain_community.vectorstores.astradb.AstraDB "langchain_community.vectorstores.astradb.AstraDB") _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AstraDB’ instance.

  * **async\_astra\_db\_client** \(_Optional_ _\[__AsyncAstraDB_ _\]_\) – _alternative to token+api\_endpoint_ , you can pass an already-created ‘astrapy.db.AsyncAstraDB’ instance.

  * **namespace** \(_Optional_ _\[__str_ _\]_\) – namespace \(aka keyspace\) where the collection is created. Defaults to the database’s “default namespace”.

  * **setup\_mode** \(_AstraSetupMode_\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

_async _aclear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.aclear)\#     

Async clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _adelete\(_prompt : str_, _llm\_string : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.adelete)\#     

Evict from cache if there’s an entry.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

None

_async _adelete\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.adelete_through_llm)\#     

A wrapper around adelete with the LLM being passed. In case the llm.invoke\(prompt\) calls have a stop param, you should pass it here

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

None

_async _alookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.alookup)\#     

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

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.aupdate)\#     

Async update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the look up method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.clear)\#     

Clear cache that can take additional keyword arguments.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

delete\(_prompt : str_, _llm\_string : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.delete)\#     

Evict from cache if there’s an entry.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

None

delete\_through\_llm\(

    _prompt : str_,     _llm : [LLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")_,     _stop : List\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.delete_through_llm)\#     

A wrapper around delete with the LLM being passed. In case the llm.invoke\(prompt\) calls have a stop param, you should pass it here

Parameters:     

  * **prompt** \(_str_\)

  * **llm** \([_LLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.LLM.html#langchain_core.language_models.llms.LLM "langchain_core.language_models.llms.LLM")\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

None

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.lookup)\#     

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

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cache.html#AstraDBCache.update)\#     

Update cache based on prompt and llm\_string.

The prompt and llm\_string are used to generate a key for the cache. The key should match that of the lookup method.

Parameters:     

  * **prompt** \(_str_\) – a string representation of the prompt. In the case of a Chat model, the prompt is a non-trivial serialization of the prompt into the language model.

  * **llm\_string** \(_str_\) – A string representation of the LLM configuration. This is used to capture the invocation parameters of the LLM \(e.g., model name, temperature, stop tokens, max tokens, etc.\). These invocation parameters are serialized into a string representation.

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\) – The value to be cached. The value is a list of Generations \(or subclasses\).

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)