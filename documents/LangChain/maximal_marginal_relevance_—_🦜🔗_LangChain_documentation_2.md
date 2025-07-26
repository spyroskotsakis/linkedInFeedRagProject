# maximal_marginal_relevance — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.maximal_marginal_relevance.html
**Word Count:** 68
**Links Count:** 71
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# maximal\_marginal\_relevance\#

langchain\_chroma.vectorstores.maximal\_marginal\_relevance\(

    _query\_embedding : ndarray_,     _embedding\_list : list_,     _lambda\_mult : float = 0.5_,     _k : int = 4_, \) → list\[int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#maximal_marginal_relevance)\#     

Calculate maximal marginal relevance.

Parameters:     

  * **query\_embedding** \(_ndarray_\) – Query embedding.

  * **embedding\_list** \(_list_\) – List of embeddings to select from.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **k** \(_int_\) – Number of Documents to return. Defaults to 4.

Returns:     

List of indices of embeddings selected by maximal marginal relevance.

Return type:     

list\[int\]

__On this page