# PostgresChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/chat_message_histories/langchain_postgres.chat_message_histories.PostgresChatMessageHistory.html
**Word Count:** 1223
**Links Count:** 141
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# PostgresChatMessageHistory\#

_class _langchain\_postgres.chat\_message\_histories.PostgresChatMessageHistory\(

    _table\_name : str_,     _session\_id : str_,     _/_ ,     _\*_ ,     _sync\_connection : Connection | None = None_,     _async\_connection : AsyncConnection | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory)\#     

Client for persisting chat message history in a Postgres database,

This client provides support for both sync and async via psycopg >=3.

The client can create schema in the database and provides methods to add messages, get messages, and clear the chat message history.

The schema has the following columns:

  * id: A serial primary key.

  * session\_id: The session ID for the chat message history.

  * message: The JSONB message content.

  * created\_at: The timestamp of when the message was created.

Messages are retrieved for a given session\_id and are sorted by the id \(which should be increasing monotonically\), and correspond to the order in which the messages were added to the history.

The “created\_at” column is not returned by the interface, but has been added for the schema so the information is available in the database.

A session\_id can be used to separate different chat histories in the same table, the session\_id should be provided when initializing the client.

This chat history client takes in a psycopg connection object \(either Connection or AsyncConnection\) and uses it to interact with the database.

This design allows to reuse the underlying connection object across multiple instantiations of this class, making instantiation fast.

This chat history client is designed for prototyping applications that involve chat and are based on Postgres.

As your application grows, you will likely need to extend the schema to handle more complex queries. For example, a chat application may involve multiple tables like a user table, a table for storing chat sessions / conversations, and this table for storing chat messages for a given session. The application will require access to additional endpoints like deleting messages by user id, listing conversations by user id or ordering them based on last message time, etc.

Feel free to adapt this implementation to suit your application’s needs.

Parameters:     

  * **session\_id** \(_str_\) – The session ID to use for the chat message history

  * **table\_name** \(_str_\) – The name of the database table to use

  * **sync\_connection** \(_Optional_ _\[__psycopg.Connection_ _\]_\) – An existing psycopg connection instance

  * **async\_connection** \(_Optional_ _\[__psycopg.AsyncConnection_ _\]_\) – An existing psycopg async connection instance

Usage:     

  * Use the create\_tables or acreate\_tables method to set up the table schema in the database.

  * Initialize the class with the appropriate session ID, table name, and database connection.

  * Add messages to the database using add\_messages or aadd\_messages.

  * Retrieve messages with get\_messages or aget\_messages.

  * Clear the session history with clear or aclear when needed.

Note

  * At least one of sync\_connection or async\_connection must be provided.

Examples:               import uuid          from langchain_core.messages import SystemMessage, AIMessage, HumanMessage     from langchain_postgres import PostgresChatMessageHistory     import psycopg          # Establish a synchronous connection to the database     # (or use psycopg.AsyncConnection for async)     sync_connection = psycopg2.connect(conn_info)          # Create the table schema (only needs to be done once)     table_name = "chat_history"     PostgresChatMessageHistory.create_tables(sync_connection, table_name)          session_id = str(uuid.uuid4())          # Initialize the chat history manager     chat_history = PostgresChatMessageHistory(         table_name,         session_id,         sync_connection=sync_connection     )          # Add messages to the chat history     chat_history.add_messages([         SystemMessage(content="Meow"),         AIMessage(content="woof"),         HumanMessage(content="bark"),     ])          print(chat_history.messages)     

Attributes

`messages` | The abstraction required a property.   ---|---      Methods

`__init__`\(table\_name, session\_id, /, \*\[, ...\]\) | Client for persisting chat message history in a Postgres database,   ---|---   `aadd_messages`\(messages\) | Add messages to the chat message history.   `aclear`\(\) | Clear the chat message history for the GIVEN session.   `acreate_tables`\(connection, table\_name, /\) | Create the table schema in the database and create relevant indexes.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the store.   `add_messages`\(messages\) | Add messages to the chat message history.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `adrop_table`\(connection, table\_name, /\) | Delete the table schema in the database.   `aget_messages`\(\) | Retrieve messages from the chat message history.   `clear`\(\) | Clear the chat message history for the GIVEN session.   `create_tables`\(connection, table\_name, /\) | Create the table schema in the database and create relevant indexes.   `drop_table`\(connection, table\_name, /\) | Delete the table schema in the database.   `get_messages`\(\) | Retrieve messages from the chat message history.      \_\_init\_\_\(

    _table\_name : str_,     _session\_id : str_,     _/_ ,     _\*_ ,     _sync\_connection : Connection | None = None_,     _async\_connection : AsyncConnection | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.__init__)\#     

Client for persisting chat message history in a Postgres database,

This client provides support for both sync and async via psycopg >=3.

The client can create schema in the database and provides methods to add messages, get messages, and clear the chat message history.

The schema has the following columns:

  * id: A serial primary key.

  * session\_id: The session ID for the chat message history.

  * message: The JSONB message content.

  * created\_at: The timestamp of when the message was created.

Messages are retrieved for a given session\_id and are sorted by the id \(which should be increasing monotonically\), and correspond to the order in which the messages were added to the history.

The “created\_at” column is not returned by the interface, but has been added for the schema so the information is available in the database.

A session\_id can be used to separate different chat histories in the same table, the session\_id should be provided when initializing the client.

This chat history client takes in a psycopg connection object \(either Connection or AsyncConnection\) and uses it to interact with the database.

This design allows to reuse the underlying connection object across multiple instantiations of this class, making instantiation fast.

This chat history client is designed for prototyping applications that involve chat and are based on Postgres.

As your application grows, you will likely need to extend the schema to handle more complex queries. For example, a chat application may involve multiple tables like a user table, a table for storing chat sessions / conversations, and this table for storing chat messages for a given session. The application will require access to additional endpoints like deleting messages by user id, listing conversations by user id or ordering them based on last message time, etc.

Feel free to adapt this implementation to suit your application’s needs.

Parameters:     

  * **session\_id** \(_str_\) – The session ID to use for the chat message history

  * **table\_name** \(_str_\) – The name of the database table to use

  * **sync\_connection** \(_Connection_ _|__None_\) – An existing psycopg connection instance

  * **async\_connection** \(_AsyncConnection_ _|__None_\) – An existing psycopg async connection instance

Return type:     

None

Usage:     

  * Use the create\_tables or acreate\_tables method to set up the table schema in the database.

  * Initialize the class with the appropriate session ID, table name, and database connection.

  * Add messages to the database using add\_messages or aadd\_messages.

  * Retrieve messages with get\_messages or aget\_messages.

  * Clear the session history with clear or aclear when needed.

Note

  * At least one of sync\_connection or async\_connection must be provided.

Examples:               import uuid          from langchain_core.messages import SystemMessage, AIMessage, HumanMessage     from langchain_postgres import PostgresChatMessageHistory     import psycopg          # Establish a synchronous connection to the database     # (or use psycopg.AsyncConnection for async)     sync_connection = psycopg2.connect(conn_info)          # Create the table schema (only needs to be done once)     table_name = "chat_history"     PostgresChatMessageHistory.create_tables(sync_connection, table_name)          session_id = str(uuid.uuid4())          # Initialize the chat history manager     chat_history = PostgresChatMessageHistory(         table_name,         session_id,         sync_connection=sync_connection     )          # Add messages to the chat history     chat_history.add_messages([         SystemMessage(content="Meow"),         AIMessage(content="woof"),         HumanMessage(content="bark"),     ])          print(chat_history.messages)     

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.aadd_messages)\#     

Add messages to the chat message history.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.aclear)\#     

Clear the chat message history for the GIVEN session.

Return type:     

None

_async static _acreate\_tables\(

    _connection : AsyncConnection_,     _table\_name : str_,     _/_ , \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.acreate_tables)\#     

Create the table schema in the database and create relevant indexes.

Parameters:     

  * **connection** \(_AsyncConnection_\)

  * **table\_name** \(_str_\)

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None\#     

Add a Message object to the store.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A BaseMessage object to store.

Raises:     

**NotImplementedError** – If the sub-class has not implemented an efficient add\_messages method.

Return type:     

None

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.add_messages)\#     

Add messages to the chat message history.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

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

_async static _adrop\_table\(

    _connection : AsyncConnection_,     _table\_name : str_,     _/_ , \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.adrop_table)\#     

Delete the table schema in the database.

Warning

This will delete the given table from the database including all the database in the table and the schema of the table.

Parameters:     

  * **connection** \(_AsyncConnection_\) – Async database connection.

  * **table\_name** \(_str_\) – The name of the table to create.

Return type:     

None

_async _aget\_messages\(\) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.aget_messages)\#     

Retrieve messages from the chat message history.

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.clear)\#     

Clear the chat message history for the GIVEN session.

Return type:     

None

_static _create\_tables\(

    _connection : Connection_,     _table\_name : str_,     _/_ , \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.create_tables)\#     

Create the table schema in the database and create relevant indexes.

Parameters:     

  * **connection** \(_Connection_\)

  * **table\_name** \(_str_\)

Return type:     

None

_static _drop\_table\(

    _connection : Connection_,     _table\_name : str_,     _/_ , \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.drop_table)\#     

Delete the table schema in the database.

Warning

This will delete the given table from the database including all the database in the table and the schema of the table.

Parameters:     

  * **connection** \(_Connection_\) – The database connection.

  * **table\_name** \(_str_\) – The name of the table to create.

Return type:     

None

get\_messages\(\) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/chat_message_histories.html#PostgresChatMessageHistory.get_messages)\#     

Retrieve messages from the chat message history.

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Examples using PostgresChatMessageHistory

  * [Postgres](https://python.langchain.com/docs/integrations/memory/postgres_chat_message_history/)

__On this page   *[/]: Positional-only parameter separator (PEP 570)   *[\*]: Keyword-only parameters separator (PEP 3102)