# AIMessage — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessage.html
**Word Count:** 412
**Links Count:** 215
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# AIMessage\#

_class _langchain\_core.messages.ai.AIMessage[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#AIMessage)\#     

Bases: [`BaseMessage`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.base.BaseMessage.html#langchain_core.messages.base.BaseMessage "langchain_core.messages.base.BaseMessage")

Message from an AI.

AIMessage is returned from a chat model as a response to a prompt.

This message represents the output of the model and consists of both the raw output as returned by the model together standardized fields \(e.g., tool calls, usage metadata\) added by the LangChain framework.

Pass in content as positional arg.

Parameters:     

  * **content** – The content of the message.

  * **kwargs** – Additional arguments to pass to the parent class.

_param _additional\_kwargs _: dict_ _\[Optional\]_\#     

Reserved for additional payload data associated with the message.

For example, for a message from an AI, this could include tool calls as encoded by the model provider.

_param _content _: str | list\[str | dict\]__\[Required\]_\#     

The string contents of the message.

_param _example _: bool_ _ = False_\#     

Use to denote that a message is part of an example conversation.

At the moment, this is ignored by most models. Usage is discouraged.

_param _id _: str | None_ _ = None_\#     

An optional unique identifier for the message. This should ideally be provided by the provider/model which created the message.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _invalid\_tool\_calls _: list\[[InvalidToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.InvalidToolCall.html#langchain_core.messages.tool.InvalidToolCall "langchain_core.messages.tool.InvalidToolCall")\]__ = \[\]_\#     

If provided, tool calls with parsing errors associated with the message.

_param _name _: str | None_ _ = None_\#     

An optional name for the message.

This can be used to provide a human-readable name for the message.

Usage of this field is optional, and whether it’s used or not is up to the model implementation.

_param _response\_metadata _: dict_ _\[Optional\]_\#     

Response metadata. For example: response headers, logprobs, token counts, model name.

_param _tool\_calls _: list\[[ToolCall](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.tool.ToolCall.html#langchain_core.messages.tool.ToolCall "langchain_core.messages.tool.ToolCall")\]__ = \[\]_\#     

If provided, tool calls associated with the message.

_param _type _: Literal\['ai'\]__ = 'ai'_\#     

The type of the message \(used for deserialization\). Defaults to “ai”.

_param _usage\_metadata _: [UsageMetadata](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.UsageMetadata.html#langchain_core.messages.ai.UsageMetadata "langchain_core.messages.ai.UsageMetadata") | None_ _ = None_\#     

If provided, usage metadata for a message, such as token counts.

This is a standard representation of token usage that is consistent across models.

pretty\_print\(\) → None\#     

Print a pretty representation of the message.

Return type:     

None

pretty\_repr\(_html : bool = False_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/messages/ai.html#AIMessage.pretty_repr)\#     

Return a pretty representation of the message.

Parameters:     

**html** \(_bool_\) – Whether to return an HTML-formatted string. Defaults to False.

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

Examples using AIMessage

  * [Build a Chatbot](https://python.langchain.com/docs/tutorials/chatbot/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Chat Bot Feedback Template](https://python.langchain.com/docs/templates/chat-bot-feedback/)

  * [ChatGLM](https://python.langchain.com/docs/integrations/llms/chatglm/)

  * [ChatOCIGenAI](https://python.langchain.com/docs/integrations/chat/oci_generative_ai/)

  * [ChatOllama](https://python.langchain.com/docs/integrations/chat/ollama/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Google Cloud Vertex AI](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm/)

  * [Google Imagen](https://python.langchain.com/docs/integrations/tools/google_imagen/)

  * [How to add a human-in-the-loop for tools](https://python.langchain.com/docs/how_to/tools_human/)

  * [How to add a semantic layer over graph database](https://python.langchain.com/docs/how_to/graph_semantic/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add examples to the prompt for query analysis](https://python.langchain.com/docs/how_to/query_few_shot/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to add tools to chatbots](https://python.langchain.com/docs/how_to/chatbots_tools/)

  * [How to compose prompts together](https://python.langchain.com/docs/how_to/prompts_composition/)

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

  * [How to do tool/function calling](https://python.langchain.com/docs/how_to/function_calling/)

  * [How to filter messages](https://python.langchain.com/docs/how_to/filter_messages/)

  * [How to handle tool errors](https://python.langchain.com/docs/how_to/tools_error/)

  * [How to merge consecutive messages of the same type](https://python.langchain.com/docs/how_to/merge_message_runs/)

  * [How to return structured data from a model](https://python.langchain.com/docs/how_to/structured_output/)

  * [How to trim messages](https://python.langchain.com/docs/how_to/trim_messages/)

  * [How to use few-shot prompting with tool calling](https://python.langchain.com/docs/how_to/tools_few_shot/)

  * [How to use prompting alone \(no tool calling\) to do extraction](https://python.langchain.com/docs/how_to/extraction_parse/)

  * [How to use reference examples when doing extraction](https://python.langchain.com/docs/how_to/extraction_examples/)

  * [Twitter \(via Apify\)](https://python.langchain.com/docs/integrations/chat_loaders/twitter/)

  * [Yuan2.0](https://python.langchain.com/docs/integrations/chat/yuan2/)

  * [ZHIPU AI](https://python.langchain.com/docs/integrations/chat/zhipuai/)

  * [Zep Cloud](https://python.langchain.com/docs/integrations/retrievers/zep_cloud_memorystore/)

  * [Zep Cloud Memory](https://python.langchain.com/docs/integrations/memory/zep_memory_cloud/)

  * [Zep Open Source](https://python.langchain.com/docs/integrations/retrievers/zep_memorystore/)

  * [Zep Open Source Memory](https://python.langchain.com/docs/integrations/memory/zep_memory/)

  * [ZepCloudChatMessageHistory](https://python.langchain.com/docs/integrations/memory/zep_cloud_chat_message_history/)

__On this page