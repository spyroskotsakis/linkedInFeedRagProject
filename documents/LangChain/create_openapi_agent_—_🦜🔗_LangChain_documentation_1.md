# create_openapi_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.planner.create_openapi_agent.html
**Word Count:** 185
**Links Count:** 169
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# create\_openapi\_agent\#

langchain\_community.agent\_toolkits.openapi.planner.create\_openapi\_agent\(

    _api\_spec : [ReducedOpenAPISpec](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec.html#langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec "langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec")_,     _requests\_wrapper : [TextRequestsWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html#langchain_community.utilities.requests.TextRequestsWrapper "langchain_community.utilities.requests.TextRequestsWrapper")_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _shared\_memory : Any | None = None_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _verbose : bool = True_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _allow\_dangerous\_requests : bool = False_,     _allowed\_operations : Sequence\[Literal\['GET', 'POST', 'PUT', 'DELETE', 'PATCH'\]\] = \('GET', 'POST'\)_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/planner.html#create_openapi_agent)\#     

Construct an OpenAI API planner and controller for a given spec.

Inject credentials via requests\_wrapper.

We use a top-level “orchestrator” agent to invoke the planner and controller, rather than a top-level planner that invokes a controller with its plan. This is to keep the planner simple.

You need to set allow\_dangerous\_requests to True to use Agent with BaseRequestsTool. Requests can be dangerous and can lead to security vulnerabilities. For example, users can ask a server to make a request to an internal server. It’s recommended to use requests through a proxy server and avoid accepting inputs from untrusted sources without proper sandboxing. Please see: <https://python.langchain.com/docs/security> for further security information.

Parameters:     

  * **api\_spec** \([_ReducedOpenAPISpec_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec.html#langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec "langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec")\) – The OpenAPI spec.

  * **requests\_wrapper** \([_TextRequestsWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.TextRequestsWrapper.html#langchain_community.utilities.requests.TextRequestsWrapper "langchain_community.utilities.requests.TextRequestsWrapper")\) – The requests wrapper.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model.

  * **shared\_memory** \(_Any_ _|__None_\) – Optional. The shared memory. Default is None.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Optional. The callback manager. Default is None.

  * **verbose** \(_bool_\) – Optional. Whether to print verbose output. Default is True.

  * **agent\_executor\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Additional keyword arguments for the agent executor.

  * **allow\_dangerous\_requests** \(_bool_\) – Optional. Whether to allow dangerous requests. Default is False.

  * **allowed\_operations** \(_Sequence_ _\[__Literal_ _\[__'GET'__,__'POST'__,__'PUT'__,__'DELETE'__,__'PATCH'__\]__\]_\) – Optional. The allowed operations. Default is \(“GET”, “POST”\).

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The agent executor.

Return type:     

_Any_

Examples using create\_openapi\_agent

  * [OpenAPI Toolkit](https://python.langchain.com/docs/integrations/tools/openapi/)

__On this page