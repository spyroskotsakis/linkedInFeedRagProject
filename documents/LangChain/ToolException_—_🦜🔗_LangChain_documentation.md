# ToolException — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.ToolException.html
**Word Count:** 50
**Links Count:** 115
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# ToolException\#

_class _langchain\_core.tools.base.ToolException[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/base.html#ToolException)\#     

Exception thrown when a tool execution error occurs.

This exception allows tools to signal errors without stopping the agent. The error is handled according to the tool’s handle\_tool\_error setting, and the result is returned as an observation to the agent.

Examples using ToolException

  * [How to create tools](https://python.langchain.com/docs/how_to/custom_tools/)

__On this page