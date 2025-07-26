# map_ai_messages — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.utils.map_ai_messages.html
**Word Count:** 30
**Links Count:** 122
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# map\_ai\_messages\#

langchain\_community.chat\_loaders.utils.map\_ai\_messages\(

    _chat\_sessions : Iterable\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]_,     _sender : str_, \) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/utils.html#map_ai_messages)\#     

Convert messages from the specified ‘sender’ to AI messages.

This is useful for fine-tuning the AI to adapt to your voice.

Parameters:     

  * **chat\_sessions** \(_Iterable_ _\[_[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession") _\]_\)

  * **sender** \(_str_\)

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using map\_ai\_messages

  * [Discord](https://python.langchain.com/docs/integrations/chat_loaders/discord/)

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

  * [GMail](https://python.langchain.com/docs/integrations/chat_loaders/gmail/)

  * [Slack](https://python.langchain.com/docs/integrations/chat_loaders/slack/)

  * [Telegram](https://python.langchain.com/docs/integrations/chat_loaders/telegram/)

  * [WeChat](https://python.langchain.com/docs/integrations/chat_loaders/wechat/)

  * [WhatsApp](https://python.langchain.com/docs/integrations/chat_loaders/whatsapp/)

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

__On this page