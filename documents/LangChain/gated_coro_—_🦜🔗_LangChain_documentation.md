# gated_coro — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.gated_coro.html
**Word Count:** 27
**Links Count:** 190
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# gated\_coro\#

_async _langchain\_core.runnables.utils.gated\_coro\(

    _semaphore : asyncio.Semaphore_,     _coro : Coroutine_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#gated_coro)\#     

Run a coroutine with a semaphore.

Parameters:     

  * **semaphore** \(_asyncio.Semaphore_\) – The semaphore to use.

  * **coro** \(_Coroutine_\) – The coroutine to run.

Returns:     

The result of the coroutine.

Return type:     

Any

__On this page