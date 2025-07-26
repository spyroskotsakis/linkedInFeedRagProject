# langchain.chains.query_constructor.schema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/chains/query_constructor/schema.html
**Word Count:** 10
**Links Count:** 13
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# Source code for langchain.chains.query\_constructor.schema               from pydantic import BaseModel, ConfigDict                              [[docs]](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.query_constructor.schema.AttributeInfo.html#langchain.chains.query_constructor.schema.AttributeInfo)     class AttributeInfo(BaseModel):         """Information about a data source attribute."""              name: str         description: str         type: str              model_config = ConfigDict(             arbitrary_types_allowed=True,             frozen=True,         )