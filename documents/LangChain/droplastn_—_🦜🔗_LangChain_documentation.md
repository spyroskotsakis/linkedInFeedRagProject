# droplastn — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.list.droplastn.html
**Word Count:** 38
**Links Count:** 125
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# droplastn\#

langchain\_core.output\_parsers.list.droplastn\(_iter : Iterator\[T\]_, _n : int_\) → Iterator\[T\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/list.html#droplastn)\#     

Drop the last n elements of an iterator.

Parameters:     

  * **iter** \(_Iterator_ _\[__T_ _\]_\) – The iterator to drop elements from.

  * **n** \(_int_\) – The number of elements to drop.

Yields:     

The elements of the iterator, except the last n elements.

Return type:     

Iterator\[T\]

__On this page