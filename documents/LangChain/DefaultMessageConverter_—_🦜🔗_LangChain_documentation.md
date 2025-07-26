# DefaultMessageConverter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.DefaultMessageConverter.html
**Word Count:** 52
**Links Count:** 148
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# DefaultMessageConverter\#

_class _langchain\_community.chat\_message\_histories.sql.DefaultMessageConverter\(_table\_name : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#DefaultMessageConverter)\#     

The default message converter for SQLChatMessageHistory.

Methods

`__init__`\(table\_name\) |    ---|---   `from_sql_model`\(sql\_message\) | Convert a SQLAlchemy model to a BaseMessage instance.   `get_sql_model_class`\(\) | Get the SQLAlchemy model class.   `to_sql_model`\(message, session\_id\) | Convert a BaseMessage instance to a SQLAlchemy model.      Parameters:     

**table\_name** \(_str_\)

\_\_init\_\_\(_table\_name : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#DefaultMessageConverter.__init__)\#     

Parameters:     

**table\_name** \(_str_\)

from\_sql\_model\(

    _sql\_message : Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#DefaultMessageConverter.from_sql_model)\#     

Convert a SQLAlchemy model to a BaseMessage instance.

Parameters:     

**sql\_message** \(_Any_\)

Return type:     

[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

get\_sql\_model\_class\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#DefaultMessageConverter.get_sql_model_class)\#     

Get the SQLAlchemy model class.

Return type:     

_Any_

to\_sql\_model\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_,     _session\_id : str_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#DefaultMessageConverter.to_sql_model)\#     

Convert a BaseMessage instance to a SQLAlchemy model.

Parameters:     

  * **message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

  * **session\_id** \(_str_\)

Return type:     

_Any_

__On this page