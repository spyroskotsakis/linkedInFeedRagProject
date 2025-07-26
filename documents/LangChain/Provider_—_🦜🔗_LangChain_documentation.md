# Provider — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.oci_generative_ai.Provider.html
**Word Count:** 16
**Links Count:** 263
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# Provider\#

_class _langchain\_community.chat\_models.oci\_generative\_ai.Provider[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider)\#     

Attributes

`stop_sequence_key` |    ---|---      Methods

`chat_generation_info`\(response\) |    ---|---   `chat_response_to_text`\(response\) |    `chat_stream_generation_info`\(event\_data\) |    `chat_stream_to_text`\(event\_data\) |    `convert_to_oci_tool`\(tool\) |    `get_role`\(message\) |    `is_chat_stream_end`\(event\_data\) |    `messages_to_oci_params`\(messages, \*\*kwargs\) |       _abstractmethod _chat\_generation\_info\(

    _response : Any_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.chat_generation_info)\#     

Parameters:     

**response** \(_Any_\)

Return type:     

_Dict_\[str, _Any_\]

_abstractmethod _chat\_response\_to\_text\(_response : Any_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.chat_response_to_text)\#     

Parameters:     

**response** \(_Any_\)

Return type:     

str

_abstractmethod _chat\_stream\_generation\_info\(

    _event\_data : Dict_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.chat_stream_generation_info)\#     

Parameters:     

**event\_data** \(_Dict_\)

Return type:     

_Dict_\[str, _Any_\]

_abstractmethod _chat\_stream\_to\_text\(

    _event\_data : Dict_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.chat_stream_to_text)\#     

Parameters:     

**event\_data** \(_Dict_\)

Return type:     

str

_abstractmethod _convert\_to\_oci\_tool\(

    _tool : Dict\[str, Any\] | Type\[BaseModel\] | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.convert_to_oci_tool)\#     

Parameters:     

**tool** \(_Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]__|__Callable_ _|_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\)

Return type:     

_Dict_\[str, _Any_\]

_abstractmethod _get\_role\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.get_role)\#     

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

Return type:     

str

_abstractmethod _is\_chat\_stream\_end\(

    _event\_data : Dict_, \) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.is_chat_stream_end)\#     

Parameters:     

**event\_data** \(_Dict_\)

Return type:     

bool

_abstractmethod _messages\_to\_oci\_params\(

    _messages : Any_,     _\*\* kwargs: Any_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/oci_generative_ai.html#Provider.messages_to_oci_params)\#     

Parameters:     

  * **messages** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page