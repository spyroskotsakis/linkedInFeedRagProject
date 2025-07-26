# PropertySettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.PropertySettings.html
**Word Count:** 44
**Links Count:** 88
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# PropertySettings\#

_class _langchain\_prompty.core.PropertySettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#PropertySettings)\#     

Bases: `BaseModel`

Property settings for a prompty model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _default _: str | int | float | list | dict | bool | None_ _ = None_\#     

_param _description _: str_ _ = ''_\#     

_param _type _: Literal\['string', 'number', 'array', 'object', 'boolean'\]__\[Required\]_\#     

__On this page