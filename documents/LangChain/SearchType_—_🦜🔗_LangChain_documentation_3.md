# SearchType — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.falkordb_vector.SearchType.html
**Word Count:** 72
**Links Count:** 323
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# SearchType\#

_class _langchain\_community.vectorstores.falkordb\_vector.SearchType\(_value_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/falkordb_vector.html#SearchType)\#     

Enumerator for different search strategies in FalkorDB VectorStore.

  * SearchType.VECTOR: This option searches using only

the vector indexes in the vectorstore, relying on the similarity between vector embeddings to return relevant results.

  * SearchType.HYBRID: This option performs a combined search,

querying both the full-text indexes and the vector indexes. It integrates traditional text search with vector-based search for more comprehensive results.

VECTOR _ = 'vector'_\#     

HYBRID _ = 'hybrid'_\#     

Examples using SearchType

  * [Docugami](https://python.langchain.com/docs/integrations/document_loaders/docugami/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [Zep Open Source](https://python.langchain.com/docs/integrations/retrievers/zep_memorystore/)

__On this page