# ModelSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.ModelSettings.html
**Word Count:** 45
**Links Count:** 93
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# ModelSettings\#

_class _langchain\_prompty.core.ModelSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#ModelSettings)\#     

Bases: `BaseModel`

Model settings for a prompty model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api _: str_ _ = ''_\#     

_param _configuration _: dict_ _ = \{\}_\#     

_param _parameters _: dict_ _ = \{\}_\#     

_param _response _: dict_ _ = \{\}_\#     

model\_dump\_safe\(\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#ModelSettings.model_dump_safe)\#     

Return type:     

dict

__On this page