# ApiConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.plugin.ApiConfig.html
**Word Count:** 40
**Links Count:** 413
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# ApiConfig\#

_class _langchain\_community.tools.plugin.ApiConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/plugin.html#ApiConfig)\#     

Bases: `BaseModel`

API Configuration.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _has\_user\_authentication _: bool | None_ _ = False_\#     

_param _type _: str_ _\[Required\]_\#     

_param _url _: str_ _\[Required\]_\#     

__On this page