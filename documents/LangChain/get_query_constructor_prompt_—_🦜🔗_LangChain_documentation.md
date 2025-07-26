# get_query_constructor_prompt — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.get_query_constructor_prompt.html
**Word Count:** 104
**Links Count:** 200
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# get\_query\_constructor\_prompt\#

langchain.chains.query\_constructor.base.get\_query\_constructor\_prompt\(

    _document\_contents : str_,     _attribute\_info : Sequence\[[AttributeInfo](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html#langchain.chains.query_constructor.schema.AttributeInfo "langchain.chains.query_constructor.schema.AttributeInfo") | dict\]_,     _\*_ ,     _examples : Sequence | None = None_,     _allowed\_comparators : Sequence\[[Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\] = \(Comparator.EQ, Comparator.NE, Comparator.GT, Comparator.GTE, Comparator.LT, Comparator.LTE, Comparator.CONTAIN, Comparator.LIKE, Comparator.IN, Comparator.NIN\)_,     _allowed\_operators : Sequence\[[Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\] = \(Operator.AND, Operator.OR, Operator.NOT\)_,     _enable\_limit : bool = False_,     _schema\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _\*\* kwargs: Any_, \) → [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/base.html#get_query_constructor_prompt)\#     

Create query construction prompt.

Parameters:     

  * **document\_contents** \(_str_\) – The contents of the document to be queried.

  * **attribute\_info** \(_Sequence_ _\[_[_AttributeInfo_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html#langchain.chains.query_constructor.schema.AttributeInfo "langchain.chains.query_constructor.schema.AttributeInfo") _|__dict_ _\]_\) – A list of AttributeInfo objects describing the attributes of the document.

  * **examples** \(_Sequence_ _|__None_\) – Optional list of examples to use for the chain.

  * **allowed\_comparators** \(_Sequence_ _\[_[_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator") _\]_\) – Sequence of allowed comparators.

  * **allowed\_operators** \(_Sequence_ _\[_[_Operator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator") _\]_\) – Sequence of allowed operators.

  * **enable\_limit** \(_bool_\) – Whether to enable the limit operator. Defaults to False.

  * **schema\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – Prompt for describing query schema. Should have string input variables allowed\_comparators and allowed\_operators.

  * **kwargs** \(_Any_\) – Additional named params to pass to FewShotPromptTemplate init.

Returns:     

A prompt template that can be used to construct queries.

Return type:     

[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")

Examples using get\_query\_constructor\_prompt

  * [How to do “self-querying” retrieval](https://python.langchain.com/docs/how_to/self_query/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/retrievers/self_query/hanavector_self_query/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)