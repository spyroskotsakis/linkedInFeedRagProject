# langchain_community.tools.wolfram_alpha.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/wolfram_alpha/tool.html
**Word Count:** 47
**Links Count:** 13
**Scraped:** 2025-07-21 09:14:31
**Status:** completed

---

# Source code for langchain\_community.tools.wolfram\_alpha.tool               """Tool for the Wolfram Alpha API."""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.wolfram_alpha.tool.WolframAlphaQueryRun.html#langchain_community.tools.wolfram_alpha.tool.WolframAlphaQueryRun)     class WolframAlphaQueryRun(BaseTool):         """Tool that queries using the Wolfram Alpha SDK."""              name: str = "wolfram_alpha"         description: str = (             "A wrapper around Wolfram Alpha. "             "Useful for when you need to answer questions about Math, "             "Science, Technology, Culture, Society and Everyday Life. "             "Input should be a search query."         )         api_wrapper: WolframAlphaAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the WolframAlpha tool."""             return self.api_wrapper.run(query)