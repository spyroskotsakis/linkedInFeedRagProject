# agents — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/agents.html
**Word Count:** 94
**Links Count:** 100
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# `agents`\#

**Agent** is a class that uses an LLM to choose a sequence of actions to take.

In Chains, a sequence of actions is hardcoded. In Agents, a language model is used as a reasoning engine to determine which actions to take and in which order.

Agents select and use **Tools** and **Toolkits** for actions.

**Functions**

[`agents.agent_toolkits.csv.base.create_csv_agent`](https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.csv.base.create_csv_agent.html#langchain_experimental.agents.agent_toolkits.csv.base.create_csv_agent "langchain_experimental.agents.agent_toolkits.csv.base.create_csv_agent")\(...\) | Create pandas dataframe agent by loading csv to a dataframe.   ---|---   [`agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent`](https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html#langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent "langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent")\(llm, df\) | Construct a Pandas agent from an LLM and dataframe\(s\).   [`agents.agent_toolkits.python.base.create_python_agent`](https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.python.base.create_python_agent.html#langchain_experimental.agents.agent_toolkits.python.base.create_python_agent "langchain_experimental.agents.agent_toolkits.python.base.create_python_agent")\(...\) | Construct a python agent from an LLM and tool.   [`agents.agent_toolkits.spark.base.create_spark_dataframe_agent`](https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.spark.base.create_spark_dataframe_agent.html#langchain_experimental.agents.agent_toolkits.spark.base.create_spark_dataframe_agent "langchain_experimental.agents.agent_toolkits.spark.base.create_spark_dataframe_agent")\(llm, df\) | Construct a Spark agent from an LLM and dataframe.   [`agents.agent_toolkits.xorbits.base.create_xorbits_agent`](https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.xorbits.base.create_xorbits_agent.html#langchain_experimental.agents.agent_toolkits.xorbits.base.create_xorbits_agent "langchain_experimental.agents.agent_toolkits.xorbits.base.create_xorbits_agent")\(...\) | Construct a xorbits agent from an LLM and dataframe.