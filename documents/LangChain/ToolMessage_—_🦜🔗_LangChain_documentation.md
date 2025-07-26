# ToolMessage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolMessage.html
**Word Count:** 386
**Links Count:** 188
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# ToolMessage\#

_class _langchain\_core.messages.tool.ToolMessage[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#ToolMessage)\#     

Bases: [`BaseMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage"), [`ToolOutputMixin`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolOutputMixin.html#langchain_core.messages.tool.ToolOutputMixin "langchain_core.messages.tool.ToolOutputMixin")

Message for passing the result of executing a tool back to a model.

ToolMessages contain the result of a tool invocation. Typically, the result is encoded inside the content field.

Example: A ToolMessage representing a result of 42 from a tool call with id

>  >     from langchain_core.messages import ToolMessage >      >     ToolMessage(content='42', tool_call_id='call_Jja7J89XsjrOLA5r!MEOW!SL') >     

Example: A ToolMessage where only part of the tool output is sent to the model     

and the full output is passed in to artifact.

Added in version 0.2.17.               from langchain_core.messages import ToolMessage          tool_output = {         "stdout": "From the graph we can see that the correlation between x and y is ...",         "stderr": None,         "artifacts": {"type": "image", "base64_data": "/9j/4gIcSU..."},     }          ToolMessage(         content=tool_output["stdout"],         artifact=tool_output,         tool_call_id='call_Jja7J89XsjrOLA5r!MEOW!SL',     )     

The tool\_call\_id field is used to associate the tool call request with the tool call response. This is useful in situations where a chat model is able to request multiple tool calls in parallel.

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

_param _type _: Literal\['tool'\]__ = 'tool'_\#     

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

Examples using ToolMessage

  * [ChatPremAI](https://python.langchain.com/docs/integrations/chat/premai/)

  * [Cohere](https://python.langchain.com/docs/integrations/providers/cohere/)

  * [Eden AI](https://python.langchain.com/docs/integrations/chat/edenai/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)

  * [How to do tool/function calling](https://python.langchain.com/docs/how_to/function_calling/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

  * [How to return structured data from a model](https://python.langchain.com/docs/how_to/structured_output/)

  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

  * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [PremAI](https://python.langchain.com/docs/integrations/providers/premai/)

__On this page