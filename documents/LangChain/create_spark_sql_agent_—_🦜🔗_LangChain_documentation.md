# create_spark_sql_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.spark_sql.base.create_spark_sql_agent.html
**Word Count:** 154
**Links Count:** 168
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# create\_spark\_sql\_agent\#

langchain\_community.agent\_toolkits.spark\_sql.base.create\_spark\_sql\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [SparkSQLToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit.html#langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit "langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit")_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _callbacks : Callbacks = None_,     _prefix : str = 'You are an agent designed to interact with Spark SQL.\nGiven an input question, create a syntactically correct Spark SQL query to run, then look at the results of the query and return the answer.\nUnless the user specifies a specific number of examples they wish to obtain, always limit your query to at most \{top\_k\} results.\nYou can order the results by a relevant column to return the most interesting examples in the database.\nNever query for all the columns from a specific table, only ask for the relevant columns given the question.\nYou have access to tools for interacting with the database.\nOnly use the below tools. Only use the information returned by the below tools to construct your final answer.\nYou MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.\n\nDO NOT make any DML statements \(INSERT, UPDATE, DELETE, DROP etc.\) to the database.\n\nIf the question does not seem related to the database, just return "I don\'t know" as the answer.\n'_,     _suffix : str = 'Begin\!\n\nQuestion: \{input\}\nThought: I should look at the tables in the database to see what I can query.\n\{agent\_scratchpad\}'_,     _format\_instructions : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _top\_k : int = 10_,     _max\_iterations : int | None = 15_,     _max\_execution\_time : float | None = None_,     _early\_stopping\_method : str = 'force'_,     _verbose : bool = False_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/spark_sql/base.html#create_spark_sql_agent)\#     

Construct a Spark SQL agent from an LLM and tools.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **toolkit** \([_SparkSQLToolkit_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit.html#langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit "langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit")\) – The Spark SQL toolkit.

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]_\) – Optional. The callback manager. Default is None.

  * **callbacks** \(_Callbacks_\) – Optional. The callbacks. Default is None.

  * **prefix** \(_str_\) – Optional. The prefix for the prompt. Default is SQL\_PREFIX.

  * **suffix** \(_str_\) – Optional. The suffix for the prompt. Default is SQL\_SUFFIX.

  * **format\_instructions** \(_Optional_ _\[__str_ _\]_\) – Optional. The format instructions for the prompt. Default is None.

  * **input\_variables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The input variables for the prompt. Default is None.

  * **top\_k** \(_int_\) – Optional. The top k for the prompt. Default is 10.

  * **max\_iterations** \(_Optional_ _\[__int_ _\]_\) – Optional. The maximum iterations to run. Default is 15.

  * **max\_execution\_time** \(_Optional_ _\[__float_ _\]_\) – Optional. The maximum execution time. Default is None.

  * **early\_stopping\_method** \(_str_\) – Optional. The early stopping method. Default is “force”.

  * **verbose** \(_bool_\) – Optional. Whether to print verbose output. Default is False.

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional. The agent executor kwargs. Default is None.

  * **kwargs** \(_Any_\) – Any. Additional keyword arguments.

Returns:     

The agent executor.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Examples using create\_spark\_sql\_agent

  * [Spark SQL Toolkit](https://python.langchain.com/docs/integrations/tools/spark_sql/)

__On this page