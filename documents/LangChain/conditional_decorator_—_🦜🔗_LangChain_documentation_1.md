# conditional_decorator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.fireworks.conditional_decorator.html
**Word Count:** 26
**Links Count:** 282
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# conditional\_decorator\#

langchain\_community.llms.fireworks.conditional\_decorator\(

    _condition : bool_,     _decorator : Callable\[\[Any\], Any\]_, \) → Callable\[\[Any\], Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/fireworks.html#conditional_decorator)\#     

Conditionally apply a decorator.

Parameters:     

  * **condition** \(_bool_\) – A boolean indicating whether to apply the decorator.

  * **decorator** \(_Callable_ _\[__\[__Any_ _\]__,__Any_ _\]_\) – A decorator function.

Returns:     

A decorator function.

Return type:     

_Callable_\[\[_Any_\], _Any_\]

__On this page