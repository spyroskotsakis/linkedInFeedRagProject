# MetaProvider — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.oci_generative_ai.MetaProvider.html
**Word Count:** 48
**Links Count:** 269
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# MetaProvider\#

_class _langchain\_community.chat\_models.oci\_generative\_ai.MetaProvider[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider)\#     

Attributes

`stop_sequence_key` |    ---|---      Methods

`__init__`\(\) |    ---|---   `chat_generation_info`\(response\) |    `chat_response_to_text`\(response\) |    `chat_stream_generation_info`\(event\_data\) |    `chat_stream_to_text`\(event\_data\) |    `convert_to_oci_tool`\(tool\) |    `get_role`\(message\) |    `is_chat_stream_end`\(event\_data\) |    `messages_to_oci_params`\(messages, \*\*kwargs\) | Convert LangChain messages to OCI chat parameters.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.__init__)\#     

Return type:     

None

chat\_generation\_info\(

    _response : Any_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.chat_generation_info)\#     

Parameters:     

**response** \(_Any_\)

Return type:     

_Dict_\[str, _Any_\]

chat\_response\_to\_text\(

    _response : Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.chat_response_to_text)\#     

Parameters:     

**response** \(_Any_\)

Return type:     

str

chat\_stream\_generation\_info\(

    _event\_data : Dict_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.chat_stream_generation_info)\#     

Parameters:     

**event\_data** \(_Dict_\)

Return type:     

_Dict_\[str, _Any_\]

chat\_stream\_to\_text\(

    _event\_data : Dict_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.chat_stream_to_text)\#     

Parameters:     

**event\_data** \(_Dict_\)

Return type:     

str

convert\_to\_oci\_tool\(

    _tool : Dict\[str, Any\] | Type\[BaseModel\] | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.convert_to_oci_tool)\#     

Parameters:     

**tool** \(_Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]__|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

_Dict_\[str, _Any_\]

get\_role\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.get_role)\#     

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

Return type:     

str

is\_chat\_stream\_end\(

    _event\_data : Dict_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.is_chat_stream_end)\#     

Parameters:     

**event\_data** \(_Dict_\)

Return type:     

bool

messages\_to\_oci\_params\(

    _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _\*\* kwargs: Any_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#MetaProvider.messages_to_oci_params)\#     

Convert LangChain messages to OCI chat parameters.

Parameters:     

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – List of LangChain BaseMessage objects

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments

Returns:     

Dict containing OCI chat parameters

Raises:     

**ValueError** – If message content is invalid

Return type:     

_Dict_\[str, _Any_\]

__On this page