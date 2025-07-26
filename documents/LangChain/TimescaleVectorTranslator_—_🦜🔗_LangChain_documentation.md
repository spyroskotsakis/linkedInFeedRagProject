# TimescaleVectorTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.timescalevector.TimescaleVectorTranslator.html
**Word Count:** 51
**Links Count:** 139
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# TimescaleVectorTranslator\#

_class _langchain\_community.query\_constructors.timescalevector.TimescaleVectorTranslator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/timescalevector.html#TimescaleVectorTranslator)\#     

Translate the internal query language elements to valid filters.

Attributes

`COMPARATOR_MAP` |    ---|---   `OPERATOR_MAP` |    `allowed_comparators` | Allowed comparators for the visitor.   `allowed_operators` | Subset of allowed logical operators.      Methods

`visit_comparison`\(comparison\) | Translate a Comparison.   ---|---   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → client.Predicates[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/timescalevector.html#TimescaleVectorTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

client.Predicates

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → client.Predicates[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/timescalevector.html#TimescaleVectorTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

client.Predicates

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/timescalevector.html#TimescaleVectorTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page