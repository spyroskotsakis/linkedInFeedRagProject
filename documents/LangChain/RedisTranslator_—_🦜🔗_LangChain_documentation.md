# RedisTranslator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.redis.RedisTranslator.html
**Word Count:** 53
**Links Count:** 157
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# RedisTranslator\#

_class _langchain\_community.query\_constructors.redis.RedisTranslator\(

    _schema : [RedisModel](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisModel.html#langchain_community.vectorstores.redis.schema.RedisModel "langchain_community.vectorstores.redis.schema.RedisModel")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/redis.html#RedisTranslator)\#     

Visitor for translating structured queries to Redis filter expressions.

Attributes

`allowed_comparators` | Subset of allowed logical comparators.   ---|---   `allowed_operators` | Subset of allowed logical operators.      Methods

`__init__`\(schema\) |    ---|---   `from_vectorstore`\(vectorstore\) |    `visit_comparison`\(comparison\) | Translate a Comparison.   `visit_operation`\(operation\) | Translate an Operation.   `visit_structured_query`\(structured\_query\) | Translate a StructuredQuery.      Parameters:     

**schema** \([_RedisModel_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisModel.html#langchain_community.vectorstores.redis.schema.RedisModel "langchain_community.vectorstores.redis.schema.RedisModel")\)

\_\_init\_\_\(

    _schema : [RedisModel](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisModel.html#langchain_community.vectorstores.redis.schema.RedisModel "langchain_community.vectorstores.redis.schema.RedisModel")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/redis.html#RedisTranslator.__init__)\#     

Parameters:     

**schema** \([_RedisModel_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.schema.RedisModel.html#langchain_community.vectorstores.redis.schema.RedisModel "langchain_community.vectorstores.redis.schema.RedisModel")\)

Return type:     

None

_classmethod _from\_vectorstore\(

    _vectorstore : [Redis](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")_, \) → RedisTranslator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/redis.html#RedisTranslator.from_vectorstore)\#     

Parameters:     

**vectorstore** \([_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")\)

Return type:     

_RedisTranslator_

visit\_comparison\(

    _comparison : [Comparison](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")_, \) → [RedisFilterExpression](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterExpression.html#langchain_community.vectorstores.redis.filters.RedisFilterExpression "langchain_community.vectorstores.redis.filters.RedisFilterExpression")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/redis.html#RedisTranslator.visit_comparison)\#     

Translate a Comparison.

Parameters:     

**comparison** \([_Comparison_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparison.html#langchain_core.structured_query.Comparison "langchain_core.structured_query.Comparison")\) – Comparison to translate.

Return type:     

[_RedisFilterExpression_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterExpression.html#langchain_community.vectorstores.redis.filters.RedisFilterExpression "langchain_community.vectorstores.redis.filters.RedisFilterExpression")

visit\_operation\(

    _operation : [Operation](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/redis.html#RedisTranslator.visit_operation)\#     

Translate an Operation.

Parameters:     

**operation** \([_Operation_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operation.html#langchain_core.structured_query.Operation "langchain_core.structured_query.Operation")\) – Operation to translate.

Return type:     

_Any_

visit\_structured\_query\(

    _structured\_query : [StructuredQuery](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")_, \) → Tuple\[str, dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/redis.html#RedisTranslator.visit_structured_query)\#     

Translate a StructuredQuery.

Parameters:     

**structured\_query** \([_StructuredQuery_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.StructuredQuery.html#langchain_core.structured_query.StructuredQuery "langchain_core.structured_query.StructuredQuery")\) – StructuredQuery to translate.

Return type:     

_Tuple_\[str, dict\]

__On this page