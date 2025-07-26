# WhatsAppChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_loaders/langchain_community.chat_loaders.whatsapp.WhatsAppChatLoader.html
**Word Count:** 149
**Links Count:** 128
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# WhatsAppChatLoader\#

_class _langchain\_community.chat\_loaders.whatsapp.WhatsAppChatLoader\(_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/whatsapp.html#WhatsAppChatLoader)\#     

Load WhatsApp conversations from a dump zip file or directory.

Initialize the WhatsAppChatLoader.

Parameters:     

**path** \(_str_\) – Path to the exported WhatsApp chat zip directory, folder, or file.

To generate the dump, open the chat, click the three dots in the top right corner, and select “More”. Then select “Export chat” and choose “Without media”.

Methods

`__init__`\(path\) | Initialize the WhatsAppChatLoader.   ---|---   `lazy_load`\(\) | Lazy load the messages from the chat file and yield them as chat sessions.   `load`\(\) | Eagerly load the chat sessions into memory.      \_\_init\_\_\(_path : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/whatsapp.html#WhatsAppChatLoader.__init__)\#     

Initialize the WhatsAppChatLoader.

Parameters:     

**path** \(_str_\) – Path to the exported WhatsApp chat zip directory, folder, or file.

To generate the dump, open the chat, click the three dots in the top right corner, and select “More”. Then select “Export chat” and choose “Without media”.

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_loaders/whatsapp.html#WhatsAppChatLoader.lazy_load)\#     

Lazy load the messages from the chat file and yield them as chat sessions.

Yields:     

_Iterator\[ChatSession\]_ – The loaded chat sessions.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using WhatsAppChatLoader

  * [Facebook - Meta](https://python.langchain.com/docs/integrations/providers/facebook/)

  * [WhatsApp](https://python.langchain.com/docs/integrations/providers/whatsapp/)

  * [WhatsApp Chat](https://python.langchain.com/docs/integrations/document_loaders/whatsapp_chat/)

__On this page