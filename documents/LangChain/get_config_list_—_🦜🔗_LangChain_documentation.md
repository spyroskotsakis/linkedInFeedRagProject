# get_config_list — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.get_config_list.html
**Word Count:** 60
**Links Count:** 196
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# get\_config\_list\#

langchain\_core.runnables.config.get\_config\_list\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | Sequence\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\] | None_,     _length : int_, \) → list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#get_config_list)\#     

Get a list of configs from a single config or a list of configs.

> It is useful for subclasses overriding batch\(\) or abatch\(\).

Parameters:     

  * **config** \(_Optional_ _\[__Union_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _,__list_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__\]__\]_\) – The config or list of configs.

  * **length** \(_int_\) – The length of the list.

Returns:     

The list of configs.

Return type:     

list\[[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\]

Raises:     

**ValueError** – If the length of the list is not equal to the length of the inputs.

__On this page