# BaseFileToolMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.file_management.utils.BaseFileToolMixin.html
**Word Count:** 62
**Links Count:** 412
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# BaseFileToolMixin\#

_class _langchain\_community.tools.file\_management.utils.BaseFileToolMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/utils.html#BaseFileToolMixin)\#     

Bases: `BaseModel`

Mixin for file system tools.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _root\_dir _: str | None_ _ = None_\#     

The final path will be chosen relative to root\_dir if specified.

get\_relative\_path\(

    _file\_path : str_, \) → Path[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/file_management/utils.html#BaseFileToolMixin.get_relative_path)\#     

Get the relative path, returning an error if unsupported.

Parameters:     

**file\_path** \(_str_\)

Return type:     

_Path_

__On this page