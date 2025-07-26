# convert_pydantic_to_openai_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_pydantic_to_openai_tool.html
**Word Count:** 71
**Links Count:** 169
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# convert\_pydantic\_to\_openai\_tool\#

langchain\_core.utils.function\_calling.convert\_pydantic\_to\_openai\_tool\(

    _model : type\[BaseModel\]_,     _\*_ ,     _name : str | None = None_,     _description : str | None = None_, \) → [ToolDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.ToolDescription.html#langchain_core.utils.function_calling.ToolDescription "langchain_core.utils.function_calling.ToolDescription")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/function_calling.html#convert_pydantic_to_openai_tool)\#     

Deprecated since version 0.1.16: Use [`convert_to_openai_tool()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_tool.html#langchain_core.utils.function_calling.convert_to_openai_tool "langchain_core.utils.function_calling.convert_to_openai_tool") instead. It will not be removed until langchain-core==1.0.

Converts a Pydantic model to a function description for the OpenAI API.

Parameters:     

  * **model** \(_type_ _\[__BaseModel_ _\]_\) – The Pydantic model to convert.

  * **name** \(_str_ _|__None_\) – The name of the function. If not provided, the title of the schema will be used.

  * **description** \(_str_ _|__None_\) – The description of the function. If not provided, the description of the schema will be used.

Returns:     

The tool description.

Return type:     

[_ToolDescription_](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.ToolDescription.html#langchain_core.utils.function_calling.ToolDescription "langchain_core.utils.function_calling.ToolDescription")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)