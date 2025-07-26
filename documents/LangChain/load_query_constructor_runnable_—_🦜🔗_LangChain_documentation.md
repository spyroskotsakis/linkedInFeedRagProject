# load_query_constructor_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.base.load_query_constructor_runnable.html
**Word Count:** 122
**Links Count:** 200
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# load\_query\_constructor\_runnable\#

langchain.chains.query\_constructor.base.load\_query\_constructor\_runnable\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _document\_contents : str_,     _attribute\_info : Sequence\[[AttributeInfo](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html#langchain.chains.query_constructor.schema.AttributeInfo "langchain.chains.query_constructor.schema.AttributeInfo") | dict\]_,     _\*_ ,     _examples : Sequence | None = None_,     _allowed\_comparators : Sequence\[[Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\] = \(Comparator.EQ, Comparator.NE, Comparator.GT, Comparator.GTE, Comparator.LT, Comparator.LTE, Comparator.CONTAIN, Comparator.LIKE, Comparator.IN, Comparator.NIN\)_,     _allowed\_operators : Sequence\[[Operator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator")\] = \(Operator.AND, Operator.OR, Operator.NOT\)_,     _enable\_limit : bool = False_,     _schema\_prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _fix\_invalid : bool = False_,     _\*\* kwargs: Any_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/base.html#load_query_constructor_runnable)\#     

Load a query constructor runnable chain.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – BaseLanguageModel to use for the chain.

  * **document\_contents** \(_str_\) – Description of the page contents of the document to be queried.

  * **attribute\_info** \(_Sequence_ _\[_[_AttributeInfo_](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html#langchain.chains.query_constructor.schema.AttributeInfo "langchain.chains.query_constructor.schema.AttributeInfo") _|__dict_ _\]_\) – Sequence of attributes in the document.

  * **examples** \(_Sequence_ _|__None_\) – Optional list of examples to use for the chain.

  * **allowed\_comparators** \(_Sequence_ _\[_[_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator") _\]_\) – Sequence of allowed comparators. Defaults to all Comparators.

  * **allowed\_operators** \(_Sequence_ _\[_[_Operator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Operator.html#langchain_core.structured_query.Operator "langchain_core.structured_query.Operator") _\]_\) – Sequence of allowed operators. Defaults to all Operators.

  * **enable\_limit** \(_bool_\) – Whether to enable the limit operator. Defaults to False.

  * **schema\_prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – Prompt for describing query schema. Should have string input variables allowed\_comparators and allowed\_operators.

  * **fix\_invalid** \(_bool_\) – Whether to fix invalid filter directives by ignoring invalid operators, comparators and attributes.

  * **kwargs** \(_Any_\) – Additional named params to pass to FewShotPromptTemplate init.

Returns:     

A Runnable that can be used to construct queries.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)