# JsonValidityEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.parsing.base.JsonValidityEvaluator.html
**Word Count:** 215
**Links Count:** 142
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# JsonValidityEvaluator\#

_class _langchain.evaluation.parsing.base.JsonValidityEvaluator\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/base.html#JsonValidityEvaluator)\#     

Evaluate whether the prediction is valid JSON.

This evaluator checks if the prediction is a valid JSON string. It does not     

require any input or reference.

Parameters:     

**kwargs** \(_Any_\)

requires\_input\#     

Whether this evaluator requires an input string. Always False.

Type:     

bool

requires\_reference\#     

Whether this evaluator requires a reference string. Always False.

Type:     

bool

evaluation\_name\#     

The name of the evaluation metric. Always “json”.

Type:     

str

Examples               >>> evaluator = JsonValidityEvaluator()     >>> prediction = '{"name": "John", "age": 30, "city": "New York"}'     >>> evaluator.evaluate(prediction)     {'score': 1}                    >>> prediction = '{"name": "John", "age": 30, "city": "New York",}'     >>> evaluator.evaluate(prediction)     {'score': 0, 'reasoning': 'Expecting property name enclosed in double quotes'}     

Attributes

`evaluation_name` | The name of the evaluation.   ---|---   `requires_input` | Whether this evaluator requires an input string.   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`__init__`\(\*\*kwargs\) |    ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      \_\_init\_\_\(

    _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/base.html#JsonValidityEvaluator.__init__)\#     

Parameters:     

**kwargs** \(_Any_\)

Return type:     

None

_async _aevaluate\_strings\(

    _\*_ ,     _prediction : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict\#     

Asynchronously evaluate Chain or LLM output, based on optional input and label.

Parameters:     

  * **prediction** \(_str_\) – The LLM or chain prediction to evaluate.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The reference label to evaluate against.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input to consider during evaluation.

  * **kwargs** \(_Any_\) – Additional keyword arguments, including callbacks, tags, etc.

Returns:     

The evaluation results containing the score or value.

Return type:     

dict

evaluate\_strings\(

    _\*_ ,     _prediction : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict\#     

Evaluate Chain or LLM output, based on optional input and label.

Parameters:     

  * **prediction** \(_str_\) – The LLM or chain prediction to evaluate.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The reference label to evaluate against.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input to consider during evaluation.

  * **kwargs** \(_Any_\) – Additional keyword arguments, including callbacks, tags, etc.

Returns:     

The evaluation results containing the score or value.

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)