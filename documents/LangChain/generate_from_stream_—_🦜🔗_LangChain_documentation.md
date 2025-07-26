# generate_from_stream — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.generate_from_stream.html
**Word Count:** 16
**Links Count:** 124
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# generate\_from\_stream\#

langchain\_core.language\_models.chat\_models.generate\_from\_stream\(

    _stream : Iterator\[[ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk")\]_, \) → [ChatResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_result.ChatResult.html#langchain_core.outputs.chat_result.ChatResult "langchain_core.outputs.chat_result.ChatResult")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/language_models/chat_models.html#generate_from_stream)\#     

Generate from a stream.

Parameters:     

**stream** \(_Iterator_ _\[_[_ChatGenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") _\]_\) – Iterator of ChatGenerationChunk.

Returns:     

Chat result.

Return type:     

[ChatResult](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_result.ChatResult.html#langchain_core.outputs.chat_result.ChatResult "langchain_core.outputs.chat_result.ChatResult")

__On this page