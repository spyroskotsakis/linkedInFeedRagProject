# langchain_core.chat_loaders — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/chat_loaders.html
**Word Count:** 28
**Links Count:** 15
**Scraped:** 2025-07-21 08:57:35
**Status:** completed

---

# Source code for langchain\_core.chat\_loaders               """Chat loaders."""          from abc import ABC, abstractmethod     from collections.abc import Iterator          from langchain_core.chat_sessions import ChatSession                              [[docs]](https://python.langchain.com/api_reference/core/chat_loaders/langchain_core.chat_loaders.BaseChatLoader.html#langchain_google_community.gmail.loader.BaseChatLoader)     class BaseChatLoader(ABC):         """Base class for chat loaders."""                         [[docs]](https://python.langchain.com/api_reference/core/chat_loaders/langchain_core.chat_loaders.BaseChatLoader.html#langchain_google_community.gmail.loader.BaseChatLoader.lazy_load)         @abstractmethod         def lazy_load(self) -> Iterator[ChatSession]:             """Lazy load the chat sessions.                  Returns:                 An iterator of chat sessions.             """                                        [[docs]](https://python.langchain.com/api_reference/core/chat_loaders/langchain_core.chat_loaders.BaseChatLoader.html#langchain_google_community.gmail.loader.BaseChatLoader.load)         def load(self) -> list[ChatSession]:             """Eagerly load the chat sessions into memory.                  Returns:                 A list of chat sessions.             """             return list(self.lazy_load())