# TelegramChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.telegram.TelegramChatLoader.html
**Word Count:** 144
**Links Count:** 127
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# TelegramChatLoader\#

_class _langchain\_community.chat\_loaders.telegram.TelegramChatLoader\(_path : str | Path_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/telegram.html#TelegramChatLoader)\#     

Load telegram conversations to LangChain chat messages.

To export, use the Telegram Desktop app from <https://desktop.telegram.org/>, select a conversation, click the three dots in the top right corner, and select “Export chat history”. Then select “Machine-readable JSON” \(preferred\) to export. Note: the ‘lite’ versions of the desktop app \(like “Telegram for MacOS”\) do not support exporting chat history.

Initialize the TelegramChatLoader.

Parameters:     

**path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – Path to the exported Telegram chat zip, directory, json, or HTML file.

Methods

`__init__`\(path\) | Initialize the TelegramChatLoader.   ---|---   `lazy_load`\(\) | Lazy load the messages from the chat file and yield them in as chat sessions.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(_path : str | Path_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/telegram.html#TelegramChatLoader.__init__)\#     

Initialize the TelegramChatLoader.

Parameters:     

**path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – Path to the exported Telegram chat zip, directory, json, or HTML file.

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/telegram.html#TelegramChatLoader.lazy_load)\#     

Lazy load the messages from the chat file and yield them in as chat sessions.

Yields:     

_ChatSession_ – The loaded chat session.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using TelegramChatLoader

  * [Telegram](https://python.langchain.com/docs/integrations/providers/telegram/)

__On this page