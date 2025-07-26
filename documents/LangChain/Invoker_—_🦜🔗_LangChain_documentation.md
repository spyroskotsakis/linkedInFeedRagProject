# Invoker — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Invoker.html
**Word Count:** 13
**Links Count:** 94
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# Invoker\#

_class _langchain\_prompty.core.Invoker\(_prompty : [Prompty](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Invoker)\#     

Base class for all invokers.

Methods

`__init__`\(prompty\) |    ---|---   `invoke`\(data\) |       Parameters:     

**prompty** \([_Prompty_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")\)

\_\_init\_\_\(

    _prompty : [Prompty](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Invoker.__init__)\#     

Parameters:     

**prompty** \([_Prompty_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")\)

Return type:     

None

_abstractmethod _invoke\(

    _data : BaseModel_, \) → BaseModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#Invoker.invoke)\#     

Parameters:     

**data** \(_BaseModel_\)

Return type:     

_BaseModel_

__On this page