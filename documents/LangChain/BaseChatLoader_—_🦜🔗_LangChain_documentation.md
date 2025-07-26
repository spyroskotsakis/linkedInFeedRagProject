# BaseChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/chat_loaders/langchain_core.chat_loaders.BaseChatLoader.html
**Word Count:** 41
**Links Count:** 111
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# BaseChatLoader\#

_class _langchain\_core.chat\_loaders.BaseChatLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_loaders.html#BaseChatLoader)\#     

Base class for chat loaders.

Methods

`lazy_load`\(\) | Lazy load the chat sessions.   ---|---   `load`\(\) | Eagerly load the chat sessions into memory.      _abstractmethod _lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_loaders.html#BaseChatLoader.lazy_load)\#     

Lazy load the chat sessions.

Returns:     

An iterator of chat sessions.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_loaders.html#BaseChatLoader.load)\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

__On this page