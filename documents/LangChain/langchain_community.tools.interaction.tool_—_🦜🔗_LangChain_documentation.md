# langchain_community.tools.interaction.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/interaction/tool.html
**Word Count:** 26
**Links Count:** 13
**Scraped:** 2025-07-21 08:58:43
**Status:** completed

---

# Source code for langchain\_community.tools.interaction.tool               """Tools for interacting with the user."""          import warnings     from typing import Any          from langchain_community.tools.human.tool import HumanInputRun                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.interaction.tool.StdInInquireTool.html#langchain_community.tools.interaction.tool.StdInInquireTool)     def StdInInquireTool(*args: Any, **kwargs: Any) -> HumanInputRun:         """Tool for asking the user for input."""         warnings.warn(             "StdInInquireTool will be deprecated in the future. "             "Please use HumanInputRun instead.",             DeprecationWarning,         )         return HumanInputRun(*args, **kwargs)