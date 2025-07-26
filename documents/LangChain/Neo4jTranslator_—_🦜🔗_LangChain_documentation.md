# Neo4jTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.neo4j.Neo4jTranslator.html
**Word Count:** 61
**Links Count:** 142
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# Neo4jTranslator\#

_class _langchain\_community.query\_constructors.neo4j.Neo4jTranslator\(_\* args: Any_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/neo4j.html#Neo4jTranslator)\#     

Deprecated since version 0.3.8: Use `:class:`~langchain_neo4j.query_constructors.neo4j.Neo4jTranslator`` instead. It will not be removed until langchain-community==1.0.

Translate Neo4j internal query language elements to valid filters.

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

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/neo4j.html#Neo4jTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

_Dict_

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/neo4j.html#Neo4jTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

_Dict_

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/neo4j.html#Neo4jTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page