# AIMessageChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html
**Word Count:** 260
**Links Count:** 186
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# AIMessageChunk\#

_class _langchain\_core.messages.ai.AIMessageChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#AIMessageChunk)\#     

Bases: [`AIMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage"), [`BaseMessageChunk`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessageChunk.html#langchain_core.messages.base.BaseMessageChunk "langchain_core.messages.base.BaseMessageChunk")

Message chunk from an AI.

Pass in content as positional arg.

Parameters:     

  * **content** – The content of the message.

  * **kwargs** – Additional arguments to pass to the parent class.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Reserved for additional payload data associated with the message.

For example, for a message from an AI, this could include tool calls as encoded by the model provider.

_param _content _: str | list\[str | dict\]__\[Required\]_\#     

The string contents of the message.

_param _example _: bool_ _ = False_\#     

Use to denote that a message is part of an example conversation.

At the moment, this is ignored by most models. Usage is discouraged.

_param _id _: str | None_ _ = None_\#     

An optional unique identifier for the message. This should ideally be provided by the provider/model which created the message.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _invalid\_tool\_calls _: list\[[InvalidToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")\]__ = \[\]_\#     

If provided, tool calls with parsing errors associated with the message.

_param _name _: str | None_ _ = None_\#     

An optional name for the message.

This can be used to provide a human-readable name for the message.

Usage of this field is optional, and whether it’s used or not is up to the model implementation.

_param _response\_metadata _: dict_ _\[Optional\]_\#     

Response metadata. For example: response headers, logprobs, token counts, model name.

_param _tool\_call\_chunks _: list\[[ToolCallChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCallChunk.html#langchain_core.messages.tool.ToolCallChunk "langchain_core.messages.tool.ToolCallChunk")\]__ = \[\]_\#     

If provided, tool call chunks associated with the message.

_param _tool\_calls _: list\[[ToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall "langchain_core.messages.tool.ToolCall")\]__ = \[\]_\#     

If provided, tool calls associated with the message.

_param _type _: Literal\['AIMessageChunk'\]__ = 'AIMessageChunk'_\#     

The type of the message \(used for deserialization\). Defaults to “AIMessageChunk”.

_param _usage\_metadata _: [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") | None_ _ = None_\#     

If provided, usage metadata for a message, such as token counts.

This is a standard representation of token usage that is consistent across models.

pretty\_print\(\) → None\#     

Print a pretty representation of the message.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str\#     

Return a pretty representation of the message.

Parameters:     

**html** \(_bool_\) – Whether to return an HTML-formatted string. Defaults to False.

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

Examples using AIMessageChunk

  * [Google Cloud Vertex AI](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm/)

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page