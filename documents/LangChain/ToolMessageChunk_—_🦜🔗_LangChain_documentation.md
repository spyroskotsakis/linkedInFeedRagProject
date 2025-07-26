# ToolMessageChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessageChunk.html
**Word Count:** 229
**Links Count:** 176
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# ToolMessageChunk\#

_class _langchain\_core.messages.tool.ToolMessageChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#ToolMessageChunk)\#     

Bases: [`ToolMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html#langchain_core.messages.tool.ToolMessage "langchain_core.messages.tool.ToolMessage"), [`BaseMessageChunk`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")

Tool Message chunk.

Create a ToolMessage.

Parameters:     

  * **content** – The string contents of the message.

  * **\*\*kwargs** – Additional fields.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Currently inherited from BaseMessage, but not used.

_param _artifact _: Any_ _ = None_\#     

Artifact of the Tool execution which is not meant to be sent to the model.

Should only be specified if it is different from the message content, e.g. if only a subset of the full tool output is being passed as message content but the full output is needed in other parts of the code.

Added in version 0.2.17.

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

Currently inherited from BaseMessage, but not used.

_param _status _: Literal\['success', 'error'\]__ = 'success'_\#     

Status of the tool invocation.

Added in version 0.2.24.

_param _tool\_call\_id _: str_ _\[Required\]_\#     

Tool call that this message is responding to.

_param _type _: Literal\['ToolMessageChunk'\]__ = 'ToolMessageChunk'_\#     

The type of the message \(used for serialization\). Defaults to “tool”.

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

Examples using ToolMessageChunk

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page