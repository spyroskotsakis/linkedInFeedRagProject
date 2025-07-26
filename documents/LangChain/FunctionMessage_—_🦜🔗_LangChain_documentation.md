# FunctionMessage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.function.FunctionMessage.html
**Word Count:** 216
**Links Count:** 169
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# FunctionMessage\#

_class _langchain\_core.messages.function.FunctionMessage[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/function.html#FunctionMessage)\#     

Bases: [`BaseMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

Message for passing the result of executing a tool back to a model.

FunctionMessage are an older version of the ToolMessage schema, and do not contain the tool\_call\_id field.

The tool\_call\_id field is used to associate the tool call request with the tool call response. This is useful in situations where a chat model is able to request multiple tool calls in parallel.

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

_param _type _: Literal\['function'\]__ = 'function'_\#     

The type of the message \(used for serialization\). Defaults to “function”.

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

Examples using FunctionMessage

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page