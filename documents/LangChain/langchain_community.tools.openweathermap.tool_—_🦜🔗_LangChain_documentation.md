# langchain_community.tools.openweathermap.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/openweathermap/tool.html
**Word Count:** 39
**Links Count:** 13
**Scraped:** 2025-07-21 09:17:16
**Status:** completed

---

# Source code for langchain\_community.tools.openweathermap.tool               """Tool for the OpenWeatherMap API."""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool     from pydantic import Field          from langchain_community.utilities.openweathermap import OpenWeatherMapAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openweathermap.tool.OpenWeatherMapQueryRun.html#langchain_community.tools.openweathermap.tool.OpenWeatherMapQueryRun)     class OpenWeatherMapQueryRun(BaseTool):         """Tool that queries the OpenWeatherMap API."""              api_wrapper: OpenWeatherMapAPIWrapper = Field(             default_factory=OpenWeatherMapAPIWrapper         )              name: str = "open_weather_map"         description: str = (             "A wrapper around OpenWeatherMap API. "             "Useful for fetching current weather information for a specified location. "             "Input should be a location string (e.g. London,GB)."         )              def _run(             self, location: str, run_manager: Optional[CallbackManagerForToolRun] = None         ) -> str:             """Use the OpenWeatherMap tool."""             return self.api_wrapper.run(location)