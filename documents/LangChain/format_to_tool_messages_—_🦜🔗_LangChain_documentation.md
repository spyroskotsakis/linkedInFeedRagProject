# format_to_tool_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.tools.format_to_tool_messages.html
**Word Count:** 36
**Links Count:** 163
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# format\_to\_tool\_messages\#

langchain.agents.format\_scratchpad.tools.format\_to\_tool\_messages\(

    _intermediate\_steps : Sequence\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/tools.html#format_to_tool_messages)\#     

Convert \(AgentAction, tool output\) tuples into ToolMessages.

Parameters:     

**intermediate\_steps** \(_Sequence_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

Returns:     

list of messages to send to the LLM for the next prediction.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

__On this page