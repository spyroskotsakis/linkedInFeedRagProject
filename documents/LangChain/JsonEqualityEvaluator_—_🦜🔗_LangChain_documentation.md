# JsonEqualityEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.parsing.base.JsonEqualityEvaluator.html
**Word Count:** 219
**Links Count:** 142
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# JsonEqualityEvaluator\#

_class _langchain.evaluation.parsing.base.JsonEqualityEvaluator\(

    _operator : Callable | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/base.html#JsonEqualityEvaluator)\#     

Evaluate whether the prediction is equal to the reference after     

parsing both as JSON.

This evaluator checks if the prediction, after parsing as JSON, is equal     

to the reference,

which is also parsed as JSON. It does not require an input string.

Parameters:     

  * **operator** \(_Callable_ _|__None_\)

  * **kwargs** \(_Any_\)

requires\_input\#     

Whether this evaluator requires an input string. Always False.

Type:     

bool

requires\_reference\#     

Whether this evaluator requires a reference string. Always True.

Type:     

bool

evaluation\_name\#     

The name of the evaluation metric. Always “parsed\_equality”.

Type:     

str

Examples               >>> evaluator = JsonEqualityEvaluator()     >>> evaluator.evaluate_strings('{"a": 1}', reference='{"a": 1}')     {'score': True}     >>> evaluator.evaluate_strings('{"a": 1}', reference='{"a": 2}')     {'score': False}                    >>> evaluator = JsonEqualityEvaluator(operator=lambda x, y: x['a'] == y['a'])     >>> evaluator.evaluate_strings('{"a": 1}', reference='{"a": 1}')     {'score': True}     >>> evaluator.evaluate_strings('{"a": 1}', reference='{"a": 2}')     {'score': False}     

Attributes

`evaluation_name` | The name of the evaluation.   ---|---   `requires_input` | Whether this evaluator requires an input string.   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`__init__`\(\[operator\]\) |    ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      \_\_init\_\_\(

    _operator : Callable | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/base.html#JsonEqualityEvaluator.__init__)\#     

Parameters:     

  * **operator** \(_Callable_ _|__None_\)

  * **kwargs** \(_Any_\)

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