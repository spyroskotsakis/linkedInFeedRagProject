# Branch — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Branch.html
**Word Count:** 75
**Links Count:** 196
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# Branch\#

_class _langchain\_core.runnables.graph.Branch\(

    _condition : Callable\[..., str\]_,     _ends : dict\[str, str\] | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Branch)\#     

Branch in a graph.

Parameters:     

  * **condition** \(_Callable_ _\[__\[__...__\]__,__str_ _\]_\) – A callable that returns a string representation of the condition.

  * **ends** \(_dict_ _\[__str_ _,__str_ _\]__|__None_\) – Optional dictionary of end node ids for the branches. Defaults to None.

Create new instance of Branch\(condition, ends\)

Attributes

`condition` | Alias for field number 0   ---|---   `ends` | Alias for field number 1      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(_value_ , _start =0_, _stop =9223372036854775807_, _/_\)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)