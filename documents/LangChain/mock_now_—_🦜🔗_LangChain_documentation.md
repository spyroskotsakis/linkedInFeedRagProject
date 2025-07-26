# mock_now — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.mock_now.html
**Word Count:** 50
**Links Count:** 167
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# mock\_now\#

langchain\_core.utils.utils.mock\_now\(

    _dt\_value : datetime_, \) → Iterator\[type\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#mock_now)\#     

Context manager for mocking out datetime.now\(\) in unit tests.

Parameters:     

**dt\_value** \(_datetime_\) – The datetime value to use for datetime.now\(\).

Yields:     

_datetime.datetime_ – The mocked datetime class.

Return type:     

_Iterator_\[type\]

Example: with mock\_now\(datetime.datetime\(2011, 2, 3, 10, 11\)\):

> assert datetime.datetime.now\(\) == datetime.datetime\(2011, 2, 3, 10, 11\)

Examples using mock\_now

  * [How to use a time-weighted vector store retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)

__On this page