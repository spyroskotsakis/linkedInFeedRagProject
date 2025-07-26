# langchain_experimental.fallacy_removal.models — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_experimental/fallacy_removal/models.html
**Word Count:** 12
**Links Count:** 13
**Scraped:** 2025-07-21 09:19:27
**Status:** completed

---

# Source code for langchain\_experimental.fallacy\_removal.models               """Models for the Logical Fallacy Chain"""          from pydantic import BaseModel                              [[docs]](https://python.langchain.com/api_reference/experimental/fallacy_removal/langchain_experimental.fallacy_removal.models.LogicalFallacy.html#langchain_experimental.fallacy_removal.models.LogicalFallacy)     class LogicalFallacy(BaseModel):         """Logical fallacy."""              fallacy_critique_request: str         fallacy_revision_request: str         name: str = "Logical Fallacy"