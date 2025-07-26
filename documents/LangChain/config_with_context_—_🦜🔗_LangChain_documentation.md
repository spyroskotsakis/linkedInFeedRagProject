# config_with_context — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.config_with_context.html
**Word Count:** 27
**Links Count:** 110
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# config\_with\_context\#

langchain\_core.beta.runnables.context.config\_with\_context\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")_,     _steps : list\[[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\]_, \) → [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#config_with_context)\#     

Patch a runnable config with context getters and setters.

Parameters:     

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\) – The runnable config.

  * **steps** \(_list_ _\[_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\]_\) – The runnable steps.

Returns:     

The patched runnable config.

Return type:     

[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")

__On this page