# VectorStoreInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_toolkits.vectorstore.toolkit.VectorStoreInfo.html
**Word Count:** 42
**Links Count:** 166
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# VectorStoreInfo\#

_class _langchain.agents.agent\_toolkits.vectorstore.toolkit.VectorStoreInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_toolkits/vectorstore/toolkit.html#VectorStoreInfo)\#     

Bases: `BaseModel`

Information about a VectorStore.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _description _: str_ _\[Required\]_\#     

_param _name _: str_ _\[Required\]_\#     

_param _vectorstore _: [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_ _\[Required\]_\#     

__On this page