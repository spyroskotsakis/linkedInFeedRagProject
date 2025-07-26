# get_client — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.redis.get_client.html
**Word Count:** 56
**Links Count:** 87
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# get\_client\#

langchain\_aws.utilities.redis.get\_client\(_redis\_url : str_, _\*\* kwargs: Any_\) → RedisType[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utilities/redis.html#get_client)\#     

Get a redis client from the connection url given. This helper accepts urls for Redis server \(TCP with/without TLS or UnixSocket\) as well as Redis Sentinel connections.

Before creating a connection the existence of the database driver is checked and ValueError raised otherwise.

To use, you should have the `redis` python package installed.

Example               from langchain_community.utilities.redis import get_client     redis_client = get_client(         redis_url="redis://username:password@localhost:6379"         index_name="my-index",         embedding_function=embeddings.embed_query,     )     

Parameters:     

  * **redis\_url** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

RedisType

__On this page