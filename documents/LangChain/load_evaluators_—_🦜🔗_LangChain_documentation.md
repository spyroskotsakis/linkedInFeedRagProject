# load_evaluators — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.loading.load_evaluators.html
**Word Count:** 68
**Links Count:** 130
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# load\_evaluators\#

langchain.evaluation.loading.load\_evaluators\(

    _evaluators : Sequence\[[EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")\]_,     _\*_ ,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _config : dict | None = None_,     _\*\* kwargs: Any_, \) → list\[[Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain") | [StringEvaluator](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html#langchain.evaluation.schema.StringEvaluator "langchain.evaluation.schema.StringEvaluator")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/loading.html#load_evaluators)\#     

Load evaluators specified by a list of evaluator types.

Parameters:     

  * **evaluators** \(_Sequence_ _\[_[_EvaluatorType_](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType") _\]_\) – The list of evaluator types to load.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _,__optional_\) – The language model to use for evaluation, if none is provided, a default ChatOpenAI gpt-4 model will be used.

  * **config** \(_dict_ _,__optional_\) – A dictionary mapping evaluator types to additional keyword arguments, by default None

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments to pass to all evaluators.

Returns:     

The loaded evaluators.

Return type:     

List\[[Chain](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.base.Chain.html#langchain.chains.base.Chain "langchain.chains.base.Chain")\]

Examples               >>> from langchain.evaluation import load_evaluators, EvaluatorType     >>> evaluators = [EvaluatorType.QA, EvaluatorType.CRITERIA]     >>> loaded_evaluators = load_evaluators(evaluators, criteria="helpfulness")     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)