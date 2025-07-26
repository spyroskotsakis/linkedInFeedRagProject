# parse_tool_call — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.parse_tool_call.html
**Word Count:** 61
**Links Count:** 126
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# parse\_tool\_call\#

langchain\_core.output\_parsers.openai\_tools.parse\_tool\_call\(

    _raw\_tool\_call : dict\[str, Any\]_,     _\*_ ,     _partial : bool = False_,     _strict : bool = False_,     _return\_id : bool = True_, \) → dict\[str, Any\] | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/openai_tools.html#parse_tool_call)\#     

Parse a single tool call.

Parameters:     

  * **raw\_tool\_call** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The raw tool call to parse.

  * **partial** \(_bool_\) – Whether to parse partial JSON. Default is False.

  * **strict** \(_bool_\) – Whether to allow non-JSON-compliant strings. Default is False.

  * **return\_id** \(_bool_\) – Whether to return the tool call id. Default is True.

Returns:     

The parsed tool call.

Raises:     

[**OutputParserException**](https://python.langchain.com/api_reference/core/exceptions/langchain_core.exceptions.OutputParserException.html#langchain_core.exceptions.OutputParserException "langchain_core.exceptions.OutputParserException") – If the tool call is not valid JSON.

Return type:     

dict\[str, _Any_\] | None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)