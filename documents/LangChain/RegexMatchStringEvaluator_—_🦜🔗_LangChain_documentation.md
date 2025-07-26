# RegexMatchStringEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.regex_match.base.RegexMatchStringEvaluator.html
**Word Count:** 197
**Links Count:** 133
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# RegexMatchStringEvaluator\#

_class _langchain.evaluation.regex\_match.base.RegexMatchStringEvaluator\(

    _\*_ ,     _flags : int = 0_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/regex_match/base.html#RegexMatchStringEvaluator)\#     

Compute a regex match between the prediction and the reference.

Examples               >>> evaluator = RegexMatchStringEvaluator(flags=re.IGNORECASE)     >>> evaluator.evaluate_strings(             prediction="Mindy is the CTO",             reference="^mindy.*cto$",         )  # This will return {'score': 1.0} due to the IGNORECASE flag                    >>> evaluator = RegexMatchStringEvaluator()     >>> evaluator.evaluate_strings(             prediction="Mindy is the CTO",             reference="^Mike.*CEO$",         )  # This will return {'score': 0.0}                    >>> evaluator.evaluate_strings(             prediction="Mindy is the CTO",             reference="^Mike.*CEO$|^Mindy.*CTO$",         )  # This will return {'score': 1.0} as the prediction matches the second pattern in the union     

Attributes

`evaluation_name` | Get the evaluation name.   ---|---   `input_keys` | Get the input keys.   `requires_input` | This evaluator does not require input.   `requires_reference` | This evaluator requires a reference.      Methods

`__init__`\(\*\[, flags\]\) |    ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      Parameters:     

  * **flags** \(_int_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _\*_ ,     _flags : int = 0_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/regex_match/base.html#RegexMatchStringEvaluator.__init__)\#     

Parameters:     

  * **flags** \(_int_\)

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