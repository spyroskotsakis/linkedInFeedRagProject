# ChatPromptAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.bedrock.ChatPromptAdapter.html
**Word Count:** 27
**Links Count:** 239
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# ChatPromptAdapter\#

_class _langchain\_community.chat\_models.bedrock.ChatPromptAdapter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/bedrock.html#ChatPromptAdapter)\#     

Adapter class to prepare the inputs from Langchain to prompt format that Chat model expects.

Methods

`convert_messages_to_prompt`\(provider, messages\) |    ---|---   `format_messages`\(provider, messages\) |       _classmethod _convert\_messages\_to\_prompt\(

    _provider : str_,     _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/bedrock.html#ChatPromptAdapter.convert_messages_to_prompt)\#     

Parameters:     

  * **provider** \(_str_\)

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

str

_classmethod _format\_messages\(

    _provider : str_,     _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → Tuple\[str | None, List\[Dict\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/bedrock.html#ChatPromptAdapter.format_messages)\#     

Parameters:     

  * **provider** \(_str_\)

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

_Tuple_\[str | None, _List_\[_Dict_\]\]

__On this page