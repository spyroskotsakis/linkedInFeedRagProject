# HumanMessage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.human.HumanMessage.html
**Word Count:** 427
**Links Count:** 268
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# HumanMessage\#

_class _langchain\_core.messages.human.HumanMessage[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/human.html#HumanMessage)\#     

Bases: [`BaseMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

Message from a human.

HumanMessages are messages that are passed in from a human to the model.

Example               from langchain_core.messages import HumanMessage, SystemMessage          messages = [         SystemMessage(             content="You are a helpful assistant! Your name is Bob."         ),         HumanMessage(             content="What is your name?"         )     ]          # Instantiate a chat model and invoke it with the messages     model = ...     print(model.invoke(messages))     

Pass in content as positional arg.

Parameters:     

  * **content** – The string contents of the message.

  * **kwargs** – Additional fields to pass to the message.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Reserved for additional payload data associated with the message.

For example, for a message from an AI, this could include tool calls as encoded by the model provider.

_param _content _: str | list\[str | dict\]__\[Required\]_\#     

The string contents of the message.

_param _example _: bool_ _ = False_\#     

Use to denote that a message is part of an example conversation.

At the moment, this is ignored by most models. Usage is discouraged. Defaults to False.

_param _id _: str | None_ _ = None_\#     

An optional unique identifier for the message. This should ideally be provided by the provider/model which created the message.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _name _: str | None_ _ = None_\#     

An optional name for the message.

This can be used to provide a human-readable name for the message.

Usage of this field is optional, and whether it’s used or not is up to the model implementation.

_param _response\_metadata _: dict_ _\[Optional\]_\#     

Response metadata. For example: response headers, logprobs, token counts, model name.

_param _type _: Literal\['human'\]__ = 'human'_\#     

The type of the message \(used for serialization\). Defaults to “human”.

pretty\_print\(\) → None\#     

Print a pretty representation of the message.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str\#     

Get a pretty representation of the message.

Parameters:     

**html** \(_bool_\) – Whether to format the message as HTML. If True, the message will be formatted with HTML tags. Default is False.

Returns:     

A pretty representation of the message.

Return type:     

str

text\(\) → str\#     

Get the text content of the message.

Returns:     

The text content of the message.

Return type:     

str

Examples using HumanMessage

  * [\# Related](https://python.langchain.com/docs/integrations/chat/solar/)

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Alibaba Cloud PAI EAS](https://python.langchain.com/docs/integrations/chat/alibaba_cloud_pai_eas/)

  * [Arthur](https://python.langchain.com/docs/integrations/providers/arthur_tracking/)

  * [Azure ML](https://python.langchain.com/docs/integrations/llms/azure_ml/)

  * [AzureMLChatOnlineEndpoint](https://python.langchain.com/docs/integrations/chat/azureml_chat_endpoint/)

  * [Browserbase](https://python.langchain.com/docs/integrations/document_loaders/browserbase/)

  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [Build a Simple LLM Application with LCEL](https://python.langchain.com/docs/tutorials/llm_chain/)

  * [Build an Agent](https://python.langchain.com/docs/tutorials/agents/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Chat Bot Feedback Template](https://python.langchain.com/docs/templates/chat-bot-feedback/)

  * [Chat with Baichuan-192K](https://python.langchain.com/docs/integrations/chat/baichuan/)

  * [Chat with Coze Bot](https://python.langchain.com/docs/integrations/chat/coze/)

  * [ChatAnyscale](https://python.langchain.com/docs/integrations/chat/anyscale/)

  * [ChatEverlyAI](https://python.langchain.com/docs/integrations/chat/everlyai/)

  * [ChatFriendli](https://python.langchain.com/docs/integrations/chat/friendli/)

  * [ChatHuggingFace](https://python.langchain.com/docs/integrations/chat/huggingface/)

  * [ChatKonko](https://python.langchain.com/docs/integrations/chat/konko/)

  * [ChatLiteLLM](https://python.langchain.com/docs/integrations/chat/litellm/)

  * [ChatLiteLLMRouter](https://python.langchain.com/docs/integrations/chat/litellm_router/)

  * [ChatNVIDIA](https://python.langchain.com/docs/integrations/chat/nvidia_ai_endpoints/)

  * [ChatOCIGenAI](https://python.langchain.com/docs/integrations/chat/oci_generative_ai/)

  * [ChatOctoAI](https://python.langchain.com/docs/integrations/chat/octoai/)

  * [ChatOllama](https://python.langchain.com/docs/integrations/chat/ollama/)

  * [ChatPremAI](https://python.langchain.com/docs/integrations/chat/premai/)

  * [ChatTongyi](https://python.langchain.com/docs/integrations/chat/tongyi/)

  * [ChatWatsonx](https://python.langchain.com/docs/integrations/chat/ibm_watsonx/)

  * [ChatYI](https://python.langchain.com/docs/integrations/chat/yi/)

  * [ChatYandexGPT](https://python.langchain.com/docs/integrations/chat/yandex/)

  * [Cohere](https://python.langchain.com/docs/integrations/llms/cohere/)

  * [Conceptual guide](https://python.langchain.com/docs/concepts/)

  * [Context](https://python.langchain.com/docs/integrations/callbacks/context/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Dappier AI](https://python.langchain.com/docs/integrations/chat/dappier/)

  * [DeepInfra](https://python.langchain.com/docs/integrations/chat/deepinfra/)

  * [Discord](https://python.langchain.com/docs/integrations/chat_loaders/discord/)

  * [Eden AI](https://python.langchain.com/docs/integrations/chat/edenai/)

  * [ErnieBotChat](https://python.langchain.com/docs/integrations/chat/ernie/)

  * [Flyte](https://python.langchain.com/docs/integrations/providers/flyte/)

  * [GPTRouter](https://python.langchain.com/docs/integrations/chat/gpt_router/)

  * [GigaChat](https://python.langchain.com/docs/integrations/chat/gigachat/)

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [Google Cloud Vertex AI](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm/)

  * [Google Imagen](https://python.langchain.com/docs/integrations/tools/google_imagen/)

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to add tools to chatbots](https://python.langchain.com/docs/how_to/chatbots_tools/)

  * [How to compose prompts together](https://python.langchain.com/docs/how_to/prompts_composition/)

  * [How to convert tools to OpenAI Functions](https://python.langchain.com/docs/how_to/tools_as_openai_functions/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

  * [How to do tool/function calling](https://python.langchain.com/docs/how_to/function_calling/)

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

  * [How to merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)

  * [How to pass multimodal data directly to models](https://python.langchain.com/docs/how_to/multimodal_inputs/)

  * [How to pass tool outputs to chat models](https://python.langchain.com/docs/how_to/tool_results_pass_to_model/)

  * [How to return structured data from a model](https://python.langchain.com/docs/how_to/structured_output/)

  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

  * [How to use callbacks in async environments](https://python.langchain.com/docs/how_to/callbacks_async/)

  * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [Javelin AI Gateway](https://python.langchain.com/docs/integrations/providers/javelin_ai_gateway/)

  * [Javelin AI Gateway Tutorial](https://python.langchain.com/docs/integrations/llms/javelin/)

  * [JinaChat](https://python.langchain.com/docs/integrations/chat/jinachat/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [Label Studio](https://python.langchain.com/docs/integrations/callbacks/labelstudio/)

  * [LlamaEdge](https://python.langchain.com/docs/integrations/chat/llama_edge/)

  * [Log10](https://python.langchain.com/docs/integrations/providers/log10/)

  * [MLX](https://python.langchain.com/docs/integrations/chat/mlx/)

  * [MLflow AI Gateway](https://python.langchain.com/docs/integrations/providers/mlflow_ai_gateway/)

  * [MLflow Deployments for LLMs](https://python.langchain.com/docs/integrations/providers/mlflow/)

  * [Maritalk](https://python.langchain.com/docs/integrations/chat/maritalk/)

  * [MiniMaxChat](https://python.langchain.com/docs/integrations/chat/minimax/)

  * [MoonshotChat](https://python.langchain.com/docs/integrations/chat/moonshot/)

  * [PremAI](https://python.langchain.com/docs/integrations/providers/premai/)

  * [PromptLayer](https://python.langchain.com/docs/integrations/callbacks/promptlayer/)

  * [PromptLayerChatOpenAI](https://python.langchain.com/docs/integrations/chat/promptlayer_chatopenai/)

  * [QianfanChatEndpoint](https://python.langchain.com/docs/integrations/chat/baidu_qianfan_endpoint/)

  * [Snowflake Cortex](https://python.langchain.com/docs/integrations/chat/snowflake/)

  * [SparkLLM Chat](https://python.langchain.com/docs/integrations/chat/sparkllm/)

  * [Tencent Hunyuan](https://python.langchain.com/docs/integrations/chat/tencent_hunyuan/)

  * [Trubrics](https://python.langchain.com/docs/integrations/callbacks/trubrics/)

  * [VolcEngineMaasChat](https://python.langchain.com/docs/integrations/chat/volcengine_maas/)

  * [WeChat](https://python.langchain.com/docs/integrations/chat_loaders/wechat/)

  * [Yuan2.0](https://python.langchain.com/docs/integrations/chat/yuan2/)

  * [ZHIPU AI](https://python.langchain.com/docs/integrations/chat/zhipuai/)

  * [Zep Cloud](https://python.langchain.com/docs/integrations/retrievers/zep_cloud_memorystore/)

  * [Zep Cloud Memory](https://python.langchain.com/docs/integrations/memory/zep_memory_cloud/)

  * [Zep Open Source](https://python.langchain.com/docs/integrations/retrievers/zep_memorystore/)

  * [Zep Open Source Memory](https://python.langchain.com/docs/integrations/memory/zep_memory/)

  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)

  * [vLLM Chat](https://python.langchain.com/docs/integrations/chat/vllm/)

  * [🦜️🏓 LangServe](https://python.langchain.com/docs/langserve/)

__On this page