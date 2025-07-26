# GetIssue — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.GetIssue.html
**Word Count:** 53
**Links Count:** 161
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# GetIssue\#

_class _langchain\_community.agent\_toolkits.github.toolkit.GetIssue[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#GetIssue)\#     

Bases: `BaseModel`

Schema for operations that require an issue number as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _issue\_number _: int_ _ = 0_\#     

Issue number as an integer, e.g. 42

__On this page