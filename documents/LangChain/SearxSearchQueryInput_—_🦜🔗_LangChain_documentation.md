# SearxSearchQueryInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.searx_search.tool.SearxSearchQueryInput.html
**Word Count:** 48
**Links Count:** 409
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# SearxSearchQueryInput\#

_class _langchain\_community.tools.searx\_search.tool.SearxSearchQueryInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/searx_search/tool.html#SearxSearchQueryInput)\#     

Bases: `BaseModel`

Input for the SearxSearch tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

query to look up on searx

__On this page