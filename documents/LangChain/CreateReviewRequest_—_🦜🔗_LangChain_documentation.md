# CreateReviewRequest — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CreateReviewRequest.html
**Word Count:** 54
**Links Count:** 161
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# CreateReviewRequest\#

_class _langchain\_community.agent\_toolkits.github.toolkit.CreateReviewRequest[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#CreateReviewRequest)\#     

Bases: `BaseModel`

Schema for operations that require a username as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _username _: str_ _\[Required\]_\#     

GitHub username of the user being requested, e.g. my\_username.

__On this page