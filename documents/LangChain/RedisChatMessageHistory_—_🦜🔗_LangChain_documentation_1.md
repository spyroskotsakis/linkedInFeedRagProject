# RedisChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/chat_message_history/langchain_redis.chat_message_history.RedisChatMessageHistory.html
**Word Count:** 1015
**Links Count:** 135
**Scraped:** 2025-07-21 08:27:44
**Status:** completed

---

# RedisChatMessageHistory\#

_class _langchain\_redis.chat\_message\_history.RedisChatMessageHistory\(

    _session\_id : str_,     _redis\_url : str = 'redis://localhost:6379'_,     _key\_prefix : str = 'chat:'_,     _ttl : int | None = None_,     _index\_name : str = 'idx:chat\_history'_,     _redis\_client : Redis | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/chat_message_history.html#RedisChatMessageHistory)\#     

Redis-based implementation of chat message history using RedisVL.

This class provides a way to store and retrieve chat message history using Redis with RedisVL for efficient indexing, querying, and document management.

redis\_client\#     

The Redis client instance.

Type:     

[Redis](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")

session\_id\#     

A unique identifier for the chat session.

Type:     

str

key\_prefix\#     

Prefix for Redis keys to namespace the messages.

Type:     

str

ttl\#     

Time-to-live for message entries in seconds.

Type:     

Optional\[int\]

index\_name\#     

Name of the Redis search index for message retrieval.

Type:     

str

Parameters:     

  * **session\_id** \(_str_\) – A unique identifier for the chat session.

  * **redis\_url** \(_str_ _,__optional_\) – URL of the Redis instance. Defaults to “redis://localhost:6379”.

  * **key\_prefix** \(_str_ _,__optional_\) – Prefix for Redis keys. Defaults to “chat:”.

  * **ttl** \(_Optional_ _\[__int_ _\]__,__optional_\) – Time-to-live for entries in seconds. Defaults to None \(no expiration\).

  * **index\_name** \(_str_ _,__optional_\) – Name of the Redis search index. Defaults to “idx:chat\_history”.

  * **redis\_client** \(_Optional_ _\[_[_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis") _\]__,__optional_\) – Existing Redis client instance. If provided, redis\_url is ignored.

  * **\*\*kwargs** – Additional keyword arguments to pass to the Redis client.

Raises:     

  * **ValueError** – If session\_id is empty or None.

  * **ResponseError** – If Redis connection fails or RedisVL operations fail.

Example               from langchain_redis import RedisChatMessageHistory     from langchain_core.messages import HumanMessage, AIMessage          history = RedisChatMessageHistory(         session_id="user123",         redis_url="redis://localhost:6379",         ttl=3600  # Expire chat history after 1 hour     )          # Add messages to the history     history.add_message(HumanMessage(content="Hello, AI!"))     history.add_message(       AIMessage(content="Hello, human! How can I assist you today?")     )          # Retrieve all messages     messages = history.messages     for message in messages:         print(f"{message.type}: {message.content}")          # Clear the history for the session     history.clear()     

Note

  * This class uses RedisVL for managing Redis JSON storage and search indexes, providing efficient querying and retrieval.

  * A Redis search index is created to enable fast lookups and search capabilities over the chat history.

  * If TTL is set, message entries will automatically expire after the specified duration.

  * The session\_id is used to group messages belonging to the same conversation or user session.

  * RedisVL automatically handles tokenization and escaping for search queries.

Attributes

`id` | Return the session ID.   ---|---   `messages` | Retrieve all messages for the current session, sorted by timestamp.      Methods

`__init__`\(session\_id\[, redis\_url, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a message to the chat history using RedisVL.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear all messages from the chat history for the current session.   `delete`\(\) | Delete all sessions and the chat history index from Redis.   `search_messages`\(query\[, limit\]\) | Search for messages in the chat history that match the given query.      \_\_init\_\_\(

    _session\_id : str_,     _redis\_url : str = 'redis://localhost:6379'_,     _key\_prefix : str = 'chat:'_,     _ttl : int | None = None_,     _index\_name : str = 'idx:chat\_history'_,     _redis\_client : Redis | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/chat_message_history.html#RedisChatMessageHistory.__init__)\#     

Parameters:     

  * **session\_id** \(_str_\)

  * **redis\_url** \(_str_\)

  * **key\_prefix** \(_str_\)

  * **ttl** \(_int_ _|__None_\)

  * **index\_name** \(_str_\)

  * **redis\_client** \(_Redis_ _|__None_\)

  * **kwargs** \(_Any_\)

Return type:     

None

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None\#     

Async add a list of messages.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

_async _aclear\(\) → None\#     

Async remove all messages from the store.

Return type:     

None

add\_ai\_message\(

    _message : [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage") | str_, \) → None\#     

Convenience method for adding an AI message string to the store.

Please note that this is a convenience method. Code should favor the bulk add\_messages interface instead to save on round-trips to the underlying persistence layer.

This method may be deprecated in a future release.

Parameters:     

**message** \([_AIMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage") _|__str_\) – The AI message to add.

Return type:     

None

add\_message\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/chat_message_history.html#RedisChatMessageHistory.add_message)\#     

Add a message to the chat history using RedisVL.

This method adds a new message to the Redis store for the current session using RedisVL’s document loading capabilities.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – The message to add to the history. This should be an instance of a class derived from BaseMessage, such as HumanMessage, AIMessage, or SystemMessage.

Raises:     

  * **ResponseError** – If Redis connection fails or RedisVL operations fail.

  * **ValueError** – If message is None or invalid.

Return type:     

None

Example               from langchain_redis import RedisChatMessageHistory     from langchain_core.messages import HumanMessage, AIMessage          history = RedisChatMessageHistory(         session_id="user123",         redis_url="redis://localhost:6379",         ttl=3600  # optional: set TTL to 1 hour     )          # Add a human message     history.add_message(HumanMessage(content="Hello, AI!"))          # Add an AI message     history.add_message(       AIMessage(content="Hello! How can I assist you today?")     )          # Verify messages were added     print(f"Number of messages: {len(history.messages)}")     

Note

  * Each message is stored as a separate entry in Redis, associated with the current session\_id.

  * Messages are stored using RedisVL’s JSON capabilities for efficient storage and retrieval.

  * If a TTL \(Time To Live\) was specified when initializing the history, it will be applied to each message.

  * The message’s content, type, and any additional data \(like timestamp\) are stored.

  * This method is thread-safe and can be used in concurrent environments.

  * The Redis search index is automatically updated to include the new message, enabling future searches.

  * Large message contents may impact performance and storage usage. Consider implementing size limits if dealing with potentially large messages.

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None\#     

Add a list of messages.

Implementations should over-ride this method to handle bulk addition of messages in an efficient manner to avoid unnecessary round-trips to the underlying store.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

add\_user\_message\(

    _message : [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html#langchain_core.messages.human.HumanMessage "langchain_core.messages.human.HumanMessage") | str_, \) → None\#     

Convenience method for adding a human message string to the store.

Please note that this is a convenience method. Code should favor the bulk add\_messages interface instead to save on round-trips to the underlying persistence layer.

This method may be deprecated in a future release.

Parameters:     

**message** \([_HumanMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html#langchain_core.messages.human.HumanMessage "langchain_core.messages.human.HumanMessage") _|__str_\) – The human message to add to the store.

Return type:     

None

_async _aget\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence layer.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/chat_message_history.html#RedisChatMessageHistory.clear)\#     

Clear all messages from the chat history for the current session.

This method removes all messages associated with the current session\_id from the Redis store using RedisVL queries.

Raises:     

**ResponseError** – If Redis connection fails or RedisVL operations fail.

Return type:     

None

Example               from langchain_redis import RedisChatMessageHistory     from langchain_core.messages import HumanMessage, AIMessage          history = RedisChatMessageHistory(session_id="user123", redis_url="redis://localhost:6379")          # Add some messages     history.add_message(HumanMessage(content="Hello, AI!"))     history.add_message(AIMessage(content="Hello, human!"))          # Clear the history     history.clear()          # Verify that the history is empty     assert len(history.messages) == 0     

Note

  * This method only clears messages for the current session\_id.

  * It uses RedisVL’s FilterQuery to find all relevant messages and then deletes them individually using the Redis client.

  * The operation removes all messages for the current session only.

  * After clearing, the Redis search index is still maintained, allowing for immediate use of the same session\_id for new messages if needed.

  * This operation is irreversible. Make sure you want to remove all messages before calling this method.

delete\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/chat_message_history.html#RedisChatMessageHistory.delete)\#     

Delete all sessions and the chat history index from Redis.

Raises:     

**ResponseError** – If Redis connection fails or RedisVL operations fail.

Return type:     

None

search\_messages\(

    _query : str_,     _limit : int = 10_, \) → List\[Dict\[str, Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/chat_message_history.html#RedisChatMessageHistory.search_messages)\#     

Search for messages in the chat history that match the given query.

This method performs a full-text search on the content of messages in the current session using RedisVL’s TextQuery capabilities.

Parameters:     

  * **query** \(_str_\) – The search query string to match against message content.

  * **limit** \(_int_ _,__optional_\) – The maximum number of results to return. Defaults to 10.

Returns:     

A list of dictionaries, each representing a     

matching message.

Each dictionary contains the message content and metadata.

Return type:     

List\[Dict\[str, Any\]\]

Raises:     

**ResponseError** – If Redis connection fails or RedisVL operations fail.

Example               from langchain_redis import RedisChatMessageHistory     from langchain_core.messages import HumanMessage, AIMessage          history = RedisChatMessageHistory(session_id="user123", redis_url="redis://localhost:6379")          # Add some messages     history.add_message(       HumanMessage(content="Tell me about Machine Learning")     )     history.add_message(       AIMessage(content="Machine Learning is a subset of AI...")     )     history.add_message(       HumanMessage(content="What are neural networks?")     )     history.add_message(       AIMessage(         content="Neural networks are a key component of deep learning..."       )     )          # Search for messages containing "learning"     results = history.search_messages("learning", limit=5)          for result in results:         print(f"Content: {result['content']}")         print(f"Type: {result['type']}")         print("---")     

Note

  * The search is performed using RedisVL’s TextQuery capabilities, which allows for efficient full-text search.

  * The search is case-insensitive and uses Redis’ default tokenization and stemming.

  * Only messages from the current session \(as defined by session\_id\) are searched.

  * The returned dictionaries include all stored fields, which typically include ‘content’, ‘type’, and any additional metadata stored with the message.

  * This method is useful for quickly finding relevant parts of a conversation without having to iterate through all messages.

Examples using RedisChatMessageHistory

  * [Redis](https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/)

__On this page