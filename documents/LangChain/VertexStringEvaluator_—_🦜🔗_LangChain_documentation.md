# VertexStringEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_vertexai/evaluators/langchain_google_vertexai.evaluators.evaluation.VertexStringEvaluator.html
**Word Count:** 155
**Links Count:** 96
**Scraped:** 2025-07-21 08:27:19
**Status:** completed

---

# VertexStringEvaluator\#

_class _langchain\_google\_vertexai.evaluators.evaluation.VertexStringEvaluator\(_metric : str_, _\*\* kwargs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/evaluators/evaluation.html#VertexStringEvaluator)\#     

Evaluate the perplexity of a predicted string.

Attributes

`evaluation_name` | The name of the evaluation.   ---|---   `requires_input` | Whether this evaluator requires an input string.   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`__init__`\(metric, \*\*kwargs\) |    ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate`\(examples, predictions, \*\[, ...\]\) |    `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      Parameters:     

**metric** \(_str_\)

\_\_init\_\_\(_metric : str_, _\*\* kwargs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/evaluators/evaluation.html#VertexStringEvaluator.__init__)\#     

Parameters:     

**metric** \(_str_\)

_async _aevaluate\_strings\(

    _\*_ ,     _prediction : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict\#     

Asynchronously evaluate Chain or LLM output, based on optional input and label.

Parameters:     

  * **prediction** \(_str_\) – The LLM or chain prediction to evaluate.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The reference label to evaluate against.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input to consider during evaluation.

  * **\*\*kwargs** – Additional keyword arguments, including callbacks, tags, etc.

Returns:     

The evaluation results containing the score or value.

Return type:     

dict

evaluate\(

    _examples : Sequence\[Dict\[str, str\]\]_,     _predictions : Sequence\[Dict\[str, str\]\]_,     _\*_ ,     _question\_key : str = 'context'_,     _answer\_key : str = 'reference'_,     _prediction\_key : str = 'prediction'_,     _instruction\_key : str = 'instruction'_,     _\*\* kwargs: Any_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/evaluators/evaluation.html#VertexStringEvaluator.evaluate)\#     

Parameters:     

  * **examples** \(_Sequence_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\)

  * **predictions** \(_Sequence_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\)

  * **question\_key** \(_str_\)

  * **answer\_key** \(_str_\)

  * **prediction\_key** \(_str_\)

  * **instruction\_key** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[dict\]

evaluate\_strings\(

    _\*_ ,     _prediction : str_,     _reference : str | None = None_,     _input : str | None = None_,     _\*\* kwargs: Any_, \) → dict\#     

Evaluate Chain or LLM output, based on optional input and label.

Parameters:     

  * **prediction** \(_str_\) – The LLM or chain prediction to evaluate.

  * **reference** \(_Optional_ _\[__str_ _\]__,__optional_\) – The reference label to evaluate against.

  * **input** \(_Optional_ _\[__str_ _\]__,__optional_\) – The input to consider during evaluation.

  * **\*\*kwargs** – Additional keyword arguments, including callbacks, tags, etc.

Returns:     

The evaluation results containing the score or value.

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)