# MmrHelper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.mmr_helper.MmrHelper.html
**Word Count:** 142
**Links Count:** 133
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# MmrHelper\#

_class _langchain\_community.graph\_vectorstores.mmr\_helper.MmrHelper\(

    _k : int_,     _query\_embedding : list\[float\]_,     _lambda\_mult : float = 0.5_,     _score\_threshold : float = -inf_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/mmr_helper.html#MmrHelper)\#     

Helper for executing an MMR traversal query.

Parameters:     

  * **query\_embedding** \(_list_ _\[__float_ _\]_\) – The embedding of the query to use for scoring.

  * **lambda\_mult** \(_float_\) – Number between 0 and 1 that determines the degree of diversity among the results with 0 corresponding to maximum diversity and 1 to minimum diversity. Defaults to 0.5.

  * **score\_threshold** \(_float_\) – Only documents with a score greater than or equal this threshold will be chosen. Defaults to -infinity.

  * **k** \(_int_\)

Create a new Traversal MMR helper.

Attributes

Methods

`__init__`\(k, query\_embedding\[, lambda\_mult, ...\]\) | Create a new Traversal MMR helper.   ---|---   `add_candidates`\(candidates\) | Add candidates to the consideration set.   `candidate_ids`\(\) | Return the IDs of the candidates.   `pop_best`\(\) | Select and pop the best item being considered.      \_\_init\_\_\(

    _k : int_,     _query\_embedding : list\[float\]_,     _lambda\_mult : float = 0.5_,     _score\_threshold : float = -inf_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/mmr_helper.html#MmrHelper.__init__)\#     

Create a new Traversal MMR helper.

Parameters:     

  * **k** \(_int_\)

  * **query\_embedding** \(_list_ _\[__float_ _\]_\)

  * **lambda\_mult** \(_float_\)

  * **score\_threshold** \(_float_\)

Return type:     

None

add\_candidates\(

    _candidates : dict\[str, list\[float\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/mmr_helper.html#MmrHelper.add_candidates)\#     

Add candidates to the consideration set.

Parameters:     

**candidates** \(_dict_ _\[__str_ _,__list_ _\[__float_ _\]__\]_\)

Return type:     

None

candidate\_ids\(\) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/mmr_helper.html#MmrHelper.candidate_ids)\#     

Return the IDs of the candidates.

Return type:     

_Iterable_\[str\]

pop\_best\(\) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/mmr_helper.html#MmrHelper.pop_best)\#     

Select and pop the best item being considered.

Updates the consideration set based on it.

Returns:     

A tuple containing the ID of the best item.

Return type:     

str | None

__On this page