# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/mistralai/chat_models/langchain_mistralai.chat_models.acompletion_with_retry.html
**Word Count:** 15
**Links Count:** 73
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_mistralai.chat\_models.acompletion\_with\_retry\(

    _llm : \_BaseVertexMaasModelGarden_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/model_garden_maas/_base.html#acompletion_with_retry)\#     

Use tenacity to retry the async completion call.

Parameters:     

  * **llm** \(_\_BaseVertexMaasModelGarden_\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page