# TencentVectorDBTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.tencentvectordb.TencentVectorDBTranslator.html
**Word Count:** 130
**Links Count:** 143
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# TencentVectorDBTranslator\#

_class _langchain\_community.query\_constructors.tencentvectordb.TencentVectorDBTranslator\(

    _meta\_keys : Sequence\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/tencentvectordb.html#TencentVectorDBTranslator)\#     

Translate StructuredQuery to Tencent VectorDB query.

Initialize the translator.

Parameters:     

**meta\_keys** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – List of meta keys to be used in the query. Default: \[\].

Attributes

`COMPARATOR_MAP` |    ---|---   `allowed_comparators` | Allowed comparators for the visitor.   `allowed_operators` | Allowed operators for the visitor.      Methods

`__init__`\(\[meta\_keys\]\) | Initialize the translator.   ---|---   `visit_comparison`\(comparison\) | Visit a comparison node and return the translated query.   `visit_operation`\(operation\) | Visit an operation node and return the translated query.   `visit_structured_query`\(structured\_query\) | Visit a structured query node and return the translated query.      \_\_init\_\_\(

    _meta\_keys : Sequence\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/tencentvectordb.html#TencentVectorDBTranslator.__init__)\#     

Initialize the translator.

Parameters:     

**meta\_keys** \(_Sequence_ _\[__str_ _\]__|__None_\) – List of meta keys to be used in the query. Default: \[\].

visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/tencentvectordb.html#TencentVectorDBTranslator.visit_comparison)\#     

Visit a comparison node and return the translated query.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison node to be visited.

Returns:     

Translated query.

Return type:     

str

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/tencentvectordb.html#TencentVectorDBTranslator.visit_operation)\#     

Visit an operation node and return the translated query.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation node to be visited.

Returns:     

Translated query.

Return type:     

str

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/tencentvectordb.html#TencentVectorDBTranslator.visit_structured_query)\#     

Visit a structured query node and return the translated query.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery node to be visited.

Returns:     

Translated query and query kwargs.

Return type:     

_Tuple_\[str, dict\]

__On this page