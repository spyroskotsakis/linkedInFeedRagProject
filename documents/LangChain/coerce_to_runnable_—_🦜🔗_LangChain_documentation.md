# coerce_to_runnable — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.coerce_to_runnable.html
**Word Count:** 25
**Links Count:** 194
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# coerce\_to\_runnable\#

langchain\_core.runnables.base.coerce\_to\_runnable\(

    _thing : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[Input\], Output\] | Callable\[\[Input\], Awaitable\[Output\]\] | Callable\[\[Iterator\[Input\]\], Iterator\[Output\]\] | Callable\[\[AsyncIterator\[Input\]\], AsyncIterator\[Output\]\] | \_RunnableCallableSync\[Input, Output\] | \_RunnableCallableAsync\[Input, Output\] | \_RunnableCallableIterator\[Input, Output\] | \_RunnableCallableAsyncIterator\[Input, Output\] | Mapping\[str, Any\]_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#coerce_to_runnable)\#     

Coerce a Runnable-like object into a Runnable.

Parameters:     

**thing** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__|__Callable_ _\[__\[__Iterator_ _\[__Input_ _\]__\]__,__Iterator_ _\[__Output_ _\]__\]__|__Callable_ _\[__\[__AsyncIterator_ _\[__Input_ _\]__\]__,__AsyncIterator_ _\[__Output_ _\]__\]__|__\_RunnableCallableSync_ _\[__Input_ _,__Output_ _\]__|__\_RunnableCallableAsync_ _\[__Input_ _,__Output_ _\]__|__\_RunnableCallableIterator_ _\[__Input_ _,__Output_ _\]__|__\_RunnableCallableAsyncIterator_ _\[__Input_ _,__Output_ _\]__|__Mapping_ _\[__str_ _,__Any_ _\]_\) – A Runnable-like object.

Returns:     

A Runnable.

Raises:     

**TypeError** – If the object is not Runnable-like.

Return type:     

[_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[_Input_ , _Output_\]

__On this page