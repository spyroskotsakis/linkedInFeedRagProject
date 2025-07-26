# langchain_ai21.chat.chat_factory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_ai21/chat/chat_factory.html
**Word Count:** 23
**Links Count:** 13
**Scraped:** 2025-07-21 08:58:20
**Status:** completed

---

# Source code for langchain\_ai21.chat.chat\_factory               from langchain_ai21.chat.chat_adapter import (         ChatAdapter,         JambaChatCompletionsAdapter,     )                              [[docs]](https://python.langchain.com/api_reference/ai21/chat/langchain_ai21.chat.chat_factory.create_chat_adapter.html#langchain_ai21.chat.chat_factory.create_chat_adapter)     def create_chat_adapter(model: str) -> ChatAdapter:         """Create a chat adapter based on the model.              Args:             model: The model to create the chat adapter for.              Returns:             The chat adapter.         """         if "jamba" in model:             return JambaChatCompletionsAdapter()              raise ValueError(f"Model {model} not supported.")