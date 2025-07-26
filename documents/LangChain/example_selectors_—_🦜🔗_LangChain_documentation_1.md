# example_selectors — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/example_selectors.html
**Word Count:** 60
**Links Count:** 104
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# `example_selectors`\#

Example selectors.

**Example selector** implements logic for selecting examples to include them in prompts. This allows us to select examples that are most relevant to the input.

**Classes**

[`example_selectors.base.BaseExampleSelector`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.base.BaseExampleSelector.html#langchain_core.example_selectors.base.BaseExampleSelector "langchain_core.example_selectors.base.BaseExampleSelector")\(\) | Interface for selecting examples to include in prompts.   ---|---   [`example_selectors.length_based.LengthBasedExampleSelector`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.length_based.LengthBasedExampleSelector.html#langchain_core.example_selectors.length_based.LengthBasedExampleSelector "langchain_core.example_selectors.length_based.LengthBasedExampleSelector") | Select examples based on length.   [`example_selectors.semantic_similarity.MaxMarginalRelevanceExampleSelector`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.MaxMarginalRelevanceExampleSelector.html#langchain_core.example_selectors.semantic_similarity.MaxMarginalRelevanceExampleSelector "langchain_core.example_selectors.semantic_similarity.MaxMarginalRelevanceExampleSelector") | Select examples based on Max Marginal Relevance.   [`example_selectors.semantic_similarity.SemanticSimilarityExampleSelector`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html#langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector "langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector") | Select examples based on semantic similarity.      **Functions**

[`example_selectors.semantic_similarity.sorted_values`](https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.sorted_values.html#langchain_core.example_selectors.semantic_similarity.sorted_values "langchain_core.example_selectors.semantic_similarity.sorted_values")\(values\) | Return a list of values in dict sorted by key.   ---|---