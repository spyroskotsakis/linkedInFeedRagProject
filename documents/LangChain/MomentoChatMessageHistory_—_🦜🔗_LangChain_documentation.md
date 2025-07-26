# MomentoChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.momento.MomentoChatMessageHistory.html
**Word Count:** 531
**Links Count:** 181
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# MomentoChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.momento.MomentoChatMessageHistory\(

    _session\_id : str_,     _cache\_client : momento.CacheClient_,     _cache\_name : str_,     _\*_ ,     _key\_prefix : str = 'message\_store:'_,     _ttl : timedelta | None = None_,     _ensure\_cache\_exists : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/momento.html#MomentoChatMessageHistory)\#     

Chat message history cache that uses Momento as a backend.

See <https://gomomento.com/>

Instantiate a chat message history cache that uses Momento as a backend.

Note: to instantiate the cache client passed to MomentoChatMessageHistory, you must have a Momento account at <https://gomomento.com/>.

Parameters:     

  * **session\_id** \(_str_\) – The session ID to use for this chat session.

  * **cache\_client** \(_CacheClient_\) – The Momento cache client.

  * **cache\_name** \(_str_\) – The name of the cache to use to store the messages.

  * **key\_prefix** \(_str_ _,__optional_\) – The prefix to apply to the cache key. Defaults to “message\_store:”.

  * **ttl** \(_Optional_ _\[__timedelta_ _\]__,__optional_\) – The TTL to use for the messages. Defaults to None, ie the default TTL of the cache will be used.

  * **ensure\_cache\_exists** \(_bool_ _,__optional_\) – Create the cache if it doesn’t exist. Defaults to True.

Raises:     

  * **ImportError** – Momento python package is not installed.

  * **TypeError** – cache\_client is not of type momento.CacheClientObject

Attributes

`messages` | Retrieve the messages from Momento.   ---|---      Methods

`__init__`\(session\_id, cache\_client, cache\_name, \*\) | Instantiate a chat message history cache that uses Momento as a backend.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Store a message in the cache.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Remove the session's messages from the cache.   `from_client_params`\(session\_id, cache\_name, ...\) | Construct cache from CacheClient parameters.      \_\_init\_\_\(

    _session\_id : str_,     _cache\_client : momento.CacheClient_,     _cache\_name : str_,     _\*_ ,     _key\_prefix : str = 'message\_store:'_,     _ttl : timedelta | None = None_,     _ensure\_cache\_exists : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/momento.html#MomentoChatMessageHistory.__init__)\#     

Instantiate a chat message history cache that uses Momento as a backend.

Note: to instantiate the cache client passed to MomentoChatMessageHistory, you must have a Momento account at <https://gomomento.com/>.

Parameters:     

  * **session\_id** \(_str_\) – The session ID to use for this chat session.

  * **cache\_client** \(_CacheClient_\) – The Momento cache client.

  * **cache\_name** \(_str_\) – The name of the cache to use to store the messages.

  * **key\_prefix** \(_str_ _,__optional_\) – The prefix to apply to the cache key. Defaults to “message\_store:”.

  * **ttl** \(_Optional_ _\[__timedelta_ _\]__,__optional_\) – The TTL to use for the messages. Defaults to None, ie the default TTL of the cache will be used.

  * **ensure\_cache\_exists** \(_bool_ _,__optional_\) – Create the cache if it doesn’t exist. Defaults to True.

Raises:     

  * **ImportError** – Momento python package is not installed.

  * **TypeError** – cache\_client is not of type momento.CacheClientObject

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/momento.html#MomentoChatMessageHistory.add_message)\#     

Store a message in the cache.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – The message object to store.

Raises:     

  * **SdkException** – Momento service or network error.

  * **Exception** – Unexpected response.

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/momento.html#MomentoChatMessageHistory.clear)\#     

Remove the session’s messages from the cache.

Raises:     

  * **SdkException** – Momento service or network error.

  * **Exception** – Unexpected response.

Return type:     

None

_classmethod _from\_client\_params\(

    _session\_id : str_,     _cache\_name : str_,     _ttl : timedelta_,     _\*_ ,     _configuration : momento.config.Configuration | None = None_,     _api\_key : str | None = None_,     _auth\_token : str | None = None_,     _\*\* kwargs: Any_, \) → MomentoChatMessageHistory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/momento.html#MomentoChatMessageHistory.from_client_params)\#     

Construct cache from CacheClient parameters.

Parameters:     

  * **session\_id** \(_str_\)

  * **cache\_name** \(_str_\)

  * **ttl** \(_timedelta_\)

  * **configuration** \(_Optional_ _\[__momento.config.Configuration_ _\]_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **auth\_token** \(_Optional_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

MomentoChatMessageHistory

Examples using MomentoChatMessageHistory

  * [Momento](https://python.langchain.com/docs/integrations/providers/momento/)

  * [Momento Cache](https://python.langchain.com/docs/integrations/memory/momento_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)