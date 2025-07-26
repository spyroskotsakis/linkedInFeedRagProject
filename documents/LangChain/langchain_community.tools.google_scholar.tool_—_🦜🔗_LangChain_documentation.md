# langchain_community.tools.google_scholar.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_scholar/tool.html
**Word Count:** 40
**Links Count:** 13
**Scraped:** 2025-07-21 09:17:16
**Status:** completed

---

# Source code for langchain\_community.tools.google\_scholar.tool               """Tool for the Google Scholar"""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.google_scholar import GoogleScholarAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_scholar.tool.GoogleScholarQueryRun.html#langchain_community.tools.google_scholar.tool.GoogleScholarQueryRun)     class GoogleScholarQueryRun(BaseTool):         """Tool that queries the Google search API."""              name: str = "google_scholar"         description: str = (             "A wrapper around Google Scholar Search. "             "Useful for when you need to get information about"             "research papers from Google Scholar"             "Input should be a search query."         )         api_wrapper: GoogleScholarAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the tool."""             return self.api_wrapper.run(query)