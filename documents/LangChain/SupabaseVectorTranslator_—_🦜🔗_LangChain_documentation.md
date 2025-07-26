# SupabaseVectorTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.supabase.SupabaseVectorTranslator.html
**Word Count:** 49
**Links Count:** 139
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# SupabaseVectorTranslator\#

_class _langchain\_community.query\_constructors.supabase.SupabaseVectorTranslator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/supabase.html#SupabaseVectorTranslator)\#     

Translate Langchain filters to Supabase PostgREST filters.

Attributes

`allowed_comparators` | Subset of allowed logical comparators.   ---|---   `allowed_operators` | Subset of allowed logical operators.   `metadata_column` |       Methods

`visit_comparison`\(comparison\) | Translate a Comparison.   ---|---   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/supabase.html#SupabaseVectorTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

str

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/supabase.html#SupabaseVectorTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

str

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, Dict\[str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/supabase.html#SupabaseVectorTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, _Dict_\[str, str\]\]

__On this page