# langchain_community.agent_toolkits.json.toolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/json/toolkit.html
**Word Count:** 19
**Links Count:** 14
**Scraped:** 2025-07-21 09:13:23
**Status:** completed

---

# Source code for langchain\_community.agent\_toolkits.json.toolkit               from __future__ import annotations          from typing import List          from langchain_core.tools import BaseTool     from langchain_core.tools.base import BaseToolkit          from langchain_community.tools.json.tool import (         JsonGetValueTool,         JsonListKeysTool,         JsonSpec,     )                              [[docs]](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.toolkit.JsonToolkit.html#langchain_community.agent_toolkits.json.toolkit.JsonToolkit)     class JsonToolkit(BaseToolkit):         """Toolkit for interacting with a JSON spec.              Parameters:             spec: The JSON spec.         """              spec: JsonSpec                         [[docs]](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.json.toolkit.JsonToolkit.html#langchain_community.agent_toolkits.json.toolkit.JsonToolkit.get_tools)         def get_tools(self) -> List[BaseTool]:             """Get the tools in the toolkit."""             return [                 JsonListKeysTool(spec=self.spec),                 JsonGetValueTool(spec=self.spec),             ]