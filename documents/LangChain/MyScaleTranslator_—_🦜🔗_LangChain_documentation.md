# MyScaleTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.myscale.MyScaleTranslator.html
**Word Count:** 50
**Links Count:** 143
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# MyScaleTranslator\#

_class _langchain\_community.query\_constructors.myscale.MyScaleTranslator\(_metadata\_key : str = 'metadata'_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/myscale.html#MyScaleTranslator)\#     

Translate MyScale internal query language elements to valid filters.

Attributes

`allowed_comparators` | Allowed comparators for the visitor.   ---|---   `allowed_operators` | Subset of allowed logical operators.   `map_dict` |       Methods

`__init__`\(\[metadata\_key\]\) |    ---|---   `visit_comparison`\(comparison\) | Translate a Comparison.   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      Parameters:     

**metadata\_key** \(_str_\)

\_\_init\_\_\(

    _metadata\_key : str = 'metadata'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/myscale.html#MyScaleTranslator.__init__)\#     

Parameters:     

**metadata\_key** \(_str_\)

Return type:     

None

visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/myscale.html#MyScaleTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

_Dict_

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/myscale.html#MyScaleTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

_Dict_

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/myscale.html#MyScaleTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page