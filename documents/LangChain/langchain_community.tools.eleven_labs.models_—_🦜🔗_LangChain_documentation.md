# langchain_community.tools.eleven_labs.models — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/eleven_labs/models.html
**Word Count:** 10
**Links Count:** 13
**Scraped:** 2025-07-21 09:13:00
**Status:** completed

---

# Source code for langchain\_community.tools.eleven\_labs.models               from enum import Enum                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.eleven_labs.models.ElevenLabsModel.html#langchain_community.tools.eleven_labs.models.ElevenLabsModel)     class ElevenLabsModel(str, Enum):         """Models available for Eleven Labs Text2Speech."""              MULTI_LINGUAL = "eleven_multilingual_v2"         MULTI_LINGUAL_FLASH = "eleven_flash_v2_5"         MONO_LINGUAL = "eleven_flash_v2"