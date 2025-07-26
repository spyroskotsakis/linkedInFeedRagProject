# invalid_tool_call — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.invalid_tool_call.html
**Word Count:** 45
**Links Count:** 151
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# invalid\_tool\_call\#

langchain\_core.messages.tool.invalid\_tool\_call\(

    _\*_ ,     _name : str | None = None_,     _args : str | None = None_,     _id : str | None = None_,     _error : str | None = None_, \) → [InvalidToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#invalid_tool_call)\#     

Create an invalid tool call.

Parameters:     

  * **name** \(_str_ _|__None_\) – The name of the tool to be called.

  * **args** \(_str_ _|__None_\) – The arguments to the tool call.

  * **id** \(_str_ _|__None_\) – An identifier associated with the tool call.

  * **error** \(_str_ _|__None_\) – An error message associated with the tool call.

Return type:     

[_InvalidToolCall_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)