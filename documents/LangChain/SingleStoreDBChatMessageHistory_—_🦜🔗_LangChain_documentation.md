# SingleStoreDBChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.singlestoredb.SingleStoreDBChatMessageHistory.html
**Word Count:** 868
**Links Count:** 172
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# SingleStoreDBChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.singlestoredb.SingleStoreDBChatMessageHistory\(

    _session\_id : str_,     _\*_ ,     _table\_name : str = 'message\_store'_,     _id\_field : str = 'id'_,     _session\_id\_field : str = 'session\_id'_,     _message\_field : str = 'message'_,     _pool\_size : int = 5_,     _max\_overflow : int = 10_,     _timeout : float = 30_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/singlestoredb.html#SingleStoreDBChatMessageHistory)\#     

Deprecated since version 0.3.22: This class is pending deprecation and may be removed in a future version. You can swap to using the SingleStoreChatMessageHistory implementation in langchain\_singlestore. See <[singlestore-labs/langchain-singlestore](https://github.com/singlestore-labs/langchain-singlestore)> for details about the new implementation. Use `from langchain_singlestore import SingleStoreChatMessageHistory` instead.

Chat message history stored in a SingleStoreDB database.

Initialize with necessary components.

Parameters:     

  * **table\_name** \(_str_ _,__optional_\) – Specifies the name of the table in use. Defaults to “message\_store”.

  * **id\_field** \(_str_ _,__optional_\) – Specifies the name of the id field in the table. Defaults to “id”.

  * **session\_id\_field** \(_str_ _,__optional_\) – Specifies the name of the session\_id field in the table. Defaults to “session\_id”.

  * **message\_field** \(_str_ _,__optional_\) – Specifies the name of the message field in the table. Defaults to “message”.

  * **pool** \(_Following arguments pertain to the connection_\)

  * **pool\_size** \(_int_ _,__optional_\) – Determines the number of active connections in the pool. Defaults to 5.

  * **max\_overflow** \(_int_ _,__optional_\) – Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10.

  * **timeout** \(_float_ _,__optional_\) – Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30.

  * **connection** \(_database_\)

  * **host** \(_str_ _,__optional_\) – Specifies the hostname, IP address, or URL for the database connection. The default scheme is “mysql”.

  * **user** \(_str_ _,__optional_\) – Database username.

  * **password** \(_str_ _,__optional_\) – Database password.

  * **port** \(_int_ _,__optional_\) – Database port. Defaults to 3306 for non-HTTP connections, 80 for HTTP connections, and 443 for HTTPS connections.

  * **database** \(_str_ _,__optional_\) – Database name.

  * **the** \(_Additional optional arguments provide further customization over_\)

  * **connection**

  * **pure\_python** \(_bool_ _,__optional_\) – Toggles the connector mode. If True, operates in pure Python mode.

  * **local\_infile** \(_bool_ _,__optional_\) – Allows local file uploads.

  * **charset** \(_str_ _,__optional_\) – Specifies the character set for string values.

  * **ssl\_key** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL key.

  * **ssl\_cert** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate.

  * **ssl\_ca** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate authority.

  * **ssl\_cipher** \(_str_ _,__optional_\) – Sets the SSL cipher list.

  * **ssl\_disabled** \(_bool_ _,__optional_\) – Disables SSL usage.

  * **ssl\_verify\_cert** \(_bool_ _,__optional_\) – Verifies the server’s certificate. Automatically enabled if `ssl_ca` is specified.

  * **ssl\_verify\_identity** \(_bool_ _,__optional_\) – Verifies the server’s identity.

  * **conv** \(_dict_ _\[__int_ _,__Callable_ _\]__,__optional_\) – A dictionary of data conversion functions.

  * **credential\_type** \(_str_ _,__optional_\) – Specifies the type of authentication to use: auth.PASSWORD, auth.JWT, or auth.BROWSER\_SSO.

  * **autocommit** \(_bool_ _,__optional_\) – Enables autocommits.

  * **results\_type** \(_str_ _,__optional_\) – Determines the structure of the query results: tuples, namedtuples, dicts.

  * **results\_format** \(_str_ _,__optional_\) – Deprecated. This option has been renamed to results\_type.

  * **session\_id** \(_str_\)

  * **kwargs** \(_Any_\)

Examples

Basic Usage:               from langchain_community.chat_message_histories import (         SingleStoreDBChatMessageHistory     )          message_history = SingleStoreDBChatMessageHistory(         session_id="my-session",         host="https://user:password@127.0.0.1:3306/database"     )     

Advanced Usage:               from langchain_community.chat_message_histories import (         SingleStoreDBChatMessageHistory     )          message_history = SingleStoreDBChatMessageHistory(         session_id="my-session",         host="127.0.0.1",         port=3306,         user="user",         password="password",         database="db",         table_name="my_custom_table",         pool_size=10,         timeout=60,     )     

Using environment variables:               from langchain_community.chat_message_histories import (         SingleStoreDBChatMessageHistory     )          os.environ['SINGLESTOREDB_URL'] = 'me:p455w0rd@s2-host.com/my_db'     message_history = SingleStoreDBChatMessageHistory("my-session")     

Attributes

`messages` | Retrieve the messages from SingleStoreDB   ---|---      Methods

`__init__`\(session\_id, \*\[, table\_name, ...\]\) | Initialize with necessary components.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Append the message to the record in SingleStoreDB   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory from SingleStoreDB      \_\_init\_\_\(

    _session\_id : str_,     _\*_ ,     _table\_name : str = 'message\_store'_,     _id\_field : str = 'id'_,     _session\_id\_field : str = 'session\_id'_,     _message\_field : str = 'message'_,     _pool\_size : int = 5_,     _max\_overflow : int = 10_,     _timeout : float = 30_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/singlestoredb.html#SingleStoreDBChatMessageHistory.__init__)\#     

Initialize with necessary components.

Parameters:     

  * **table\_name** \(_str_ _,__optional_\) – Specifies the name of the table in use. Defaults to “message\_store”.

  * **id\_field** \(_str_ _,__optional_\) – Specifies the name of the id field in the table. Defaults to “id”.

  * **session\_id\_field** \(_str_ _,__optional_\) – Specifies the name of the session\_id field in the table. Defaults to “session\_id”.

  * **message\_field** \(_str_ _,__optional_\) – Specifies the name of the message field in the table. Defaults to “message”.

  * **pool** \(_Following arguments pertain to the connection_\)

  * **pool\_size** \(_int_ _,__optional_\) – Determines the number of active connections in the pool. Defaults to 5.

  * **max\_overflow** \(_int_ _,__optional_\) – Determines the maximum number of connections allowed beyond the pool\_size. Defaults to 10.

  * **timeout** \(_float_ _,__optional_\) – Specifies the maximum wait time in seconds for establishing a connection. Defaults to 30.

  * **connection** \(_database_\)

  * **host** \(_str_ _,__optional_\) – Specifies the hostname, IP address, or URL for the database connection. The default scheme is “mysql”.

  * **user** \(_str_ _,__optional_\) – Database username.

  * **password** \(_str_ _,__optional_\) – Database password.

  * **port** \(_int_ _,__optional_\) – Database port. Defaults to 3306 for non-HTTP connections, 80 for HTTP connections, and 443 for HTTPS connections.

  * **database** \(_str_ _,__optional_\) – Database name.

  * **the** \(_Additional optional arguments provide further customization over_\)

  * **connection**

  * **pure\_python** \(_bool_ _,__optional_\) – Toggles the connector mode. If True, operates in pure Python mode.

  * **local\_infile** \(_bool_ _,__optional_\) – Allows local file uploads.

  * **charset** \(_str_ _,__optional_\) – Specifies the character set for string values.

  * **ssl\_key** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL key.

  * **ssl\_cert** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate.

  * **ssl\_ca** \(_str_ _,__optional_\) – Specifies the path of the file containing the SSL certificate authority.

  * **ssl\_cipher** \(_str_ _,__optional_\) – Sets the SSL cipher list.

  * **ssl\_disabled** \(_bool_ _,__optional_\) – Disables SSL usage.

  * **ssl\_verify\_cert** \(_bool_ _,__optional_\) – Verifies the server’s certificate. Automatically enabled if `ssl_ca` is specified.

  * **ssl\_verify\_identity** \(_bool_ _,__optional_\) – Verifies the server’s identity.

  * **conv** \(_dict_ _\[__int_ _,__Callable_ _\]__,__optional_\) – A dictionary of data conversion functions.

  * **credential\_type** \(_str_ _,__optional_\) – Specifies the type of authentication to use: auth.PASSWORD, auth.JWT, or auth.BROWSER\_SSO.

  * **autocommit** \(_bool_ _,__optional_\) – Enables autocommits.

  * **results\_type** \(_str_ _,__optional_\) – Determines the structure of the query results: tuples, namedtuples, dicts.

  * **results\_format** \(_str_ _,__optional_\) – Deprecated. This option has been renamed to results\_type.

  * **session\_id** \(_str_\)

  * **kwargs** \(_Any_\)

Examples

Basic Usage:               from langchain_community.chat_message_histories import (         SingleStoreDBChatMessageHistory     )          message_history = SingleStoreDBChatMessageHistory(         session_id="my-session",         host="https://user:password@127.0.0.1:3306/database"     )     

Advanced Usage:               from langchain_community.chat_message_histories import (         SingleStoreDBChatMessageHistory     )          message_history = SingleStoreDBChatMessageHistory(         session_id="my-session",         host="127.0.0.1",         port=3306,         user="user",         password="password",         database="db",         table_name="my_custom_table",         pool_size=10,         timeout=60,     )     

Using environment variables:               from langchain_community.chat_message_histories import (         SingleStoreDBChatMessageHistory     )          os.environ['SINGLESTOREDB_URL'] = 'me:p455w0rd@s2-host.com/my_db'     message_history = SingleStoreDBChatMessageHistory("my-session")     

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/singlestoredb.html#SingleStoreDBChatMessageHistory.add_message)\#     

Append the message to the record in SingleStoreDB

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/singlestoredb.html#SingleStoreDBChatMessageHistory.clear)\#     

Clear session memory from SingleStoreDB

Return type:     

None

Examples using SingleStoreDBChatMessageHistory

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/providers/singlestoredb/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)