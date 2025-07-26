# gather_with_concurrency — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.gather_with_concurrency.html
**Word Count:** 35
**Links Count:** 190
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# gather\_with\_concurrency\#

_async _langchain\_core.runnables.utils.gather\_with\_concurrency\(

    _n : int | None_,     _\* coros: Coroutine_, \) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#gather_with_concurrency)\#     

Gather coroutines with a limit on the number of concurrent coroutines.

Parameters:     

  * **n** \(_Union_ _\[__int_ _,__None_ _\]_\) – The number of coroutines to run concurrently.

  * **\*coros** \(_Coroutine_\) – The coroutines to run.

Returns:     

The results of the coroutines.

Return type:     

list

__On this page