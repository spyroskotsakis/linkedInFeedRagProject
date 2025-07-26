# BaseMessagePromptTemplate — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html
**Word Count:** 69
**Links Count:** 147
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# BaseMessagePromptTemplate\#

_class _langchain\_core.prompts.message.BaseMessagePromptTemplate[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/message.html#BaseMessagePromptTemplate)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable"), `ABC`

Base class for message prompt templates.

_async _aformat\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/message.html#BaseMessagePromptTemplate.aformat_messages)\#     

Async format messages from kwargs.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

List of BaseMessages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_abstractmethod _format\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/message.html#BaseMessagePromptTemplate.format_messages)\#     

Format messages from kwargs. Should return a list of BaseMessages.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

List of BaseMessages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

pretty\_print\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/message.html#BaseMessagePromptTemplate.pretty_print)\#     

Print a human-readable representation.

Return type:     

None

pretty\_repr\(

    _html : bool = False_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/message.html#BaseMessagePromptTemplate.pretty_repr)\#     

Human-readable representation.

Parameters:     

**html** \(_bool_\) – Whether to format as HTML. Defaults to False.

Returns:     

Human-readable representation.

Return type:     

str

_abstract property _input\_variables _: list\[str\]_\#     

Input variables for this prompt template.

Returns:     

List of input variables.

__On this page