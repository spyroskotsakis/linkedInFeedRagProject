# merge_chat_runs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.utils.merge_chat_runs.html
**Word Count:** 39
**Links Count:** 121
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# merge\_chat\_runs\#

langchain\_community.chat\_loaders.utils.merge\_chat\_runs\(

    _chat\_sessions : Iterable\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]_, \) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/utils.html#merge_chat_runs)\#     

Merge chat runs together.

A chat run is a sequence of messages from the same sender.

Parameters:     

**chat\_sessions** \(_Iterable_ _\[_[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession") _\]_\) – A list of chat sessions.

Returns:     

A list of chat sessions with merged chat runs.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using merge\_chat\_runs

  * [Discord](https://python.langchain.com/docs/integrations/chat_loaders/discord/)

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

  * [Slack](https://python.langchain.com/docs/integrations/chat_loaders/slack/)

  * [Telegram](https://python.langchain.com/docs/integrations/chat_loaders/telegram/)

  * [WeChat](https://python.langchain.com/docs/integrations/chat_loaders/wechat/)

  * [WhatsApp](https://python.langchain.com/docs/integrations/chat_loaders/whatsapp/)

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

__On this page