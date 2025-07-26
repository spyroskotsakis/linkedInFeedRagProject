# HanaTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.hanavector.HanaTranslator.html
**Word Count:** 120
**Links Count:** 144
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# HanaTranslator\#

_class _langchain\_community.query\_constructors.hanavector.HanaTranslator\(_\* args: Any_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/hanavector.html#HanaTranslator)\#     

Deprecated since version 0.3.23: This class is deprecated and will be removed in a future version. Please use query\_constructors.HanaTranslator from the langchain\_hana package instead. See [SAP/langchain-integration-for-sap-hana-cloud](https://github.com/SAP/langchain-integration-for-sap-hana-cloud) for details. Use `query_constructors import HanaTranslator;` instead. It will not be removed until langchain-community==1.0.

**DEPRECATED** : This class is deprecated and will no longer be maintained. Please use query\_constructors.HanaTranslator from the langchain\_hana package instead. It offers an improved implementation and full support.

Translate internal query language elements to valid filters params for HANA vectorstore.

Attributes

`allowed_comparators` | Allowed comparators for the visitor.   ---|---   `allowed_operators` | Subset of allowed logical operators.      Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `visit_comparison`\(comparison\) | Translate a Comparison.   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      \_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → Any\#     

Parameters:     

  * **self** \(_Any_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/hanavector.html#HanaTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

_Dict_

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/hanavector.html#HanaTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

_Dict_

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/hanavector.html#HanaTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

Examples using HanaTranslator

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/retrievers/self_query/hanavector_self_query/)

__On this page