# SQLChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.SQLChatMessageHistory.html
**Word Count:** 451
**Links Count:** 193
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# SQLChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.sql.SQLChatMessageHistory\(

    _session\_id : str_,     _connection\_string : str | None = None_,     _table\_name : str = 'message\_store'_,     _session\_id\_field\_name : str = 'session\_id'_,     _custom\_message\_converter : [BaseMessageConverter](https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.BaseMessageConverter.html#langchain_community.chat_message_histories.sql.BaseMessageConverter "langchain_community.chat_message_histories.sql.BaseMessageConverter") | None = None_,     _connection : None | AsyncEngine | Engine | str = None_,     _engine\_args : Dict\[str, Any\] | None = None_,     _async\_mode : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory)\#     

Chat message history stored in an SQL database.

Example               from langchain_core.messages import HumanMessage          from langchain_community.chat_message_histories import SQLChatMessageHistory          # create sync sql message history by connection_string     message_history = SQLChatMessageHistory(         session_id='foo', connection_string='sqlite///:memory.db'     )     message_history.add_message(HumanMessage("hello"))     message_history.message          # create async sql message history using aiosqlite     # from sqlalchemy.ext.asyncio import create_async_engine     #     # async_engine = create_async_engine("sqlite+aiosqlite:///memory.db")     # async_message_history = SQLChatMessageHistory(     #     session_id='foo', connection=async_engine,     # )     # await async_message_history.aadd_message(HumanMessage("hello"))     # await async_message_history.aget_messages()     

Initialize with a SQLChatMessageHistory instance.

Parameters:     

  * **session\_id** \(_str_\) – Indicates the id of the same session.

  * **connection\_string** \(_str_ _|__None_\) – String parameter configuration for connecting to the database.

  * **table\_name** \(_str_\) – Table name used to save data.

  * **session\_id\_field\_name** \(_str_\) – The name of field of session\_id.

  * **custom\_message\_converter** \([_BaseMessageConverter_](https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.BaseMessageConverter.html#langchain_community.chat_message_histories.sql.BaseMessageConverter "langchain_community.chat_message_histories.sql.BaseMessageConverter") _|__None_\) – Custom message converter for converting database data and BaseMessage

  * **connection** \(_None_ _|__AsyncEngine_ _|__Engine_ _|__str_\) – Database connection object, which can be a string containing connection configuration, Engine object or AsyncEngine object.

  * **engine\_args** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Additional configuration for creating database engines.

  * **async\_mode** \(_bool_ _|__None_\) – Whether it is an asynchronous connection.

Attributes

`Session` |    ---|---   `messages` | Retrieve all messages from db      Methods

`__init__`\(session\_id\[, connection\_string, ...\]\) | Initialize with a SQLChatMessageHistory instance.   ---|---   `aadd_message`\(message\) | Add a Message object to the store.   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Clear session memory from db   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Append the message to the record in db   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Retrieve all messages from db   `clear`\(\) | Clear session memory from db   `get_messages`\(\) |       \_\_init\_\_\(

    _session\_id : str_,     _connection\_string : str | None = None_,     _table\_name : str = 'message\_store'_,     _session\_id\_field\_name : str = 'session\_id'_,     _custom\_message\_converter : [BaseMessageConverter](https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.BaseMessageConverter.html#langchain_community.chat_message_histories.sql.BaseMessageConverter "langchain_community.chat_message_histories.sql.BaseMessageConverter") | None = None_,     _connection : None | AsyncEngine | Engine | str = None_,     _engine\_args : Dict\[str, Any\] | None = None_,     _async\_mode : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.__init__)\#     

Initialize with a SQLChatMessageHistory instance.

Parameters:     

  * **session\_id** \(_str_\) – Indicates the id of the same session.

  * **connection\_string** \(_str_ _|__None_\) – String parameter configuration for connecting to the database.

  * **table\_name** \(_str_\) – Table name used to save data.

  * **session\_id\_field\_name** \(_str_\) – The name of field of session\_id.

  * **custom\_message\_converter** \([_BaseMessageConverter_](https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.BaseMessageConverter.html#langchain_community.chat_message_histories.sql.BaseMessageConverter "langchain_community.chat_message_histories.sql.BaseMessageConverter") _|__None_\) – Custom message converter for converting database data and BaseMessage

  * **connection** \(_None_ _|__AsyncEngine_ _|__Engine_ _|__str_\) – Database connection object, which can be a string containing connection configuration, Engine object or AsyncEngine object.

  * **engine\_args** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Additional configuration for creating database engines.

  * **async\_mode** \(_bool_ _|__None_\) – Whether it is an asynchronous connection.

_async _aadd\_message\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.aadd_message)\#     

Add a Message object to the store.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A BaseMessage object to store.

Return type:     

None

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.aadd_messages)\#     

Async add a list of messages.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.aclear)\#     

Clear session memory from db

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.add_message)\#     

Append the message to the record in db

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

Return type:     

None

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.add_messages)\#     

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

_async _aget\_messages\(\) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.aget_messages)\#     

Retrieve all messages from db

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.clear)\#     

Clear session memory from db

Return type:     

None

get\_messages\(\) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#SQLChatMessageHistory.get_messages)\#     

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Examples using SQLChatMessageHistory

  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)

  * [SQL \(SQLAlchemy\)](https://python.langchain.com/docs/integrations/memory/sql_chat_message_history/)

  * [SQLite](https://python.langchain.com/docs/integrations/providers/sqlite/)

__On this page