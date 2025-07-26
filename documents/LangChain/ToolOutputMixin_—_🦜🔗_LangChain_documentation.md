# ToolOutputMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolOutputMixin.html
**Word Count:** 48
**Links Count:** 149
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# ToolOutputMixin\#

_class _langchain\_core.messages.tool.ToolOutputMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#ToolOutputMixin)\#     

Mixin for objects that tools can return directly.

If a custom BaseTool is invoked with a ToolCall and the output of custom code is not an instance of ToolOutputMixin, the output will automatically be coerced to a string and wrapped in a ToolMessage.

__On this page