# AgentTokenBufferMemory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_functions_agent.agent_token_buffer_memory.AgentTokenBufferMemory.html
**Word Count:** 186
**Links Count:** 201
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# AgentTokenBufferMemory\#

_class _langchain.agents.openai\_functions\_agent.agent\_token\_buffer\_memory.AgentTokenBufferMemory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/agent_token_buffer_memory.html#AgentTokenBufferMemory)\#     

Bases: [`BaseChatMemory`](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.chat_memory.BaseChatMemory.html#langchain.memory.chat_memory.BaseChatMemory "langchain.memory.chat_memory.BaseChatMemory")

Memory used to save agent output AND intermediate steps.

Parameters:     

  * **human\_prefix** – Prefix for human messages. Default is “Human”.

  * **ai\_prefix** – Prefix for AI messages. Default is “AI”.

  * **llm** – Language model.

  * **memory\_key** – Key to save memory under. Default is “history”.

  * **max\_token\_limit** – Maximum number of tokens to keep in the buffer. Once the buffer exceeds this many tokens, the oldest messages will be pruned. Default is 12000.

  * **return\_messages** – Whether to return messages. Default is True.

  * **output\_key** – Key to save output under. Default is “output”.

  * **intermediate\_steps\_key** – Key to save intermediate steps under. Default is “intermediate\_steps”.

  * **format\_as\_tools** – Whether to format as tools. Default is False.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

_param _chat\_memory _: [BaseChatMessageHistory](https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html#langchain_core.chat_history.BaseChatMessageHistory "langchain_core.chat_history.BaseChatMessageHistory")_ _\[Optional\]_\#     

_param _format\_as\_tools _: bool_ _ = False_\#     

_param _human\_prefix _: str_ _ = 'Human'_\#     

_param _input\_key _: str | None_ _ = None_\#     

_param _intermediate\_steps\_key _: str_ _ = 'intermediate\_steps'_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _max\_token\_limit _: int_ _ = 12000_\#     

The max number of tokens to keep in the buffer. Once the buffer exceeds this many tokens, the oldest messages will be pruned.

_param _memory\_key _: str_ _ = 'history'_\#     

_param _output\_key _: str_ _ = 'output'_\#     

_param _return\_messages _: bool_ _ = True_\#     

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

    _inputs : dict\[str, Any\]_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/agent_token_buffer_memory.html#AgentTokenBufferMemory.load_memory_variables)\#     

Return history buffer.

Parameters:     

**inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Inputs to the agent.

Returns:     

A dictionary with the history buffer.

Return type:     

dict\[str, _Any_\]

save\_context\(

    _inputs : dict\[str, Any\]_,     _outputs : dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/agent_token_buffer_memory.html#AgentTokenBufferMemory.save_context)\#     

Save context from this conversation to buffer. Pruned.

Parameters:     

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Inputs to the agent.

  * **outputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – Outputs from the agent.

Return type:     

None

_property _buffer _: list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

String buffer of memory.

__On this page