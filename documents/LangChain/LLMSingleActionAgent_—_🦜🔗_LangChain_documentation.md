# LLMSingleActionAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.LLMSingleActionAgent.html
**Word Count:** 286
**Links Count:** 224
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# LLMSingleActionAgent\#

_class _langchain.agents.agent.LLMSingleActionAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent.html#LLMSingleActionAgent)\#     

Bases: [`BaseSingleActionAgent`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")

Deprecated since version 0.1.0: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) as well as guides for [Migrating from AgentExecutor](https://python.langchain.com/docs/how_to/migrate_agent/) and LangGraph’s [Pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). It will not be removed until langchain==1.0.

Base class for single action agents.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

LLMChain to use for agent.

_param _output\_parser _: [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser")_ _\[Required\]_\#     

Output parser to use for agent.

_param _stop _: list\[str\]__\[Required\]_\#     

List of strings to stop on.

_classmethod _from\_llm\_and\_tools\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [BaseSingleActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")\#     

Construct an agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Tools to use.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callback manager to use.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

Agent object.

Return type:     

[BaseSingleActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")

_async _aplan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent.html#LLMSingleActionAgent.aplan)\#     

Async given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Action specifying what tool to use.

Return type:     

[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

get\_allowed\_tools\(\) → list\[str\] | None\#     

Return type:     

list\[str\] | None

plan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent.html#LLMSingleActionAgent.plan)\#     

Given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with the observations.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Action specifying what tool to use.

Return type:     

[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

return\_stopped\_response\(

    _early\_stopping\_method : str_,     _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _\*\* kwargs: Any_, \) → [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\#     

Return response when agent has been stopped due to max iterations.

Parameters:     

  * **early\_stopping\_method** \(_str_\) – Method to use for early stopping.

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Agent finish object.

Return type:     

[AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

Raises:     

**ValueError** – If early\_stopping\_method is not supported.

save\(

    _file\_path : Path | str_, \) → None\#     

Save the agent.

Parameters:     

**file\_path** \(_Path_ _|__str_\) – Path to file to save the agent to.

Return type:     

None

Example: .. code-block:: python

> \# If working with agent executor agent.agent.save\(file\_path=”path/agent.yaml”\)

tool\_run\_logging\_kwargs\(\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent.html#LLMSingleActionAgent.tool_run_logging_kwargs)\#     

Return logging kwargs for tool run.

Return type:     

dict

_property _input\_keys _: list\[str\]_\#     

Return the input keys.

Returns:     

List of input keys.

_property _return\_values _: list\[str\]_\#     

Return values of the agent.

__On this page