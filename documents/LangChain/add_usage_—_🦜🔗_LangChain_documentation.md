# add_usage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.add_usage.html
**Word Count:** 13
**Links Count:** 155
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# add\_usage\#

langchain\_core.messages.ai.add\_usage\(

    _left : [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") | None_,     _right : [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") | None_, \) → [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#add_usage)\#     

Recursively add two UsageMetadata objects.

Example               from langchain_core.messages.ai import add_usage          left = UsageMetadata(         input_tokens=5,         output_tokens=0,         total_tokens=5,         input_token_details=InputTokenDetails(cache_read=3)     )     right = UsageMetadata(         input_tokens=0,         output_tokens=10,         total_tokens=10,         output_token_details=OutputTokenDetails(reasoning=4)     )          add_usage(left, right)     

results in               UsageMetadata(         input_tokens=5,         output_tokens=10,         total_tokens=15,         input_token_details=InputTokenDetails(cache_read=3),         output_token_details=OutputTokenDetails(reasoning=4)     )     

Parameters:     

  * **left** \([_UsageMetadata_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") _|__None_\)

  * **right** \([_UsageMetadata_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") _|__None_\)

Return type:     

[_UsageMetadata_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata")

__On this page