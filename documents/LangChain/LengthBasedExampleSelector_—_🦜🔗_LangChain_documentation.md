# LengthBasedExampleSelector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.length_based.LengthBasedExampleSelector.html
**Word Count:** 185
**Links Count:** 128
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# LengthBasedExampleSelector\#

_class _langchain\_core.example\_selectors.length\_based.LengthBasedExampleSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/length_based.html#LengthBasedExampleSelector)\#     

Bases: [`BaseExampleSelector`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.base.BaseExampleSelector.html#langchain_core.example_selectors.base.BaseExampleSelector "langchain_core.example_selectors.base.BaseExampleSelector"), `BaseModel`

Select examples based on length.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _example\_prompt _: [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_ _\[Required\]_\#     

Prompt template used to format the examples.

_param _example\_text\_lengths _: list\[int\]__\[Optional\]_\#     

Length of each example.

_param _examples _: list\[dict\]__\[Required\]_\#     

A list of the examples that the prompt template expects.

_param _get\_text\_length _: Callable\[\[str\], int\]__ = <function \_get\_length\_based>_\#     

Function to measure prompt length. Defaults to word count.

_param _max\_length _: int_ _ = 2048_\#     

Max length for the prompt, beyond which examples are cut.

_async _aadd\_example\(

    _example : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/length_based.html#LengthBasedExampleSelector.aadd_example)\#     

Async add new example to list.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

None

add\_example\(

    _example : dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/length_based.html#LengthBasedExampleSelector.add_example)\#     

Add new example to list.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

None

_async _aselect\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/length_based.html#LengthBasedExampleSelector.aselect_examples)\#     

Async select which examples to use based on the input lengths.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Returns:     

A list of examples to include in the prompt.

Return type:     

list\[dict\]

select\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/length_based.html#LengthBasedExampleSelector.select_examples)\#     

Select which examples to use based on the input lengths.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Returns:     

A list of examples to include in the prompt.

Return type:     

list\[dict\]

Examples using LengthBasedExampleSelector

  * [How to select examples by length](https://python.langchain.com/docs/how_to/example_selectors_length_based/)

__On this page