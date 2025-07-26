# langchain_community.tools.nasa.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/nasa/tool.html
**Word Count:** 36
**Links Count:** 13
**Scraped:** 2025-07-21 09:13:00
**Status:** completed

---

# Source code for langchain\_community.tools.nasa.tool               """     This tool allows agents to interact with the NASA API, specifically     the the NASA Image & Video Library and Exoplanet     """          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool     from pydantic import Field          from langchain_community.utilities.nasa import NasaAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nasa.tool.NasaAction.html#langchain_community.tools.nasa.tool.NasaAction)     class NasaAction(BaseTool):         """Tool that queries the Atlassian Jira API."""              api_wrapper: NasaAPIWrapper = Field(default_factory=NasaAPIWrapper)         mode: str         name: str = ""         description: str = ""              def _run(             self,             instructions: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the NASA API to run an operation."""             return self.api_wrapper.run(self.mode, instructions)