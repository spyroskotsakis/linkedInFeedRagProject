# caches — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/caches.html
**Word Count:** 92
**Links Count:** 98
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# `caches`\#

Cache classes.

Warning

Beta Feature\!

**Cache** provides an optional caching layer for LLMs.

Cache is useful for two reasons:

  * It can save you money by reducing the number of API calls you make to the LLM provider if you’re often requesting the same completion multiple times.

  * It can speed up your application by reducing the number of API calls you make to the LLM provider.

Cache directly competes with Memory. See documentation for Pros and Cons.

**Class hierarchy:**               BaseCache --> <name>Cache  # Examples: InMemoryCache, RedisCache, GPTCache     

**Classes**

[`caches.BaseCache`](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.BaseCache.html#langchain_core.caches.BaseCache "langchain_core.caches.BaseCache")\(\) | Interface for a caching layer for LLMs and Chat models.   ---|---   [`caches.InMemoryCache`](https://python.langchain.com/api_reference/core/caches/langchain_core.caches.InMemoryCache.html#langchain_core.caches.InMemoryCache "langchain_core.caches.InMemoryCache")\(\*\[, maxsize\]\) | Cache that stores things in memory.