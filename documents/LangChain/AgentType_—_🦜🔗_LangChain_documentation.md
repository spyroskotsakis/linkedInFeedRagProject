# AgentType — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html
**Word Count:** 251
**Links Count:** 226
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# AgentType\#

_class _langchain.agents.agent\_types.AgentType\(_value_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/agent_types.html#AgentType)\#     

Deprecated since version 0.1.0: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) as well as guides for [Migrating from AgentExecutor](https://python.langchain.com/docs/how_to/migrate_agent/) and LangGraph’s [Pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). It will not be removed until langchain==1.0.

An enum for agent types.

See documentation: <https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html>

ZERO\_SHOT\_REACT\_DESCRIPTION _ = 'zero-shot-react-description'_\#     

A zero shot agent that does a reasoning step before acting.

REACT\_DOCSTORE _ = 'react-docstore'_\#     

A zero shot agent that does a reasoning step before acting.

This agent has access to a document store that allows it to look up relevant information to answering the question.

SELF\_ASK\_WITH\_SEARCH _ = 'self-ask-with-search'_\#     

An agent that breaks down a complex question into a series of simpler questions.

This agent uses a search tool to look up answers to the simpler questions in order to answer the original complex question.

CONVERSATIONAL\_REACT\_DESCRIPTION _ = 'conversational-react-description'_\#     

CHAT\_ZERO\_SHOT\_REACT\_DESCRIPTION _ = 'chat-zero-shot-react-description'_\#     

A zero shot agent that does a reasoning step before acting.

This agent is designed to be used in conjunction

CHAT\_CONVERSATIONAL\_REACT\_DESCRIPTION _ = 'chat-conversational-react-description'_\#     

STRUCTURED\_CHAT\_ZERO\_SHOT\_REACT\_DESCRIPTION _ = 'structured-chat-zero-shot-react-description'_\#     

An zero-shot react agent optimized for chat models.

This agent is capable of invoking tools that have multiple inputs.

OPENAI\_FUNCTIONS _ = 'openai-functions'_\#     

An agent optimized for using open AI functions.

OPENAI\_MULTI\_FUNCTIONS _ = 'openai-multi-functions'_\#     

Examples using AgentType

  * [AINetwork Toolkit](https://python.langchain.com/docs/integrations/tools/ainetwork/)

  * [AWS Lambda](https://python.langchain.com/docs/integrations/tools/awslambda/)

  * [Aim](https://python.langchain.com/docs/integrations/providers/aim_tracking/)

  * [Amazon API Gateway](https://python.langchain.com/docs/integrations/llms/amazon_api_gateway/)

  * [Argilla](https://python.langchain.com/docs/integrations/callbacks/argilla/)

  * [Azure Cognitive Services Toolkit](https://python.langchain.com/docs/integrations/tools/azure_cognitive_services/)

  * [Bearly Code Interpreter](https://python.langchain.com/docs/integrations/tools/bearly/)

  * [ChatGPT Plugins](https://python.langchain.com/docs/integrations/tools/chatgpt_plugins/)

  * [ClearML](https://python.langchain.com/docs/integrations/providers/clearml_tracking/)

  * [ClickUp Toolkit](https://python.langchain.com/docs/integrations/tools/clickup/)

  * [Comet Tracing](https://python.langchain.com/docs/integrations/callbacks/comet_tracing/)

  * [Connery Toolkit](https://python.langchain.com/docs/integrations/tools/connery_toolkit/)

  * [Connery Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/connery/)

  * [E2B Data Analysis](https://python.langchain.com/docs/integrations/tools/e2b_data_analysis/)

  * [Eden AI](https://python.langchain.com/docs/integrations/tools/edenai_tools/)

  * [Eleven Labs Text2Speech](https://python.langchain.com/docs/integrations/tools/eleven_labs_tts/)

  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)

  * [Gitlab Toolkit](https://python.langchain.com/docs/integrations/tools/gitlab/)

  * [Google Drive](https://python.langchain.com/docs/integrations/tools/google_drive/)

  * [Google Finance](https://python.langchain.com/docs/integrations/tools/google_finance/)

  * [Google Jobs](https://python.langchain.com/docs/integrations/tools/google_jobs/)

  * [Google Serper](https://python.langchain.com/docs/integrations/tools/google_serper/)

  * [GraphQL](https://python.langchain.com/docs/integrations/tools/graphql/)

  * [Human as a tool](https://python.langchain.com/docs/integrations/tools/human_tools/)

  * [Jira Toolkit](https://python.langchain.com/docs/integrations/tools/jira/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [MLflow](https://python.langchain.com/docs/integrations/providers/mlflow_tracking/)

  * [Memorize](https://python.langchain.com/docs/integrations/tools/memorize/)

  * [NASA Toolkit](https://python.langchain.com/docs/integrations/tools/nasa/)

  * [Natural Language API Toolkits](https://python.langchain.com/docs/integrations/tools/openapi_nla/)

  * [Office365 Toolkit](https://python.langchain.com/docs/integrations/tools/office365/)

  * [OpenWeatherMap](https://python.langchain.com/docs/integrations/tools/openweathermap/)

  * [Pandas Dataframe](https://python.langchain.com/docs/integrations/tools/pandas/)

  * [PlayWright Browser Toolkit](https://python.langchain.com/docs/integrations/tools/playwright/)

  * [SearchApi](https://python.langchain.com/docs/integrations/providers/searchapi/)

  * [Serper - Google Search API](https://python.langchain.com/docs/integrations/providers/google_serper/)

  * [Shell \(bash\)](https://python.langchain.com/docs/integrations/tools/bash/)

  * [Steam Toolkit](https://python.langchain.com/docs/integrations/tools/steam/)

  * [WandB Tracing](https://python.langchain.com/docs/integrations/providers/wandb_tracing/)

  * [Weights & Biases](https://python.langchain.com/docs/integrations/providers/wandb_tracking/)

  * [Xata](https://python.langchain.com/docs/integrations/memory/xata_chat_message_history/)

  * [Yahoo Finance News](https://python.langchain.com/docs/integrations/tools/yahoo_finance_news/)

  * [Zapier Natural Language Actions](https://python.langchain.com/docs/integrations/tools/zapier/)

  * [Zep Cloud Memory](https://python.langchain.com/docs/integrations/memory/zep_memory_cloud/)

  * [Zep Open Source Memory](https://python.langchain.com/docs/integrations/memory/zep_memory/)

__On this page