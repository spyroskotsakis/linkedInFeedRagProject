# format_tool_to_openai_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.format_tool_to_openai_function.html
**Word Count:** 31
**Links Count:** 170
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# format\_tool\_to\_openai\_function\#

langchain\_core.utils.function\_calling.format\_tool\_to\_openai\_function\(

    _tool : [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_, \) → [FunctionDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription")\#     

Deprecated since version 0.1.16: Use [`convert_to_openai_function()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_function.html#langchain_core.utils.function_calling.convert_to_openai_function "langchain_core.utils.function_calling.convert_to_openai_function") instead. It will not be removed until langchain-core==1.0.

Format tool into the OpenAI function API.

Parameters:     

**tool** \([_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\) – The tool to format.

Returns:     

The function description.

Return type:     

[FunctionDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription")

__On this page