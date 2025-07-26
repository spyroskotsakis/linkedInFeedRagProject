# convert_python_function_to_ernie_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.ernie_functions.base.convert_python_function_to_ernie_function.html
**Word Count:** 44
**Links Count:** 159
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# convert\_python\_function\_to\_ernie\_function\#

langchain\_community.chains.ernie\_functions.base.convert\_python\_function\_to\_ernie\_function\(

    _function : Callable_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/ernie_functions/base.html#convert_python_function_to_ernie_function)\#     

Convert a Python function to an Ernie function-calling API compatible dict.

Assumes the Python function has type hints and a docstring with a description. If     

the docstring has Google Python style argument descriptions, these will be included as well.

Parameters:     

**function** \(_Callable_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page