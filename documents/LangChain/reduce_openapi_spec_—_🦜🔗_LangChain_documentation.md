# reduce_openapi_spec — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.reduce_openapi_spec.html
**Word Count:** 59
**Links Count:** 163
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# reduce\_openapi\_spec\#

langchain\_community.agent\_toolkits.openapi.spec.reduce\_openapi\_spec\(

    _spec : dict_,     _dereference : bool = True_, \) → [ReducedOpenAPISpec](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec.html#langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec "langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/openapi/spec.html#reduce_openapi_spec)\#     

Simplify/distill/minify a spec somehow.

I want a smaller target for retrieval and \(more importantly\) I want smaller results from retrieval. I was hoping <https://openapi.tools/> would have some useful bits to this end, but doesn’t seem so.

Parameters:     

  * **spec** \(_dict_\) – The OpenAPI spec.

  * **dereference** \(_bool_\) – Whether to dereference the spec. Default is True.

Returns:     

The reduced OpenAPI spec.

Return type:     

[ReducedOpenAPISpec](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec.html#langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec "langchain_community.agent_toolkits.openapi.spec.ReducedOpenAPISpec")

Examples using reduce\_openapi\_spec

  * [OpenAPI Toolkit](https://python.langchain.com/docs/integrations/tools/openapi/)

__On this page