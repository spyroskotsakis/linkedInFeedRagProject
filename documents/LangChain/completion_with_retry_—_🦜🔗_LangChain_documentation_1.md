# completion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.completion_with_retry.html
**Word Count:** 17
**Links Count:** 233
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# completion\_with\_retry\#

langchain\_community.chat\_models.gpt\_router.completion\_with\_retry\(

    _llm : [GPTRouter](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouter.html#langchain_community.chat_models.gpt_router.GPTRouter "langchain_community.chat_models.gpt_router.GPTRouter")_,     _models\_priority\_list : List\[[GPTRouterModel](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouterModel.html#langchain_community.chat_models.gpt_router.GPTRouterModel "langchain_community.chat_models.gpt_router.GPTRouterModel")\]_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → GenerationResponse | Generator\[ChunkedGenerationResponse, None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/gpt_router.html#completion_with_retry)\#     

Use tenacity to retry the completion call.

Parameters:     

  * **llm** \([_GPTRouter_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouter.html#langchain_community.chat_models.gpt_router.GPTRouter "langchain_community.chat_models.gpt_router.GPTRouter")\)

  * **models\_priority\_list** \(_List_ _\[_[_GPTRouterModel_](https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.gpt_router.GPTRouterModel.html#langchain_community.chat_models.gpt_router.GPTRouterModel "langchain_community.chat_models.gpt_router.GPTRouterModel") _\]_\)

  * **run\_manager** \(_Optional_ _\[_[_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

Union\[GenerationResponse, Generator\[ChunkedGenerationResponse, None, None\]\]

__On this page