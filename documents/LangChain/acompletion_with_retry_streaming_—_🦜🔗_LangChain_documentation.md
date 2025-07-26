# acompletion_with_retry_streaming — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.fireworks.acompletion_with_retry_streaming.html
**Word Count:** 16
**Links Count:** 231
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# acompletion\_with\_retry\_streaming\#

_async _langchain\_community.chat\_models.fireworks.acompletion\_with\_retry\_streaming\(

    _llm : [ChatFireworks](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.fireworks.ChatFireworks.html#langchain_community.chat_models.fireworks.ChatFireworks "langchain_community.chat_models.fireworks.ChatFireworks")_,     _use\_retry : bool_,     _\*_ ,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/fireworks.html#acompletion_with_retry_streaming)\#     

Use tenacity to retry the completion call for streaming.

Parameters:     

  * **llm** \([_ChatFireworks_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.fireworks.ChatFireworks.html#langchain_community.chat_models.fireworks.ChatFireworks "langchain_community.chat_models.fireworks.ChatFireworks")\)

  * **use\_retry** \(_bool_\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)