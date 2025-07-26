# parse_and_check_json_markdown — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.json.parse_and_check_json_markdown.html
**Word Count:** 55
**Links Count:** 167
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# parse\_and\_check\_json\_markdown\#

langchain\_core.utils.json.parse\_and\_check\_json\_markdown\(

    _text : str_,     _expected\_keys : list\[str\]_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/json.html#parse_and_check_json_markdown)\#     

Parse and check a JSON string from a Markdown string.

Checks that it contains the expected keys.

Parameters:     

  * **text** \(_str_\) – The Markdown string.

  * **expected\_keys** \(_list_ _\[__str_ _\]_\) – The expected keys in the JSON string.

Returns:     

The parsed JSON object as a Python dictionary.

Raises:     

[**OutputParserException**](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.OutputParserException.html#langchain_core.exceptions.OutputParserException "langchain_core.exceptions.OutputParserException") – If the JSON string is invalid or does not contain the expected keys.

Return type:     

dict

__On this page