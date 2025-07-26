# EvalConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.config.EvalConfig.html
**Word Count:** 74
**Links Count:** 110
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# EvalConfig\#

_class _langchain.smith.evaluation.config.EvalConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#EvalConfig)\#     

Bases: `BaseModel`

Configuration for a given run evaluator.

Parameters:     

**evaluator\_type** \([_EvaluatorType_](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")\) – The type of evaluator to use.

get\_kwargs\(\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#EvalConfig.get_kwargs)\#     

Get the keyword arguments for the evaluator configuration.

Return type:     

dict\[str, _Any_\]

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _evaluator\_type _: [EvaluatorType](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.EvaluatorType.html#langchain.evaluation.schema.EvaluatorType "langchain.evaluation.schema.EvaluatorType")_ _\[Required\]_\#     

get\_kwargs\(\) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/config.html#EvalConfig.get_kwargs)\#     

Get the keyword arguments for the load\_evaluator call.

Returns:     

The keyword arguments for the load\_evaluator call.

Return type:     

Dict\[str, Any\]

__On this page