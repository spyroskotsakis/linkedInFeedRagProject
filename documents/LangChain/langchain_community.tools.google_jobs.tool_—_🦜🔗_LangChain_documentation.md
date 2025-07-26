# langchain_community.tools.google_jobs.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_jobs/tool.html
**Word Count:** 41
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:23
**Status:** completed

---

# Source code for langchain\_community.tools.google\_jobs.tool               """Tool for the Google Trends"""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.google_jobs import GoogleJobsAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_jobs.tool.GoogleJobsQueryRun.html#langchain_community.tools.google_jobs.tool.GoogleJobsQueryRun)     class GoogleJobsQueryRun(BaseTool):         """Tool that queries the Google Jobs API."""              name: str = "google_jobs"         description: str = (             "A wrapper around Google Jobs Search. "             "Useful for when you need to get information about"             "google search Jobs from Google Jobs"             "Input should be a search query."         )         api_wrapper: GoogleJobsAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the tool."""             return self.api_wrapper.run(query)