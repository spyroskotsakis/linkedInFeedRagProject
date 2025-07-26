# SearchCode — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.SearchCode.html
**Word Count:** 55
**Links Count:** 161
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# SearchCode\#

_class _langchain\_community.agent\_toolkits.github.toolkit.SearchCode[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#SearchCode)\#     

Bases: `BaseModel`

Schema for operations that require a search query as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _search\_query _: str_ _\[Required\]_\#     

A keyword-focused natural language searchquery for code, e.g. MyFunctionName\(\).

__On this page