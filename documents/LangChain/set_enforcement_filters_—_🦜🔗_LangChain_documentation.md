# set_enforcement_filters — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.enforcement_filters.set_enforcement_filters.html
**Word Count:** 16
**Links Count:** 165
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# set\_enforcement\_filters\#

langchain\_community.chains.pebblo\_retrieval.enforcement\_filters.set\_enforcement\_filters\(

    _retriever : [VectorStoreRetriever](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")_,     _auth\_context : [AuthContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") | None_,     _semantic\_context : [SemanticContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.SemanticContext.html#langchain_community.chains.pebblo_retrieval.models.SemanticContext "langchain_community.chains.pebblo_retrieval.models.SemanticContext") | None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/enforcement_filters.html#set_enforcement_filters)\#     

Set identity and semantic enforcement filters in the retriever.

Parameters:     

  * **retriever** \([_VectorStoreRetriever_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStoreRetriever.html#langchain_core.vectorstores.base.VectorStoreRetriever "langchain_core.vectorstores.base.VectorStoreRetriever")\)

  * **auth\_context** \([_AuthContext_](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") _|__None_\)

  * **semantic\_context** \([_SemanticContext_](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.SemanticContext.html#langchain_community.chains.pebblo_retrieval.models.SemanticContext "langchain_community.chains.pebblo_retrieval.models.SemanticContext") _|__None_\)

Return type:     

None

__On this page