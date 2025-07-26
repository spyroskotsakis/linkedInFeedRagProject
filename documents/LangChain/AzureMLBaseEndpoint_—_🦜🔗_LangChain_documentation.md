# AzureMLBaseEndpoint — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLBaseEndpoint.html
**Word Count:** 160
**Links Count:** 314
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# AzureMLBaseEndpoint\#

_class _langchain\_community.llms.azureml\_endpoint.AzureMLBaseEndpoint[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLBaseEndpoint)\#     

Bases: `BaseModel`

Azure ML Online Endpoint models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _content\_formatter _: Any_ _ = None_\#     

The content formatter that provides an input and output transform function to handle formats between the LLM and the endpoint

_param _deployment\_name _: str_ _ = ''_\#     

Deployment Name for Endpoint. NOT REQUIRED to call endpoint. Should be passed to constructor or specified as env var AZUREML\_DEPLOYMENT\_NAME.

_param _endpoint\_api\_key _: SecretStr_ _ = SecretStr\(''\)_\#     

Authentication Key for Endpoint. Should be passed to constructor or specified as env var AZUREML\_ENDPOINT\_API\_KEY.

_param _endpoint\_api\_type _: [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")_ _ = AzureMLEndpointApiType.dedicated_\#     

Type of the endpoint being consumed. Possible values are serverless for pay-as-you-go and dedicated for dedicated endpoints.

_param _endpoint\_url _: str_ _ = ''_\#     

URL of pre-existing Endpoint. Should be passed to constructor or specified as env var AZUREML\_ENDPOINT\_URL.

_param _max\_retries _: int_ _ = 1_\#     

_param _model\_kwargs _: dict | None_ _ = None_\#     

Keyword arguments to pass to the model.

_param _timeout _: int_ _ = 50_\#     

Request timeout for calls to the endpoint

_classmethod _validate\_client\(

    _field\_value : Any_,     _values : Dict_, \) → [AzureMLEndpointClient](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointClient.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointClient "langchain_community.llms.azureml_endpoint.AzureMLEndpointClient")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLBaseEndpoint.validate_client)\#     

Validate that api key and python package exists in environment.

Parameters:     

  * **field\_value** \(_Any_\)

  * **values** \(_Dict_\)

Return type:     

[_AzureMLEndpointClient_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointClient.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointClient "langchain_community.llms.azureml_endpoint.AzureMLEndpointClient")

_classmethod _validate\_content\_formatter\(

    _field\_value : Any_,     _values : Dict_, \) → [ContentFormatterBase](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.ContentFormatterBase.html#langchain_community.llms.azureml_endpoint.ContentFormatterBase "langchain_community.llms.azureml_endpoint.ContentFormatterBase")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLBaseEndpoint.validate_content_formatter)\#     

Validate that content formatter is supported by endpoint type.

Parameters:     

  * **field\_value** \(_Any_\)

  * **values** \(_Dict_\)

Return type:     

[_ContentFormatterBase_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.ContentFormatterBase.html#langchain_community.llms.azureml_endpoint.ContentFormatterBase "langchain_community.llms.azureml_endpoint.ContentFormatterBase")

_classmethod _validate\_endpoint\_api\_type\(

    _field\_value : Any_,     _values : Dict_, \) → [AzureMLEndpointApiType](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/azureml_endpoint.html#AzureMLBaseEndpoint.validate_endpoint_api_type)\#     

Validate that endpoint api type is compatible with the URL format.

Parameters:     

  * **field\_value** \(_Any_\)

  * **values** \(_Dict_\)

Return type:     

[_AzureMLEndpointApiType_](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType.html#langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType "langchain_community.llms.azureml_endpoint.AzureMLEndpointApiType")

__On this page