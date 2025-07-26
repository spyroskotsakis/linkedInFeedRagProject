# JambaChatCompletionsAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ai21/chat/langchain_ai21.chat.chat_adapter.JambaChatCompletionsAdapter.html
**Word Count:** 12
**Links Count:** 89
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# JambaChatCompletionsAdapter\#

_class _langchain\_ai21.chat.chat\_adapter.JambaChatCompletionsAdapter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_adapter.html#JambaChatCompletionsAdapter)\#     

Adapter for Jamba Chat Completions.

Methods

`call`\(\) |    ---|---   `convert_messages`\(messages\) |       call\(

    _client : Any_,     _stream : Literal\[True\]_,     _\*\* params: Any_, \) → Iterator\[[ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_adapter.html#JambaChatCompletionsAdapter.call)\# call\(

    _client : Any_,     _stream : Literal\[False\]_,     _\*\* params: Any_, \) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]     

convert\_messages\(

    _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_adapter.html#JambaChatCompletionsAdapter.convert_messages)\#     

Parameters:     

**messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page