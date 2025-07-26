# load_agent_from_config — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.loading.load_agent_from_config.html
**Word Count:** 65
**Links Count:** 167
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# load\_agent\_from\_config\#

langchain.agents.loading.load\_agent\_from\_config\(

    _config : dict_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _tools : list\[[Tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html#langchain_core.tools.simple.Tool "langchain_core.tools.simple.Tool")\] | None = None_,     _\*\* kwargs: Any_, \) → [BaseSingleActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent") | [BaseMultiActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/loading.html#load_agent_from_config)\#     

Deprecated since version 0.1.0: It will not be removed until langchain==1.0.

Load agent from Config Dict.

Parameters:     

  * **config** \(_dict_\) – Config dict to load agent from.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_\) – Language model to use as the agent.

  * **tools** \(_list_ _\[_[_Tool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.simple.Tool.html#langchain_core.tools.simple.Tool "langchain_core.tools.simple.Tool") _\]__|__None_\) – List of tools this agent has access to.

  * **kwargs** \(_Any_\) – Additional keyword arguments passed to the agent executor.

Returns:     

An agent executor.

Raises:     

**ValueError** – If agent type is not specified in the config.

Return type:     

[_BaseSingleActionAgent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent") | [_BaseMultiActionAgent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")

__On this page