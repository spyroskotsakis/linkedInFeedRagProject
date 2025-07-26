# langchain_google_vertexai.model_garden_maas.mistral — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_google_vertexai/model_garden_maas/mistral.html
**Word Count:** 14
**Links Count:** 14
**Scraped:** 2025-07-21 09:20:15
**Status:** completed

---

# Source code for langchain\_google\_vertexai.model\_garden\_maas.mistral               from typing import Any, Optional          from langchain_core.callbacks import (         CallbackManagerForLLMRun,     )     from langchain_mistralai import (  # type: ignore[unused-ignore, import-not-found]         chat_models,     )          from langchain_google_vertexai.model_garden_maas._base import (         _BaseVertexMaasModelGarden,         acompletion_with_retry,         completion_with_retry,     )          chat_models.acompletion_with_retry = acompletion_with_retry  # type: ignore[unused-ignore, assignment]                              [[docs]](https://python.langchain.com/api_reference/google_vertexai/model_garden_maas/langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral.html#langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral)     class VertexModelGardenMistral(_BaseVertexMaasModelGarden, chat_models.ChatMistralAI):  # type: ignore[unused-ignore, misc]                    [[docs]](https://python.langchain.com/api_reference/google_vertexai/model_garden_maas/langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral.html#langchain_google_vertexai.model_garden_maas.mistral.VertexModelGardenMistral.completion_with_retry)         def completion_with_retry(             self, run_manager: Optional[CallbackManagerForLLMRun] = None, **kwargs: Any         ) -> Any:             return completion_with_retry(self, **kwargs)