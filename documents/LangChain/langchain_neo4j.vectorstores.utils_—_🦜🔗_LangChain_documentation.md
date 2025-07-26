# langchain_neo4j.vectorstores.utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_neo4j/vectorstores/utils.html
**Word Count:** 13
**Links Count:** 13
**Scraped:** 2025-07-21 08:57:58
**Status:** completed

---

# Source code for langchain\_neo4j.vectorstores.utils               from enum import Enum                              [[docs]](https://python.langchain.com/api_reference/neo4j/vectorstores/langchain_neo4j.vectorstores.utils.DistanceStrategy.html#langchain_neo4j.vectorstores.utils.DistanceStrategy)     class DistanceStrategy(str, Enum):         """Enumerator of the Distance strategies for calculating distances         between vectors."""              EUCLIDEAN_DISTANCE = "EUCLIDEAN_DISTANCE"         MAX_INNER_PRODUCT = "MAX_INNER_PRODUCT"         DOT_PRODUCT = "DOT_PRODUCT"         JACCARD = "JACCARD"         COSINE = "COSINE"