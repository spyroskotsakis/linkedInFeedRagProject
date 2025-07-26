# FolderFacebookMessengerChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.facebook_messenger.FolderFacebookMessengerChatLoader.html
**Word Count:** 67
**Links Count:** 127
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# FolderFacebookMessengerChatLoader\#

_class _langchain\_community.chat\_loaders.facebook\_messenger.FolderFacebookMessengerChatLoader\(_path : str | Path_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/facebook_messenger.html#FolderFacebookMessengerChatLoader)\#     

Load Facebook Messenger chat data from a folder.

Parameters:     

**path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – The path to the directory containing the chat files.

Methods

`__init__`\(path\) |    ---|---   `lazy_load`\(\) | Lazy loads the chat data from the folder.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(

    _path : str | Path_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/facebook_messenger.html#FolderFacebookMessengerChatLoader.__init__)\#     

Parameters:     

**path** \(_str_ _|__Path_\)

Return type:     

None

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/facebook_messenger.html#FolderFacebookMessengerChatLoader.lazy_load)\#     

Lazy loads the chat data from the folder.

Yields:     

_ChatSession_ – A chat session containing the loaded messages.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using FolderFacebookMessengerChatLoader

  * [Facebook - Meta](https://python.langchain.com/docs/integrations/providers/facebook/)

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

__On this page