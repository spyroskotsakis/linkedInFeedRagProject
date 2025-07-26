# Edge — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Edge.html
**Word Count:** 146
**Links Count:** 204
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# Edge\#

_class _langchain\_core.runnables.graph.Edge\(

    _source : str_,     _target : str_,     _data : [Stringifiable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Stringifiable.html#langchain_core.runnables.graph.Stringifiable "langchain_core.runnables.graph.Stringifiable") | None = None_,     _conditional : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Edge)\#     

Edge in a graph.

Parameters:     

  * **source** \(_str_\) – The source node id.

  * **target** \(_str_\) – The target node id.

  * **data** \([_Stringifiable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.graph.Stringifiable.html#langchain_core.runnables.graph.Stringifiable "langchain_core.runnables.graph.Stringifiable") _|__None_\) – Optional data associated with the edge. Defaults to None.

  * **conditional** \(_bool_\) – Whether the edge is conditional. Defaults to False.

Create new instance of Edge\(source, target, data, conditional\)

Attributes

`conditional` | Alias for field number 3   ---|---   `data` | Alias for field number 2   `source` | Alias for field number 0   `target` | Alias for field number 1      Methods

`copy`\(\*\[, source, target\]\) | Return a copy of the edge with optional new source and target nodes.   ---|---   `count`\(value, /\) | Return number of occurrences of value.   `index`\(value\[, start, stop\]\) | Return first index of value.      copy\(

    _\*_ ,     _source : str | None = None_,     _target : str | None = None_, \) → Edge[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/graph.html#Edge.copy)\#     

Return a copy of the edge with optional new source and target nodes.

Parameters:     

  * **source** \(_str_ _|__None_\) – The new source node id. Defaults to None.

  * **target** \(_str_ _|__None_\) – The new target node id. Defaults to None.

Returns:     

A copy of the edge with the new source and target nodes.

Return type:     

_Edge_

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(_value_ , _start =0_, _stop =9223372036854775807_, _/_\)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)   *[/]: Positional-only parameter separator (PEP 570)