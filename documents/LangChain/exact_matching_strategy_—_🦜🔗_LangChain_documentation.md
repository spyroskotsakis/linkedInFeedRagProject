# exact_matching_strategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.deanonymizer_matching_strategies.exact_matching_strategy.html
**Word Count:** 33
**Links Count:** 108
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# exact\_matching\_strategy\#

langchain\_experimental.data\_anonymizer.deanonymizer\_matching\_strategies.exact\_matching\_strategy\(

    _text : str_,     _deanonymizer\_mapping : Dict\[str, Dict\[str, str\]\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/deanonymizer_matching_strategies.html#exact_matching_strategy)\#     

Exact matching strategy for deanonymization.

It replaces all the anonymized entities with the original ones.

Parameters:     

  * **text** \(_str_\) – text to deanonymize

  * **deanonymizer\_mapping** \(_Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]_\) – mapping between anonymized entities and original ones

Return type:     

str

__On this page