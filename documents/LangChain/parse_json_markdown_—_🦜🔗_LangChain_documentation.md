# parse_json_markdown — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.json.parse_json_markdown.html
**Word Count:** 33
**Links Count:** 166
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# parse\_json\_markdown\#

langchain\_core.utils.json.parse\_json\_markdown\(_json\_string: str, \*, parser: ~typing.Callable\[\[str\], ~typing.Any\] = <function parse\_partial\_json>_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/json.html#parse_json_markdown)\#     

Parse a JSON string from a Markdown string.

Parameters:     

  * **json\_string** \(_str_\) – The Markdown string.

  * **parser** \(_Callable_ _\[__\[__str_ _\]__,__Any_ _\]_\) – The parser to use. Defaults to parse\_partial\_json.

Returns:     

The parsed JSON object as a Python dictionary.

Return type:     

dict

__On this page