# UsageMetadata — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html
**Word Count:** 91
**Links Count:** 161
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# UsageMetadata\#

_class _langchain\_core.messages.ai.UsageMetadata[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#UsageMetadata)\#     

Usage metadata for a message, such as token counts.

This is a standard representation of token usage that is consistent across models.

Example               {         "input_tokens": 350,         "output_tokens": 240,         "total_tokens": 590,         "input_token_details": {             "audio": 10,             "cache_creation": 200,             "cache_read": 100,         },         "output_token_details": {             "audio": 10,             "reasoning": 200,         }     }     

Changed in version 0.3.9: Added `input_token_details` and `output_token_details`.

input\_tokens _: int_\#     

Count of input \(or prompt\) tokens. Sum of all input token types.

output\_tokens _: int_\#     

Count of output \(or completion\) tokens. Sum of all output token types.

total\_tokens _: int_\#     

Total token count. Sum of input\_tokens + output\_tokens.

input\_token\_details _: NotRequired\[[InputTokenDetails](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.InputTokenDetails.html#langchain_core.messages.ai.InputTokenDetails "langchain_core.messages.ai.InputTokenDetails")\]_\#     

Breakdown of input token counts.

Does _not_ need to sum to full input token count. Does _not_ need to have all keys.

output\_token\_details _: NotRequired\[[OutputTokenDetails](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.OutputTokenDetails.html#langchain_core.messages.ai.OutputTokenDetails "langchain_core.messages.ai.OutputTokenDetails")\]_\#     

Breakdown of output token counts.

Does _not_ need to sum to full output token count. Does _not_ need to have all keys.

__On this page