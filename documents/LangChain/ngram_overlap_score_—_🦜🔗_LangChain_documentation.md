# ngram_overlap_score — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/example_selectors/langchain_community.example_selectors.ngram_overlap.ngram_overlap_score.html
**Word Count:** 37
**Links Count:** 100
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# ngram\_overlap\_score\#

langchain\_community.example\_selectors.ngram\_overlap.ngram\_overlap\_score\(

    _source : List\[str\]_,     _example : List\[str\]_, \) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/example_selectors/ngram_overlap.html#ngram_overlap_score)\#     

Compute ngram overlap score of source and example as sentence\_bleu score from NLTK package.

Use sentence\_bleu with method1 smoothing function and auto reweighting. Return float value between 0.0 and 1.0 inclusive. <https://www.nltk.org/_modules/nltk/translate/bleu_score.html> <https://aclanthology.org/P02-1040.pdf>

Parameters:     

  * **source** \(_List_ _\[__str_ _\]_\)

  * **example** \(_List_ _\[__str_ _\]_\)

Return type:     

float

__On this page