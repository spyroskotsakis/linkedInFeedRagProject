# ConversationBufferMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.buffer.ConversationBufferMemory.html
**Word Count:** 160
**Links Count:** 159
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# ConversationBufferMemory\#

_class _langchain.memory.buffer.ConversationBufferMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

A basic memory implementation that simply stores the conversation history.

This stores the entire conversation history in memory without any additional processing.

Note that additional processing may be required in some situations when the conversation history is too large to fit in the context window of the model.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _return\_messages _: bool_ _ = False_\#     

_async _abuffer\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.abuffer)\#     

String buffer of memory.

Return type:     

_Any_

_async _abuffer\_as\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.abuffer_as_messages)\#     

Exposes the buffer as a list of messages in case return\_messages is False.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_async _abuffer\_as\_str\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.abuffer_as_str)\#     

Exposes the buffer as a string in case return\_messages is True.

Return type:     

str

_async _aclear\(\) → None\#     

Clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.aload_memory_variables)\#     

Return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None\#     

Clear memory contents.

Return type:     

None

load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/buffer.html#ConversationBufferMemory.load_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

dict\[str, _Any_\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _buffer _: Any_\#     

String buffer of memory.

_property _buffer\_as\_messages _: list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

Exposes the buffer as a list of messages in case return\_messages is False.

_property _buffer\_as\_str _: str_\#     

Exposes the buffer as a string in case return\_messages is True.

Examples using ConversationBufferMemory

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/conversation_chain/)

  * [Bittensor](https://python.langchain.com/docs/integrations/llms/bittensor/)

  * [Gradio](https://python.langchain.com/docs/integrations/tools/gradio_tools/)

  * [Llama2Chat](https://python.langchain.com/docs/integrations/chat/llama2_chat/)

  * [Memorize](https://python.langchain.com/docs/integrations/tools/memorize/)

  * [Reddit Search ](https://python.langchain.com/docs/integrations/tools/reddit_search/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SceneXplain](https://python.langchain.com/docs/integrations/tools/sceneXplain/)

  * [Xata](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history/)

__On this page