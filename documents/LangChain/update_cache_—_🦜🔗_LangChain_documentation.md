# update_cache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.update_cache.html
**Word Count:** 52
**Links Count:** 124
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# update\_cache\#

langchain\_core.language\_models.llms.update\_cache\(

    _cache : [BaseCache](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") | bool | None_,     _existing\_prompts : dict\[int, list\]_,     _llm\_string : str_,     _missing\_prompt\_idxs : list\[int\]_,     _new\_results : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _prompts : list\[str\]_, \) → dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/language_models/llms.html#update_cache)\#     

Update the cache and get the LLM output.

Parameters:     

  * **cache** \([_BaseCache_](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") _|__bool_ _|__None_\) – Cache object.

  * **existing\_prompts** \(_dict_ _\[__int_ _,__list_ _\]_\) – Dictionary of existing prompts.

  * **llm\_string** \(_str_\) – LLM string.

  * **missing\_prompt\_idxs** \(_list_ _\[__int_ _\]_\) – List of missing prompt indexes.

  * **new\_results** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\) – LLMResult object.

  * **prompts** \(_list_ _\[__str_ _\]_\) – List of prompts.

Returns:     

LLM output.

Raises:     

**ValueError** – If the cache is not set and cache is True.

Return type:     

dict | None

__On this page