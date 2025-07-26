# langchain.agents.schema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/agents/schema.html
**Word Count:** 32
**Links Count:** 13
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# Source code for langchain.agents.schema               from typing import Any          from langchain_core.agents import AgentAction     from langchain_core.prompts.chat import ChatPromptTemplate                              [[docs]](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.schema.AgentScratchPadChatPromptTemplate.html#langchain.agents.schema.AgentScratchPadChatPromptTemplate)     class AgentScratchPadChatPromptTemplate(ChatPromptTemplate):         """Chat prompt template for the agent scratchpad."""              @classmethod         def is_lc_serializable(cls) -> bool:             return False              def _construct_agent_scratchpad(             self,             intermediate_steps: list[tuple[AgentAction, str]],         ) -> str:             if len(intermediate_steps) == 0:                 return ""             thoughts = ""             for action, observation in intermediate_steps:                 thoughts += action.log                 thoughts += f"\nObservation: {observation}\nThought: "             return (                 f"This was your previous work "                 f"(but I haven't seen any of it! I only see what "                 f"you return as final answer):\n{thoughts}"             )              def _merge_partial_and_user_variables(self, **kwargs: Any) -> dict[str, Any]:             intermediate_steps = kwargs.pop("intermediate_steps")             kwargs["agent_scratchpad"] = self._construct_agent_scratchpad(                 intermediate_steps,             )             return kwargs