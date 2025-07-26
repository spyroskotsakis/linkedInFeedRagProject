# prefix_config_spec — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.configurable.prefix_config_spec.html
**Word Count:** 38
**Links Count:** 194
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# prefix\_config\_spec\#

langchain\_core.runnables.configurable.prefix\_config\_spec\(

    _spec : [ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")_,     _prefix : str_, \) → [ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/configurable.html#prefix_config_spec)\#     

Prefix the id of a ConfigurableFieldSpec.

This is useful when a RunnableConfigurableAlternatives is used as a ConfigurableField of another RunnableConfigurableAlternatives.

Parameters:     

  * **spec** \([_ConfigurableFieldSpec_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")\) – The ConfigurableFieldSpec to prefix.

  * **prefix** \(_str_\) – The prefix to add.

Returns:     

The prefixed ConfigurableFieldSpec.

Return type:     

[ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")

__On this page