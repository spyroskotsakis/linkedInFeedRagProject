# FileInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.bearly.tool.FileInfo.html
**Word Count:** 45
**Links Count:** 413
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# FileInfo\#

_class _langchain\_community.tools.bearly.tool.FileInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/bearly/tool.html#FileInfo)\#     

Bases: `BaseModel`

Information about a file to be uploaded.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str_ _\[Required\]_\#     

_param _source\_path _: str_ _\[Required\]_\#     

_param _target\_path _: str_ _\[Required\]_\#     

__On this page