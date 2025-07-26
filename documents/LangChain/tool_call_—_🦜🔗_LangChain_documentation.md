# tool_call — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.tool_call.html
**Word Count:** 35
**Links Count:** 151
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# tool\_call\#

langchain\_core.messages.tool.tool\_call\(

    _\*_ ,     _name : str_,     _args : dict\[str, Any\]_,     _id : str | None_, \) → [ToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall "langchain_core.messages.tool.ToolCall")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#tool_call)\#     

Create a tool call.

Parameters:     

  * **name** \(_str_\) – The name of the tool to be called.

  * **args** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The arguments to the tool call.

  * **id** \(_str_ _|__None_\) – An identifier associated with the tool call.

Return type:     

[_ToolCall_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall "langchain_core.messages.tool.ToolCall")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)