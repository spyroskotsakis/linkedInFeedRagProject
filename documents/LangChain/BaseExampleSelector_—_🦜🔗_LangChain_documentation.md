# BaseExampleSelector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.base.BaseExampleSelector.html
**Word Count:** 128
**Links Count:** 120
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# BaseExampleSelector\#

_class _langchain\_core.example\_selectors.base.BaseExampleSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/base.html#BaseExampleSelector)\#     

Interface for selecting examples to include in prompts.

Methods

`aadd_example`\(example\) | Async add new example to store.   ---|---   `add_example`\(example\) | Add new example to store.   `aselect_examples`\(input\_variables\) | Async select which examples to use based on the inputs.   `select_examples`\(input\_variables\) | Select which examples to use based on the inputs.      _async _aadd\_example\(

    _example : dict\[str, str\]_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/base.html#BaseExampleSelector.aadd_example)\#     

Async add new example to store.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

_Any_

_abstractmethod _add\_example\(

    _example : dict\[str, str\]_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/base.html#BaseExampleSelector.add_example)\#     

Add new example to store.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

_Any_

_async _aselect\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/base.html#BaseExampleSelector.aselect_examples)\#     

Async select which examples to use based on the inputs.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

list\[dict\]

_abstractmethod _select\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/base.html#BaseExampleSelector.select_examples)\#     

Select which examples to use based on the inputs.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Return type:     

list\[dict\]

Examples using BaseExampleSelector

  * [How to use example selectors](https://python.langchain.com/docs/how_to/example_selectors/)

__On this page