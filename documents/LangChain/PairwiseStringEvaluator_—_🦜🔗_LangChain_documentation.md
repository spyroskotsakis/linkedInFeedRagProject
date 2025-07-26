# PairwiseStringEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.schema.PairwiseStringEvaluator.html
**Word Count:** 149
**Links Count:** 131
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# PairwiseStringEvaluator\#

_class _langchain.evaluation.schema.PairwiseStringEvaluator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#PairwiseStringEvaluator)\#     

Compare the output of two models \(or two outputs of the same model\).

Attributes

`requires_input` | Whether this evaluator requires an input string.   ---|---   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`aevaluate_string_pairs`\(\*, prediction, ...\[, ...\]\) | Asynchronously evaluate the output string pairs.   ---|---   `evaluate_string_pairs`\(\*, prediction, ...\[, ...\]\) | Evaluate the output string pairs.      _async _aevaluate\_string\_pairs\(

    _\*_ ,     _prediction : str_,     _prediction\_b : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#PairwiseStringEvaluator.aevaluate_string_pairs)\#     

Asynchronously evaluate the output string pairs.

Parameters:     

  * **prediction** \(_str_\) – The output string from the first model.

  * **prediction\_b** \(_str_\) – The output string from the second model.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The expected output / reference string.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input string.

  * **kwargs** \(_Any_\) – Additional keyword arguments, such as callbacks and optional reference strings.

Returns:     

A dictionary containing the preference, scores, and/or other information.

Return type:     

dict

evaluate\_string\_pairs\(

    _\*_ ,     _prediction : str_,     _prediction\_b : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/schema.html#PairwiseStringEvaluator.evaluate_string_pairs)\#     

Evaluate the output string pairs.

Parameters:     

  * **prediction** \(_str_\) – The output string from the first model.

  * **prediction\_b** \(_str_\) – The output string from the second model.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The expected output / reference string.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input string.

  * **kwargs** \(_Any_\) – Additional keyword arguments, such as callbacks and optional reference strings.

Returns:     

A dictionary containing the preference, scores, and/or other information.

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)