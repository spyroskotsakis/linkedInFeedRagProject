# OpenAIMultiFunctionsAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_functions_multi_agent.base.OpenAIMultiFunctionsAgent.html
**Word Count:** 362
**Links Count:** 231
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# OpenAIMultiFunctionsAgent\#

_class _langchain.agents.openai\_functions\_multi\_agent.base.OpenAIMultiFunctionsAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_multi_agent/base.html#OpenAIMultiFunctionsAgent)\#     

Bases: [`BaseMultiActionAgent`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")

Deprecated since version 0.1.0: Use `create_openai_tools_agent()` instead. It will not be removed until langchain==1.0.

Agent driven by OpenAIs function powered API.

Parameters:     

  * **llm** – This should be an instance of ChatOpenAI, specifically a model that supports using functions.

  * **tools** – The tools this agent has access to.

  * **prompt** – The prompt for this agent, should support agent\_scratchpad as one of the variables. For an easy way to construct this prompt, use OpenAIMultiFunctionsAgent.create\_prompt\(…\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _\[Required\]_\#     

_param _tools _: Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__\[Required\]_\#     

_classmethod _create\_prompt\(

    _system\_message: ~langchain\_core.messages.system.SystemMessage | None = <object object>_,     _extra\_prompt\_messages: list\[~langchain\_core.prompts.message.BaseMessagePromptTemplate\] | None = None_, \) → [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_multi_agent/base.html#OpenAIMultiFunctionsAgent.create_prompt)\#     

Create prompt for this agent.

Parameters:     

  * **system\_message** \([_SystemMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html#langchain_core.messages.system.SystemMessage "langchain_core.messages.system.SystemMessage") _|__None_\) – Message to use as the system message that will be the first in the prompt.

  * **extra\_prompt\_messages** \(_list_ _\[_[_BaseMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") _\]__|__None_\) – Prompt messages that will be placed between the system message and the new human input. Default is None.

Returns:     

A prompt template to pass into this agent.

Return type:     

[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")

_classmethod _from\_llm\_and\_tools\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], callback\_manager: ~langchain\_core.callbacks.base.BaseCallbackManager | None = None, extra\_prompt\_messages: list\[~langchain\_core.prompts.message.BaseMessagePromptTemplate\] | None = None, system\_message: ~langchain\_core.messages.system.SystemMessage | None = <object object>, \*\*kwargs: ~typing.Any_\) → [BaseMultiActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_multi_agent/base.html#OpenAIMultiFunctionsAgent.from_llm_and_tools)\#     

Construct an agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of tools to use.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – The callback manager to use. Default is None.

  * **extra\_prompt\_messages** \(_list_ _\[_[_BaseMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") _\]__|__None_\) – Extra prompt messages to use. Default is None.

  * **system\_message** \([_SystemMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html#langchain_core.messages.system.SystemMessage "langchain_core.messages.system.SystemMessage") _|__None_\) – The system message to use. Default is a default system message.

  * **kwargs** \(_Any_\) – Additional arguments.

Return type:     

[_BaseMultiActionAgent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseMultiActionAgent.html#langchain.agents.agent.BaseMultiActionAgent "langchain.agents.agent.BaseMultiActionAgent")

_async _aplan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → list\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\] | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_multi_agent/base.html#OpenAIMultiFunctionsAgent.aplan)\#     

Async given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to use. Default is None.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Action specifying what tool to use.

Return type:     

list\[[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\] | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

get\_allowed\_tools\(\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_multi_agent/base.html#OpenAIMultiFunctionsAgent.get_allowed_tools)\#     

Get allowed tools.

Return type:     

list\[str\]

plan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → list\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\] | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_multi_agent/base.html#OpenAIMultiFunctionsAgent.plan)\#     

Given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to use. Default is None.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Action specifying what tool to use.

Return type:     

list\[[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction")\] | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

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

Raises:     

  * **NotImplementedError** – If agent does not support saving.

  * **ValueError** – If file\_path is not json or yaml.

Return type:     

None

Example: .. code-block:: python

> \# If working with agent executor agent.agent.save\(file\_path=”path/agent.yaml”\)

tool\_run\_logging\_kwargs\(\) → dict\#     

Return logging kwargs for tool run.

Return type:     

dict

_property _functions _: list\[dict\]_\#     

Get the functions for the agent.

_property _input\_keys _: list\[str\]_\#     

Get input keys. Input refers to user input here.

_property _return\_values _: list\[str\]_\#     

Return values of the agent.

__On this page