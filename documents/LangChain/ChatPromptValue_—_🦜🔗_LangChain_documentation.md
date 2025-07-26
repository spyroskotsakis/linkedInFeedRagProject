# ChatPromptValue — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ChatPromptValue.html
**Word Count:** 32
**Links Count:** 116
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# ChatPromptValue\#

_class _langchain\_core.prompt\_values.ChatPromptValue[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ChatPromptValue)\#     

Bases: [`PromptValue`](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

Chat prompt value.

A type of a prompt value that is built from messages.

_param _messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]__\[Required\]_\#     

List of messages.

to\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ChatPromptValue.to_messages)\#     

Return prompt as a list of messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

to\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ChatPromptValue.to_string)\#     

Return prompt as string.

Return type:     

str

__On this page