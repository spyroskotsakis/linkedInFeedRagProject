# AstraDBChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/astradb/chat_message_histories/langchain_astradb.chat_message_histories.AstraDBChatMessageHistory.html
**Word Count:** 828
**Links Count:** 124
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# AstraDBChatMessageHistory\#

_class _langchain\_astradb.chat\_message\_histories.AstraDBChatMessageHistory\(

    _\*_ ,     _session\_id : str_,     _collection\_name : str = 'langchain\_message\_store'_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory)\#     

Chat message history that stores history in Astra DB.

Parameters:     

  * **session\_id** \(_str_\) – arbitrary key that is used to store the messages of a single chat session.

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Attributes

`messages` | Retrieve all session messages from DB.   ---|---      Methods

`__init__`\(\*, session\_id\[, collection\_name, ...\]\) | Chat message history that stores history in Astra DB.   ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the store.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Remove all messages from the store.      \_\_init\_\_\(

    _\*_ ,     _session\_id : str_,     _collection\_name : str = 'langchain\_message\_store'_,     _token : str | TokenProvider | None = None_,     _api\_endpoint : str | None = None_,     _namespace : str | None = None_,     _environment : str | None = None_,     _setup\_mode : [SetupMode](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode") = SetupMode.SYNC_,     _pre\_delete\_collection : bool = False_,     _ext\_callers : list\[tuple\[str | None, str | None\] | str | None\] | None = None_,     _api\_options : APIOptions | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory.__init__)\#     

Chat message history that stores history in Astra DB.

Parameters:     

  * **session\_id** \(_str_\) – arbitrary key that is used to store the messages of a single chat session.

  * **collection\_name** \(_str_\) – name of the Astra DB collection to create/use.

  * **token** \(_str_ _|__TokenProvider_ _|__None_\) – API token for Astra DB usage, either in the form of a string or a subclass of astrapy.authentication.TokenProvider. If not provided, the environment variable ASTRA\_DB\_APPLICATION\_TOKEN is inspected.

  * **api\_endpoint** \(_str_ _|__None_\) – full URL to the API endpoint, such as https://<DB-ID>-us-east1.apps.astra.datastax.com. If not provided, the environment variable ASTRA\_DB\_API\_ENDPOINT is inspected.

  * **namespace** \(_str_ _|__None_\) – namespace \(aka keyspace\) where the collection is created. If not provided, the environment variable ASTRA\_DB\_KEYSPACE is inspected. Defaults to the database’s “default namespace”.

  * **environment** \(_str_ _|__None_\) – a string specifying the environment of the target Data API. If omitted, defaults to “prod” \(Astra DB production\). Other values are in astrapy.constants.Environment enum class.

  * **setup\_mode** \([_SetupMode_](https://python.langchain.com/api_reference/astradb/utils/langchain_astradb.utils.astradb.SetupMode.html#langchain_astradb.utils.astradb.SetupMode "langchain_astradb.utils.astradb.SetupMode")\) – mode used to create the Astra DB collection \(SYNC, ASYNC or OFF\).

  * **pre\_delete\_collection** \(_bool_\) – whether to delete the collection before creating it. If False and the collection already exists, the collection will be used as is.

  * **ext\_callers** \(_list_ _\[__tuple_ _\[__str_ _|__None_ _,__str_ _|__None_ _\]__|__str_ _|__None_ _\]__|__None_\) – one or more caller identities to identify Data API calls in the User-Agent header. This is a list of \(name, version\) pairs, or just strings if no version info is provided, which, if supplied, becomes the leading part of the User-Agent string in all API requests related to this component.

  * **api\_options** \(_APIOptions_ _|__None_\) – an instance of `astrapy.utils.api_options.APIOptions` that can be supplied to customize the interaction with the Data API regarding serialization/deserialization, timeouts, custom headers and so on. The provided options are applied on top of settings already tailored to this library, and if specified will take precedence. Passing None \(default\) means no customization is requested. Refer to the astrapy documentation for details.

Return type:     

None

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory.aadd_messages)\#     

Async add a list of messages.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory.aclear)\#     

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None\#     

Add a Message object to the store.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A BaseMessage object to store.

Raises:     

**NotImplementedError** – If the sub-class has not implemented an efficient add\_messages method.

Return type:     

None

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory.add_messages)\#     

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

_async _aget\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory.aget_messages)\#     

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence layer.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_astradb/chat_message_histories.html#AstraDBChatMessageHistory.clear)\#     

Remove all messages from the store.

Return type:     

None

Examples using AstraDBChatMessageHistory

  * [Astra DB ](https://python.langchain.com/docs/integrations/memory/astradb_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)