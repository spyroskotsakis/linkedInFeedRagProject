# structured_query — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/structured_query.html
**Word Count:** 39
**Links Count:** 110
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# `structured_query`\#

Internal representation of a structured query language.

**Classes**

[`structured_query.Comparator`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\(value\) | Enumerator of the comparison operators.   ---|---   [`structured_query.Comparison`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison") | Comparison to a value.   [`structured_query.Expr`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Expr.html#langchain_core.structured_query.Expr "langchain_core.structured_query.Expr") | Base class for all expressions.   [`structured_query.FilterDirective`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective") | Filtering expression.   [`structured_query.Operation`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation") | Logical operation over other directives.   [`structured_query.Operator`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\(value\) | Enumerator of the operations.   [`structured_query.StructuredQuery`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery") | Structured query.   [`structured_query.Visitor`](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html#langchain_core.structured_query.Visitor "langchain_core.structured_query.Visitor")\(\) | Defines interface for IR translation using a visitor pattern.