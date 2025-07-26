# BaseChatMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html
**Word Count:** 140
**Links Count:** 131
**Scraped:** 2025-07-21 07:49:33
**Status:** completed

---

# BaseChatMemory\#

_class _langchain.memory.chat\_memory.BaseChatMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory)\#     

Bases: `BaseMemory`, `ABC`

Deprecated since version 0.3.1: Please see the migration guide at: <https://python.langchain.com/docs/versions/migrating_memory/> It will not be removed until langchain==1.0.0.

Abstract base class for chat memory.

**ATTENTION** This abstraction was created prior to when chat models had     

native tool calling capabilities. It does **NOT** support native tool calling capabilities for chat models and will fail SILENTLY if used with a chat model that has native tool calling.

DO NOT USE THIS ABSTRACTION FOR NEW CODE.

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _return\_messages _: bool_ _ = False_\#     

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.aclear)\#     

Clear memory contents.

Return type:     

None

_async _aload\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Async return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

dict\[str, _Any_\]

_async _asave\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.asave_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.clear)\#     

Clear memory contents.

Return type:     

None

_abstractmethod _load\_memory\_variables\(

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\]\#     

Return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

dict\[str, _Any_\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/memory/chat_memory.html#BaseChatMemory.save_context)\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_abstract property _memory\_variables _: list\[str\]_\#     

The string keys this memory class will add to chain inputs.

__On this page