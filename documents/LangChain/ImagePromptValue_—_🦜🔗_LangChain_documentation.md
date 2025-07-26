# ImagePromptValue — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ImagePromptValue.html
**Word Count:** 22
**Links Count:** 118
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# ImagePromptValue\#

_class _langchain\_core.prompt\_values.ImagePromptValue[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ImagePromptValue)\#     

Bases: [`PromptValue`](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue")

Image prompt value.

_param _image\_url _: [ImageURL](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.ImageURL.html#langchain_core.prompt_values.ImageURL "langchain_core.prompt_values.ImageURL")_ _\[Required\]_\#     

Image URL.

_param _type _: Literal\['ImagePromptValue'\]__ = 'ImagePromptValue'_\#     

to\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ImagePromptValue.to_messages)\#     

Return prompt \(image URL\) as messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

to\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompt_values.html#ImagePromptValue.to_string)\#     

Return prompt \(image URL\) as string.

Return type:     

str

__On this page