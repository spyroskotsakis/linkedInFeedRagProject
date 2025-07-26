# create_json_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.base.create_json_agent.html
**Word Count:** 98
**Links Count:** 168
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# create\_json\_agent\#

langchain\_community.agent\_toolkits.json.base.create\_json\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [JsonToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.toolkit.JsonToolkit.html#langchain_community.agent_toolkits.json.toolkit.JsonToolkit "langchain_community.agent_toolkits.json.toolkit.JsonToolkit")_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str = 'You are an agent designed to interact with JSON.\nYour goal is to return a final answer by interacting with the JSON.\nYou have access to the following tools which help you learn more about the JSON you are interacting with.\nOnly use the below tools. Only use the information returned by the below tools to construct your final answer.\nDo not make up any information that is not contained in the JSON.\nYour input to the tools should be in the form of \`data\["key"\]\[0\]\` where \`data\` is the JSON blob you are interacting with, and the syntax used is Python. \nYou should only use keys that you know for a fact exist. You must validate that a key exists by seeing it previously when calling \`json\_spec\_list\_keys\`. \nIf you have not seen a key in one of those responses, you cannot use it.\nYou should only add one key at a time to the path. You cannot add multiple keys at once.\nIf you encounter a "KeyError", go back to the previous key, look at the available keys, and try again.\n\nIf the question does not seem to be related to the JSON, just return "I don\'t know" as the answer.\nAlways begin your interaction with the \`json\_spec\_list\_keys\` tool with input "data" to see what keys exist in the JSON.\n\nNote that sometimes the value at a given path is large. In this case, you will get an error "Value is a large dictionary, should explore its keys directly".\nIn this case, you should ALWAYS follow up by using the \`json\_spec\_list\_keys\` tool to see what keys exist at that path.\nDo not simply refer the user to the JSON or a section of the JSON, as this is not a valid answer. Keep digging until you find the answer and explicitly return it.\n'_,     _suffix : str = 'Begin\!"\n\nQuestion: \{input\}\nThought: I should look at the keys that exist in data to see what I have access to\n\{agent\_scratchpad\}'_,     _format\_instructions : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _verbose : bool = False_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/json/base.html#create_json_agent)\#     

Construct a json agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **toolkit** \([_JsonToolkit_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.toolkit.JsonToolkit.html#langchain_community.agent_toolkits.json.toolkit.JsonToolkit "langchain_community.agent_toolkits.json.toolkit.JsonToolkit")\) – The toolkit to use.

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]_\) – The callback manager to use. Default is None.

  * **prefix** \(_str_\) – The prefix to use. Default is JSON\_PREFIX.

  * **suffix** \(_str_\) – The suffix to use. Default is JSON\_SUFFIX.

  * **format\_instructions** \(_Optional_ _\[__str_ _\]_\) – The format instructions to use. Default is None.

  * **input\_variables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – The input variables to use. Default is None.

  * **verbose** \(_bool_\) – Whether to print verbose output. Default is False.

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional additional arguments for the agent executor.

  * **kwargs** \(_Any_\) – Additional arguments for the agent.

Returns:     

The agent executor.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Examples using create\_json\_agent

  * [JSON Toolkit](https://python.langchain.com/docs/integrations/tools/json/)

__On this page