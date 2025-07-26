# APIProperty — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIProperty.html
**Word Count:** 106
**Links Count:** 433
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# APIProperty\#

_class _langchain\_community.tools.openapi.utils.api\_models.APIProperty[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIProperty)\#     

Bases: [`APIPropertyBase`](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIPropertyBase.html#langchain_community.tools.openapi.utils.api_models.APIPropertyBase "langchain_community.tools.openapi.utils.api_models.APIPropertyBase")

A model for a property in the query, path, header, or cookie params.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _default _: Any | None_ _ = None_\#     

The default value of the property.

_param _description _: str | None_ _ = None_\#     

The description of the property.

_param _location _: [APIPropertyLocation](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIPropertyLocation.html#langchain_community.tools.openapi.utils.api_models.APIPropertyLocation "langchain_community.tools.openapi.utils.api_models.APIPropertyLocation")_ _\[Required\]_\#     

The path/how it’s being passed to the endpoint.

_param _name _: str_ _\[Required\]_\#     

The name of the property.

_param _required _: bool_ _\[Required\]_\#     

Whether the property is required.

_param _type _: SCHEMA\_TYPE_ _\[Required\]_\#     

The type of the property.

Either a primitive type, a component/parameter type, or an array or ‘object’ \(dict\) of the above.

_classmethod _from\_parameter\(

    _parameter : [Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")_,     _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")_, \) → APIProperty[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIProperty.from_parameter)\#     

Instantiate from an OpenAPI Parameter.

Parameters:     

  * **parameter** \([_Parameter_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\)

  * **spec** \([_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")\)

Return type:     

APIProperty

_static _is\_supported\_location\(_location : str_\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIProperty.is_supported_location)\#     

Return whether the provided location is supported.

Parameters:     

**location** \(_str_\)

Return type:     

bool

__On this page