# Parameter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html
**Word Count:** 42
**Links Count:** 418
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# Parameter\#

_class _langchain\_community.tools.connery.models.Parameter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/models.html#Parameter)\#     

Bases: `BaseModel`

Connery Action parameter model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str | None_ _ = None_\#     

_param _key _: str_ _\[Required\]_\#     

_param _title _: str_ _\[Required\]_\#     

_param _type _: Any_ _\[Required\]_\#     

_param _validation _: [Validation](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Validation.html#langchain_community.tools.connery.models.Validation "langchain_community.tools.connery.models.Validation") | None_ _ = None_\#     

__On this page