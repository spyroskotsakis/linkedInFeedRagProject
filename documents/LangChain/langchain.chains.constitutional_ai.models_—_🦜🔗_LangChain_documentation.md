# langchain.chains.constitutional_ai.models — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/chains/constitutional_ai/models.html
**Word Count:** 15
**Links Count:** 13
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# Source code for langchain.chains.constitutional\_ai.models               """Models for the Constitutional AI chain."""          from pydantic import BaseModel                              [[docs]](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.constitutional_ai.models.ConstitutionalPrinciple.html#langchain.chains.constitutional_ai.models.ConstitutionalPrinciple)     class ConstitutionalPrinciple(BaseModel):         """Class for a constitutional principle."""              critique_request: str         revision_request: str         name: str = "Constitutional Principle"