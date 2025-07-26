# ChatSession — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html
**Word Count:** 40
**Links Count:** 110
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# ChatSession\#

_class _langchain\_core.chat\_sessions.ChatSession[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/chat_sessions.html#ChatSession)\#     

Chat Session.

Chat Session represents a single conversation, channel, or other group of messages.

messages _: Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_\#     

A sequence of the LangChain chat messages loaded from the source.

functions _: Sequence\[dict\]_\#     

A sequence of the function calling specs for the messages.

Examples using ChatSession

  * [Discord](https://python.langchain.com/docs/integrations/chat_loaders/discord/)

  * [Slack](https://python.langchain.com/docs/integrations/chat_loaders/slack/)

  * [Telegram](https://python.langchain.com/docs/integrations/chat_loaders/telegram/)

  * [WeChat](https://python.langchain.com/docs/integrations/chat_loaders/wechat/)

  * [WhatsApp](https://python.langchain.com/docs/integrations/chat_loaders/whatsapp/)

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

__On this page