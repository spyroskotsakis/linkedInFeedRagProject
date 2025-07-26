# ExactMatchStringEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.exact_match.base.ExactMatchStringEvaluator.html
**Word Count:** 180
**Links Count:** 133
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# ExactMatchStringEvaluator\#

_class _langchain.evaluation.exact\_match.base.ExactMatchStringEvaluator\(

    _\*_ ,     _ignore\_case : bool = False_,     _ignore\_punctuation : bool = False_,     _ignore\_numbers : bool = False_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/exact_match/base.html#ExactMatchStringEvaluator)\#     

Compute an exact match between the prediction and the reference.

Examples               >>> evaluator = ExactMatchChain()     >>> evaluator.evaluate_strings(             prediction="Mindy is the CTO",             reference="Mindy is the CTO",         )  # This will return {'score': 1.0}                    >>> evaluator.evaluate_strings(             prediction="Mindy is the CTO",             reference="Mindy is the CEO",         )  # This will return {'score': 0.0}     

Attributes

`evaluation_name` | Get the evaluation name.   ---|---   `input_keys` | Get the input keys.   `requires_input` | This evaluator does not require input.   `requires_reference` | This evaluator requires a reference.      Methods

`__init__`\(\*\[, ignore\_case, ...\]\) |    ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      Parameters:     

  * **ignore\_case** \(_bool_\)

  * **ignore\_punctuation** \(_bool_\)

  * **ignore\_numbers** \(_bool_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _\*_ ,     _ignore\_case : bool = False_,     _ignore\_punctuation : bool = False_,     _ignore\_numbers : bool = False_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/exact_match/base.html#ExactMatchStringEvaluator.__init__)\#     

Parameters:     

  * **ignore\_case** \(_bool_\)

  * **ignore\_punctuation** \(_bool_\)

  * **ignore\_numbers** \(_bool_\)

  * **kwargs** \(_Any_\)

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