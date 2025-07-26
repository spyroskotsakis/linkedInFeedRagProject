# langchain_community.llms.openllm — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/llms/openllm.html
**Word Count:** 32
**Links Count:** 13
**Scraped:** 2025-07-21 09:18:00
**Status:** completed

---

# Source code for langchain\_community.llms.openllm               from __future__ import annotations          from typing import Any, Dict          from langchain_community.llms.openai import BaseOpenAI     from langchain_community.utils.openai import is_openai_v1                              [[docs]](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openllm.OpenLLM.html#langchain_community.llms.openllm.OpenLLM)     class OpenLLM(BaseOpenAI):         """OpenAI's compatible API client for OpenLLM server              .. versionchanged:: 0.2.11                 Changed in 0.2.11 to support OpenLLM 0.6. Now behaves similar to OpenAI wrapper.         """              @classmethod         def is_lc_serializable(cls) -> bool:             return False              @property         def _invocation_params(self) -> Dict[str, Any]:             """Get the parameters used to invoke the model."""                  params: Dict[str, Any] = {                 "model": self.model_name,                 **self._default_params,                 "logit_bias": None,             }             if not is_openai_v1():                 params.update(                     {                         "api_key": self.openai_api_key,                         "api_base": self.openai_api_base,                     }                 )                  return params              @property         def _llm_type(self) -> str:             return "openllm"