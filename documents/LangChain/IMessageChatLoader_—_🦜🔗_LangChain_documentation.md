# IMessageChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.imessage.IMessageChatLoader.html
**Word Count:** 182
**Links Count:** 126
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# IMessageChatLoader\#

_class _langchain\_community.chat\_loaders.imessage.IMessageChatLoader\(_path : str | Path | None = None_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/imessage.html#IMessageChatLoader)\#     

Load chat sessions from the iMessage chat.db SQLite file.

It only works on macOS when you have iMessage enabled and have the chat.db file.

The chat.db file is likely located at ~/Library/Messages/chat.db. However, your terminal may not have permission to access this file. To resolve this, you can copy the file to a different location, change the permissions of the file, or grant full disk access for your terminal emulator in System Settings > Security and Privacy > Full Disk Access.

Initialize the IMessageChatLoader.

Parameters:     

**path** \(_str_ _or_ _Path_ _,__optional_\) – Path to the chat.db SQLite file. Defaults to None, in which case the default path ~/Library/Messages/chat.db will be used.

Methods

`__init__`\(\[path\]\) | Initialize the IMessageChatLoader.   ---|---   `lazy_load`\(\) | Lazy load the chat sessions from the iMessage chat.db and yield them in the required format.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(

    _path : str | Path | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/imessage.html#IMessageChatLoader.__init__)\#     

Initialize the IMessageChatLoader.

Parameters:     

**path** \(_str_ _or_ _Path_ _,__optional_\) – Path to the chat.db SQLite file. Defaults to None, in which case the default path ~/Library/Messages/chat.db will be used.

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/imessage.html#IMessageChatLoader.lazy_load)\#     

Lazy load the chat sessions from the iMessage chat.db and yield them in the required format.

Yields:     

_ChatSession_ – Loaded chat session.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using IMessageChatLoader

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

__On this page