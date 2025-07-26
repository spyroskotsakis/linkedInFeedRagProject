# subtract_usage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.subtract_usage.html
**Word Count:** 26
**Links Count:** 155
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# subtract\_usage\#

langchain\_core.messages.ai.subtract\_usage\(

    _left : [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") | None_,     _right : [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") | None_, \) → [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#subtract_usage)\#     

Recursively subtract two UsageMetadata objects.

Token counts cannot be negative so the actual operation is max\(left - right, 0\).

Example               from langchain_core.messages.ai import subtract_usage          left = UsageMetadata(         input_tokens=5,         output_tokens=10,         total_tokens=15,         input_token_details=InputTokenDetails(cache_read=4)     )     right = UsageMetadata(         input_tokens=3,         output_tokens=8,         total_tokens=11,         output_token_details=OutputTokenDetails(reasoning=4)     )          subtract_usage(left, right)     

results in               UsageMetadata(         input_tokens=2,         output_tokens=2,         total_tokens=4,         input_token_details=InputTokenDetails(cache_read=4),         output_token_details=OutputTokenDetails(reasoning=0)     )     

Parameters:     

  * **left** \([_UsageMetadata_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") _|__None_\)

  * **right** \([_UsageMetadata_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") _|__None_\)

Return type:     

[_UsageMetadata_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata")

__On this page