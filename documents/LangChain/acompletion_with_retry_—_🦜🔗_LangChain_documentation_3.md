# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.litellm.acompletion_with_retry.html
**Word Count:** 15
**Links Count:** 231
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_community.chat\_models.litellm.acompletion\_with\_retry\(

    _llm : [ChatLiteLLM](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.litellm.ChatLiteLLM.html#langchain_community.chat_models.litellm.ChatLiteLLM "langchain_community.chat_models.litellm.ChatLiteLLM")_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/litellm.html#acompletion_with_retry)\#     

Use tenacity to retry the async completion call.

Parameters:     

  * **llm** \([_ChatLiteLLM_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.litellm.ChatLiteLLM.html#langchain_community.chat_models.litellm.ChatLiteLLM "langchain_community.chat_models.litellm.ChatLiteLLM")\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page