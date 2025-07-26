# langchain_community.tools.merriam_webster.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/merriam_webster/tool.html
**Word Count:** 41
**Links Count:** 13
**Scraped:** 2025-07-21 09:15:18
**Status:** completed

---

# Source code for langchain\_community.tools.merriam\_webster.tool               """Tool for the Merriam-Webster API."""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.merriam_webster import MerriamWebsterAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.merriam_webster.tool.MerriamWebsterQueryRun.html#langchain_community.tools.merriam_webster.tool.MerriamWebsterQueryRun)     class MerriamWebsterQueryRun(BaseTool):         """Tool that searches the Merriam-Webster API."""              name: str = "merriam_webster"         description: str = (             "A wrapper around Merriam-Webster. "             "Useful for when you need to get the definition of a word."             "Input should be the word you want the definition of."         )         api_wrapper: MerriamWebsterAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the Merriam-Webster tool."""             return self.api_wrapper.run(query)