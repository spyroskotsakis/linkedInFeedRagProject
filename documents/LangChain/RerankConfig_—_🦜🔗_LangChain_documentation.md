# RerankConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.RerankConfig.html
**Word Count:** 103
**Links Count:** 321
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# RerankConfig\#

_class _langchain\_community.vectorstores.vectara.RerankConfig\(

    _reranker : str = 'none'_,     _rerank\_k : int = 50_,     _mmr\_diversity\_bias : float = 0.3_,     _user\_function : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#RerankConfig)\#     

Configuration for Reranker.

reranker: “mmr”, “rerank\_multilingual\_v1”, “udf” or “none” rerank\_k: number of results to fetch before reranking, defaults to 50 mmr\_diversity\_bias: for MMR only - a number between 0 and 1 that determines

> the degree of diversity among the results with 0 corresponding to minimum diversity and 1 to maximum diversity. Defaults to 0.3. Note: mmr\_diversity\_bias is equivalent 1-lambda\_mult where lambda\_mult is the value often used in max\_marginal\_relevance\_search\(\) We chose to use that since we believe it’s more intuitive to the user.

user\_function: for UDF only - the user function to use for reranking.

Attributes

`mmr_diversity_bias` |    ---|---   `rerank_k` |    `reranker` |    `user_function` |       Methods

`__init__`\(\[reranker, rerank\_k, ...\]\) |    ---|---      Parameters:     

  * **reranker** \(_str_\)

  * **rerank\_k** \(_int_\)

  * **mmr\_diversity\_bias** \(_float_\)

  * **user\_function** \(_str_\)

\_\_init\_\_\(

    _reranker : str = 'none'_,     _rerank\_k : int = 50_,     _mmr\_diversity\_bias : float = 0.3_,     _user\_function : str = ''_, \) → None\#     

Parameters:     

  * **reranker** \(_str_\)

  * **rerank\_k** \(_int_\)

  * **mmr\_diversity\_bias** \(_float_\)

  * **user\_function** \(_str_\)

Return type:     

None

Examples using RerankConfig

  * [Vectara](https://python.langchain.com/docs/integrations/vectorstores/vectara/)

  * [Vectara Chat](https://python.langchain.com/docs/integrations/providers/vectara/vectara_chat/)

__On this page