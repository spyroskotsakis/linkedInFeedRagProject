# APIRequestBodyProperty — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIRequestBodyProperty.html
**Word Count:** 96
**Links Count:** 431
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# APIRequestBodyProperty\#

_class _langchain\_community.tools.openapi.utils.api\_models.APIRequestBodyProperty[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIRequestBodyProperty)\#     

Bases: [`APIPropertyBase`](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openapi.utils.api_models.APIPropertyBase.html#langchain_community.tools.openapi.utils.api_models.APIPropertyBase "langchain_community.tools.openapi.utils.api_models.APIPropertyBase")

A model for a request body property.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _default _: Any | None_ _ = None_\#     

The default value of the property.

_param _description _: str | None_ _ = None_\#     

The description of the property.

_param _name _: str_ _\[Required\]_\#     

The name of the property.

_param _properties _: List\['APIRequestBodyProperty'\]__\[Required\]_\#     

The sub-properties of the property.

_param _references\_used _: List\[str\]__\[Required\]_\#     

The references used by the property.

_param _required _: bool_ _\[Required\]_\#     

Whether the property is required.

_param _type _: SCHEMA\_TYPE_ _\[Required\]_\#     

The type of the property.

Either a primitive type, a component/parameter type, or an array or ‘object’ \(dict\) of the above.

_classmethod _from\_schema\(

    _schema : [Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")_,     _name : str_,     _required : bool_,     _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")_,     _references\_used : List\[str\] | None = None_, \) → APIRequestBodyProperty[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/openapi/utils/api_models.html#APIRequestBodyProperty.from_schema)\#     

Recursively populate from an OpenAPI Schema.

Parameters:     

  * **schema** \([_Schema_](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")\)

  * **name** \(_str_\)

  * **required** \(_bool_\)

  * **spec** \([_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")\)

  * **references\_used** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

Return type:     

APIRequestBodyProperty

__On this page