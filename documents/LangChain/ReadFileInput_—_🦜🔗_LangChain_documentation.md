# ReadFileInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.read.ReadFileInput.html
**Word Count:** 43
**Links Count:** 409
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# ReadFileInput\#

_class _langchain\_community.tools.file\_management.read.ReadFileInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/read.html#ReadFileInput)\#     

Bases: `BaseModel`

Input for ReadFileTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _file\_path _: str_ _\[Required\]_\#     

name of file

__On this page