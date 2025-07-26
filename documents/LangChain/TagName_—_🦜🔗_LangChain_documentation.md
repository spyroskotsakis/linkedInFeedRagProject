# TagName — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.TagName.html
**Word Count:** 54
**Links Count:** 161
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# TagName\#

_class _langchain\_community.agent\_toolkits.github.toolkit.TagName[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#TagName)\#     

Bases: `BaseModel`

Schema for operations that require a tag name as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tag\_name _: str_ _\[Required\]_\#     

The tag name of the release, e.g. v1.0.0.

__On this page