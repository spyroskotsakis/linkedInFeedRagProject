# BaseChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/chat_history/langchain_core.chat_history.BaseChatMessageHistory.html
**Word Count:** 427
**Links Count:** 149
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# BaseChatMessageHistory\#

_class _langchain\_core.chat\_history.BaseChatMessageHistory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory)\#     

Abstract base class for storing chat message history.

Implementations guidelines:

Implementations are expected to over-ride all or some of the following methods:

  * add\_messages: sync variant for bulk addition of messages

  * aadd\_messages: async variant for bulk addition of messages

  * messages: sync variant for getting messages

  * aget\_messages: async variant for getting messages

  * clear: sync variant for clearing messages

  * aclear: async variant for clearing messages

add\_messages contains a default implementation that calls add\_message for each message in the sequence. This is provided for backwards compatibility with existing implementations which only had add\_message.

Async variants all have default implementations that call the sync variants. Implementers can choose to over-ride the async implementations to provide truly async implementations.

Usage guidelines:

When used for updating history, users should favor usage of add\_messages over add\_message or other variants like add\_user\_message and add\_ai\_message to avoid unnecessary round-trips to the underlying persistence layer.

Example: Shows a default implementation.

>  >     class FileChatMessageHistory(BaseChatMessageHistory): >         storage_path: str >         session_id: str >      >         @property >         def messages(self): >             with open( >                 os.path.join(storage_path, session_id), >                 "r", >                 encoding="utf-8", >             ) as f: >                 messages = json.loads(f.read()) >             return messages_from_dict(messages) >      >         def add_messages(self, messages: Sequence[BaseMessage]) -> None: >             all_messages = list(self.messages)  # Existing messages >             all_messages.extend(messages)  # Add new messages >      >             serialized = [message_to_dict(message) for message in all_messages] >             # Can be further optimized by only writing new messages >             # using append mode. >             with open(os.path.join(storage_path, session_id), "w") as f: >                 json.dump(messages, f) >      >         def clear(self): >             with open(os.path.join(storage_path, session_id), "w") as f: >                 f.write("[]") >     

Attributes

Methods

`aadd_messages`\(messages\) | Async add a list of messages.   ---|---   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Add a Message object to the store.   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Remove all messages from the store.      _async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.aadd_messages)\#     

Async add a list of messages.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.aclear)\#     

Async remove all messages from the store.

Return type:     

None

add\_ai\_message\(

    _message : [AIMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage") | str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.add_ai_message)\#     

Convenience method for adding an AI message string to the store.

Please note that this is a convenience method. Code should favor the bulk add\_messages interface instead to save on round-trips to the underlying persistence layer.

This method may be deprecated in a future release.

Parameters:     

**message** \([_AIMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html#langchain_core.messages.ai.AIMessage "langchain_core.messages.ai.AIMessage") _|__str_\) – The AI message to add.

Return type:     

None

add\_message\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.add_message)\#     

Add a Message object to the store.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – A BaseMessage object to store.

Raises:     

**NotImplementedError** – If the sub-class has not implemented an efficient add\_messages method.

Return type:     

None

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.add_messages)\#     

Add a list of messages.

Implementations should over-ride this method to handle bulk addition of messages in an efficient manner to avoid unnecessary round-trips to the underlying store.

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – A sequence of BaseMessage objects to store.

Return type:     

None

add\_user\_message\(

    _message : [HumanMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html#langchain_core.messages.human.HumanMessage "langchain_core.messages.human.HumanMessage") | str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.add_user_message)\#     

Convenience method for adding a human message string to the store.

Please note that this is a convenience method. Code should favor the bulk add\_messages interface instead to save on round-trips to the underlying persistence layer.

This method may be deprecated in a future release.

Parameters:     

**message** \([_HumanMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html#langchain_core.messages.human.HumanMessage "langchain_core.messages.human.HumanMessage") _|__str_\) – The human message to add to the store.

Return type:     

None

_async _aget\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.aget_messages)\#     

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence layer.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

_abstractmethod _clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_history.html#BaseChatMessageHistory.clear)\#     

Remove all messages from the store.

Return type:     

None

Examples using BaseChatMessageHistory

  * [\# Legacy](https://python.langchain.com/docs/versions/migrating_chains/conversation_chain/)

  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

__On this page