# completion_with_retry — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.google_palm.completion_with_retry.html
**Word Count:** 14
**Links Count:** 290
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# completion\_with\_retry\#

langchain\_community.llms.google\_palm.completion\_with\_retry\(

    _llm : [GooglePalm](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.google_palm.GooglePalm.html#langchain_community.llms.google_palm.GooglePalm "langchain_community.llms.google_palm.GooglePalm")_,     _prompt : [PromptValue](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") | str | Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") | list\[str\] | tuple\[str, str\] | str | dict\[str, Any\]\]_,     _is\_gemini : bool = False_,     _stream : bool = False_,     _run\_manager : [CallbackManagerForLLMRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/google_palm.html#completion_with_retry)\#     

Use tenacity to retry the completion call.

Parameters:     

  * **llm** \([_GooglePalm_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.google_palm.GooglePalm.html#langchain_community.llms.google_palm.GooglePalm "langchain_community.llms.google_palm.GooglePalm")\)

  * **prompt** \([_PromptValue_](https://python.langchain.com/api_reference/core/prompt_values/langchain_core.prompt_values.PromptValue.html#langchain_core.prompt_values.PromptValue "langchain_core.prompt_values.PromptValue") _|__str_ _|__Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _|__list_ _\[__str_ _\]__|__tuple_ _\[__str_ _,__str_ _\]__|__str_ _|__dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **is\_gemini** \(_bool_\)

  * **stream** \(_bool_\)

  * **run\_manager** \([_CallbackManagerForLLMRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForLLMRun.html#langchain_core.callbacks.manager.CallbackManagerForLLMRun "langchain_core.callbacks.manager.CallbackManagerForLLMRun") _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

__On this page