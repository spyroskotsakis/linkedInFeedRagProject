# InvalidToolCall — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html
**Word Count:** 50
**Links Count:** 159
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# InvalidToolCall\#

_class _langchain\_core.messages.tool.InvalidToolCall[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#InvalidToolCall)\#     

Allowance for errors made by LLM.

Here we add an error key to surface errors made during generation \(e.g., invalid JSON arguments.\)

name _: str | None_\#     

The name of the tool to be called.

args _: str | None_\#     

The arguments to the tool call.

id _: str | None_\#     

An identifier associated with the tool call.

error _: str | None_\#     

An error message associated with the tool call.

type _: NotRequired\[Literal\['invalid\_tool\_call'\]\]_\#     

__On this page