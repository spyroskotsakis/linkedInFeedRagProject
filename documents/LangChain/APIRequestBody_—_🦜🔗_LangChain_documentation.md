# APIRequestBody — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIRequestBody.html
**Word Count:** 60
**Links Count:** 421
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# APIRequestBody\#

_class _langchain\_community.tools.openapi.utils.api\_models.APIRequestBody[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIRequestBody)\#     

Bases: `BaseModel`

A model for a request body.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str | None_ _\[Required\]_\#     

The description of the request body.

_param _media\_type _: str_ _\[Required\]_\#     

The media type of the request body.

_param _properties _: List\[[APIRequestBodyProperty](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIRequestBodyProperty.html#langchain_community.tools.openapi.utils.api_models.APIRequestBodyProperty "langchain_community.tools.openapi.utils.api_models.APIRequestBodyProperty")\]__\[Required\]_\#     

_classmethod _from\_request\_body\(

    _request\_body : RequestBody_,     _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")_, \) → APIRequestBody[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIRequestBody.from_request_body)\#     

Instantiate from an OpenAPI RequestBody.

Parameters:     

  * **request\_body** \(_RequestBody_\)

  * **spec** \([_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")\)

Return type:     

APIRequestBody

__On this page