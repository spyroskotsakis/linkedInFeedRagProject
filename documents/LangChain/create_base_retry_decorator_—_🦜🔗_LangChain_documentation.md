# create_base_retry_decorator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.llms.create_base_retry_decorator.html
**Word Count:** 58
**Links Count:** 124
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# create\_base\_retry\_decorator\#

langchain\_core.language\_models.llms.create\_base\_retry\_decorator\(

    _error\_types : list\[type\[BaseException\]\]_,     _max\_retries : int = 1_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_, \) → Callable\[\[Any\], Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/language_models/llms.html#create_base_retry_decorator)\#     

Create a retry decorator for a given LLM and provided a list of error types.

Parameters:     

  * **error\_types** \(_list_ _\[__type_ _\[__BaseException_ _\]__\]_\) – List of error types to retry on.

  * **max\_retries** \(_int_\) – Number of retries. Default is 1.

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|_[_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\) – Callback manager for the run. Default is None.

Returns:     

A retry decorator.

Raises:     

**ValueError** – If the cache is not set and cache is True.

Return type:     

_Callable_\[\[_Any_\], _Any_\]

__On this page