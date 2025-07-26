# XataChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.xata.XataChatMessageHistory.html
**Word Count:** 272
**Links Count:** 171
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# XataChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.xata.XataChatMessageHistory\(

    _session\_id : str_,     _db\_url : str_,     _api\_key : str_,     _branch\_name : str = 'main'_,     _table\_name : str = 'messages'_,     _create\_table : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/xata.html#XataChatMessageHistory)\#     

Chat message history stored in a Xata database.

Initialize with Xata client.

Attributes

`messages` |    ---|---      Methods

`__init__`\(session\_id, db\_url, api\_key\[, ...\]\) | Initialize with Xata client.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Append the message to the Xata table   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Delete session from Xata table.      Parameters:     

  * **session\_id** \(_str_\)

  * **db\_url** \(_str_\)

  * **api\_key** \(_str_\)

  * **branch\_name** \(_str_\)

  * **table\_name** \(_str_\)

  * **create\_table** \(_bool_\)

\_\_init\_\_\(

    _session\_id : str_,     _db\_url : str_,     _api\_key : str_,     _branch\_name : str = 'main'_,     _table\_name : str = 'messages'_,     _create\_table : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/xata.html#XataChatMessageHistory.__init__)\#     

Initialize with Xata client.

Parameters:     

  * **session\_id** \(_str_\)

  * **db\_url** \(_str_\)

  * **api\_key** \(_str_\)

  * **branch\_name** \(_str_\)

  * **table\_name** \(_str_\)

  * **create\_table** \(_bool_\)

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/xata.html#XataChatMessageHistory.add_message)\#     

Append the message to the Xata table

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/xata.html#XataChatMessageHistory.clear)\#     

Delete session from Xata table.

Return type:     

None

Examples using XataChatMessageHistory

  * [Xata](https://python.langchain.com/docs/integrations/providers/xata/)

__On this page