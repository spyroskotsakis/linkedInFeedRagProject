# APIOperation — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIOperation.html
**Word Count:** 95
**Links Count:** 448
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# APIOperation\#

_class _langchain\_community.tools.openapi.utils.api\_models.APIOperation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIOperation)\#     

Bases: `BaseModel`

A model for a single API operation.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _base\_url _: str_ _\[Required\]_\#     

The base URL of the operation.

_param _description _: str | None_ _\[Required\]_\#     

The description of the operation.

_param _method _: [HTTPVerb](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.HTTPVerb.html#langchain_community.utilities.openapi.HTTPVerb "langchain_community.utilities.openapi.HTTPVerb")_ _\[Required\]_\#     

The HTTP method of the operation.

_param _operation\_id _: str_ _\[Required\]_\#     

The unique identifier of the operation.

_param _path _: str_ _\[Required\]_\#     

The path of the operation.

_param _properties _: Sequence\[[APIProperty](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIProperty.html#langchain_community.tools.openapi.utils.api_models.APIProperty "langchain_community.tools.openapi.utils.api_models.APIProperty")\]__\[Required\]_\#     

_param _request\_body _: [APIRequestBody](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIRequestBody.html#langchain_community.tools.openapi.utils.api_models.APIRequestBody "langchain_community.tools.openapi.utils.api_models.APIRequestBody") | None_ _\[Required\]_\#     

The request body of the operation.

_classmethod _from\_openapi\_spec\(

    _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")_,     _path : str_,     _method : str_, \) → APIOperation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIOperation.from_openapi_spec)\#     

Create an APIOperation from an OpenAPI spec.

Parameters:     

  * **spec** \([_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")\)

  * **path** \(_str_\)

  * **method** \(_str_\)

Return type:     

_APIOperation_

_classmethod _from\_openapi\_url\(

    _spec\_url : str_,     _path : str_,     _method : str_, \) → APIOperation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIOperation.from_openapi_url)\#     

Create an APIOperation from an OpenAPI URL.

Parameters:     

  * **spec\_url** \(_str_\)

  * **path** \(_str_\)

  * **method** \(_str_\)

Return type:     

_APIOperation_

_static _ts\_type\_from\_python\(

    _type\_ : str | Type | tuple | None | Enum_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIOperation.ts_type_from_python)\#     

Parameters:     

**type\_** \(_str_ _|__Type_ _|__tuple_ _|__None_ _|__Enum_\)

Return type:     

str

to\_typescript\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIOperation.to_typescript)\#     

Get typescript string representation of the operation.

Return type:     

str

_property _body\_params _: List\[str\]_\#     

_property _path\_params _: List\[str\]_\#     

_property _query\_params _: List\[str\]_\#     

__On this page