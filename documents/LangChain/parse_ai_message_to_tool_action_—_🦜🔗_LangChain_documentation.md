# parse_ai_message_to_tool_action — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.output_parsers.tools.parse_ai_message_to_tool_action.html
**Word Count:** 15
**Links Count:** 165
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# parse\_ai\_message\_to\_tool\_action\#

langchain.agents.output\_parsers.tools.parse\_ai\_message\_to\_tool\_action\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → list\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\] | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/output_parsers/tools.html#parse_ai_message_to_tool_action)\#     

Parse an AI message potentially containing tool\_calls.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

Return type:     

list\[[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\] | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

__On this page