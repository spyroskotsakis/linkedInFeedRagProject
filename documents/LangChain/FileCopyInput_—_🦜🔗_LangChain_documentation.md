# FileCopyInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.copy.FileCopyInput.html
**Word Count:** 51
**Links Count:** 411
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# FileCopyInput\#

_class _langchain\_community.tools.file\_management.copy.FileCopyInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/copy.html#FileCopyInput)\#     

Bases: `BaseModel`

Input for CopyFileTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _destination\_path _: str_ _\[Required\]_\#     

Path to save the copied file

_param _source\_path _: str_ _\[Required\]_\#     

Path of the file to copy

__On this page