# batch_iterate — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.iter.batch_iterate.html
**Word Count:** 31
**Links Count:** 166
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# batch\_iterate\#

langchain\_core.utils.iter.batch\_iterate\(

    _size : int | None_,     _iterable : Iterable\[T\]_, \) → Iterator\[list\[T\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/iter.html#batch_iterate)\#     

Utility batching function.

Parameters:     

  * **size** \(_int_ _|__None_\) – The size of the batch. If None, returns a single batch.

  * **iterable** \(_Iterable_ _\[__T_ _\]_\) – The iterable to batch.

Yields:     

The batches of the iterable.

Return type:     

_Iterator_\[list\[_T_\]\]

__On this page