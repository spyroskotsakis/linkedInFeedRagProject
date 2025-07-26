# SystemMessage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.system.SystemMessage.html
**Word Count:** 308
**Links Count:** 215
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# SystemMessage\#

_class _langchain\_core.messages.system.SystemMessage[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/system.html#SystemMessage)\#     

Bases: [`BaseMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

Message for priming AI behavior.

The system message is usually passed in as the first of a sequence of input messages.

Example               from langchain_core.messages import HumanMessage, SystemMessage          messages = [         SystemMessage(             content="You are a helpful assistant! Your name is Bob."         ),         HumanMessage(             content="What is your name?"         )     ]          # Define a chat model and invoke it with the messages     print(model.invoke(messages))     

Pass in content as positional arg.

Parameters:     

  * **content** – The string contents of the message.

  * **kwargs** – Additional fields to pass to the message.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Reserved for additional payload data associated with the message.

For example, for a message from an AI, this could include tool calls as encoded by the model provider.

_param _content _: str | list\[str | dict\]__\[Required\]_\#     

The string contents of the message.

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

_param _type _: Literal\['system'\]__ = 'system'_\#     

The type of the message \(used for serialization\). Defaults to “system”.

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

Examples using SystemMessage

  * [\# Related](https://python.langchain.com/docs/integrations/chat/solar/)

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)

  * [Build a Question/Answering system over SQL data](https://python.langchain.com/docs/tutorials/sql_qa/)

  * [Build a Simple LLM Application with LCEL](https://python.langchain.com/docs/tutorials/llm_chain/)

  * [ChatAnyscale](https://python.langchain.com/docs/integrations/chat/anyscale/)

  * [ChatEverlyAI](https://python.langchain.com/docs/integrations/chat/everlyai/)

  * [ChatFriendli](https://python.langchain.com/docs/integrations/chat/friendli/)

  * [ChatHuggingFace](https://python.langchain.com/docs/integrations/chat/huggingface/)

  * [ChatKonko](https://python.langchain.com/docs/integrations/chat/konko/)

  * [ChatOCIGenAI](https://python.langchain.com/docs/integrations/chat/oci_generative_ai/)

  * [ChatOctoAI](https://python.langchain.com/docs/integrations/chat/octoai/)

  * [ChatPremAI](https://python.langchain.com/docs/integrations/chat/premai/)

  * [ChatTongyi](https://python.langchain.com/docs/integrations/chat/tongyi/)

  * [ChatWatsonx](https://python.langchain.com/docs/integrations/chat/ibm_watsonx/)

  * [ChatYI](https://python.langchain.com/docs/integrations/chat/yi/)

  * [ChatYandexGPT](https://python.langchain.com/docs/integrations/chat/yandex/)

  * [Context](https://python.langchain.com/docs/integrations/callbacks/context/)

  * [Exa Search](https://python.langchain.com/docs/integrations/tools/exa_search/)

  * [GigaChat](https://python.langchain.com/docs/integrations/chat/gigachat/)

  * [Google Cloud Vertex AI](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to compose prompts together](https://python.langchain.com/docs/how_to/prompts_composition/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)

  * [How to merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)

  * [How to migrate from legacy LangChain agents to LangGraph](https://python.langchain.com/docs/how_to/migrate_agent/)

  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [Javelin AI Gateway](https://python.langchain.com/docs/integrations/providers/javelin_ai_gateway/)

  * [Javelin AI Gateway Tutorial](https://python.langchain.com/docs/integrations/llms/javelin/)

  * [JinaChat](https://python.langchain.com/docs/integrations/chat/jinachat/)

  * [LLMonitor](https://python.langchain.com/docs/integrations/callbacks/llmonitor/)

  * [Label Studio](https://python.langchain.com/docs/integrations/callbacks/labelstudio/)

  * [Llama2Chat](https://python.langchain.com/docs/integrations/chat/llama2_chat/)

  * [LlamaEdge](https://python.langchain.com/docs/integrations/chat/llama_edge/)

  * [MLflow AI Gateway](https://python.langchain.com/docs/integrations/providers/mlflow_ai_gateway/)

  * [MLflow Deployments for LLMs](https://python.langchain.com/docs/integrations/providers/mlflow/)

  * [MoonshotChat](https://python.langchain.com/docs/integrations/chat/moonshot/)

  * [PremAI](https://python.langchain.com/docs/integrations/providers/premai/)

  * [Robocorp Toolkit](https://python.langchain.com/docs/integrations/tools/robocorp/)

  * [Snowflake Cortex](https://python.langchain.com/docs/integrations/chat/snowflake/)

  * [Trubrics](https://python.langchain.com/docs/integrations/callbacks/trubrics/)

  * [Yuan2.0](https://python.langchain.com/docs/integrations/chat/yuan2/)

  * [ZHIPU AI](https://python.langchain.com/docs/integrations/chat/zhipuai/)

  * [vLLM Chat](https://python.langchain.com/docs/integrations/chat/vllm/)

  * [🦜️🏓 LangServe](https://python.langchain.com/docs/langserve/)

__On this page