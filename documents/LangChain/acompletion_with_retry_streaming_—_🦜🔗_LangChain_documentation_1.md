# acompletion_with_retry_streaming — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.acompletion_with_retry_streaming.html
**Word Count:** 16
**Links Count:** 286
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# acompletion\_with\_retry\_streaming\#

_async _langchain\_community.llms.fireworks.acompletion\_with\_retry\_streaming\(

    _llm : [Fireworks](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.Fireworks.html#langchain_community.llms.fireworks.Fireworks "langchain_community.llms.fireworks.Fireworks")_,     _use\_retry : bool_,     _\*_ ,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/fireworks.html#acompletion_with_retry_streaming)\#     

Use tenacity to retry the completion call for streaming.

Parameters:     

  * **llm** \([_Fireworks_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.Fireworks.html#langchain_community.llms.fireworks.Fireworks "langchain_community.llms.fireworks.Fireworks")\)

  * **use\_retry** \(_bool_\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)