# InputTokenDetails — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.InputTokenDetails.html
**Word Count:** 90
**Links Count:** 155
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# InputTokenDetails\#

_class _langchain\_core.messages.ai.InputTokenDetails[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#InputTokenDetails)\#     

Breakdown of input token counts.

Does _not_ need to sum to full input token count. Does _not_ need to have all keys.

Example               {         "audio": 10,         "cache_creation": 200,         "cache_read": 100,     }     

Added in version 0.3.9.

May also hold extra provider-specific keys.

audio _: int_\#     

Audio input tokens.

cache\_creation _: int_\#     

Input tokens that were cached and there was a cache miss.

Since there was a cache miss, the cache was created from these tokens.

cache\_read _: int_\#     

Input tokens that were cached and there was a cache hit.

Since there was a cache hit, the tokens were read from the cache. More precisely, the model state given these tokens was read from the cache.

__On this page