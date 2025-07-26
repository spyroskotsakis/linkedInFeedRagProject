# RedisFilterExpression — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterExpression.html
**Word Count:** 75
**Links Count:** 340
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# RedisFilterExpression\#

_class _langchain\_community.vectorstores.redis.filters.RedisFilterExpression\(

    _\_filter : str | None = None_,     _operator : [RedisFilterOperator](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterOperator.html#langchain_community.vectorstores.redis.filters.RedisFilterOperator "langchain_community.vectorstores.redis.filters.RedisFilterOperator") | None = None_,     _left : RedisFilterExpression | None = None_,     _right : RedisFilterExpression | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/filters.html#RedisFilterExpression)\#     

Logical expression of RedisFilterFields.

RedisFilterExpressions can be combined using the & and | operators to create complex logical expressions that evaluate to the Redis Query language.

This presents an interface by which users can create complex queries without having to know the Redis Query language.

Filter expressions are not initialized directly. Instead they are built by combining RedisFilterFields using the & and | operators.

Examples               >>> from langchain_community.vectorstores.redis import RedisTag, RedisNum     >>> brand_is_nike = RedisTag("brand") == "nike"     >>> price_is_under_100 = RedisNum("price") < 100     >>> filter = brand_is_nike & price_is_under_100     >>> print(str(filter))     (@brand:{nike} @price:[-inf (100)])     

Methods

`__init__`\(\[\_filter, operator, left, right\]\) |    ---|---   `format_expression`\(left, right, operator\_str\) |       Parameters:     

  * **\_filter** \(_str_ _|__None_\)

  * **operator** \([_RedisFilterOperator_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterOperator.html#langchain_community.vectorstores.redis.filters.RedisFilterOperator "langchain_community.vectorstores.redis.filters.RedisFilterOperator") _|__None_\)

  * **left** \(_RedisFilterExpression_ _|__None_\)

  * **right** \(_RedisFilterExpression_ _|__None_\)

\_\_init\_\_\(

    _\_filter : str | None = None_,     _operator : [RedisFilterOperator](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterOperator.html#langchain_community.vectorstores.redis.filters.RedisFilterOperator "langchain_community.vectorstores.redis.filters.RedisFilterOperator") | None = None_,     _left : RedisFilterExpression | None = None_,     _right : RedisFilterExpression | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/filters.html#RedisFilterExpression.__init__)\#     

Parameters:     

  * **\_filter** \(_str_ _|__None_\)

  * **operator** \([_RedisFilterOperator_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.filters.RedisFilterOperator.html#langchain_community.vectorstores.redis.filters.RedisFilterOperator "langchain_community.vectorstores.redis.filters.RedisFilterOperator") _|__None_\)

  * **left** \(_RedisFilterExpression_ _|__None_\)

  * **right** \(_RedisFilterExpression_ _|__None_\)

_static _format\_expression\(

    _left : RedisFilterExpression_,     _right : RedisFilterExpression_,     _operator\_str : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/redis/filters.html#RedisFilterExpression.format_expression)\#     

Parameters:     

  * **left** \(_RedisFilterExpression_\)

  * **right** \(_RedisFilterExpression_\)

  * **operator\_str** \(_str_\)

Return type:     

str

__On this page