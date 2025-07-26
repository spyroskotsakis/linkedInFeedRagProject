# WriteFileInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.write.WriteFileInput.html
**Word Count:** 53
**Links Count:** 413
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# WriteFileInput\#

_class _langchain\_community.tools.file\_management.write.WriteFileInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/write.html#WriteFileInput)\#     

Bases: `BaseModel`

Input for WriteFileTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _append _: bool_ _ = False_\#     

Whether to append to an existing file.

_param _file\_path _: str_ _\[Required\]_\#     

name of file

_param _text _: str_ _\[Required\]_\#     

text to write to file

__On this page