# create_sql_query_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.create_sql_query_chain.html
**Word Count:** 343
**Links Count:** 205
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# create\_sql\_query\_chain\#

langchain.chains.sql\_database.query.create\_sql\_query\_chain\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _db : [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _k : int = 5_,     _\*_ ,     _get\_col\_comments : bool | None = None_, \) → [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[[SQLInput](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInput.html#langchain.chains.sql_database.query.SQLInput "langchain.chains.sql_database.query.SQLInput") | [SQLInputWithTables](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInputWithTables.html#langchain.chains.sql_database.query.SQLInputWithTables "langchain.chains.sql_database.query.SQLInputWithTables") | dict\[str, Any\], str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/sql_database/query.html#create_sql_query_chain)\#     

Create a chain that generates SQL queries.

> _Security Note_ : This chain generates SQL queries for the given database. >
>> The SQLDatabase class provides a get\_table\_info method that can be used to get column information as well as sample data from the table. >>  >> To mitigate risk of leaking sensitive data, limit permissions to read and scope to the tables that are needed. >>  >> Optionally, use the SQLInputWithTables input type to specify which tables are allowed to be accessed. >>  >> Control access to who can submit requests to this chain. >>  >> See <https://python.langchain.com/docs/security> for more information. >  > Args: >      >  > llm: The language model to use. db: The SQLDatabase to generate the query for. prompt: The prompt to use. If none is provided, will choose one >
>> based on dialect. Defaults to None. See Prompt section below for more. >  > k: The number of results per select statement to return. Defaults to 5. get\_col\_comments: Whether to retrieve column comments along with table info. >
>> Defaults to False. >  > Returns: >      >  > A chain that takes in a question and generates a SQL query that answers that question. >  > Example: >
>>  >>     # pip install -U langchain langchain-community langchain-openai >>     from langchain_openai import ChatOpenAI >>     from langchain.chains import create_sql_query_chain >>     from langchain_community.utilities import SQLDatabase >>      >>     db = SQLDatabase.from_uri("sqlite:///Chinook.db") >>     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0) >>     chain = create_sql_query_chain(llm, db) >>     response = chain.invoke({"question": "How many employees are there"}) >>      >  > Prompt: >      >  > If no prompt is provided, a default prompt is selected based on the SQLDatabase dialect. If one is provided, it must support input variables: >      >  >   * input: The user question plus suffix “ >  > 

SQLQuery: “ is passed here.     

>   * top\_k: The number of results per select statement \(the k argument to >      >  > this function\) is passed in here. >  >   * table\_info: Table definitions and sample rows are passed in here. If the >      >  > user specifies “table\_names\_to\_use” when invoking chain, only those will be included. Otherwise, all tables are included. >  >   * dialect \(optional\): If dialect input variable is in prompt, the db >      >  > dialect will be passed in here. >  > 

Here’s an example prompt:               from langchain_core.prompts import PromptTemplate          template = '''Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.     Use the following format:          Question: "Question here"     SQLQuery: "SQL Query to run"     SQLResult: "Result of the SQLQuery"     Answer: "Final answer here"          Only use the following tables:          {table_info}.          Question: {input}'''     prompt = PromptTemplate.from_template(template)     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **db** \([_SQLDatabase_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")\)

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\)

  * **k** \(_int_\)

  * **get\_col\_comments** \(_Optional_ _\[__bool_ _\]_\)

Return type:     

[Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Union\[[SQLInput](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInput.html#langchain.chains.sql_database.query.SQLInput "langchain.chains.sql_database.query.SQLInput"), [SQLInputWithTables](https://python.langchain.com/api_reference/langchain/chains/langchain.chains.sql_database.query.SQLInputWithTables.html#langchain.chains.sql_database.query.SQLInputWithTables "langchain.chains.sql_database.query.SQLInputWithTables"), dict\[str, Any\]\], str\]

Examples using create\_sql\_query\_chain

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)

  * [How to deal with large databases when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_large_db/)

  * [How to do query validation as part of SQL question-answering](https://python.langchain.com/docs/how_to/sql_query_checking/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)