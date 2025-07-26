# abatch_iterate — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.aiter.abatch_iterate.html
**Word Count:** 30
**Links Count:** 166
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# abatch\_iterate\#

_async _langchain\_core.utils.aiter.abatch\_iterate\(

    _size : int_,     _iterable : AsyncIterable\[T\]_, \) → AsyncIterator\[list\[T\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/aiter.html#abatch_iterate)\#     

Utility batching function for async iterables.

Parameters:     

  * **size** \(_int_\) – The size of the batch.

  * **iterable** \(_AsyncIterable_ _\[__T_ _\]_\) – The async iterable to batch.

Returns:     

An async iterator over the batches.

Return type:     

_AsyncIterator_\[list\[_T_\]\]

__On this page