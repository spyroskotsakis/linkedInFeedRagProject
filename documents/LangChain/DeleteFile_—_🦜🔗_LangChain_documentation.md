# DeleteFile — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.github.toolkit.DeleteFile.html
**Word Count:** 77
**Links Count:** 161
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# DeleteFile\#

_class _langchain\_community.agent\_toolkits.github.toolkit.DeleteFile[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/github/toolkit.html#DeleteFile)\#     

Bases: `BaseModel`

Schema for operations that require a file path as input.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _formatted\_filepath _: str_ _\[Required\]_\#     

The full file path of the file you would like to delete where the path must NOT start with a slash, e.g. some\_dir/my\_file.py. Only input a string, not the param name.

__On this page