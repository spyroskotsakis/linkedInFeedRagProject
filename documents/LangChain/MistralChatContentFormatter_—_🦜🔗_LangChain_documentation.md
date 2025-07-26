# MistralChatContentFormatter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.azureml_endpoint.MistralChatContentFormatter.html
**Word Count:** 104
**Links Count:** 253
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# MistralChatContentFormatter\#

_class _langchain\_community.chat\_models.azureml\_endpoint.MistralChatContentFormatter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/azureml_endpoint.html#MistralChatContentFormatter)\#     

Content formatter for Mistral.

Attributes

`SUPPORTED_ROLES` |    ---|---   `accepts` | The MIME type of the response data returned from the endpoint   `content_type` | The MIME type of the input data passed to the endpoint   `format_error_msg` |    `supported_api_types` | Supported APIs for the given formatter.      Methods

`__init__`\(\) |    ---|---   `escape_special_characters`\(prompt\) | Escapes any special characters in prompt   `format_messages_request_payload`\(messages, ...\) | Formats the request according to the chosen api   `format_request_payload`\(prompt, model\_kwargs\) | Formats the request body according to the input schema of the model.   `format_response_payload`\(output\[, api\_type\]\) | Formats response      \_\_init\_\_\(\) → None\#     

Return type:     

None

_static _escape\_special\_characters\(

    _prompt : str_, \) → str\#     

Escapes any special characters in prompt

Parameters:     

**prompt** \(_str_\)

Return type:     

str

format\_messages\_request\_payload\(

    _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _model\_kwargs : Dict_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/azureml_endpoint.html#MistralChatContentFormatter.format_messages_request_payload)\#     

Formats the request according to the chosen api

Parameters:     

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **model\_kwargs** \(_Dict_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

bytes

format\_request\_payload\(

    _prompt : str_,     _model\_kwargs : Dict_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType") = AzureMLEndpointApiType.dedicated_, \) → Any\#     

Formats the request body according to the input schema of the model. Returns bytes or seekable file like object in the format specified in the content\_type request header.

Parameters:     

  * **prompt** \(_str_\)

  * **model\_kwargs** \(_Dict_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

_Any_

format\_response\_payload\(

    _output : bytes_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType") = AzureMLEndpointApiType.dedicated_, \) → [ChatGeneration](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html#langchain_core.outputs.chat_generation.ChatGeneration "langchain_core.outputs.chat_generation.ChatGeneration")\#     

Formats response

Parameters:     

  * **output** \(_bytes_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

[_ChatGeneration_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html#langchain_core.outputs.chat_generation.ChatGeneration "langchain_core.outputs.chat_generation.ChatGeneration")

__On this page