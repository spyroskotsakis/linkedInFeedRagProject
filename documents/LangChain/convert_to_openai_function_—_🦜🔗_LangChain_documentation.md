# convert_to_openai_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_function.html
**Word Count:** 176
**Links Count:** 170
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# convert\_to\_openai\_function\#

langchain\_core.utils.function\_calling.convert\_to\_openai\_function\(

    _function : dict\[str, Any\] | type | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_,     _\*_ ,     _strict : bool | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/function_calling.html#convert_to_openai_function)\#     

Convert a raw function/class to an OpenAI function.

Parameters:     

  * **function** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__type_ _,__Callable_ _,_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – A dictionary, Pydantic BaseModel class, TypedDict class, a LangChain Tool object, or a Python function. If a dictionary is passed in, it is assumed to already be a valid OpenAI function, a JSON schema with top-level ‘title’ key specified, an Anthropic format tool, or an Amazon Bedrock Converse format tool.

  * **strict** \(_Optional_ _\[__bool_ _\]_\) – If True, model output is guaranteed to exactly match the JSON Schema provided in the function definition. If None, `strict` argument will not be included in function definition.

Returns:     

A dict version of the passed in function which is compatible with the OpenAI function-calling API.

Raises:     

**ValueError** – If function is not in a supported format.

Return type:     

dict\[str, Any\]

Changed in version 0.2.29: `strict` arg added.

Changed in version 0.3.13: Support for Anthropic format tools added.

Changed in version 0.3.14: Support for Amazon Bedrock Converse format tools added.

Changed in version 0.3.16: ‘description’ and ‘parameters’ keys are now optional. Only ‘name’ is required and guaranteed to be part of the output.

Examples using convert\_to\_openai\_function

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to convert tools to OpenAI Functions](https://python.langchain.com/docs/how_to/tools_as_openai_functions/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)