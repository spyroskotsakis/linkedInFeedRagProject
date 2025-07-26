# reciprocal_rank_fusion — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.reciprocal_rank_fusion.html
**Word Count:** 74
**Links Count:** 90
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# reciprocal\_rank\_fusion\#

langchain\_postgres.v2.hybrid\_search\_config.reciprocal\_rank\_fusion\(

    _primary\_search\_results : Sequence\[RowMapping\]_,     _secondary\_search\_results : Sequence\[RowMapping\]_,     _rrf\_k : float = 60_,     _fetch\_top\_k : int = 4_, \) → Sequence\[dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/hybrid_search_config.html#reciprocal_rank_fusion)\#     

Ranks documents using Reciprocal Rank Fusion \(RRF\) of scores from two sources.

Parameters:     

  * **primary\_search\_results** \(_Sequence_ _\[__RowMapping_ _\]_\) – A list of \(document, distance\) tuples from the primary search.

  * **secondary\_search\_results** \(_Sequence_ _\[__RowMapping_ _\]_\) – A list of \(document, distance\) tuples from the secondary search.

  * **rrf\_k** \(_float_\) – The RRF parameter k. Defaults to 60.

  * **fetch\_top\_k** \(_int_\) – The number of documents to fetch after merging the results. Defaults to 4.

Returns:     

A list of \(document\_id, rrf\_score\) tuples, sorted by rrf\_score in descending order.

Return type:     

_Sequence_\[dict\[str, _Any_\]\]

__On this page