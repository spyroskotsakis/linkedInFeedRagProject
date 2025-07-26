# LLMManagerMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.LLMManagerMixin.html
**Word Count:** 162
**Links Count:** 154
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# LLMManagerMixin\#

_class _langchain\_core.callbacks.base.LLMManagerMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#LLMManagerMixin)\#     

Mixin for LLM callbacks.

Methods

`on_llm_end`\(response, \*, run\_id\[, parent\_run\_id\]\) | Run when LLM ends running.   ---|---   `on_llm_error`\(error, \*, run\_id\[, parent\_run\_id\]\) | Run when LLM errors.   `on_llm_new_token`\(token, \*\[, chunk, ...\]\) | Run on new LLM token.      on\_llm\_end\(

    _response : [LLMResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#LLMManagerMixin.on_llm_end)\#     

Run when LLM ends running.

Parameters:     

  * **response** \([_LLMResult_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult")\) – The response which was generated.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_llm\_error\(

    _error : BaseException_,     _\*_ ,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#LLMManagerMixin.on_llm_error)\#     

Run when LLM errors.

Parameters:     

  * **error** \(_BaseException_\) – The error that occurred.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

on\_llm\_new\_token\(

    _token : str_,     _\*_ ,     _chunk : [GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") | None = None_,     _run\_id : UUID_,     _parent\_run\_id : UUID | None = None_,     _\*\* kwargs: Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/callbacks/base.html#LLMManagerMixin.on_llm_new_token)\#     

Run on new LLM token. Only available when streaming is enabled.

Parameters:     

  * **token** \(_str_\) – The new token.

  * **chunk** \([_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") _|_[_ChatGenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk")\) – The new generated chunk, containing content and other information.

  * **run\_id** \(_UUID_\) – The run ID. This is the ID of the current run.

  * **parent\_run\_id** \(_UUID_\) – The parent run ID. This is the ID of the parent run.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Return type:     

Any

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)