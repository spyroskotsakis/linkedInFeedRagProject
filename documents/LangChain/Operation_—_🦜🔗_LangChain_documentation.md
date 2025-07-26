# Operation — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html
**Word Count:** 46
**Links Count:** 118
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# Operation\#

_class _langchain\_core.structured\_query.Operation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Operation)\#     

Bases: [`FilterDirective`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective")

Logical operation over other directives.

Create an Operation.

Parameters:     

  * **operator** – The operator to use.

  * **arguments** – The arguments to the operator.

_param _arguments _: list\[[FilterDirective](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective")\]__\[Required\]_\#     

The arguments to the operator.

_param _operator _: [Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")_ _\[Required\]_\#     

The operator to use.

accept\(

    _visitor : [Visitor](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")_, \) → Any\#     

Accept a visitor.

Parameters:     

**visitor** \([_Visitor_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")\) – visitor to accept.

Returns:     

result of visiting.

Return type:     

_Any_

Examples using Operation

  * [How to construct filters for query analysis](https://python.langchain.com/docs/how_to/query_constructing_filters/)

__On this page