# ReadFile — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.ReadFile.html
**Word Count:** 69
**Links Count:** 161
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# ReadFile\#

_class _langchain\_community.agent\_toolkits.github.toolkit.ReadFile[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#ReadFile)\#     

Bases: `BaseModel`

Schema for operations that require a file path as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _formatted\_filepath _: str_ _\[Required\]_\#     

The full file path of the file you would like to read where the path must NOT start with a slash, e.g. some\_dir/my\_file.py.

__On this page