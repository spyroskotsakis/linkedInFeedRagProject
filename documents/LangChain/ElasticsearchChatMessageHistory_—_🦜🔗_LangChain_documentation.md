# ElasticsearchChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.elasticsearch.ElasticsearchChatMessageHistory.html
**Word Count:** 359
**Links Count:** 179
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# ElasticsearchChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.elasticsearch.ElasticsearchChatMessageHistory\(

    _index : str_,     _session\_id : str_,     _\*_ ,     _es\_connection : Elasticsearch | None = None_,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _ensure\_ascii : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/elasticsearch.html#ElasticsearchChatMessageHistory)\#     

Deprecated since version 0.0.27: Use `Use langchain-elasticsearch package` instead.

Chat message history that stores history in Elasticsearch.

Parameters:     

  * **es\_url** \(_str_ _|__None_\) – URL of the Elasticsearch instance to connect to.

  * **es\_cloud\_id** \(_str_ _|__None_\) – Cloud ID of the Elasticsearch instance to connect to.

  * **es\_user** \(_str_ _|__None_\) – Username to use when connecting to Elasticsearch.

  * **es\_password** \(_str_ _|__None_\) – Password to use when connecting to Elasticsearch.

  * **es\_api\_key** \(_str_ _|__None_\) – API key to use when connecting to Elasticsearch.

  * **es\_connection** \(_Elasticsearch_ _|__None_\) – Optional pre-existing Elasticsearch connection.

  * **ensure\_ascii** \(_bool_ _|__None_\) – Used to escape ASCII symbols in json.dumps. Defaults to True.

  * **index** \(_str_\) – Name of the index to use.

  * **session\_id** \(_str_\) – Arbitrary key that is used to store the messages of a single chat session.

Attributes

`messages` | Retrieve the messages from Elasticsearch   ---|---      Methods

`__init__`\(index, session\_id, \*\[, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a message to the chat session in Elasticsearch   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory in Elasticsearch   `connect_to_elasticsearch`\(\*\[, es\_url, ...\]\) |    `get_user_agent`\(\) |       \_\_init\_\_\(

    _index : str_,     _session\_id : str_,     _\*_ ,     _es\_connection : Elasticsearch | None = None_,     _es\_url : str | None = None_,     _es\_cloud\_id : str | None = None_,     _es\_user : str | None = None_,     _es\_api\_key : str | None = None_,     _es\_password : str | None = None_,     _ensure\_ascii : bool | None = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/elasticsearch.html#ElasticsearchChatMessageHistory.__init__)\#     

Parameters:     

  * **index** \(_str_\)

  * **session\_id** \(_str_\)

  * **es\_connection** \(_Elasticsearch_ _|__None_\)

  * **es\_url** \(_str_ _|__None_\)

  * **es\_cloud\_id** \(_str_ _|__None_\)

  * **es\_user** \(_str_ _|__None_\)

  * **es\_api\_key** \(_str_ _|__None_\)

  * **es\_password** \(_str_ _|__None_\)

  * **ensure\_ascii** \(_bool_ _|__None_\)

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/elasticsearch.html#ElasticsearchChatMessageHistory.add_message)\#     

Add a message to the chat session in Elasticsearch

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/elasticsearch.html#ElasticsearchChatMessageHistory.clear)\#     

Clear session memory in Elasticsearch

Return type:     

None

_static _connect\_to\_elasticsearch\(

    _\*_ ,     _es\_url : str | None = None_,     _cloud\_id : str | None = None_,     _api\_key : str | None = None_,     _username : str | None = None_,     _password : str | None = None_, \) → Elasticsearch[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/elasticsearch.html#ElasticsearchChatMessageHistory.connect_to_elasticsearch)\#     

Parameters:     

  * **es\_url** \(_str_ _|__None_\)

  * **cloud\_id** \(_str_ _|__None_\)

  * **api\_key** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

Return type:     

Elasticsearch

_static _get\_user\_agent\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/elasticsearch.html#ElasticsearchChatMessageHistory.get_user_agent)\#     

Return type:     

str

Examples using ElasticsearchChatMessageHistory

  * [Elasticsearch](https://python.langchain.com/docs/integrations/memory/elasticsearch_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)