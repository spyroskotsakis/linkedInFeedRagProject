# CosmosDBChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/chat_message_histories/langchain_azure_ai.chat_message_histories.cosmos_db.CosmosDBChatMessageHistory.html
**Word Count:** 549
**Links Count:** 129
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# CosmosDBChatMessageHistory\#

_class _langchain\_azure\_ai.chat\_message\_histories.cosmos\_db.CosmosDBChatMessageHistory\(

    _cosmos\_endpoint : str_,     _cosmos\_database : str_,     _cosmos\_container : str_,     _session\_id : str_,     _user\_id : str_,     _credential : Any = None_,     _connection\_string : str | None = None_,     _ttl : int | None = None_,     _cosmos\_client\_kwargs : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory)\#     

Chat message history backed by Azure CosmosDB.

Initializes a new instance of the CosmosDBChatMessageHistory class.

Make sure to call prepare\_cosmos or use the context manager to make sure your database is ready.

Either a credential or a connection string must be provided.

Parameters:     

  * **cosmos\_endpoint** \(_str_\) – The connection endpoint for the Azure Cosmos DB account.

  * **cosmos\_database** \(_str_\) – The name of the database to use.

  * **cosmos\_container** \(_str_\) – The name of the container to use.

  * **session\_id** \(_str_\) – The session ID to use, can be overwritten while loading.

  * **user\_id** \(_str_\) – The user ID to use, can be overwritten while loading.

  * **credential** \(_Any_\) – The credential to use to authenticate to Azure Cosmos DB.

  * **connection\_string** \(_Optional_ _\[__str_ _\]_\) – The connection string to use to authenticate.

  * **ttl** \(_Optional_ _\[__int_ _\]_\) – The time to live \(in seconds\) to use for documents in the container.

  * **cosmos\_client\_kwargs** \(_Optional_ _\[__dict_ _\]_\) – Additional kwargs to pass to the CosmosClient.

Attributes

Methods

`__init__`\(cosmos\_endpoint, cosmos\_database, ...\) | Initializes a new instance of the CosmosDBChatMessageHistory class.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a self-created message to the store.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory from this memory and cosmos.   `load_messages`\(\) | Retrieve the messages from Cosmos.   `prepare_cosmos`\(\) | Prepare the CosmosDB client.   `upsert_messages`\(\) | Update the cosmosdb item.      \_\_init\_\_\(

    _cosmos\_endpoint : str_,     _cosmos\_database : str_,     _cosmos\_container : str_,     _session\_id : str_,     _user\_id : str_,     _credential : Any = None_,     _connection\_string : str | None = None_,     _ttl : int | None = None_,     _cosmos\_client\_kwargs : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory.__init__)\#     

Initializes a new instance of the CosmosDBChatMessageHistory class.

Make sure to call prepare\_cosmos or use the context manager to make sure your database is ready.

Either a credential or a connection string must be provided.

Parameters:     

  * **cosmos\_endpoint** \(_str_\) – The connection endpoint for the Azure Cosmos DB account.

  * **cosmos\_database** \(_str_\) – The name of the database to use.

  * **cosmos\_container** \(_str_\) – The name of the container to use.

  * **session\_id** \(_str_\) – The session ID to use, can be overwritten while loading.

  * **user\_id** \(_str_\) – The user ID to use, can be overwritten while loading.

  * **credential** \(_Any_\) – The credential to use to authenticate to Azure Cosmos DB.

  * **connection\_string** \(_str_ _|__None_\) – The connection string to use to authenticate.

  * **ttl** \(_int_ _|__None_\) – The time to live \(in seconds\) to use for documents in the container.

  * **cosmos\_client\_kwargs** \(_dict_ _|__None_\) – Additional kwargs to pass to the CosmosClient.

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory.add_message)\#     

Add a self-created message to the store.

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory.clear)\#     

Clear session memory from this memory and cosmos.

Return type:     

None

load\_messages\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory.load_messages)\#     

Retrieve the messages from Cosmos.

Return type:     

None

prepare\_cosmos\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory.prepare_cosmos)\#     

Prepare the CosmosDB client.

Use this function or the context manager to make sure your database is ready.

Return type:     

None

upsert\_messages\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/chat_message_histories/cosmos_db.html#CosmosDBChatMessageHistory.upsert_messages)\#     

Update the cosmosdb item.

Return type:     

None

__On this page