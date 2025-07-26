# get_all_basemodel_annotations — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.get_all_basemodel_annotations.html
**Word Count:** 36
**Links Count:** 114
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# get\_all\_basemodel\_annotations\#

langchain\_core.tools.base.get\_all\_basemodel\_annotations\(

    _cls : type\[BaseModel\] | Any_,     _\*_ ,     _default\_to\_bound : bool = True_, \) → dict\[str, type\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/base.html#get_all_basemodel_annotations)\#     

Get all annotations from a Pydantic BaseModel and its parents.

Parameters:     

  * **cls** \(_type_ _\[__BaseModel_ _\]__|__Any_\) – The Pydantic BaseModel class.

  * **default\_to\_bound** \(_bool_\) – Whether to default to the bound of a TypeVar if it exists.

Return type:     

dict\[str, type\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)