# create_retry_decorator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.create_retry_decorator.html
**Word Count:** 16
**Links Count:** 255
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# create\_retry\_decorator\#

langchain\_community.utilities.vertexai.create\_retry\_decorator\(

    _llm : [BaseLLM](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.BaseLLM.html#langchain_core.language_models.llms.BaseLLM "langchain_core.language_models.llms.BaseLLM")_,     _\*_ ,     _max\_retries : int = 1_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_, \) → Callable\[\[Any\], Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/vertexai.html#create_retry_decorator)\#     

Create a retry decorator for Vertex / Palm LLMs.

Parameters:     

  * **llm** \([_BaseLLM_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.BaseLLM.html#langchain_core.language_models.llms.BaseLLM "langchain_core.language_models.llms.BaseLLM")\)

  * **max\_retries** \(_int_\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|_[_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

Return type:     

_Callable_\[\[_Any_\], _Any_\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)