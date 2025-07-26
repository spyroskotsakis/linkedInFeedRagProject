# maximal_marginal_relevance — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.utils.maximal_marginal_relevance.html
**Word Count:** 52
**Links Count:** 102
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# maximal\_marginal\_relevance\#

langchain\_core.vectorstores.utils.maximal\_marginal\_relevance\(

    _query\_embedding : np.ndarray_,     _embedding\_list : list_,     _lambda\_mult : float = 0.5_,     _k : int = 4_, \) → list\[int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/vectorstores/utils.html#maximal_marginal_relevance)\#     

Calculate maximal marginal relevance.

Parameters:     

  * **query\_embedding** \(_np.ndarray_\) – The query embedding.

  * **embedding\_list** \(_list_\) – A list of embeddings.

  * **lambda\_mult** \(_float_\) – The lambda parameter for MMR. Default is 0.5.

  * **k** \(_int_\) – The number of embeddings to return. Default is 4.

Returns:     

A list of indices of the embeddings to return.

Raises:     

**ImportError** – If numpy is not installed.

Return type:     

list\[int\]

__On this page