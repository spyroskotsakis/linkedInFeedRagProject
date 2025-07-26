# ConversationalChatAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.conversational_chat.base.ConversationalChatAgent.html
**Word Count:** 379
**Links Count:** 238
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# ConversationalChatAgent\#

_class _langchain.agents.conversational\_chat.base.ConversationalChatAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/conversational_chat/base.html#ConversationalChatAgent)\#     

Bases: [`Agent`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")

Deprecated since version 0.1.0: Use `create_json_chat_agent()` instead. It will not be removed until langchain==1.0.

An agent designed to hold a conversation in addition to using tools.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _allowed\_tools _: list\[str\] | None_ _ = None_\#     

Allowed tools for the agent. If None, all tools are allowed.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

LLMChain to use for agent.

_param _output\_parser _: [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser")_ _\[Optional\]_\#     

Output parser for the agent.

_param _template\_tool\_response _: str_ _ = "TOOL RESPONSE:\n---------------------\n\{observation\}\n\nUSER'S INPUT\n--------------------\n\nOkay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES\! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else."_\#     

Template for the tool response.

_classmethod _create\_prompt\(

    _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _system\_message : str = 'Assistant is a large language model trained by OpenAI.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n\nAssistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n\nOverall, Assistant is a powerful system that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.'_,     _human\_message : str = "TOOLS\n------\nAssistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:\n\n\{\{tools\}\}\n\n\{format\_instructions\}\n\nUSER'S INPUT\n--------------------\nHere is the user's input \(remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else\):\n\n\{\{\{\{input\}\}\}\}"_,     _input\_variables : list\[str\] | None = None_,     _output\_parser : [BaseOutputParser](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") | None = None_, \) → [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/conversational_chat/base.html#ConversationalChatAgent.create_prompt)\#     

Create a prompt for the agent.

Parameters:     

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – The tools to use.

  * **system\_message** \(_str_\) – The system message to use. Defaults to the PREFIX.

  * **human\_message** \(_str_\) – The human message to use. Defaults to the SUFFIX.

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – The input variables to use. Defaults to None.

  * **output\_parser** \([_BaseOutputParser_](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.base.BaseOutputParser.html#langchain_core.output_parsers.base.BaseOutputParser "langchain_core.output_parsers.base.BaseOutputParser") _|__None_\) – The output parser to use. Defaults to None.

Returns:     

A PromptTemplate.

Return type:     

[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")

_classmethod _from\_llm\_and\_tools\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _output\_parser : [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") | None = None_,     _system\_message : str = 'Assistant is a large language model trained by OpenAI.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n\nAssistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n\nOverall, Assistant is a powerful system that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.'_,     _human\_message : str = "TOOLS\n------\nAssistant can ask the user to use tools to look up information that may be helpful in answering the users original question. The tools the human can use are:\n\n\{\{tools\}\}\n\n\{format\_instructions\}\n\nUSER'S INPUT\n--------------------\nHere is the user's input \(remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else\):\n\n\{\{\{\{input\}\}\}\}"_,     _input\_variables : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [Agent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/conversational_chat/base.html#ConversationalChatAgent.from_llm_and_tools)\#     

Construct an agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of tools to use.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – The callback manager to use. Default is None.

  * **output\_parser** \([_AgentOutputParser_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") _|__None_\) – The output parser to use. Default is None.

  * **system\_message** \(_str_\) – The system message to use. Default is PREFIX.

  * **human\_message** \(_str_\) – The human message to use. Default is SUFFIX.

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – The input variables to use. Default is None.

  * **\*\*kwargs** \(_Any_\) – Any additional arguments.

Returns:     

An agent.

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