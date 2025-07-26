# DirectoryListingInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.list_dir.DirectoryListingInput.html
**Word Count:** 43
**Links Count:** 409
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# DirectoryListingInput\#

_class _langchain\_community.tools.file\_management.list\_dir.DirectoryListingInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/list_dir.html#DirectoryListingInput)\#     

Bases: `BaseModel`

Input for ListDirectoryTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _dir\_path _: str_ _ = '.'_\#     

Subdirectory to list.

__On this page