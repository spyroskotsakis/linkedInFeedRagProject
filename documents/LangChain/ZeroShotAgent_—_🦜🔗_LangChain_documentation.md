# ZeroShotAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.mrkl.base.ZeroShotAgent.html
**Word Count:** 472
**Links Count:** 237
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# ZeroShotAgent\#

_class _langchain.agents.mrkl.base.ZeroShotAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/mrkl/base.html#ZeroShotAgent)\#     

Bases: [`Agent`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")

Deprecated since version 0.1.0: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) as well as guides for [Migrating from AgentExecutor](https://python.langchain.com/docs/how_to/migrate_agent/) and LangGraph’s [Pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). It will not be removed until langchain==1.0.

Agent for the MRKL chain.

Parameters:     

**output\_parser** – Output parser for the agent.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_tools _: list\[str\] | None_ _ = None_\#     

Allowed tools for the agent. If None, all tools are allowed.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

LLMChain to use for agent.

_param _output\_parser _: [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser")_ _\[Optional\]_\#     

Output parser to use for agent.

_classmethod _create\_prompt\(

    _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _prefix : str = 'Answer the following questions as best you can. You have access to the following tools:'_,     _suffix : str = 'Begin\!\n\nQuestion: \{input\}\nThought:\{agent\_scratchpad\}'_,     _format\_instructions : str = 'Use the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of \[\{tool\_names\}\]\nAction Input: the input to the action\nObservation: the result of the action\n... \(this Thought/Action/Action Input/Observation can repeat N times\)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question'_,     _input\_variables : list\[str\] | None = None_, \) → [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/mrkl/base.html#ZeroShotAgent.create_prompt)\#     

Create prompt in the style of the zero shot agent.

Parameters:     

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – List of tools the agent will have access to, used to format the prompt.

  * **prefix** \(_str_\) – String to put before the list of tools. Defaults to PREFIX.

  * **suffix** \(_str_\) – String to put after the list of tools. Defaults to SUFFIX.

  * **format\_instructions** \(_str_\) – Instructions on how to use the tools. Defaults to FORMAT\_INSTRUCTIONS

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – List of input variables the final prompt will expect. Defaults to None.

Returns:     

A PromptTemplate with the template assembled from the pieces here.

Return type:     

[_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")

_classmethod _from\_llm\_and\_tools\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _output\_parser : [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") | None = None_,     _prefix : str = 'Answer the following questions as best you can. You have access to the following tools:'_,     _suffix : str = 'Begin\!\n\nQuestion: \{input\}\nThought:\{agent\_scratchpad\}'_,     _format\_instructions : str = 'Use the following format:\n\nQuestion: the input question you must answer\nThought: you should always think about what to do\nAction: the action to take, should be one of \[\{tool\_names\}\]\nAction Input: the input to the action\nObservation: the result of the action\n... \(this Thought/Action/Action Input/Observation can repeat N times\)\nThought: I now know the final answer\nFinal Answer: the final answer to the original input question'_,     _input\_variables : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [Agent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/mrkl/base.html#ZeroShotAgent.from_llm_and_tools)\#     

Construct an agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The LLM to use as the agent LLM.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The tools to use.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – The callback manager to use. Defaults to None.

  * **output\_parser** \([_AgentOutputParser_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") _|__None_\) – The output parser to use. Defaults to None.

  * **prefix** \(_str_\) – The prefix to use. Defaults to PREFIX.

  * **suffix** \(_str_\) – The suffix to use. Defaults to SUFFIX.

  * **format\_instructions** \(_str_\) – The format instructions to use. Defaults to FORMAT\_INSTRUCTIONS.

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – The input variables to use. Defaults to None.

  * **kwargs** \(_Any_\) – Additional parameters to pass to the agent.

Return type:     

[_Agent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")

_async _aplan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\#     

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

Get allowed tools.

Return type:     

list\[str\] | None

get\_full\_inputs\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _\*\* kwargs: Any_, \) → dict\[str, Any\]\#     

Create the full inputs for the LLMChain from intermediate steps.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Full inputs for the LLMChain.

Return type:     

Dict\[str, Any\]

plan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")\#     

Given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

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

**ValueError** – If early\_stopping\_method is not in \[‘force’, ‘generate’\].

save\(_file\_path : Path | str_\) → None\#     

Save the agent.

Parameters:     

**file\_path** \(_Path_ _|__str_\) – Path to file to save the agent to.

Return type:     

None

Example: .. code-block:: python

> \# If working with agent executor agent.agent.save\(file\_path=”path/agent.yaml”\)

tool\_run\_logging\_kwargs\(\) → dict\#     

Return logging kwargs for tool run.

Return type:     

dict

_property _llm\_prefix _: str_\#     

Prefix to append the llm call with.

Returns:     

”

Return type:     

“Thought

_property _observation\_prefix _: str_\#     

Prefix to append the observation with.

Returns:     

”

Return type:     

“Observation

_property _return\_values _: list\[str\]_\#     

Return values of the agent.

__On this page