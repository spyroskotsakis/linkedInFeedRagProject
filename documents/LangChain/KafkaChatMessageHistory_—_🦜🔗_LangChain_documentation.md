# KafkaChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.kafka.KafkaChatMessageHistory.html
**Word Count:** 675
**Links Count:** 197
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# KafkaChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.kafka.KafkaChatMessageHistory\(

    _session\_id : str_,     _bootstrap\_servers : str_,     _ttl\_ms : int = 604800000_,     _replication\_factor : int = 1_,     _partition : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory)\#     

Chat message history stored in Kafka.

Setup:     

Install `confluent-kafka-python`.               pip install confluent_kafka     

Instantiate:                    from langchain_community.chat_message_histories import KafkaChatMessageHistory          history = KafkaChatMessageHistory(         session_id="your_session_id",         bootstrap_servers="host:port",     )     

Add and retrieve messages:                    # Add messages     history.add_messages([message1, message2, message3, ...])          # Retrieve messages     message_batch_0 = history.messages          # retrieve messages after message_batch_0     message_batch_1 = history.messages          # Reset to beginning and retrieve messages     messages_from_beginning = history.messages_from_beginning()     

Retrieving messages is stateful. Internally, it uses Kafka consumer to read. The consumed offset is maintained persistently.

To retrieve messages, you can use the following methods: \- messages:

> continue consuming chat messages from last one.

  * messages\_from\_beginning:     

reset the consumer to the beginning of the chat history and return messages. Optional parameters: 1\. max\_message\_count: maximum number of messages to return. 2\. max\_time\_sec: maximum time in seconds to wait for messages.

  * messages\_from\_latest:     

reset to end of the chat history and try consuming messages. Optional parameters same as above.

  * messages\_from\_last\_consumed:     

continuing from the last consumed message, similar to messages. Optional parameters same as above.

max\_message\_count and max\_time\_sec are used to avoid blocking indefinitely     

when retrieving messages. As a result, the method to retrieve messages may not return all messages. Change max\_message\_count and max\_time\_sec to retrieve all history messages.

Parameters:     

  * **session\_id** \(_str_\) – The ID for single chat session. It is used as Kafka topic name.

  * **bootstrap\_servers** \(_str_\) – Comma-separated host/port pairs to establish connection to Kafka cluster <https://kafka.apache.org/documentation.html#adminclientconfigs_bootstrap.servers>

  * **ttl\_ms** \(_int_\) – Time-to-live \(milliseconds\) for automatic expiration of entries. Default 7 days. -1 for no expiration. It translates to <https://kafka.apache.org/documentation.html#topicconfigs_retention.ms>

  * **replication\_factor** \(_int_\) – The replication factor for the topic. Default 1.

  * **partition** \(_int_\) – The number of partitions for the topic. Default 3.

Attributes

`messages` | Retrieve the messages for the session, from Kafka topic continuously from last consumed message.   ---|---      Methods

`__init__`\(session\_id, bootstrap\_servers\[, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the store.   `add_messages`\(messages\[, flush\_timeout\_seconds\]\) | Add messages to the chat history by producing to the Kafka topic.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear the chat history by deleting the Kafka topic.   `close`\(\) | Release the resources.   `messages_from_beginning`\(\[max\_message\_count, ...\]\) | Retrieve messages from Kafka topic from the beginning.   `messages_from_last_consumed`\(\[...\]\) | Retrieve messages from Kafka topic from the last consumed message.   `messages_from_latest`\(\[max\_message\_count, ...\]\) | Reset to the end offset.      \_\_init\_\_\(

    _session\_id : str_,     _bootstrap\_servers : str_,     _ttl\_ms : int = 604800000_,     _replication\_factor : int = 1_,     _partition : int = 3_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.__init__)\#     

Parameters:     

  * **session\_id** \(_str_\) – The ID for single chat session. It is used as Kafka topic name.

  * **bootstrap\_servers** \(_str_\) – Comma-separated host/port pairs to establish connection to Kafka cluster <https://kafka.apache.org/documentation.html#adminclientconfigs_bootstrap.servers>

  * **ttl\_ms** \(_int_\) – Time-to-live \(milliseconds\) for automatic expiration of entries. Default 7 days. -1 for no expiration. It translates to <https://kafka.apache.org/documentation.html#topicconfigs_retention.ms>

  * **replication\_factor** \(_int_\) – The replication factor for the topic. Default 1.

  * **partition** \(_int_\) – The number of partitions for the topic. Default 3.

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None\#     

Add a Message object to the store.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A BaseMessage object to store.

Raises:     

**NotImplementedError** – If the sub-class has not implemented an efficient add\_messages method.

Return type:     

None

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _flush\_timeout\_seconds : float = 5.0_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.add_messages)\#     

Add messages to the chat history by producing to the Kafka topic.

Parameters:     

  * **messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

  * **flush\_timeout\_seconds** \(_float_\)

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

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.clear)\#     

Clear the chat history by deleting the Kafka topic.

Return type:     

None

close\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.close)\#     

Release the resources. Nothing to be released at this moment.

Return type:     

None

messages\_from\_beginning\(

    _max\_message\_count : int | None = 5_,     _max\_time\_sec : float | None = 5.0_, \) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.messages_from_beginning)\#     

Retrieve messages from Kafka topic from the beginning. This method resets the consumer to the beginning and consumes messages.

> Args: >      >  > max\_message\_count: Maximum number of messages to consume. max\_time\_sec: Time limit in seconds to consume messages. >  > Returns: >      >  > List of messages.

Parameters:     

  * **max\_message\_count** \(_int_ _|__None_\)

  * **max\_time\_sec** \(_float_ _|__None_\)

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

messages\_from\_last\_consumed\(

    _max\_message\_count : int | None = 5_,     _max\_time\_sec : float | None = 5.0_, \) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.messages_from_last_consumed)\#     

Retrieve messages from Kafka topic from the last consumed message. Please note this method is stateful. Internally, it uses Kafka consumer to consume messages, and maintains the commit offset.

> Args: >      >  > max\_message\_count: Maximum number of messages to consume. max\_time\_sec: Time limit in seconds to consume messages. >  > Returns: >      >  > List of messages.

Parameters:     

  * **max\_message\_count** \(_int_ _|__None_\)

  * **max\_time\_sec** \(_float_ _|__None_\)

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

messages\_from\_latest\(

    _max\_message\_count : int | None = 5_,     _max\_time\_sec : float | None = 5.0_, \) → List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/kafka.html#KafkaChatMessageHistory.messages_from_latest)\#     

Reset to the end offset. Try to consume messages if available.

Parameters:     

  * **max\_message\_count** \(_int_ _|__None_\) – Maximum number of messages to consume.

  * **max\_time\_sec** \(_float_ _|__None_\) – Time limit in seconds to consume messages.

Returns:     

List of messages.

Return type:     

_List_\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

Examples using KafkaChatMessageHistory

  * [Kafka](https://python.langchain.com/docs/integrations/memory/kafka_chat_message_history/)

__On this page