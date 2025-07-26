# JinaInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.jina_search.tool.JinaInput.html
**Word Count:** 48
**Links Count:** 409
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# JinaInput\#

_class _langchain\_community.tools.jina\_search.tool.JinaInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/jina_search/tool.html#JinaInput)\#     

Bases: `BaseModel`

Input for the Jina search tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

search query to look up

__On this page