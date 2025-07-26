# unique_by_key — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.ensemble.unique_by_key.html
**Word Count:** 43
**Links Count:** 106
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# unique\_by\_key\#

langchain.retrievers.ensemble.unique\_by\_key\(

    _iterable : Iterable\[T\]_,     _key : Callable\[\[T\], H\]_, \) → Iterator\[T\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/retrievers/ensemble.html#unique_by_key)\#     

Yield unique elements of an iterable based on a key function.

Parameters:     

  * **iterable** \(_Iterable_ _\[__T_ _\]_\) – The iterable to filter.

  * **key** \(_Callable_ _\[__\[__T_ _\]__,__H_ _\]_\) – A function that returns a hashable key for each element.

Yields:     

Unique elements of the iterable based on the key function.

Return type:     

_Iterator_\[_T_\]

__On this page