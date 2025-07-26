# py_anext — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.aiter.py_anext.html
**Word Count:** 92
**Links Count:** 166
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# py\_anext\#

langchain\_core.utils.aiter.py\_anext\(_iterator: ~collections.abc.AsyncIterator\[~langchain\_core.utils.aiter.T\], default: ~langchain\_core.utils.aiter.T | ~typing.Any = <object object>_\) → Awaitable\[T | None | Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/aiter.html#py_anext)\#     

Pure-Python implementation of anext\(\) for testing purposes.

Closely matches the builtin anext\(\) C implementation. Can be used to compare the built-in implementation of the inner coroutines machinery to C-implementation of \_\_anext\_\_\(\) and send\(\) or throw\(\) on the returned generator.

Parameters:     

  * **iterator** \(_AsyncIterator_ _\[__T_ _\]_\) – The async iterator to advance.

  * **default** \(_T_ _|__Any_\) – The value to return if the iterator is exhausted. If not provided, a StopAsyncIteration exception is raised.

Returns:     

The next value from the iterator, or the default value     

if the iterator is exhausted.

Raises:     

**TypeError** – If the iterator is not an async iterator.

Return type:     

_Awaitable_\[_T_ | None | _Any_\]

__On this page