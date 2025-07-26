# NoInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.NoInput.html
**Word Count:** 53
**Links Count:** 161
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# NoInput\#

_class _langchain\_community.agent\_toolkits.github.toolkit.NoInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#NoInput)\#     

Bases: `BaseModel`

Schema for operations that do not require any input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _no\_input _: str_ _ = ''_\#     

No input required, e.g. \`\` \(empty string\).

__On this page