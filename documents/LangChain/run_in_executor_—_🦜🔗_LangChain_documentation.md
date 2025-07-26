# run_in_executor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.run_in_executor.html
**Word Count:** 57
**Links Count:** 192
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# run\_in\_executor\#

_async _langchain\_core.runnables.config.run\_in\_executor\(_executor\_or\_config: ~concurrent.futures.\_base.Executor | ~langchain\_core.runnables.config.RunnableConfig | None, func: ~typing.Callable\[\[~P\], ~langchain\_core.runnables.config.T\], \*args: ~typing.~P, \*\*kwargs: ~typing.~P_\) → T[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#run_in_executor)\#     

Run a function in an executor.

Parameters:     

  * **executor\_or\_config** \(_Executor_ _|_[_RunnableConfig_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig "langchain_core.runnables.config.RunnableConfig") _|__None_\) – The executor or config to run in.

  * **func** \(_Callable_ _\[__P_ _,__Output_ _\]_\) – The function.

  * **\*args** \(_Any_\) – The positional arguments to the function.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to the function.

Returns:     

The output of the function.

Return type:     

Output

Raises:     

**RuntimeError** – If the function raises a StopIteration.

Examples using run\_in\_executor

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page