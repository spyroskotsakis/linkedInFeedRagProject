# completion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.completion_with_retry.html
**Word Count:** 14
**Links Count:** 288
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# completion\_with\_retry\#

langchain\_community.llms.openai.completion\_with\_retry\(

    _llm : [BaseOpenAI](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.BaseOpenAI.html#langchain_community.llms.openai.BaseOpenAI "langchain_community.llms.openai.BaseOpenAI") | [OpenAIChat](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.OpenAIChat.html#langchain_community.llms.openai.OpenAIChat "langchain_community.llms.openai.OpenAIChat")_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/openai.html#completion_with_retry)\#     

Use tenacity to retry the completion call.

Parameters:     

  * **llm** \([_BaseOpenAI_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.BaseOpenAI.html#langchain_community.llms.openai.BaseOpenAI "langchain_community.llms.openai.BaseOpenAI") _|_[_OpenAIChat_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openai.OpenAIChat.html#langchain_community.llms.openai.OpenAIChat "langchain_community.llms.openai.OpenAIChat")\)

  * **run\_manager** \([_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page