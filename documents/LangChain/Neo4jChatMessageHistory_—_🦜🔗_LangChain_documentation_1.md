# Neo4jChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/neo4j/chat_message_histories/langchain_neo4j.chat_message_histories.neo4j.Neo4jChatMessageHistory.html
**Word Count:** 278
**Links Count:** 120
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# Neo4jChatMessageHistory\#

_class _langchain\_neo4j.chat\_message\_histories.neo4j.Neo4jChatMessageHistory\(

    _session\_id : str | int_,     _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _database : str = 'neo4j'_,     _node\_label : str = 'Session'_,     _window : int = 3_,     _\*_ ,     _graph : [Neo4jGraph](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html#langchain_neo4j.graphs.neo4j_graph.Neo4jGraph "langchain_neo4j.graphs.neo4j_graph.Neo4jGraph") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chat_message_histories/neo4j.html#Neo4jChatMessageHistory)\#     

Chat message history stored in a Neo4j database.

Attributes

`messages` | Retrieve the messages from Neo4j   ---|---      Methods

`__init__`\(session\_id\[, url, username, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Async add a list of messages.   `aclear`\(\) | Async remove all messages from the store.   `add_ai_message`\(message\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\) | Append the message to the record in Neo4j   `add_messages`\(messages\) | Add a list of messages.   `add_user_message`\(message\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\[delete\_session\_node\]\) | Clear session memory from Neo4j      Parameters:     

  * **session\_id** \(_str_ _|__int_\)

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **database** \(_str_\)

  * **node\_label** \(_str_\)

  * **window** \(_int_\)

  * **graph** \([_Neo4jGraph_](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html#langchain_neo4j.graphs.neo4j_graph.Neo4jGraph "langchain_neo4j.graphs.neo4j_graph.Neo4jGraph") _|__None_\)

\_\_init\_\_\(

    _session\_id : str | int_,     _url : str | None = None_,     _username : str | None = None_,     _password : str | None = None_,     _database : str = 'neo4j'_,     _node\_label : str = 'Session'_,     _window : int = 3_,     _\*_ ,     _graph : [Neo4jGraph](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html#langchain_neo4j.graphs.neo4j_graph.Neo4jGraph "langchain_neo4j.graphs.neo4j_graph.Neo4jGraph") | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chat_message_histories/neo4j.html#Neo4jChatMessageHistory.__init__)\#     

Parameters:     

  * **session\_id** \(_str_ _|__int_\)

  * **url** \(_str_ _|__None_\)

  * **username** \(_str_ _|__None_\)

  * **password** \(_str_ _|__None_\)

  * **database** \(_str_\)

  * **node\_label** \(_str_\)

  * **window** \(_int_\)

  * **graph** \([_Neo4jGraph_](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.neo4j_graph.Neo4jGraph.html#langchain_neo4j.graphs.neo4j_graph.Neo4jGraph "langchain_neo4j.graphs.neo4j_graph.Neo4jGraph") _|__None_\)

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

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chat_message_histories/neo4j.html#Neo4jChatMessageHistory.add_message)\#     

Append the message to the record in Neo4j

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

clear\(

    _delete\_session\_node : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_neo4j/chat_message_histories/neo4j.html#Neo4jChatMessageHistory.clear)\#     

Clear session memory from Neo4j

Parameters:     

**delete\_session\_node** \(_bool_\) – Whether to delete the session node. Defaults to False.

Return type:     

None

Examples using Neo4jChatMessageHistory

  * [Neo4j](https://python.langchain.com/docs/integrations/memory/neo4j_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)