# VectaraQueryConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.VectaraQueryConfig.html
**Word Count:** 101
**Links Count:** 335
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# VectaraQueryConfig\#

_class _langchain\_community.vectorstores.vectara.VectaraQueryConfig\(

    _k : int = 10_,     _lambda\_val : float = 0.0_,     _filter : str = ''_,     _score\_threshold : float | None = None_,     _n\_sentence\_before : int = 2_,     _n\_sentence\_after : int = 2_,     _n\_sentence\_context : int | None = None_,     _mmr\_config : [MMRConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.MMRConfig.html#langchain_community.vectorstores.vectara.MMRConfig "langchain_community.vectorstores.vectara.MMRConfig") | None = None_,     _summary\_config : [SummaryConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.SummaryConfig.html#langchain_community.vectorstores.vectara.SummaryConfig "langchain_community.vectorstores.vectara.SummaryConfig") | None = None_,     _rerank\_config : [RerankConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.RerankConfig.html#langchain_community.vectorstores.vectara.RerankConfig "langchain_community.vectorstores.vectara.RerankConfig") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#VectaraQueryConfig)\#     

Configuration for Vectara query.

k: Number of Documents to return. Defaults to 10. lambda\_val: lexical match parameter for hybrid search. filter Dictionary of argument\(s\) to filter on metadata. For example a

> filter can be “doc.rating > 3.0 and part.lang = ‘deu’”\} see <https://docs.vectara.com/docs/search-apis/sql/filter-overview> for more details.

score\_threshold: minimal score threshold for the result.     

If defined, results with score less than this value will be filtered out.

n\_sentence\_before: number of sentences before the matching segment     

to add, defaults to 2

n\_sentence\_after: number of sentences before the matching segment     

to add, defaults to 2

rerank\_config: RerankConfig configuration dataclass summary\_config: SummaryConfig configuration dataclass

Attributes

`filter` |    ---|---   `k` |    `lambda_val` |    `n_sentence_after` |    `n_sentence_before` |    `score_threshold` |       Methods

`__init__`\(\[k, lambda\_val, filter, ...\]\) |    ---|---      Parameters:     

  * **k** \(_int_\)

  * **lambda\_val** \(_float_\)

  * **filter** \(_str_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **n\_sentence\_before** \(_int_\)

  * **n\_sentence\_after** \(_int_\)

  * **n\_sentence\_context** \(_Optional_ _\[__int_ _\]_\)

  * **mmr\_config** \(_Optional_ _\[_[_MMRConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.MMRConfig.html#langchain_community.vectorstores.vectara.MMRConfig "langchain_community.vectorstores.vectara.MMRConfig") _\]_\)

  * **summary\_config** \([_SummaryConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.SummaryConfig.html#langchain_community.vectorstores.vectara.SummaryConfig "langchain_community.vectorstores.vectara.SummaryConfig")\)

  * **rerank\_config** \([_RerankConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.RerankConfig.html#langchain_community.vectorstores.vectara.RerankConfig "langchain_community.vectorstores.vectara.RerankConfig")\)

\_\_init\_\_\(

    _k : int = 10_,     _lambda\_val : float = 0.0_,     _filter : str = ''_,     _score\_threshold : float | None = None_,     _n\_sentence\_before : int = 2_,     _n\_sentence\_after : int = 2_,     _n\_sentence\_context : int | None = None_,     _mmr\_config : [MMRConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.MMRConfig.html#langchain_community.vectorstores.vectara.MMRConfig "langchain_community.vectorstores.vectara.MMRConfig") | None = None_,     _summary\_config : [SummaryConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.SummaryConfig.html#langchain_community.vectorstores.vectara.SummaryConfig "langchain_community.vectorstores.vectara.SummaryConfig") | None = None_,     _rerank\_config : [RerankConfig](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.RerankConfig.html#langchain_community.vectorstores.vectara.RerankConfig "langchain_community.vectorstores.vectara.RerankConfig") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/vectara.html#VectaraQueryConfig.__init__)\#     

Parameters:     

  * **k** \(_int_\)

  * **lambda\_val** \(_float_\)

  * **filter** \(_str_\)

  * **score\_threshold** \(_float_ _|__None_\)

  * **n\_sentence\_before** \(_int_\)

  * **n\_sentence\_after** \(_int_\)

  * **n\_sentence\_context** \(_int_ _|__None_\)

  * **mmr\_config** \([_MMRConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.MMRConfig.html#langchain_community.vectorstores.vectara.MMRConfig "langchain_community.vectorstores.vectara.MMRConfig") _|__None_\)

  * **summary\_config** \([_SummaryConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.SummaryConfig.html#langchain_community.vectorstores.vectara.SummaryConfig "langchain_community.vectorstores.vectara.SummaryConfig") _|__None_\)

  * **rerank\_config** \([_RerankConfig_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.vectara.RerankConfig.html#langchain_community.vectorstores.vectara.RerankConfig "langchain_community.vectorstores.vectara.RerankConfig") _|__None_\)

Examples using VectaraQueryConfig

  * [Vectara](https://python.langchain.com/docs/integrations/vectorstores/vectara/)

  * [Vectara Chat](https://python.langchain.com/docs/integrations/providers/vectara/vectara_chat/)

__On this page