# BranchName — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.BranchName.html
**Word Count:** 53
**Links Count:** 161
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# BranchName\#

_class _langchain\_community.agent\_toolkits.github.toolkit.BranchName[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#BranchName)\#     

Bases: `BaseModel`

Schema for operations that require a branch name as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _branch\_name _: str_ _\[Required\]_\#     

The name of the branch, e.g. my\_branch.

__On this page