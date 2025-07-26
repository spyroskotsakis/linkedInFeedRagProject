# fix_filter_directive — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.fix_filter_directive.html
**Word Count:** 40
**Links Count:** 196
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# fix\_filter\_directive\#

langchain.chains.query\_constructor.base.fix\_filter\_directive\(

    _filter : [FilterDirective](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective") | None_,     _\*_ ,     _allowed\_comparators : Sequence\[[Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\] | None = None_,     _allowed\_operators : Sequence\[[Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\] | None = None_,     _allowed\_attributes : Sequence\[str\] | None = None_, \) → [FilterDirective](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/base.html#fix_filter_directive)\#     

Fix invalid filter directive.

Parameters:     

  * **filter** \([_FilterDirective_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective") _|__None_\) – Filter directive to fix.

  * **allowed\_comparators** \(_Sequence_ _\[_[_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator") _\]__|__None_\) – allowed comparators. Defaults to all comparators.

  * **allowed\_operators** \(_Sequence_ _\[_[_Operator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator") _\]__|__None_\) – allowed operators. Defaults to all operators.

  * **allowed\_attributes** \(_Sequence_ _\[__str_ _\]__|__None_\) – allowed attributes. Defaults to all attributes.

Returns:     

Fixed filter directive.

Return type:     

[_FilterDirective_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.FilterDirective.html#langchain_core.structured_query.FilterDirective "langchain_core.structured_query.FilterDirective") | None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)