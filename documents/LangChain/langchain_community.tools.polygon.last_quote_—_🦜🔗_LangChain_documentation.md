# langchain_community.tools.polygon.last_quote — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/polygon/last_quote.html
**Word Count:** 57
**Links Count:** 14
**Scraped:** 2025-07-21 09:12:16
**Status:** completed

---

# Source code for langchain\_community.tools.polygon.last\_quote               from typing import Optional, Type          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool     from pydantic import BaseModel          from langchain_community.utilities.polygon import PolygonAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.polygon.last_quote.Inputs.html#langchain_community.tools.polygon.last_quote.Inputs)     class Inputs(BaseModel):         """Inputs for Polygon's Last Quote API"""              query: str                                             [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.polygon.last_quote.PolygonLastQuote.html#langchain_community.tools.polygon.last_quote.PolygonLastQuote)     class PolygonLastQuote(BaseTool):         """Tool that gets the last quote of a ticker from Polygon"""              mode: str = "get_last_quote"         name: str = "polygon_last_quote"         description: str = (             "A wrapper around Polygon's Last Quote API. "             "This tool is useful for fetching the latest price of a stock. "             "Input should be the ticker that you want to query the last price quote for."         )         args_schema: Type[BaseModel] = Inputs              api_wrapper: PolygonAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the Polygon API tool."""             return self.api_wrapper.run(self.mode, ticker=query)