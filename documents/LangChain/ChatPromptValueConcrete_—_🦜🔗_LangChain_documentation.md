# ChatPromptValueConcrete — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValueConcrete.html
**Word Count:** 35
**Links Count:** 115
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# ChatPromptValueConcrete\#

_class _langchain\_core.prompt\_values.ChatPromptValueConcrete[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ChatPromptValueConcrete)\#     

Bases: [`ChatPromptValue`](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html#langchain_core.prompt_values.ChatPromptValue "langchain_core.prompt_values.ChatPromptValue")

Chat prompt value which explicitly lists out the message types it accepts.

For use in external schemas.

_param _messages _: Sequence\[AnyMessage\]__\[Required\]_\#     

Sequence of messages.

_param _type _: Literal\['ChatPromptValueConcrete'\]__ = 'ChatPromptValueConcrete'_\#     

to\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Return prompt as a list of messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

to\_string\(\) → str\#     

Return prompt as string.

Return type:     

str

__On this page