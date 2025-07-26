# format_log_to_str — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.log.format_log_to_str.html
**Word Count:** 53
**Links Count:** 162
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# format\_log\_to\_str\#

langchain.agents.format\_scratchpad.log.format\_log\_to\_str\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _observation\_prefix : str = 'Observation: '_,     _llm\_prefix : str = 'Thought: '_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/log.html#format_log_to_str)\#     

Construct the scratchpad that lets the agent continue its thought process.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – List of tuples of AgentAction and observation strings.

  * **observation\_prefix** \(_str_\) – Prefix to append the observation with. Defaults to “Observation: “.

  * **llm\_prefix** \(_str_\) – Prefix to append the llm call with. Defaults to “Thought: “.

Returns:     

The scratchpad.

Return type:     

str

Examples using format\_log\_to\_str

  * [MLX](https://python.langchain.com/docs/integrations/chat/mlx/)

__On this page