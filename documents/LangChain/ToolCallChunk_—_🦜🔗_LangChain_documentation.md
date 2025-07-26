# ToolCallChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCallChunk.html
**Word Count:** 66
**Links Count:** 159
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# ToolCallChunk\#

_class _langchain\_core.messages.tool.ToolCallChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#ToolCallChunk)\#     

A chunk of a tool call \(e.g., as part of a stream\).

When merging ToolCallChunks \(e.g., via AIMessageChunk.\_\_add\_\_\), all string attributes are concatenated. Chunks are only merged if their values of index are equal and not None.

Example:               left_chunks = [ToolCallChunk(name="foo", args='{"a":', index=0)]     right_chunks = [ToolCallChunk(name=None, args='1}', index=0)]          (         AIMessageChunk(content="", tool_call_chunks=left_chunks)         + AIMessageChunk(content="", tool_call_chunks=right_chunks)     ).tool_call_chunks == [ToolCallChunk(name='foo', args='{"a":1}', index=0)]     

name _: str | None_\#     

The name of the tool to be called.

args _: str | None_\#     

The arguments to the tool call.

id _: str | None_\#     

An identifier associated with the tool call.

index _: int | None_\#     

The index of the tool call in a sequence.

type _: NotRequired\[Literal\['tool\_call\_chunk'\]\]_\#     

__On this page