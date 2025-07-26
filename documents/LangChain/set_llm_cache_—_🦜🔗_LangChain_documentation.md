# set_llm_cache — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/globals/langchain_core.globals.set_llm_cache.html
**Word Count:** 45
**Links Count:** 116
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# set\_llm\_cache\#

langchain\_core.globals.set\_llm\_cache\(_value : [BaseCache](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") | None_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/globals.html#set_llm_cache)\#     

Set a new LLM cache, overwriting the previous value, if any.

Parameters:     

**value** \([_BaseCache_](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache") _|__None_\) – The new LLM cache to use. If None, the LLM cache is disabled.

Return type:     

None

Examples using set\_llm\_cache

  * [Astra DB](https://python.langchain.com/docs/integrations/providers/astradb/)

  * [Cassandra](https://python.langchain.com/docs/integrations/providers/cassandra/)

  * [Couchbase](https://python.langchain.com/docs/integrations/providers/couchbase/)

  * [DSPy](https://python.langchain.com/docs/integrations/providers/dspy/)

  * [How to cache LLM responses](https://python.langchain.com/docs/how_to/llm_caching/)

  * [How to cache chat model responses](https://python.langchain.com/docs/how_to/chat_model_caching/)

  * [Model caches](https://python.langchain.com/docs/integrations/llm_caching/)

  * [Momento](https://python.langchain.com/docs/integrations/providers/momento/)

  * [MongoDB Atlas](https://python.langchain.com/docs/integrations/providers/mongodb_atlas/)

  * [Redis](https://python.langchain.com/docs/integrations/providers/redis/)

__On this page