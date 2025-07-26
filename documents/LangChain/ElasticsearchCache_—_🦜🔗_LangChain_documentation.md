# ElasticsearchCache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/cache/langchain_elasticsearch.cache.ElasticsearchCache.html
**Word Count:** 708
**Links Count:** 120
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# ElasticsearchCache\#

_class _langchain\_elasticsearch.cache.ElasticsearchCache\(

    _index\_name : str_,     _store\_input : bool = True_,     _store\_input\_params : bool = True_,     _metadata : Dict\[str, Any\] | None = None_,     _\*_ ,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _es\_params : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/cache.html#ElasticsearchCache)\#     

Initialize the Elasticsearch cache store by specifying the index/alias to use and determining which additional information \(like input, input parameters, and any other metadata\) should be stored in the cache.

Parameters:     

  * **index\_name** \(_str_\) – The name of the index or the alias to use for the cache. If they do not exist an index is created, according to the default mapping defined by the mapping property.

  * **store\_input** \(_bool_\) – Whether to store the LLM input in the cache, i.e., the input prompt. Default to True.

  * **store\_input\_params** \(_bool_\) – Whether to store the input parameters in the cache, i.e., the LLM parameters used to generate the LLM response. Default to True.

  * **metadata** \(_Optional_ _\[__dict_ _\]_\) – Additional metadata to store in the cache, for filtering purposes. This must be JSON serializable in an Elasticsearch document. Default to None.

  * **es\_url** \(_str_ _|__None_\) – URL of the Elasticsearch instance to connect to.

  * **es\_cloud\_id** \(_str_ _|__None_\) – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** \(_str_ _|__None_\) – Username to use when connecting to Elasticsearch.

  * **es\_password** \(_str_ _|__None_\) – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** \(_str_ _|__None_\) – API key to use when connecting to Elasticsearch.

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Other parameters for the Elasticsearch client.

Attributes

`mapping` | Get the default mapping for the index.   ---|---      Methods

`__init__`\(index\_name\[, store\_input, ...\]\) | Initialize the Elasticsearch cache store by specifying the index/alias to use and determining which additional information \(like input, input parameters, and any other metadata\) should be stored in the cache.   ---|---   `aclear`\(\*\*kwargs\) | Async clear cache that can take additional keyword arguments.   `alookup`\(prompt, llm\_string\) | Async look up based on prompt and llm\_string.   `aupdate`\(prompt, llm\_string, return\_val\) | Async update cache based on prompt and llm\_string.   `build_document`\(prompt, llm\_string, return\_val\) | Build the Elasticsearch document for storing a single LLM interaction   `clear`\(\*\*kwargs\) | Clear cache.   `is_alias`\(\) |    `lookup`\(prompt, llm\_string\) | Look up based on prompt and llm\_string.   `update`\(prompt, llm\_string, return\_val\) | Update based on prompt and llm\_string.      \_\_init\_\_\(

    _index\_name : str_,     _store\_input : bool = True_,     _store\_input\_params : bool = True_,     _metadata : Dict\[str, Any\] | None = None_,     _\*_ ,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _es\_params : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/cache.html#ElasticsearchCache.__init__)\#     

Initialize the Elasticsearch cache store by specifying the index/alias to use and determining which additional information \(like input, input parameters, and any other metadata\) should be stored in the cache.

Parameters:     

  * **index\_name** \(_str_\) – The name of the index or the alias to use for the cache. If they do not exist an index is created, according to the default mapping defined by the mapping property.

  * **store\_input** \(_bool_\) – Whether to store the LLM input in the cache, i.e., the input prompt. Default to True.

  * **store\_input\_params** \(_bool_\) – Whether to store the input parameters in the cache, i.e., the LLM parameters used to generate the LLM response. Default to True.

  * **metadata** \(_Optional_ _\[__dict_ _\]_\) – Additional metadata to store in the cache, for filtering purposes. This must be JSON serializable in an Elasticsearch document. Default to None.

  * **es\_url** \(_str_ _|__None_\) – URL of the Elasticsearch instance to connect to.

  * **es\_cloud\_id** \(_str_ _|__None_\) – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** \(_str_ _|__None_\) – Username to use when connecting to Elasticsearch.

  * **es\_password** \(_str_ _|__None_\) – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** \(_str_ _|__None_\) – API key to use when connecting to Elasticsearch.

  * **es\_params** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Other parameters for the Elasticsearch client.

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

build\_document\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/cache.html#ElasticsearchCache.build_document)\#     

Build the Elasticsearch document for storing a single LLM interaction

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

_Dict_\[str, _Any_\]

clear\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/cache.html#ElasticsearchCache.clear)\#     

Clear cache.

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

is\_alias\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/cache.html#ElasticsearchCache.is_alias)\#     

Return type:     

bool

lookup\(

    _prompt : str_,     _llm\_string : str_, \) → Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/cache.html#ElasticsearchCache.lookup)\#     

Look up based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

Return type:     

_Sequence_\[[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\] | None

update\(

    _prompt : str_,     _llm\_string : str_,     _return\_val : Sequence\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_sync/cache.html#ElasticsearchCache.update)\#     

Update based on prompt and llm\_string.

Parameters:     

  * **prompt** \(_str_\)

  * **llm\_string** \(_str_\)

  * **return\_val** \(_Sequence_ _\[_[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") _\]_\)

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)