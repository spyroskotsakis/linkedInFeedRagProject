# convert_pydantic_to_ernie_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_tool.html
**Word Count:** 19
**Links Count:** 106
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# convert\_pydantic\_to\_ernie\_tool\#

langchain\_community.utils.ernie\_functions.convert\_pydantic\_to\_ernie\_tool\(

    _model : Type\[BaseModel\]_,     _\*_ ,     _name : str | None = None_,     _description : str | None = None_, \) → [ToolDescription](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.ToolDescription.html#langchain_community.utils.ernie_functions.ToolDescription "langchain_community.utils.ernie_functions.ToolDescription")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utils/ernie_functions.html#convert_pydantic_to_ernie_tool)\#     

Convert a Pydantic model to a function description for the Ernie API.

Parameters:     

  * **model** \(_Type_ _\[__BaseModel_ _\]_\)

  * **name** \(_str_ _|__None_\)

  * **description** \(_str_ _|__None_\)

Return type:     

[_ToolDescription_](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.ToolDescription.html#langchain_community.utils.ernie_functions.ToolDescription "langchain_community.utils.ernie_functions.ToolDescription")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)