# ensure_topic_exists — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.kafka.ensure_topic_exists.html
**Word Count:** 30
**Links Count:** 128
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# ensure\_topic\_exists\#

langchain\_community.chat\_message\_histories.kafka.ensure\_topic\_exists\(

    _admin\_client : AdminClient_,     _topic\_name : str_,     _replication\_factor : int_,     _partition : int_,     _ttl\_ms : int_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#ensure_topic_exists)\#     

Create topic if it doesn’t exist, and return the number of partitions. If the topic already exists, we don’t change the topic configuration.

Parameters:     

  * **admin\_client** \(_AdminClient_\)

  * **topic\_name** \(_str_\)

  * **replication\_factor** \(_int_\)

  * **partition** \(_int_\)

  * **ttl\_ms** \(_int_\)

Return type:     

int

__On this page