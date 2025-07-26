# completion_with_retry_batching — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.completion_with_retry_batching.html
**Word Count:** 14
**Links Count:** 286
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# completion\_with\_retry\_batching\#

langchain\_community.llms.fireworks.completion\_with\_retry\_batching\(

    _llm : [Fireworks](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.Fireworks.html#langchain_community.llms.fireworks.Fireworks "langchain_community.llms.fireworks.Fireworks")_,     _use\_retry : bool_,     _\*_ ,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/fireworks.html#completion_with_retry_batching)\#     

Use tenacity to retry the completion call.

Parameters:     

  * **llm** \([_Fireworks_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.Fireworks.html#langchain_community.llms.fireworks.Fireworks "langchain_community.llms.fireworks.Fireworks")\)

  * **use\_retry** \(_bool_\)

  * **run\_manager** \([_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)