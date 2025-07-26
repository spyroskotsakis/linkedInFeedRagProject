# langchain-redis: 0.2.3 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/index.html
**Word Count:** 58
**Links Count:** 82
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# langchain-redis: 0.2.3\#

## [cache](https://python.langchain.com/api_reference/redis/cache.html#langchain-redis-cache)\#

**Classes**

[`cache.EmbeddingsVectorizer`](https://python.langchain.com/api_reference/redis/cache/langchain_redis.cache.EmbeddingsVectorizer.html#langchain_redis.cache.EmbeddingsVectorizer "langchain_redis.cache.EmbeddingsVectorizer") | Create a new model by parsing and validating input data from keyword arguments.   ---|---   [`cache.RedisCache`](https://python.langchain.com/api_reference/redis/cache/langchain_redis.cache.RedisCache.html#langchain_redis.cache.RedisCache "langchain_redis.cache.RedisCache")\(\[redis\_url, ttl, prefix, ...\]\) | Redis cache implementation for LangChain.   [`cache.RedisSemanticCache`](https://python.langchain.com/api_reference/redis/cache/langchain_redis.cache.RedisSemanticCache.html#langchain_redis.cache.RedisSemanticCache "langchain_redis.cache.RedisSemanticCache")\(embeddings\[, ...\]\) | Redis-based semantic cache implementation for LangChain.      ## [chat\_message\_history](https://python.langchain.com/api_reference/redis/chat_message_history.html#langchain-redis-chat-message-history)\#

**Classes**

[`chat_message_history.RedisChatMessageHistory`](https://python.langchain.com/api_reference/redis/chat_message_history/langchain_redis.chat_message_history.RedisChatMessageHistory.html#langchain_redis.chat_message_history.RedisChatMessageHistory "langchain_redis.chat_message_history.RedisChatMessageHistory")\(...\) | Redis-based implementation of chat message history using RedisVL.   ---|---      ## [config](https://python.langchain.com/api_reference/redis/config.html#langchain-redis-config)\#

**Classes**

[`config.RedisConfig`](https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html#langchain_redis.config.RedisConfig "langchain_redis.config.RedisConfig") | Configuration class for Redis vector store settings.   ---|---      ## [vectorstores](https://python.langchain.com/api_reference/redis/vectorstores.html#langchain-redis-vectorstores)\#

**Classes**

[`vectorstores.RedisVectorStore`](https://python.langchain.com/api_reference/redis/vectorstores/langchain_redis.vectorstores.RedisVectorStore.html#langchain_redis.vectorstores.RedisVectorStore "langchain_redis.vectorstores.RedisVectorStore")\(embeddings\[, ...\]\) | Redis vector store integration.   ---|---      **Functions**

[`vectorstores.cosine_similarity`](https://python.langchain.com/api_reference/redis/vectorstores/langchain_redis.vectorstores.cosine_similarity.html#langchain_redis.vectorstores.cosine_similarity "langchain_redis.vectorstores.cosine_similarity")\(X, Y\) | Row-wise cosine similarity between two equal-width matrices.   ---|---   [`vectorstores.maximal_marginal_relevance`](https://python.langchain.com/api_reference/redis/vectorstores/langchain_redis.vectorstores.maximal_marginal_relevance.html#langchain_redis.vectorstores.maximal_marginal_relevance "langchain_redis.vectorstores.maximal_marginal_relevance")\(...\) | Calculate maximal marginal relevance.