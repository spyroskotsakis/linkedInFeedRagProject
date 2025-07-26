# make_invalid_tool_call — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.openai_tools.make_invalid_tool_call.html
**Word Count:** 30
**Links Count:** 127
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# make\_invalid\_tool\_call\#

langchain\_core.output\_parsers.openai\_tools.make\_invalid\_tool\_call\(

    _raw\_tool\_call : dict\[str, Any\]_,     _error\_msg : str | None_, \) → [InvalidToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/openai_tools.html#make_invalid_tool_call)\#     

Create an InvalidToolCall from a raw tool call.

Parameters:     

  * **raw\_tool\_call** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The raw tool call.

  * **error\_msg** \(_str_ _|__None_\) – The error message.

Returns:     

An InvalidToolCall instance with the error message.

Return type:     

[_InvalidToolCall_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")

__On this page