# OpenAPISpec — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html
**Word Count:** 180
**Links Count:** 329
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# OpenAPISpec\#

_class _langchain\_community.utilities.openapi.OpenAPISpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec)\#     

OpenAPI Model that removes mis-formatted parts of the spec.

Attributes

`base_url` | Get the base url.   ---|---   `openapi` |       Methods

`from_file`\(path\) | Get an OpenAPI spec from a file path.   ---|---   `from_spec_dict`\(spec\_dict\) | Get an OpenAPI spec from a dict.   `from_text`\(text\) | Get an OpenAPI spec from a text.   `from_url`\(url\) | Get an OpenAPI spec from a URL.   `get_cleaned_operation_id`\(operation, path, method\) | Get a cleaned operation id from an operation id.   `get_methods_for_path`\(path\) | Return a list of valid methods for the specified path.   `get_operation`\(path, method\) | Get the operation object for a given path and HTTP method.   `get_parameters_for_operation`\(operation\) | Get the components for a given operation.   `get_parameters_for_path`\(path\) |    `get_referenced_schema`\(ref\) | Get a schema \(or nested reference\) or err.   `get_request_body_for_operation`\(operation\) | Get the request body for a given operation.   `get_schema`\(schema\[, depth, max\_depth\]\) |    `parse_obj`\(obj\) |       _classmethod _from\_file\(

    _path : str | Path_, \) → OpenAPISpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.from_file)\#     

Get an OpenAPI spec from a file path.

Parameters:     

**path** \(_str_ _|__Path_\)

Return type:     

_OpenAPISpec_

_classmethod _from\_spec\_dict\(

    _spec\_dict : dict_, \) → OpenAPISpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.from_spec_dict)\#     

Get an OpenAPI spec from a dict.

Parameters:     

**spec\_dict** \(_dict_\)

Return type:     

_OpenAPISpec_

_classmethod _from\_text\(

    _text : str_, \) → OpenAPISpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.from_text)\#     

Get an OpenAPI spec from a text.

Parameters:     

**text** \(_str_\)

Return type:     

_OpenAPISpec_

_classmethod _from\_url\(

    _url : str_, \) → OpenAPISpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.from_url)\#     

Get an OpenAPI spec from a URL.

Parameters:     

**url** \(_str_\)

Return type:     

_OpenAPISpec_

_static _get\_cleaned\_operation\_id\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_,     _path : str_,     _method : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_cleaned_operation_id)\#     

Get a cleaned operation id from an operation id.

Parameters:     

  * **operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\)

  * **path** \(_str_\)

  * **method** \(_str_\)

Return type:     

str

get\_methods\_for\_path\(

    _path : str_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_methods_for_path)\#     

Return a list of valid methods for the specified path.

Parameters:     

**path** \(_str_\)

Return type:     

_List_\[str\]

get\_operation\(

    _path : str_,     _method : str_, \) → [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_operation)\#     

Get the operation object for a given path and HTTP method.

Parameters:     

  * **path** \(_str_\)

  * **method** \(_str_\)

Return type:     

[Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")

get\_parameters\_for\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → List\[[Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_parameters_for_operation)\#     

Get the components for a given operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\)

Return type:     

List\[[Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\]

get\_parameters\_for\_path\(

    _path : str_, \) → List\[[Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_parameters_for_path)\#     

Parameters:     

**path** \(_str_\)

Return type:     

List\[[Parameter](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter "langchain_community.tools.connery.models.Parameter")\]

get\_referenced\_schema\(_ref : Reference_\) → [Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_referenced_schema)\#     

Get a schema \(or nested reference\) or err.

Parameters:     

**ref** \(_Reference_\)

Return type:     

[Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")

get\_request\_body\_for\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → RequestBody | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_request_body_for_operation)\#     

Get the request body for a given operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\)

Return type:     

Optional\[RequestBody\]

get\_schema\(

    _schema : Reference | [Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")_,     _depth : int = 0_,     _max\_depth : int | None = None_, \) → [Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.get_schema)\#     

Parameters:     

  * **schema** \(_Union_ _\[__Reference_ _,_[_Schema_](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema") _\]_\)

  * **depth** \(_int_\)

  * **max\_depth** \(_Optional_ _\[__int_ _\]_\)

Return type:     

[Schema](https://python.langchain.com/api_reference/neo4j/chains/langchain_neo4j.chains.graph_qa.cypher_utils.Schema.html#langchain_neo4j.chains.graph_qa.cypher_utils.Schema "langchain_neo4j.chains.graph_qa.cypher_utils.Schema")

_classmethod _parse\_obj\(

    _obj : dict_, \) → OpenAPISpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openapi.html#OpenAPISpec.parse_obj)\#     

Parameters:     

**obj** \(_dict_\)

Return type:     

_OpenAPISpec_

__On this page