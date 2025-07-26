# ChatGeneration — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html
**Word Count:** 112
**Links Count:** 118
**Scraped:** 2025-07-21 07:54:30
**Status:** completed

---

# ChatGeneration\#

_class _langchain\_core.outputs.chat\_generation.ChatGeneration[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/chat_generation.html#ChatGeneration)\#     

Bases: [`Generation`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")

A single chat generation output.

A subclass of Generation that represents the response from a chat model that generates chat messages.

The message attribute is a structured representation of the chat message. Most of the time, the message will be of type AIMessage.

Users working with chat models will usually access information via either AIMessage \(returned from runnable interfaces\) or LLMResult \(available via callbacks\).

_param _generation\_info _: dict\[str, Any\] | None_ _ = None_\#     

Raw response from the provider.

May include things like the reason for finishing or token log probabilities.

_param _message _: [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_ _\[Required\]_\#     

The message output by the chat model.

_param _text _: str_ _ = ''_\#     

_SHOULD NOT BE SET DIRECTLY_ The text contents of the output message.

_param _type _: Literal\['ChatGeneration'\]__ = 'ChatGeneration'_\#     

Type is used exclusively for serialization purposes.

Examples using ChatGeneration

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page