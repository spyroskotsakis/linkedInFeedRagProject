# SlackChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.slack.SlackChatLoader.html
**Word Count:** 126
**Links Count:** 126
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# SlackChatLoader\#

_class _langchain\_community.chat\_loaders.slack.SlackChatLoader\(_path : str | Path_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/slack.html#SlackChatLoader)\#     

Load Slack conversations from a dump zip file.

Initialize the chat loader with the path to the exported Slack dump zip file.

Parameters:     

**path** \(_str_ _|__Path_\) – Path to the exported Slack dump zip file.

Methods

`__init__`\(path\) | Initialize the chat loader with the path to the exported Slack dump zip file.   ---|---   `lazy_load`\(\) | Lazy load the chat sessions from the Slack dump file and yield them in the required format.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(_path : str | Path_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/slack.html#SlackChatLoader.__init__)\#     

Initialize the chat loader with the path to the exported Slack dump zip file.

Parameters:     

**path** \(_str_ _|__Path_\) – Path to the exported Slack dump zip file.

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/slack.html#SlackChatLoader.lazy_load)\#     

Lazy load the chat sessions from the Slack dump file and yield them in the required format.

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

Examples using SlackChatLoader

  * [Slack](https://python.langchain.com/docs/integrations/providers/slack/)

__On this page