# resolve_criteria — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.criteria.eval_chain.resolve_criteria.html
**Word Count:** 59
**Links Count:** 125
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# resolve\_criteria\#

langchain.evaluation.criteria.eval\_chain.resolve\_criteria\(

    _criteria : Mapping\[str, str\] | [Criteria](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.criteria.eval_chain.Criteria.html#langchain.evaluation.criteria.eval_chain.Criteria "langchain.evaluation.criteria.eval_chain.Criteria") | [ConstitutionalPrinciple](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html#langchain.chains.constitutional_ai.models.ConstitutionalPrinciple "langchain.chains.constitutional_ai.models.ConstitutionalPrinciple") | str | None_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/criteria/eval_chain.html#resolve_criteria)\#     

Resolve the criteria to evaluate.

Parameters:     

**criteria** \(_CRITERIA\_TYPE_\) – 

The criteria to evaluate the runs against. It can be:     

  * a mapping of a criterion name to its description

  * a single criterion name present in one of the default criteria

  * a single ConstitutionalPrinciple instance

Returns:     

A dictionary mapping criterion names to descriptions.

Return type:     

Dict\[str, str\]

Examples               >>> criterion = "relevance"     >>> CriteriaEvalChain.resolve_criteria(criteria)     {'relevance': 'Is the submission referring to a real quote from the text?'}     

__On this page