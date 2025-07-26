# InjectedToolCallId — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.InjectedToolCallId.html
**Word Count:** 57
**Links Count:** 118
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# InjectedToolCallId\#

_class _langchain\_core.tools.base.InjectedToolCallId[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/base.html#InjectedToolCallId)\#     

Annotation for injecting the tool call ID.

This annotation is used to mark a tool parameter that should receive the tool call ID at runtime.

Example

\`\`\`python from typing\_extensions import Annotated from langchain\_core.messages import ToolMessage from langchain\_core.tools import tool, InjectedToolCallId

@tool def foo\(

> x: int, tool\_call\_id: Annotated\[str, InjectedToolCallId\]

\) -> ToolMessage:     

“””Return x.””” return ToolMessage\(

> str\(x\), artifact=x, name=”foo”, tool\_call\_id=tool\_call\_id

\)

\`\`\`

__On this page