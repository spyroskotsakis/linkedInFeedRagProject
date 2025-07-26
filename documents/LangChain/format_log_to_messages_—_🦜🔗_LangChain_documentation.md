# format_log_to_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.log_to_messages.format_log_to_messages.html
**Word Count:** 38
**Links Count:** 163
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# format\_log\_to\_messages\#

langchain.agents.format\_scratchpad.log\_to\_messages.format\_log\_to\_messages\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _template\_tool\_response : str = '\{observation\}'_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/log_to_messages.html#format_log_to_messages)\#     

Construct the scratchpad that lets the agent continue its thought process.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – List of tuples of AgentAction and observation strings.

  * **template\_tool\_response** \(_str_\) – Template to format the observation with. Defaults to “\{observation\}”.

Returns:     

The scratchpad.

Return type:     

List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

__On this page