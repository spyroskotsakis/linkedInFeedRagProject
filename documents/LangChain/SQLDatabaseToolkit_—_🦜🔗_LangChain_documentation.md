# SQLDatabaseToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit.html
**Word Count:** 106
**Links Count:** 179
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# SQLDatabaseToolkit\#

_class _langchain\_community.agent\_toolkits.sql.toolkit.SQLDatabaseToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/sql/toolkit.html#SQLDatabaseToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

SQLDatabaseToolkit for interacting with SQL databases.

Setup:     

Install `langchain-community`.               pip install -U langchain-community     

Key init args:     

db: SQLDatabase     

The SQL database.

llm: BaseLanguageModel     

The language model \(for use with QuerySQLCheckerTool\)

Instantiate:                    from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit     from langchain_community.utilities.sql_database import SQLDatabase     from langchain_openai import ChatOpenAI          db = SQLDatabase.from_uri("sqlite:///Chinook.db")     llm = ChatOpenAI(temperature=0)          toolkit = SQLDatabaseToolkit(db=db, llm=llm)     

Tools:                    toolkit.get_tools()     

Use within an agent:                    from langchain import hub     from langgraph.prebuilt import create_react_agent          # Pull prompt (or define your own)     prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")     system_message = prompt_template.format(dialect="SQLite", top_k=5)          # Create agent     agent_executor = create_react_agent(         llm, toolkit.get_tools(), state_modifier=system_message     )          # Query agent     example_query = "Which country's customers spent the most?"          events = agent_executor.stream(         {"messages": [("user", example_query)]},         stream_mode="values",     )     for event in events:         event["messages"][-1].pretty_print()     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _db _: [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase")_ _\[Required\]_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

get\_context\(\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/sql/toolkit.html#SQLDatabaseToolkit.get_context)\#     

Return db context that you may want in agent prompt.

Return type:     

dict

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/sql/toolkit.html#SQLDatabaseToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

_property _dialect _: str_\#     

Return string representation of SQL dialect to use.

Examples using SQLDatabaseToolkit

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [CnosDB](https://python.langchain.com/docs/integrations/providers/cnosdb/)

  * [SQLDatabase Toolkit](https://python.langchain.com/docs/integrations/tools/sql_database/)

__On this page