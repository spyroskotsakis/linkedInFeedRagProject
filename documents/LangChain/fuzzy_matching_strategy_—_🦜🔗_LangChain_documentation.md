# fuzzy_matching_strategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.deanonymizer_matching_strategies.fuzzy_matching_strategy.html
**Word Count:** 77
**Links Count:** 108
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# fuzzy\_matching\_strategy\#

langchain\_experimental.data\_anonymizer.deanonymizer\_matching\_strategies.fuzzy\_matching\_strategy\(

    _text : str_,     _deanonymizer\_mapping : Dict\[str, Dict\[str, str\]\]_,     _max\_l\_dist : int = 3_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/deanonymizer_matching_strategies.html#fuzzy_matching_strategy)\#     

Fuzzy matching strategy for deanonymization.

It uses fuzzy matching to find the position of the anonymized entity in the text. It replaces all the anonymized entities with the original ones.

Parameters:     

  * **text** \(_str_\) – text to deanonymize

  * **deanonymizer\_mapping** \(_Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]_\) – mapping between anonymized entities and original ones

  * **max\_l\_dist** \(_int_\) – maximum Levenshtein distance between the anonymized entity and the text segment to consider it a match

Return type:     

str

Examples of matching:     

Kaenu Reves -> Keanu Reeves John F. Kennedy -> John Kennedy

__On this page