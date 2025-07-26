# DynamoDBChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.dynamodb.DynamoDBChatMessageHistory.html
**Word Count:** 505
**Links Count:** 173
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# DynamoDBChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.dynamodb.DynamoDBChatMessageHistory\(

    _table\_name : str_,     _session\_id : str_,     _endpoint\_url : str | None = None_,     _primary\_key\_name : str = 'SessionId'_,     _key : Dict\[str, str\] | None = None_,     _boto3\_session : Session | None = None_,     _kms\_key\_id : str | None = None_,     _ttl : int | None = None_,     _ttl\_key\_name : str = 'expireAt'_,     _history\_size : int | None = None_,     _history\_messages\_key : str | None = 'History'_,     _\*_ ,     _coerce\_float\_to\_decimal : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/dynamodb.html#DynamoDBChatMessageHistory)\#     

Chat message history that stores history in AWS DynamoDB.

This class expects that a DynamoDB table exists with name table\_name

Parameters:     

  * **table\_name** \(_str_\) – name of the DynamoDB table

  * **session\_id** \(_str_\) – arbitrary key that is used to store the messages of a single chat session.

  * **endpoint\_url** \(_Optional_ _\[__str_ _\]_\) – URL of the AWS endpoint to connect to. This argument is optional and useful for test purposes, like using Localstack. If you plan to use AWS cloud service, you normally don’t have to worry about setting the endpoint\_url.

  * **primary\_key\_name** \(_str_\) – name of the primary key of the DynamoDB table. This argument is optional, defaulting to “SessionId”.

  * **key** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\) – an optional dictionary with a custom primary and secondary key. This argument is optional, but useful when using composite dynamodb keys, or isolating records based off of application details such as a user id. This may also contain global and local secondary index keys.

  * **kms\_key\_id** \(_Optional_ _\[__str_ _\]_\) – an optional AWS KMS Key ID, AWS KMS Key ARN, or AWS KMS Alias for client-side encryption

  * **ttl** \(_Optional_ _\[__int_ _\]_\) – Optional Time-to-live \(TTL\) in seconds. Allows you to define a per-item expiration timestamp that indicates when an item can be deleted from the table. DynamoDB handles deletion of expired items without consuming write throughput. To enable this feature on the table, follow the \[AWS DynamoDB documentation\]\(<https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/time-to-live-ttl-how-to.html>\)

  * **history\_size** \(_Optional_ _\[__int_ _\]_\) – Maximum number of messages to store. If None then there is no limit. If not None then only the latest history\_size messages are stored.

  * **history\_messages\_key** \(_Optional_ _\[__str_ _\]_\) – Key for the chat history where the messages are stored and updated

  * **coerce\_float\_to\_decimal** \(_bool_\) – If True, all float values in the messages will be converted to Decimal.

  * **boto3\_session** \(_Optional_ _\[__Session_ _\]_\)

  * **ttl\_key\_name** \(_str_\)

Attributes

`messages` | Retrieve the messages from DynamoDB   ---|---      Methods

`__init__`\(table\_name, session\_id\[, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the store.   `add_messages`\(messages\) | Append the message to the record in DynamoDB   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory from DynamoDB      \_\_init\_\_\(

    _table\_name : str_,     _session\_id : str_,     _endpoint\_url : str | None = None_,     _primary\_key\_name : str = 'SessionId'_,     _key : Dict\[str, str\] | None = None_,     _boto3\_session : Session | None = None_,     _kms\_key\_id : str | None = None_,     _ttl : int | None = None_,     _ttl\_key\_name : str = 'expireAt'_,     _history\_size : int | None = None_,     _history\_messages\_key : str | None = 'History'_,     _\*_ ,     _coerce\_float\_to\_decimal : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/dynamodb.html#DynamoDBChatMessageHistory.__init__)\#     

Parameters:     

  * **table\_name** \(_str_\)

  * **session\_id** \(_str_\)

  * **endpoint\_url** \(_Optional_ _\[__str_ _\]_\)

  * **primary\_key\_name** \(_str_\)

  * **key** \(_Optional_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]_\)

  * **boto3\_session** \(_Optional_ _\[__Session_ _\]_\)

  * **kms\_key\_id** \(_Optional_ _\[__str_ _\]_\)

  * **ttl** \(_Optional_ _\[__int_ _\]_\)

  * **ttl\_key\_name** \(_str_\)

  * **history\_size** \(_Optional_ _\[__int_ _\]_\)

  * **history\_messages\_key** \(_Optional_ _\[__str_ _\]_\)

  * **coerce\_float\_to\_decimal** \(_bool_\)

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

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/dynamodb.html#DynamoDBChatMessageHistory.add_messages)\#     

Append the message to the record in DynamoDB

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

_async _aget\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence layer.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/dynamodb.html#DynamoDBChatMessageHistory.clear)\#     

Clear session memory from DynamoDB

Return type:     

None

Examples using DynamoDBChatMessageHistory

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [AWS DynamoDB](https://python.langchain.com/docs/integrations/memory/aws_dynamodb/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)