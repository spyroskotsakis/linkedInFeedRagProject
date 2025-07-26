# StringPromptValue — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.StringPromptValue.html
**Word Count:** 18
**Links Count:** 117
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# StringPromptValue\#

_class _langchain\_core.prompt\_values.StringPromptValue[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#StringPromptValue)\#     

Bases: [`PromptValue`](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

String prompt value.

_param _text _: str_ _\[Required\]_\#     

Prompt text.

_param _type _: Literal\['StringPromptValue'\]__ = 'StringPromptValue'_\#     

to\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#StringPromptValue.to_messages)\#     

Return prompt as messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

to\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#StringPromptValue.to_string)\#     

Return prompt as string.

Return type:     

str

__On this page