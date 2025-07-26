# TemplateSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.TemplateSettings.html
**Word Count:** 44
**Links Count:** 86
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# TemplateSettings\#

_class _langchain\_prompty.core.TemplateSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#TemplateSettings)\#     

Bases: `BaseModel`

Template settings for a prompty model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _parser _: str_ _ = ''_\#     

_param _type _: str_ _ = 'mustache'_\#     

__On this page