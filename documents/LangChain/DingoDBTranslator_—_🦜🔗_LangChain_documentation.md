# DingoDBTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.dingo.DingoDBTranslator.html
**Word Count:** 49
**Links Count:** 143
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# DingoDBTranslator\#

_class _langchain\_community.query\_constructors.dingo.DingoDBTranslator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/dingo.html#DingoDBTranslator)\#     

Translate DingoDB internal query language elements to valid filters.

Attributes

`allowed_comparators` | Subset of allowed logical comparators.   ---|---   `allowed_operators` | Subset of allowed logical operators.      Methods

`visit_comparison`\(comparison\) | Translate a Comparison.   ---|---   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/dingo.html#DingoDBTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

[_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/dingo.html#DingoDBTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

[_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/dingo.html#DingoDBTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page