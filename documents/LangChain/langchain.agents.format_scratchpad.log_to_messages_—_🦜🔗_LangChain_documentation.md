# langchain.agents.format_scratchpad.log_to_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/log_to_messages.html
**Word Count:** 33
**Links Count:** 13
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# Source code for langchain.agents.format\_scratchpad.log\_to\_messages               from langchain_core.agents import AgentAction     from langchain_core.messages import AIMessage, BaseMessage, HumanMessage                              [[docs]](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.log_to_messages.format_log_to_messages.html#langchain.agents.format_scratchpad.log_to_messages.format_log_to_messages)     def format_log_to_messages(         intermediate_steps: list[tuple[AgentAction, str]],         template_tool_response: str = "{observation}",     ) -> list[BaseMessage]:         """Construct the scratchpad that lets the agent continue its thought process.              Args:             intermediate_steps: List of tuples of AgentAction and observation strings.             template_tool_response: Template to format the observation with.                  Defaults to "{observation}".              Returns:             List[BaseMessage]: The scratchpad.         """         thoughts: list[BaseMessage] = []         for action, observation in intermediate_steps:             thoughts.append(AIMessage(content=action.log))             human_message = HumanMessage(                 content=template_tool_response.format(observation=observation),             )             thoughts.append(human_message)         return thoughts