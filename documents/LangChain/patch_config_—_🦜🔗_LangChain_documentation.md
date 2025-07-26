# patch_config — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.patch_config.html
**Word Count:** 63
**Links Count:** 196
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# patch\_config\#

langchain\_core.runnables.config.patch\_config\(

    _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") | None_,     _\*_ ,     _callbacks : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _recursion\_limit : int | None = None_,     _max\_concurrency : int | None = None_,     _run\_name : str | None = None_,     _configurable : dict\[str, Any\] | None = None_, \) → [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#patch_config)\#     

Patch a config with new values.

Parameters:     

  * **config** \(_Optional_ _\[_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]_\) – The config to patch.

  * **callbacks** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]__,__optional_\) – The callbacks to set. Defaults to None.

  * **recursion\_limit** \(_Optional_ _\[__int_ _\]__,__optional_\) – The recursion limit to set. Defaults to None.

  * **max\_concurrency** \(_Optional_ _\[__int_ _\]__,__optional_\) – The max concurrency to set. Defaults to None.

  * **run\_name** \(_Optional_ _\[__str_ _\]__,__optional_\) – The run name to set. Defaults to None.

  * **configurable** \(_Optional_ _\[__dict_ _\[__str_ _,__Any_ _\]__\]__,__optional_\) – The configurable to set. Defaults to None.

Returns:     

The patched config.

Return type:     

[RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)