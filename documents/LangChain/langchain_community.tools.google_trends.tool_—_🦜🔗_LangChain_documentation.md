# langchain_community.tools.google_trends.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_trends/tool.html
**Word Count:** 41
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:00
**Status:** completed

---

# Source code for langchain\_community.tools.google\_trends.tool               """Tool for the Google Trends"""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_trends.tool.GoogleTrendsQueryRun.html#langchain_community.tools.google_trends.tool.GoogleTrendsQueryRun)     class GoogleTrendsQueryRun(BaseTool):         """Tool that queries the Google trends API."""              name: str = "google_trends"         description: str = (             "A wrapper around Google Trends Search. "             "Useful for when you need to get information about"             "google search trends from Google Trends"             "Input should be a search query."         )         api_wrapper: GoogleTrendsAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the tool."""             return self.api_wrapper.run(query)