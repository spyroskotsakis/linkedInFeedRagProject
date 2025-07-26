# load_tools — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.load_tools.load_tools.html
**Word Count:** 281
**Links Count:** 207
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# load\_tools\#

langchain\_community.agent\_toolkits.load\_tools.load\_tools\(

    _tool\_names : List\[str\]_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_,     _allow\_dangerous\_tools : bool = False_,     _\*\* kwargs: Any_, \) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/load_tools.html#load_tools)\#     

Load tools based on their name.

Tools allow agents to interact with various resources and services like APIs, databases, file systems, etc.

Please scope the permissions of each tools to the minimum required for the application.

For example, if an application only needs to read from a database, the database tool should not be given write permissions. Moreover consider scoping the permissions to only allow accessing specific tables and impose user-level quota for limiting resource usage.

Please read the APIs of the individual tools to determine which configuration they support.

See \[Security\]\(<https://python.langchain.com/docs/security>\) for more information.

Parameters:     

  * **tool\_names** \(_List_ _\[__str_ _\]_\) – name of tools to load.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_\) – An optional language model may be needed to initialize certain tools. Defaults to None.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Optional callback manager or list of callback handlers. If not provided, default global callback manager will be used.

  * **allow\_dangerous\_tools** \(_bool_\) – Optional flag to allow dangerous tools. Tools that contain some level of risk. Please use with caution and read the documentation of these tools to understand the risks and how to mitigate them. Refer to <https://python.langchain.com/docs/security> for more information. Please note that this list may not be fully exhaustive. It is your responsibility to understand which tools you’re using and the risks associated with them. Defaults to False.

  * **kwargs** \(_Any_\) – Additional keyword arguments.

Returns:     

List of tools.

Raises:     

  * **ValueError** – If the tool name is unknown.

  * **ValueError** – If the tool requires an LLM to be provided.

  * **ValueError** – If the tool requires some parameters that were not provided.

  * **ValueError** – If the tool is a dangerous tool and allow\_dangerous\_tools is False.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using load\_tools

  * [AWS Lambda](https://python.langchain.com/docs/integrations/tools/awslambda/)

  * [Aim](https://python.langchain.com/docs/integrations/providers/aim_tracking/)

  * [Amazon API Gateway](https://python.langchain.com/docs/integrations/llms/amazon_api_gateway/)

  * [ArXiv](https://python.langchain.com/docs/integrations/tools/arxiv/)

  * [Argilla](https://python.langchain.com/docs/integrations/callbacks/argilla/)

  * [ChatGPT Plugins](https://python.langchain.com/docs/integrations/tools/chatgpt_plugins/)

  * [ClearML](https://python.langchain.com/docs/integrations/providers/clearml_tracking/)

  * [Comet](https://python.langchain.com/docs/integrations/providers/comet_tracking/)

  * [Comet Tracing](https://python.langchain.com/docs/integrations/callbacks/comet_tracing/)

  * [Dall-E Image Generator](https://python.langchain.com/docs/integrations/tools/dalle_image_generator/)

  * [DataForSEO](https://python.langchain.com/docs/integrations/providers/dataforseo/)

  * [Dataherald](https://python.langchain.com/docs/integrations/providers/dataherald/)

  * [Eleven Labs Text2Speech](https://python.langchain.com/docs/integrations/tools/eleven_labs_tts/)

  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)

  * [Golden](https://python.langchain.com/docs/integrations/providers/golden/)

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [Google Drive](https://python.langchain.com/docs/integrations/tools/google_drive/)

  * [Google Finance](https://python.langchain.com/docs/integrations/tools/google_finance/)

  * [Google Jobs](https://python.langchain.com/docs/integrations/tools/google_jobs/)

  * [GraphQL](https://python.langchain.com/docs/integrations/tools/graphql/)

  * [How to track token usage in ChatModels](https://python.langchain.com/docs/how_to/chat_token_usage_tracking/)

  * [Human as a tool](https://python.langchain.com/docs/integrations/tools/human_tools/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [MLX](https://python.langchain.com/docs/integrations/chat/mlx/)

  * [MLflow](https://python.langchain.com/docs/integrations/providers/mlflow_tracking/)

  * [Memorize](https://python.langchain.com/docs/integrations/tools/memorize/)

  * [OpenWeatherMap](https://python.langchain.com/docs/integrations/providers/openweathermap/)

  * [SageMaker Tracking](https://python.langchain.com/docs/integrations/callbacks/sagemaker_tracking/)

  * [SceneXplain](https://python.langchain.com/docs/integrations/tools/sceneXplain/)

  * [SearchApi](https://python.langchain.com/docs/integrations/providers/searchapi/)

  * [SearxNG Search API](https://python.langchain.com/docs/integrations/providers/searx/)

  * [SerpAPI](https://python.langchain.com/docs/integrations/providers/serpapi/)

  * [Serper - Google Search API](https://python.langchain.com/docs/integrations/providers/google_serper/)

  * [Stack Exchange](https://python.langchain.com/docs/integrations/providers/stackexchange/)

  * [Streamlit](https://python.langchain.com/docs/integrations/callbacks/streamlit/)

  * [WandB Tracing](https://python.langchain.com/docs/integrations/providers/wandb_tracing/)

  * [Weights & Biases](https://python.langchain.com/docs/integrations/providers/wandb_tracking/)

  * [Wolfram Alpha](https://python.langchain.com/docs/integrations/providers/wolfram_alpha/)

__On this page