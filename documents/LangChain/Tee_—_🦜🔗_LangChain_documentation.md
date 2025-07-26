# Tee — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.aiter.Tee.html
**Word Count:** 268
**Links Count:** 174
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# Tee\#

_class _langchain\_core.utils.aiter.Tee\(

    _iterable : AsyncIterator\[T\]_,     _n : int = 2_,     _\*_ ,     _lock : AbstractAsyncContextManager\[Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/aiter.html#Tee)\#     

Create `n` separate asynchronous iterators over `iterable`.

This splits a single `iterable` into multiple iterators, each providing the same items in the same order. All child iterators may advance separately but share the same items from `iterable` – when the most advanced iterator retrieves an item, it is buffered until the least advanced iterator has yielded it as well. A `tee` works lazily and can handle an infinite `iterable`, provided that all iterators advance.               async def derivative(sensor_data):         previous, current = a.tee(sensor_data, n=2)         await a.anext(previous)  # advance one iterator         return a.map(operator.sub, previous, current)     

Unlike `itertools.tee()`, `tee()` returns a custom type instead of a `tuple`. Like a tuple, it can be indexed, iterated and unpacked to get the child iterators. In addition, its `aclose()` method immediately closes all children, and it can be used in an `async with` context for the same effect.

If `iterable` is an iterator and read elsewhere, `tee` will _not_ provide these items. Also, `tee` must internally buffer each item until the last iterator has yielded it; if the most and least advanced iterator differ by most data, using a `list` is more efficient \(but not lazy\).

If the underlying iterable is concurrency safe \(`anext` may be awaited concurrently\) the resulting iterators are concurrency safe as well. Otherwise, the iterators are safe if there is only ever one single “most advanced” iterator. To enforce sequential use of `anext`, provide a `lock` \- e.g. an `asyncio.Lock` instance in an `asyncio` application - and access is automatically synchronised.

Create a `tee`.

Parameters:     

  * **iterable** \(_AsyncIterator_ _\[__T_ _\]_\) – The iterable to split.

  * **n** \(_int_\) – The number of iterators to create. Defaults to 2.

  * **lock** \(_AbstractAsyncContextManager_ _\[__Any_ _\]__|__None_\) – The lock to synchronise access to the shared buffers. Defaults to None.

Methods

`__init__`\(iterable\[, n, lock\]\) | Create a `tee`.   ---|---   `aclose`\(\) | Async close all child iterators.      \_\_init\_\_\(

    _iterable : AsyncIterator\[T\]_,     _n : int = 2_,     _\*_ ,     _lock : AbstractAsyncContextManager\[Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/aiter.html#Tee.__init__)\#     

Create a `tee`.

Parameters:     

  * **iterable** \(_AsyncIterator_ _\[__T_ _\]_\) – The iterable to split.

  * **n** \(_int_\) – The number of iterators to create. Defaults to 2.

  * **lock** \(_AbstractAsyncContextManager_ _\[__Any_ _\]__|__None_\) – The lock to synchronise access to the shared buffers. Defaults to None.

_async _aclose\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/aiter.html#Tee.aclose)\#     

Async close all child iterators.

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)