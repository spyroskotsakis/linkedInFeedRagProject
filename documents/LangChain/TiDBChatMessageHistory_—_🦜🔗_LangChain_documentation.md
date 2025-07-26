# TiDBChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.tidb.TiDBChatMessageHistory.html
**Word Count:** 375
**Links Count:** 175
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# TiDBChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.tidb.TiDBChatMessageHistory\(

    _session\_id : str_,     _connection\_string : str_,     _table\_name : str = 'langchain\_message\_store'_,     _earliest\_time : datetime | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/tidb.html#TiDBChatMessageHistory)\#     

Represents a chat message history stored in a TiDB database.

Initializes a new instance of the TiDBChatMessageHistory class.

Parameters:     

  * **session\_id** \(_str_\) – The ID of the chat session.

  * **connection\_string** \(_str_\) – The connection string for the TiDB database. format: mysql+pymysql://<host>:<PASSWORD>@<host>:4000/<db>?ssl\_ca=/etc/ssl/cert.pem&ssl\_verify\_cert=true&ssl\_verify\_identity=true

  * **table\_name** \(_str_ _,__optional_\) – the table name to store the chat messages. Defaults to “langchain\_message\_store”.

  * **earliest\_time** \(_Optional_ _\[__datetime_ _\]__,__optional_\) – The earliest time to retrieve messages from. Defaults to None.

Attributes

`messages` | returns all messages   ---|---      Methods

`__init__`\(session\_id, connection\_string\[, ...\]\) | Initializes a new instance of the TiDBChatMessageHistory class.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | adds a message to the database and cache   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | clears all messages   `reload_cache`\(\) | reloads messages from database to cache      \_\_init\_\_\(

    _session\_id : str_,     _connection\_string : str_,     _table\_name : str = 'langchain\_message\_store'_,     _earliest\_time : datetime | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/tidb.html#TiDBChatMessageHistory.__init__)\#     

Initializes a new instance of the TiDBChatMessageHistory class.

Parameters:     

  * **session\_id** \(_str_\) – The ID of the chat session.

  * **connection\_string** \(_str_\) – The connection string for the TiDB database. format: mysql+pymysql://<host>:<PASSWORD>@<host>:4000/<db>?ssl\_ca=/etc/ssl/cert.pem&ssl\_verify\_cert=true&ssl\_verify\_identity=true

  * **table\_name** \(_str_ _,__optional_\) – the table name to store the chat messages. Defaults to “langchain\_message\_store”.

  * **earliest\_time** \(_Optional_ _\[__datetime_ _\]__,__optional_\) – The earliest time to retrieve messages from. Defaults to None.

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/tidb.html#TiDBChatMessageHistory.add_message)\#     

adds a message to the database and cache

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/tidb.html#TiDBChatMessageHistory.clear)\#     

clears all messages

Return type:     

None

reload\_cache\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/tidb.html#TiDBChatMessageHistory.reload_cache)\#     

reloads messages from database to cache

Return type:     

None

Examples using TiDBChatMessageHistory

  * [TiDB](https://python.langchain.com/docs/integrations/providers/tidb/)

__On this page