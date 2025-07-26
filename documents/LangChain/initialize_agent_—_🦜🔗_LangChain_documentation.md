# initialize_agent — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/agents/langchain.agents.initialize.initialize_agent.html
**Word Count:** 260
**Links Count:** 221
**Scraped:** 2025-07-21 07:48:06
**Status:** completed

---

# initialize\_agent\#

langchain.agents.initialize.initialize\_agent\(

    _tools : Sequence\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _agent : [AgentType](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") | None = None_,     _callback\_manager : [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _agent\_path : str | None = None_,     _agent\_kwargs : dict | None = None_,     _\*_ ,     _tags : Sequence\[str\] | None = None_,     _\*\* kwargs: Any_, \) → [AgentExecutor](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/agents/initialize.html#initialize_agent)\#     

Deprecated since version 0.1.0: LangChain agents will continue to be supported, but it is recommended for new use cases to be built with LangGraph. LangGraph offers a more flexible and full-featured framework for building agents, including support for tool-calling, persistence of state, and human-in-the-loop workflows. For details, refer to the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) as well as guides for [Migrating from AgentExecutor](https://python.langchain.com/docs/how_to/migrate_agent/) and LangGraph’s [Pre-built ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/). It will not be removed until langchain==1.0.

Load an agent executor given tools and LLM.

Parameters:     

  * **tools** \(_Sequence_ _\[_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\) – List of tools this agent has access to.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – Language model to use as the agent.

  * **agent** \([_AgentType_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent_types.AgentType.html#langchain.agents.agent_types.AgentType "langchain.agents.agent_types.AgentType") _|__None_\) – Agent type to use. If None and agent\_path is also None, will default to AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION. Defaults to None.

  * **callback\_manager** \([_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – CallbackManager to use. Global callback manager is used if not provided. Defaults to None.

  * **agent\_path** \(_str_ _|__None_\) – Path to serialized agent to use. If None and agent is also None, will default to AgentType.ZERO\_SHOT\_REACT\_DESCRIPTION. Defaults to None.

  * **agent\_kwargs** \(_dict_ _|__None_\) – Additional keyword arguments to pass to the underlying agent. Defaults to None.

  * **tags** \(_Sequence_ _\[__str_ _\]__|__None_\) – Tags to apply to the traced runs. Defaults to None.

  * **kwargs** \(_Any_\) – Additional keyword arguments passed to the agent executor.

Returns:     

An agent executor.

Raises:     

  * **ValueError** – If both agent and agent\_path are specified.

  * **ValueError** – If agent is not a valid agent type.

  * **ValueError** – If both agent and agent\_path are None.

Return type:     

[_AgentExecutor_](https://python.langchain.com/api_reference/langchain/agents/langchain.agents.agent.AgentExecutor.html#langchain.agents.agent.AgentExecutor "langchain.agents.agent.AgentExecutor")

Examples using initialize\_agent

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

  * [Comet](https://python.langchain.com/docs/integrations/providers/comet_tracking/)

  * [Comet Tracing](https://python.langchain.com/docs/integrations/callbacks/comet_tracing/)

  * [Connery Toolkit](https://python.langchain.com/docs/integrations/tools/connery_toolkit/)

  * [Connery Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/connery/)

  * [Dall-E Image Generator](https://python.langchain.com/docs/integrations/tools/dalle_image_generator/)

  * [E2B Data Analysis](https://python.langchain.com/docs/integrations/tools/e2b_data_analysis/)

  * [Eden AI](https://python.langchain.com/docs/integrations/tools/edenai_tools/)

  * [Eleven Labs Text2Speech](https://python.langchain.com/docs/integrations/tools/eleven_labs_tts/)

  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)

  * [Gitlab Toolkit](https://python.langchain.com/docs/integrations/tools/gitlab/)

  * [Google Drive](https://python.langchain.com/docs/integrations/tools/google_drive/)

  * [Google Finance](https://python.langchain.com/docs/integrations/tools/google_finance/)

  * [Google Jobs](https://python.langchain.com/docs/integrations/tools/google_jobs/)

  * [Google Serper](https://python.langchain.com/docs/integrations/tools/google_serper/)

  * [Gradio](https://python.langchain.com/docs/integrations/tools/gradio_tools/)

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

  * [PlayWright Browser Toolkit](https://python.langchain.com/docs/integrations/tools/playwright/)

  * [SageMaker Tracking](https://python.langchain.com/docs/integrations/callbacks/sagemaker_tracking/)

  * [SceneXplain](https://python.langchain.com/docs/integrations/tools/sceneXplain/)

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)