# create_pandas_dataframe_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html
**Word Count:** 366
**Links Count:** 117
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# create\_pandas\_dataframe\_agent\#

langchain\_experimental.agents.agent\_toolkits.pandas.base.create\_pandas\_dataframe\_agent\(

    _llm : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\], [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | str\]_,     _df : Any_,     _agent\_type : [AgentType](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") | Literal\['openai-tools', 'tool-calling'\] = AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str | None = None_,     _suffix : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _verbose : bool = False_,     _return\_intermediate\_steps : bool = False_,     _max\_iterations : int | None = 15_,     _max\_execution\_time : float | None = None_,     _early\_stopping\_method : str = 'force'_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _include\_df\_in\_prompt : bool | None = True_,     _number\_of\_head\_rows : int = 5_,     _extra\_tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\] = \(\)_,     _engine : Literal\['pandas', 'modin'\] = 'pandas'_,     _allow\_dangerous\_code : bool = False_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/agents/agent_toolkits/pandas/base.html#create_pandas_dataframe_agent)\#     

Construct a Pandas agent from an LLM and dataframe\(s\).

Security Notice:     

This agent relies on access to a python repl tool which can execute arbitrary code. This can be dangerous and requires a specially sandboxed environment to be safely used. Failure to run this code in a properly sandboxed environment can lead to arbitrary code execution vulnerabilities, which can lead to data breaches, data loss, or other security incidents.

Do not use this code with untrusted inputs, with elevated permissions, or without consulting your security team about proper sandboxing\!

You must opt-in to use this functionality by setting allow\_dangerous\_code=True.

Parameters:     

  * **llm** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[_[_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") _|__str_ _|__Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__\]__,_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__str_ _\]_\) – Language model to use for the agent. If agent\_type is “tool-calling” then llm is expected to support tool calling.

  * **df** \(_Any_\) – Pandas dataframe or list of Pandas dataframes.

  * **agent\_type** \([_AgentType_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") _|__Literal_ _\[__'openai-tools'__,__'tool-calling'__\]_\) – One of “tool-calling”, “openai-tools”, “openai-functions”, or “zero-shot-react-description”. Defaults to “zero-shot-react-description”. “tool-calling” is recommended over the legacy “openai-tools” and “openai-functions” types.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – DEPRECATED. Pass “callbacks” key into ‘agent\_executor\_kwargs’ instead to pass constructor callbacks to AgentExecutor.

  * **prefix** \(_str_ _|__None_\) – Prompt prefix string.

  * **suffix** \(_str_ _|__None_\) – Prompt suffix string.

  * **input\_variables** \(_List_ _\[__str_ _\]__|__None_\) – DEPRECATED. Input variables automatically inferred from constructed prompt.

  * **verbose** \(_bool_\) – AgentExecutor verbosity.

  * **return\_intermediate\_steps** \(_bool_\) – Passed to AgentExecutor init.

  * **max\_iterations** \(_int_ _|__None_\) – Passed to AgentExecutor init.

  * **max\_execution\_time** \(_float_ _|__None_\) – Passed to AgentExecutor init.

  * **early\_stopping\_method** \(_str_\) – Passed to AgentExecutor init.

  * **agent\_executor\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Arbitrary additional AgentExecutor args.

  * **include\_df\_in\_prompt** \(_bool_ _|__None_\) – Whether to include the first number\_of\_head\_rows in the prompt. Must be None if suffix is not None.

  * **number\_of\_head\_rows** \(_int_\) – Number of initial rows to include in prompt if include\_df\_in\_prompt is True.

  * **extra\_tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Additional tools to give to agent on top of a PythonAstREPLTool.

  * **engine** \(_Literal_ _\[__'pandas'__,__'modin'__\]_\) – One of “modin” or “pandas”. Defaults to “pandas”.

  * **allow\_dangerous\_code** \(_bool_\) – bool, default False This agent relies on access to a python repl tool which can execute arbitrary code. This can be dangerous and requires a specially sandboxed environment to be safely used. Failure to properly sandbox this class can lead to arbitrary code execution vulnerabilities, which can lead to data breaches, data loss, or other security incidents. You must opt in to use this functionality by setting allow\_dangerous\_code=True.

  * **\*\*kwargs** \(_Any_\) – DEPRECATED. Not used, kept for backwards compatibility.

Returns:     

An AgentExecutor with the specified agent\_type agent and access to a PythonAstREPLTool with the DataFrame\(s\) and any user-provided extra\_tools.

Return type:     

[_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Example               from langchain_openai import ChatOpenAI     from langchain_experimental.agents import create_pandas_dataframe_agent     import pandas as pd          df = pd.read_csv("titanic.csv")     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)     agent_executor = create_pandas_dataframe_agent(         llm,         df,         agent_type="tool-calling",         verbose=True     )     

Examples using create\_pandas\_dataframe\_agent

  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)

  * [Pandas Dataframe](https://python.langchain.com/docs/integrations/tools/pandas/)

__On this page