# Visitor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Visitor.html
**Word Count:** 50
**Links Count:** 124
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# Visitor\#

_class _langchain\_core.structured\_query.Visitor[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Visitor)\#     

Defines interface for IR translation using a visitor pattern.

Attributes

`allowed_comparators` | Allowed comparators for the visitor.   ---|---   `allowed_operators` | Allowed operators for the visitor.      Methods

`visit_comparison`\(comparison\) | Translate a Comparison.   ---|---   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      _abstractmethod _visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Visitor.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

_Any_

_abstractmethod _visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Visitor.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

_Any_

_abstractmethod _visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/structured_query.html#Visitor.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Any_

__On this page