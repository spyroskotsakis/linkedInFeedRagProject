# DDGInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ddg_search.tool.DDGInput.html
**Word Count:** 48
**Links Count:** 409
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# DDGInput\#

_class _langchain\_community.tools.ddg\_search.tool.DDGInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/ddg_search/tool.html#DDGInput)\#     

Bases: `BaseModel`

Input for the DuckDuckGo search tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

search query to look up

__On this page