# get_prompts — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.get_prompts.html
**Word Count:** 51
**Links Count:** 122
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# get\_prompts\#

langchain\_core.language\_models.llms.get\_prompts\(

    _params : dict\[str, Any\]_,     _prompts : list\[str\]_,     _cache : [BaseCache](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") | bool | None = None_, \) → tuple\[dict\[int, list\], str, list\[int\], list\[str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/language_models/llms.html#get_prompts)\#     

Get prompts that are already cached.

Parameters:     

  * **params** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Dictionary of parameters.

  * **prompts** \(_list_ _\[__str_ _\]_\) – List of prompts.

  * **cache** \([_BaseCache_](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") _|__bool_ _|__None_\) – Cache object. Default is None.

Returns:     

A tuple of existing prompts, llm\_string, missing prompt indexes,     

and missing prompts.

Raises:     

**ValueError** – If the cache is not set and cache is True.

Return type:     

tuple\[dict\[int, list\], str, list\[int\], list\[str\]\]

__On this page