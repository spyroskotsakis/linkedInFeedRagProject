# create_python_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.python.base.create_python_agent.html
**Word Count:** 16
**Links Count:** 109
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# create\_python\_agent\#

langchain\_experimental.agents.agent\_toolkits.python.base.create\_python\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tool : [PythonREPLTool](https://python.langchain.com/api_reference/experimental/tools/langchain_experimental.tools.python.tool.PythonREPLTool.html#langchain_experimental.tools.python.tool.PythonREPLTool "langchain_experimental.tools.python.tool.PythonREPLTool")_,     _agent\_type : [AgentType](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") = AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _verbose : bool = False_,     _prefix : str = 'You are an agent designed to write and execute python code to answer questions.\nYou have access to a python REPL, which you can use to execute python code.\nIf you get an error, debug your code and try again.\nOnly use the output of your code to answer the question. \nYou might know the answer without running any code, but you should still run the code to get the answer.\nIf it does not seem like you can write code to answer the question, just return "I don\'t know" as the answer.\n'_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Dict\[str, Any\]_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/agents/agent_toolkits/python/base.html#create_python_agent)\#     

Construct a python agent from an LLM and tool.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **tool** \([_PythonREPLTool_](https://python.langchain.com/api_reference/experimental/tools/langchain_experimental.tools.python.tool.PythonREPLTool.html#langchain_experimental.tools.python.tool.PythonREPLTool "langchain_experimental.tools.python.tool.PythonREPLTool")\)

  * **agent\_type** \([_AgentType_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType")\)

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **verbose** \(_bool_\)

  * **prefix** \(_str_\)

  * **agent\_executor\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

[_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

__On this page