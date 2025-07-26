# SingleFileFacebookMessengerChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.facebook_messenger.SingleFileFacebookMessengerChatLoader.html
**Word Count:** 65
**Links Count:** 127
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# SingleFileFacebookMessengerChatLoader\#

_class _langchain\_community.chat\_loaders.facebook\_messenger.SingleFileFacebookMessengerChatLoader\(

    _path : Path | str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/facebook_messenger.html#SingleFileFacebookMessengerChatLoader)\#     

Load Facebook Messenger chat data from a single file.

Parameters:     

**path** \(_Union_ _\[__Path_ _,__str_ _\]_\) – The path to the chat file.

Methods

`__init__`\(path\) |    ---|---   `lazy_load`\(\) | Lazy loads the chat data from the file.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(

    _path : Path | str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/facebook_messenger.html#SingleFileFacebookMessengerChatLoader.__init__)\#     

Parameters:     

**path** \(_Path_ _|__str_\)

Return type:     

None

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/facebook_messenger.html#SingleFileFacebookMessengerChatLoader.lazy_load)\#     

Lazy loads the chat data from the file.

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

Examples using SingleFileFacebookMessengerChatLoader

  * [Facebook - Meta](https://python.langchain.com/docs/integrations/providers/facebook/)

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

__On this page