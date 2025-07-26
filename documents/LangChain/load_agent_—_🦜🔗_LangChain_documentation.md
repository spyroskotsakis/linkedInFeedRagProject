# load_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.loading.load_agent.html
**Word Count:** 53
**Links Count:** 163
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# load\_agent\#

langchain.agents.loading.load\_agent\(

    _path : str | Path_,     _\*\* kwargs: Any_, \) → [BaseSingleActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent") | [BaseMultiActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/loading.html#load_agent)\#     

Deprecated since version 0.1.0: It will not be removed until langchain==1.0.

Unified method for loading an agent from LangChainHub or local fs.

Parameters:     

  * **path** \(_str_ _|__Path_\) – Path to the agent file.

  * **kwargs** \(_Any_\) – Additional keyword arguments passed to the agent executor.

Returns:     

An agent executor.

Raises:     

**RuntimeError** – If loading from the deprecated github-based Hub is attempted.

Return type:     

[_BaseSingleActionAgent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent") | [_BaseMultiActionAgent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")

__On this page