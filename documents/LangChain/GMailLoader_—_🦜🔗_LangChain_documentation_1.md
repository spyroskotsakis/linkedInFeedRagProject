# GMailLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/gmail/langchain_google_community.gmail.loader.GMailLoader.html
**Word Count:** 166
**Links Count:** 120
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# GMailLoader\#

_class _langchain\_google\_community.gmail.loader.GMailLoader\(

    _creds : Any_,     _n : int = 100_,     _raise\_error : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/loader.html#GMailLoader)\#     

Load data from GMail.

There are many ways you could want to load data from GMail. This loader is currently fairly opinionated in how to do so. The way it does it is it first looks for all messages that you have sent. It then looks for messages where you are responding to a previous email. It then fetches that previous email, and creates a training example of that email, followed by your email.

Note that there are clear limitations here. For example, all examples created are only looking at the previous email for context.

To use:

  * Set up a Google Developer Account:     

Go to the Google Developer Console, create a project, and enable the Gmail API for that project. This will give you a credentials.json file that you’ll need later.

Methods

`__init__`\(creds\[, n, raise\_error\]\) |    ---|---   `lazy_load`\(\) | Lazy load the chat sessions.   `load`\(\) | Eagerly load the chat sessions into memory.      Parameters:     

  * **creds** \(_Any_\)

  * **n** \(_int_\)

  * **raise\_error** \(_bool_\)

\_\_init\_\_\(

    _creds : Any_,     _n : int = 100_,     _raise\_error : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/loader.html#GMailLoader.__init__)\#     

Parameters:     

  * **creds** \(_Any_\)

  * **n** \(_int_\)

  * **raise\_error** \(_bool_\)

Return type:     

None

lazy\_load\(\) → Iterator\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/loader.html#GMailLoader.lazy_load)\#     

Lazy load the chat sessions.

Returns:     

An iterator of chat sessions.

Return type:     

_Iterator_\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

load\(\) → list\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]\#     

Eagerly load the chat sessions into memory.

Returns:     

A list of chat sessions.

Return type:     

list\[[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]

Examples using GMailLoader

  * [GMail](https://python.langchain.com/docs/integrations/chat_loaders/gmail/)

__On this page