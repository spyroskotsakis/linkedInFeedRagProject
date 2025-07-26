# SingleKeyEvalConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.SingleKeyEvalConfig.html
**Word Count:** 126
**Links Count:** 113
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# SingleKeyEvalConfig\#

_class _langchain.smith.evaluation.config.SingleKeyEvalConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#SingleKeyEvalConfig)\#     

Bases: [`EvalConfig`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.EvalConfig.html#langchain.smith.evaluation.config.EvalConfig "langchain.smith.evaluation.config.EvalConfig")

Configuration for a run evaluator that only requires a single key.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _\[Required\]_\#     

_param _input\_key _: str | None_ _ = None_\#     

The key from the traced run’s inputs dictionary to use to represent the input. If not provided, it will be inferred automatically.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the traced run’s outputs dictionary to use to represent the prediction. If not provided, it will be inferred automatically.

_param _reference\_key _: str | None_ _ = None_\#     

The key in the dataset run to use as the reference string. If not provided, we will attempt to infer automatically.

get\_kwargs\(\) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#SingleKeyEvalConfig.get_kwargs)\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

__On this page