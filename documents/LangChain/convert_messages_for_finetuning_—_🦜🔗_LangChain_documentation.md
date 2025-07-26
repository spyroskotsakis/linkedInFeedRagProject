# convert_messages_for_finetuning — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.convert_messages_for_finetuning.html
**Word Count:** 34
**Links Count:** 115
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# convert\_messages\_for\_finetuning\#

langchain\_community.adapters.openai.convert\_messages\_for\_finetuning\(

    _sessions : Iterable\[[ChatSession](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession")\]_, \) → List\[List\[dict\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#convert_messages_for_finetuning)\#     

Convert messages to a list of lists of dictionaries for fine-tuning.

Parameters:     

**sessions** \(_Iterable_ _\[_[_ChatSession_](https://python.langchain.com/api_reference/core/chat_sessions/langchain_core.chat_sessions.ChatSession.html#langchain_core.chat_sessions.ChatSession "langchain_core.chat_sessions.ChatSession") _\]_\) – The chat sessions.

Returns:     

The list of lists of dictionaries.

Return type:     

_List_\[_List_\[dict\]\]

Examples using convert\_messages\_for\_finetuning

  * [Facebook Messenger](https://python.langchain.com/docs/integrations/chat_loaders/facebook/)

  * [LangSmith Chat Datasets](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_dataset/)

  * [LangSmith LLM Runs](https://python.langchain.com/docs/integrations/chat_loaders/langsmith_llm_runs/)

  * [iMessage](https://python.langchain.com/docs/integrations/chat_loaders/imessage/)

__On this page