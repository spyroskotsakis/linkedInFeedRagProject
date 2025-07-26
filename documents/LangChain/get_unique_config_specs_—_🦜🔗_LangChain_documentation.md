# get_unique_config_specs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.get_unique_config_specs.html
**Word Count:** 33
**Links Count:** 194
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# get\_unique\_config\_specs\#

langchain\_core.runnables.utils.get\_unique\_config\_specs\(

    _specs : Iterable\[[ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")\]_, \) → list\[[ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#get_unique_config_specs)\#     

Get the unique config specs from a sequence of config specs.

Parameters:     

**specs** \(_Iterable_ _\[_[_ConfigurableFieldSpec_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec") _\]_\) – The config specs.

Returns:     

The unique config specs.

Return type:     

list\[[ConfigurableFieldSpec](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html#langchain_core.runnables.utils.ConfigurableFieldSpec "langchain_core.runnables.utils.ConfigurableFieldSpec")\]

Raises:     

**ValueError** – If the runnable sequence contains conflicting config specs.

__On this page