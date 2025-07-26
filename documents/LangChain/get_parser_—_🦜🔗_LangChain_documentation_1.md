# get_parser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.parser.get_parser.html
**Word Count:** 23
**Links Count:** 192
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# get\_parser\#

langchain.chains.query\_constructor.parser.get\_parser\(

    _allowed\_comparators : Sequence\[[Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\] | None = None_,     _allowed\_operators : Sequence\[[Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\] | None = None_,     _allowed\_attributes : Sequence\[str\] | None = None_, \) → Lark[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/parser.html#get_parser)\#     

Return a parser for the query language.

Parameters:     

  * **allowed\_comparators** \(_Sequence_ _\[_[_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator") _\]__|__None_\) – Optional\[Sequence\[Comparator\]\]

  * **allowed\_operators** \(_Sequence_ _\[_[_Operator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator") _\]__|__None_\) – Optional\[Sequence\[Operator\]\]

  * **allowed\_attributes** \(_Sequence_ _\[__str_ _\]__|__None_\)

Returns:     

Lark parser for the query language.

Return type:     

_Lark_

__On this page