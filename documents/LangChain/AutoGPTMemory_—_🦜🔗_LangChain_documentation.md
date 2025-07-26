# AutoGPTMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/autonomous_agents/langchain_experimental.autonomous_agents.autogpt.memory.AutoGPTMemory.html
**Word Count:** 84
**Links Count:** 148
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# AutoGPTMemory\#

_class _langchain\_experimental.autonomous\_agents.autogpt.memory.AutoGPTMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/memory.html#AutoGPTMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")

Memory for AutoGPT.

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _output\_key _: str | None_ _ = None_\#     

_param _retriever _: [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_ _\[Required\]_\#     

VectorStoreRetriever object to connect to.

_param _return\_messages _: bool_ _ = False_\#     

_async _aclear\(\) → None\#     

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

    _inputs : Dict\[str, Any\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/autonomous_agents/autogpt/memory.html#AutoGPTMemory.load_memory_variables)\#     

Return key-value pairs given the text input to the chain.

Parameters:     

**inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the chain.

Returns:     

A dictionary of key-value pairs.

Return type:     

_Dict_\[str, _Any_\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, str\]_, \) → None\#     

Save context from this conversation to buffer.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **outputs** \(_dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_property _memory\_variables _: List\[str\]_\#     

The string keys this memory class will add to chain inputs.

__On this page