# PkgInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.PkgInfo.html
**Word Count:** 39
**Links Count:** 171
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# PkgInfo\#

_class _langchain\_community.chains.pebblo\_retrieval.models.PkgInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#PkgInfo)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _documentation\_url _: str | None_ _\[Required\]_\#     

_param _installed\_via _: str | None_ _\[Required\]_\#     

_param _liscence\_type _: str | None_ _\[Required\]_\#     

_param _location _: str | None_ _\[Required\]_\#     

_param _project\_home\_page _: str | None_ _\[Required\]_\#     

_param _pypi\_url _: str | None_ _\[Required\]_\#     

__On this page