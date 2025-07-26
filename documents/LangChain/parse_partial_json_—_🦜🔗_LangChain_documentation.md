# parse_partial_json — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.json.parse_partial_json.html
**Word Count:** 39
**Links Count:** 166
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# parse\_partial\_json\#

langchain\_core.utils.json.parse\_partial\_json\(

    _s : str_,     _\*_ ,     _strict : bool = False_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/json.html#parse_partial_json)\#     

Parse a JSON string that may be missing closing braces.

Parameters:     

  * **s** \(_str_\) – The JSON string to parse.

  * **strict** \(_bool_\) – Whether to use strict parsing. Defaults to False.

Returns:     

The parsed JSON object as a Python dictionary.

Return type:     

_Any_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)