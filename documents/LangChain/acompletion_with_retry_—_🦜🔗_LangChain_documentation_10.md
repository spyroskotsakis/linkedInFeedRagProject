# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.vertexai.acompletion_with_retry.html
**Word Count:** 14
**Links Count:** 286
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_community.llms.vertexai.acompletion\_with\_retry\(

    _llm : [VertexAI](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.vertexai.VertexAI.html#langchain_community.llms.vertexai.VertexAI "langchain_community.llms.vertexai.VertexAI")_,     _prompt : str_,     _is\_gemini : bool = False_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/vertexai.html#acompletion_with_retry)\#     

Use tenacity to retry the completion call.

Parameters:     

  * **llm** \([_VertexAI_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.vertexai.VertexAI.html#langchain_community.llms.vertexai.VertexAI "langchain_community.llms.vertexai.VertexAI")\)

  * **prompt** \(_str_\)

  * **is\_gemini** \(_bool_\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page