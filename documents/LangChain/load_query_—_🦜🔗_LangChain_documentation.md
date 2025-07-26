# load_query — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.load_query.html
**Word Count:** 54
**Links Count:** 249
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# load\_query\#

langchain\_community.utilities.clickup.load\_query\(

    _query : str_,     _fault\_tolerant : bool = False_, \) → Tuple\[Dict | None, str | None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#load_query)\#     

Parse a JSON string and return the parsed object.

If parsing fails, returns an error message.

Parameters:     

  * **query** \(_str_\) – The JSON string to parse.

  * **fault\_tolerant** \(_bool_\)

Returns:     

A tuple containing the parsed object or None and an error message or None.

Return type:     

_Tuple_\[_Dict_ | None, str | None\]

Exceptions:     

json.JSONDecodeError: If the input is not a valid JSON string.

__On this page