# CreateFile — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.CreateFile.html
**Word Count:** 53
**Links Count:** 161
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# CreateFile\#

_class _langchain\_community.agent\_toolkits.github.toolkit.CreateFile[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#CreateFile)\#     

Bases: `BaseModel`

Schema for operations that require a file path and content as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _formatted\_file _: str_ _\[Required\]_\#     

Follow the required formatting.

__On this page