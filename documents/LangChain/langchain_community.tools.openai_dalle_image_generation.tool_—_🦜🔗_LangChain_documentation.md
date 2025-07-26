# langchain_community.tools.openai_dalle_image_generation.tool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/openai_dalle_image_generation/tool.html
**Word Count:** 58
**Links Count:** 13
**Scraped:** 2025-07-21 09:14:06
**Status:** completed

---

# Source code for langchain\_community.tools.openai\_dalle\_image\_generation.tool               """Tool for the OpenAI DALLE V1 Image Generation SDK."""          from typing import Optional          from langchain_core.callbacks import CallbackManagerForToolRun     from langchain_core.tools import BaseTool          from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.openai_dalle_image_generation.tool.OpenAIDALLEImageGenerationTool.html#langchain_community.tools.openai_dalle_image_generation.tool.OpenAIDALLEImageGenerationTool)     class OpenAIDALLEImageGenerationTool(BaseTool):         """Tool that generates an image using OpenAI DALLE."""              name: str = "openai_dalle"         description: str = (             "A wrapper around OpenAI DALLE Image Generation. "             "Useful for when you need to generate an image of"             "people, places, paintings, animals, or other subjects. "             "Input should be a text prompt to generate an image."         )         api_wrapper: DallEAPIWrapper              def _run(             self,             query: str,             run_manager: Optional[CallbackManagerForToolRun] = None,         ) -> str:             """Use the OpenAI DALLE Image Generation tool."""             return self.api_wrapper.run(query)