# langchain_community.tools.connery.models — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/models.html
**Word Count:** 14
**Links Count:** 15
**Scraped:** 2025-07-21 09:12:16
**Status:** completed

---

# Source code for langchain\_community.tools.connery.models               from typing import Any, List, Optional          from pydantic import BaseModel                              [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Validation.html#langchain_community.tools.connery.models.Validation)     class Validation(BaseModel):         """Connery Action parameter validation model."""              required: Optional[bool] = None                                             [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Parameter.html#langchain_community.tools.connery.models.Parameter)     class Parameter(BaseModel):         """Connery Action parameter model."""              key: str         title: str         description: Optional[str] = None         type: Any         validation: Optional[Validation] = None                                             [[docs]](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.models.Action.html#langchain_community.tools.connery.models.Action)     class Action(BaseModel):         """Connery Action model."""              id: str         key: str         title: str         description: Optional[str] = None         type: str         inputParameters: List[Parameter]         outputParameters: List[Parameter]         pluginId: str