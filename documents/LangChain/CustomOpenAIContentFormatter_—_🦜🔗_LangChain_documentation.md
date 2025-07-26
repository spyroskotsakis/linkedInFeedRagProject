# CustomOpenAIContentFormatter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.CustomOpenAIContentFormatter.html
**Word Count:** 75
**Links Count:** 300
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# CustomOpenAIContentFormatter\#

_class _langchain\_community.llms.azureml\_endpoint.CustomOpenAIContentFormatter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#CustomOpenAIContentFormatter)\#     

Content formatter for models that use the OpenAI like API scheme.

Attributes

`accepts` | The MIME type of the response data returned from the endpoint   ---|---   `content_type` | The MIME type of the input data passed to the endpoint   `format_error_msg` |    `supported_api_types` | Supported APIs for the given formatter.      Methods

`escape_special_characters`\(prompt\) | Escapes any special characters in prompt   ---|---   `format_request_payload`\(prompt, model\_kwargs, ...\) | Formats the request according to the chosen api   `format_response_payload`\(output, api\_type\) | Formats response      _static _escape\_special\_characters\(

    _prompt : str_, \) → str\#     

Escapes any special characters in prompt

Parameters:     

**prompt** \(_str_\)

Return type:     

str

format\_request\_payload\(

    _prompt : str_,     _model\_kwargs : Dict_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")_, \) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#CustomOpenAIContentFormatter.format_request_payload)\#     

Formats the request according to the chosen api

Parameters:     

  * **prompt** \(_str_\)

  * **model\_kwargs** \(_Dict_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

bytes

format\_response\_payload\(

    _output : bytes_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")_, \) → [Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#CustomOpenAIContentFormatter.format_response_payload)\#     

Formats response

Parameters:     

  * **output** \(_bytes_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")

Examples using CustomOpenAIContentFormatter

  * [Azure ML](https://python.langchain.com/docs/integrations/llms/azure_ml/)

__On this page