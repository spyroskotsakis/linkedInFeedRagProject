# RedisChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.redis.RedisChatMessageHistory.html
**Word Count:** 407
**Links Count:** 171
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# RedisChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.redis.RedisChatMessageHistory\(

    _session\_id : str_,     _url : str = 'redis://localhost:6379/0'_,     _key\_prefix : str = 'message\_store:'_,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/redis.html#RedisChatMessageHistory)\#     

Chat message history stored in a Redis database.

Setup:     

Install `redis` python package.               pip install redis     

Instantiate:                    

from langchain\_community.chat\_message\_histories import RedisChatMessageHistory

history = RedisChatMessageHistory\(     

session\_id = “your-session-id”, url=”redis://your-host:your-port:your-database”, \# redis://localhost:6379/0

\)

Add and retrieve messages:                    # Add single message     history.add_message(message)          # Add batch messages     history.add_messages([message1, message2, message3, ...])          # Add human message     history.add_user_message(human_message)          # Add ai message     history.add_ai_message(ai_message)          # Retrieve messages     messages = history.messages     

Initialize with a RedisChatMessageHistory instance.

Parameters:     

  * **session\_id** \(_str_\) – str The ID for single chat session. Used to form keys with key\_prefix.

  * **url** \(_str_\) – Optional\[str\] String parameter configuration for connecting to the redis.

  * **key\_prefix** \(_str_\) – Optional\[str\] The prefix of the key, combined with session id to form the key.

  * **ttl** \(_int_ _|__None_\) – Optional\[int\] Set the expiration time of key, the unit is seconds.

Attributes

`key` | Construct the record key to use   ---|---   `messages` | Retrieve the messages from Redis      Methods

`__init__`\(session\_id\[, url, key\_prefix, ttl\]\) | Initialize with a RedisChatMessageHistory instance.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Append the message to the record in Redis   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory from Redis      \_\_init\_\_\(

    _session\_id : str_,     _url : str = 'redis://localhost:6379/0'_,     _key\_prefix : str = 'message\_store:'_,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/redis.html#RedisChatMessageHistory.__init__)\#     

Initialize with a RedisChatMessageHistory instance.

Parameters:     

  * **session\_id** \(_str_\) – str The ID for single chat session. Used to form keys with key\_prefix.

  * **url** \(_str_\) – Optional\[str\] String parameter configuration for connecting to the redis.

  * **key\_prefix** \(_str_\) – Optional\[str\] The prefix of the key, combined with session id to form the key.

  * **ttl** \(_int_ _|__None_\) – Optional\[int\] Set the expiration time of key, the unit is seconds.

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/redis.html#RedisChatMessageHistory.add_message)\#     

Append the message to the record in Redis

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

Return type:     

None

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/redis.html#RedisChatMessageHistory.clear)\#     

Clear session memory from Redis

Return type:     

None

Examples using RedisChatMessageHistory

  * [Redis](https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/)

__On this page