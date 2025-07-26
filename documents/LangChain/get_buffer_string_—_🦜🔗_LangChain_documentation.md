# get_buffer_string — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.get_buffer_string.html
**Word Count:** 81
**Links Count:** 151
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# get\_buffer\_string\#

langchain\_core.messages.utils.get\_buffer\_string\(

    _messages : Sequence\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]_,     _human\_prefix : str = 'Human'_,     _ai\_prefix : str = 'AI'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/utils.html#get_buffer_string)\#     

Convert a sequence of Messages to strings and concatenate them into one string.

Parameters:     

  * **messages** \(_Sequence_ _\[_[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage") _\]_\) – Messages to be converted to strings.

  * **human\_prefix** \(_str_\) – The prefix to prepend to contents of HumanMessages. Default is “Human”.

  * **ai\_prefix** \(_str_\) – THe prefix to prepend to contents of AIMessages. Default is “AI”.

Returns:     

A single string concatenation of all input messages.

Raises:     

**ValueError** – If an unsupported message type is encountered.

Return type:     

str

Example               from langchain_core import AIMessage, HumanMessage          messages = [         HumanMessage(content="Hi, how are you?"),         AIMessage(content="Good, how are you?"),     ]     get_buffer_string(messages)     # -> "Human: Hi, how are you?\nAI: Good, how are you?"     

__On this page