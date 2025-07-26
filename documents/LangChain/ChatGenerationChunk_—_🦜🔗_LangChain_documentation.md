# ChatGenerationChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html
**Word Count:** 63
**Links Count:** 117
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# ChatGenerationChunk\#

_class _langchain\_core.outputs.chat\_generation.ChatGenerationChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/chat_generation.html#ChatGenerationChunk)\#     

Bases: [`ChatGeneration`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html#langchain_core.outputs.chat_generation.ChatGeneration "langchain_core.outputs.chat_generation.ChatGeneration")

ChatGeneration chunk.

ChatGeneration chunks can be concatenated with other ChatGeneration chunks.

_param _generation\_info _: dict\[str, Any\] | None_ _ = None_\#     

Raw response from the provider.

May include things like the reason for finishing or token log probabilities.

_param _message _: [BaseMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")_ _\[Required\]_\#     

The message chunk output by the chat model.

_param _text _: str_ _ = ''_\#     

_SHOULD NOT BE SET DIRECTLY_ The text contents of the output message.

_param _type _: Literal\['ChatGenerationChunk'\]__ = 'ChatGenerationChunk'_\#     

Type is used exclusively for serialization purposes.

Examples using ChatGenerationChunk

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page