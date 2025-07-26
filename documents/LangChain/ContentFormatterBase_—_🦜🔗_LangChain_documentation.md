# ContentFormatterBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.ContentFormatterBase.html
**Word Count:** 129
**Links Count:** 301
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# ContentFormatterBase\#

_class _langchain\_community.llms.azureml\_endpoint.ContentFormatterBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#ContentFormatterBase)\#     

Transform request and response of AzureML endpoint to match with required schema.

Attributes

`accepts` | The MIME type of the response data returned from the endpoint   ---|---   `content_type` | The MIME type of the input data passed to the endpoint   `format_error_msg` |    `supported_api_types` | Supported APIs for the given formatter.      Methods

`escape_special_characters`\(prompt\) | Escapes any special characters in prompt   ---|---   `format_request_payload`\(prompt, model\_kwargs\) | Formats the request body according to the input schema of the model.   `format_response_payload`\(output\[, api\_type\]\) | Formats the response body according to the output schema of the model.      _static _escape\_special\_characters\(

    _prompt : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#ContentFormatterBase.escape_special_characters)\#     

Escapes any special characters in prompt

Parameters:     

**prompt** \(_str_\)

Return type:     

str

format\_request\_payload\(

    _prompt : str_,     _model\_kwargs : Dict_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType") = AzureMLEndpointApiType.dedicated_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#ContentFormatterBase.format_request_payload)\#     

Formats the request body according to the input schema of the model. Returns bytes or seekable file like object in the format specified in the content\_type request header.

Parameters:     

  * **prompt** \(_str_\)

  * **model\_kwargs** \(_Dict_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

_Any_

_abstractmethod _format\_response\_payload\(

    _output : bytes_,     _api\_type : [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType") = AzureMLEndpointApiType.dedicated_, \) → [Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#ContentFormatterBase.format_response_payload)\#     

Formats the response body according to the output schema of the model. Returns the data type that is received from the response.

Parameters:     

  * **output** \(_bytes_\)

  * **api\_type** \([_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")\)

Return type:     

[_Generation_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")

Examples using ContentFormatterBase

  * [Azure ML](https://python.langchain.com/docs/integrations/llms/azure_ml/)

__On this page