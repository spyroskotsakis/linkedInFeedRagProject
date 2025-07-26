# Runtime — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Runtime.html
**Word Count:** 41
**Links Count:** 179
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# Runtime\#

_class _langchain\_community.chains.pebblo\_retrieval.models.Runtime[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#Runtime)\#     

Bases: `BaseModel`

OS, language details

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _host _: str_ _\[Required\]_\#     

_param _ip _: str | None_ _ = ''_\#     

_param _language _: str_ _\[Required\]_\#     

_param _language\_version _: str_ _\[Required\]_\#     

_param _os _: str_ _\[Required\]_\#     

_param _os\_version _: str_ _\[Required\]_\#     

_param _path _: str_ _\[Required\]_\#     

_param _platform _: str_ _\[Required\]_\#     

_param _runtime _: str | None_ _ = ''_\#     

_param _type _: str | None_ _ = ''_\#     

__On this page