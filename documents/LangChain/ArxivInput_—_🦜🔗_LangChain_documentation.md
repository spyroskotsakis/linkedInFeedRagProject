# ArxivInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.arxiv.tool.ArxivInput.html
**Word Count:** 47
**Links Count:** 409
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# ArxivInput\#

_class _langchain\_community.tools.arxiv.tool.ArxivInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/arxiv/tool.html#ArxivInput)\#     

Bases: `BaseModel`

Input for the Arxiv tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

search query to look up

__On this page