# create_openapi_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.base.create_openapi_agent.html
**Word Count:** 200
**Links Count:** 169
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# create\_openapi\_agent\#

langchain\_community.agent\_toolkits.openapi.base.create\_openapi\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [OpenAPIToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit.html#langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit "langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit")_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str = "You are an agent designed to answer questions by making web requests to an API given the openapi spec.\n\nIf the question does not seem related to the API, return I don't know. Do not make up an answer.\nOnly use information provided by the tools to construct your response.\n\nFirst, find the base URL needed to make the request.\n\nSecond, find the relevant paths needed to answer the question. Take note that, sometimes, you might need to make more than one request to more than one path to answer the question.\n\nThird, find the required parameters needed to make the request. For GET requests, these are usually URL parameters and for POST requests, these are request body parameters.\n\nFourth, make the requests needed to answer the question. Ensure that you are sending the correct parameters to the request by checking which parameters are required. For parameters with a fixed set of values, please use the spec to look at which values are allowed.\n\nUse the exact parameter names as listed in the spec, do not make up any names or abbreviate the names of parameters.\nIf you get a not found error, ensure that you are using a path that actually exists in the spec.\n"_,     _suffix : str = 'Begin\!\n\nQuestion: \{input\}\nThought: I should explore the spec to find the base server url for the API in the servers node.\n\{agent\_scratchpad\}'_,     _format\_instructions : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _max\_iterations : int | None = 15_,     _max\_execution\_time : float | None = None_,     _early\_stopping\_method : str = 'force'_,     _verbose : bool = False_,     _return\_intermediate\_steps : bool = False_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/base.html#create_openapi_agent)\#     

Construct an OpenAPI agent from an LLM and tools.

_Security Note_ : When creating an OpenAPI agent, check the permissions     

and capabilities of the underlying toolkit.

For example, if the default implementation of OpenAPIToolkit uses the RequestsToolkit which contains tools to make arbitrary network requests against any URL \(e.g., GET, POST, PATCH, PUT, DELETE\),

Control access to who can submit issue requests using this toolkit and what network access it has.

See <https://python.langchain.com/docs/security> for more information.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **toolkit** \([_OpenAPIToolkit_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit.html#langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit "langchain_community.agent_toolkits.openapi.toolkit.OpenAPIToolkit")\) – The OpenAPI toolkit.

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]_\) – Optional. The callback manager. Default is None.

  * **prefix** \(_str_\) – Optional. The prefix for the prompt. Default is OPENAPI\_PREFIX.

  * **suffix** \(_str_\) – Optional. The suffix for the prompt. Default is OPENAPI\_SUFFIX.

  * **format\_instructions** \(_Optional_ _\[__str_ _\]_\) – Optional. The format instructions for the prompt. Default is None.

  * **input\_variables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The input variables for the prompt. Default is None.

  * **max\_iterations** \(_Optional_ _\[__int_ _\]_\) – Optional. The maximum number of iterations. Default is 15.

  * **max\_execution\_time** \(_Optional_ _\[__float_ _\]_\) – Optional. The maximum execution time. Default is None.

  * **early\_stopping\_method** \(_str_\) – Optional. The early stopping method. Default is “force”.

  * **verbose** \(_bool_\) – Optional. Whether to print verbose output. Default is False.

  * **return\_intermediate\_steps** \(_bool_\) – Optional. Whether to return intermediate steps. Default is False.

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional. Additional keyword arguments for the agent executor.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The agent executor.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Examples using create\_openapi\_agent

  * [OpenAPI Toolkit](https://python.langchain.com/docs/integrations/tools/openapi/)

__On this page