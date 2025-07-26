# langchain_community.tools.stackexchange.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/stackexchange/tool.html
**Word Count:** 40
**Links Count:** 13
**Scraped:** 2025-07-21 09:16:48
**Status:** completed

---

# Source code for langchain\_community.tools.stackexchange.tool               """Tool for the Wikipedia API."""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.stackexchange import StackExchangeAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.stackexchange.tool.StackExchangeTool.html#langchain_community.tools.stackexchange.tool.StackExchangeTool)     class StackExchangeTool(BaseTool):         """Tool that uses StackExchange"""              name: str = "stack_exchange"         description: str = (             "A wrapper around StackExchange. "             "Useful for when you need to answer specific programming questions"             "code excerpts, code examples and solutions"             "Input should be a fully formed question."         )         api_wrapper: StackExchangeAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the Stack Exchange tool."""             return self.api_wrapper.run(query)