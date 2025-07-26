# get_cohere_chat_request — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.cohere.get_cohere_chat_request.html
**Word Count:** 31
**Links Count:** 229
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# get\_cohere\_chat\_request\#

langchain\_community.chat\_models.cohere.get\_cohere\_chat\_request\(

    _messages : List\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _\*_ ,     _connectors : List\[Dict\[str, str\]\] | None = None_,     _\*\* kwargs: Any_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/cohere.html#get_cohere_chat_request)\#     

Get the request for the Cohere chat API.

Parameters:     

  * **messages** \(_List_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – The messages.

  * **connectors** \(_List_ _\[__Dict_ _\[__str_ _,__str_ _\]__\]__|__None_\) – The connectors.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments.

Returns:     

The request for the Cohere chat API.

Return type:     

_Dict_\[str, _Any_\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)