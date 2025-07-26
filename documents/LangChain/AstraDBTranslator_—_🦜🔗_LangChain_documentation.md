# AstraDBTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.astradb.AstraDBTranslator.html
**Word Count:** 51
**Links Count:** 139
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# AstraDBTranslator\#

_class _langchain\_community.query\_constructors.astradb.AstraDBTranslator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/astradb.html#AstraDBTranslator)\#     

Translate AstraDB internal query language elements to valid filters.

Attributes

`allowed_comparators` | Subset of allowed logical operators.   ---|---   `allowed_operators` | Allowed operators for the visitor.      Methods

`visit_comparison`\(comparison\) | Translate a Comparison.   ---|---   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/astradb.html#AstraDBTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

_Dict_

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/astradb.html#AstraDBTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

_Dict_

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/astradb.html#AstraDBTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page