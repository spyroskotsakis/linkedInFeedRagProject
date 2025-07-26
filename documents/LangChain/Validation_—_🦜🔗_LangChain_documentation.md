# Validation — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Validation.html
**Word Count:** 43
**Links Count:** 409
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# Validation\#

_class _langchain\_community.tools.connery.models.Validation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/models.html#Validation)\#     

Bases: `BaseModel`

Connery Action parameter validation model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _required _: bool | None_ _ = None_\#     

__On this page