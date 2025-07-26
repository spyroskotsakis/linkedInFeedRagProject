# AsyncElasticsearchChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/elasticsearch/chat_history/langchain_elasticsearch.chat_history.AsyncElasticsearchChatMessageHistory.html
**Word Count:** 263
**Links Count:** 129
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# AsyncElasticsearchChatMessageHistory\#

_class _langchain\_elasticsearch.chat\_history.AsyncElasticsearchChatMessageHistory\(

    _index : str_,     _session\_id : str_,     _\*_ ,     _es\_connection : AsyncElasticsearch | None = None_,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _esnsure\_ascii : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/chat_history.html#AsyncElasticsearchChatMessageHistory)\#     

Attributes

Methods

`__init__`\(index, session\_id, \*\[, ...\]\) |    ---|---   `aadd_message`\(message\) | Add messages to the chat session in Elasticsearch   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Clear session memory in Elasticsearch   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the store.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Retrieve the messages from Elasticsearch   `clear`\(\) | Remove all messages from the store.   `create_if_missing`\(\) |       Parameters:     

  * **index** \(_str_\)

  * **session\_id** \(_str_\)

  * **es\_connection** \(_AsyncElasticsearch_ _|__None_\)

  * **es\_url** \(_str_ _|__None_\)

  * **es\_cloud\_id** \(_str_ _|__None_\)

  * **es\_user** \(_str_ _|__None_\)

  * **es\_api\_key** \(_str_ _|__None_\)

  * **es\_password** \(_str_ _|__None_\)

  * **esnsure\_ascii** \(_bool_ _|__None_\)

\_\_init\_\_\(

    _index : str_,     _session\_id : str_,     _\*_ ,     _es\_connection : AsyncElasticsearch | None = None_,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _esnsure\_ascii : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/chat_history.html#AsyncElasticsearchChatMessageHistory.__init__)\#     

Parameters:     

  * **index** \(_str_\)

  * **session\_id** \(_str_\)

  * **es\_connection** \(_AsyncElasticsearch_ _|__None_\)

  * **es\_url** \(_str_ _|__None_\)

  * **es\_cloud\_id** \(_str_ _|__None_\)

  * **es\_user** \(_str_ _|__None_\)

  * **es\_api\_key** \(_str_ _|__None_\)

  * **es\_password** \(_str_ _|__None_\)

  * **esnsure\_ascii** \(_bool_ _|__None_\)

_async _aadd\_message\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/chat_history.html#AsyncElasticsearchChatMessageHistory.aadd_message)\#     

Add messages to the chat session in Elasticsearch

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

Return type:     

None

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/chat_history.html#AsyncElasticsearchChatMessageHistory.aadd_messages)\#     

Async add a list of messages.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/chat_history.html#AsyncElasticsearchChatMessageHistory.aclear)\#     

Clear session memory in Elasticsearch

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

_async _aget\_messages\(\) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/chat_history.html#AsyncElasticsearchChatMessageHistory.aget_messages)\#     

Retrieve the messages from Elasticsearch

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/chat_history.html#AsyncElasticsearchChatMessageHistory.clear)\#     

Remove all messages from the store.

Return type:     

None

_async _create\_if\_missing\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_elasticsearch/_async/chat_history.html#AsyncElasticsearchChatMessageHistory.create_if_missing)\#     

Return type:     

None

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)