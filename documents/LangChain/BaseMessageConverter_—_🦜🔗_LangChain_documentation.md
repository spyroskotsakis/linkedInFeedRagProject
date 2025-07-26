# BaseMessageConverter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_message_histories/langchain_community.chat_message_histories.sql.BaseMessageConverter.html
**Word Count:** 52
**Links Count:** 144
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# BaseMessageConverter\#

_class _langchain\_community.chat\_message\_histories.sql.BaseMessageConverter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#BaseMessageConverter)\#     

Convert BaseMessage to the SQLAlchemy model.

Methods

`from_sql_model`\(sql\_message\) | Convert a SQLAlchemy model to a BaseMessage instance.   ---|---   `get_sql_model_class`\(\) | Get the SQLAlchemy model class.   `to_sql_model`\(message, session\_id\) | Convert a BaseMessage instance to a SQLAlchemy model.      _abstractmethod _from\_sql\_model\(

    _sql\_message : Any_, \) → [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#BaseMessageConverter.from_sql_model)\#     

Convert a SQLAlchemy model to a BaseMessage instance.

Parameters:     

**sql\_message** \(_Any_\)

Return type:     

[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

_abstractmethod _get\_sql\_model\_class\(\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#BaseMessageConverter.get_sql_model_class)\#     

Get the SQLAlchemy model class.

Return type:     

_Any_

_abstractmethod _to\_sql\_model\(

    _message : [BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")_,     _session\_id : str_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_message_histories/sql.html#BaseMessageConverter.to_sql_model)\#     

Convert a BaseMessage instance to a SQLAlchemy model.

Parameters:     

  * **message** \([_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\)

  * **session\_id** \(_str_\)

Return type:     

_Any_

__On this page