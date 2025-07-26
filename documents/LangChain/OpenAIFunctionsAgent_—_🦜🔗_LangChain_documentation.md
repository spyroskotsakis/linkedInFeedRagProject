# OpenAIFunctionsAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_functions_agent.base.OpenAIFunctionsAgent.html
**Word Count:** 400
**Links Count:** 239
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# OpenAIFunctionsAgent\#

_class _langchain.agents.openai\_functions\_agent.base.OpenAIFunctionsAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent)\#     

Bases: [`BaseSingleActionAgent`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")

Deprecated since version 0.1.0: Use [`create_openai_functions_agent()`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.openai_functions_agent.base.create_openai_functions_agent.html#langchain.agents.openai_functions_agent.base.create_openai_functions_agent "langchain.agents.openai_functions_agent.base.create_openai_functions_agent") instead. It will not be removed until langchain==1.0.

An Agent driven by OpenAIs function powered API.

Parameters:     

  * **llm** – This should be an instance of ChatOpenAI, specifically a model that supports using functions.

  * **tools** – The tools this agent has access to.

  * **prompt** – The prompt for this agent, should support agent\_scratchpad as one of the variables. For an easy way to construct this prompt, use OpenAIFunctionsAgent.create\_prompt\(…\)

  * **output\_parser** – The output parser for this agent. Should be an instance of OpenAIFunctionsAgentOutputParser. Defaults to OpenAIFunctionsAgentOutputParser.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

_param _output\_parser _: type\[[OpenAIFunctionsAgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.output_parsers.openai_functions.OpenAIFunctionsAgentOutputParser.html#langchain.agents.output_parsers.openai_functions.OpenAIFunctionsAgentOutputParser "langchain.agents.output_parsers.openai_functions.OpenAIFunctionsAgentOutputParser")\]__ = <class 'langchain.agents.output\_parsers.openai\_functions.OpenAIFunctionsAgentOutputParser'>_\#     

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")_ _\[Required\]_\#     

_param _tools _: Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__\[Required\]_\#     

_classmethod _create\_prompt\(

    _system\_message: ~langchain\_core.messages.system.SystemMessage | None = <object object>_,     _extra\_prompt\_messages: list\[~langchain\_core.prompts.message.BaseMessagePromptTemplate\] | None = None_, \) → [ChatPromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent.create_prompt)\#     

Create prompt for this agent.

Parameters:     

  * **system\_message** \([_SystemMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html#langchain_core.messages.system.SystemMessage "langchain_core.messages.system.SystemMessage") _|__None_\) – Message to use as the system message that will be the first in the prompt.

  * **extra\_prompt\_messages** \(_list_ _\[_[_BaseMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") _\]__|__None_\) – Prompt messages that will be placed between the system message and the new human input.

Returns:     

A prompt template to pass into this agent.

Return type:     

[_ChatPromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate "langchain_core.prompts.chat.ChatPromptTemplate")

_classmethod _from\_llm\_and\_tools\(_llm: ~langchain\_core.language\_models.base.BaseLanguageModel, tools: ~collections.abc.Sequence\[~langchain\_core.tools.base.BaseTool\], callback\_manager: ~langchain\_core.callbacks.base.BaseCallbackManager | None = None, extra\_prompt\_messages: list\[~langchain\_core.prompts.message.BaseMessagePromptTemplate\] | None = None, system\_message: ~langchain\_core.messages.system.SystemMessage | None = <object object>, \*\*kwargs: ~typing.Any_\) → [BaseSingleActionAgent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent.from_llm_and_tools)\#     

Construct an agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The LLM to use as the agent.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The tools to use.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – The callback manager to use. Defaults to None.

  * **extra\_prompt\_messages** \(_list_ _\[_[_BaseMessagePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate") _\]__|__None_\) – Extra prompt messages to use. Defaults to None.

  * **system\_message** \([_SystemMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html#langchain_core.messages.system.SystemMessage "langchain_core.messages.system.SystemMessage") _|__None_\) – The system message to use. Defaults to a default system message.

  * **kwargs** \(_Any_\) – Additional parameters to pass to the agent.

Return type:     

[_BaseSingleActionAgent_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.BaseSingleActionAgent.html#langchain.agents.agent.BaseSingleActionAgent "langchain.agents.agent.BaseSingleActionAgent")

_async _aplan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _\*\* kwargs: Any_, \) → [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent.aplan)\#     

Async given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to use. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Action specifying what tool to use. If the agent is finished, returns an AgentFinish. If the agent is not finished, returns an AgentAction.

Return type:     

[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

get\_allowed\_tools\(\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent.get_allowed_tools)\#     

Get allowed tools.

Return type:     

list\[str\]

plan\(

    _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _with\_functions : bool = True_,     _\*\* kwargs: Any_, \) → [AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent.plan)\#     

Given input, decided what to do.

Parameters:     

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Steps the LLM has taken to date, along with observations.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to use. Defaults to None.

  * **with\_functions** \(_bool_\) – Whether to use functions. Defaults to True.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

Action specifying what tool to use. If the agent is finished, returns an AgentFinish. If the agent is not finished, returns an AgentAction.

Return type:     

[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") | [_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

return\_stopped\_response\(

    _early\_stopping\_method : str_,     _intermediate\_steps : list\[tuple\[[AgentAction](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction"), str\]\]_,     _\*\* kwargs: Any_, \) → [AgentFinish](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/openai_functions_agent/base.html#OpenAIFunctionsAgent.return_stopped_response)\#     

Return response when agent has been stopped due to max iterations.

Parameters:     

  * **early\_stopping\_method** \(_str_\) – The early stopping method to use.

  * **intermediate\_steps** \(_list_ _\[__tuple_ _\[_[_AgentAction_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentAction.html#langchain_core.agents.AgentAction "langchain_core.agents.AgentAction") _,__str_ _\]__\]_\) – Intermediate steps.

  * **\*\*kwargs** \(_Any_\) – User inputs.

Returns:     

AgentFinish.

Raises:     

  * **ValueError** – If early\_stopping\_method is not force or generate.

  * **ValueError** – If agent\_decision is not an AgentAction.

Return type:     

[_AgentFinish_](https://python.langchain.com/api_reference/core/agents/langchain_core.agents.AgentFinish.html#langchain_core.agents.AgentFinish "langchain_core.agents.AgentFinish")

save\(

    _file\_path : Path | str_, \) → None\#     

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

_property _functions _: list\[dict\]_\#     

Get functions.

_property _input\_keys _: list\[str\]_\#     

Get input keys. Input refers to user input here.

_property _return\_values _: list\[str\]_\#     

Return values of the agent.

Examples using OpenAIFunctionsAgent

  * [Exa Search](https://python.langchain.com/docs/integrations/tools/exa_search/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [Robocorp Toolkit](https://python.langchain.com/docs/integrations/tools/robocorp/)

__On this page