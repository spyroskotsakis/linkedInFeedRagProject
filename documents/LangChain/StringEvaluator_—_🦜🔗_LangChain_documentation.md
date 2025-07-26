# StringEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.StringEvaluator.html
**Word Count:** 158
**Links Count:** 131
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# StringEvaluator\#

_class _langchain.evaluation.schema.StringEvaluator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#StringEvaluator)\#     

Grade, tag, or otherwise evaluate predictions relative to their inputs and/or reference labels.

Attributes

`evaluation_name` | The name of the evaluation.   ---|---   `requires_input` | Whether this evaluator requires an input string.   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   ---|---   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      _async _aevaluate\_strings\(

    _\*_ ,     _prediction : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#StringEvaluator.aevaluate_strings)\#     

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

    _\*_ ,     _prediction : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#StringEvaluator.evaluate_strings)\#     

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