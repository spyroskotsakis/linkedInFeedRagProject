# UpstashRedisChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.upstash_redis.UpstashRedisChatMessageHistory.html
**Word Count:** 281
**Links Count:** 172
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# UpstashRedisChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.upstash\_redis.UpstashRedisChatMessageHistory\(

    _session\_id : str_,     _url : str = ''_,     _token : str = ''_,     _key\_prefix : str = 'message\_store:'_,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/upstash_redis.html#UpstashRedisChatMessageHistory)\#     

Chat message history stored in an Upstash Redis database.

Attributes

`key` | Construct the record key to use   ---|---   `messages` | Retrieve the messages from Upstash Redis      Methods

`__init__`\(session\_id\[, url, token, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Append the message to the record in Upstash Redis   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory from Upstash Redis      Parameters:     

  * **session\_id** \(_str_\)

  * **url** \(_str_\)

  * **token** \(_str_\)

  * **key\_prefix** \(_str_\)

  * **ttl** \(_int_ _|__None_\)

\_\_init\_\_\(

    _session\_id : str_,     _url : str = ''_,     _token : str = ''_,     _key\_prefix : str = 'message\_store:'_,     _ttl : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/upstash_redis.html#UpstashRedisChatMessageHistory.__init__)\#     

Parameters:     

  * **session\_id** \(_str_\)

  * **url** \(_str_\)

  * **token** \(_str_\)

  * **key\_prefix** \(_str_\)

  * **ttl** \(_int_ _|__None_\)

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/upstash_redis.html#UpstashRedisChatMessageHistory.add_message)\#     

Append the message to the record in Upstash Redis

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/upstash_redis.html#UpstashRedisChatMessageHistory.clear)\#     

Clear session memory from Upstash Redis

Return type:     

None

Examples using UpstashRedisChatMessageHistory

  * [Upstash Redis](https://python.langchain.com/docs/integrations/memory/upstash_redis_chat_message_history/)

  * [Upstash Vector](https://python.langchain.com/docs/integrations/providers/upstash/)

__On this page