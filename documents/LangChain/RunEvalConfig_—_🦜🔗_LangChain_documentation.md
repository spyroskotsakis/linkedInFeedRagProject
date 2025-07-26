# RunEvalConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.RunEvalConfig.html
**Word Count:** 1983
**Links Count:** 400
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# RunEvalConfig\#

_class _langchain.smith.evaluation.config.RunEvalConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig)\#     

Bases: `BaseModel`

Configuration for a run evaluation.

Parameters:     

  * **evaluators** \(_List_ _\[__Union_ _\[_[_EvaluatorType_](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType") _,_[_EvalConfig_](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.EvalConfig.html#langchain.smith.evaluation.config.EvalConfig "langchain.smith.evaluation.config.EvalConfig") _,__RunEvaluator_ _,__Callable_ _\]__\]_\) – Configurations for which evaluators to apply to the dataset run. Each can be the string of an [`EvaluatorType`](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType"), such as EvaluatorType.QA, the evaluator type string \(“qa”\), or a configuration for a given evaluator \(e.g., `RunEvalConfig.QA`\).

  * **custom\_evaluators** \(_Optional_ _\[__List_ _\[__Union_ _\[__RunEvaluator_ _,_[_StringEvaluator_](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html#langchain.evaluation.schema.StringEvaluator "langchain.evaluation.schema.StringEvaluator") _\]__\]__\]_\) – Custom evaluators to apply to the dataset run.

  * **reference\_key** \(_Optional_ _\[__str_ _\]_\) – The key in the dataset run to use as the reference string. If not provided, it will be inferred automatically.

  * **prediction\_key** \(_Optional_ _\[__str_ _\]_\) – The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

  * **input\_key** \(_Optional_ _\[__str_ _\]_\) – The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

  * **eval\_llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to pass to any evaluators that use a language model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _batch\_evaluators _: list\[Callable\[\[Sequence\[Run\], Sequence\[Example\] | None\], EvaluationResult | EvaluationResults | dict\]\] | None_ _ = None_\#     

Evaluators that run on an aggregate/batch level.

These generate 1 or more metrics that are assigned to the full test run. As a result, they are not associated with individual traces.

_param _custom\_evaluators _: list\[Callable\[\[Run, Example | None\], EvaluationResult | EvaluationResults | dict\] | RunEvaluator | [StringEvaluator](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html#langchain.evaluation.schema.StringEvaluator "langchain.evaluation.schema.StringEvaluator")\] | None_ _ = None_\#     

Custom evaluators to apply to the dataset run.

_param _eval\_llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

The language model to pass to any evaluators that require one.

_param _evaluators _: list\[[EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType") | str | [EvalConfig](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.EvalConfig.html#langchain.smith.evaluation.config.EvalConfig "langchain.smith.evaluation.config.EvalConfig") | Callable\[\[Run, Example | None\], EvaluationResult | EvaluationResults | dict\] | RunEvaluator | [StringEvaluator](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html#langchain.evaluation.schema.StringEvaluator "langchain.evaluation.schema.StringEvaluator")\]__\[Optional\]_\#     

Configurations for which evaluators to apply to the dataset run. Each can be the string of an [`EvaluatorType`](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType"), such as EvaluatorType.QA, the evaluator type string \(“qa”\), or a configuration for a given evaluator \(e.g., `RunEvalConfig.QA`\).

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

_class _CoTQA[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.CoTQA)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a context-based QA evaluator.

Parameters:     

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\) – The prompt template to use for generating the question.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to use for the evaluation chain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.CONTEXT\_QA_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None_ _ = None_\#     

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _ContextQA[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.ContextQA)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a context-based QA evaluator.

Parameters:     

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\) – The prompt template to use for generating the question.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to use for the evaluation chain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.CONTEXT\_QA_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None_ _ = None_\#     

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _Criteria[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.Criteria)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a reference-free criteria evaluator.

Parameters:     

  * **criteria** \(_Optional_ _\[__CRITERIA\_TYPE_ _\]_\) – The criteria to evaluate.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to use for the evaluation chain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _criteria _: Mapping\[str, str\] | [Criteria](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.criteria.eval_chain.Criteria.html#langchain.evaluation.criteria.eval_chain.Criteria "langchain.evaluation.criteria.eval_chain.Criteria") | [ConstitutionalPrinciple](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html#langchain.chains.constitutional_ai.models.ConstitutionalPrinciple "langchain.chains.constitutional_ai.models.ConstitutionalPrinciple") | None_ _ = None_\#     

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.CRITERIA_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _EmbeddingDistance[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.EmbeddingDistance)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for an embedding distance evaluator.

Parameters:     

  * **embeddings** \(_Optional_ _\[_[_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") _\]_\) – The embeddings to use for computing the distance.

  * **distance\_metric** \(_Optional_ _\[__EmbeddingDistanceEnum_ _\]_\) – The distance metric to use for computing the distance.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _distance\_metric _: [EmbeddingDistance](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.embedding_distance.base.EmbeddingDistance.html#langchain.evaluation.embedding_distance.base.EmbeddingDistance "langchain.evaluation.embedding_distance.base.EmbeddingDistance") | None_ _ = None_\#     

_param _embeddings _: [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings") | None_ _ = None_\#     

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.EMBEDDING\_DISTANCE_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _ExactMatch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.ExactMatch)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for an exact match string evaluator.

Parameters:     

  * **ignore\_case** \(_bool_\) – Whether to ignore case when comparing strings.

  * **ignore\_punctuation** \(_bool_\) – Whether to ignore punctuation when comparing strings.

  * **ignore\_numbers** \(_bool_\) – Whether to ignore numbers when comparing strings.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.EXACT\_MATCH_\#     

_param _ignore\_case _: bool_ _ = False_\#     

_param _ignore\_numbers _: bool_ _ = False_\#     

_param _ignore\_punctuation _: bool_ _ = False_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _JsonEqualityEvaluator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.JsonEqualityEvaluator)\#     

Bases: [`EvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.EvalConfig.html#langchain.smith.evaluation.config.EvalConfig "langchain.smith.evaluation.config.EvalConfig")

Configuration for a json equality evaluator.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.JSON\_EQUALITY_\#     

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _JsonValidity[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.JsonValidity)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a json validity evaluator.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.JSON\_VALIDITY_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _LabeledCriteria[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.LabeledCriteria)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a labeled \(with references\) criteria evaluator.

Parameters:     

  * **criteria** \(_Optional_ _\[__CRITERIA\_TYPE_ _\]_\) – The criteria to evaluate.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to use for the evaluation chain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _criteria _: Mapping\[str, str\] | [Criteria](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.criteria.eval_chain.Criteria.html#langchain.evaluation.criteria.eval_chain.Criteria "langchain.evaluation.criteria.eval_chain.Criteria") | [ConstitutionalPrinciple](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html#langchain.chains.constitutional_ai.models.ConstitutionalPrinciple "langchain.chains.constitutional_ai.models.ConstitutionalPrinciple") | None_ _ = None_\#     

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.LABELED\_CRITERIA_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _LabeledScoreString[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.LabeledScoreString)\#     

Bases: `ScoreString`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _criteria _: CRITERIA\_TYPE | None_ _ = None_\#     

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.LABELED\_SCORE\_STRING_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _normalize\_by _: float | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None_ _ = None_\#     

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _QA[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.QA)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a QA evaluator.

Parameters:     

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\) – The prompt template to use for generating the question.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to use for the evaluation chain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.QA_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None_ _ = None_\#     

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _RegexMatch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.RegexMatch)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a regex match string evaluator.

Parameters:     

**flags** \(_int_\) – The flags to pass to the regex. Example: re.IGNORECASE.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.REGEX\_MATCH_\#     

_param _flags _: int_ _ = 0_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _ScoreString[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.ScoreString)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a score string evaluator. This is like the criteria evaluator but it is configured by default to return a score on the scale from 1-10.

It is recommended to normalize these scores by setting normalize\_by to 10.

Parameters:     

  * **criteria** \(_Optional_ _\[__CRITERIA\_TYPE_ _\]_\) – The criteria to evaluate.

  * **llm** \(_Optional_ _\[_[_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _\]_\) – The language model to use for the evaluation chain.

  * **normalize\_by** \(_Optional_ _\[__int_ _\]__= None_\) – If you want to normalize the score, the denominator to use. If not provided, the score will be between 1 and 10 \(by default\).

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _criteria _: Mapping\[str, str\] | [Criteria](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.criteria.eval_chain.Criteria.html#langchain.evaluation.criteria.eval_chain.Criteria "langchain.evaluation.criteria.eval_chain.Criteria") | [ConstitutionalPrinciple](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html#langchain.chains.constitutional_ai.models.ConstitutionalPrinciple "langchain.chains.constitutional_ai.models.ConstitutionalPrinciple") | None_ _ = None_\#     

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.SCORE\_STRING_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None_ _ = None_\#     

_param _normalize\_by _: float | None_ _ = None_\#     

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _prompt _: [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None_ _ = None_\#     

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

_class _StringDistance[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#RunEvalConfig.StringDistance)\#     

Bases: [`SingleKeyEvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html#langchain.smith.evaluation.config.SingleKeyEvalConfig "langchain.smith.evaluation.config.SingleKeyEvalConfig")

Configuration for a string distance evaluator.

Parameters:     

**distance** \(_Optional_ _\[__StringDistanceEnum_ _\]_\) – The string distance metric to use.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _distance _: [StringDistance](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.string_distance.base.StringDistance.html#langchain.evaluation.string_distance.base.StringDistance "langchain.evaluation.string_distance.base.StringDistance") | None_ _ = None_\#     

The string distance metric to use. damerau\_levenshtein: The Damerau-Levenshtein distance. levenshtein: The Levenshtein distance. jaro: The Jaro distance. jaro\_winkler: The Jaro-Winkler distance.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _ = EvaluatorType.STRING\_DISTANCE_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _normalize\_score _: bool_ _ = True_\#     

Whether to normalize the distance to between 0 and 1. Applies only to the Levenshtein and Damerau-Levenshtein distances.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\]\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

__On this page