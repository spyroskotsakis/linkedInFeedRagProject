# parse_tool_calls — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_calls.html
**Word Count:** 62
**Links Count:** 126
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# parse\_tool\_calls\#

langchain\_core.output\_parsers.openai\_tools.parse\_tool\_calls\(

    _raw\_tool\_calls : list\[dict\]_,     _\*_ ,     _partial : bool = False_,     _strict : bool = False_,     _return\_id : bool = True_, \) → list\[dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/openai_tools.html#parse_tool_calls)\#     

Parse a list of tool calls.

Parameters:     

  * **raw\_tool\_calls** \(_list_ _\[__dict_ _\]_\) – The raw tool calls to parse.

  * **partial** \(_bool_\) – Whether to parse partial JSON. Default is False.

  * **strict** \(_bool_\) – Whether to allow non-JSON-compliant strings. Default is False.

  * **return\_id** \(_bool_\) – Whether to return the tool call id. Default is True.

Returns:     

The parsed tool calls.

Raises:     

[**OutputParserException**](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.OutputParserException.html#langchain_core.exceptions.OutputParserException "langchain_core.exceptions.OutputParserException") – If any of the tool calls are not valid JSON.

Return type:     

list\[dict\[str, _Any_\]\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)