# ConversationalAgent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.conversational.base.ConversationalAgent.html
**Word Count:** 528
**Links Count:** 239
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# ConversationalAgent\#

_class _langchain.agents.conversational.base.ConversationalAgent[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/conversational/base.html#ConversationalAgent)\#     

Bases: [`Agent`](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")

Deprecated since version 0.1.0: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) as well as guides for [Migrating from AgentExecutor](https://python.langchain.com/docs/how_to/migrate_agent/) and LangGraph’s [Pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). It will not be removed until langchain==1.0.

An agent that holds a conversation in addition to using tools.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _ai\_prefix _: str_ _ = 'AI'_\#     

Prefix to use before AI output.

_param _allowed\_tools _: list\[str\] | None_ _ = None_\#     

Allowed tools for the agent. If None, all tools are allowed.

_param _llm\_chain _: [LLMChain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.llm.LLMChain.html#langchain.chains.llm.LLMChain "langchain.chains.llm.LLMChain")_ _\[Required\]_\#     

LLMChain to use for agent.

_param _output\_parser _: [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser")_ _\[Optional\]_\#     

Output parser for the agent.

_classmethod _create\_prompt\(

    _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _prefix : str = 'Assistant is a large language model trained by OpenAI.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n\nAssistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n\nOverall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.\n\nTOOLS:\n------\n\nAssistant has access to the following tools:'_,     _suffix : str = 'Begin\!\n\nPrevious conversation history:\n\{chat\_history\}\n\nNew input: \{input\}\n\{agent\_scratchpad\}'_,     _format\_instructions : str = 'To use a tool, please use the following format:\n\n\`\`\`\nThought: Do I need to use a tool? Yes\nAction: the action to take, should be one of \[\{tool\_names\}\]\nAction Input: the input to the action\nObservation: the result of the action\n\`\`\`\n\nWhen you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:\n\n\`\`\`\nThought: Do I need to use a tool? No\n\{ai\_prefix\}: \[your response here\]\n\`\`\`'_,     _ai\_prefix : str = 'AI'_,     _human\_prefix : str = 'Human'_,     _input\_variables : list\[str\] | None = None_, \) → [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/conversational/base.html#ConversationalAgent.create_prompt)\#     

Create prompt in the style of the zero-shot agent.

Parameters:     

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – List of tools the agent will have access to, used to format the prompt.

  * **prefix** \(_str_\) – String to put before the list of tools. Defaults to PREFIX.

  * **suffix** \(_str_\) – String to put after the list of tools. Defaults to SUFFIX.

  * **format\_instructions** \(_str_\) – Instructions on how to use the tools. Defaults to FORMAT\_INSTRUCTIONS

  * **ai\_prefix** \(_str_\) – String to use before AI output. Defaults to “AI”.

  * **human\_prefix** \(_str_\) – String to use before human output. Defaults to “Human”.

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – List of input variables the final prompt will expect. Defaults to \[“input”, “chat\_history”, “agent\_scratchpad”\].

Returns:     

A PromptTemplate with the template assembled from the pieces here.

Return type:     

[_PromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")

_classmethod _from\_llm\_and\_tools\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _output\_parser : [AgentOutputParser](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") | None = None_,     _prefix : str = 'Assistant is a large language model trained by OpenAI.\n\nAssistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.\n\nAssistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.\n\nOverall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.\n\nTOOLS:\n------\n\nAssistant has access to the following tools:'_,     _suffix : str = 'Begin\!\n\nPrevious conversation history:\n\{chat\_history\}\n\nNew input: \{input\}\n\{agent\_scratchpad\}'_,     _format\_instructions : str = 'To use a tool, please use the following format:\n\n\`\`\`\nThought: Do I need to use a tool? Yes\nAction: the action to take, should be one of \[\{tool\_names\}\]\nAction Input: the input to the action\nObservation: the result of the action\n\`\`\`\n\nWhen you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:\n\n\`\`\`\nThought: Do I need to use a tool? No\n\{ai\_prefix\}: \[your response here\]\n\`\`\`'_,     _ai\_prefix : str = 'AI'_,     _human\_prefix : str = 'Human'_,     _input\_variables : list\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [Agent](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.Agent.html#langchain.agents.agent.Agent "langchain.agents.agent.Agent")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/conversational/base.html#ConversationalAgent.from_llm_and_tools)\#     

Construct an agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A list of tools to use.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – The callback manager to use. Default is None.

  * **output\_parser** \([_AgentOutputParser_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentOutputParser.html#langchain.agents.agent.AgentOutputParser "langchain.agents.agent.AgentOutputParser") _|__None_\) – The output parser to use. Default is None.

  * **prefix** \(_str_\) – The prefix to use in the prompt. Default is PREFIX.

  * **suffix** \(_str_\) – The suffix to use in the prompt. Default is SUFFIX.

  * **format\_instructions** \(_str_\) – The format instructions to use. Default is FORMAT\_INSTRUCTIONS.

  * **ai\_prefix** \(_str_\) – The prefix to use before AI output. Default is “AI”.

  * **human\_prefix** \(_str_\) – The prefix to use before human output. Default is “Human”.

  * **input\_variables** \(_list_ _\[__str_ _\]__|__None_\) – The input variables to use. Default is None.

  * **\*\*kwargs** \(_Any_\) – Any additional keyword arguments to pass to the agent.

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