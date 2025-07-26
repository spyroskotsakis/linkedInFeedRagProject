# JsonEditDistanceEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.parsing.json_distance.JsonEditDistanceEvaluator.html
**Word Count:** 275
**Links Count:** 137
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# JsonEditDistanceEvaluator\#

_class _langchain.evaluation.parsing.json\_distance.JsonEditDistanceEvaluator\(

    _string\_distance : Callable\[\[str, str\], float\] | None = None_,     _canonicalize : Callable\[\[Any\], Any\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/json_distance.html#JsonEditDistanceEvaluator)\#     

An evaluator that calculates the edit distance between JSON strings.

This evaluator computes a normalized Damerau-Levenshtein distance between two JSON strings after parsing them and converting them to a canonical format \(i.e., whitespace and key order are normalized\). It can be customized with alternative distance and canonicalization functions.

Parameters:     

  * **string\_distance** \(_Optional_ _\[__Callable_ _\[__\[__str_ _,__str_ _\]__,__float_ _\]__\]_\) – A callable that computes the distance between two strings. If not provided, a Damerau-Levenshtein distance from the rapidfuzz package will be used.

  * **canonicalize** \(_Optional_ _\[__Callable_ _\[__\[__Any_ _\]__,__Any_ _\]__\]_\) – A callable that converts a parsed JSON object into its canonical string form. If not provided, the default behavior is to serialize the JSON with sorted keys and no extra whitespace.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments.

\_string\_distance\#     

The internal distance computation function.

Type:     

Callable\[\[str, str\], float\]

\_canonicalize\#     

The internal canonicalization function.

Type:     

Callable\[\[Any\], Any\]

Examples               >>> evaluator = JsonEditDistanceEvaluator()     >>> result = evaluator.evaluate_strings(prediction='{"a": 1, "b": 2}', reference='{"a": 1, "b": 3}')     >>> assert result["score"] is not None     

Raises:     

**ImportError** – If rapidfuzz is not installed and no alternative string\_distance function is provided.

Parameters:     

  * **string\_distance** \(_Callable_ _\[__\[__str_ _,__str_ _\]__,__float_ _\]__|__None_\)

  * **canonicalize** \(_Callable_ _\[__\[__Any_ _\]__,__Any_ _\]__|__None_\)

  * **kwargs** \(_Any_\)

Attributes

`evaluation_name` | The name of the evaluation.   ---|---   `requires_input` | Whether this evaluator requires an input string.   `requires_reference` | Whether this evaluator requires a reference label.      Methods

`__init__`\(\[string\_distance, canonicalize\]\) |    ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      \_\_init\_\_\(

    _string\_distance : Callable\[\[str, str\], float\] | None = None_,     _canonicalize : Callable\[\[Any\], Any\] | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/json_distance.html#JsonEditDistanceEvaluator.__init__)\#     

Parameters:     

  * **string\_distance** \(_Callable_ _\[__\[__str_ _,__str_ _\]__,__float_ _\]__|__None_\)

  * **canonicalize** \(_Callable_ _\[__\[__Any_ _\]__,__Any_ _\]__|__None_\)

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