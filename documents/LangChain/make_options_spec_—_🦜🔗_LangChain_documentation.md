# make_options_spec — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.make_options_spec.html
**Word Count:** 33
**Links Count:** 196
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# make\_options\_spec\#

langchain\_core.runnables.configurable.make\_options\_spec\(

    _spec : [ConfigurableFieldSingleOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") | [ConfigurableFieldMultiOption](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")_,     _description : str | None_, \) → [ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/configurable.html#make_options_spec)\#     

Make a ConfigurableFieldSpec for a ConfigurableFieldSingleOption or ConfigurableFieldMultiOption.

Parameters:     

  * **spec** \([_ConfigurableFieldSingleOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html#langchain_core.runnables.utils.ConfigurableFieldSingleOption "langchain_core.runnables.utils.ConfigurableFieldSingleOption") _|_[_ConfigurableFieldMultiOption_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldMultiOption.html#langchain_core.runnables.utils.ConfigurableFieldMultiOption "langchain_core.runnables.utils.ConfigurableFieldMultiOption")\) – The ConfigurableFieldSingleOption or ConfigurableFieldMultiOption.

  * **description** \(_str_ _|__None_\) – The description to use if the spec does not have one.

Returns:     

The ConfigurableFieldSpec.

Return type:     

[_ConfigurableFieldSpec_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")

__On this page