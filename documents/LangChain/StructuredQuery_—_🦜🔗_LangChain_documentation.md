# StructuredQuery — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html
**Word Count:** 47
**Links Count:** 119
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# StructuredQuery\#

_class _langchain\_core.structured\_query.StructuredQuery[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#StructuredQuery)\#     

Bases: [`Expr`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Expr.html#langchain_core.structured_query.Expr "langchain_core.structured_query.Expr")

Structured query.

Create a StructuredQuery.

Parameters:     

  * **query** – The query string.

  * **filter** – The filtering expression.

  * **limit** – The limit on the number of results.

_param _filter _: [FilterDirective](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective") | None_ _\[Required\]_\#     

Filtering expression.

_param _limit _: int | None_ _\[Required\]_\#     

Limit on the number of results.

_param _query _: str_ _\[Required\]_\#     

Query string.

accept\(

    _visitor : [Visitor](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")_, \) → Any\#     

Accept a visitor.

Parameters:     

**visitor** \([_Visitor_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")\) – visitor to accept.

Returns:     

result of visiting.

Return type:     

_Any_

Examples using StructuredQuery

  * [How to construct filters for query analysis](https://python.langchain.com/docs/how_to/query_constructing_filters/)

__On this page