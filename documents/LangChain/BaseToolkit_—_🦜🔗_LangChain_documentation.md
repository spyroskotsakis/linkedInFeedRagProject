# BaseToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html
**Word Count:** 80
**Links Count:** 119
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# BaseToolkit\#

_class _langchain\_core.tools.base.BaseToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/base.html#BaseToolkit)\#     

Bases: `BaseModel`, `ABC`

Base class for toolkits containing related tools.

A toolkit is a collection of related tools that can be used together to accomplish a specific task or work with a particular system.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_abstractmethod _get\_tools\(\) → list\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/base.html#BaseToolkit.get_tools)\#     

Get all tools in the toolkit.

Returns:     

List of tools contained in this toolkit.

Return type:     

list\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

__On this page