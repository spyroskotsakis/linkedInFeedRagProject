# tool_call_chunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.tool_call_chunk.html
**Word Count:** 46
**Links Count:** 151
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# tool\_call\_chunk\#

langchain\_core.messages.tool.tool\_call\_chunk\(

    _\*_ ,     _name : str | None = None_,     _args : str | None = None_,     _id : str | None = None_,     _index : int | None = None_, \) → [ToolCallChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCallChunk.html#langchain_core.messages.tool.ToolCallChunk "langchain_core.messages.tool.ToolCallChunk")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#tool_call_chunk)\#     

Create a tool call chunk.

Parameters:     

  * **name** \(_str_ _|__None_\) – The name of the tool to be called.

  * **args** \(_str_ _|__None_\) – The arguments to the tool call.

  * **id** \(_str_ _|__None_\) – An identifier associated with the tool call.

  * **index** \(_int_ _|__None_\) – The index of the tool call in a sequence.

Return type:     

[_ToolCallChunk_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCallChunk.html#langchain_core.messages.tool.ToolCallChunk "langchain_core.messages.tool.ToolCallChunk")

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)