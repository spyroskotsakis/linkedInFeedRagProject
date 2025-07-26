# CreatePR — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CreatePR.html
**Word Count:** 53
**Links Count:** 161
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# CreatePR\#

_class _langchain\_community.agent\_toolkits.github.toolkit.CreatePR[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#CreatePR)\#     

Bases: `BaseModel`

Schema for operations that require a PR title and body as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _formatted\_pr _: str_ _\[Required\]_\#     

Follow the required formatting.

__On this page