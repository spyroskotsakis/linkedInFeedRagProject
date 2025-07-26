# process_value — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/query_constructors/langchain_community.query_constructors.milvus.process_value.html
**Word Count:** 40
**Links Count:** 123
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# process\_value\#

langchain\_community.query\_constructors.milvus.process\_value\(

    _value : int | float | str_,     _comparator : [Comparator](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/query_constructors/milvus.html#process_value)\#     

Convert a value to a string and add double quotes if it is a string.

It required for comparators involving strings.

Parameters:     

  * **value** \(_int_ _|__float_ _|__str_\) – The value to convert.

  * **comparator** \([_Comparator_](https://python.langchain.com/api_reference/core/structured_query/langchain_core.structured_query.Comparator.html#langchain_core.structured_query.Comparator "langchain_core.structured_query.Comparator")\) – The comparator.

Returns:     

The converted value as a string.

Return type:     

str

__On this page