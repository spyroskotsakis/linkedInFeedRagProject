# convert_to_ernie_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.ernie_functions.base.convert_to_ernie_function.html
**Word Count:** 56
**Links Count:** 159
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# convert\_to\_ernie\_function\#

langchain\_community.chains.ernie\_functions.base.convert\_to\_ernie\_function\(

    _function : Dict\[str, Any\] | Type\[BaseModel\] | Callable_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/ernie_functions/base.html#convert_to_ernie_function)\#     

Convert a raw function/class to an Ernie function.

Parameters:     

**function** \(_Dict_ _\[__str_ _,__Any_ _\]__|__Type_ _\[__BaseModel_ _\]__|__Callable_\) – Either a dictionary, a pydantic.BaseModel class, or a Python function. If a dictionary is passed in, it is assumed to already be a valid Ernie function.

Returns:     

A dict version of the passed in function which is compatible with the     

Ernie function-calling API.

Return type:     

_Dict_\[str, _Any_\]

__On this page