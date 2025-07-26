# FileSearchInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.file_search.FileSearchInput.html
**Word Count:** 50
**Links Count:** 411
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# FileSearchInput\#

_class _langchain\_community.tools.file\_management.file\_search.FileSearchInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/file_search.html#FileSearchInput)\#     

Bases: `BaseModel`

Input for FileSearchTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _dir\_path _: str_ _ = '.'_\#     

Subdirectory to search in.

_param _pattern _: str_ _\[Required\]_\#     

Unix shell regex, where \* matches everything.

__On this page