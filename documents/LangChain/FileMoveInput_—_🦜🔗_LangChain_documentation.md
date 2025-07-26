# FileMoveInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.move.FileMoveInput.html
**Word Count:** 51
**Links Count:** 411
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# FileMoveInput\#

_class _langchain\_community.tools.file\_management.move.FileMoveInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/move.html#FileMoveInput)\#     

Bases: `BaseModel`

Input for MoveFileTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _destination\_path _: str_ _\[Required\]_\#     

New path for the moved file

_param _source\_path _: str_ _\[Required\]_\#     

Path of the file to move

__On this page