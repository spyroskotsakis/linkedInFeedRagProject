# example_selectors — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/example_selectors.html
**Word Count:** 91
**Links Count:** 96
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# `example_selectors`\#

**Example selector** implements logic for selecting examples to include them in prompts. This allows us to select examples that are most relevant to the input.

There could be multiple strategies for selecting examples. For example, one could select examples based on the similarity of the input to the examples. Another strategy could be to select examples based on the diversity of the examples.

**Classes**

[`example_selectors.ngram_overlap.NGramOverlapExampleSelector`](https://python.langchain.com/api_reference/community/example_selectors/langchain_community.example_selectors.ngram_overlap.NGramOverlapExampleSelector.html#langchain_community.example_selectors.ngram_overlap.NGramOverlapExampleSelector "langchain_community.example_selectors.ngram_overlap.NGramOverlapExampleSelector") | Select and order examples based on ngram overlap score \(sentence\_bleu score from NLTK package\).   ---|---      **Functions**

[`example_selectors.ngram_overlap.ngram_overlap_score`](https://python.langchain.com/api_reference/community/example_selectors/langchain_community.example_selectors.ngram_overlap.ngram_overlap_score.html#langchain_community.example_selectors.ngram_overlap.ngram_overlap_score "langchain_community.example_selectors.ngram_overlap.ngram_overlap_score")\(...\) | Compute ngram overlap score of source and example as sentence\_bleu score from NLTK package.   ---|---