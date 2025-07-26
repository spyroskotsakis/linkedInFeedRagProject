# LangSmithDatasetChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.langsmith.LangSmithDatasetChatLoader.html
**Word Count:** 157
**Links Count:** 130
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# LangSmithDatasetChatLoader\#

_class _langchain\_community.chat\_loaders.langsmith.LangSmithDatasetChatLoader\(

    _\*_ ,     _dataset\_name : str_,     _client : 'Client' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/langsmith.html#LangSmithDatasetChatLoader)\#     

Load chat sessions from a LangSmith dataset with the “chat” data type.

dataset\_name\#     

The name of the LangSmith dataset.

Type:     

str

client\#     

Instance of LangSmith client for fetching data.

Type:     

Client

Initialize a new LangSmithChatDatasetLoader instance.

Parameters:     

  * **dataset\_name** \(_str_\) – The name of the LangSmith dataset.

  * **client** \(_Optional_ _\[__'Client'__\]_\) – An instance of LangSmith client; if not provided, a new client instance will be created.

Methods

`__init__`\(\*, dataset\_name\[, client\]\) | Initialize a new LangSmithChatDatasetLoader instance.   ---|---   `lazy_load`\(\) | Lazy load the chat sessions from the specified LangSmith dataset.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(

    _\*_ ,     _dataset\_name : str_,     _client : 'Client' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/langsmith.html#LangSmithDatasetChatLoader.__init__)\#     

Initialize a new LangSmithChatDatasetLoader instance.

Parameters:     

  * **dataset\_name** \(_str_\) – The name of the LangSmith dataset.

  * **client** \(_Optional_ _\[__'Client'__\]_\) – An instance of LangSmith client; if not provided, a new client instance will be created.

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/langsmith.html#LangSmithDatasetChatLoader.lazy_load)\#     

Lazy load the chat sessions from the specified LangSmith dataset.

This method fetches the chat data from the dataset and converts each data point to chat sessions on-the-fly, yielding one session at a time.

Returns:     

Iterator of chat sessions containing messages.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using LangSmithDatasetChatLoader

  * [LangSmith Chat Datasets](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_dataset/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)