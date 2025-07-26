# format_tool_to_openai_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.format_tool_to_openai_tool.html
**Word Count:** 31
**Links Count:** 171
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# format\_tool\_to\_openai\_tool\#

langchain\_core.utils.function\_calling.format\_tool\_to\_openai\_tool\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → [ToolDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.ToolDescription.html#langchain_core.utils.function_calling.ToolDescription "langchain_core.utils.function_calling.ToolDescription")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/function_calling.html#format_tool_to_openai_tool)\#     

Deprecated since version 0.1.16: Use [`convert_to_openai_tool()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html#langchain_core.utils.function_calling.convert_to_openai_tool "langchain_core.utils.function_calling.convert_to_openai_tool") instead. It will not be removed until langchain-core==1.0.

Format tool into the OpenAI function API.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\) – The tool to format.

Returns:     

The tool description.

Return type:     

[ToolDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.ToolDescription.html#langchain_core.utils.function_calling.ToolDescription "langchain_core.utils.function_calling.ToolDescription")

__On this page