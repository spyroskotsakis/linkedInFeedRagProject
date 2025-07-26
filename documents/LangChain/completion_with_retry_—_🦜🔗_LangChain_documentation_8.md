# completion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.vertexai.completion_with_retry.html
**Word Count:** 14
**Links Count:** 286
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# completion\_with\_retry\#

langchain\_community.llms.vertexai.completion\_with\_retry\(

    _llm : [VertexAI](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.vertexai.VertexAI.html#langchain_community.llms.vertexai.VertexAI "langchain_community.llms.vertexai.VertexAI")_,     _prompt : List\[str | 'Image'\]_,     _stream : bool = False_,     _is\_gemini : bool = False_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/vertexai.html#completion_with_retry)\#     

Use tenacity to retry the completion call.

Parameters:     

  * **llm** \([_VertexAI_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.vertexai.VertexAI.html#langchain_community.llms.vertexai.VertexAI "langchain_community.llms.vertexai.VertexAI")\)

  * **prompt** \(_List_ _\[__Union_ _\[__str_ _,__'Image'__\]__\]_\)

  * **stream** \(_bool_\)

  * **is\_gemini** \(_bool_\)

  * **run\_manager** \(_Optional_ _\[_[_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

Any

__On this page