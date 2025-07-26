# merge_chat_runs_in_session — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.utils.merge_chat_runs_in_session.html
**Word Count:** 36
**Links Count:** 114
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# merge\_chat\_runs\_in\_session\#

langchain\_community.chat\_loaders.utils.merge\_chat\_runs\_in\_session\(

    _chat\_session : [ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")_,     _delimiter : str = '\n\n'_, \) → [ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/utils.html#merge_chat_runs_in_session)\#     

Merge chat runs together in a chat session.

A chat run is a sequence of messages from the same sender.

Parameters:     

  * **chat\_session** \([_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\) – A chat session.

  * **delimiter** \(_str_\)

Returns:     

A chat session with merged chat runs.

Return type:     

[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")

__On this page