# AzureCosmosDbNoSQLTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/query_constructors/langchain_azure_ai.query_constructors.cosmosdb_no_sql.AzureCosmosDbNoSQLTranslator.html
**Word Count:** 109
**Links Count:** 97
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# AzureCosmosDbNoSQLTranslator\#

_class _langchain\_azure\_ai.query\_constructors.cosmosdb\_no\_sql.AzureCosmosDbNoSQLTranslator\(_table\_name : str = 'c'_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/query_constructors/cosmosdb_no_sql.html#AzureCosmosDbNoSQLTranslator)\#     

A visitor that converts a StructuredQuery into an CosmosDB NO SQL query.

Initialize the translator with the table name.

Attributes

`allowed_comparators` | Allowed comparators for the visitor.   ---|---   `allowed_operators` | Allowed operators for the visitor.      Methods

`__init__`\(\[table\_name\]\) | Initialize the translator with the table name.   ---|---   `visit_comparison`\(comparison\) | Visit a comparison operation and convert it into an SQL condition.   `visit_operation`\(operation\) | Visit logical operations and convert them into SQL expressions.   `visit_structured_query`\(structured\_query\) | Visit a structured query and convert it into parameter for vectorstore.      Parameters:     

**table\_name** \(_str_\)

\_\_init\_\_\(

    _table\_name : str = 'c'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/query_constructors/cosmosdb_no_sql.html#AzureCosmosDbNoSQLTranslator.__init__)\#     

Initialize the translator with the table name.

Parameters:     

**table\_name** \(_str_\)

Return type:     

None

visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/query_constructors/cosmosdb_no_sql.html#AzureCosmosDbNoSQLTranslator.visit_comparison)\#     

Visit a comparison operation and convert it into an SQL condition.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\)

Return type:     

str

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/query_constructors/cosmosdb_no_sql.html#AzureCosmosDbNoSQLTranslator.visit_operation)\#     

Visit logical operations and convert them into SQL expressions.

Uses parentheses to ensure correct precedence.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\)

Return type:     

str

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/query_constructors/cosmosdb_no_sql.html#AzureCosmosDbNoSQLTranslator.visit_structured_query)\#     

Visit a structured query and convert it into parameter for vectorstore.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\)

Return type:     

_Tuple_\[str, _Dict_\[str, _Any_\]\]

__On this page