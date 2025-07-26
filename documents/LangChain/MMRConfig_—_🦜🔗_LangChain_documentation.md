# MMRConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.MMRConfig.html
**Word Count:** 98
**Links Count:** 319
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# MMRConfig\#

_class _langchain\_community.vectorstores.vectara.MMRConfig\(

    _is\_enabled : bool = False_,     _mmr\_k : int = 50_,     _diversity\_bias : float = 0.3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#MMRConfig)\#     

Configuration for Maximal Marginal Relevance \(MMR\) search.     

This will soon be deprated in favor of RerankConfig.

is\_enabled: True if MMR is enabled, False otherwise mmr\_k: number of results to fetch for MMR, defaults to 50 diversity\_bias: number between 0 and 1 that determines the degree

> of diversity among the results with 0 corresponding to minimum diversity and 1 to maximum diversity. Defaults to 0.3. Note: diversity\_bias is equivalent 1-lambda\_mult where lambda\_mult is the value often used in max\_marginal\_relevance\_search\(\) We chose to use that since we believe it’s more intuitive to the user.

Attributes

`diversity_bias` |    ---|---   `is_enabled` |    `mmr_k` |       Methods

`__init__`\(\[is\_enabled, mmr\_k, diversity\_bias\]\) |    ---|---      Parameters:     

  * **is\_enabled** \(_bool_\)

  * **mmr\_k** \(_int_\)

  * **diversity\_bias** \(_float_\)

\_\_init\_\_\(

    _is\_enabled : bool = False_,     _mmr\_k : int = 50_,     _diversity\_bias : float = 0.3_, \) → None\#     

Parameters:     

  * **is\_enabled** \(_bool_\)

  * **mmr\_k** \(_int_\)

  * **diversity\_bias** \(_float_\)

Return type:     

None

__On this page