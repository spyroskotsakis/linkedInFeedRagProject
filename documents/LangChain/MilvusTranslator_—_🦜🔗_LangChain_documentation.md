# MilvusTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.milvus.MilvusTranslator.html
**Word Count:** 51
**Links Count:** 139
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# MilvusTranslator\#

_class _langchain\_community.query\_constructors.milvus.MilvusTranslator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/milvus.html#MilvusTranslator)\#     

Translate Milvus internal query language elements to valid filters.

Attributes

`allowed_comparators` | Allowed comparators for the visitor.   ---|---   `allowed_operators` | Subset of allowed logical comparators.      Methods

`visit_comparison`\(comparison\) | Translate a Comparison.   ---|---   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/milvus.html#MilvusTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

str

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/milvus.html#MilvusTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

str

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/milvus.html#MilvusTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page