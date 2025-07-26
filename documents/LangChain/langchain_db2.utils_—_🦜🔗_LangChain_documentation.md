# langchain_db2.utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_db2/utils.html
**Word Count:** 5
**Links Count:** 15
**Scraped:** 2025-07-21 08:58:20
**Status:** completed

---

# Source code for langchain\_db2.utils               from typing import Protocol, runtime_checkable                              [[docs]](https://python.langchain.com/api_reference/db2/utils/langchain_db2.utils.EmbeddingsSchema.html#langchain_db2.utils.EmbeddingsSchema)     @runtime_checkable     class EmbeddingsSchema(Protocol):                    [[docs]](https://python.langchain.com/api_reference/db2/utils/langchain_db2.utils.EmbeddingsSchema.html#langchain_db2.utils.EmbeddingsSchema.embed_documents)         def embed_documents(self, texts: list[str]) -> list[list[float]]: ...                                   [[docs]](https://python.langchain.com/api_reference/db2/utils/langchain_db2.utils.EmbeddingsSchema.html#langchain_db2.utils.EmbeddingsSchema.embed_query)         def embed_query(self, text: str) -> list[float]: ...