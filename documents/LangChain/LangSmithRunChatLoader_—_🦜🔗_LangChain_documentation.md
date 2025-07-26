# LangSmithRunChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.langsmith.LangSmithRunChatLoader.html
**Word Count:** 158
**Links Count:** 130
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# LangSmithRunChatLoader\#

_class _langchain\_community.chat\_loaders.langsmith.LangSmithRunChatLoader\(

    _runs : Iterable\[str | Run\]_,     _client : 'Client' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/langsmith.html#LangSmithRunChatLoader)\#     

Load chat sessions from a list of LangSmith “llm” runs.

runs\#     

The list of LLM run IDs or run objects.

Type:     

Iterable\[Union\[str, Run\]\]

client\#     

Instance of LangSmith client for fetching data.

Type:     

Client

Initialize a new LangSmithRunChatLoader instance.

Parameters:     

  * **runs** \(_Iterable_ _\[__Union_ _\[__str_ _,__Run_ _\]__\]_\) – List of LLM run IDs or run objects.

  * **client** \(_Optional_ _\[__'Client'__\]_\) – An instance of LangSmith client, if not provided, a new client instance will be created.

Methods

`__init__`\(runs\[, client\]\) | Initialize a new LangSmithRunChatLoader instance.   ---|---   `lazy_load`\(\) | Lazy load the chat sessions from the iterable of run IDs.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(

    _runs : Iterable\[str | Run\]_,     _client : 'Client' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/langsmith.html#LangSmithRunChatLoader.__init__)\#     

Initialize a new LangSmithRunChatLoader instance.

Parameters:     

  * **runs** \(_Iterable_ _\[__Union_ _\[__str_ _,__Run_ _\]__\]_\) – List of LLM run IDs or run objects.

  * **client** \(_Optional_ _\[__'Client'__\]_\) – An instance of LangSmith client, if not provided, a new client instance will be created.

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/langsmith.html#LangSmithRunChatLoader.lazy_load)\#     

Lazy load the chat sessions from the iterable of run IDs.

This method fetches the runs and converts them to chat sessions on-the-fly, yielding one session at a time.

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

Examples using LangSmithRunChatLoader

  * [LangSmith LLM Runs](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_llm_runs/)

__On this page