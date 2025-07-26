# ngram_fuzzy_matching_strategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.deanonymizer_matching_strategies.ngram_fuzzy_matching_strategy.html
**Word Count:** 92
**Links Count:** 108
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# ngram\_fuzzy\_matching\_strategy\#

langchain\_experimental.data\_anonymizer.deanonymizer\_matching\_strategies.ngram\_fuzzy\_matching\_strategy\(

    _text : str_,     _deanonymizer\_mapping : Dict\[str, Dict\[str, str\]\]_,     _fuzzy\_threshold : int = 85_,     _use\_variable\_length : bool = True_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/deanonymizer_matching_strategies.html#ngram_fuzzy_matching_strategy)\#     

N-gram fuzzy matching strategy for deanonymization.

It replaces all the anonymized entities with the original ones. It uses fuzzy matching to find the position of the anonymized entity in the text. It generates n-grams of the same length as the anonymized entity from the text and uses fuzzy matching to find the position of the anonymized entity in the text.

Parameters:     

  * **text** \(_str_\) – text to deanonymize

  * **deanonymizer\_mapping** \(_Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]_\) – mapping between anonymized entities and original ones

  * **fuzzy\_threshold** \(_int_\) – fuzzy matching threshold

  * **use\_variable\_length** \(_bool_\) – whether to use \(n-1, n, n+1\)-grams or just n-grams

Return type:     

str

__On this page