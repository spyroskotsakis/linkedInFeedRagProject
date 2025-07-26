# ToolCall — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html
**Word Count:** 78
**Links Count:** 158
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# ToolCall\#

_class _langchain\_core.messages.tool.ToolCall[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#ToolCall)\#     

Represents a request to call a tool.

Example               {         "name": "foo",         "args": {"a": 1},         "id": "123"     }     

This represents a request to call the tool named “foo” with arguments \{“a”: 1\} and an identifier of “123”.

name _: str_\#     

The name of the tool to be called.

args _: dict\[str, Any\]_\#     

The arguments to the tool call.

id _: str | None_\#     

An identifier associated with the tool call.

An identifier is needed to associate a tool call request with a tool call result in events when multiple concurrent tool calls are made.

type _: NotRequired\[Literal\['tool\_call'\]\]_\#     

Examples using ToolCall

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

__On this page