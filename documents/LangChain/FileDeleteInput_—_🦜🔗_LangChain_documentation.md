# FileDeleteInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.delete.FileDeleteInput.html
**Word Count:** 46
**Links Count:** 409
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# FileDeleteInput\#

_class _langchain\_community.tools.file\_management.delete.FileDeleteInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/delete.html#FileDeleteInput)\#     

Bases: `BaseModel`

Input for DeleteFileTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _file\_path _: str_ _\[Required\]_\#     

Path of the file to delete

__On this page