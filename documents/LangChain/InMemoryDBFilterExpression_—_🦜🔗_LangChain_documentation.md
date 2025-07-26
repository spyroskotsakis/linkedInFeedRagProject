# InMemoryDBFilterExpression — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression.html
**Word Count:** 106
**Links Count:** 126
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# InMemoryDBFilterExpression\#

_class _langchain\_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterExpression\(

    _\_filter : str | None = None_,     _operator : [InMemoryDBFilterOperator](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator") | None = None_,     _left : InMemoryDBFilterExpression | None = None_,     _right : InMemoryDBFilterExpression | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/filters.html#InMemoryDBFilterExpression)\#     

Logical expression of InMemoryDBFilterFields.

InMemoryDBFilterExpressions can be combined using the & and | operators to create complex logical expressions that evaluate to the InMemoryDB Query language.

This presents an interface by which users can create complex queries without having to know the InMemoryDB Query language.

Filter expressions are not initialized directly. Instead they are built by combining InMemoryDBFilterFields using the & and | operators.

Examples: >>> from langchain\_aws.vectorstores.inmemorydb import \( … InMemoryDBTag, InMemoryDBNum … \) >>> brand\_is\_nike = InMemoryDBTag\(“brand”\) == “nike” >>> price\_is\_under\_100 = InMemoryDBNum\(“price”\) < 100 >>> filter = brand\_is\_nike & price\_is\_under\_100 >>> print\(str\(filter\)\) \(@brand:\{nike\} @price:\[-inf \(100\)\]\)

Methods

`__init__`\(\[\_filter, operator, left, right\]\) |    ---|---   `format_expression`\(left, right, operator\_str\) |       Parameters:     

  * **\_filter** \(_str_ _|__None_\)

  * **operator** \([_InMemoryDBFilterOperator_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator") _|__None_\)

  * **left** \(_InMemoryDBFilterExpression_ _|__None_\)

  * **right** \(_InMemoryDBFilterExpression_ _|__None_\)

\_\_init\_\_\(

    _\_filter : str | None = None_,     _operator : [InMemoryDBFilterOperator](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator") | None = None_,     _left : InMemoryDBFilterExpression | None = None_,     _right : InMemoryDBFilterExpression | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/filters.html#InMemoryDBFilterExpression.__init__)\#     

Parameters:     

  * **\_filter** \(_str_ _|__None_\)

  * **operator** \([_InMemoryDBFilterOperator_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator.html#langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator "langchain_aws.vectorstores.inmemorydb.filters.InMemoryDBFilterOperator") _|__None_\)

  * **left** \(_InMemoryDBFilterExpression_ _|__None_\)

  * **right** \(_InMemoryDBFilterExpression_ _|__None_\)

_static _format\_expression\(

    _left : InMemoryDBFilterExpression_,     _right : InMemoryDBFilterExpression_,     _operator\_str : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/filters.html#InMemoryDBFilterExpression.format_expression)\#     

Parameters:     

  * **left** \(_InMemoryDBFilterExpression_\)

  * **right** \(_InMemoryDBFilterExpression_\)

  * **operator\_str** \(_str_\)

Return type:     

str

__On this page