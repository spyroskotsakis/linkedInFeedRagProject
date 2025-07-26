# coro_with_context — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.coro_with_context.html
**Word Count:** 36
**Links Count:** 192
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# coro\_with\_context\#

langchain\_core.runnables.utils.coro\_with\_context\(

    _coro : Awaitable\[Any\]_,     _context : [Context](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.Context.html#langchain_core.beta.runnables.context.Context "langchain_core.beta.runnables.context.Context")_,     _\*_ ,     _create\_task : bool = False_, \) → Awaitable\[Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#coro_with_context)\#     

Await a coroutine with a context.

Parameters:     

  * **coro** \(_Awaitable_ _\[__Any_ _\]_\) – The coroutine to await.

  * **context** \([_Context_](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.Context.html#langchain_core.beta.runnables.context.Context "langchain_core.beta.runnables.context.Context")\) – The context to use.

  * **create\_task** \(_bool_\) – Whether to create a task. Defaults to False.

Returns:     

The coroutine with the context.

Return type:     

Awaitable\[Any\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)