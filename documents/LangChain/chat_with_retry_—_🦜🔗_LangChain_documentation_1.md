# chat_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.premai.chat_with_retry.html
**Word Count:** 14
**Links Count:** 231
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# chat\_with\_retry\#

langchain\_community.chat\_models.premai.chat\_with\_retry\(

    _llm : [ChatPremAI](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.premai.ChatPremAI.html#langchain_community.chat_models.premai.ChatPremAI "langchain_community.chat_models.premai.ChatPremAI")_,     _project\_id : int_,     _messages : List\[dict\]_,     _stream : bool = False_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/premai.html#chat_with_retry)\#     

Using tenacity for retry in completion call

Parameters:     

  * **llm** \([_ChatPremAI_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.premai.ChatPremAI.html#langchain_community.chat_models.premai.ChatPremAI "langchain_community.chat_models.premai.ChatPremAI")\)

  * **project\_id** \(_int_\)

  * **messages** \(_List_ _\[__dict_ _\]_\)

  * **stream** \(_bool_\)

  * **run\_manager** \([_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page