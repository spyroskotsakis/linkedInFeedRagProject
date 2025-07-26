# JsonSchemaEvaluator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.parsing.json_schema.JsonSchemaEvaluator.html
**Word Count:** 250
**Links Count:** 142
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# JsonSchemaEvaluator\#

_class _langchain.evaluation.parsing.json\_schema.JsonSchemaEvaluator\(_\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/json_schema.html#JsonSchemaEvaluator)\#     

An evaluator that validates a JSON prediction against a JSON schema reference.

This evaluator checks if a given JSON prediction conforms to the provided JSON schema. If the prediction is valid, the score is True \(no errors\). Otherwise, the score is False \(error occurred\).

requires\_input\#     

Whether the evaluator requires input.

Type:     

bool

requires\_reference\#     

Whether the evaluator requires reference.

Type:     

bool

evaluation\_name\#     

The name of the evaluation.

Type:     

str

Examples

evaluator = JsonSchemaEvaluator\(\) result = evaluator.evaluate\_strings\(

> prediction=’\{“name”: “John”, “age”: 30\}’, reference=\{ >
>> “type”: “object”, “properties”: \{ >> >>> “name”: \{“type”: “string”\}, “age”: \{“type”: “integer”\} >>  >> \} >  > \}

\) assert result\[“score”\] is not None

Initializes the JsonSchemaEvaluator.

Parameters:     

**kwargs** \(_Any_\) – Additional keyword arguments.

Raises:     

**ImportError** – If the jsonschema package is not installed.

Attributes

`evaluation_name` | Returns the name of the evaluation.   ---|---   `requires_input` | Returns whether the evaluator requires input.   `requires_reference` | Returns whether the evaluator requires reference.      Methods

`__init__`\(\*\*kwargs\) | Initializes the JsonSchemaEvaluator.   ---|---   `aevaluate_strings`\(\*, prediction\[, ...\]\) | Asynchronously evaluate Chain or LLM output, based on optional input and label.   `evaluate_strings`\(\*, prediction\[, reference, ...\]\) | Evaluate Chain or LLM output, based on optional input and label.      \_\_init\_\_\(_\*\* kwargs: Any_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/parsing/json_schema.html#JsonSchemaEvaluator.__init__)\#     

Initializes the JsonSchemaEvaluator.

Parameters:     

**kwargs** \(_Any_\) – Additional keyword arguments.

Raises:     

**ImportError** – If the jsonschema package is not installed.

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