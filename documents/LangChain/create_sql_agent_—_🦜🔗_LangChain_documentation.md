# create_sql_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.base.create_sql_agent.html
**Word Count:** 241
**Links Count:** 177
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# create\_sql\_agent\#

langchain\_community.agent\_toolkits.sql.base.create\_sql\_agent\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _toolkit : [SQLDatabaseToolkit](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit.html#langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit "langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit") | None = None_,     _agent\_type : [AgentType](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") | Literal\['openai-tools', 'tool-calling'\] | None = None_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _prefix : str | None = None_,     _suffix : str | None = None_,     _format\_instructions : str | None = None_,     _input\_variables : List\[str\] | None = None_,     _top\_k : int = 10_,     _max\_iterations : int | None = 15_,     _max\_execution\_time : float | None = None_,     _early\_stopping\_method : str = 'force'_,     _verbose : bool = False_,     _agent\_executor\_kwargs : Dict\[str, Any\] | None = None_,     _extra\_tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\] = \(\)_,     _\*_ ,     _db : [SQLDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase") | None = None_,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/sql/base.html#create_sql_agent)\#     

Construct a SQL agent from an LLM and toolkit or database.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use for the agent. If agent\_type is “tool-calling” then llm is expected to support tool calling.

  * **toolkit** \(_Optional_ _\[_[_SQLDatabaseToolkit_](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit.html#langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit "langchain_community.agent_toolkits.sql.toolkit.SQLDatabaseToolkit") _\]_\) – SQLDatabaseToolkit for the agent to use. Must provide exactly one of ‘toolkit’ or ‘db’. Specify ‘toolkit’ if you want to use a different model for the agent and the toolkit.

  * **agent\_type** \(_Optional_ _\[__Union_ _\[_[_AgentType_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") _,__Literal_ _\[__'openai-tools'__,__'tool-calling'__\]__\]__\]_\) – One of “tool-calling”, “openai-tools”, “openai-functions”, or “zero-shot-react-description”. Defaults to “zero-shot-react-description”. “tool-calling” is recommended over the legacy “openai-tools” and “openai-functions” types.

  * **callback\_manager** \(_Optional_ _\[_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _\]_\) – DEPRECATED. Pass “callbacks” key into ‘agent\_executor\_kwargs’ instead to pass constructor callbacks to AgentExecutor.

  * **prefix** \(_Optional_ _\[__str_ _\]_\) – Prompt prefix string. Must contain variables “top\_k” and “dialect”.

  * **suffix** \(_Optional_ _\[__str_ _\]_\) – Prompt suffix string. Default depends on agent type.

  * **format\_instructions** \(_Optional_ _\[__str_ _\]_\) – Formatting instructions to pass to ZeroShotAgent.create\_prompt\(\) when ‘agent\_type’ is “zero-shot-react-description”. Otherwise ignored.

  * **input\_variables** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – DEPRECATED.

  * **top\_k** \(_int_\) – Number of rows to query for by default.

  * **max\_iterations** \(_Optional_ _\[__int_ _\]_\) – Passed to AgentExecutor init.

  * **max\_execution\_time** \(_Optional_ _\[__float_ _\]_\) – Passed to AgentExecutor init.

  * **early\_stopping\_method** \(_str_\) – Passed to AgentExecutor init.

  * **verbose** \(_bool_\) – AgentExecutor verbosity.

  * **agent\_executor\_kwargs** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Arbitrary additional AgentExecutor args.

  * **extra\_tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – Additional tools to give to agent on top of the ones that come with SQLDatabaseToolkit.

  * **db** \(_Optional_ _\[_[_SQLDatabase_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.sql_database.SQLDatabase.html#langchain_community.utilities.sql_database.SQLDatabase "langchain_community.utilities.sql_database.SQLDatabase") _\]_\) – SQLDatabase from which to create a SQLDatabaseToolkit. Toolkit is created using ‘db’ and ‘llm’. Must provide exactly one of ‘db’ or ‘toolkit’.

  * **prompt** \(_Optional_ _\[_[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _\]_\) – Complete agent prompt. prompt and \{prefix, suffix, format\_instructions, input\_variables\} are mutually exclusive.

  * **\*\*kwargs** \(_Any_\) – Arbitrary additional Agent args.

Returns:     

An AgentExecutor with the specified agent\_type agent.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Example               from langchain_openai import ChatOpenAI     from langchain_community.agent_toolkits import create_sql_agent     from langchain_community.utilities import SQLDatabase          db = SQLDatabase.from_uri("sqlite:///Chinook.db")     llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)     agent_executor = create_sql_agent(llm, db=db, agent_type="tool-calling", verbose=True)     

Examples using create\_sql\_agent

  * [CnosDB](https://python.langchain.com/docs/integrations/providers/cnosdb/)

  * [How to do question answering over CSVs](https://python.langchain.com/docs/how_to/sql_csv/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)