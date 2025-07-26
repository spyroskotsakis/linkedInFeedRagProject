# CassandraChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.cassandra.CassandraChatMessageHistory.html
**Word Count:** 408
**Links Count:** 179
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# CassandraChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.cassandra.CassandraChatMessageHistory\(

    _session\_id : str_,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = 'message\_store'_,     _ttl\_seconds : int | None = None_,     _\*_ ,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory)\#     

Chat message history that is backed by Cassandra.

Initialize a new instance of CassandraChatMessageHistory.

Parameters:     

  * **session\_id** \(_str_\) – arbitrary key that is used to store the messages of a single chat session.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – name of the table to use.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – time-to-live \(seconds\) for automatic expiration of stored entries. None \(default\) for no expiration.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Cassandra table \(SYNC, ASYNC or OFF\).

Attributes

`messages` | Retrieve all session messages from DB   ---|---      Methods

`__init__`\(session\_id\[, session, keyspace, ...\]\) | Initialize a new instance of CassandraChatMessageHistory.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Clear session memory from DB   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Write a message to the table   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Retrieve all session messages from DB   `clear`\(\) | Clear session memory from DB      \_\_init\_\_\(

    _session\_id : str_,     _session : Session | None = None_,     _keyspace : str | None = None_,     _table\_name : str = 'message\_store'_,     _ttl\_seconds : int | None = None_,     _\*_ ,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory.__init__)\#     

Initialize a new instance of CassandraChatMessageHistory.

Parameters:     

  * **session\_id** \(_str_\) – arbitrary key that is used to store the messages of a single chat session.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Cassandra driver session. If not provided, it is resolved from cassio.

  * **keyspace** \(_Optional_ _\[__str_ _\]_\) – Cassandra key space. If not provided, it is resolved from cassio.

  * **table\_name** \(_str_\) – name of the table to use.

  * **ttl\_seconds** \(_Optional_ _\[__int_ _\]_\) – time-to-live \(seconds\) for automatic expiration of stored entries. None \(default\) for no expiration.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Cassandra table \(SYNC, ASYNC or OFF\).

Return type:     

None

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory.aadd_messages)\#     

Async add a list of messages.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory.aclear)\#     

Clear session memory from DB

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory.add_message)\#     

Write a message to the table

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A message to write.

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

_async _aget\_messages\(\) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory.aget_messages)\#     

Retrieve all session messages from DB

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/cassandra.html#CassandraChatMessageHistory.clear)\#     

Clear session memory from DB

Return type:     

None

Examples using CassandraChatMessageHistory

  * [Cassandra](https://python.langchain.com/docs/integrations/providers/cassandra/)

  * [Cassandra ](https://python.langchain.com/docs/integrations/memory/cassandra_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)