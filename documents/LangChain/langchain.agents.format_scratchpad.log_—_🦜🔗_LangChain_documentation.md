# langchain.agents.format_scratchpad.log — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/agents/format_scratchpad/log.html
**Word Count:** 46
**Links Count:** 13
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# Source code for langchain.agents.format\_scratchpad.log               from langchain_core.agents import AgentAction                              [[docs]](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.format_scratchpad.log.format_log_to_str.html#langchain.agents.format_scratchpad.log.format_log_to_str)     def format_log_to_str(         intermediate_steps: list[tuple[AgentAction, str]],         observation_prefix: str = "Observation: ",         llm_prefix: str = "Thought: ",     ) -> str:         """Construct the scratchpad that lets the agent continue its thought process.              Args:             intermediate_steps: List of tuples of AgentAction and observation strings.             observation_prefix: Prefix to append the observation with.                  Defaults to "Observation: ".             llm_prefix: Prefix to append the llm call with.                     Defaults to "Thought: ".              Returns:             str: The scratchpad.         """         thoughts = ""         for action, observation in intermediate_steps:             thoughts += action.log             thoughts += f"\n{observation_prefix}{observation}\n{llm_prefix}"         return thoughts