# ChatAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ai21/chat/langchain_ai21.chat.chat_adapter.ChatAdapter.html
**Word Count:** 33
**Links Count:** 89
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# ChatAdapter\#

_class _langchain\_ai21.chat.chat\_adapter.ChatAdapter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_adapter.html#ChatAdapter)\#     

Common interface for the different Chat models available in AI21.

It converts LangChain messages to AI21 messages. Calls the appropriate AI21 model API with the converted messages.

Methods

`call`\(\) |    ---|---   `convert_messages`\(messages\) |       _abstractmethod _call\(

    _client : Any_,     _stream : Literal\[True\]_,     _\*\* params: Any_, \) → Iterator\[[ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_adapter.html#ChatAdapter.call)\# _abstractmethod _call\(

    _client : Any_,     _stream : Literal\[False\]_,     _\*\* params: Any_, \) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]     

_abstractmethod _convert\_messages\(

    _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_adapter.html#ChatAdapter.convert_messages)\#     

Parameters:     

**messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page