# create_index — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.nanopq.create_index.html
**Word Count:** 30
**Links Count:** 174
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# create\_index\#

langchain\_community.retrievers.nanopq.create\_index\(

    _contexts : List\[str\]_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_, \) → ndarray[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/retrievers/nanopq.html#create_index)\#     

Create an index of embeddings for a list of contexts.

Parameters:     

  * **contexts** \(_List_ _\[__str_ _\]_\) – List of contexts to embed.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – Embeddings model to use.

Returns:     

Index of embeddings.

Return type:     

_ndarray_

__On this page