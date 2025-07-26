# JsonSpec — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.json.tool.JsonSpec.html
**Word Count:** 95
**Links Count:** 424
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# JsonSpec\#

_class _langchain\_community.tools.json.tool.JsonSpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/json/tool.html#JsonSpec)\#     

Bases: `BaseModel`

Base class for JSON spec.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _dict\__: Dict_ _\[Required\]_\#     

_param _max\_value\_length _: int_ _ = 200_\#     

_classmethod _from\_file\(

    _path : Path_, \) → JsonSpec[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/json/tool.html#JsonSpec.from_file)\#     

Create a JsonSpec from a file.

Parameters:     

**path** \(_Path_\)

Return type:     

_JsonSpec_

keys\(_text : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/json/tool.html#JsonSpec.keys)\#     

Return the keys of the dict at the given path.

Parameters:     

**text** \(_str_\) – Python representation of the path to the dict \(e.g. data\[“key1”\]\[0\]\[“key2”\]\).

Return type:     

str

value\(_text : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/json/tool.html#JsonSpec.value)\#     

Return the value of the dict at the given path.

Parameters:     

**text** \(_str_\) – Python representation of the path to the dict \(e.g. data\[“key1”\]\[0\]\[“key2”\]\).

Return type:     

str

Examples using JsonSpec

  * [JSON Toolkit](https://python.langchain.com/docs/integrations/tools/json/)

  * [OpenAPI Toolkit](https://python.langchain.com/docs/integrations/tools/openapi/)

__On this page