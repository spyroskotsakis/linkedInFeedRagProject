# langchain_core.chat_sessions — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/chat_sessions.html
**Word Count:** 45
**Links Count:** 13
**Scraped:** 2025-07-21 08:57:35
**Status:** completed

---

# Source code for langchain\_core.chat\_sessions               """**Chat Sessions** are a collection of messages and function calls."""          from collections.abc import Sequence     from typing import TypedDict          from langchain_core.messages import BaseMessage                              [[docs]](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession)     class ChatSession(TypedDict, total=False):         """Chat Session.              Chat Session represents a single conversation, channel, or other group of messages.         """              messages: Sequence[BaseMessage]         """A sequence of the LangChain chat messages loaded from the source."""         functions: Sequence[dict]         """A sequence of the function calling specs for the messages."""