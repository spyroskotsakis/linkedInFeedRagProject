# format_to_openai_function_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.openai_functions.format_to_openai_function_messages.html
**Word Count:** 55
**Links Count:** 164
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# format\_to\_openai\_function\_messages\#

langchain.agents.format\_scratchpad.openai\_functions.format\_to\_openai\_function\_messages\(

    _intermediate\_steps : Sequence\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/openai_functions.html#format_to_openai_function_messages)\#     

Convert \(AgentAction, tool output\) tuples into FunctionMessages.

Parameters:     

**intermediate\_steps** \(_Sequence_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations

Returns:     

list of messages to send to the LLM for the next prediction

Raises:     

**ValueError** – if the observation cannot be converted to a string.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Examples using format\_to\_openai\_function\_messages

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

__On this page