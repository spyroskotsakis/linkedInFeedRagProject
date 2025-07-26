# convert_python_function_to_openai_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_python_function_to_openai_function.html
**Word Count:** 63
**Links Count:** 168
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# convert\_python\_function\_to\_openai\_function\#

langchain\_core.utils.function\_calling.convert\_python\_function\_to\_openai\_function\(

    _function : Callable_, \) → [FunctionDescription](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription")\#     

Deprecated since version 0.1.16: Use [`convert_to_openai_function()`](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_openai_function.html#langchain_core.utils.function_calling.convert_to_openai_function "langchain_core.utils.function_calling.convert_to_openai_function") instead. It will not be removed until langchain-core==1.0.

Convert a Python function to an OpenAI function-calling API compatible dict.

Assumes the Python function has type hints and a docstring with a description. If     

the docstring has Google Python style argument descriptions, these will be included as well.

Parameters:     

**function** \(_Callable_\) – The Python function to convert.

Returns:     

The OpenAI function description.

Return type:     

[_FunctionDescription_](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.FunctionDescription.html#langchain_core.utils.function_calling.FunctionDescription "langchain_core.utils.function_calling.FunctionDescription")

__On this page