# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.fireworks.acompletion_with_retry.html
**Word Count:** 15
**Links Count:** 231
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_community.chat\_models.fireworks.acompletion\_with\_retry\(

    _llm : [ChatFireworks](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.fireworks.ChatFireworks.html#langchain_community.chat_models.fireworks.ChatFireworks "langchain_community.chat_models.fireworks.ChatFireworks")_,     _use\_retry : bool_,     _\*_ ,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/fireworks.html#acompletion_with_retry)\#     

Use tenacity to retry the async completion call.

Parameters:     

  * **llm** \([_ChatFireworks_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.fireworks.ChatFireworks.html#langchain_community.chat_models.fireworks.ChatFireworks "langchain_community.chat_models.fireworks.ChatFireworks")\)

  * **use\_retry** \(_bool_\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)