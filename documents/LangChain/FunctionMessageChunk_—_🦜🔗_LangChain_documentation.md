# FunctionMessageChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.function.FunctionMessageChunk.html
**Word Count:** 158
**Links Count:** 170
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# FunctionMessageChunk\#

_class _langchain\_core.messages.function.FunctionMessageChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/function.html#FunctionMessageChunk)\#     

Bases: [`FunctionMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.function.FunctionMessage.html#langchain_core.messages.function.FunctionMessage "langchain_core.messages.function.FunctionMessage"), [`BaseMessageChunk`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")

Function Message chunk.

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

_param _name _: str_ _\[Required\]_\#     

The name of the function that was executed.

_param _response\_metadata _: dict_ _\[Optional\]_\#     

Response metadata. For example: response headers, logprobs, token counts, model name.

_param _type _: Literal\['FunctionMessageChunk'\]__ = 'FunctionMessageChunk'_\#     

The type of the message \(used for serialization\). Defaults to “FunctionMessageChunk”.

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

Examples using FunctionMessageChunk

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page