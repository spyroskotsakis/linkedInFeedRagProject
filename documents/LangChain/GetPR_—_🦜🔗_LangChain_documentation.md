# GetPR — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.GetPR.html
**Word Count:** 54
**Links Count:** 161
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# GetPR\#

_class _langchain\_community.agent\_toolkits.github.toolkit.GetPR[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#GetPR)\#     

Bases: `BaseModel`

Schema for operations that require a PR number as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _pr\_number _: int_ _ = 0_\#     

The PR number as an integer, e.g. 12

__On this page