# acompletion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.acompletion_with_retry.html
**Word Count:** 17
**Links Count:** 233
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# acompletion\_with\_retry\#

_async _langchain\_community.chat\_models.gpt\_router.acompletion\_with\_retry\(

    _llm : [GPTRouter](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouter.html#langchain_community.chat_models.gpt_router.GPTRouter "langchain_community.chat_models.gpt_router.GPTRouter")_,     _models\_priority\_list : List\[[GPTRouterModel](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouterModel.html#langchain_community.chat_models.gpt_router.GPTRouterModel "langchain_community.chat_models.gpt_router.GPTRouterModel")\]_,     _run\_manager : [AsyncCallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → GenerationResponse | AsyncGenerator\[ChunkedGenerationResponse, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/gpt_router.html#acompletion_with_retry)\#     

Use tenacity to retry the async completion call.

Parameters:     

  * **llm** \([_GPTRouter_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouter.html#langchain_community.chat_models.gpt_router.GPTRouter "langchain_community.chat_models.gpt_router.GPTRouter")\)

  * **models\_priority\_list** \(_List_ _\[_[_GPTRouterModel_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouterModel.html#langchain_community.chat_models.gpt_router.GPTRouterModel "langchain_community.chat_models.gpt_router.GPTRouterModel") _\]_\)

  * **run\_manager** \(_Optional_ _\[_[_AsyncCallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun "langchain_core.callbacks.manager.AsyncCallbackManagerForLLMRun") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

Union\[GenerationResponse, AsyncGenerator\[ChunkedGenerationResponse, None\]\]

__On this page