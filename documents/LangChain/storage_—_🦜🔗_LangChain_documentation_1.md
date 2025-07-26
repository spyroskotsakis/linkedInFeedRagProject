# storage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/storage.html
**Word Count:** 107
**Links Count:** 116
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# `storage`\#

**Storage** is an implementation of key-value store.

Storage module provides implementations of various key-value stores that conform to a simple key-value interface.

The primary goal of these storages is to support caching.

**Class hierarchy:**               BaseStore --> <name>Store  # Examples: MongoDBStore, RedisStore     

**Classes**

[`storage.astradb.AstraDBBaseStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBBaseStore.html#langchain_community.storage.astradb.AstraDBBaseStore "langchain_community.storage.astradb.AstraDBBaseStore")\(\*args, \*\*kwargs\) | Base class for the DataStax AstraDB data store.   ---|---   [`storage.cassandra.CassandraByteStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.cassandra.CassandraByteStore.html#langchain_community.storage.cassandra.CassandraByteStore "langchain_community.storage.cassandra.CassandraByteStore")\(table, \*\) | A ByteStore implementation using Cassandra as the backend.   [`storage.mongodb.MongoDBByteStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.mongodb.MongoDBByteStore.html#langchain_community.storage.mongodb.MongoDBByteStore "langchain_community.storage.mongodb.MongoDBByteStore")\(...\[, ...\]\) | BaseStore implementation using MongoDB as the underlying store.   [`storage.mongodb.MongoDBStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.mongodb.MongoDBStore.html#langchain_community.storage.mongodb.MongoDBStore "langchain_community.storage.mongodb.MongoDBStore")\(...\[, ...\]\) | BaseStore implementation using MongoDB as the underlying store.   [`storage.redis.RedisStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.redis.RedisStore.html#langchain_community.storage.redis.RedisStore "langchain_community.storage.redis.RedisStore")\(\*\[, client, ...\]\) | BaseStore implementation using Redis as the underlying store.   [`storage.sql.LangchainKeyValueStores`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.LangchainKeyValueStores.html#langchain_community.storage.sql.LangchainKeyValueStores "langchain_community.storage.sql.LangchainKeyValueStores")\(\*\*kwargs\) | Table used to save values.   [`storage.sql.SQLStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.SQLStore.html#langchain_community.storage.sql.SQLStore "langchain_community.storage.sql.SQLStore")\(\*, namespace\[, db\_url, ...\]\) | BaseStore interface that works on an SQL database.   [`storage.upstash_redis.UpstashRedisByteStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisByteStore.html#langchain_community.storage.upstash_redis.UpstashRedisByteStore "langchain_community.storage.upstash_redis.UpstashRedisByteStore")\(\*\) | BaseStore implementation using Upstash Redis as the underlying store to store raw bytes.      **Functions**

[`storage.sql.items_equal`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.sql.items_equal.html#langchain_community.storage.sql.items_equal "langchain_community.storage.sql.items_equal")\(x, y\) |    ---|---      **Deprecated classes**

[`storage.astradb.AstraDBByteStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBByteStore.html#langchain_community.storage.astradb.AstraDBByteStore "langchain_community.storage.astradb.AstraDBByteStore")\(collection\_name\) |    ---|---   [`storage.astradb.AstraDBStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.astradb.AstraDBStore.html#langchain_community.storage.astradb.AstraDBStore "langchain_community.storage.astradb.AstraDBStore")\(collection\_name\) |    [`storage.upstash_redis.UpstashRedisStore`](https://python.langchain.com/api_reference/community/storage/langchain_community.storage.upstash_redis.UpstashRedisStore.html#langchain_community.storage.upstash_redis.UpstashRedisStore "langchain_community.storage.upstash_redis.UpstashRedisStore")\(\*\[, ...\]\) |