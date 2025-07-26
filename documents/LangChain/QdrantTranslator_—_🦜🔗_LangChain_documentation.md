# QdrantTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.qdrant.QdrantTranslator.html
**Word Count:** 49
**Links Count:** 143
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# QdrantTranslator\#

_class _langchain\_community.query\_constructors.qdrant.QdrantTranslator\(_metadata\_key : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/qdrant.html#QdrantTranslator)\#     

Translate Qdrant internal query language elements to valid filters.

Attributes

`allowed_comparators` | Subset of allowed logical comparators.   ---|---   `allowed_operators` | Subset of allowed logical operators.      Methods

`__init__`\(metadata\_key\) |    ---|---   `visit_comparison`\(comparison\) | Translate a Comparison.   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      Parameters:     

**metadata\_key** \(_str_\)

\_\_init\_\_\(_metadata\_key : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/qdrant.html#QdrantTranslator.__init__)\#     

Parameters:     

**metadata\_key** \(_str_\)

visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → rest.FieldCondition[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/qdrant.html#QdrantTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

rest.FieldCondition

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → rest.Filter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/qdrant.html#QdrantTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

rest.Filter

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/qdrant.html#QdrantTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page