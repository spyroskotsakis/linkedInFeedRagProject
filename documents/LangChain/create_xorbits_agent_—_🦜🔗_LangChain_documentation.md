# create_xorbits_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.xorbits.base.create_xorbits_agent.html
**Word Count:** 172
**Links Count:** 105
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# create\_xorbits\_agent\#

langchain\_experimental.agents.agent\_toolkits.xorbits.base.create\_xorbits\_agent\(

    _llm : [BaseLLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.BaseLLM.html#langchain_core.language_models.llms.BaseLLM "langchain_core.language_models.llms.BaseLLM")_,     _data : Any_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str = ''_,     _suffix : str = ''_,     _input\_variables : List\[str\] | None = None_,     _verbose : bool = False_,     _return\_intermediate\_steps : bool = False_,     _max\_iterations : int | None = 15_,     _max\_execution\_time : float | None = None_,     _early\_stopping\_method : str = 'force'_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _allow\_dangerous\_code : bool = False_,     _\*\* kwargs: Dict\[str, Any\]_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/agents/agent_toolkits/xorbits/base.html#create_xorbits_agent)\#     

Construct a xorbits agent from an LLM and dataframe.

Security Notice:     

This agent relies on access to a python repl tool which can execute arbitrary code. This can be dangerous and requires a specially sandboxed environment to be safely used. Failure to run this code in a properly sandboxed environment can lead to arbitrary code execution vulnerabilities, which can lead to data breaches, data loss, or other security incidents.

Do not use this code with untrusted inputs, with elevated permissions, or without consulting your security team about proper sandboxing\!

You must opt in to use this functionality by setting allow\_dangerous\_code=True.

Parameters:     

  * **allow\_dangerous\_code** \(_bool_\) – bool, default False This agent relies on access to a python repl tool which can execute arbitrary code. This can be dangerous and requires a specially sandboxed environment to be safely used. Failure to properly sandbox this class can lead to arbitrary code execution vulnerabilities, which can lead to data breaches, data loss, or other security incidents. You must opt in to use this functionality by setting allow\_dangerous\_code=True.

  * **llm** \([_BaseLLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.BaseLLM.html#langchain_core.language_models.llms.BaseLLM "langchain_core.language_models.llms.BaseLLM")\)

  * **data** \(_Any_\)

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

  * **prefix** \(_str_\)

  * **suffix** \(_str_\)

  * **input\_variables** \(_List_ _\[__str_ _\]__|__None_\)

  * **verbose** \(_bool_\)

  * **return\_intermediate\_steps** \(_bool_\)

  * **max\_iterations** \(_int_ _|__None_\)

  * **max\_execution\_time** \(_float_ _|__None_\)

  * **early\_stopping\_method** \(_str_\)

  * **agent\_executor\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

[_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

__On this page