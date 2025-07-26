# PromptValue — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html
**Word Count:** 39
**Links Count:** 113
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# PromptValue\#

_class _langchain\_core.prompt\_values.PromptValue[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#PromptValue)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable"), `ABC`

Base abstract class for inputs to any language model.

PromptValues can be converted to both LLM \(pure text-generation\) inputs and ChatModel inputs.

_abstractmethod _to\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#PromptValue.to_messages)\#     

Return prompt as a list of Messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_abstractmethod _to\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#PromptValue.to_string)\#     

Return prompt value as string.

Return type:     

str

__On this page