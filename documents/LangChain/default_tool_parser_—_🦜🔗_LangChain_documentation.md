# default_tool_parser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.default_tool_parser.html
**Word Count:** 12
**Links Count:** 153
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# default\_tool\_parser\#

langchain\_core.messages.tool.default\_tool\_parser\(

    _raw\_tool\_calls : list\[dict\]_, \) → tuple\[list\[[ToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall "langchain_core.messages.tool.ToolCall")\], list\[[InvalidToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/tool.html#default_tool_parser)\#     

Best-effort parsing of tools.

Parameters:     

**raw\_tool\_calls** \(_list_ _\[__dict_ _\]_\)

Return type:     

tuple\[list\[[_ToolCall_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall "langchain_core.messages.tool.ToolCall")\], list\[[_InvalidToolCall_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")\]\]

__On this page