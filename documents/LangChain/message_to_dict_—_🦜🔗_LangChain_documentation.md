# message_to_dict — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.message_to_dict.html
**Word Count:** 42
**Links Count:** 151
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# message\_to\_dict\#

langchain\_core.messages.base.message\_to\_dict\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/base.html#message_to_dict)\#     

Convert a Message to a dictionary.

Parameters:     

**message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\) – Message to convert.

Returns:     

Message as a dict. The dict will have a “type” key with the message type and a “data” key with the message data as a dict.

Return type:     

dict

__On this page