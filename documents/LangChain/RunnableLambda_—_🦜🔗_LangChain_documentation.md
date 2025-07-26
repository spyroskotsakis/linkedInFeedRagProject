# RunnableLambda — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableLambda.html
**Word Count:** 269
**Links Count:** 236
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# RunnableLambda\#

_class _langchain\_core.runnables.base.RunnableLambda\(

    _func : Callable\[\[Input\], Iterator\[Output\]\] | Callable\[\[Input\], [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\]\] | Callable\[\[Input\], Output\] | Callable\[\[Input, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Output\] | Callable\[\[Input, [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun")\], Output\] | Callable\[\[Input, [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun"), [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Output\] | Callable\[\[Input\], Awaitable\[Output\]\] | Callable\[\[Input\], AsyncIterator\[Output\]\] | Callable\[\[Input, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Awaitable\[Output\]\] | Callable\[\[Input, [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\], Awaitable\[Output\]\] | Callable\[\[Input, [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun"), [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Awaitable\[Output\]\]_,     _afunc : Callable\[\[Input\], Awaitable\[Output\]\] | Callable\[\[Input\], AsyncIterator\[Output\]\] | Callable\[\[Input, [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Awaitable\[Output\]\] | Callable\[\[Input, [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun")\], Awaitable\[Output\]\] | Callable\[\[Input, [AsyncCallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun"), [RunnableConfig](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig")\], Awaitable\[Output\]\] | None = None_,     _name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#RunnableLambda)\#     

RunnableLambda converts a python callable into a Runnable.

Wrapping a callable in a RunnableLambda makes the callable usable within either a sync or async context.

RunnableLambda can be composed as any other Runnable and provides seamless integration with LangChain tracing.

`RunnableLambda` is best suited for code that does not need to support streaming. If you need to support streaming \(i.e., be able to operate on chunks of inputs and yield chunks of outputs\), use `RunnableGenerator` instead.

Note that if a `RunnableLambda` returns an instance of `Runnable`, that instance is invoked \(or streamed\) during execution.

Examples               # This is a RunnableLambda     from langchain_core.runnables import RunnableLambda          def add_one(x: int) -> int:         return x + 1          runnable = RunnableLambda(add_one)          runnable.invoke(1) # returns 2     runnable.batch([1, 2, 3]) # returns [2, 3, 4]          # Async is supported by default by delegating to the sync implementation     await runnable.ainvoke(1) # returns 2     await runnable.abatch([1, 2, 3]) # returns [2, 3, 4]               # Alternatively, can provide both synd and sync implementations     async def add_one_async(x: int) -> int:         return x + 1          runnable = RunnableLambda(add_one, afunc=add_one_async)     runnable.invoke(1) # Uses add_one     await runnable.ainvoke(1) # Uses add_one_async     

Create a RunnableLambda from a callable, and async callable or both.

Accepts both sync and async variants to allow providing efficient implementations for sync and async execution.

Parameters:     

  * **func** \(_Union_ _\[__Union_ _\[__Callable_ _\[__\[__Input_ _\]__,__Iterator_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _\]__,_[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _\]__,__Output_ _\]__,__Callable_ _\[__\[__Input_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Output_ _\]__,__Callable_ _\[__\[__Input_ _,_[_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _\]__,__Output_ _\]__,__Callable_ _\[__\[__Input_ _,_[_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Output_ _\]__\]__,__Union_ _\[__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _\]__,__AsyncIterator_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Awaitable_ _\[__Output_ _\]__\]__\]__\]_\) – Either sync or async callable

  * **afunc** \(_Optional_ _\[__Union_ _\[__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _\]__,__AsyncIterator_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _\]__,__Awaitable_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__Input_ _,_[_AsyncCallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun.html#langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun "langchain_core.callbacks.manager.AsyncCallbackManagerForChainRun") _,_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _\]__,__Awaitable_ _\[__Output_ _\]__\]__\]__\]_\) – An async callable that takes an input and returns an output. Defaults to None.

  * **name** \(_str_ _|__None_\) – The name of the Runnable. Defaults to None.

Raises:     

  * **TypeError** – If the func is not a callable type.

  * **TypeError** – If both func and afunc are provided.

Note

RunnableLambda implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

> The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

Attributes

Methods

`__init__`\(\*args, \*\*kwargs\) | Initialize self.   ---|---      Examples using RunnableLambda

  * [How to convert Runnables as Tools](https://python.langchain.com/docs/how_to/convert_runnable_to_tool/)

  * [How to dispatch custom callback events](https://python.langchain.com/docs/how_to/callbacks_custom_events/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to retry when a parsing error occurs](https://python.langchain.com/docs/how_to/output_parser_retry/)

  * [How to route between sub-chains](https://python.langchain.com/docs/how_to/routing/)

  * [How to run custom functions](https://python.langchain.com/docs/how_to/functions/)

  * [How to select examples from a LangSmith dataset](https://python.langchain.com/docs/how_to/example_selectors_langsmith/)

  * [How to stream runnables](https://python.langchain.com/docs/how_to/streaming/)

  * [LangChain Expression Language Cheatsheet](https://python.langchain.com/docs/how_to/lcel_cheatsheet/)

  * [Upstash Ratelimit Callback](https://python.langchain.com/docs/integrations/callbacks/upstash_ratelimit/)

  * [Vector stores and retrievers](https://python.langchain.com/docs/tutorials/retrievers/)

  * [🦜️🏓 LangServe](https://python.langchain.com/docs/langserve/)

__On this page