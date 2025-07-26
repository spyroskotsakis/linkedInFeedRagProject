# Prompty — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html
**Word Count:** 45
**Links Count:** 124
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# Prompty\#

_class _langchain\_prompty.core.Prompty[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Prompty)\#     

Bases: `BaseModel`

Base Prompty model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _authors _: list\[str\]__ = \[\]_\#     

_param _base _: str_ _ = ''_\#     

_param _basePrompty _: Prompty | None_ _ = None_\#     

_param _content _: str_ _ = ''_\#     

_param _description _: str_ _ = ''_\#     

_param _file _: FilePath_ _ = ''_\#     

Constraints:     

  * **path\_type** = file

_param _inputs _: dict\[str, [PropertySettings](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.PropertySettings.html#langchain_prompty.core.PropertySettings "langchain_prompty.core.PropertySettings")\]__ = \{\}_\#     

_param _model _: [ModelSettings](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.ModelSettings.html#langchain_prompty.core.ModelSettings "langchain_prompty.core.ModelSettings")_ _\[Optional\]_\#     

_param _name _: str_ _ = ''_\#     

_param _outputs _: dict\[str, [PropertySettings](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.PropertySettings.html#langchain_prompty.core.PropertySettings "langchain_prompty.core.PropertySettings")\]__ = \{\}_\#     

_param _sample _: dict_ _ = \{\}_\#     

_param _tags _: list\[str\]__ = \[\]_\#     

_param _template _: [TemplateSettings](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.TemplateSettings.html#langchain_prompty.core.TemplateSettings "langchain_prompty.core.TemplateSettings")_ _\[Required\]_\#     

_param _version _: str_ _ = ''_\#     

_static _normalize\(

    _attribute : Any_,     _parent : Path_,     _env\_error : bool = True_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Prompty.normalize)\#     

Parameters:     

  * **attribute** \(_Any_\)

  * **parent** \(_Path_\)

  * **env\_error** \(_bool_\)

Return type:     

_Any_

to\_safe\_dict\(\) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Prompty.to_safe_dict)\#     

Return type:     

dict\[str, _Any_\]

to\_safe\_json\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Prompty.to_safe_json)\#     

Return type:     

str

__On this page