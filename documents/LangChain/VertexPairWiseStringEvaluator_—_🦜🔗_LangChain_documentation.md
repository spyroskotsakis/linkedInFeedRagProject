# VertexPairWiseStringEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/evaluators/langchain_google_vertexai.evaluators.evaluation.VertexPairWiseStringEvaluator.html
**Word Count:** 142
**Links Count:** 92
**Scraped:** 2025-07-21 08:27:18
**Status:** completed

---

# VertexPairWiseStringEvaluator\#

_class _langchain\_google\_vertexai.evaluators.evaluation.VertexPairWiseStringEvaluator\(_metric : str_, _\*\* kwargs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/evaluators/evaluation.html#VertexPairWiseStringEvaluator)\#     

Evaluate the perplexity of a predicted string.

Attributes

`requires_input` | Whether this evaluator requires an input string.   ---|---   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`__init__`\(metric, \*\*kwargs\) |    ---|---   `aevaluate_string_pairs`\(\*, prediction, ...\[, ...\]\) | Asynchronously evaluate the output string pairs.   `evaluate_string_pairs`\(\*, prediction, ...\[, ...\]\) | Evaluate the output string pairs.      Parameters:     

**metric** \(_str_\)

\_\_init\_\_\(

    _metric : str_,     _\*\* kwargs_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/evaluators/evaluation.html#VertexPairWiseStringEvaluator.__init__)\#     

Parameters:     

**metric** \(_str_\)

_async _aevaluate\_string\_pairs\(

    _\*_ ,     _prediction : str_,     _prediction\_b : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict\#     

Asynchronously evaluate the output string pairs.

Parameters:     

  * **prediction** \(_str_\) – The output string from the first model.

  * **prediction\_b** \(_str_\) – The output string from the second model.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The expected output / reference string.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input string.

  * **\*\*kwargs** – Additional keyword arguments, such as callbacks and optional reference strings.

Returns:     

A dictionary containing the preference, scores, and/or other information.

Return type:     

dict

evaluate\_string\_pairs\(

    _\*_ ,     _prediction : str_,     _prediction\_b : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict\#     

Evaluate the output string pairs.

Parameters:     

  * **prediction** \(_str_\) – The output string from the first model.

  * **prediction\_b** \(_str_\) – The output string from the second model.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The expected output / reference string.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input string.

  * **\*\*kwargs** – Additional keyword arguments, such as callbacks and optional reference strings.

Returns:     

A dictionary containing the preference, scores, and/or other information.

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)