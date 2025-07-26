# create_csv_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.csv.base.create_csv_agent.html
**Word Count:** 81
**Links Count:** 101
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# create\_csv\_agent\#

langchain\_experimental.agents.agent\_toolkits.csv.base.create\_csv\_agent\(

    _llm : LanguageModelLike_,     _path : str | IOBase | List\[str | IOBase\]_,     _pandas\_kwargs : dict | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/agents/agent_toolkits/csv/base.html#create_csv_agent)\#     

Create pandas dataframe agent by loading csv to a dataframe.

Parameters:     

  * **llm** \(_LanguageModelLike_\) – Language model to use for the agent.

  * **path** \(_Union_ _\[__str_ _,__IOBase_ _,__List_ _\[__Union_ _\[__str_ _,__IOBase_ _\]__\]__\]_\) – A string path, file-like object or a list of string paths/file-like objects that can be read in as pandas DataFrames with pd.read\_csv\(\).

  * **pandas\_kwargs** \(_Optional_ _\[__dict_ _\]_\) – Named arguments to pass to pd.read\_csv\(\).

  * **kwargs** \(_Any_\) – Additional kwargs to pass to langchain\_experimental.agents.agent\_toolkits.pandas.base.create\_pandas\_dataframe\_agent\(\).

Returns:     

An AgentExecutor with the specified agent\_type agent and access to a PythonAstREPLTool with the loaded DataFrame\(s\) and any user-provided extra\_tools.

Return type:     

[AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Example               from langchain_openai import ChatOpenAI     from langchain_experimental.agents import create_csv_agent          llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)     agent_executor = create_csv_agent(         llm,         "titanic.csv",         agent_type="openai-tools",         verbose=True     )     

__On this page