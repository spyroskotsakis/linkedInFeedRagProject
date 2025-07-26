# maximal_marginal_relevance — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/milvus/vectorstores/langchain_milvus.vectorstores.milvus.maximal_marginal_relevance.html
**Word Count:** 40
**Links Count:** 75
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# maximal\_marginal\_relevance\#

langchain\_milvus.vectorstores.milvus.maximal\_marginal\_relevance\(

    _query\_embedding : ndarray_,     _embedding\_list : list_,     _lambda\_mult : float = 0.5_,     _k : int = 4_, \) → List\[int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/vectorstores/milvus.html#maximal_marginal_relevance)\#     

Calculate maximal marginal relevance.

Parameters:     

  * **query\_embedding** \(_ndarray_\) – The query embedding.

  * **embedding\_list** \(_list_\) – The list of embeddings.

  * **lambda\_mult** \(_float_\) – The lambda multiplier. Defaults to 0.5.

  * **k** \(_int_\) – The number of results to return. Defaults to 4.

Returns:     

The list of indices.

Return type:     

List\[int\]

__On this page