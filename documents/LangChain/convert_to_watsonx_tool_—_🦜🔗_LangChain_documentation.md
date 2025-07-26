# convert_to_watsonx_tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.convert_to_watsonx_tool.html
**Word Count:** 65
**Links Count:** 82
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# convert\_to\_watsonx\_tool\#

langchain\_ibm.utils.convert\_to\_watsonx\_tool\(_tool : [WatsonxTool](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool")_\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ibm/utils.html#convert_to_watsonx_tool)\#     

Convert WatsonxTool to watsonx tool structure.

Parameters:     

**tool** \([_WatsonxTool_](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool")\) – WatsonxTool from WatsonxToolkit

Return type:     

dict

Example:               from langchain_ibm import WatsonxToolkit          watsonx_toolkit = WatsonxToolkit(         url="https://us-south.ml.cloud.ibm.com",         apikey="*****",     )     weather_tool = watsonx_toolkit.get_tool("Weather")     convert_to_watsonx_tool(weather_tool)          # Return     # {     #     "type": "function",     #     "function": {     #         "name": "Weather",     #         "description": "Find the weather for a city.",     #         "parameters": {     #             "type": "object",     #             "properties": {     #                 "location": {     #                     "title": "location",     #                     "description": "Name of the location",     #                     "type": "string",     #                 },     #                 "country": {     #                     "title": "country",     #                     "description": "Name of the state or country",     #                     "type": "string",     #                 },     #             },     #             "required": ["location"],     #         },     #     },     # }     

__On this page