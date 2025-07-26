# get_client — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.redis.get_client.html
**Word Count:** 159
**Links Count:** 249
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# get\_client\#

langchain\_community.utilities.redis.get\_client\(_redis\_url : str_, _\*\* kwargs: Any_\) → RedisType[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/redis.html#get_client)\#     

Get a redis client from the connection url given. This helper accepts urls for Redis server \(TCP with/without TLS or UnixSocket\) as well as Redis Sentinel connections.

Redis Cluster is not supported.

Before creating a connection the existence of the database driver is checked an and ValueError raised otherwise

To use, you should have the `redis` python package installed.

Example               from langchain_community.utilities.redis import get_client     redis_client = get_client(         redis_url="redis://username:password@localhost:6379"         index_name="my-index",         embedding_function=embeddings.embed_query,     )     

To use a redis replication setup with multiple redis server and redis sentinels set “redis\_url” to “redis+sentinel://” scheme. With this url format a path is needed holding the name of the redis service within the sentinels to get the correct redis server connection. The default service name is “mymaster”. The optional second part of the path is the redis db number to connect to.

An optional username or password is used for both connections to the rediserver and the sentinel, different passwords for server and sentinel are not supported. And as another constraint only one sentinel instance can be given:

Example               from langchain_community.utilities.redis import get_client     redis_client = get_client(         redis_url="redis+sentinel://username:password@sentinelhost:26379/mymaster/0"         index_name="my-index",         embedding_function=embeddings.embed_query,     )     

Parameters:     

  * **redis\_url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

RedisType

__On this page