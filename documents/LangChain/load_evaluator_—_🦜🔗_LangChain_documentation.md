# load_evaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.loading.load_evaluator.html
**Word Count:** 46
**Links Count:** 130
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# load\_evaluator\#

langchain.evaluation.loading.load\_evaluator\(

    _evaluator : [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_,     _\*_ ,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _\*\* kwargs: Any_, \) → [Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") | [StringEvaluator](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html#langchain.evaluation.schema.StringEvaluator "langchain.evaluation.schema.StringEvaluator")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/loading.html#load_evaluator)\#     

Load the requested evaluation chain specified by a string.

Parameters:     

  * **evaluator** \([_EvaluatorType_](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")\) – The type of evaluator to load.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _,__optional_\) – The language model to use for evaluation, by default None

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments to pass to the evaluator.

Returns:     

The loaded evaluation chain.

Return type:     

[Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")

Examples               >>> from langchain.evaluation import load_evaluator, EvaluatorType     >>> evaluator = load_evaluator(EvaluatorType.QA)     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)