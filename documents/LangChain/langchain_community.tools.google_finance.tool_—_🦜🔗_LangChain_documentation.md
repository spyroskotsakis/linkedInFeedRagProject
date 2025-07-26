# langchain_community.tools.google_finance.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_finance/tool.html
**Word Count:** 41
**Links Count:** 13
**Scraped:** 2025-07-21 09:14:31
**Status:** completed

---

# Source code for langchain\_community.tools.google\_finance.tool               """Tool for the Google Finance"""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.google_finance import GoogleFinanceAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_finance.tool.GoogleFinanceQueryRun.html#langchain_community.tools.google_finance.tool.GoogleFinanceQueryRun)     class GoogleFinanceQueryRun(BaseTool):         """Tool that queries the Google Finance API."""              name: str = "google_finance"         description: str = (             "A wrapper around Google Finance Search. "             "Useful for when you need to get information about"             "google search Finance from Google Finance"             "Input should be a search query."         )         api_wrapper: GoogleFinanceAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the tool."""             return self.api_wrapper.run(query)