# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.acompletion_with_retry.html
**Word Count:** 15
**Links Count:** 288
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_community.llms.openai.acompletion\_with\_retry\(

    _llm : [BaseOpenAI](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.BaseOpenAI.html#langchain_community.llms.openai.BaseOpenAI "langchain_community.llms.openai.BaseOpenAI") | [OpenAIChat](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.OpenAIChat.html#langchain_community.llms.openai.OpenAIChat "langchain_community.llms.openai.OpenAIChat")_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/openai.html#acompletion_with_retry)\#     

Use tenacity to retry the async completion call.

Parameters:     

  * **llm** \([_BaseOpenAI_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.BaseOpenAI.html#langchain_community.llms.openai.BaseOpenAI "langchain_community.llms.openai.BaseOpenAI") _|_[_OpenAIChat_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.OpenAIChat.html#langchain_community.llms.openai.OpenAIChat "langchain_community.llms.openai.OpenAIChat")\)

  * **run\_manager** \([_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page