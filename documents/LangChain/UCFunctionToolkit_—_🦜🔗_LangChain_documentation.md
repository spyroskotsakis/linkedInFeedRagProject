# UCFunctionToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.databricks.tool.UCFunctionToolkit.html
**Word Count:** 118
**Links Count:** 424
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# UCFunctionToolkit\#

_class _langchain\_community.tools.databricks.tool.UCFunctionToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/databricks/tool.html#UCFunctionToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Deprecated since version 0.3.18: Use `:class:`~databricks_langchain.uc_ai.UCFunctionToolkit`` instead. It will not be removed until langchain-community==1.0.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _tools _: Dict\[str, [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]__\[Optional\]_\#     

_param _warehouse\_id _: str_ _\[Required\]_\#     

The ID of a Databricks SQL Warehouse to execute functions.

_param _workspace\_client _: Any_ _\[Optional\]_\#     

Databricks workspace client.

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/databricks/tool.html#UCFunctionToolkit.get_tools)\#     

Get all tools in the toolkit.

Returns:     

List of tools contained in this toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

include\(

    _\* function\_names: str_,     _\*\* kwargs: Any_, \) → Self[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/databricks/tool.html#UCFunctionToolkit.include)\#     

Includes UC functions to the toolkit.

Parameters:     

  * **functions** – A list of UC function names in the format “catalog\_name.schema\_name.function\_name” or “catalog\_name.schema\_name.\*”. If the function name ends with “.\*”, all functions in the schema will be added.

  * **kwargs** \(_Any_\) – Extra arguments to pass to StructuredTool, e.g., return\_direct.

  * **function\_names** \(_str_\)

Return type:     

_Self_

Examples using UCFunctionToolkit

  * [Databricks Unity Catalog \(UC\)](https://python.langchain.com/docs/integrations/tools/databricks/)

__On this page