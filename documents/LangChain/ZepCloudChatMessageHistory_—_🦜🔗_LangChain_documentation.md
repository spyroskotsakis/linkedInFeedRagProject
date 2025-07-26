# ZepCloudChatMessageHistory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.zep_cloud.ZepCloudChatMessageHistory.html
**Word Count:** 359
**Links Count:** 183
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# ZepCloudChatMessageHistory\#

_class _langchain\_community.chat\_message\_histories.zep\_cloud.ZepCloudChatMessageHistory\(

    _session\_id : str_,     _api\_key : str_,     _\*_ ,     _memory\_type : MemoryGetRequestMemoryType | None = None_,     _lastn : int | None = None_,     _ai\_prefix : str | None = None_,     _human\_prefix : str | None = None_,     _summary\_instruction : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory)\#     

Chat message history that uses Zep Cloud as a backend.

Recommended usage:               # Set up Zep Chat History     zep_chat_history = ZepChatMessageHistory(         session_id=session_id,         api_key=<your_api_key>,     )          # Use a standard ConversationBufferMemory to encapsulate the Zep chat history     memory = ConversationBufferMemory(         memory_key="chat_history", chat_memory=zep_chat_history     )     

Zep - Recall, understand, and extract data from chat histories. Power personalized AI experiences.

Zep is a long-term memory service for AI Assistant apps. With Zep, you can provide AI assistants with the ability to recall past conversations, no matter how distant, while also reducing hallucinations, latency, and cost.

see Zep Cloud Docs: <https://help.getzep.com>

This class is a thin wrapper around the zep-python package. Additional Zep functionality is exposed via the zep\_summary, zep\_messages and zep\_facts properties.

For more information on the zep-python package, see: [getzep/zep-python](https://github.com/getzep/zep-python)

Attributes

`messages` | Retrieve messages from Zep memory   ---|---   `zep_facts` | Retrieve conversation facts from Zep memory   `zep_messages` | Retrieve summary from Zep memory   `zep_summary` | Retrieve summary from Zep memory      Methods

`__init__`\(session\_id, api\_key, \*\[, ...\]\) |    ---|---   `aadd_messages`\(messages\) | Append the messages to the Zep memory history asynchronously   `aclear`\(\) | Clear session memory from Zep asynchronously.   `add_ai_message`\(message\[, metadata\]\) | Convenience method for adding an AI message string to the store.   `add_message`\(message\[, metadata\]\) | Append the message to the Zep memory history   `add_messages`\(messages\) | Append the messages to the Zep memory history   `add_user_message`\(message\[, metadata\]\) | Convenience method for adding a human message string to the store.   `aget_messages`\(\) | Async version of getting messages.   `clear`\(\) | Clear session memory from Zep.   `search`\(query\[, metadata, search\_scope, ...\]\) | Search Zep memory for messages matching the query      Parameters:     

  * **session\_id** \(_str_\)

  * **api\_key** \(_str_\)

  * **memory\_type** \(_Optional_ _\[__MemoryGetRequestMemoryType_ _\]_\)

  * **lastn** \(_Optional_ _\[__int_ _\]_\)

  * **ai\_prefix** \(_Optional_ _\[__str_ _\]_\)

  * **human\_prefix** \(_Optional_ _\[__str_ _\]_\)

  * **summary\_instruction** \(_Optional_ _\[__str_ _\]_\)

\_\_init\_\_\(

    _session\_id : str_,     _api\_key : str_,     _\*_ ,     _memory\_type : MemoryGetRequestMemoryType | None = None_,     _lastn : int | None = None_,     _ai\_prefix : str | None = None_,     _human\_prefix : str | None = None_,     _summary\_instruction : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.__init__)\#     

Parameters:     

  * **session\_id** \(_str_\)

  * **api\_key** \(_str_\)

  * **memory\_type** \(_Optional_ _\[__MemoryGetRequestMemoryType_ _\]_\)

  * **lastn** \(_Optional_ _\[__int_ _\]_\)

  * **ai\_prefix** \(_Optional_ _\[__str_ _\]_\)

  * **human\_prefix** \(_Optional_ _\[__str_ _\]_\)

  * **summary\_instruction** \(_Optional_ _\[__str_ _\]_\)

Return type:     

None

_async _aadd\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.aadd_messages)\#     

Append the messages to the Zep memory history asynchronously

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

None

_async _aclear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.aclear)\#     

Clear session memory from Zep asynchronously. Note that Zep is long-term storage for memory and this is not advised unless you have specific data retention requirements.

Return type:     

None

add\_ai\_message\(

    _message : str_,     _metadata : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.add_ai_message)\#     

Convenience method for adding an AI message string to the store.

Parameters:     

  * **message** \(_str_\) – The string contents of an AI message.

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to attach to the message.

Return type:     

None

add\_message\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_,     _metadata : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.add_message)\#     

Append the message to the Zep memory history

Parameters:     

  * **message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

None

add\_messages\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.add_messages)\#     

Append the messages to the Zep memory history

Parameters:     

**messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\)

Return type:     

None

add\_user\_message\(

    _message : str_,     _metadata : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.add_user_message)\#     

Convenience method for adding a human message string to the store.

Parameters:     

  * **message** \(_str_\) – The string contents of a human message.

  * **metadata** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional metadata to attach to the message.

Return type:     

None

_async _aget\_messages\(\) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Async version of getting messages.

Can over-ride this method to provide an efficient async implementation.

In general, fetching messages may involve IO to the underlying persistence layer.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

clear\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.clear)\#     

Clear session memory from Zep. Note that Zep is long-term storage for memory and this is not advised unless you have specific data retention requirements.

Return type:     

None

search\(

    _query : str_,     _metadata : Dict | None = None_,     _search\_scope : [SearchScope](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope "langchain_community.retrievers.zep.SearchScope") = 'messages'_,     _search\_type : [SearchType](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.multi_vector.SearchType.html#langchain.retrievers.multi_vector.SearchType "langchain.retrievers.multi_vector.SearchType") = 'similarity'_,     _mmr\_lambda : float | None = None_,     _limit : int | None = None_, \) → List\[MemorySearchResult\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/zep_cloud.html#ZepCloudChatMessageHistory.search)\#     

Search Zep memory for messages matching the query

Parameters:     

  * **query** \(_str_\)

  * **metadata** \(_Optional_ _\[__Dict_ _\]_\)

  * **search\_scope** \([_SearchScope_](https://python.langchain.com/api_reference/community/retrievers/langchain_community.retrievers.zep.SearchScope.html#langchain_community.retrievers.zep.SearchScope "langchain_community.retrievers.zep.SearchScope")\)

  * **search\_type** \([_SearchType_](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.multi_vector.SearchType.html#langchain.retrievers.multi_vector.SearchType "langchain.retrievers.multi_vector.SearchType")\)

  * **mmr\_lambda** \(_Optional_ _\[__float_ _\]_\)

  * **limit** \(_Optional_ _\[__int_ _\]_\)

Return type:     

List\[MemorySearchResult\]

Examples using ZepCloudChatMessageHistory

  * [Zep](https://python.langchain.com/docs/integrations/providers/zep/)

  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)