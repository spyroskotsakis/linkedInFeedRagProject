# utilities — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utilities.html
**Word Count:** 59
**Links Count:** 90
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# `utilities`\#

**Classes**

[`utilities.redis.TokenEscaper`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.redis.TokenEscaper.html#langchain_aws.utilities.redis.TokenEscaper "langchain_aws.utilities.redis.TokenEscaper")\(\[escape\_chars\_re\]\) | Escape punctuation within an input string.   ---|---   [`utilities.utils.DistanceStrategy`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.DistanceStrategy.html#langchain_aws.utilities.utils.DistanceStrategy "langchain_aws.utilities.utils.DistanceStrategy")\(value\) | Enumerator of the Distance strategies for calculating distances between vectors.      **Functions**

[`utilities.math.cosine_similarity`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.math.cosine_similarity.html#langchain_aws.utilities.math.cosine_similarity "langchain_aws.utilities.math.cosine_similarity")\(X, Y\) | Row-wise cosine similarity between two equal-width matrices.   ---|---   [`utilities.math.cosine_similarity_top_k`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.math.cosine_similarity_top_k.html#langchain_aws.utilities.math.cosine_similarity_top_k "langchain_aws.utilities.math.cosine_similarity_top_k")\(X, Y\) | Row-wise cosine similarity with optional top-k and score threshold filtering.   [`utilities.redis.get_client`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.redis.get_client.html#langchain_aws.utilities.redis.get_client "langchain_aws.utilities.redis.get_client")\(redis\_url, \*\*kwargs\) | Get a redis client from the connection url given.   [`utilities.utils.filter_complex_metadata`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.filter_complex_metadata.html#langchain_aws.utilities.utils.filter_complex_metadata "langchain_aws.utilities.utils.filter_complex_metadata")\(...\) | Filter out metadata types that are not supported for a vector store.   [`utilities.utils.maximal_marginal_relevance`](https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.maximal_marginal_relevance.html#langchain_aws.utilities.utils.maximal_marginal_relevance "langchain_aws.utilities.utils.maximal_marginal_relevance")\(...\) | Calculate maximal marginal relevance.