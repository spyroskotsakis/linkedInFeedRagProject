# BaseMessage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html
**Word Count:** 253
**Links Count:** 182
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# BaseMessage\#

_class _langchain\_core.messages.base.BaseMessage[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/base.html#BaseMessage)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Base abstract message class.

Messages are the inputs and outputs of ChatModels.

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

_param _type _: str_ _\[Required\]_\#     

The type of the message. Must be a string that is unique to the message type.

The purpose of this field is to allow for easy identification of the message type when deserializing messages.

pretty\_print\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/base.html#BaseMessage.pretty_print)\#     

Print a pretty representation of the message.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/base.html#BaseMessage.pretty_repr)\#     

Get a pretty representation of the message.

Parameters:     

**html** \(_bool_\) – Whether to format the message as HTML. If True, the message will be formatted with HTML tags. Default is False.

Returns:     

A pretty representation of the message.

Return type:     

str

text\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/base.html#BaseMessage.text)\#     

Get the text content of the message.

Returns:     

The text content of the message.

Return type:     

str

Examples using BaseMessage

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/llm_math_chain/)

  * [Chat Bot Feedback Template](https://python.langchain.com/docs/templates/chat-bot-feedback/)

  * [Discord](https://python.langchain.com/docs/integrations/chat_loaders/discord/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to attach callbacks to a runnable](https://python.langchain.com/docs/how_to/callbacks_attach/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

  * [How to pass callbacks in at runtime](https://python.langchain.com/docs/how_to/callbacks_runtime/)

  * [How to propagate callbacks constructor](https://python.langchain.com/docs/how_to/callbacks_constructor/)

  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [WeChat](https://python.langchain.com/docs/integrations/chat_loaders/wechat/)

__On this page