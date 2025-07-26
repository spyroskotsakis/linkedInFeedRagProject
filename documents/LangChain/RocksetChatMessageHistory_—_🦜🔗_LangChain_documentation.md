# RocksetChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.rocksetdb.RocksetChatMessageHistory.html
**Word Count:** 533
**Links Count:** 171
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# RocksetChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.rocksetdb.RocksetChatMessageHistory\(

    _session\_id: str_,     _client: ~typing.Any_,     _collection: str_,     _workspace: str = 'commons'_,     _messages\_key: str = 'messages'_,     _sync: bool = False_,     _message\_uuid\_method: ~typing.Callable\[\[\]_,     _str | int\] = <function RocksetChatMessageHistory.<lambda>>_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/rocksetdb.html#RocksetChatMessageHistory)\#     

Uses Rockset to store chat messages.

To use, ensure that the rockset python package installed.

Example               from langchain_community.chat_message_histories import (         RocksetChatMessageHistory     )     from rockset import RocksetClient          history = RocksetChatMessageHistory(         session_id="MySession",         client=RocksetClient(),         collection="langchain_demo",         sync=True     )          history.add_user_message("hi!")     history.add_ai_message("whats up?")          print(history.messages)  # noqa: T201     

Constructs a new RocksetChatMessageHistory.

Parameters:     

  * **session\_id** \(_-_\) – The ID of the chat session

  * **client** \(_-_\) – The RocksetClient object to use to query

  * **collection** \(_-_\) – The name of the collection to use to store chat messages. If a collection with the given name does not exist in the workspace, it is created.

  * **workspace** \(_-_\) – The workspace containing collection. Defaults to “commons”

  * **messages\_key** \(_-_\) – The DB column containing message history. Defaults to “messages”

  * **sync** \(_-_\) – Whether to wait for messages to be added. Defaults to False. NOTE: setting this to True will slow down performance.

  * **message\_uuid\_method** \(_-_\) – The method that generates message IDs. If set, all messages will have an id field within the additional\_kwargs property. If this param is not set and sync is False, message IDs will not be created. If this param is not set and sync is True, the uuid.uuid4 method will be used to create message IDs.

Attributes

`ADD_TIMEOUT_MS` |    ---|---   `CREATE_TIMEOUT_MS` |    `SLEEP_INTERVAL_MS` |    `messages` | Messages in this chat history.      Methods

`__init__`\(session\_id, client, collection\[, ...\]\) | Constructs a new RocksetChatMessageHistory.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the history.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Removes all messages from the chat history      \_\_init\_\_\(

    _session\_id: str_,     _client: ~typing.Any_,     _collection: str_,     _workspace: str = 'commons'_,     _messages\_key: str = 'messages'_,     _sync: bool = False_,     _message\_uuid\_method: ~typing.Callable\[\[\]_,     _str | int\] = <function RocksetChatMessageHistory.<lambda>>_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/rocksetdb.html#RocksetChatMessageHistory.__init__)\#     

Constructs a new RocksetChatMessageHistory.

Parameters:     

  * **session\_id** \(_-_\) – The ID of the chat session

  * **client** \(_-_\) – The RocksetClient object to use to query

  * **collection** \(_-_\) – The name of the collection to use to store chat messages. If a collection with the given name does not exist in the workspace, it is created.

  * **workspace** \(_-_\) – The workspace containing collection. Defaults to “commons”

  * **messages\_key** \(_-_\) – The DB column containing message history. Defaults to “messages”

  * **sync** \(_-_\) – Whether to wait for messages to be added. Defaults to False. NOTE: setting this to True will slow down performance.

  * **message\_uuid\_method** \(_-_\) – The method that generates message IDs. If set, all messages will have an id field within the additional\_kwargs property. If this param is not set and sync is False, message IDs will not be created. If this param is not set and sync is True, the uuid.uuid4 method will be used to create message IDs.

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/rocksetdb.html#RocksetChatMessageHistory.add_message)\#     

Add a Message object to the history.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A BaseMessage object to store.

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/rocksetdb.html#RocksetChatMessageHistory.clear)\#     

Removes all messages from the chat history

Return type:     

None

Examples using RocksetChatMessageHistory

  * [Rockset](https://python.langchain.com/docs/integrations/providers/rockset/)

__On this page