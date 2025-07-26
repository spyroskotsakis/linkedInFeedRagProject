# MessagesPlaceholder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html
**Word Count:** 354
**Links Count:** 180
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# MessagesPlaceholder\#

_class _langchain\_core.prompts.chat.MessagesPlaceholder[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#MessagesPlaceholder)\#     

Bases: [`BaseMessagePromptTemplate`](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.message.BaseMessagePromptTemplate.html#langchain_core.prompts.message.BaseMessagePromptTemplate "langchain_core.prompts.message.BaseMessagePromptTemplate")

Prompt template that assumes variable is already list of messages.

A placeholder which can be used to pass in a list of messages.

Direct usage:

>  >     from langchain_core.prompts import MessagesPlaceholder >      >     prompt = MessagesPlaceholder("history") >     prompt.format_messages() # raises KeyError >      >     prompt = MessagesPlaceholder("history", optional=True) >     prompt.format_messages() # returns empty list [] >      >     prompt.format_messages( >         history=[ >             ("system", "You are an AI assistant."), >             ("human", "Hello!"), >         ] >     ) >     # -> [ >     #     SystemMessage(content="You are an AI assistant."), >     #     HumanMessage(content="Hello!"), >     # ] >     

Building a prompt with chat history:

>  >     from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder >      >     prompt = ChatPromptTemplate.from_messages( >         [ >             ("system", "You are a helpful assistant."), >             MessagesPlaceholder("history"), >             ("human", "{question}") >         ] >     ) >     prompt.invoke( >        { >            "history": [("human", "what's 5 + 2"), ("ai", "5 + 2 is 7")], >            "question": "now multiply that by 4" >        } >     ) >     # -> ChatPromptValue(messages=[ >     #     SystemMessage(content="You are a helpful assistant."), >     #     HumanMessage(content="what's 5 + 2"), >     #     AIMessage(content="5 + 2 is 7"), >     #     HumanMessage(content="now multiply that by 4"), >     # ]) >     

Limiting the number of messages:

>  >     from langchain_core.prompts import MessagesPlaceholder >      >     prompt = MessagesPlaceholder("history", n_messages=1) >      >     prompt.format_messages( >         history=[ >             ("system", "You are an AI assistant."), >             ("human", "Hello!"), >         ] >     ) >     # -> [ >     #     HumanMessage(content="Hello!"), >     # ] >     

Create a messages placeholder.

Parameters:     

  * **variable\_name** – Name of variable to use as messages.

  * **optional** – If True format\_messages can be called with no arguments and will return an empty list. If False then a named argument with name variable\_name must be passed in, even if the value is an empty list. Defaults to False.\]

_param _n\_messages _: PositiveInt | None_ _ = None_\#     

Maximum number of messages to include. If None, then will include all. Defaults to None.

_param _optional _: bool_ _ = False_\#     

If True format\_messages can be called with no arguments and will return an empty list. If False then a named argument with name variable\_name must be passed in, even if the value is an empty list.

_param _variable\_name _: str_ _\[Required\]_\#     

Name of variable to use as messages.

_async _aformat\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]\#     

Async format messages from kwargs.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

List of BaseMessages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

format\_messages\(

    _\*\* kwargs: Any_, \) → list\[[BaseMessage](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#MessagesPlaceholder.format_messages)\#     

Format messages from kwargs.

Parameters:     

**\*\*kwargs** \(_Any_\) – Keyword arguments to use for formatting.

Returns:     

List of BaseMessage.

Raises:     

**ValueError** – If variable is not a list of messages.

Return type:     

list\[[_BaseMessage_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")\]

pretty\_print\(\) → None\#     

Print a human-readable representation.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/chat.html#MessagesPlaceholder.pretty_repr)\#     

Human-readable representation.

Parameters:     

**html** \(_bool_\) – Whether to format as HTML. Defaults to False.

Returns:     

Human-readable representation.

Return type:     

str

_property _input\_variables _: list\[str\]_\#     

Input variables for this prompt template.

Returns:     

List of input variable names.

Examples using MessagesPlaceholder

  * [AWS DynamoDB](https://python.langchain.com/docs/integrations/memory/aws_dynamodb/)

  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)

  * [Build an Extraction Chain](https://python.langchain.com/docs/tutorials/extraction/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Couchbase](https://python.langchain.com/docs/integrations/memory/couchbase_chat_message_history/)

  * [Google AlloyDB for PostgreSQL](https://python.langchain.com/docs/integrations/memory/google_alloydb/)

  * [Google El Carro Oracle](https://python.langchain.com/docs/integrations/memory/google_el_carro/)

  * [Google SQL for MySQL](https://python.langchain.com/docs/integrations/memory/google_sql_mysql/)

  * [Google SQL for PostgreSQL](https://python.langchain.com/docs/integrations/memory/google_sql_pg/)

  * [Google SQL for SQL Server](https://python.langchain.com/docs/integrations/memory/google_sql_mssql/)

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)

  * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [Llama2Chat](https://python.langchain.com/docs/integrations/chat/llama2_chat/)

  * [MongoDB](https://python.langchain.com/docs/integrations/memory/mongodb_chat_message_history/)

  * [Redis](https://python.langchain.com/docs/integrations/memory/redis_chat_message_history/)

  * [SQL \(SQLAlchemy\)](https://python.langchain.com/docs/integrations/memory/sql_chat_message_history/)

  * [SQLite](https://python.langchain.com/docs/integrations/memory/sqlite/)

  * [Streamlit](https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history/)

  * [TiDB](https://python.langchain.com/docs/integrations/memory/tidb_chat_message_history/)

  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)

__On this page