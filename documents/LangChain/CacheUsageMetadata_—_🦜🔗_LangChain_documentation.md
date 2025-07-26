# CacheUsageMetadata — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/model_garden/langchain_google_vertexai.model_garden.CacheUsageMetadata.html
**Word Count:** 25
**Links Count:** 99
**Scraped:** 2025-07-21 08:27:18
**Status:** completed

---

# CacheUsageMetadata\#

_class _langchain\_google\_vertexai.model\_garden.CacheUsageMetadata[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/model_garden.html#CacheUsageMetadata)\#     

input\_tokens _: int_\#     

output\_tokens _: int_\#     

total\_tokens _: int_\#     

input\_token\_details _: NotRequired\[[InputTokenDetails](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.InputTokenDetails.html#langchain_core.messages.ai.InputTokenDetails "langchain_core.messages.ai.InputTokenDetails")\]_\#     

output\_token\_details _: NotRequired\[[OutputTokenDetails](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.OutputTokenDetails.html#langchain_core.messages.ai.OutputTokenDetails "langchain_core.messages.ai.OutputTokenDetails")\]_\#     

cache\_creation\_input\_tokens _: int | None_\#     

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens _: int | None_\#     

The number of input tokens read from the cache.

__On this page