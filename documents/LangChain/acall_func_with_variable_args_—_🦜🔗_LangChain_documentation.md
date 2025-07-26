# acall_func_with_variable_args — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.acall_func_with_variable_args.html
**Word Count:** 62
**Links Count:** 202
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# acall\_func\_with\_variable\_args\#

langchain\_core.runnables.config.acall\_func\_with\_variable\_args\(

    _func : Callable\[\[Input\], Awaitable\[Output\]\] | Callable\[\[Input, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Awaitable\[Output\]\] | Callable\[\[Input, [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\], Awaitable\[Output\]\] | Callable\[\[Input, [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun"), [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Awaitable\[Output\]\]_,     _input : Input_,     _config : [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")_,     _run\_manager : [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") | None = None_,     _\*\* kwargs: Any_, \) → Awaitable\[Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#acall_func_with_variable_args)\#     

Async call function that may optionally accept a run\_manager and/or config.

Parameters:     

  * **func** \(_Union_ _\[__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Awaitable_ _\[__Output_ _\]__\]__\]_\) – The function to call.

  * **input** \(_Input_\) – The input to the function.

  * **config** \([_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\) – The config to pass to the function.

  * **run\_manager** \(_Optional_ _\[_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _\]_\) – The run manager to pass to the function. Defaults to None.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to pass to the function.

Returns:     

The output of the function.

Return type:     

Awaitable\[Output\]

__On this page