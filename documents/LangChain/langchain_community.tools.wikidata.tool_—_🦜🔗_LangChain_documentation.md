# langchain_community.tools.wikidata.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/wikidata/tool.html
**Word Count:** 56
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:43
**Status:** completed

---

# Source code for langchain\_community.tools.wikidata.tool               """Tool for the Wikidata API."""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.wikidata import WikidataAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.wikidata.tool.WikidataQueryRun.html#langchain_community.tools.wikidata.tool.WikidataQueryRun)     class WikidataQueryRun(BaseTool):         """Tool that searches the Wikidata API."""              name: str = "Wikidata"         description: str = (             "A wrapper around Wikidata. "             "Useful for when you need to answer general questions about "             "people, places, companies, facts, historical events, or other subjects. "             "Input should be the exact name of the item you want information about "             "or a Wikidata QID."         )         api_wrapper: WikidataAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the Wikidata tool."""             return self.api_wrapper.run(query)