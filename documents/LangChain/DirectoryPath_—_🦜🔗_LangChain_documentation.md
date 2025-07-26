# DirectoryPath — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.DirectoryPath.html
**Word Count:** 63
**Links Count:** 161
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# DirectoryPath\#

_class _langchain\_community.agent\_toolkits.github.toolkit.DirectoryPath[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#DirectoryPath)\#     

Bases: `BaseModel`

Schema for operations that require a directory path as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _input _: str_ _ = ''_\#     

The path of the directory, e.g. some\_dir/inner\_dir. Only input a string, do not include the parameter name.

__On this page