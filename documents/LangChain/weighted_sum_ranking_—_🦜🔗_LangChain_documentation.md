# weighted_sum_ranking — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.weighted_sum_ranking.html
**Word Count:** 87
**Links Count:** 90
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# weighted\_sum\_ranking\#

langchain\_postgres.v2.hybrid\_search\_config.weighted\_sum\_ranking\(

    _primary\_search\_results : Sequence\[RowMapping\]_,     _secondary\_search\_results : Sequence\[RowMapping\]_,     _primary\_results\_weight : float = 0.5_,     _secondary\_results\_weight : float = 0.5_,     _fetch\_top\_k : int = 4_, \) → Sequence\[dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/hybrid_search_config.html#weighted_sum_ranking)\#     

Ranks documents using a weighted sum of scores from two sources.

Parameters:     

  * **primary\_search\_results** \(_Sequence_ _\[__RowMapping_ _\]_\) – A list of \(document, distance\) tuples from the primary search.

  * **secondary\_search\_results** \(_Sequence_ _\[__RowMapping_ _\]_\) – A list of \(document, distance\) tuples from the secondary search.

  * **primary\_results\_weight** \(_float_\) – The weight for the primary source’s scores. Defaults to 0.5.

  * **secondary\_results\_weight** \(_float_\) – The weight for the secondary source’s scores. Defaults to 0.5.

  * **fetch\_top\_k** \(_int_\) – The number of documents to fetch after merging the results. Defaults to 4.

Returns:     

A list of \(document, distance\) tuples, sorted by weighted\_score in descending order.

Return type:     

_Sequence_\[dict\[str, _Any_\]\]

__On this page