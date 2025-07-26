# convert_pydantic_to_ernie_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_function.html
**Word Count:** 19
**Links Count:** 106
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# convert\_pydantic\_to\_ernie\_function\#

langchain\_community.utils.ernie\_functions.convert\_pydantic\_to\_ernie\_function\(

    _model : Type\[BaseModel\]_,     _\*_ ,     _name : str | None = None_,     _description : str | None = None_, \) → [FunctionDescription](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.FunctionDescription.html#langchain_community.utils.ernie_functions.FunctionDescription "langchain_community.utils.ernie_functions.FunctionDescription")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utils/ernie_functions.html#convert_pydantic_to_ernie_function)\#     

Convert a Pydantic model to a function description for the Ernie API.

Parameters:     

  * **model** \(_Type_ _\[__BaseModel_ _\]_\)

  * **name** \(_str_ _|__None_\)

  * **description** \(_str_ _|__None_\)

Return type:     

[_FunctionDescription_](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.FunctionDescription.html#langchain_community.utils.ernie_functions.FunctionDescription "langchain_community.utils.ernie_functions.FunctionDescription")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)