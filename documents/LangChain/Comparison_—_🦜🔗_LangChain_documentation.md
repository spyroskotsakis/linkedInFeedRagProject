# Comparison — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html
**Word Count:** 52
**Links Count:** 119
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# Comparison\#

_class _langchain\_core.structured\_query.Comparison[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Comparison)\#     

Bases: [`FilterDirective`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective")

Comparison to a value.

Create a Comparison.

Parameters:     

  * **comparator** – The comparator to use.

  * **attribute** – The attribute to compare.

  * **value** – The value to compare to.

_param _attribute _: str_ _\[Required\]_\#     

The attribute to compare.

_param _comparator _: [Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")_ _\[Required\]_\#     

The comparator to use.

_param _value _: Any_ _\[Required\]_\#     

The value to compare to.

accept\(

    _visitor : [Visitor](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")_, \) → Any\#     

Accept a visitor.

Parameters:     

**visitor** \([_Visitor_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")\) – visitor to accept.

Returns:     

result of visiting.

Return type:     

_Any_

Examples using Comparison

  * [How to construct filters for query analysis](https://python.langchain.com/docs/how_to/query_constructing_filters/)

__On this page