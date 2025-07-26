# langchain_community.tools.google_lens.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_lens/tool.html
**Word Count:** 43
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:00
**Status:** completed

---

# Source code for langchain\_community.tools.google\_lens.tool               """Tool for the Google Lens"""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.google_lens import GoogleLensAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_lens.tool.GoogleLensQueryRun.html#langchain_community.tools.google_lens.tool.GoogleLensQueryRun)     class GoogleLensQueryRun(BaseTool):         """Tool that queries the Google Lens API."""              name: str = "google_lens"         description: str = (             "A wrapper around Google Lens Search. "             "Useful for when you need to get information related"             "to an image from Google Lens"             "Input should be a url to an image."         )         api_wrapper: GoogleLensAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the tool."""             return self.api_wrapper.run(query)