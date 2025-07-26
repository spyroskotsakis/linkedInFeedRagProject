# create_prem_retry_decorator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.premai.create_prem_retry_decorator.html
**Word Count:** 15
**Links Count:** 231
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# create\_prem\_retry\_decorator\#

langchain\_community.chat\_models.premai.create\_prem\_retry\_decorator\(

    _llm : [ChatPremAI](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.premai.ChatPremAI.html#langchain_community.chat_models.premai.ChatPremAI "langchain_community.chat_models.premai.ChatPremAI")_,     _\*_ ,     _max\_retries : int = 1_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_, \) → Callable\[\[Any\], Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/premai.html#create_prem_retry_decorator)\#     

Create a retry decorator for PremAI API errors.

Parameters:     

  * **llm** \([_ChatPremAI_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.premai.ChatPremAI.html#langchain_community.chat_models.premai.ChatPremAI "langchain_community.chat_models.premai.ChatPremAI")\)

  * **max\_retries** \(_int_\)

  * **run\_manager** \([_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

Return type:     

_Callable_\[\[_Any_\], _Any_\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)