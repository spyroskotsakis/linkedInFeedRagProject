# NGramOverlapExampleSelector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/example_selectors/langchain_community.example_selectors.ngram_overlap.NGramOverlapExampleSelector.html
**Word Count:** 195
**Links Count:** 119
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# NGramOverlapExampleSelector\#

_class _langchain\_community.example\_selectors.ngram\_overlap.NGramOverlapExampleSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/example_selectors/ngram_overlap.html#NGramOverlapExampleSelector)\#     

Bases: [`BaseExampleSelector`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.base.BaseExampleSelector.html#langchain_core.example_selectors.base.BaseExampleSelector "langchain_core.example_selectors.base.BaseExampleSelector"), `BaseModel`

Select and order examples based on ngram overlap score \(sentence\_bleu score from NLTK package\).

<https://www.nltk.org/_modules/nltk/translate/bleu_score.html> <https://aclanthology.org/P02-1040.pdf>

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _example\_prompt _: [PromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.prompt.PromptTemplate.html#langchain_core.prompts.prompt.PromptTemplate "langchain_core.prompts.prompt.PromptTemplate")_ _\[Required\]_\#     

Prompt template used to format the examples.

_param _examples _: List\[dict\]__\[Required\]_\#     

A list of the examples that the prompt template expects.

_param _threshold _: float_ _ = -1.0_\#     

Threshold at which algorithm stops. Set to -1.0 by default.

For negative threshold: select\_examples sorts examples by ngram\_overlap\_score, but excludes none. For threshold greater than 1.0: select\_examples excludes all examples, and returns an empty list. For threshold equal to 0.0: select\_examples sorts examples by ngram\_overlap\_score, and excludes examples with no ngram overlap with input.

_async _aadd\_example\(

    _example : dict\[str, str\]_, \) → Any\#     

Async add new example to store.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

_Any_

add\_example\(

    _example : Dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/example_selectors/ngram_overlap.html#NGramOverlapExampleSelector.add_example)\#     

Add new example to list.

Parameters:     

**example** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

None

_async _aselect\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\]\#     

Async select which examples to use based on the inputs.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

list\[dict\]

select\_examples\(

    _input\_variables : Dict\[str, str\]_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/example_selectors/ngram_overlap.html#NGramOverlapExampleSelector.select_examples)\#     

Return list of examples sorted by ngram\_overlap\_score with input.

Descending order. Excludes any examples with ngram\_overlap\_score less than or equal to threshold.

Parameters:     

**input\_variables** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Return type:     

_List_\[dict\]

Examples using NGramOverlapExampleSelector

  * [How to select examples by n-gram overlap](https://python.langchain.com/docs/how_to/example_selectors_ngram/)

__On this page