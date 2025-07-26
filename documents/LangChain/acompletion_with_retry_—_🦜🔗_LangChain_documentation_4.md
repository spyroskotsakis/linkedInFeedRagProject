# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.openai.acompletion_with_retry.html
**Word Count:** 15
**Links Count:** 231
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_community.chat\_models.openai.acompletion\_with\_retry\(

    _llm : [ChatOpenAI](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.openai.ChatOpenAI.html#langchain_community.chat_models.openai.ChatOpenAI "langchain_community.chat_models.openai.ChatOpenAI")_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/openai.html#acompletion_with_retry)\#     

Use tenacity to retry the async completion call.

Parameters:     

  * **llm** \([_ChatOpenAI_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.openai.ChatOpenAI.html#langchain_community.chat_models.openai.ChatOpenAI "langchain_community.chat_models.openai.ChatOpenAI")\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page