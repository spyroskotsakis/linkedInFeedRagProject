# ChatMessageChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.chat.ChatMessageChunk.html
**Word Count:** 181
**Links Count:** 171
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# ChatMessageChunk\#

_class _langchain\_core.messages.chat.ChatMessageChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/chat.html#ChatMessageChunk)\#     

Bases: [`ChatMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.chat.ChatMessage.html#langchain_core.messages.chat.ChatMessage "langchain_core.messages.chat.ChatMessage"), [`BaseMessageChunk`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")

Chat Message chunk.

Pass in content as positional arg.

Parameters:     

**content** – The string contents of the message.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Reserved for additional payload data associated with the message.

For example, for a message from an AI, this could include tool calls as encoded by the model provider.

_param _content _: str | list\[str | dict\]__\[Required\]_\#     

The string contents of the message.

_param _id _: str | None_ _ = None_\#     

An optional unique identifier for the message. This should ideally be provided by the provider/model which created the message.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _name _: str | None_ _ = None_\#     

An optional name for the message.

This can be used to provide a human-readable name for the message.

Usage of this field is optional, and whether it’s used or not is up to the model implementation.

_param _response\_metadata _: dict_ _\[Optional\]_\#     

Response metadata. For example: response headers, logprobs, token counts, model name.

_param _role _: str_ _\[Required\]_\#     

The speaker / role of the Message.

_param _type _: Literal\['ChatMessageChunk'\]__ = 'ChatMessageChunk'_\#     

The type of the message \(used during serialization\). Defaults to “ChatMessageChunk”.

pretty\_print\(\) → None\#     

Print a pretty representation of the message.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str\#     

Get a pretty representation of the message.

Parameters:     

**html** \(_bool_\) – Whether to format the message as HTML. If True, the message will be formatted with HTML tags. Default is False.

Returns:     

A pretty representation of the message.

Return type:     

str

text\(\) → str\#     

Get the text content of the message.

Returns:     

The text content of the message.

Return type:     

str

__On this page