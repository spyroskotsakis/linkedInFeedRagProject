# langchain_community.llms.openlm — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/llms/openlm.html
**Word Count:** 22
**Links Count:** 14
**Scraped:** 2025-07-21 08:58:43
**Status:** completed

---

# Source code for langchain\_community.llms.openlm               from typing import Any, Dict          from langchain_core.utils import pre_init          from langchain_community.llms.openai import BaseOpenAI                              [[docs]](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openlm.OpenLM.html#langchain_community.llms.openlm.OpenLM)     class OpenLM(BaseOpenAI):         """OpenLM models."""              @classmethod         def is_lc_serializable(cls) -> bool:             return False              @property         def _invocation_params(self) -> Dict[str, Any]:             return {**{"model": self.model_name}, **super()._invocation_params}                         [[docs]](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.openlm.OpenLM.html#langchain_community.llms.openlm.OpenLM.validate_environment)         @pre_init         def validate_environment(cls, values: Dict) -> Dict:             try:                 import openlm                      values["client"] = openlm.Completion             except ImportError:                 raise ImportError(                     "Could not import openlm python package. "                     "Please install it with `pip install openlm`."                 )             if values["streaming"]:                 raise ValueError("Streaming not supported with openlm")             return values